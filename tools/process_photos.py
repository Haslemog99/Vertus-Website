#!/usr/bin/env python3
"""Convert incoming Vertus photos to WebP and place them in assets/img.

Mapping is based on a visual pass of the 32 JPGs dropped into incoming/.
Re-run after adding/replacing photos in the mapping below.
"""
from __future__ import annotations

import os
from PIL import Image

SRC = os.path.join(os.path.dirname(__file__), "..", "incoming", "Vertus Hotel ")
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img")

# dest stem (no ext) -> source filename
MAP = {
    # Exterior / lobby
    "hero-home": "IMG_1775.JPG",
    "exterior-day": "IMG_1775.JPG",
    "lobby": "IMG_1749.JPG",
    "lobby-detail": "IMG_1750.JPG",
    # Classic room
    "room-classic": "IMG_1773.JPG",
    "room-classic-2": "IMG_1752.JPG",
    "room-classic-3": "IMG_1772.JPG",
    # Deluxe room
    "room-deluxe": "IMG_1765.JPG",
    "room-deluxe-2": "IMG_1769.JPG",
    "room-deluxe-3": "IMG_1778.JPG",
    # Suite
    "room-suite": "IMG_1770.JPG",
    "room-suite-2": "IMG_1766.JPG",
    "room-suite-3": "IMG_1768.JPG",
    # Bathrooms
    "room-bathroom": "IMG_1753.JPG",
    "room-bathroom-2": "IMG_1754.JPG",
    "room-bathroom-3": "IMG_1759.JPG",
    # Extra room angles (gallery)
    "room-extra-1": "IMG_1751.JPG",
    "room-extra-2": "IMG_1755.JPG",
    "room-extra-3": "IMG_1758.JPG",
    "room-extra-4": "IMG_1760.JPG",
    "room-extra-5": "IMG_1762.JPG",
    "room-extra-6": "IMG_1763.JPG",
    "room-extra-7": "IMG_1776.JPG",
    "room-extra-8": "IMG_1777.JPG",
    "room-extra-9": "IMG_1779.JPG",
    # Dining / bar
    "dining-restaurant": "IMG_1782.JPG",
    "dining-restaurant-2": "IMG_1783.JPG",
    "dining-bar": "IMG_1785.JPG",
    "dining-bar-2": "IMG_1787.JPG",
    "dining-bar-3": "IMG_1784.JPG",
    "dining-lounge": "IMG_1786.JPG",
    # Pool
    "amenity-pool": "IMG_1780.JPG",
    "amenity-pool-2": "IMG_1781.JPG",
}

# Max edge for web delivery (hero gets a wider budget)
MAX = {
    "hero-home": 1920,
    "exterior-day": 1600,
}


def convert(src_name: str, dest_stem: str) -> None:
    src_path = os.path.join(SRC, src_name)
    if not os.path.isfile(src_path):
        raise SystemExit(f"missing source: {src_path}")
    im = Image.open(src_path)
    im = im.convert("RGB")
    max_edge = MAX.get(dest_stem, 1400)
    im.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
    out_path = os.path.join(OUT, f"{dest_stem}.webp")
    im.save(out_path, "WEBP", quality=82, method=4)
    print(f"{src_name} -> {dest_stem}.webp ({im.size[0]}x{im.size[1]})")


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for dest, src in MAP.items():
        convert(src, dest)
    # Remove obsolete SVG placeholders that now have real photos
    for obsolete in (
        "hero-home.svg", "exterior-day.svg", "lobby.svg",
        "room-classic.svg", "room-deluxe.svg", "room-suite.svg", "room-bathroom.svg",
        "dining-restaurant.svg", "dining-bar.svg", "dining-breakfast.svg",
        "amenity-pool.svg", "amenity-gym.svg", "amenity-spa.svg", "surroundings.svg",
    ):
        path = os.path.join(OUT, obsolete)
        if os.path.isfile(path):
            os.remove(path)
            print(f"removed {obsolete}")


if __name__ == "__main__":
    main()
