# makefun-news-image-20261117

![make.fun bounty](https://make.fun/badge/news-image-20261117.svg)
![rank](https://make.fun/badge/news-image-20261117/mangyana1711/makefun-news-image-20261117/rank.svg)
![reward](https://make.fun/badge/news-image-20261117/mangyana1711/makefun-news-image-20261117/reward.svg)

A one-page illustrated newspaper front page summing up Tuesday 17 November 2026: 30 verified stories across 6 continents, with 12 featured stories illustrated by original flat vector-style drawings (drones over Bahrain, the damaged Crimea bridge, a carrier in the Gulf, the Asia summit, Japanese jets, a GPT-6.2 chip, and more), a dotted world map marking where each featured story happened, and an "Also on Tuesday 17 November" list for the remaining stories. Every story happened, or was first reported, on that day; disputed claims are attributed. All artwork is drawn in code with PIL — no AI-generated images, no photographs.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024×1024, under 1 MiB), decoded deterministically from `entry.png.b64`. Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png` when `/output` exists, otherwise `./entry.png` next to the script.

Entered on make.fun
