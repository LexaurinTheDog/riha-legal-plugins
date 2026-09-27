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


def snimky(kod):
    """Snímky a délky jednoho případu (bez závěrečné karty), uložené do pripady/{kod}/frames/."""
    d = os.path.join(P, kod)
    v = json.load(open(os.path.join(d, "video.json")))
    s = os.path.join(d, "shots")
    seq = [(card(v["titulek"], v["podtitul"], kicker=f"CODEXIS AI · skill {v['skill']}", foot=FOOT), 5.5)]
    seq += [(shot(os.path.join(s, f), cap), 6.0) for f, cap in v["zabery"]]
    seq += [(page(os.path.join(s, f), k, t, n), 8.0) for f, k, t, n in v["stranky"]]
    return ulozit(seq, os.path.join(d, "frames"))


def ulozit(seq, out):
    os.makedirs(out, exist_ok=True)
    paths = []
    for i, (im, _) in enumerate(seq):
        p = os.path.join(out, f"{i:02d}.png"); im.save(p); paths.append(p)
    return paths, [t for _, t in seq]


def zaver():
    return ulozit([(card("Návrh připraví AI. Podpis zůstává advokátovi.",
                         ["Každý výstup před odesláním kontroluje advokát.", "Oborové skilly pro CODEXIS AI: " + REPO],
                         kicker="RIHA legal", foot=FOOT, qr=os.path.join(HERE, "qr_marketplace.png")), 6.0)],
                  os.path.join(P, "frames_zaver"))


def video(kody, out):
    """Případy za sebou, závěrečná karta jen jednou na konci."""
    paths, dur = [], []
    for k in kody + [None]:
        p, d = snimky(k) if k else zaver()
        paths += p; dur += d
    build(paths, dur, out)


if __name__ == "__main__":
    # python3 make_pripady.py            -> každý případ zvlášť
    # python3 make_pripady.py --spoj a b -> jedno video pripady/ukazky_{a}_{b}….mp4
    args = sys.argv[1:]
    if args[:1] == ["--spoj"]:
        video(args[1:], os.path.join(P, "ukazky_" + "_".join(args[1:]) + ".mp4"))
    else:
        for k in args or sorted(x for x in os.listdir(P) if os.path.exists(os.path.join(P, x, "video.json"))):
            video([k], os.path.join(P, k, f"{k}.mp4"))
