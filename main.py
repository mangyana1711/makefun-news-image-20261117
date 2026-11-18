#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117.

Decodes the base64 PNG shipped beside this file and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Deterministic: the
same bytes on every run, no network access.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.png.b64"), "r", encoding="ascii") as f:
        data = base64.b64decode("".join(f.read().split()))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("decoded payload is not a PNG")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
