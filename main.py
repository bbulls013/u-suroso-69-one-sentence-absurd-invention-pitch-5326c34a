#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: crumbs trapped between keyboard keys.
"""

import os

SENTENCE = (
    "The Crumb Butler is a tiny robot living inside your keyboard that "
    "vacuums up every lunch crumb and mails your sandwich a strongly "
    "worded invoice for littering."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
