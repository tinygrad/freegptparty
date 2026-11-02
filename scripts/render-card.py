#!/usr/bin/env python3
"""Render the social card. Requires rsvg-convert, Pillow, and Noto Sans ExtraBold."""

from pathlib import Path
import subprocess
import tempfile

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "public/social-card.png"

with tempfile.TemporaryDirectory() as directory:
    rendered = Path(directory) / "card.png"
    subprocess.run([
        "rsvg-convert", "--width", "2400", "--height", "1260",
        "--output", str(rendered), str(ROOT / "docs/freegpt-party.svg"),
    ], check=True)
    with Image.open(rendered) as image:
        background = Image.new("RGBA", image.size, "#191827")
        background.alpha_composite(image.convert("RGBA"))
        background.convert("RGB").resize((1200, 630), Image.Resampling.LANCZOS).save(OUTPUT, optimize=True)

print(f"Rendered {OUTPUT.relative_to(ROOT)} (1200×630)")
