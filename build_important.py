#!/usr/bin/env python3
"""
Build a rolling "most important papers" digest from cached JSONs.

Scans every per-day JSON folder under the output dir for papers scoring ≥4
on any topic, and renders one big HTML/Markdown file at:

    {OUTPUT_DIR}/report_important.html
    {OUTPUT_DIR}/report_important.md

Papers are grouped by date, newest day first. Within a day, sorted by
max topic score then by sum.

Run standalone:
    python build_important.py
    python build_important.py --start-date 2026-04-26
    python build_important.py --threshold 5     # stricter
    python build_important.py --output-dir /custom/path

Auto-runs at the end of every digest run if you call it from arxiv_daily.py.
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

# Reuse the rendering pipeline from the main script. Importing is safe —
# arxiv_daily.py's heavy work is guarded by `if __name__ == "__main__"`.
import arxiv_daily as ad

# ---------- defaults ----------
DEFAULT_START_DATE = "2026-04-26"
DEFAULT_THRESHOLD = 5   # max topic score required for a paper to qualify


# ---------- date and JSON discovery ----------
def parse_iso_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def find_dated_json_folders(output_dir, start_date_str):
    """Return list of (date_str, json_dir) for every YYYY-MM-DD folder
    under output_dir whose date is >= start_date. Sorted newest first."""
    try:
        start = parse_iso_date(start_date_str)
    except ValueError:
        raise SystemExit(f"Invalid start date: {start_date_str!r}; expected YYYY-MM-DD.")

    out = []
    for child in output_dir.iterdir():
        if not child.is_dir():
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", child.name):
            continue
        try:
            d = parse_iso_date(child.name)
        except ValueError:
            continue
        if d < start:
            continue
        json_dir = child / "JSON"
        if json_dir.exists() and json_dir.is_dir():
            out.append((child.name, json_dir))

    out.sort(key=lambda pair: pair[0], reverse=True)
    return out


# ---------- entry filtering ----------
def load_entries_from_dir(json_dir):
    """Load every JSON in a folder, skipping unreadable ones."""
    entries = []
    for jf in sorted(json_dir.glob("*.json")):
        try:
            with jf.open("r", encoding="utf-8") as f:
                entries.append(json.load(f))
        except Exception as exc:
            print(f"  skipping unreadable {jf.name}: {exc}")
    return entries


def is_important(entry, threshold):
    """A paper is important iff some topic scored >= threshold."""
    scores = entry.get("topic_scores") or {}
    if not scores:
        return False
    return max(scores.values()) >= threshold


# ---------- figure path rewriting ----------
def adjust_figure_paths(entry, date_str):
    """report_important.html lives one level up from the per-day folders,
    so figure paths need a date prefix. Returns a shallow copy of entry
    with rewritten paths so we don't mutate the cached JSON."""
    e = dict(entry)
    figs = entry.get("figures")
    if figs:
        new_figs = []
        for fig in figs:
            f = dict(fig)
            img = f.get("image")
            if img and not img.startswith(("http://", "https://", "/")) and not img.startswith(date_str + "/"):
                f["image"] = f"{date_str}/{img}"
            new_figs.append(f)
        e["figures"] = new_figs
    fig = entry.get("figure")
    if fig and not fig.startswith(("http://", "https://", "/")) and not fig.startswith(date_str + "/"):
        e["figure"] = f"{date_str}/{fig}"
    return e


def adjust_anchor_for_date(entry, date_str):
    """Make sure anchor ids are unique across days by stashing a date-aware
    arxiv_id used by the renderer's _entry_anchor_id helper."""
    e = dict(entry)
    raw = entry.get("arxiv_id") or entry.get("url", "").rsplit("/", 1)[-1]
    raw = re.sub(r"v\d+$", "", raw)
    e["arxiv_id"] = f"{date_str}-{raw}"
    return e


# ---------- markdown construction ----------
def build_important_markdown(by_date, threshold):
    total = sum(len(papers) for _, papers in by_date)
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        '<a id="top"></a>',
        f"# Most important arxiv papers",
        "",
        f"*Papers scoring ≥{threshold}/5 on at least one topic. "
        f"{total} paper(s) total across {len(by_date)} day(s). "
        f"Last refreshed {today}.*",
        "",
    ]

    for date_str, papers in by_date:
        if not papers:
            continue
        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            pretty_date = d.strftime("%A, %B %-d, %Y")
        except ValueError:
            pretty_date = date_str
        lines.append("---")
        lines.append("")
        lines.append(f"## {pretty_date}  ([daily report]({date_str}/report.html))")
        lines.append("")
        lines.append(f"*{len(papers)} important paper(s) this day*")
        lines.append("")
        for e in papers:
            ad._render_entry(e, lines)

    return "\n".join(lines)


# ---------- public entry point ----------
def build_important_report(output_dir=None,
                           start_date=DEFAULT_START_DATE,
                           threshold=DEFAULT_THRESHOLD,
                           verbose=True):
    """Scan JSONs, build the rolling important-papers report. Returns the
    path to the HTML file written, or None if no important papers exist yet."""
    output_dir = Path(output_dir) if output_dir else ad.OUTPUT_DIR
    output_dir = output_dir.resolve()

    if not output_dir.exists():
        if verbose:
            print(f"output dir does not exist: {output_dir}")
        return None

    folders = find_dated_json_folders(output_dir, start_date)
    if verbose:
        print(f"Found {len(folders)} dated JSON folder(s) since {start_date}")

    by_date = []  # list of (date_str, [adjusted entries], newest first)
    grand_total_scanned = 0
    grand_total_kept = 0

    for date_str, json_dir in folders:
        entries = load_entries_from_dir(json_dir)
        grand_total_scanned += len(entries)
        keepers = [e for e in entries if is_important(e, threshold)]

        # Sort within the day: max score desc, then sum desc, then title.
        def _sort_key(e):
            scores = e.get("topic_scores") or {}
            return (-max(scores.values(), default=0),
                    -sum(scores.values()),
                    (e.get("title") or "").lower())
        keepers.sort(key=_sort_key)

        # Adjust paths and anchor IDs so the merged HTML works.
        adjusted = [adjust_anchor_for_date(adjust_figure_paths(e, date_str), date_str)
                    for e in keepers]
        if adjusted:
            by_date.append((date_str, adjusted))
        grand_total_kept += len(keepers)
        if verbose:
            print(f"  {date_str}: {len(keepers)}/{len(entries)} important")

    if not by_date:
        if verbose:
            print(f"No papers scoring >= {threshold} found across {grand_total_scanned} entries.")
        # Still write a placeholder so the file isn't stale or missing.
        markdown_text = (
            f'<a id="top"></a>\n# Most important arxiv papers\n\n'
            f'*No papers scoring ≥{threshold}/5 yet. Last refreshed '
            f'{datetime.now().strftime("%Y-%m-%d")}.*'
        )
    else:
        markdown_text = build_important_markdown(by_date, threshold)

    md_path = output_dir / "report_important.md"
    html_path = output_dir / "report_important.html"

    md_path.write_text(markdown_text, encoding="utf-8")
    html_text = ad.markdown_to_html_document(markdown_text, "Most important arxiv papers")
    html_path.write_text(html_text, encoding="utf-8")

    if verbose:
        print(f"\nWrote: {md_path}")
        print(f"Wrote: {html_path}")
        print(f"Kept {grand_total_kept} of {grand_total_scanned} papers across {len(by_date)} day(s).")

    return html_path


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output-dir", type=Path,
                        help="Override OUTPUT_DIR (default: from arxiv_daily.py)")
    parser.add_argument("--start-date", default=DEFAULT_START_DATE,
                        help=f"Earliest YYYY-MM-DD folder to scan (default {DEFAULT_START_DATE})")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD,
                        help=f"Min topic score to qualify (default {DEFAULT_THRESHOLD})")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    build_important_report(
        output_dir=args.output_dir,
        start_date=args.start_date,
        threshold=args.threshold,
        verbose=not args.quiet,
    )


if __name__ == "__main__":
    main()
