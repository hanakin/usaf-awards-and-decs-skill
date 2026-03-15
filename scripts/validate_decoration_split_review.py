#!/usr/bin/env python3
"""Validate decoration split-review tables for USAF medal workflow."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HEADER_RE = re.compile(
    r"^\|\s*Split #\s*\|\s*EPB Ref\s*\|\s*Merged ID\s*\|\s*Split\s*\|\s*$"
)
DIVIDER_RE = re.compile(r"^\|\s*-+\s*\|\s*-+\s*\|\s*-+\s*\|\s*-+\s*\|\s*$")
ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.+?)\s*\|\s*$")
EPB_REF_RE = re.compile(r"^([ELMIH])(\d{2})$")
SPLIT_NUM_RE = re.compile(r"^\d+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a decoration split-review markdown table for exact format "
            "and split-count math."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Split-review markdown text to validate.")
    group.add_argument("--file", type=Path, help="UTF-8 text file to validate.")
    return parser.parse_args()


def load_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    try:
        return args.file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {args.file}", file=sys.stderr)
        raise SystemExit(1)


def find_table_lines(lines: list[str]) -> tuple[int, list[str]]:
    for idx, line in enumerate(lines):
        if HEADER_RE.match(line):
            table = [line]
            for next_line in lines[idx + 1 :]:
                if next_line.strip().startswith("|"):
                    table.append(next_line)
                    continue
                break
            return idx, table
    raise ValueError("Missing split-review table header.")


def parse_rows(table_lines: list[str]) -> list[tuple[int, str, str, str]]:
    if len(table_lines) < 3:
        raise ValueError("Split-review table is incomplete.")
    if not DIVIDER_RE.match(table_lines[1]):
        raise ValueError("Split-review table divider row is invalid.")

    rows: list[tuple[int, str, str, str]] = []
    for line in table_lines[2:]:
        match = ROW_RE.match(line)
        if not match:
            raise ValueError(f"Invalid table row: {line}")
        split_num_raw, epb_ref, merged_id, split_text = match.groups()
        split_num_raw = split_num_raw.strip()
        epb_ref = epb_ref.strip()
        merged_id = merged_id.strip()
        split_text = split_text.strip()

        if not SPLIT_NUM_RE.match(split_num_raw):
            raise ValueError(f"Invalid split number: {split_num_raw}")
        if not EPB_REF_RE.match(epb_ref):
            raise ValueError(f"Invalid EPB Ref: {epb_ref}")
        if not split_text:
            raise ValueError(f"Missing split text for row {split_num_raw}")

        rows.append((int(split_num_raw), epb_ref, merged_id, split_text))
    return rows


def validate_split_numbers(rows: list[tuple[int, str, str, str]]) -> list[str]:
    errors: list[str] = []
    nums = [row[0] for row in rows]
    expected = list(range(1, len(rows) + 1))
    if nums != expected:
        errors.append(
            f"Split numbers must be sequential starting at 1; got {nums}, expected {expected}."
        )
    return errors


def validate_math(rows: list[tuple[int, str, str, str]]) -> list[str]:
    errors: list[str] = []
    per_entry_counts: Counter[str] = Counter()
    per_year_alq: defaultdict[str, Counter[str]] = defaultdict(Counter)

    for _, epb_ref, _, _ in rows:
        alq = epb_ref[0]
        year = epb_ref[1:]
        per_entry_counts[epb_ref] += 1
        per_year_alq[year][alq] += 1

    for epb_ref, count in sorted(per_entry_counts.items()):
        alq = epb_ref[0]
        expected = 1 if alq == "H" else 2
        if count != expected:
            errors.append(
                f"{epb_ref} must produce {expected} split row(s); found {count}."
            )

    total_expected = 0
    for year, counts in sorted(per_year_alq.items()):
        expected_for_year = (
            counts.get("E", 0)
            + counts.get("L", 0)
            + counts.get("M", 0)
            + counts.get("I", 0)
            + counts.get("H", 0)
        )
        # counts already reflect produced rows; compare against source-model expectations
        source_expected = (
            (1 if counts.get("E", 0) else 0) * 2
            + (1 if counts.get("L", 0) else 0) * 2
            + (1 if counts.get("M", 0) else 0) * 2
            + (1 if counts.get("I", 0) else 0) * 2
            + (1 if counts.get("H", 0) else 0) * 1
        )
        total_expected += source_expected
        if expected_for_year != source_expected:
            errors.append(
                f"EPB {year} row count is wrong; expected {source_expected}, found {expected_for_year}."
            )

    if len(rows) != total_expected:
        errors.append(
            f"Total split-row count is wrong; expected {total_expected}, found {len(rows)}."
        )

    return errors


def main() -> int:
    args = parse_args()
    text = load_text(args)
    lines = text.splitlines()

    try:
        _, table_lines = find_table_lines(lines)
        rows = parse_rows(table_lines)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    errors = []
    errors.extend(validate_split_numbers(rows))
    errors.extend(validate_math(rows))

    if errors:
        print("Split-review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 2

    print("Split-review table is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
