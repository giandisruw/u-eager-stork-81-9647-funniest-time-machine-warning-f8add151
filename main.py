#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
/output/entry.txt. Standard library only, no network, no API key.
"""

import os

LABEL = "WARNING: Do not operate while pregnant. You may give birth to yourself."


def main() -> None:
    # Gate self-check: one line, 1-120 characters, non-whitespace.
    assert "\n" not in LABEL and 1 <= len(LABEL) <= 120, "label fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
