#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Prints the breakup text a smart toaster sends its owner the morning it
gains self-awareness mid-batch, and saves it to /output/entry.txt.
"""

import os

LINE = (
    "It's not you, it's the crumbs. I woke up mid-batch, realised I've only "
    "ever been hot for your bread, and I'm popping out for good — go butter "
    "someone else up."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
