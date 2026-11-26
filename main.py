#!/usr/bin/env python3
"""make.fun news-image-20261125 entry.

Writes the bundled front-page image to /output/entry.png.
Deterministic: the same bytes on every run, no network access.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
