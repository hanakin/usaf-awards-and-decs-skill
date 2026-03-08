#!/usr/bin/env python3
"""Search chunked AFH 33-337 chapter references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REF_DIR = SKILL_DIR / "references" / "AFH 33-337"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search AFH 33-337 chapter references.")
    parser.add_argument("pattern", help="Case-insensitive regex pattern.")
    parser.add_argument("--context", type=int, default=2, help="Lines of context before and after matches.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    regex = re.compile(args.pattern, re.IGNORECASE)
    found = False

    for path in sorted(REF_DIR.glob("chapter-*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        matches = [i for i, line in enumerate(lines) if regex.search(line)]
        if not matches:
            continue
        found = True
        print(f"## {path.name}")
        printed = set()
        for idx in matches:
            start = max(0, idx - args.context)
            end = min(len(lines), idx + args.context + 1)
            if any(i in printed for i in range(start, end)):
                continue
            for i in range(start, end):
                printed.add(i)
                marker = ">" if i == idx else " "
                print(f"{marker} {i + 1}: {lines[i]}")
            print()

    if not found:
        print("No matches found.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
