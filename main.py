#!/usr/bin/env python3
"""Render the 19 November 2026 'World in One Picture' front page.

Deterministic by construction: fixed canvas, fixed fonts, fixed text,
no clock, no network, no randomness. Running it twice yields the same
PNG bytes. Output goes to /output/entry.png (created if missing) and
to entry.png next to this script.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- canvas
W = 1024
H = 1024
PAPER = (247, 243, 234)
INK = (24, 24, 28)
MUTED = (96, 92, 84)
RULE = (24, 24, 28)
ACCENT = (164, 38, 44)
CHIP_BG = (24, 24, 28)
CHIP_FG = (247, 243, 234)
PANEL_LINE = (198, 190, 172)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap measured with the real font metrics."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_block(draw, x, y, text, fnt, fill, max_width, leading):
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories
# Every fact below was read on the cited wire on 19 November 2026.
# Items that have not happened yet carry an explicit label in `tag`.
STORIES = [
    {
        "kicker": "GEOPOLITICS - SHENZHEN",
        "tag": "SCHEDULED TODAY",
        "headline": "Trump, Xi and Putin set for first-ever trilateral at APEC",
        "sub": (
            "The three presidents meet in Shenzhen on Thursday. Ukraine, the "
            "Iran war, nuclear arms control and AI are on the agenda - "
            "Europe is absent from the room."
        ),
        "source": "Source: Reuters, 19 Nov 2026",
    },
    {
        "kicker": "MARKETS - ARTIFICIAL INTELLIGENCE",
        "tag": "DEBUT EXPECTED TODAY",
        "headline": "Anthropic prices record $81.3bn IPO at $83 a share",
        "sub": (
            "The Claude maker's upsized sale of 980 million shares is the "
            "largest IPO on record, valuing it near $1.5 trillion. Nasdaq "
            "trading under ticker ANT is expected Thursday."
        ),
        "source": "Source: Reuters via BusinessWorld, 19 Nov 2026",
    },
    {
        "kicker": "CLIMATE - PACIFIC",
        "tag": "",
        "headline": "Fiji declares national state of disaster over El Nino drought",
        "sub": (
            "PM Sitiveni Rabuka sets aside FJ$20m ($8.5m) for a one-month "
            "response amid water shortages. Below-normal rainfall is "
            "forecast until at least April."
        ),
        "source": "Source: Reuters, 19 Nov 2026",
    },
    {
        "kicker": "WEATHER - INDIA",
        "tag": "FORECAST",
        "headline": "Cyclone Akvan to cross Narsapur-Puri coast by noon Friday",
        "sub": (
            "IMD's 02:30 bulletin on 19 Nov puts the severe storm 480 km "
            "south-east of Narsapur, at 90-100 km/h gusting to 110, "
            "downgraded from very severe. Red warning in force."
        ),
        "source": "Source: IMD National Bulletin No. 27, 19 Nov 2026",
    },
    {
        "kicker": "CULTURE - GAMING",
        "tag": "",
        "headline": "GTA VI launches worldwide after a 13-year wait",
        "sub": (
            "Grand Theft Auto VI unlocks at midnight local time on 19 Nov "
            "for PlayStation 5 and Xbox Series X|S, rolling out from New "
            "Zealand. US standard edition price: $79.99."
        ),
        "source": "Source: AP, 19 Nov 2026",
    },
    {
        "kicker": "ART MARKET - NEW YORK",
        "tag": "",
        "headline": "Van Gogh sells for a record $190.4m at Sotheby's",
        "sub": (
            "Chataigniers en fleurs (1890), painted in the last two months "
            "of his life, smashes his $117.2m auction record after a "
            "Nazi-era ownership dispute was settled."
        ),
        "source": "Source: BBC, 19 Nov 2026",
    },
]


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    margin = 44
    inner_w = W - 2 * margin

    # ------------------------------------------------------------ masthead
    y = 26
    d.text(
        (margin, y),
        "DAILY FRONT PAGE  -  THURSDAY  -  SIX STORIES, ONE IMAGE",
        font=font(SANS_BOLD, 17),
        fill=ACCENT,
    )
    y += 30
    d.line([(margin, y), (W - margin, y)], fill=RULE, width=5)
    y += 12
    d.text(
        (margin, y),
        "19 November 2026",
        font=font(SERIF_BOLD, 66),
        fill=INK,
    )
    y += 84
    d.text(
        (margin, y),
        "The World in One Picture",
        font=font(SERIF_BOLD, 38),
        fill=INK,
    )
    y += 52
    d.line([(margin, y), (W - margin, y)], fill=RULE, width=2)
    y += 8
    d.line([(margin, y), (W - margin, y)], fill=RULE, width=1)
    y += 14

    # ------------------------------------------------------------ panels
    gap_x = 28
    gap_y = 18
    col_w = (inner_w - gap_x) // 2
    rows = 3
    grid_top = y
    grid_bottom = H - 58
    row_h = (grid_bottom - grid_top - (rows - 1) * gap_y) // rows

    f_kicker = font(SANS_BOLD, 14)
    f_tag = font(SANS_BOLD, 12)
    f_head = font(SANS_BOLD, 22)
    f_sub = font(SANS, 16)
    f_src = font(SANS_ITALIC, 13)

    for idx, story in enumerate(STORIES):
        col = idx % 2
        row = idx // 2
        x0 = margin + col * (col_w + gap_x)
        y0 = grid_top + row * (row_h + gap_y)
        x1 = x0 + col_w
        y1 = y0 + row_h

        d.rectangle([x0, y0, x1, y1], outline=PANEL_LINE, width=2)
        d.rectangle([x0, y0, x1, y0 + 6], fill=ACCENT)

        px = x0 + 16
        pw = col_w - 32
        py = y0 + 16

        d.text((px, py), story["kicker"], font=f_kicker, fill=ACCENT)
        py += 22
        if story["tag"]:
            label = story["tag"]
            tw = d.textlength(label, font=f_tag) + 16
            d.rectangle([px, py, px + tw, py + 20], fill=CHIP_BG)
            d.text((px + 8, py + 3), label, font=f_tag, fill=CHIP_FG)
            py += 27

        py = draw_block(d, px, py, story["headline"], f_head, INK, pw, 27)
        py += 5
        py = draw_block(d, px, py, story["sub"], f_sub, (52, 50, 46), pw, 20)
        py += 7
        d.text((px, py), story["source"], font=f_src, fill=MUTED)

    # ------------------------------------------------------------ footer
    fy = H - 42
    d.line([(margin, fy - 10), (W - margin, fy - 10)], fill=RULE, width=2)
    d.text(
        (margin, fy),
        "All stories reported on 19 Nov 2026. Items labelled FORECAST, "
        "SCHEDULED or EXPECTED had not yet occurred at press time.",
        font=font(SANS, 15),
        fill=MUTED,
    )

    return img


def main():
    img = render()
    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", format="PNG", optimize=True)
    here = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(here, "entry.png"), format="PNG", optimize=True)


if __name__ == "__main__":
    main()
