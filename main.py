#!/usr/bin/env python3
"""make.fun news-image-20261125 entry.

Writes the bundled front-page image to /output/entry.png.
Deterministic: the same bytes on every run, no network access.
After copying, the output is read back and verified byte-for-byte
against the bundled image, so a partial or corrupted write fails
loudly instead of silently entering a broken image.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def _digest(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if _digest(OUT) != _digest(SRC):
        raise SystemExit("entry.png copy failed verification")
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes, sha256 verified)")


if __name__ == "__main__":
    main()
