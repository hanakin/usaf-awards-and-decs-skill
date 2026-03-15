#!/usr/bin/env python3
"""Run the decoration split build + validation workflow."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BUILD_SCRIPT = SCRIPT_DIR / "build_decoration_splits.py"
VALIDATE_SCRIPT = SCRIPT_DIR / "validate_decoration_split_review.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build deterministic decoration splits, then validate the split-review "
            "table format and count math."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Year-tagged EPB text to process.")
    group.add_argument("--file", type=Path, help="UTF-8 EPB text file to process.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    build_cmd = ["python3", str(BUILD_SCRIPT)]
    if args.text is not None:
        build_cmd.extend(["--text", args.text])
    else:
        build_cmd.extend(["--file", str(args.file)])

    build_result = subprocess.run(build_cmd, capture_output=True, text=True)
    if build_result.stdout:
        print(build_result.stdout, end="")
    if build_result.stderr:
        print(build_result.stderr, file=sys.stderr, end="")

    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(build_result.stdout)

    validate_result = subprocess.run(
        ["python3", str(VALIDATE_SCRIPT), "--file", str(temp_path)],
        capture_output=True,
        text=True,
    )

    try:
        temp_path.unlink(missing_ok=True)
    except OSError:
        pass

    if validate_result.returncode != 0:
        if validate_result.stdout:
            print(validate_result.stdout, end="")
        if validate_result.stderr:
            print(validate_result.stderr, file=sys.stderr, end="")
        return validate_result.returncode

    if build_result.returncode != 0:
        return build_result.returncode

    print()
    print(validate_result.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
