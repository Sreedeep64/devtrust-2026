#!/usr/bin/env python3
"""Generate the DevTrust 2026 one-page report and Handshake cover image."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "output" / "pdf" / "developer-ai-trust-2026.pdf"
COVER_PATH = ROOT / "assets" / "devtrust-cover.png"

PAGE_W, PAGE_H = 1280, 720

COLORS = {
    "ink": "#15221E",
    "muted": "#5D6B65",
    "paper": "#F5F2EA",
    "card": "#FCFBF7",
    "line": "#D6D9D1",
    "green": "#2E6B55",
    "mint": "#B9E7D0",
    "lime": "#D8F57A",
    "coral": "#EF7D62",
    "navy": "#183A45",
    "white": "#FFFFFF",
}

TRUST = [
    ("Trust when easy to verify", 48.0),
    ("Many tasks, not important decisions", 16.3),
    ("Low-risk tasks only", 16.3),
    ("Do not trust for most work", 12.3),
    ("Important work decisions", 6.6),
]

VALIDATION = [
    ("Run locally", 76.5),
    ("Compare with codebase", 63.9),
    ("Inspect tests / security", 53.0),
    ("Read official docs", 38.0),
    ("Use as-is", 9.6),
]


def hex_color(value: str):
    from reportlab.lib.colors import HexColor

    return HexColor(value)


def register_fonts() -> None:
    pdfmetrics.registerFont(
        TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    )


def round_rect(c, x, y, w, h, radius, fill, stroke=None, width=1):
    c.setFillColor(hex_color(fill))
    if stroke:
        c.setStrokeColor(hex_color(stroke))
        c.setLineWidth(width)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)


def draw_text(c, text, x, y, size, color, font="Arial", max_width=None):
    c.setFont(font, size)
    c.setFillColor(hex_color(color))
    if max_width:
        while size > 7 and c.stringWidth(text, font, size) > max_width:
            size -= 0.5
            c.setFont(font, size)
    c.drawString(x, y, text)


def draw_report() -> None:
    register_fonts()
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(PDF_PATH), pagesize=(PAGE_W, PAGE_H))
    c.setTitle("DevTrust 2026 - Developer Attitudes Toward AI Tools")
    c.setAuthor("Sreedeep Reddy Dugasani")

    c.setFillColor(hex_color(COLORS["paper"]))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Header and finding.
    round_rect(c, 52, 659, 175, 30, 15, COLORS["ink"])
    draw_text(c, "DEVTRUST 2026", 70, 668, 12, COLORS["lime"], "Arial-Bold")
    draw_text(
        c,
        "STACK OVERFLOW DEVELOPER SURVEY",
        246,
        669,
        11,
        COLORS["muted"],
        "Arial-Bold",
    )

    draw_text(c, "AI adoption is broad.", 52, 594, 42, COLORS["ink"], "Arial-Bold")
    draw_text(c, "Trust is conditional.", 52, 548, 42, COLORS["green"], "Arial-Bold")
    draw_text(
        c,
        "The strongest signal is not rejection. It is a demand for output that can be checked.",
        54,
        516,
        16,
        COLORS["muted"],
    )

    # A secondary group comparison, kept separate from the main finding.
    round_rect(c, 806, 505, 422, 70, 16, COLORS["card"], COLORS["line"])
    draw_text(c, "ATTITUDE BY EXPERIENCE", 830, 548, 10, COLORS["green"], "Arial-Bold")
    draw_text(c, "Favorable: 53% (1-5 yrs)  |  69% (16+ yrs)", 830, 526, 14, COLORS["ink"], "Arial-Bold")
    draw_text(c, "Observed association; the survey does not establish causation.", 830, 510, 9, COLORS["muted"])

    # Primary chart card.
    chart_x, chart_y, chart_w, chart_h = 52, 188, 730, 300
    round_rect(c, chart_x, chart_y, chart_w, chart_h, 22, COLORS["navy"])
    draw_text(c, "HOW DEVELOPERS TRUST AI OUTPUT", 82, 451, 12, COLORS["mint"], "Arial-Bold")
    draw_text(c, "Share of respondents", 82, 425, 11, "#B8CACB")

    bar_x = 345
    max_bar = 340
    row_y = 370
    for i, (label, value) in enumerate(TRUST):
        y = row_y - i * 41
        draw_text(c, label, 82, y + 4, 13, COLORS["white"], max_width=240)
        c.setFillColor(hex_color("#31535C"))
        c.roundRect(bar_x, y, max_bar, 14, 7, fill=1, stroke=0)
        fill_color = COLORS["lime"] if i == 0 else COLORS["mint"]
        c.setFillColor(hex_color(fill_color))
        c.roundRect(bar_x, y, max_bar * value / 50.0, 14, 7, fill=1, stroke=0)
        draw_text(c, f"{value:.1f}%", 700, y - 1, 15, COLORS["white"], "Arial-Bold")

    draw_text(
        c,
        "n = 14,304  |  Percentages may not total 100 because of rounding.",
        82,
        195,
        10,
        "#B8CACB",
    )

    # Recommendation card.
    rec_x, rec_y, rec_w, rec_h = 806, 188, 422, 300
    round_rect(c, rec_x, rec_y, rec_w, rec_h, 22, COLORS["card"], COLORS["line"])
    round_rect(c, 834, 433, 89, 26, 13, COLORS["lime"])
    draw_text(c, "RECOMMEND", 848, 441, 10, COLORS["ink"], "Arial-Bold")
    draw_text(c, "Design for verification,", 834, 392, 24, COLORS["ink"], "Arial-Bold")
    draw_text(c, "not autopilot.", 834, 364, 24, COLORS["green"], "Arial-Bold")

    steps = [
        ("01", "Keep AI close to reversible work."),
        ("02", "Attach context, tests and source links."),
        ("03", "Require human review for high-risk calls."),
    ]
    sy = 318
    for number, step in steps:
        c.setFillColor(hex_color(COLORS["ink"]))
        c.circle(850, sy + 3, 14, fill=1, stroke=0)
        draw_text(c, number, 841, sy - 1, 9, COLORS["lime"], "Arial-Bold")
        draw_text(c, step, 879, sy - 1, 13, COLORS["ink"], max_width=310)
        sy -= 52

    # Validation evidence strip.
    draw_text(c, "WHAT DEVELOPERS DO BEFORE USING AN AI ANSWER", 52, 148, 12, COLORS["ink"], "Arial-Bold")
    x = 52
    tile_gap = 12
    tile_w = (1176 - tile_gap * 4) / 5
    for label, value in VALIDATION:
        round_rect(c, x, 72, tile_w, 58, 12, COLORS["card"], COLORS["line"])
        draw_text(c, f"{value:.1f}%", x + 14, 100, 20, COLORS["green"], "Arial-Bold")
        draw_text(c, label, x + 14, 82, 10.5, COLORS["muted"], max_width=tile_w - 28)
        x += tile_w + tile_gap

    # Footer with audience caveat and source.
    draw_text(
        c,
        "Overall survey: 30,903 valid responses across 169 countries. Trust question: n = 14,304.",
        52,
        38,
        9.5,
        COLORS["muted"],
    )
    draw_text(
        c,
        "Voluntary Stack Overflow respondents are not a representative sample of all developers.",
        52,
        22,
        9.5,
        COLORS["muted"],
    )
    source = "Source: survey.stackoverflow.co/2026/ai/data  |  Accessed Nov 19, 2026"
    c.setFont("Arial", 9.5)
    c.setFillColor(hex_color(COLORS["muted"]))
    c.drawRightString(1228, 22, source)

    c.showPage()
    c.save()


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        if bold
        else "/System/Library/Fonts/Supplemental/Arial.ttf"
    )
    return ImageFont.truetype(path, size=size)


def pill(draw, box, fill, radius):
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_cover() -> None:
    COVER_PATH.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (1800, 1200), COLORS["paper"])
    draw = ImageDraw.Draw(img)

    # Decorative field.
    draw.ellipse((1350, -180, 1950, 420), fill="#D8F57A")
    draw.ellipse((-260, 890, 320, 1470), fill="#B9E7D0")
    draw.rounded_rectangle((95, 90, 1705, 1110), radius=42, fill=COLORS["card"], outline=COLORS["line"], width=3)

    pill(draw, (150, 145, 410, 198), COLORS["ink"], 26)
    draw.text((180, 158), "DEVTRUST 2026", font=load_font(25, True), fill=COLORS["lime"])
    draw.text((450, 158), "STACK OVERFLOW DEVELOPER SURVEY", font=load_font(22, True), fill=COLORS["muted"])

    draw.text((150, 275), "AI adoption is broad.", font=load_font(72, True), fill=COLORS["ink"])
    draw.text((150, 355), "Trust is conditional.", font=load_font(72, True), fill=COLORS["green"])
    draw.text(
        (154, 458),
        "A clear signal for teams building with AI: make every output easy to check.",
        font=load_font(28),
        fill=COLORS["muted"],
    )

    # Main evidence visualization.
    panel = (150, 560, 1125, 1005)
    draw.rounded_rectangle(panel, radius=34, fill=COLORS["navy"])
    draw.text((200, 610), "TRUST WHEN OUTPUT IS EASY TO VERIFY", font=load_font(22, True), fill=COLORS["mint"])
    draw.text((200, 686), "48.0%", font=load_font(110, True), fill=COLORS["lime"])
    draw.text((200, 825), "Only 6.6% extend that trust", font=load_font(32, True), fill=COLORS["white"])
    draw.text((200, 870), "to important work decisions.", font=load_font(32, True), fill=COLORS["white"])
    draw.text((200, 947), "n = 14,304", font=load_font(20), fill="#B8CACB")

    # Recommendation block.
    draw.rounded_rectangle((1185, 560, 1650, 1005), radius=34, fill="#EEF4E8")
    pill(draw, (1235, 610, 1425, 662), COLORS["lime"], 26)
    draw.text((1262, 623), "RECOMMEND", font=load_font(20, True), fill=COLORS["ink"])
    draw.text((1235, 716), "Design for", font=load_font(44, True), fill=COLORS["ink"])
    draw.text((1235, 766), "verification,", font=load_font(44, True), fill=COLORS["green"])
    draw.text((1235, 816), "not autopilot.", font=load_font(44, True), fill=COLORS["green"])
    draw.text((1238, 915), "Source: Stack Overflow", font=load_font(23), fill=COLORS["muted"])
    draw.text((1238, 949), "Developer Survey 2026", font=load_font(23), fill=COLORS["muted"])

    img.save(COVER_PATH, quality=95)


if __name__ == "__main__":
    draw_report()
    draw_cover()
    print(PDF_PATH)
    print(COVER_PATH)
