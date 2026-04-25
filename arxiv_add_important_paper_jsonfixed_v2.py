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
OUTPUT_DIR = Path.home() / "arxiv_digests"
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

HIGHLIGHT_AUTHORS = [
    "Sarang Gopalakrishnan",
    "Andrii G. Sotnikov",
    "Denys I. Bondar",
    "Anders S. Sorensen",
    "Rosario Fazio",
    "Suzanne Yelin",
    "Jamir Marino",
    "Mikhail Lukin",
]

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
    Compute the arXiv submission window corresponding to the latest visible
    arXiv "new" papers.

    Important convention:
      Papers displayed as "today's new papers" were usually submitted during
      the PREVIOUS completed submission window.

    Therefore, if the most recent cutoff is today at 14:00 ET, we move one
    arXiv workday back and use:

        previous_previous_workday 14:00 ET <= submitted < previous_workday 14:00 ET

    Example:
      If today is 2026-04-24 and the not-yet-visible window is
      2026-04-23 14:00 ET to 2026-04-24 14:00 ET, this function instead uses
      2026-04-22 14:00 ET to 2026-04-23 14:00 ET.
    """
    eastern = ZoneInfo("America/New_York")

    if now is None:
        now_et = datetime.now(eastern)
    else:
        now_et = now.astimezone(eastern)

    today = now_et.date()
    cutoff_time = datetime.strptime("14:00", "%H:%M").time()

    # First find the latest completed cutoff day.
    if now_et.time() < cutoff_time:
        latest_completed_cutoff_day = previous_arxiv_workday(today)
    else:
        latest_completed_cutoff_day = today

    while latest_completed_cutoff_day.weekday() >= 5:
        latest_completed_cutoff_day = previous_arxiv_workday(latest_completed_cutoff_day)

    # Move one full arXiv workday back to match the currently visible "new" list.
    end_day = previous_arxiv_workday(latest_completed_cutoff_day)
    start_day = previous_arxiv_workday(end_day)

    start_et = datetime.combine(start_day, cutoff_time, tzinfo=eastern)
    end_et = datetime.combine(end_day, cutoff_time, tzinfo=eastern)

    return start_et.astimezone(timezone.utc), end_et.astimezone(timezone.utc), start_et, end_et


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
        # Special case: JSON treats \u as Unicode escape, so LaTeX commands
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


# ---------- Markdown rendering ----------
def _render_entry(e, lines):
    """Append one paper's markdown block to lines."""
    star = "⭐ " if e.get("highlighted") else ""
    lines.append(f"### {star}[{e['title']}]({e['url']})")
    lines.append("")

    if e.get("highlighted"):
        pretty = ", ".join(e["highlighted"])
        lines.append(f"**Highlighted author(s):** {pretty}  ")

    lines.append(f"**Authors:** {e['authors']}  ")
    lines.append(f"**Type:** {e['type']} · **PDF:** <{e['pdf']}>  ")
    lines.append(f"**Analysis basis:** {e.get('analysis_basis', 'unknown')}")
    lines.append("")

    if e.get("figures"):
        lines.append("<details open><summary>Figures</summary>")
        lines.append("")
        lines.append('<div style="display:flex; overflow-x:auto; gap:12px; padding:8px 0;">')
        for fig in e["figures"]:
            image = fig.get("image")
            caption = fig.get("caption") or f"Figure from page {fig.get('page', '?')}"
            safe_caption = caption.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            lines.append(
                f'<div style="min-width:220px; max-width:260px;">'
                f'<img src="{image}" width="220"><br>'
                f'<small>{safe_caption}</small>'
                f'</div>'
            )
        lines.append("</div>")
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


def build_markdown_digest(entries_by_cat, date_str):
    total = sum(len(v) for v in entries_by_cat.values())
    all_entries = [e for items in entries_by_cat.values() for e in items]
    highlighted = [e for e in all_entries if e.get("highlighted")]

    lines = [
        f"# arxiv digest (quant-ph + cond-mat) — {date_str}",
        "",
        f"*{total} papers · {len(highlighted)} highlighted*",
        "",
    ]

    if highlighted:
        lines.append("")
        lines.append(f"## ⭐ Highlighted ({len(highlighted)})")
        lines.append("")
        lines.append("*Papers by authors on your watch list. Full entries appear only once in their normal category below.*")
        lines.append("")

        for e in highlighted:
            pretty = ", ".join(e.get("highlighted", []))
            lines.append(f"- ⭐ [{e['title']}]({e['url']}) — {pretty}")

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



# ---------- important-paper workflow ----------
IMPORTANT_PAPERS_MD = Path(os.environ.get(
    "IMPORTANT_PAPERS_MD",
    str(OUTPUT_DIR / "important_papers.md")
))


def normalize_arxiv_id(arxiv_id):
    """
    Accept forms like:
      2404.12345
      2404.12345v2
      https://arxiv.org/abs/2404.12345
      https://arxiv.org/pdf/2404.12345
    and return the arXiv id string.
    """
    s = arxiv_id.strip()
    s = s.replace("https://", "").replace("http://", "")
    s = s.replace("arxiv.org/abs/", "").replace("arxiv.org/pdf/", "")
    s = s.replace(".pdf", "")
    s = s.strip("/")
    return s


def fetch_paper_by_id(arxiv_id):
    arxiv_id = normalize_arxiv_id(arxiv_id)

    search = arxiv.Search(id_list=[arxiv_id], max_results=1)

    api_client = arxiv.Client(
        page_size=1,
        delay_seconds=ARXIV_DELAY_SECONDS,
        num_retries=ARXIV_NUM_RETRIES,
    )

    try:
        results = list(api_client.results(search))
    except AttributeError:
        results = list(search.results())

    if not results:
        raise ValueError(f"No arXiv paper found for id: {arxiv_id}")

    return results[0]


def make_entry_from_paper(paper, out_dir, tmpdir):
    """
    Analyze one arXiv paper using the same logic as the daily digest.
    Returns a markdown-entry dictionary compatible with _render_entry().
    """
    arxiv_id = arxiv_base_id(paper)
    safe_arxiv_id = arxiv_id.replace("/", "_")
    pdf_path = tmpdir / f"{safe_arxiv_id}.pdf"

    print(f"Downloading PDF for {arxiv_id}: {paper.title[:90]}")

    try:
        paper.download_pdf(dirpath=str(tmpdir), filename=pdf_path.name)
    except Exception as e:
        print(f"  PDF download failed: {e}")
        pdf_path = None

    print("Analyzing paper with LLM...")
    cat, typ, analysis = classify_and_summarize(paper, pdf_path=pdf_path)

    figures = []
    if pdf_path is not None and pdf_path.exists():
        figures = extract_figures_with_captions_from_pdf(pdf_path, out_dir)
        pdf_path.unlink(missing_ok=True)

    return {
        "title": paper.title.strip().replace("\n", " "),
        "authors": ", ".join(a.name for a in paper.authors),
        "abstract": paper.summary.strip().replace("\n", " "),
        "url": paper.entry_id,
        "pdf": paper.pdf_url,
        "type": typ,
        "category": cat,
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
        "highlighted": [],
        "arxiv_id": arxiv_id,
        "added_date": datetime.now().strftime("%Y-%m-%d"),
    }


def render_single_entry(e):
    lines = []
    lines.append("")
    lines.append(f"<!-- arxiv_id: {e['arxiv_id']} -->")
    lines.append(f"<!-- added: {e['added_date']} -->")
    lines.append("")
    _render_entry(e, lines)
    return "\n".join(lines)


def important_file_has_arxiv_id(path, arxiv_id):
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return f"<!-- arxiv_id: {arxiv_id} -->" in text


def ensure_important_file_header(path):
    if path.exists():
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    header = [
        "# Important arXiv papers",
        "",
        "This file is generated by `arxiv_add_important_paper.py`.",
        "",
    ]
    path.write_text("\n".join(header), encoding="utf-8")


def append_paper_to_important_md(arxiv_id, important_md=IMPORTANT_PAPERS_MD):
    paper = fetch_paper_by_id(arxiv_id)
    normalized_id = arxiv_base_id(paper)

    ensure_important_file_header(important_md)

    if important_file_has_arxiv_id(important_md, normalized_id):
        print(f"Already present in {important_md}: {normalized_id}")
        return

    out_dir = important_md.parent / "important_paper_assets"
    out_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir_name:
        tmpdir = Path(tmpdir_name)
        entry = make_entry_from_paper(paper, out_dir, tmpdir)

    entry_md = render_single_entry(entry)

    with important_md.open("a", encoding="utf-8") as f:
        f.write("\n")
        f.write(entry_md)
        f.write("\n")

    print(f"Added {normalized_id} to: {important_md}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Analyze specific arXiv papers and append them to an important-papers Markdown file."
    )
    parser.add_argument(
        "arxiv_ids",
        nargs="+",
        help="One or more arXiv IDs or arXiv URLs, e.g. 2404.12345 or https://arxiv.org/abs/2404.12345",
    )
    parser.add_argument(
        "--out",
        type=str,
        default=str(IMPORTANT_PAPERS_MD),
        help="Path to important papers Markdown file. Default: ~/arxiv_digests/important_papers.md",
    )

    args = parser.parse_args()
    important_md = Path(args.out).expanduser().resolve()

    for arxiv_id in args.arxiv_ids:
        try:
            append_paper_to_important_md(arxiv_id, important_md=important_md)
        except Exception as e:
            print(f"Failed for {arxiv_id}: {e}")


if __name__ == "__main__":
    main()
