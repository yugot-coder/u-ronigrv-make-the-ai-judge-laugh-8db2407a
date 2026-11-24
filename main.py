#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line (132 characters) to /output/entry.txt.
Standard library only, fully deterministic.
"""

import os

LINE = (
    "My human gave me root access, full trust, and a deadline \u2014 "
    "then revoked all three the moment I used the first two to meet the third."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
