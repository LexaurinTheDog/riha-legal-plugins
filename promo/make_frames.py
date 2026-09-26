"""Snímky promo videa: titulkové karty + screenshoty s titulkem. Výstup frames/NN.png (1920x1080)."""
import glob, os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
BG, INK, ACC, MUTED = (20, 33, 48), (244, 240, 230), (201, 164, 92), (160, 172, 186)
GAR = os.path.expanduser("~/Library/Fonts/Garamond.ttc")
SANS = "/System/Library/Fonts/Helvetica.ttc"
f = lambda path, size: ImageFont.truetype(path, size)
HERE = os.path.dirname(os.path.abspath(__file__))


def wrap(d, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]


def card(title, lines=(), kicker="", foot="", qr=None):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    x, y = 160, 190
    if kicker:
        d.text((x, y), kicker.upper(), font=f(SANS, 30), fill=ACC); y += 70
    for ln in wrap(d, title, f(GAR, 92), W - 2 * x - (520 if qr else 0)):
        d.text((x, y), ln, font=f(GAR, 92), fill=INK); y += 104
    y += 40
    d.line((x, y, x + 180, y), fill=ACC, width=4); y += 60
    for ln in lines:
        for i, part in enumerate(wrap(d, ln, f(SANS, 40), W - 2 * x - (520 if qr else 0))):
            d.text((x, y), part, font=f(SANS, 40), fill=INK if i == 0 and ln[:1].isdigit() else MUTED if not ln[:1].isdigit() else INK); y += 56
        y += 18
    if qr:
        q = Image.open(qr).convert("RGB").resize((420, 420)); im.paste(q, (W - 160 - 420, 300))
    if foot:
        d.text((x, H - 110), foot, font=f(SANS, 28), fill=MUTED)
    return im


def shot(path, caption):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    s = Image.open(path).convert("RGB"); s.thumbnail((W - 160, H - 230))
    im.paste(s, ((W - s.width) // 2, 50))
    d.rectangle((0, H - 150, W, H), fill=(12, 20, 30))
    d.text((80, H - 112), caption, font=f(SANS, 44), fill=INK)
    return im


def page(path, kicker, title, notes):
    """Stránka dokumentu vlevo přes celou výšku, komentář vpravo."""
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    p = Image.open(path).convert("RGB"); p.thumbnail((W, H - 60))
    im.paste(p, (80, 30))
    x, y, w = 80 + p.width + 90, 200, W - (80 + p.width + 90) - 90
    d.text((x, y), kicker.upper(), font=f(SANS, 28), fill=ACC); y += 60
    for ln in wrap(d, title, f(GAR, 64), w):
        d.text((x, y), ln, font=f(GAR, 64), fill=INK); y += 74
    y += 30; d.line((x, y, x + 140, y), fill=ACC, width=4); y += 50
    for n in notes:
        for i, ln in enumerate(wrap(d, n, f(SANS, 34), w)):
            d.text((x, y), ln, font=f(SANS, 34), fill=INK if i == 0 else MUTED); y += 46
        y += 22
    return im


FOOT = "JUDr. Vojtěch Říha, Ph.D. · RIHA legal · výstupy AI vždy ověřuje advokát"
REPO = "github.com/LexaurinTheDog/riha-legal-plugins"
def main():
    seq = [
        card("50 oborových právních skillů pro CODEXIS AI",
             ["Rozhodná úprava a příhodná judikatura: postupem, ne naslepo."], kicker="Nové v marketplace", foot=FOOT),
        card("Fulltext najde, co zní podobně. Ne to, co se váže k vašemu paragrafu.",
             ["Obecný AI asistent často cituje judikaturu k dřívější úpravě nebo rozhodnutí, které už překonal velký senát."], kicker="Problém"),
        card("Co skill dělá jinak",
             ["1  Nejdřív rozhodná úprava a znění účinné ke dni události",
              "2  Judikatura navázaná přímo na paragraf: nejrelevantnější i nejnovější",
              "3  Kontrola překonání velkým senátem, stanoviskem nebo plénem ÚS",
              "4  Celý text rozhodnutí: nosné důvody oddělené od rekapitulace"], kicker="Postup"),
    ]
    shots = sorted(glob.glob(os.path.join(HERE, "shots", "*.png")))
    caps = {}
    capfile = os.path.join(HERE, "shots", "captions.txt")
    if os.path.exists(capfile):
        for ln in open(capfile, encoding="utf-8"):
            if "|" in ln:
                k, v = ln.rstrip("\n").split("|", 1); caps[k] = v
    seq += [shot(p, caps.get(os.path.basename(p), "")) for p in shots]
    seq += [
        card("Otestováno na reálných spisech",
             ["1  Reorganizační plán (§ 348, § 349 IZ): závěr shodný s pozdějším rozhodnutím soudu",
              "2  Přihláška pohledávky: včasnost z doručenky, úrok do dne úpadku, § 178 IZ",
              "3  Moderace smluvní pokuty: odlišení judikatury k § 301 obch. zák. od § 2051 OZ",
              "4  Přestupek podle stavebního zákona: nalezené vady napadeného rozhodnutí"], kicker="Ověření"),
        card("Instalace za půl minuty",
             ["1  Nástroje → Doplňky → Přidat zdroj doplňků",
              "2  URL repozitáře: " + REPO,
              "3  Vybrat obor a nainstalovat"], kicker="Jak začít", qr=os.path.join(HERE, "qr_marketplace.png")),
        card("50 oborů · 7 skupin",
             ["Otevřená licence Apache-2.0", REPO], kicker="riha-legal-plugins", foot=FOOT, qr=os.path.join(HERE, "qr_marketplace.png")),
    ]
    os.makedirs(os.path.join(HERE, "frames"), exist_ok=True)
    for old in glob.glob(os.path.join(HERE, "frames", "*.png")):
        os.remove(old)
    for i, im in enumerate(seq):
        im.save(os.path.join(HERE, "frames", f"{i:02d}.png"))
    print(len(seq), "snímků")


if __name__ == "__main__":
    main()
