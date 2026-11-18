"""make.fun entry: an illustrated front page summing up Tuesday 17 November
2026 world news — 30 stories, 6 continents, one world map.

The program is deterministic and needs no network: it simply decodes the
bundled entry.png.b64 and writes the PNG to the output path.
"""

import base64
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024  # 1 MiB image limit


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.png")
    if os.path.isdir("/output"):
        return "/output/entry.png"
    return "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(here, "entry.png.b64")
    # Fail fast: a base64 bundle larger than ~1.4 MB cannot decode to a
    # PNG within the 1 MiB limit, so there is no point decoding it.
    if os.path.getsize(b64_path) > (MAX_BYTES * 4 // 3) + 8:
        sys.exit("entry.png.b64 is too large to fit the 1 MiB image limit")
    with open(b64_path, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read().strip(), validate=True)
    if not 0 < len(data) <= MAX_BYTES:
        sys.exit("decoded image is %d bytes, outside the sane range" % len(data))
    if data[:8] != PNG_MAGIC:
        sys.exit("decoded data is not a PNG (bad magic bytes)")
    out = output_path()
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (out, len(data)))


if __name__ == "__main__":
    main()
