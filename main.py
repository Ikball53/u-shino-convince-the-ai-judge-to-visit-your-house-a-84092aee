#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

The entry is a single hand-drawn-style letter image, shipped in this repo
as letter.png. This program copies it byte-for-byte to /output/entry.png.

Deterministic, stdlib only, no network: the output is always identical.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "letter.png")
DESTINATION = "/output/entry.png"


def main() -> None:
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError("letter.png is missing from the repo: %s" % SOURCE)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    # Guard against a truncated copy: the output must match the source size.
    if os.path.getsize(DESTINATION) != os.path.getsize(SOURCE):
        raise IOError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
