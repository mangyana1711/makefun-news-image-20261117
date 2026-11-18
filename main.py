#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117 (v2, illustrated front page).

Writes the 17 November 2026 world-news front page to entry.png by decoding
the base64 image stored beside this file. Standard library only, no network.
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.png")
    if os.path.isdir("/output"):
        return "/output/entry.png"
    return os.path.join(HERE, "entry.png")


def main():
    with open(os.path.join(HERE, "entry.png.b64"), "r") as f:
        data = base64.b64decode(f.read())
    if not data.startswith(PNG_MAGIC):
        sys.exit("decoded entry.png.b64 is not a PNG image")
    if len(data) > 1048576:
        sys.exit("decoded image exceeds the 1 MiB limit")
    out = output_path()
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)
    print("wrote", out, len(data), "bytes")


if __name__ == "__main__":
    main()
