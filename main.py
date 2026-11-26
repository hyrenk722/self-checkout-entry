"""Life Choices in the Returns Queue — entry for The Self-Checkout Is Judging You.

make.fun competition u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.
Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

LINE = "Please place your twelve yoghurts in the bagging area, and your life choices in the returns queue."

MAX_CHARS = 200


def check_gate(line):
    """The competition gate: one line, 1..200 chars, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, gate allows 1..200")
    if not line.strip():
        raise ValueError("entry must not be blank")
    return line


def main():
    line = check_gate(LINE)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    back = out.read_text(encoding="utf-8")
    if back != line:
        raise ValueError("round-trip mismatch: entry.txt differs from LINE")


if __name__ == "__main__":
    main()
