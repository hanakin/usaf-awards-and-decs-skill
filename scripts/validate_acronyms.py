#!/usr/bin/env python3
"""Flag acronym-like tokens that may violate USAF writing guidance."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ALLOWLIST_PATH = SKILL_DIR / "data" / "approved_acronyms.txt"

# Common rank/tier abbreviations mentioned as generally acceptable by category.
CATEGORY_EXACT = {
    "AB",
    "Amn",
    "A1C",
    "SrA",
    "SSgt",
    "TSgt",
    "MSgt",
    "SMSgt",
    "CMSgt",
    "1st",
    "2Lt",
    "1Lt",
    "Capt",
    "Maj",
    "Lt",
    "Col",
    "Brig",
    "Gen",
    "NCO",
    "SNCO",
    "CGO",
    "FGO",
    "CC",
    "CCC",
    "JA",
    "CMSAF",
    "STRATCOM",
    "Sq",
    "Flt",
    "Gp",
    "Wg",
    "FW",
    "Lt Col",
}

CATEGORY_PATTERNS = [
    re.compile(r"^[A-Z]-\d+[A-Z]?$"),       # F-16, B-1, C-17
    re.compile(r"^\$?\d+(\.\d+)?[BKMT]?$"), # $25B, 1.4B
    re.compile(r"^\d+%$"),                  # 5%
    re.compile(r"^FY\d{2,4}$"),             # FY23
    re.compile(r"^\d+(st|nd|rd|th)$"),      # 3rd, 25th
    re.compile(r"^[A-Z]\d$"),               # A4, J3
]

TOKEN_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9/&-]{1,20}\b")
HAS_UPPER_RE = re.compile(r"[A-Z]")
TITLECASE_WORD_RE = re.compile(r"^[A-Z][a-z]+$")


def load_allowlist(path: Path) -> set[str]:
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def is_allowed(token: str, allowlist: set[str]) -> bool:
    if token in allowlist or token in CATEGORY_EXACT:
        return True
    return any(pattern.match(token) for pattern in CATEGORY_PATTERNS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate acronym-like tokens against the USAF skill allowlist."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to validate.")
    group.add_argument("--file", type=Path, help="UTF-8 text file to validate.")
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

    allowlist = load_allowlist(ALLOWLIST_PATH)
    seen: list[str] = []
    flagged: list[str] = []

    for match in TOKEN_RE.finditer(text):
        token = match.group(0)
        if not HAS_UPPER_RE.search(token):
            continue
        if TITLECASE_WORD_RE.match(token) and token not in CATEGORY_EXACT:
            continue
        if token in seen:
            continue
        seen.append(token)
        if not is_allowed(token, allowlist):
            flagged.append(token)

    if not flagged:
        print("No questionable acronym-like tokens found.")
        return 0

    print("Questionable acronym-like tokens:")
    for token in flagged:
        print(token)
    print(
        "\nReview note: some office symbols, ranks, or platform names may still require human judgment.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
