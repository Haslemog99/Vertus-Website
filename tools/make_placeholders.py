#!/usr/bin/env python3
"""Generate neutral SVG placeholder images for the Vertus alpha.

Each placeholder is labelled with the photo that should replace it (see plan §6).
Re-run any time: python3 tools/make_placeholders.py
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img")

# (filename, width, height, label, background, foreground)
SPECS = [
    ("hero-home",        1920, 1080, "PHOTO · Exterior at dusk (hero)",   "#2E4B42", "#EFE9E0"),
    ("exterior-day",     1200,  800, "PHOTO · Exterior, daytime",         "#C9BBA8", "#3A342C"),
    ("lobby",            1200,  800, "PHOTO · Lobby / reception",         "#D8CDBC", "#3A342C"),
    ("room-classic",     1200,  800, "PHOTO · Classic Room",              "#CFC2AE", "#3A342C"),
    ("room-deluxe",      1200,  800, "PHOTO · Deluxe Room",               "#C4B49E", "#3A342C"),
    ("room-suite",       1200,  800, "PHOTO · Suite",                     "#B9A98F", "#3A342C"),
    ("room-bathroom",    1200,  800, "PHOTO · Room bathroom",             "#DDD4C6", "#3A342C"),
    ("dining-restaurant",1200,  800, "PHOTO · Restaurant",                "#A89377", "#F5F0E8"),
    ("dining-bar",       1200,  800, "PHOTO · Bar",                       "#8F7A5E", "#F5F0E8"),
    ("dining-breakfast", 1200,  800, "PHOTO · Breakfast",                 "#C9B9A0", "#3A342C"),
    ("amenity-pool",     1200,  800, "PHOTO · Pool",                      "#9FAEA6", "#26302B"),
    ("amenity-gym",      1200,  800, "PHOTO · Gym",                       "#B3ABA0", "#33302B"),
    ("amenity-spa",      1200,  800, "PHOTO · Spa / wellness",            "#C6BBAE", "#33302B"),
    ("surroundings",     1200,  800, "PHOTO · Neighbourhood",             "#BDB49F", "#33302B"),
    ("map",              1200,  675, "MAP · Embed once address is known", "#E4DED2", "#4A4437"),
]

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="{w}" height="{h}" fill="{bg}"/>
  <rect x="24" y="24" width="{iw}" height="{ih}" fill="none" stroke="{fg}" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="10 8"/>
  <text x="50%" y="{ly}" fill="{fg}" fill-opacity="0.4" font-family="Georgia, serif" font-size="{fs}" text-anchor="middle" dominant-baseline="middle">{label}</text>
</svg>
"""

os.makedirs(OUT, exist_ok=True)
for name, w, h, label, bg, fg in SPECS:
    # Hero images sit behind centered page text, so their label goes near the top
    label_y = "22%" if name.startswith("hero") else "50%"
    svg = SVG.format(w=w, h=h, iw=w - 48, ih=h - 48, bg=bg, fg=fg, fs=max(28, w // 34), label=label, ly=label_y)
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(svg)
    print(f"wrote assets/img/{name}.svg")
