#!/usr/bin/env python3
"""Build chunked chapter references for AFH 33-337 from fixed PDF page ranges."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
OUT_DIR = SKILL_DIR / "references" / "AFH 33-337"

# The printed handbook page number to PDF page number offset for this source file.
PDF_PAGE_OFFSET = 8

CHAPTERS = [
    (1, "A Basic Philosophy of Communication", 3),
    (2, "Seven Steps to Effective Communication (Overview)", 8),
    (3, "Step 1 (Analyze Purpose and Audience)", 15),
    (4, "Step 2 (Research Your Topic)", 23),
    (5, "Step 3 (Support Your Ideas)", 41),
    (6, "Step 4 (Organize and Outline)", 53),
    (7, "Step 5 (Draft)", 65),
    (8, "Step 6 (Edit)", 91),
    (9, "Step 7 (Fight for Feedback and Get Approval)", 103),
    (10, "Air Force Speaking", 111),
    (11, "Effective Listening Strategies", 123),
    (12, "Electronic Communications and Social Media", 133),
    (13, "Meetings", 153),
    (14, "The Official Memorandum", 163),
    (15, "The Personal Letter", 191),
    (16, "Air Force Papers", 219),
    (17, "The Staff Study", 229),
    (18, "The Staff Package", 237),
    (19, "Writing Better Bullet Statements", 247),
    (20, "The Official Biography", 257),
    (21, "The Resume", 265),
    (22, "Envelopes and Mail", 275),
    (23, "Air Force Publications/Forms", 283),
    (24, "Writing Terminology", 287),
    (25, "Punctuation", 295),
    (26, "Abbreviations", 331),
    (27, "Capitalization", 341),
    (28, "Numbers", 355),
]


def slugify(text: str) -> str:
    text = text.lower()
    text = text.replace("resume", "resume")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def clean_text(text: str) -> str:
    text = text.replace("\f", "\n")
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped.startswith("The Tongue and Quill"):
            continue
        if re.fullmatch(r"AFH\s+33-337,?\s+27 MAY 2015", stripped):
            continue
        if re.fullmatch(r"AFH 337, 27 MAY 2015", stripped):
            continue
        lines.append(line)
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def extract_pages(pdf_path: Path, start_page: int, end_page: int) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", "-f", str(start_page), "-l", str(end_page), str(pdf_path), "-"],
        check=True,
        capture_output=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def write_index() -> None:
    lines = [
        "# AFH 33-337",
        "",
        "Chunked chapter references for `The Tongue and Quill`.",
        "",
        "Use `scripts/search_tongue_and_quill.py` or `rg` to find specific guidance before loading a chapter file.",
        "",
        "## Chapters",
        "",
    ]
    for chapter_num, chapter_title, _ in CHAPTERS:
        filename = f"chapter-{chapter_num:02d}-{slugify(chapter_title)}.md"
        lines.append(f"- [{filename}](./{filename})")
    lines.append("")
    (OUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_chapters(pdf_path: Path) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in OUT_DIR.glob("chapter-*.md"):
        old_file.unlink()
    index_file = OUT_DIR / "index.md"
    if index_file.exists():
        index_file.unlink()

    for idx, (chapter_num, chapter_title, printed_start) in enumerate(CHAPTERS):
        next_printed_start = CHAPTERS[idx + 1][2] if idx + 1 < len(CHAPTERS) else 370
        pdf_start = printed_start + PDF_PAGE_OFFSET
        pdf_end = next_printed_start + PDF_PAGE_OFFSET - 1
        raw = extract_pages(pdf_path, pdf_start, pdf_end)
        body = clean_text(raw)
        filename = OUT_DIR / f"chapter-{chapter_num:02d}-{slugify(chapter_title)}.md"
        content = f"# Chapter {chapter_num}: {chapter_title}\n\n{body}"
        filename.write_text(content, encoding="utf-8")

    write_index()


def main() -> int:
    pdf_path = Path(
        "/Users/hanakin/Library/Mobile Documents/com~apple~CloudDocs/Sites/pdf-md/pdfs/afh33-337.pdf"
    )
    write_chapters(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
