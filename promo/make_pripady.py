"""Videa ukázkových případů: oborový skill v CODEXIS AI -> hotový dokument na hlavičkovém papíře.

python3 make_pripady.py [kod ...]   -> pripady/{kod}/{kod}.mp4 podle pripady/{kod}/video.json

video.json: {"titulek", "podtitul": [...], "skill",
             "zabery": [["01_zadani.png", "popisek"], ...],
             "stranky": [["str-1.png", "kicker", "nadpis", ["poznámka", ...]], ...]}
"""
import json, os, sys
from make_frames import card, shot, page, FOOT, REPO
from build_video import build

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "pripady")


def video(kod):
    d = os.path.join(P, kod)
    v = json.load(open(os.path.join(d, "video.json")))
    s = os.path.join(d, "shots")
    seq = [(card(v["titulek"], v["podtitul"], kicker=f"CODEXIS AI · skill {v['skill']}", foot=FOOT), 5.5)]
    seq += [(shot(os.path.join(s, f), cap), 6.0) for f, cap in v["zabery"]]
    seq += [(page(os.path.join(s, f), k, t, n), 8.0) for f, k, t, n in v["stranky"]]
    seq.append((card("Návrh připraví AI. Podpis zůstává advokátovi.",
                     ["Každý výstup před odesláním kontroluje advokát.", "Oborové skilly pro CODEXIS AI: " + REPO],
                     kicker="RIHA legal", foot=FOOT, qr=os.path.join(HERE, "qr_marketplace.png")), 6.0))
    out = os.path.join(d, "frames"); os.makedirs(out, exist_ok=True)
    paths = []
    for i, (im, _) in enumerate(seq):
        p = os.path.join(out, f"{i:02d}.png"); im.save(p); paths.append(p)
    build(paths, [t for _, t in seq], os.path.join(d, f"{kod}.mp4"))


if __name__ == "__main__":
    for k in sys.argv[1:] or sorted(x for x in os.listdir(P) if os.path.exists(os.path.join(P, x, "video.json"))):
        video(k)
