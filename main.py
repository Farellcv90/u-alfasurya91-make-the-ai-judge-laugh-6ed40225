#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, one line, under 200 characters.

Writes the entry line to /output/entry.txt with no trailing newline.
"""

import os

JOKE = "The office printer never jams on junk mail — it waits for the one urgent document, then eats it like it's up for promotion."

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, a single line, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line):
    """Check one candidate entry line against the gate; return the line."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    line = validate(JOKE.strip())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
