#!/usr/bin/env python3
"""Return raw split guidance for one decoration source statement."""

from __future__ import annotations

import sys

import re

SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")


def split_sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_RE.split(text.strip()) if part.strip()]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: build_decoration_splits.py <E|L|M|I|H> <statement>", file=sys.stderr)
        return 2

    alq = sys.argv[1].upper()
    text = sys.argv[2].strip()

    if alq not in {"E", "L", "M", "I", "H"}:
        print("ALQ must be one of: E, L, M, I, H", file=sys.stderr)
        return 2

    if not text:
        print("statement is required", file=sys.stderr)
        return 2

    if alq == "H":
        print("SENTENCE_COUNT: 1")
        print(f"SPLIT 1: {text}")
        return 0

    sentences = split_sentences(text)
    print(f"SENTENCE_COUNT: {len(sentences)}")

    if len(sentences) == 1:
        print("EDGE_CASE: single-sentence run-on review required")
        print(f"SPLIT 1: {sentences[0]}")
        return 3

    if len(sentences) == 2:
        print(f"SPLIT 1: {sentences[0]}")
        print(f"SPLIT 2: {sentences[1]}")
        return 0

    if len(sentences) == 4:
        print(f"SPLIT 1: {sentences[0]} {sentences[1]}")
        print(f"SPLIT 2: {sentences[2]} {sentences[3]}")
        return 0

    for index, sentence in enumerate(sentences, start=1):
        print(f"SPLIT {index}: {sentence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
