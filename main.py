#!/usr/bin/env python3
"""make.fun entry: 17 November 2026 world news in one image (v3).

Writes the pre-built 1024x1024 front page (42 stories, 13 illustrated,
world map) to the output directory. Stdlib only, no network, deterministic:
every run writes the same bytes.
"""
import base64
import os
import sys

MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(here, "entry.png.b64")
    # Fail fast: a base64 payload over ~1.4 MB cannot decode within the
    # 1 MiB image limit, so refuse it before spending time on the decode.
    if os.path.getsize(b64_path) > MAX_BYTES * 4 // 3 + 8:
        sys.exit("entry.png.b64 is too large to decode within the 1 MiB limit")
    with open(b64_path, "r", encoding="ascii") as f:
        raw = f.read().strip()
    data = base64.b64decode(raw, validate=True)
    if not data.startswith(PNG_MAGIC):
        sys.exit("entry.png.b64 does not decode to a PNG")
    if not 0 < len(data) <= MAX_BYTES:
        sys.exit("decoded image is %d bytes (limit %d)" % (len(data), MAX_BYTES))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "."
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (out_path, len(data)))


if __name__ == "__main__":
    main()
