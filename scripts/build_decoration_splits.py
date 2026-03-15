#!/usr/bin/env python3
"""Build decoration split rows from year-tagged EPB input.

This helper is intentionally conservative:
- `H` always stays whole
- `E/L/M/I` with 2 sentences auto-split into 2 rows
- `E/L/M/I` with 4 sentences auto-split into `1+2` and `3+4`
- single-sentence run-ons and other nonstandard cases are flagged for manual review

The goal is to automate the deterministic cases and leave edge cases to review.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ALQS = ("E", "L", "M", "I", "H")
EPB_RE = re.compile(r"^EPB\s*(\d{2,4})\s*:\s*$", re.IGNORECASE)
ALQ_RE = re.compile(r"^([ELMIH])\s*:\s*$")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
TRANSITION_RE = re.compile(r"^(Also|Additionally|Moreover|Furthermore|Finally)\b[\s,]*", re.IGNORECASE)
EDGE_RESULT_RE = re.compile(r"^(This|That|These|It)\b", re.IGNORECASE)
NEW_ACCOMPLISHMENT_RE = re.compile(
    r"^(He|She|They|Peter|Snuffy|SrA|SSgt|TSgt|MSgt)\b", re.IGNORECASE
)


@dataclass
class SourceEntry:
    year: str
    alq: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build conservative decoration splits from year-tagged EPB input."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="EPB text to parse.")
    group.add_argument("--file", type=Path, help="UTF-8 EPB text file to parse.")
    return parser.parse_args()


def load_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    try:
        return args.file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {args.file}", file=sys.stderr)
        raise SystemExit(1)


def normalize_year(year: str) -> str:
    return year[-2:]


def parse_entries(text: str) -> list[SourceEntry]:
    entries: list[SourceEntry] = []
    current_year: str | None = None
    current_alq: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        epb_match = EPB_RE.match(line)
        if epb_match:
            current_year = normalize_year(epb_match.group(1))
            current_alq = None
            continue

        alq_match = ALQ_RE.match(line)
        if alq_match:
            current_alq = alq_match.group(1)
            continue

        if line.startswith("-"):
            if current_year is None or current_alq is None:
                raise ValueError(f"Bullet outside EPB/ALQ context: {line}")
            text_value = line[1:].strip()
            entries.append(SourceEntry(current_year, current_alq, text_value))

    return entries


def split_sentences(text: str) -> list[str]:
    parts = [part.strip() for part in SENTENCE_SPLIT_RE.split(text.strip()) if part.strip()]
    return parts


def opener_repair(text: str) -> str:
    text = TRANSITION_RE.sub("", text).strip()
    return text


def is_four_sentence_edge_case(sentences: list[str]) -> bool:
    if len(sentences) != 4:
        return False
    third = sentences[2].strip()
    fourth = sentences[3].strip()
    return bool(EDGE_RESULT_RE.match(third) and NEW_ACCOMPLISHMENT_RE.match(fourth))


def auto_split(entry: SourceEntry) -> tuple[list[str], str | None]:
    if entry.alq == "H":
        return [entry.text], None

    sentences = split_sentences(entry.text)

    if len(sentences) == 2:
        return [sentences[0], opener_repair(sentences[1])], None

    if len(sentences) == 4:
        if is_four_sentence_edge_case(sentences):
            return [], "manual review: 4-sentence 3+1 edge case"
        return [
            f"{sentences[0]} {sentences[1]}",
            opener_repair(f"{sentences[2]} {sentences[3]}"),
        ], None

    if len(sentences) == 1:
        return [], "manual review: single-sentence run-on or unsplittable one-sentence entry"

    return [], f"manual review: unsupported sentence count ({len(sentences)})"


def main() -> int:
    args = parse_args()
    text = load_text(args)

    try:
        entries = parse_entries(text)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print("Split Review")
    print()
    print("| Split # | EPB Ref | Merged ID | Split |")
    print("|---|---|---|---|")

    split_num = 1
    manual_flags: list[str] = []
    per_ref_counts: dict[str, int] = {}

    for entry in entries:
        epb_ref = f"{entry.alq}{entry.year}"
        splits, flag = auto_split(entry)
        if flag:
            manual_flags.append(f"{epb_ref}: {flag}")
            continue

        per_ref_counts[epb_ref] = len(splits)
        for split in splits:
            print(f"| {split_num} | {epb_ref} |  | {split} |")
            split_num += 1

    print()
    print("Proposed Merges")
    print()
    print("- None yet")
    print()
    print("Review Needed")
    print("- Valid merges:")
    print("- Invalid merges:")
    print("- Missing merges:")

    if manual_flags:
        print()
        print("Manual review required:")
        for flag in manual_flags:
            print(f"- {flag}")

    return 0 if not manual_flags else 3


if __name__ == "__main__":
    raise SystemExit(main())
