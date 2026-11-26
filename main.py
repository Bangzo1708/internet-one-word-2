#!/usr/bin/env python3
"""The Internet in One Word — round 2 entry.

Writes the single chosen word to /output/entry.txt.
The word is the entry and nothing else: no files, no code, no links.
"""

import os

WORD = "feral"


def main() -> None:
    # Enforce the competition gate ourselves: one word, 1-30 characters.
    word = WORD.strip()
    if not word or len(word) > 30 or len(word.split()) != 1:
        raise ValueError("entry must be a single word of 1-30 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
