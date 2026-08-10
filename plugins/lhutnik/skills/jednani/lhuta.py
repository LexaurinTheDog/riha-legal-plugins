#!/usr/bin/env python3
"""Výpočet konce procesní lhůty podle § 57 o. s. ř.

§ 57 odst. 1: do běhu lhůty se nezapočítává den, kdy došlo ke skutečnosti
určující počátek lhůty (lhůta počíná běžet dnem následujícím).
§ 57 odst. 2: lhůty podle týdnů/měsíců/let končí dnem, který se označením
shoduje se dnem rozhodné skutečnosti; není-li takový den v měsíci, končí
posledním dnem měsíce. Připadne-li konec na sobotu, neděli nebo svátek,
je posledním dnem lhůty nejblíže následující pracovní den.

Použití:
    python3 lhuta.py 2026-02-02 30d
    python3 lhuta.py 2026-02-02 2m --json
"""
import sys
import json
import argparse
from datetime import date, timedelta


def velikonocni_nedele(rok: int) -> date:
    """Gaussův/Meeusův algoritmus (gregoriánský kalendář)."""
    a = rok % 19
    b, c = divmod(rok, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mesic, den = divmod(h + l - 7 * m + 114, 31)
    return date(rok, mesic, den + 1)


def svatky(rok: int) -> set:
    """Státní svátky a dny pracovního klidu v ČR (z. č. 245/2000 Sb.)."""
    nedele = velikonocni_nedele(rok)
    return {
        date(rok, 1, 1),                 # Den obnovy samostatného českého státu
        nedele - timedelta(days=2),      # Velký pátek
        nedele + timedelta(days=1),      # Velikonoční pondělí
        date(rok, 5, 1),                 # Svátek práce
        date(rok, 5, 8),                 # Den vítězství
        date(rok, 7, 5),                 # Cyril a Metoděj
        date(rok, 7, 6),                 # Mistr Jan Hus
        date(rok, 9, 28),                # Den české státnosti
        date(rok, 10, 28),               # Vznik samostatného Československa
        date(rok, 11, 17),               # Den boje za svobodu a demokracii
        date(rok, 12, 24),               # Štědrý den
        date(rok, 12, 25),               # 1. svátek vánoční
        date(rok, 12, 26),               # 2. svátek vánoční
    }


def je_pracovni_den(d: date) -> bool:
    return d.weekday() < 5 and d not in svatky(d.year)


def posun_na_pracovni_den(d: date) -> date:
    while not je_pracovni_den(d):
        d += timedelta(days=1)
    return d


def pricti_mesice(d: date, n: int) -> date:
    """Týž den v označení; není-li, poslední den měsíce."""
    rok = d.year + (d.month - 1 + n) // 12
    mesic = (d.month - 1 + n) % 12 + 1
    den = d.day
    while True:
        try:
            return date(rok, mesic, den)
        except ValueError:
            den -= 1


def konec_lhuty(pocatek: date, delka: int, jednotka: str):
    """Vrátí (posledni_den, posledni_den_pred_posunem, byl_posunut)."""
    if jednotka == "d":
        syrovy = pocatek + timedelta(days=delka)
    elif jednotka == "t":
        syrovy = pocatek + timedelta(weeks=delka)
    elif jednotka == "m":
        syrovy = pricti_mesice(pocatek, delka)
    elif jednotka == "r":
        syrovy = pricti_mesice(pocatek, delka * 12)
    else:
        raise ValueError(f"neznámá jednotka: {jednotka!r} (použij d/t/m/r)")
    konecny = posun_na_pracovni_den(syrovy)
    return konecny, syrovy, konecny != syrovy


def duvod_posunu(d: date) -> str:
    if d in svatky(d.year):
        return "svátek"
    return {5: "sobota", 6: "neděle"}.get(d.weekday(), "")


def main():
    p = argparse.ArgumentParser(description="Konec procesní lhůty dle § 57 o. s. ř.")
    p.add_argument("pocatek", help="datum rozhodné skutečnosti (YYYY-MM-DD)")
    p.add_argument("lhuta", help="délka a jednotka, např. 30d, 2t, 3m, 1r")
    p.add_argument("--json", action="store_true", help="strojově čitelný výstup")
    a = p.parse_args()

    try:
        pocatek = date.fromisoformat(a.pocatek)
    except ValueError:
        sys.exit(f"CHYBA: '{a.pocatek}' není platné datum ve tvaru YYYY-MM-DD")

    text = a.lhuta.strip().lower()
    if not text[:-1].isdigit() or text[-1] not in "dtmr":
        sys.exit(f"CHYBA: '{a.lhuta}' není platná lhůta (očekávám např. 30d, 2t, 3m, 1r)")
    delka, jednotka = int(text[:-1]), text[-1]

    konecny, syrovy, posunuto = konec_lhuty(pocatek, delka, jednotka)
    zacatek_behu = pocatek + timedelta(days=1)

    if a.json:
        print(json.dumps({
            "pocatek_rozhodna_skutecnost": pocatek.isoformat(),
            "lhuta_bezi_od": zacatek_behu.isoformat(),
            "posledni_den": konecny.isoformat(),
            "posledni_den_pred_posunem": syrovy.isoformat(),
            "posunuto": posunuto,
            "duvod_posunu": duvod_posunu(syrovy) if posunuto else None,
        }, ensure_ascii=False, indent=2))
    else:
        dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
        print(f"Rozhodná skutečnost:  {pocatek}  ({dny[pocatek.weekday()]})")
        print(f"Lhůta běží od:        {zacatek_behu}  ({dny[zacatek_behu.weekday()]})")
        print(f"POSLEDNÍ DEN LHŮTY:   {konecny}  ({dny[konecny.weekday()]})")
        if posunuto:
            print(f"  (posunuto z {syrovy} — {duvod_posunu(syrovy)})")


if __name__ == "__main__":
    main()
