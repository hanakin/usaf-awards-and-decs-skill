#!/usr/bin/env python3
"""Count text exactly for USAF writing constraints.

Counts every character in the provided string, including letters, digits,
spaces, tabs, newlines, punctuation, symbols, and other special characters.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Return the exact character count for a string or file. "
            "Counts all characters, including whitespace and symbols."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to count exactly.")
    group.add_argument("--file", type=Path, help="Path to a UTF-8 text file to count exactly.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.text is not None:
        text = args.text
    else:
        try:
            text = args.file.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"File not found: {args.file}", file=sys.stderr)
            return 1

    print(len(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
