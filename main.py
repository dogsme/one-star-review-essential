#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of the sun to
/output/entry.txt, one line, 160 characters or fewer.
"""

import os

REVIEW = "The sun shines straight into my eyes every morning and clocks off before I finish work. One star. Terrible opening hours."


def main():
    text = REVIEW.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError("review must be 1 to 160 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
