from pathlib import Path
import re
import math

INPUT_MD = Path("digest_output_t.md")
OUTPUT_DIR = Path("split_report")
PAPERS_PER_PAGE = 20

OUTPUT_DIR.mkdir(exist_ok=True)

text = INPUT_MD.read_text(encoding="utf-8")

# Split only before paper anchors
paper_start_re = re.compile(
    r'(?=^<a id="paper-[^"]+"></a>\s*$)',
    re.MULTILINE,
)

parts = paper_start_re.split(text)

header = parts[0].strip() + "\n\n"
paper_sections = [p.strip() + "\n" for p in parts[1:] if p.strip()]

n_pages = math.ceil(len(paper_sections) / PAPERS_PER_PAGE)

index_lines = [
    "# Daily arXiv Report",
    "",
    f"Total papers: {len(paper_sections)}",
    "",
    "## Pages",
    "",
]

for i in range(n_pages):
    start = i * PAPERS_PER_PAGE + 1
    end = min((i + 1) * PAPERS_PER_PAGE, len(paper_sections))
    filename = f"papers_{i+1:02d}.md"
    index_lines.append(f"- [Papers {start}–{end}]({filename})")

index_lines.append("")
index_lines.append("---")
index_lines.append("")
index_lines.append(header)

(OUTPUT_DIR / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

for i in range(n_pages):
    start = i * PAPERS_PER_PAGE
    end = min((i + 1) * PAPERS_PER_PAGE, len(paper_sections))

    filename = f"papers_{i+1:02d}.md"

    nav = [
        "# Daily arXiv Report",
        "",
        "[← Index](index.md)",
        "",
    ]

    if i > 0:
        nav.append(f"[← Previous](papers_{i:02d}.md)")
    if i < n_pages - 1:
        nav.append(f"[Next →](papers_{i+2:02d}.md)")

    nav.extend([
        "",
        f"## Papers {start + 1}–{end}",
        "",
        "---",
        "",
    ])

    page_text = "\n".join(nav) + "\n\n".join(paper_sections[start:end])

    (OUTPUT_DIR / filename).write_text(page_text, encoding="utf-8")

print(f"Split {len(paper_sections)} papers into {n_pages} pages.")
print(f"Output written to: {OUTPUT_DIR}")
