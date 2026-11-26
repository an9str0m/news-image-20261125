#!/usr/bin/env python3
"""Build the v2 entry image for make.fun news-image-20261125.

The artwork (assets/*.webp) was generated without any text; every word
on the page is typeset here with PIL so the headlines are perfectly
legible for the AI judge, which reads only the image. Layout follows
the reviewed spec: the date is the largest element, the West Java mine
disaster is the lead story, four world stories sit in a 2x2 grid, and
the Pakistan astronaut story closes the page.

Run: python3 build_entry.py  ->  writes entry.png (1024x1024)
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
W = H = 1024
MARGIN = 40
CW = W - 2 * MARGIN  # content width

CREAM = (246, 241, 229)
NAVY = (27, 42, 74)
VERMILLION = (179, 57, 46)
WHITE = (255, 255, 255)

SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_cover(img, box_w, box_h):
    """Resize + center-crop img to exactly box_w x box_h."""
    scale = max(box_w / img.width, box_h / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)),
                     Image.LANCZOS)
    x = (img.width - box_w) // 2
    y = (img.height - box_h) // 2
    return img.crop((x, y, x + box_w, y + box_h))


def draw_lines(draw, xy, lines, fnt, fill, leading):
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def rule(draw, y, thick=3):
    draw.rectangle([MARGIN, y, W - MARGIN, y + thick], fill=NAVY)
    return y + thick


def cell(draw, page, x, y, w, h, img_name, headline, accent_last=False,
         accent_idx=None):
    """One grid story: thumbnail left, headline right."""
    thumb = 148
    if img_name:
        img = Image.open(os.path.join(ASSETS, img_name)).convert("RGB")
        page.paste(fit_cover(img, thumb, thumb), (x, y))
    else:
        # KOSPI cell: a bold vermillion down arrow instead of a photo.
        draw.rectangle([x, y, x + thumb, y + thumb], fill=NAVY)
        cx, cy = x + thumb // 2, y + thumb // 2
        draw.polygon([(cx - 42, cy - 38), (cx + 42, cy - 38), (cx, cy + 48)],
                     fill=WHITE)
        draw.rectangle([cx - 15, cy - 72, cx + 15, cy - 38], fill=WHITE)
    tx = x + thumb + 18
    fnt = font(SANS_BOLD, 31)
    lines = headline.split("\n")
    ty = y + (thumb - len(lines) * 37) // 2
    for i, line in enumerate(lines):
        fill = VERMILLION if (i == accent_idx or
                              (accent_last and i == len(lines) - 1)) else NAVY
        draw.text((tx, ty), line, font=fnt, fill=fill)
        ty += 37


def main():
    page = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(page)

    # --- masthead ---------------------------------------------------
    y = rule(draw, 30, 7)
    y = rule(draw, y + 5, 2)
    y = centered(draw, y + 14, "THE WORLD IN A DAY", font(SERIF_BOLD, 44), NAVY)
    y = centered(draw, y + 2, "WEDNESDAY, NOVEMBER 25, 2026",
                 font(SANS_BOLD, 55), VERMILLION)
    y = rule(draw, y + 12, 3)

    # --- lead story: West Java mine ---------------------------------
    top = y + 18
    draw.text((MARGIN, top), "INDONESIA", font=font(SANS_BOLD, 24),
              fill=VERMILLION)
    draw_lines(draw, (MARGIN, top + 34),
               ["WEST JAVA FLOODS", "HIT GOLD MINE"],
               font(SANS_BOLD, 54), NAVY, 64)
    draw.text((MARGIN, top + 176), "9 DEAD, 17 TRAPPED",
              font=font(SANS_BOLD, 45), fill=VERMILLION)
    mine = Image.open(os.path.join(
        ASSETS, "media-generation-spot-mine-0-86ef10c0-6ec2-41eb-b821-a27f89ef56a1.webp")).convert("RGB")
    page.paste(fit_cover(mine, 356, 224), (W - MARGIN - 356, top + 6))
    draw = ImageDraw.Draw(page)
    y = rule(draw, top + 238, 3)

    # --- 2x2 grid -----------------------------------------------------
    gtop = y + 16
    colw = (CW - 24) // 2
    rowh = 168
    cell(draw, page, MARGIN, gtop, colw, rowh,
         "media-generation-spot-containers-0-efd4236c-3aab-44bb-ab6e-8f34160167f8.webp",
         "US PROPOSES\nTARIFFS UP TO 20%\nON 14 ECONOMIES", accent_idx=1)
    cell(draw, page, MARGIN + colw + 24, gtop, colw, rowh,
         None, "AI FEARS:\nKOSPI FALLS\n6.2%", accent_last=True)
    draw = ImageDraw.Draw(page)
    cell(draw, page, MARGIN, gtop + rowh + 14, colw, rowh,
         "media-generation-spot-tanker-0-8661d879-087e-4d98-82e4-af43f0657de0.webp",
         "TANKERS HIT\nMINES IN\nHORMUZ")
    cell(draw, page, MARGIN + colw + 24, gtop + rowh + 14, colw, rowh,
         "media-generation-spot-talks-0-961577bd-f3f9-44c9-a345-d0a33bca3806.webp",
         "UKRAINE PEACE\nTALKS AMID\nSTRIKES")
    draw = ImageDraw.Draw(page)
    y = rule(draw, gtop + 2 * rowh + 28, 3)

    # --- bottom strip: science ---------------------------------------
    top = y + 16
    astro = Image.open(os.path.join(
        ASSETS, "media-generation-spot-astronaut-0-5c17a3d6-404a-4fb0-90da-cd51a1d08de1.webp")).convert("RGB")
    strip_h = H - MARGIN - top
    page.paste(fit_cover(astro, 330, strip_h), (MARGIN, top))
    draw = ImageDraw.Draw(page)
    tx = MARGIN + 330 + 24
    draw.text((tx, top + 6), "SCIENCE", font=font(SANS_BOLD, 24),
              fill=VERMILLION)
    draw_lines(draw, (tx, top + 40),
               ["PAKISTAN'S FIRST", "ASTRONAUT IN ORBIT"],
               font(SANS_BOLD, 40), NAVY, 48)

    page.save(os.path.join(HERE, "entry.png"), optimize=True)
    print("wrote entry.png", os.path.getsize(os.path.join(HERE, "entry.png")))


if __name__ == "__main__":
    main()
