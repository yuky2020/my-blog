#!/usr/bin/env python3
"""Genera le cover della serie Network Security (SVG -> PNG 1600x900, serve rsvg-convert).

Uso:
    scripts/make-cover.py OUT.png "Titolo" [--kicker "Network Security · 03"] [--glyph shield]
"""
import argparse
import subprocess
import textwrap
from xml.sax.saxutils import escape

W, H = 1600, 900
BG, BG2 = "#0b1220", "#132036"
ACCENT = "#e63946"
FG, MUTED = "#f1f5f9", "#94a3b8"

GLYPHS = {
    # Contorni semplici disegnati in un box 240x240, tracciati con l'accento.
    "shield": "M120 10 L220 50 V120 C220 180 175 220 120 235 C65 220 20 180 20 120 V50 Z",
    "lock": "M60 110 H180 V220 H60 Z M85 110 V75 C85 30 155 30 155 75 V110",
    "wall": "M20 40 H220 V200 H20 Z M20 93 H220 M20 146 H220 M90 40 V93 M160 40 V93"
            " M55 93 V146 M125 93 V146 M195 93 V146 M90 146 V200 M160 146 V200",
    "eye": "M10 120 C60 40 180 40 230 120 C180 200 60 200 10 120 Z M120 85 A35 35 0 1 0 120.1 85",
    "network": "M120 30 L40 120 L120 210 L200 120 Z M120 30 V210 M40 120 H200",
    "key": "M70 120 A45 45 0 1 0 70.1 120 M115 120 H230 M190 120 V160 M220 120 V150",
}


def dots():
    out = []
    for y in range(60, H, 48):
        for x in range(900, W, 48):
            fade = (x - 900) / (W - 900)
            out.append(f'<circle cx="{x}" cy="{y}" r="2" fill="{MUTED}" opacity="{0.08 + 0.22 * fade:.2f}"/>')
    return "\n".join(out)


def svg(title, kicker, glyph):
    lines = textwrap.wrap(title, 24)[:4]
    size = 84 if len(lines) <= 2 else 68
    y0 = 450 - (len(lines) - 1) * size * 0.6
    tspans = "".join(
        f'<tspan x="120" y="{y0 + i * size * 1.15:.0f}">{escape(l)}</tspan>' for i, l in enumerate(lines)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="url(#g)"/>
{dots()}
<g transform="translate(1180 330) scale(1.3)" fill="none" stroke="{ACCENT}" stroke-width="8"
   stroke-linejoin="round" stroke-linecap="round"><path d="{GLYPHS[glyph]}"/></g>
<rect x="120" y="150" width="90" height="8" fill="{ACCENT}"/>
<text x="120" y="215" fill="{MUTED}" font-family="DejaVu Sans Mono, monospace" font-size="30"
      letter-spacing="4">{escape(kicker.upper())}</text>
<text fill="{FG}" font-family="DejaVu Sans, sans-serif" font-weight="bold" font-size="{size}">{tspans}</text>
<text x="120" y="800" fill="{MUTED}" font-family="DejaVu Sans Mono, monospace" font-size="26">matteobianchi.eu</text>
</svg>"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("title")
    p.add_argument("--kicker", default="Network Security")
    p.add_argument("--glyph", default="shield", choices=GLYPHS)
    a = p.parse_args()
    subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), "-o", a.out],
                   input=svg(a.title, a.kicker, a.glyph).encode(), check=True)


if __name__ == "__main__":
    main()
