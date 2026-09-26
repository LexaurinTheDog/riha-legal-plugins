"""Video: hlavičkový papír RIHA legal ze zadaných údajů -> smlouva a žaloba (CODEXIS AI)."""
import os
from make_frames import card, shot, page, FOOT, REPO
from build_video import build

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "hlavicka", "shots_v2")
OUT = os.path.join(HERE, "hlavicka", "frames")


seq = [
    (card("Hlavičkový papír, smlouva a žaloba",
          ["Schválená šablona RIHA legal → smlouva o právních službách a žaloba na zaplacení.",
           "Smyšlené strany, údaje klientů ponechány jako [DOPLNIT]."],
          kicker="CODEXIS AI · ukázka", foot=FOOT), 5.5),
    (shot(f"{S}/01_sablona_word.png", "Hlavičkový papír podle vzoru kanceláře – ověřeno ve Wordu (1. a 2. strana)"), 6.5),
    (shot(f"{S}/02_zadani_smlouva.png", "1  Nahraji šablonu a zadám smlouvu o poskytování právních služeb"), 6.0),
    (shot(f"{S}/03_prubeh.png", "Agent ověří zákon o advokacii a tarif a píše jen do těla šablony"), 6.0),
    (page(f"{S}/04_smlouva_str1.png", "Výstup 1 · strana 1", "Smlouva o poskytování právních služeb",
          ["Plná hlavička: IČ, ev. č. ČAK, sídlo, kontakty, účet", "Časová odměna 3 000 Kč, záloha 20 000 Kč",
           "Výslovně: advokát není plátcem DPH", "Údaje klienta [DOPLNIT]"]), 8.0),
    (page(f"{S}/05_smlouva_str2.png", "Výstup 1 · strana 2", "Výpověď podle § 20 ZA a podpisy",
          ["Klient kdykoli, advokát jen ze zákonných důvodů", "15 dnů neodkladných úkonů po skončení",
           "Každá strana má vlastní místo a datum podpisu"]), 7.5),
    (shot(f"{S}/06_zadani_zaloba.png", "2  Na stejném hlavičkovém papíře zadám žalobu na zaplacení"), 6.0),
    (page(f"{S}/07_zaloba_str1.png", "Výstup 2 · strana 1", "Žaloba o zaplacení 245 000 Kč",
          ["Soud podle sídla žalovaného [DOPLNIT]", "Prodlení od 16. 5. 2026",
           "Úrok 11,50 %: repo ČNB k 1. 1. 2026 (3,50 %) + 8 p. b.", "Paušál 1 200 Kč mezi podnikateli"]), 8.0),
    (page(f"{S}/08_zaloba_str2.png", "Výstup 2 · strana 2", "Poplatek, náklady a petit",
          ["Soudní poplatek 5 %: 12 250 Kč", "Odměna 3 × 9 300 Kč + 3 × 450 Kč",
           "Předběžné náklady 41 500 Kč", "Čísla ověřena proti předpisům k 26. 9. 2026"]), 8.5),
    (card("Návrh připraví AI. Podpis zůstává advokátovi.",
          ["Každý výstup před odesláním kontroluje advokát.", "Oborové skilly pro CODEXIS AI: " + REPO],
          kicker="RIHA legal", foot=FOOT, qr=os.path.join(HERE, "qr_marketplace.png")), 6.0),
]
os.makedirs(OUT, exist_ok=True)
paths = []
for i, (im, _) in enumerate(seq):
    p = os.path.join(OUT, f"{i:02d}.png"); im.save(p); paths.append(p)
build(paths, [d for _, d in seq], os.path.join(HERE, "hlavicka", "hlavickovy_papir_smlouva_zaloba.mp4"))
