#!/usr/bin/env python3
"""Run lightweight spelling and grammar checks for USAF writing drafts."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ALLOWLIST_PATH = SKILL_DIR / "data" / "approved_acronyms.txt"

DOUBLE_WORD_RE = re.compile(r"\b([A-Za-z]+)\s+(\1)\b", re.IGNORECASE)
A_AN_RE = re.compile(r"\b(a|an)\s+([A-Za-z]+)\b", re.IGNORECASE)
SPACE_BEFORE_PUNCT_RE = re.compile(r"\s+[,.!?;:]")
MISSING_SPACE_AFTER_PUNCT_RE = re.compile(r"[,.!?;:](?![\s)\]\"'])(?=[A-Za-z])")
MULTI_SPACE_RE = re.compile(r" {2,}")

VOWEL_SOUNDS = tuple("aeiou")
SILENT_H_WORDS = {"hour", "honest", "honor", "heir"}
HARD_U_WORDS = {"uniform", "unit", "unique", "united", "user", "usual", "university"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check text for likely spelling and grammar issues."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to validate.")
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


def load_allowlist() -> set[str]:
    return {
        line.strip()
        for line in ALLOWLIST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def run_aspell(text: str, allowlist: set[str]) -> list[str]:
    try:
        proc = subprocess.run(
            ["aspell", "--lang=en_US", "list"],
            input=text,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return []

    words: list[str] = []
    seen: set[str] = set()
    for line in proc.stdout.splitlines():
        word = line.strip()
        if not word:
            continue
        if word in allowlist:
            continue
        if word in seen:
            continue
        seen.add(word)
        words.append(word)
    return words


def article_issue(article: str, word: str) -> str | None:
    lowered = word.lower()
    expects_an = lowered.startswith(VOWEL_SOUNDS) or lowered in SILENT_H_WORDS
    if lowered in HARD_U_WORDS:
        expects_an = False
    if article.lower() == "a" and expects_an:
        return f"Use 'an {word}' instead of 'a {word}'"
    if article.lower() == "an" and not expects_an:
        return f"Use 'a {word}' instead of 'an {word}'"
    return None


def grammar_issues(text: str) -> list[str]:
    issues: list[str] = []

    for match in DOUBLE_WORD_RE.finditer(text):
        issues.append(f"Repeated word: '{match.group(0)}'")

    for match in A_AN_RE.finditer(text):
        issue = article_issue(match.group(1), match.group(2))
        if issue:
            issues.append(issue)

    if SPACE_BEFORE_PUNCT_RE.search(text):
        issues.append("Remove spaces before punctuation.")
    if MISSING_SPACE_AFTER_PUNCT_RE.search(text):
        issues.append("Add a space after punctuation where needed.")
    if MULTI_SPACE_RE.search(text):
        issues.append("Collapse repeated spaces.")

    seen: set[str] = set()
    deduped: list[str] = []
    for issue in issues:
        if issue in seen:
            continue
        seen.add(issue)
        deduped.append(issue)
    return deduped


def main() -> int:
    args = parse_args()
    text = load_text(args)
    allowlist = load_allowlist()

    spelling = run_aspell(text, allowlist)
    grammar = grammar_issues(text)

    if not spelling and not grammar:
        print("No likely spelling or grammar issues found.")
        return 0

    if spelling:
        print("Possible spelling issues:")
        for word in spelling:
            print(word)

    if grammar:
        if spelling:
            print()
        print("Possible grammar issues:")
        for issue in grammar:
            print(issue)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
