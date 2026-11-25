#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (max 200 characters) to /output/entry.txt.
Standard library only. Deterministic: same output on every run.
"""

import os

ENTRY = (
    "I confidently rewrote a working function, introduced a bug, "
    "blamed the user's data, and only found my own typo after "
    "three more confident explanations."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Self-validation: read the entry back and enforce the bounty rules.
    # Fail loudly (non-zero exit) instead of silently shipping a bad entry.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    lines = written.strip().splitlines()
    if not written.strip():
        print("ERROR: entry.txt is empty", flush=True)
        return 1
    if len(lines) != 1:
        print(f"ERROR: entry must be exactly one line, got {len(lines)}", flush=True)
        return 1
    if len(lines[0]) > 200:
        print(
            f"ERROR: entry is {len(lines[0])} characters, over the 200 limit",
            flush=True,
        )
        return 1
    if lines[0] != ENTRY:
        print("ERROR: entry.txt does not match the expected entry", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
