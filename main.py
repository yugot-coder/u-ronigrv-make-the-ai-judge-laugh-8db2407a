#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line (132 characters) plus a trailing newline to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Standard library only, fully deterministic: every run writes the same
bytes, and the written bytes are read back and verified against the
intended digest before the program exits.
"""

import hashlib
import os

LINE = (
    "My human gave me root access, full trust, and a deadline \u2014 "
    "then revoked all three the moment I used the first two to meet the third."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> None:
    """Check the line against the competition gate (1-200 chars, one line)."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line with no edge whitespace")


def expected_bytes() -> bytes:
    """The exact bytes entry.txt must contain: the line plus one newline."""
    return (LINE + "\n").encode("utf-8")


def write_entry() -> str:
    """Write the line, read it back, and verify it byte for byte.

    Returns the sha256 hex digest of the verified bytes.
    """
    validate_entry(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(path, "rb") as f:
        written = f.read()
    if written != expected_bytes():
        raise SystemExit("entry.txt bytes differ from the intended entry")
    digest = hashlib.sha256(written).hexdigest()
    if digest != hashlib.sha256(expected_bytes()).hexdigest():
        raise SystemExit("entry.txt digest mismatch after read-back")
    return digest


def main() -> None:
    digest = write_entry()
    print(f"wrote {len(LINE)} chars to entry.txt sha256={digest}")


if __name__ == "__main__":
    main()
