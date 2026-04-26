#!/usr/bin/env python3
"""
Daily arxiv quant-ph + selected cond-mat digest -> Markdown.

Fetches recent papers, downloads each PDF to a temporary directory, extracts
full PDF text for analysis with a local Ollama model, extracts a lightweight figure gallery with captions
when possible, writes a dated Markdown digest, and automatically deletes PDFs
when the run finishes.

Requirements:
    pip install arxiv ollama PyMuPDF

Prerequisites:
    - Ollama installed and running (`ollama serve` if not auto-started)
    - A model pulled, e.g. `ollama pull gemma3:4b`

Env vars, optional:
    OLLAMA_HOST              default http://localhost:11434
    OLLAMA_MODEL             default gemma4:26b
    ARXIV_LOOKBACK_HOURS     override weekday-aware lookback
    OLLAMA_NUM_CTX           default 8192
    OLLAMA_NUM_PREDICT       default 2000
"""

import json
import os
import re
import tempfile
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

import arxiv
import fitz  # PyMuPDF
import ollama


# ---------- config ----------
MODEL = os.environ.get("OLLAMA_MODEL", "gemma4:26b")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OUTPUT_DIR = Path("/Users/oksanachelpanova/Dropbox/arxiv/output")
FETCH_LIMIT = int(os.environ.get("ARXIV_FETCH_LIMIT", "400"))
MAX_PAPERS_TO_PROCESS = os.environ.get("MAX_PAPERS_TO_PROCESS")
MAX_PAPERS_TO_PROCESS = int(MAX_PAPERS_TO_PROCESS) if MAX_PAPERS_TO_PROCESS else None

# Be polite to arXiv API and avoid HTTP 429.
ARXIV_PAGE_SIZE = int(os.environ.get("ARXIV_PAGE_SIZE", "50"))
ARXIV_DELAY_SECONDS = float(os.environ.get("ARXIV_DELAY_SECONDS", "4.0"))
ARXIV_NUM_RETRIES = int(os.environ.get("ARXIV_NUM_RETRIES", "8"))

NUM_CTX = int(os.environ.get("OLLAMA_NUM_CTX", "8192"))
NUM_PREDICT = int(os.environ.get("OLLAMA_NUM_PREDICT", "3000"))

# Full-paper analysis can be expensive. These settings keep it practical.
CHUNK_CHARS = 12000
CHUNK_OVERLAP = 1200
MAX_CHUNKS_PER_PAPER = 8

# Figure gallery settings.
# Conservative defaults keep the output folder small.
MAX_FIGURES_PER_PAPER = int(os.environ.get("MAX_FIGURES_PER_PAPER", "10"))
FIGURE_RENDER_ZOOM = float(os.environ.get("FIGURE_RENDER_ZOOM", "1.25"))
FIGURE_JPEG_QUALITY = int(os.environ.get("FIGURE_JPEG_QUALITY", "65"))
FIGURE_MIN_AREA = int(os.environ.get("FIGURE_MIN_AREA", "40000"))

# Search each archive separately instead of using one long OR query.
# This reproduces the behavior of your older quant-ph-only script more reliably
# and avoids losing entries because of API query parsing or max_results ordering.
ARXIV_QUERIES = [
    ("quant-ph", "cat:quant-ph"),
    ("cond-mat.quant-gas", "cat:cond-mat.quant-gas"),
    ("cond-mat.stat-mech", "cat:cond-mat.stat-mech"),
    ("cond-mat.str-el", "cat:cond-mat.str-el"),
    ("cond-mat.dis-nn", "cat:cond-mat.dis-nn"),
]

CATEGORIES = [
    "quantum information and computing",
    "AMO physics",
    "numerical methods",
    "quantum gases",
    "statistical mechanics",
    "strongly correlated electrons",
    "disordered systems and neural networks",
    "other",
]

# Highlight authors are loaded from an external text file so the same list
# can be reused across multiple versions of the script. Default location
# is `highlight_authors.txt` next to this script; override with
# HIGHLIGHT_AUTHORS_FILE env var if you keep it elsewhere.
HIGHLIGHT_AUTHORS_FILE = Path(
    os.environ.get(
        "HIGHLIGHT_AUTHORS_FILE",
        Path(__file__).resolve().parent / "highlight_authors.txt",
    )
)


def _load_highlight_authors(path):
    """Read author names from a text file. Lines starting with '#' or blank
    lines are ignored. Returns the list, possibly empty."""
    if not path.exists():
        print(f"warn: highlight authors file not found at {path}; nobody will be highlighted.")
        return []
    names = []
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            names.append(line)
    return names


HIGHLIGHT_AUTHORS = _load_highlight_authors(HIGHLIGHT_AUTHORS_FILE)


# Topics of personal research interest. Each topic is keyed by a short label
# (used in headings and JSON) and has a one-sentence description that the LLM
# uses to score relevance from 0 to 5. Edit, add, or remove freely.
#   0 = unrelated
#   1 = mentions topic in passing
#   2 = uses related techniques but not focused on it
#   3 = relevant; topic is one of several themes
#   4 = directly studies this topic; main focus
#   5 = breakthrough/landmark result on exactly this topic
TOPICS = {
    "Rydberg arrays":
        "Experiments or theory using arrays of Rydberg atoms (tweezer arrays, "
        "programmable quantum simulators, blockade-mediated entanglement).",
    "free-space correlated emission":
        "Cooperative or correlated photon emission from atoms in free space "
        "(Dicke superradiance, subradiance, free-space cooperativity).",
    "Frenkel-Kontorova":
        "The Frenkel-Kontorova model and its variants — chains in periodic "
        "potentials, commensurate/incommensurate transitions, friction.",
    "Dicke superradiance":
        "Dicke superradiance, sub/superradiant states, collective spontaneous "
        "emission, cavity-Dicke physics.",
    "interference shaping light":
        "Interference effects (multi-path, structured, quantum) used to shape "
        "the spectral, spatial, or statistical properties of light sources.",
    "kinetically constrained dynamics":
        "Dynamics of kinetically constrained models, including Hilbert-space "
        "fragmentation, scars, slow thermalization from constraints.",
}

# Relevance score >= this threshold makes a paper appear in the
# "Most relevant" top section. 3 means "directly relevant or better".
RELEVANCE_THRESHOLD = 3

client = ollama.Client(host=OLLAMA_HOST)


# ---------- author matching ----------
def _normalize_name(name):
    """Lowercase, strip accents, drop punctuation, collapse initials."""
    import unicodedata

    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace(".", " ").replace(",", " ")
    tokens = [t for t in s.split() if t]

    if len(tokens) <= 1:
        return " ".join(tokens)

    given, surname = tokens[0], tokens[-1]
    middles = [t for t in tokens[1:-1] if len(t) > 1]
    return " ".join([given] + middles + [surname])


_HIGHLIGHT_SET = {_normalize_name(a) for a in HIGHLIGHT_AUTHORS}


def paper_highlight_matches(paper):
    """Return list of highlighted author names that appear on this paper."""
    hits = []
    for author in paper.authors:
        norm = _normalize_name(author.name)

        if norm in _HIGHLIGHT_SET:
            hits.append(author.name)
            continue

        parts = norm.split()
        if len(parts) >= 2:
            first_initial, surname = parts[0][0], parts[-1]
            for h in _HIGHLIGHT_SET:
                hp = h.split()
                if len(hp) >= 2 and hp[-1] == surname and hp[0][0] == first_initial:
                    hits.append(author.name)
                    break

    return hits


# ---------- fetch ----------
def previous_arxiv_workday(day):
    """
    Return the previous arXiv announcement workday.

    arXiv's usual submission cutoff is 14:00 Eastern Time. New papers announced
    for a given workday are those submitted after the previous workday cutoff
    and before the current workday cutoff. Weekends are skipped.
    """
    day = day - timedelta(days=1)
    while day.weekday() >= 5:  # Saturday=5, Sunday=6
        day = day - timedelta(days=1)
    return day


def compute_arxiv_submission_window(now=None):
    """
    Compute the arXiv submission window for the day this script is run on.

    Submission cutoffs are 14:00 US Eastern Time (= 18:00 UTC in EDT,
    19:00 UTC in EST). The window is the (start_day 14:00, end_day 14:00)
    pair we want to fetch papers from.

    Mapping by weekday of the run (per user spec):

        Mon  ->  Thu 14:00 ET  -> Fri 14:00 ET
        Tue  ->  Fri 14:00 ET  -> Mon 14:00 ET
        Wed  ->  Mon 14:00 ET  -> Tue 14:00 ET
        Thu  ->  Tue 14:00 ET  -> Wed 14:00 ET
        Fri  ->  Wed 14:00 ET  -> Thu 14:00 ET
        Sat  ->  Wed 14:00 ET  -> Thu 14:00 ET   (same as Friday)
        Sun  ->  Wed 14:00 ET  -> Thu 14:00 ET   (same as Friday)

    Friday/Saturday/Sunday all see the same Wed->Thu window because the next
    arXiv mailing (announcing Thu->Fri papers) goes out Sunday evening.

    Override with ARXIV_LOOKBACK_HOURS env var (legacy behavior — picks the
    last N hours from now), but the default uses the explicit table above.
    """
    eastern = ZoneInfo("America/New_York")

    if now is None:
        now_et = datetime.now(eastern)
    else:
        now_et = now.astimezone(eastern)

    today = now_et.date()
    cutoff_time = datetime.strptime("14:00", "%H:%M").time()

    # weekday(): Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=5, Sun=6
    # For each run weekday, give (start_offset, end_offset) in days from `today`
    # — both offsets are negative (in the past) and end_offset > start_offset.
    # Numbers are chosen so that, for example:
    #   Mon (today): end_day = Fri = today-3, start_day = Thu = today-4
    #   Tue (today): end_day = Mon = today-1, start_day = Fri = today-4
    weekday_to_offsets = {
        0: (-4, -3),  # Mon: Thu -> Fri
        1: (-4, -1),  # Tue: Fri -> Mon
        2: (-2, -1),  # Wed: Mon -> Tue
        3: (-2, -1),  # Thu: Tue -> Wed
        4: (-2, -1),  # Fri: Wed -> Thu
        5: (-3, -2),  # Sat: Wed -> Thu
        6: (-4, -3),  # Sun: Wed -> Thu
    }

    start_offset, end_offset = weekday_to_offsets[now_et.weekday()]
    start_day = today + timedelta(days=start_offset)
    end_day = today + timedelta(days=end_offset)

    start_et = datetime.combine(start_day, cutoff_time, tzinfo=eastern)
    end_et = datetime.combine(end_day, cutoff_time, tzinfo=eastern)

    return (start_et.astimezone(timezone.utc),
            end_et.astimezone(timezone.utc),
            start_et,
            end_et)


def arxiv_base_id(result):
    """
    Return version-independent arXiv ID.

    Examples:
        http://arxiv.org/abs/2404.12345v2 -> 2404.12345
        http://arxiv.org/abs/quant-ph/0101001v1 -> quant-ph/0101001
    """
    arxiv_id = result.entry_id.rsplit("/", 1)[-1]
    return re.sub(r"v\d+$", "", arxiv_id)


def fetch_recent_papers(max_papers=None):
    start_utc, end_utc, start_et, end_et = compute_arxiv_submission_window()

    env = os.environ.get("ARXIV_LOOKBACK_HOURS")
    if env:
        # Optional emergency fallback to the old rolling-window behavior.
        lookback = int(env)
        start_utc = datetime.now(timezone.utc) - timedelta(hours=lookback)
        end_utc = datetime.now(timezone.utc)
        print(
            f"  using ARXIV_LOOKBACK_HOURS={lookback}; "
            f"window {start_utc:%Y-%m-%d %H:%M} to {end_utc:%Y-%m-%d %H:%M} UTC"
        )
    else:
        print(
            "  arXiv-style submission window: "
            f"{start_et:%Y-%m-%d %H:%M %Z} to {end_et:%Y-%m-%d %H:%M %Z}"
        )
        print(
            f"  UTC window: {start_utc:%Y-%m-%d %H:%M} to {end_utc:%Y-%m-%d %H:%M}"
        )

    print("  fetching archives separately:", ", ".join(label for label, _ in ARXIV_QUERIES))

    papers = []
    seen = set()

    api_client = arxiv.Client(
        page_size=ARXIV_PAGE_SIZE,
        delay_seconds=ARXIV_DELAY_SECONDS,
        num_retries=ARXIV_NUM_RETRIES,
    )

    for label, query in ARXIV_QUERIES:
        if max_papers is not None and len(papers) >= max_papers:
            break

        search = arxiv.Search(
            query=query,
            max_results=FETCH_LIMIT,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        count_this_query = 0

        try:
            results_iter = api_client.results(search)
        except AttributeError:
            results_iter = search.results()

        for r in results_iter:
            if max_papers is not None and len(papers) >= max_papers:
                break

            # Since results are sorted newest first, we can stop this archive
            # once entries are older than the start of the target window.
            if r.published < start_utc:
                break

            base_id = arxiv_base_id(r)
            if base_id in seen:
                continue

            if start_utc <= r.published < end_utc:
                papers.append(r)
                seen.add(base_id)
                count_this_query += 1

        print(f"  {label}: {count_this_query} papers")

    papers.sort(key=lambda r: r.published, reverse=True)
    return papers


# ---------- PDF text extraction ----------
def extract_pdf_text(pdf_path):
    """Extract readable text from a PDF with PyMuPDF."""
    chunks = []
    doc = None

    try:
        doc = fitz.open(pdf_path)

        for page_idx, page in enumerate(doc):
            text = page.get_text("text")
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\n{3,}", "\n\n", text).strip()

            if text:
                chunks.append(f"\n\n--- Page {page_idx + 1} ---\n{text}")

    except Exception as e:
        print(f"  text extraction failed: {e}")

    finally:
        if doc is not None:
            doc.close()

    return "\n".join(chunks).strip()


def split_text(text, chunk_chars=CHUNK_CHARS, overlap=CHUNK_OVERLAP):
    """Split text into overlapping character chunks."""
    if not text:
        return []

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + chunk_chars, n)
        chunks.append(text[start:end])

        if end == n:
            break

        start = max(0, end - overlap)

    return chunks


# ---------- figure extraction ----------
def clean_caption(text, max_chars=700):
    """Compact caption text for Markdown display."""
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + "..."
    return text


def extract_caption_blocks(page):
    """
    Extract candidate figure captions from a page.

    Heuristic: look for text blocks starting with Fig., FIG., Figure, etc.
    This caption-based method works better for vector-heavy arXiv/APS PDFs
    than raw embedded-image extraction.
    """
    candidates = []

    try:
        blocks = page.get_text("blocks")
    except Exception:
        return candidates

    for block in blocks:
        if len(block) < 5:
            continue

        x0, y0, x1, y1, txt = block[:5]
        txt_clean = clean_caption(txt)

        if re.match(r"^(fig\.?|figure)\s*\d+", txt_clean, flags=re.IGNORECASE):
            candidates.append(
                {
                    "bbox": fitz.Rect(x0, y0, x1, y1),
                    "text": txt_clean,
                }
            )

    candidates.sort(key=lambda c: (c["bbox"].y0, c["bbox"].x0))
    return candidates


def save_pixmap_as_jpg(pix, img_path, jpeg_quality=FIGURE_JPEG_QUALITY):
    """Save pixmap as JPG, compatible with older PyMuPDF versions."""
    try:
        pix.save(str(img_path), jpg_quality=jpeg_quality)
    except TypeError:
        pix.save(str(img_path))


def caption_to_figure_clip(page, caption_bbox):
    """
    Estimate the figure region belonging to a caption by cropping above it.

    This captures vector figures, unlike raw embedded-image extraction.
    """
    page_rect = page.rect
    page_w = page_rect.width

    margin_x = 18
    margin_y = 10
    caption_center_x = 0.5 * (caption_bbox.x0 + caption_bbox.x1)

    # Approximate one-column vs two-column layout from caption width.
    if caption_bbox.width < 0.72 * page_w:
        if caption_center_x < page_w / 2:
            x0 = margin_x
            x1 = page_w / 2 - 6
        else:
            x0 = page_w / 2 + 6
            x1 = page_w - margin_x
    else:
        x0 = margin_x
        x1 = page_w - margin_x

    y1 = max(0, caption_bbox.y0 - margin_y)
    y0 = max(0, y1 - 320)

    return fitz.Rect(x0, y0, x1, y1) & page_rect


def extract_figures_with_captions_from_pdf(
    pdf_path,
    out_dir,
    max_figures=MAX_FIGURES_PER_PAPER,
    zoom=FIGURE_RENDER_ZOOM,
    jpeg_quality=FIGURE_JPEG_QUALITY,
):
    """
    Extract a lightweight figure gallery from a paper.

    Main method:
      - find figure captions,
      - render the page region above each caption as a compressed JPG,
      - display that crop together with the caption.

    Fallback:
      - if no captions are detected, save a few low-resolution page previews.
    """
    arxiv_id = pdf_path.stem.replace("/", "_")
    fig_dir = out_dir / f"{arxiv_id}_figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    figures = []
    doc = None

    try:
        doc = fitz.open(pdf_path)
        mat = fitz.Matrix(zoom, zoom)

        for page_num in range(len(doc)):
            if len(figures) >= max_figures:
                break

            page = doc[page_num]
            captions = extract_caption_blocks(page)

            for cap in captions:
                if len(figures) >= max_figures:
                    break

                clip = caption_to_figure_clip(page, cap["bbox"])

                if clip.width * clip.height < FIGURE_MIN_AREA:
                    continue

                try:
                    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
                except Exception:
                    continue

                img_name = f"{arxiv_id}_fig{len(figures) + 1}.jpg"
                img_path = fig_dir / img_name
                save_pixmap_as_jpg(pix, img_path, jpeg_quality=jpeg_quality)

                figures.append(
                    {
                        "image": str(img_path.relative_to(out_dir)),
                        "caption": cap["text"],
                        "page": page_num + 1,
                    }
                )

        if not figures:
            for page_num in range(len(doc)):
                if len(figures) >= max_figures:
                    break

                if page_num == 0 and len(doc) > 1:
                    continue

                page = doc[page_num]

                try:
                    pix = page.get_pixmap(matrix=mat, clip=page.rect, alpha=False)
                except Exception:
                    continue

                img_name = f"{arxiv_id}_page{page_num + 1}.jpg"
                img_path = fig_dir / img_name
                save_pixmap_as_jpg(pix, img_path, jpeg_quality=jpeg_quality)

                figures.append(
                    {
                        "image": str(img_path.relative_to(out_dir)),
                        "caption": f"Low-resolution page preview, page {page_num + 1}",
                        "page": page_num + 1,
                    }
                )

        print(f"  extracted {len(figures)} figure/page preview(s)")
        return figures

    except Exception as e:
        print(f"  figure gallery extraction failed: {e}")
        return []

    finally:
        if doc is not None:
            doc.close()


def extract_main_figure_from_pdf(pdf_path, out_dir):
    """
    Backward-compatible wrapper: return the first extracted figure path, if any.
    """
    figs = extract_figures_with_captions_from_pdf(pdf_path, out_dir, max_figures=1)
    if not figs:
        return None
    return out_dir / figs[0]["image"]


# ---------- Ollama helpers ----------
def chat_ollama(prompt, num_predict=NUM_PREDICT):
    chat_kwargs = dict(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0.2,
            "num_predict": num_predict,
            "num_ctx": NUM_CTX,
        },
    )

    try:
        resp = client.chat(**chat_kwargs, think=False)
    except TypeError:
        resp = client.chat(**chat_kwargs)

    msg = resp["message"] if isinstance(resp, dict) else resp.message
    text = (msg["content"] if isinstance(msg, dict) else msg.content) or ""

    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<\|?channel\|?>.*?<\|?channel\|?>", "", text, flags=re.DOTALL)

    return text.strip()


def _extract_balanced_json_object(text):
    """
    Extract the first balanced {...} object from model output.
    This is safer than a greedy regex if there is prose around the JSON.
    """
    start = text.find("{")
    if start == -1:
        return None

    depth = 0
    in_string = False
    escape = False

    for i in range(start, len(text)):
        ch = text[i]

        if escape:
            escape = False
            continue

        if ch == "\\":
            escape = True
            continue

        if ch == '"':
            in_string = not in_string
            continue

        if in_string:
            continue

        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]

    return None


def parse_json_object(text):
    """
    Parse the JSON object returned by the model.

    Robust to:
      - Markdown fences like ```json ... ```
      - LaTeX-style invalid JSON escapes such as \\lambda, \\mathcal, \\omega
      - trailing commas
    """
    text = (text or "").strip()

    # Remove optional Markdown code fences.
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text).strip()

    raw = _extract_balanced_json_object(text)
    if raw is None:
        raise ValueError(f"no JSON found in model output: {text[:500]!r}")

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Escape LaTeX-style backslashes while preserving real JSON escapes.
        # Special case: JSON treats \u as a Unicode escape, so LaTeX commands
        # like \uparrow or \underbrace must also be escaped unless followed
        # by exactly four hex digits.
        repaired = re.sub(r'\\u(?![0-9a-fA-F]{4})', r'\\\\u', raw)
        repaired = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', repaired)
        # Remove trailing commas before } or ].
        repaired = re.sub(r",\s*([}\]])", r"\1", repaired)
        return json.loads(repaired)


# ---------- classify + summarize ----------
CHUNK_PROMPT = """You are reading part of a scientific paper for a daily arxiv digest.

Paper title: {title}
Authors: {authors}
Primary arxiv categories: {primary_cat}

This is chunk {chunk_i} of {num_chunks} from the full PDF text.

Text chunk:
{text_chunk}

Extract concise notes from this chunk. Focus on:
- the main scientific problem,
- the physical system, model, Hamiltonian, master equation, or experimental platform,
- methods, approximations, simulations, calculations, or measurements,
- key observables, diagnostics, parameters, regimes, scales, or limits,
- main results and how the argument develops,
- what figures, tables, or captions in this chunk appear to show,
- limitations, assumptions, or open questions.

Return bullet-point notes only. Do not invent details.
"""


FINAL_PROMPT = """You are helping organize a daily arxiv digest of quantum physics and condensed matter papers.

Paper title: {title}

Primary arxiv categories: {primary_cat}

Authors: {authors}

Abstract:
{abstract}

Analysis basis:
{analysis_basis}

Notes extracted from the PDF:
{paper_notes}

Classify this paper into exactly ONE of these buckets:

  - "quantum information and computing"   -> qubits, QEC, quantum algorithms, quantum networks, photonic QI
  - "AMO physics"                          -> cold atoms, trapped ions, Rydberg, cavity QED, molecular physics
  - "numerical methods"                    -> tensor networks, Monte Carlo, DMRG, neural quantum states, classical simulation techniques
  - "quantum gases"                        -> BEC, BCS, ultracold Fermi/Bose gases (cond-mat.quant-gas)
  - "statistical mechanics"                -> thermodynamics, phase transitions, non-equilibrium (cond-mat.stat-mech)
  - "strongly correlated electrons"        -> Hubbard, high-Tc, heavy fermions, correlated materials (cond-mat.str-el)
  - "disordered systems and neural networks" -> localization, glasses, spin glasses, ML-physics (cond-mat.dis-nn)
  - "other"                                -> anything that doesn't fit above

Return ONLY a valid JSON object with these fields, nothing else. Do not use Markdown code fences. Do not use LaTeX backslashes inside JSON strings:
{{
  "category": "<one of the bucket labels above, exactly as written>",
  "type": "<one of exactly: theory | experiment | both>",
  "main_problem": "<1-2 sentences>",
  "main_result": "<1-2 sentences>",
  "method": "<1-2 sentences>",
  "model_or_system": "<1-3 sentences describing the physical system, model, Hamiltonian, master equation, or experimental platform>",
  "key_observables": "<important observables, diagnostics, quantities, or measurements; write 'not specified' if unclear>",
  "important_parameters": "<important parameters, regimes, limits, or scales; write 'not specified' if unclear>",
  "main_assumptions": "<main assumptions, approximations, or limitations; write 'not specified' if unclear>",
  "figures_summary": "<compact description of what the main figures appear to show, based only on extracted notes/captions; write 'not specified' if unclear>",
  "paper_structure": "<section-by-section or logic-by-logic structure of the paper in compact prose>",
  "why_interesting": "<why this may be interesting for a theoretical physicist working on AMO, open quantum systems, quantum optics, or many-body dynamics; write 'not directly relevant' if not relevant>",
  "summary": "<up to 5 sentences in plain English describing what the paper does and why it matters>"
}}
"""


def analyze_pdf_chunks(paper, full_text):
    chunks = split_text(full_text)

    if not chunks:
        return ""

    # Prefer the beginning and end of the paper if it is very long.
    if len(chunks) > MAX_CHUNKS_PER_PAPER:
        head = MAX_CHUNKS_PER_PAPER // 2
        tail = MAX_CHUNKS_PER_PAPER - head
        chunks = chunks[:head] + chunks[-tail:]

    notes = []

    for idx, text_chunk in enumerate(chunks, 1):
        print(f"  analyzing PDF chunk {idx}/{len(chunks)}")

        prompt = CHUNK_PROMPT.format(
            title=paper.title,
            authors=", ".join(a.name for a in paper.authors),
            primary_cat=", ".join(paper.categories) if paper.categories else "unknown",
            chunk_i=idx,
            num_chunks=len(chunks),
            text_chunk=text_chunk,
        )

        try:
            chunk_notes = chat_ollama(prompt, num_predict=800)
        except Exception as e:
            print(f"  chunk analysis failed: {e}")
            continue

        if chunk_notes:
            notes.append(f"Chunk {idx} notes:\n{chunk_notes}")

    return "\n\n".join(notes)


def classify_and_summarize(paper, pdf_path=None):
    full_text = ""

    if pdf_path is not None and pdf_path.exists():
        full_text = extract_pdf_text(pdf_path)

    if full_text:
        paper_notes = analyze_pdf_chunks(paper, full_text)
        analysis_basis = "full PDF text, analyzed in chunks"
    else:
        paper_notes = paper.summary.strip()
        analysis_basis = "abstract only; PDF text extraction failed or PDF unavailable"

    prompt = FINAL_PROMPT.format(
        title=paper.title,
        primary_cat=", ".join(paper.categories) if paper.categories else "unknown",
        authors=", ".join(a.name for a in paper.authors),
        abstract=paper.summary.strip(),
        analysis_basis=analysis_basis,
        paper_notes=paper_notes,
    )

    text = chat_ollama(prompt, num_predict=NUM_PREDICT)
    data = parse_json_object(text)

    cat = str(data.get("category", "")).strip().lower()
    typ = str(data.get("type", "")).strip().lower()

    if cat not in CATEGORIES:
        cat = "other"

    if typ not in ("theory", "experiment", "both"):
        typ = "theory"

    result = {
        "main_problem": str(data.get("main_problem", "")).strip(),
        "main_result": str(data.get("main_result", "")).strip(),
        "method": str(data.get("method", "")).strip(),
        "model_or_system": str(data.get("model_or_system", "")).strip(),
        "key_observables": str(data.get("key_observables", "")).strip(),
        "important_parameters": str(data.get("important_parameters", "")).strip(),
        "main_assumptions": str(data.get("main_assumptions", "")).strip(),
        "figures_summary": str(data.get("figures_summary", "")).strip(),
        "paper_structure": str(data.get("paper_structure", "")).strip(),
        "why_interesting": str(data.get("why_interesting", "")).strip(),
        "summary": str(data.get("summary", "")).strip(),
        "analysis_basis": analysis_basis,
    }

    return cat, typ, result


# ---------- relevance scoring ----------
RELEVANCE_PROMPT = """You are scoring how relevant an arxiv paper is to a researcher's
specific topics of interest. Use the analysis we already produced for the paper
(below), not the raw abstract — it's already condensed and accurate.

PAPER ANALYSIS:
- Title: {title}
- Category: {category}
- Type: {type}
- Main problem: {main_problem}
- Main result: {main_result}
- Method: {method}
- Model or system: {model_or_system}
- Key observables: {key_observables}
- Why it may be interesting: {why_interesting}

TOPICS OF INTEREST (each has a key and a description):
{topic_list}

For each topic, give an integer relevance score from 0 to 5:
  0 = unrelated
  1 = mentions topic in passing only
  2 = uses related techniques but not focused on it
  3 = directly relevant; topic is one of several themes
  4 = directly studies this topic; main focus of the paper
  5 = breakthrough or landmark result on exactly this topic

Be strict: most papers should score 0 on most topics. Reserve 4-5 for papers
where the topic is the actual subject of the work, not just a tool or
analogy that happens to be mentioned.

Return ONLY a JSON object mapping each topic key to its integer score, like:
{{"topic_key_1": 0, "topic_key_2": 3, ...}}

Use the EXACT topic keys shown above."""


def score_relevance_topics(paper, analysis, category, paper_type):
    """
    Ask the LLM to score the paper's relevance to each topic in TOPICS.
    Returns dict mapping topic key -> integer score 0..5.
    Returns {} if TOPICS is empty or if the LLM call fails.
    """
    if not TOPICS:
        return {}

    topic_list = "\n".join(f"- {key}: {desc}" for key, desc in TOPICS.items())
    prompt = RELEVANCE_PROMPT.format(
        title=paper.title,
        category=category,
        type=paper_type,
        main_problem=analysis.get("main_problem", "") or "(not extracted)",
        main_result=analysis.get("main_result", "") or "(not extracted)",
        method=analysis.get("method", "") or "(not extracted)",
        model_or_system=analysis.get("model_or_system", "") or "(not extracted)",
        key_observables=analysis.get("key_observables", "") or "(not extracted)",
        why_interesting=analysis.get("why_interesting", "") or "(not extracted)",
        topic_list=topic_list,
    )

    try:
        text = chat_ollama(prompt, num_predict=300)
        data = parse_json_object(text)
    except Exception as e:
        print(f"  relevance scoring failed: {e}")
        return {key: 0 for key in TOPICS}

    scores = {}
    for key in TOPICS:
        v = data.get(key, 0)
        try:
            score = int(v)
        except (TypeError, ValueError):
            score = 0
        scores[key] = max(0, min(5, score))
    return scores


# ---------- per-paper JSON cache ----------
def paper_json_path(out_dir, arxiv_id):
    """Path where this paper's analysis JSON lives. Auto-creates the JSON/ subfolder."""
    safe_id = arxiv_id.replace("/", "_")
    json_dir = out_dir / "JSON"
    json_dir.mkdir(parents=True, exist_ok=True)
    return json_dir / f"{safe_id}.json"


def load_cached_entry(out_dir, arxiv_id):
    """Return the cached entry dict for this paper, or None if absent or unreadable."""
    p = paper_json_path(out_dir, arxiv_id)
    if not p.exists():
        return None
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"  warn: could not read cached JSON {p.name}: {e}")
        return None


def save_paper_entry(out_dir, arxiv_id, entry):
    """
    Write entry as JSON to {out_dir}/JSON/{arxiv_id}.json. The entry already
    contains everything needed to re-render the paper's section without
    rerunning the LLM.
    """
    p = paper_json_path(out_dir, arxiv_id)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2, ensure_ascii=False)
    tmp.replace(p)


# ---------- Markdown rendering ----------
def _entry_anchor_id(e):
    """Stable anchor id for a paper entry, derived from its arxiv id when
    available and falling back to a slug of the URL."""
    raw = e.get("arxiv_id") or e.get("url", "")
    raw = raw.rsplit("/", 1)[-1]
    raw = re.sub(r"v\d+$", "", raw)
    slug = re.sub(r"[^a-zA-Z0-9._-]", "-", raw).strip("-")
    return f"paper-{slug or 'entry'}"


def _render_entry(e, lines):
    """Append one paper's markdown block to lines."""
    anchor = _entry_anchor_id(e)
    # Anchor for in-page jumps from the top sections. Empty <a id="..."> works
    # in GitHub-rendered markdown and VS Code preview alike.
    lines.append(f'<a id="{anchor}"></a>')

    star = "⭐ " if e.get("highlighted") else ""
    lines.append(f"### {star}[{e['title']}]({e['url']})")
    lines.append("")

    if e.get("highlighted"):
        pretty = ", ".join(e["highlighted"])
        lines.append(f"**Highlighted author(s):** {pretty}  ")

    lines.append(f"**Authors:** {e['authors']}  ")
    lines.append(f"**Type:** {e['type']} · **PDF:** <{e['pdf']}>  ")
    lines.append(f"**Analysis basis:** {e.get('analysis_basis', 'unknown')}")

    # Topic relevance: only show topics with score >= 1, sorted high to low.
    topics = e.get("topic_scores") or {}
    if topics:
        relevant = sorted(
            [(k, v) for k, v in topics.items() if v >= 1],
            key=lambda kv: (-kv[1], kv[0]),
        )
        if relevant:
            badges = []
            for key, score in relevant:
                fire = "🔥 " if score >= RELEVANCE_THRESHOLD else ""
                badges.append(f"{fire}`{key}` **{score}/5**")
            lines.append("**Topic relevance:** " + " · ".join(badges))
    lines.append("")

    if e.get("figures"):
        # One <details> block per figure. The first is `open`, the rest are
        # collapsed and labelled "📷 Fig 2", "📷 Fig 3", etc. Click any label
        # to expand that figure. Works on github.com (web + mobile) and in
        # VS Code's Markdown preview without any CSS.
        for idx, fig in enumerate(e["figures"], 1):
            image = fig.get("image")
            caption = fig.get("caption") or f"Figure from page {fig.get('page', '?')}"
            safe_caption = caption.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            open_attr = " open" if idx == 1 else ""
            lines.append(f"<details{open_attr}><summary>📷 Fig {idx}</summary>")
            lines.append("")
            lines.append(f'<img src="{image}" width="500"><br>')
            lines.append(f"<sub>{safe_caption}</sub>")
            lines.append("")
            lines.append("</details>")
            lines.append("")
    elif e.get("figure"):
        lines.append(f"![main figure]({e['figure']})")
        lines.append("")

    if e.get("main_problem"):
        lines.append(f"**Main problem.** {e['main_problem']}")
        lines.append("")

    if e.get("main_result"):
        lines.append(f"**Main result.** {e['main_result']}")
        lines.append("")

    if e.get("method"):
        lines.append(f"**Method.** {e['method']}")
        lines.append("")

    lines.append(f"**Summary.** {e['summary']}")
    lines.append("")
    detail_items = [
        ("Model / system", e.get("model_or_system")),
        ("Key observables", e.get("key_observables")),
        ("Important parameters / regimes", e.get("important_parameters")),
        ("Assumptions / limitations", e.get("main_assumptions")),
        ("Figures summary", e.get("figures_summary")),
        ("Paper structure", e.get("paper_structure")),
        ("Why it may be interesting", e.get("why_interesting")),
    ]
    detail_items = [
        (k, v) for k, v in detail_items
        if v and v.strip() and v.strip().lower() not in {"not specified", "unknown", "not directly relevant"}
    ]

    if detail_items:
        lines.append("<details><summary>Detailed structure</summary>")
        lines.append("")
        for label, value in detail_items:
            lines.append(f"**{label}.** {value}")
            lines.append("")
        lines.append("</details>")
        lines.append("")

    lines.append("<details><summary>Abstract</summary>")
    lines.append("")
    lines.append(e["abstract"])
    lines.append("")
    lines.append("</details>")
    lines.append("")
    # Small "back to top" link so the reader can jump back without scrolling.
    lines.append("<sub>[↑ back to top](#top)</sub>")
    lines.append("")


def build_markdown_digest(entries_by_cat, date_str, progress=None):
    total = sum(len(v) for v in entries_by_cat.values())
    all_entries = [e for items in entries_by_cat.values() for e in items]
    highlighted = [e for e in all_entries if e.get("highlighted")]

    # Pick papers with at least one topic scoring at or above the threshold.
    def _max_topic_score(e):
        scores = e.get("topic_scores") or {}
        return max(scores.values()) if scores else 0

    # Show every paper with at least one nonzero topic score, sorted by
    # how strongly its top topic matches.
    relevant = [e for e in all_entries if _max_topic_score(e) >= 1]
    relevant.sort(
        key=lambda e: (-_max_topic_score(e),
                       -sum((e.get("topic_scores") or {}).values()),
                       e["title"].lower()),
    )

    header_meta = f"*{total} papers · {len(relevant)} relevant · {len(highlighted)} highlighted*"
    if progress is not None:
        done, planned = progress
        if done < planned:
            header_meta += f"  \n_⏳ in progress: {done}/{planned} papers processed (file updates after each one)_"
        elif planned == 0:
            header_meta += "  \n_⏳ starting up..._"

    lines = [
        '<a id="top"></a>',
        f"# arxiv digest (quant-ph + cond-mat) — {date_str}",
        "",
        header_meta,
        "",
    ]

    if relevant:
        lines.append("")
        lines.append(f"## 🔥 Most relevant ({len(relevant)})")
        lines.append("")
        lines.append(
            "*Every paper with at least one nonzero topic score, sorted by best-matching score. "
            f"🔥 marks scores ≥{RELEVANCE_THRESHOLD}/5. "
            "Click the title to jump to the full entry below; click [arXiv] to open the paper page.*"
        )
        lines.append("")
        for e in relevant:
            scores = e.get("topic_scores") or {}
            shown = sorted(
                [(k, v) for k, v in scores.items() if v >= 1],
                key=lambda kv: (-kv[1], kv[0]),
            )
            badges = []
            for key, score in shown:
                fire = "🔥 " if score >= RELEVANCE_THRESHOLD else ""
                badges.append(f"{fire}`{key}` **{score}/5**")
            tags = " · ".join(badges)
            star = "⭐ " if e.get("highlighted") else ""
            anchor = _entry_anchor_id(e)
            lines.append(
                f"- {star}[{e['title']}](#{anchor}) [[arXiv]]({e['url']}) — {tags}"
            )
        lines.append("")

    if highlighted:
        lines.append("")
        lines.append(f"## ⭐ Highlighted ({len(highlighted)})")
        lines.append("")
        lines.append(
            "*Papers by authors on your watch list. "
            "Click the title to jump to the full entry below; click [arXiv] to open the paper page.*"
        )
        lines.append("")

        for e in highlighted:
            pretty = ", ".join(e.get("highlighted", []))
            anchor = _entry_anchor_id(e)
            lines.append(
                f"- ⭐ [{e['title']}](#{anchor}) [[arXiv]]({e['url']}) — {pretty}"
            )

        lines.append("")

    for cat in CATEGORIES:
        items = entries_by_cat[cat]

        if not items:
            continue

        lines.append("")
        lines.append(f"## {cat} ({len(items)})")
        lines.append("")

        for e in items:
            _render_entry(e, lines)

    return "\n".join(lines)



# ---------- main ----------
def _write_digest_atomic(digest_path, entries_by_cat, date_str, papers_done, papers_total):
    """
    Write the digest to disk atomically: write to a temp file in the same
    directory, then rename. This guarantees the user never sees a half-written
    file even if they Ctrl+C in the middle of a write.
    """
    text = build_markdown_digest(
        entries_by_cat, date_str,
        progress=(papers_done, papers_total),
    )
    tmp = digest_path.with_suffix(digest_path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(digest_path)  # atomic on POSIX and Windows


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    out_dir = OUTPUT_DIR / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    digest_path = out_dir / "digest_fig_test.md"

    print(f"Fetching quant-ph + cond-mat papers for {date_str}...")
    if MAX_PAPERS_TO_PROCESS is not None:
        print(f"  WARNING: MAX_PAPERS_TO_PROCESS={MAX_PAPERS_TO_PROCESS}; only this many papers will be processed.")
    papers = fetch_recent_papers(max_papers=MAX_PAPERS_TO_PROCESS)

    print(f"  {len(papers)} papers in lookback window.\n")

    entries_by_cat = {c: [] for c in CATEGORIES}
    processed_arxiv_ids = set()

    # Write an initial empty digest so the file exists right away — useful
    # if you're tailing it from another window.
    _write_digest_atomic(digest_path, entries_by_cat, date_str, 0, len(papers))
    print(f"Digest will grow at: {digest_path}\n")

    try:
        with tempfile.TemporaryDirectory() as tmpdir_name:
            tmpdir = Path(tmpdir_name)

            for i, paper in enumerate(papers, 1):
                matched = paper_highlight_matches(paper)
                star = "⭐ " if matched else ""
                print(f"[{i}/{len(papers)}] {star}{paper.title[:90]}")

                arxiv_id = arxiv_base_id(paper)
                if arxiv_id in processed_arxiv_ids:
                    print(f"  skipping duplicate arXiv id {arxiv_id}")
                    continue
                processed_arxiv_ids.add(arxiv_id)

                # If we already analyzed this paper, reuse the saved JSON.
                cached = load_cached_entry(out_dir, arxiv_id)
                if cached is not None:
                    cat = cached.get("category") or "other"
                    if cat not in CATEGORIES:
                        cat = "other"
                    # Make sure highlighted reflects the current author list,
                    # in case it was edited since the cache was written.
                    cached["highlighted"] = matched
                    # If TOPICS was added/changed since caching, rescore.
                    cached_topics = set((cached.get("topic_scores") or {}).keys())
                    if cached_topics != set(TOPICS):
                        analysis_for_score = {
                            k: cached.get(k, "") for k in
                            ("main_problem", "main_result", "method",
                             "model_or_system", "key_observables", "why_interesting")
                        }
                        cached["topic_scores"] = score_relevance_topics(
                            paper, analysis_for_score, cat, cached.get("type", "theory"),
                        )
                        save_paper_entry(out_dir, arxiv_id, {**cached, "category": cat})
                    print(f"  cached → category: {cat}")
                    entries_by_cat[cat].append(cached)
                    _write_digest_atomic(digest_path, entries_by_cat, date_str, i, len(papers))
                    continue

                safe_arxiv_id = arxiv_id.replace("/", "_")
                pdf_path = tmpdir / f"{safe_arxiv_id}.pdf"

                try:
                    paper.download_pdf(dirpath=str(tmpdir), filename=pdf_path.name)
                except Exception as e:
                    print(f"  PDF download failed: {e}")
                    pdf_path = None

                try:
                    cat, typ, analysis = classify_and_summarize(paper, pdf_path=pdf_path)
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    print(f"  classify failed: {e}")
                    continue

                # Score relevance to your topics (only after we have analysis).
                topic_scores = score_relevance_topics(paper, analysis, cat, typ)
                if topic_scores:
                    top_match = max(topic_scores.values())
                    print(f"  category: {cat}; top topic score: {top_match}/5")
                else:
                    print(f"  category: {cat}")

                figures = []
                if pdf_path is not None and pdf_path.exists():
                    figures = extract_figures_with_captions_from_pdf(pdf_path, out_dir)
                    pdf_path.unlink(missing_ok=True)

                entry = {
                    "arxiv_id": arxiv_id,
                    "category": cat,
                    "title": paper.title.strip().replace("\n", " "),
                    "authors": ", ".join(a.name for a in paper.authors),
                    "abstract": paper.summary.strip().replace("\n", " "),
                    "url": paper.entry_id,
                    "pdf": paper.pdf_url,
                    "type": typ,
                    "summary": analysis["summary"],
                    "main_problem": analysis["main_problem"],
                    "main_result": analysis["main_result"],
                    "method": analysis["method"],
                    "model_or_system": analysis.get("model_or_system", ""),
                    "key_observables": analysis.get("key_observables", ""),
                    "important_parameters": analysis.get("important_parameters", ""),
                    "main_assumptions": analysis.get("main_assumptions", ""),
                    "figures_summary": analysis.get("figures_summary", ""),
                    "paper_structure": analysis.get("paper_structure", ""),
                    "why_interesting": analysis.get("why_interesting", ""),
                    "analysis_basis": analysis["analysis_basis"],
                    "figures": figures,
                    "figure": figures[0]["image"] if figures else None,
                    "highlighted": matched,
                    "topic_scores": topic_scores,
                }

                # Save per-paper JSON so this paper can be skipped on rerun
                # and reused for offline analysis later.
                save_paper_entry(out_dir, arxiv_id, entry)

                entries_by_cat[cat].append(entry)

                # Refresh the on-disk digest after every successful paper.
                # Atomic write means a Ctrl+C here cannot leave a corrupt file.
                _write_digest_atomic(digest_path, entries_by_cat, date_str, i, len(papers))

    except KeyboardInterrupt:
        # Make sure whatever we have is on disk, then exit politely.
        _write_digest_atomic(
            digest_path, entries_by_cat, date_str,
            len(processed_arxiv_ids), len(papers),
        )
        done = sum(len(v) for v in entries_by_cat.values())
        print(f"\nInterrupted. Saved {done} processed paper(s) to: {digest_path}")
        return

    print(f"\nDigest written to: {digest_path}")


if __name__ == "__main__":
    main()
