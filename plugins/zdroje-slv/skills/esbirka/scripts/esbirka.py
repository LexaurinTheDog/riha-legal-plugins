#!/usr/bin/env python3
"""
esbirka.py — dotazy na e-Sbírku (zákony a jejich časová znění).

Zdroj dat:
  1. Veřejné API s klíčem   https://api.e-sbirka.gov.cz   (klíč v ~/.claude/esbirka.env)
  2. Veřejná cache portálu  https://e-sbirka.gov.cz/sbr-cache  (bez klíče, stejná data)

Bez klíče se použije cache portálu; s klíčem API. Volbu lze vynutit --base / --verejne.
Pouze standardní knihovna (urllib), žádné závislosti.

Použití (výběr):
  esbirka.py search "občanský zákoník" [--pocet 10] [--start 0]
  esbirka.py info 89/2012 [--k 2020-05-01]
  esbirka.py zneni 89/2012                       # historie časových znění
  esbirka.py obsah 89/2012 [--k DATUM] [--uzel ID]
  esbirka.py par 89/2012 "§ 2079" [--k DATUM] [--format md|text|html|json]
  esbirka.py text 89/2012 [--k DATUM] [--od "§ 2079" --do "§ 2084"] [--format ...]
  esbirka.py diff 89/2012 --z 2025-07-01 --k 2026-01-01 [--par "§ 2079"]
  esbirka.py souvislosti 89/2012 [--typ MENI]
  esbirka.py castka sb 2025 100
  esbirka.py raw GET "/dokumenty-sbirky/%2Fsb%2F2012%2F89/historie"
  esbirka.py raw POST /jednoducha-vyhledavani '{"fulltext":"nadace","start":0,"pocet":5}'
  esbirka.py diagnose                            # ověří klíč a název hlavičky

Označení předpisu lze zadat jako: "89/2012", "89/2012 Sb.", "č. 89/2012 Sb.",
"6/2021 Sb. m. s.", "/sb/2012/89" nebo "/sb/2012/89/2026-01-01".
"""
import argparse
import datetime as _dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ENV_FILE = os.path.expanduser("~/.claude/esbirka.env")
CACHE_DIR = os.path.expanduser("~/.cache/esbirka")
API_BASE = "https://api.e-sbirka.gov.cz"
PUBLIC_BASE = "https://e-sbirka.gov.cz/sbr-cache"
UA = "esbirka-skill/1.0 (+law-skills)"
CACHE_TTL = 7 * 24 * 3600

# Způsob předání klíče: hlavička `esel-api-access-key` (ověřeno 9/2026). Ostatní varianty jsou záloha,
# kdyby MV název změnilo – `diagnose` je projde a funkční si zapamatuje.
AUTH_CANDIDATES = [
    ("header", "esel-api-access-key"),
    ("header", "X-API-Key"),
    ("header", "X-Api-Key"),
    ("header", "api-key"),
    ("header", "apiKey"),
    ("header", "ApiKey"),
    ("header", "X-API-KEY"),
    ("header", "Api-Key"),
    ("header", "x-api-klic"),
    ("bearer", "Authorization"),
    ("query", "apiKey"),
    ("query", "api_key"),
    ("query", "klic"),
]

SBIRKY = {"sb.": "sb", "sb": "sb", "sb. m. s.": "sm", "sb.m.s.": "sm", "sm": "sm",
          "ú. l.": "ul0", "u.l.": "ul0"}


# ───────────────────────── konfigurace ─────────────────────────

def load_env():
    cfg = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip()
    for k in ("ESBIRKA_API_KEY", "ESBIRKA_BASE", "ESBIRKA_AUTH"):
        if os.environ.get(k):
            cfg[k] = os.environ[k]
    return cfg


def auth_memo_path():
    return os.path.join(CACHE_DIR, "auth.json")


def load_auth_memo():
    try:
        with open(auth_memo_path(), encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return None


def save_auth_memo(mode, name):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(auth_memo_path(), "w", encoding="utf-8") as fh:
        json.dump({"mode": mode, "name": name}, fh)


class Client:
    def __init__(self, base=None, verejne=False, verbose=False, no_cache=False):
        cfg = load_env()
        self.key = cfg.get("ESBIRKA_API_KEY")
        self.verbose = verbose
        self.no_cache = no_cache
        self.auth = None  # (mode, name)
        if verejne or (not self.key and not base and not cfg.get("ESBIRKA_BASE")):
            self.base = PUBLIC_BASE
            self.key = None
        else:
            self.base = (base or cfg.get("ESBIRKA_BASE") or API_BASE).rstrip("/")
        if self.key:
            a = cfg.get("ESBIRKA_AUTH")  # např. "header:X-API-Key" nebo "query:apiKey"
            if a and ":" in a:
                self.auth = tuple(a.split(":", 1))
            else:
                memo = load_auth_memo()
                self.auth = (memo["mode"], memo["name"]) if memo else AUTH_CANDIDATES[0]

    # ── nízká úroveň ──
    def _build(self, method, path, params, body, auth):
        url = self.base + path
        q = dict(params or {})
        headers = {"Accept": "application/json", "User-Agent": UA}
        if body is not None:
            headers["Content-Type"] = "application/json"
        # klíč jen na oficiální API — jiná --base / ESBIRKA_BASE ho nedostane (ochrana proti vynesení klíče)
        if self.key and auth and urllib.parse.urlparse(url).hostname == urllib.parse.urlparse(API_BASE).hostname:
            mode, name = auth
            if mode == "header":
                headers[name] = self.key
            elif mode == "bearer":
                headers[name] = "Bearer " + self.key
            elif mode == "query":
                q[name] = self.key
        if q:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(q, doseq=True)
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        return urllib.request.Request(url, data=data, headers=headers, method=method)

    def _do(self, req):
        if self.verbose:
            shown = req.full_url.replace(urllib.parse.quote_plus(self.key), "***") if self.key else req.full_url
            print(f"→ {req.get_method()} {shown}", file=sys.stderr)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                return r.status, raw
        except urllib.error.HTTPError as e:
            return e.code, e.read()
        except urllib.error.URLError as e:
            raise SystemExit(f"Chyba spojení: {e.reason}")

    def call(self, method, path, params=None, body=None, cache=False):
        """Vrátí dekódovaný JSON, nebo skončí s chybou. Při 401 s klíčem zkusí ostatní způsoby autentizace."""
        ck = None
        if cache and not self.no_cache and method == "GET":
            ck = os.path.join(CACHE_DIR, hashlib.sha1((self.base + path + json.dumps(params or {}, sort_keys=True)).encode()).hexdigest() + ".json")
            if os.path.exists(ck) and time.time() - os.path.getmtime(ck) < CACHE_TTL:
                with open(ck, encoding="utf-8") as fh:
                    return json.load(fh)
        status, raw = self._do(self._build(method, path, params, body, self.auth))
        if status == 401 and self.key and self.base == API_BASE:
            for cand in AUTH_CANDIDATES:
                if cand == self.auth:
                    continue
                s2, r2 = self._do(self._build(method, path, params, body, cand))
                if s2 != 401:
                    self.auth = cand
                    save_auth_memo(*cand)
                    if self.verbose:
                        print(f"ℹ autentizace funguje jako {cand[0]}:{cand[1]} (zapamatováno)", file=sys.stderr)
                    status, raw = s2, r2
                    break
            else:
                print("⚠ API s klíčem odmítlo všechny způsoby autentizace – přepínám na veřejnou cache portálu.", file=sys.stderr)
                self.base, self.key = PUBLIC_BASE, None
                status, raw = self._do(self._build(method, path, params, body, None))
        # API s klíčem (služba „daver“) nemá všechny endpointy cache portálu („dasex“); na generické 404
        # (Spring {"status":404}, ne formát e-Sbírky {"chyby":[…]}) zkus tentýž dotaz jednorázově v cache.
        if status == 404 and self.base != PUBLIC_BASE and b'"chyby"' not in raw:
            if self.verbose:
                print("ℹ endpoint na API s klíčem chybí – jednorázově volám veřejnou cache portálu", file=sys.stderr)
            req = self._build(method, path, params, body, None)
            req.full_url = PUBLIC_BASE + req.full_url[len(self.base):]
            status, raw = self._do(req)
        try:
            data = json.loads(raw.decode("utf-8")) if raw else None
        except ValueError:
            raise SystemExit(f"HTTP {status}: neplatná odpověď (ne JSON): {raw[:300]!r}")
        if status >= 400 or (isinstance(data, dict) and data.get("chyby")):
            errs = (data or {}).get("chyby") if isinstance(data, dict) else None
            if errs:
                msg = "; ".join(f"{e.get('kod')}: {e.get('popis')}" for e in errs)
                if any(e.get("kod") == "DOKUMENT_NENALEZEN" for e in errs):
                    msg += "\n  Tip: k zadanému datu předpis nebyl účinný (před účinností / po zrušení) – přehled intervalů dá příkaz `zneni`."
            else:
                msg = raw[:300].decode("utf-8", "replace")
            raise SystemExit(f"e-Sbírka HTTP {status}: {msg}")
        if ck:
            os.makedirs(CACHE_DIR, exist_ok=True)
            with open(ck, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False)
        return data

    # ── doménové volání ──
    def dok(self, stale_url, sub="", params=None, cache=False):
        path = "/dokumenty-sbirky/" + urllib.parse.quote(stale_url, safe="") + (("/" + sub) if sub else "")
        return self.call("GET", path, params=params, cache=cache)


# ───────────────────────── pomocné funkce ─────────────────────────

def parse_predpis(s, datum=None):
    """'89/2012 Sb.' | '89/2012' | '6/2021 Sb. m. s.' | '/sb/2012/89[/datum]' → staleUrl."""
    s = s.strip()
    if s.startswith("/"):
        base = s
    else:
        m = re.match(r"^(?:z(?:ák(?:on)?)?\.?\s*)?(?:č\.?\s*)?(\d+)\s*/\s*(\d{4})\s*(.*)$", s, re.I)
        if not m:
            raise SystemExit(f"Nerozumím označení předpisu: {s!r} (očekávám např. '89/2012 Sb.' nebo '/sb/2012/89')")
        cislo, rok, rest = m.group(1), m.group(2), m.group(3).strip().lower()
        rest = re.sub(r"\s+", " ", rest)
        sb = SBIRKY.get(rest, "sb") if rest else "sb"
        if rest and rest not in SBIRKY:
            for k, v in SBIRKY.items():
                if rest.startswith(k):
                    sb = v
                    break
        base = f"/{sb}/{rok}/{cislo}"
    if datum:
        parts = base.strip("/").split("/")
        base = "/" + "/".join(parts[:3]) + "/" + norm_date(datum)
    return base


def norm_date(d):
    d = d.strip()
    if d in ("dnes", "today"):
        return _dt.date.today().isoformat()
    m = re.match(r"^(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})$", d)
    if m:
        return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    if re.match(r"^\d{4}-\d{2}-\d{2}$", d):
        return d
    raise SystemExit(f"Neplatné datum: {d!r} (použij RRRR-MM-DD nebo D. M. RRRR)")


def cz_date(iso):
    if not iso:
        return "–"
    try:
        y, m, d = iso[:10].split("-")
        return f"{int(d)}. {int(m)}. {y}"
    except Exception:
        return iso


def xhtml_to_text(x):
    if not x:
        return ""
    x = re.sub(r"<br\s*/?>", "\n", x)
    x = re.sub(r"</(p|div|li|tr|h\d)>", "\n", x)
    x = re.sub(r"<var>(.*?)</var>", r"\1 ", x)
    x = re.sub(r"<[^>]+>", "", x)
    x = html.unescape(x)
    x = re.sub(r"[ \t]+", " ", x)
    return x.strip()


def fragment_label(f):
    """Krátké označení fragmentu z ELI (par_2079 → § 2079, odst_2 → odst. 2, pism_c → písm. c) …)."""
    tail = (f.get("eli") or "").split("/")[-1]
    m = re.match(r"^(par|odst|pism|bod|cl|cast|hlava|dil|oddil|pododdil|priloha)_(.+)$", tail)
    if not m:
        return ""
    typ, val = m.groups()
    val = val.replace("_", "/")
    return {"par": f"§ {val}", "odst": f"odst. {val}", "pism": f"písm. {val})", "bod": f"bod {val}",
            "cl": f"čl. {val}", "cast": f"ČÁST {val}", "hlava": f"HLAVA {val}", "dil": f"Díl {val}",
            "oddil": f"Oddíl {val}", "pododdil": f"Pododdíl {val}", "priloha": f"Příloha {val}"}[typ]


def render_fragments(frags, fmt="md"):
    if fmt == "json":
        return json.dumps(frags, ensure_ascii=False, indent=1)
    if fmt == "html":
        return "\n".join(f.get("xhtml") or "" for f in frags)
    # Typy fragmentů (kodTypuFragmentu): Prefix_*, Cast, Hlava, Dil, Oddil, Pododdil, Nadpis_nad (nadpis nad §),
    # Paragraf, Nadpis_pod (nadpis pod §), Odstavec_*, Pismeno_*, Bod_*, Pokracovani_Text, Priloha, …
    out = []
    for f in frags:
        typ = f.get("kodTypuFragmentu", "")
        if typ.startswith("Virtual_"):
            continue
        txt = xhtml_to_text(f.get("xhtml"))
        if not txt:
            continue
        if typ.startswith("Pismeno"):
            indent = "  "
        elif typ.startswith("Bod"):
            indent = "    "
        else:
            indent = ""
        if fmt == "md":
            if typ.startswith("Paragraf") or typ.startswith("Clanek"):
                out.append(f"\n### {txt}")
            elif typ in ("Cast", "Hlava", "Dil", "Oddil", "Pododdil") or typ.startswith("Priloha"):
                out.append(f"\n## {txt}")
            elif typ.startswith("Nadpis"):
                out.append(f"**{txt}**")
            elif typ.startswith("Prefix"):
                out.append(f"*{txt}*")
            else:
                out.append(indent + txt)
        else:
            if typ.startswith("Paragraf") or typ in ("Cast", "Hlava", "Dil", "Oddil", "Pododdil"):
                out.append("\n" + txt)
            else:
                out.append(indent + txt)
    return "\n".join(out).strip() + "\n"


def all_fragments(c, stale_url, params=None):
    """Stáhne všechny stránky fragmentů (stránka = 1000 fragmentů; u velkých kodexů ~10 stránek)."""
    page = 0
    frags = []
    while True:
        p = {"cisloStranky": page}
        p.update(params or {})
        d = c.dok(stale_url, "fragmenty", params=p, cache=True)
        frags.extend(d.get("seznam", []))
        page += 1
        if page >= int(d.get("pocetStranek", 1)):
            break
    return frags


def find_ustanoveni(c, stale_url, text, max_pocet=8):
    d = c.dok(stale_url, "nabidka-ustanoveni", params={"text": text, "maxPocet": max_pocet})
    return d.get("fragmentyNabidky", [])


def subtree(frags, fragment_id):
    """Fragment s daným id a všechny jeho potomky (podle prefixu ELI)."""
    root = next((f for f in frags if f.get("id") == fragment_id), None)
    if not root:
        return []
    prefix = root["eli"] + "/"
    return [f for f in frags if f.get("id") == fragment_id or (f.get("eli") or "").startswith(prefix)]


def print_json(d):
    print(json.dumps(d, ensure_ascii=False, indent=1))


def head_info(d):
    """Hlavička znění – společná pro info/text/par."""
    typ = {"AKTUALNI": "aktuální znění", "MINULE": "minulé znění", "BUDOUCI": "budoucí znění",
           "VYHLASENE": "vyhlášené znění"}.get(d.get("typZneni"), d.get("typZneni", ""))
    od, do = d.get("datumUcinnostiZneniOd"), d.get("datumUcinnostiZneniDo")
    rozsah = f"účinné od {cz_date(od)}" + (f" do {cz_date(do)}" if do else "")
    lines = [f"{d.get('uplnaCitace')}",
             f"{typ}, {rozsah}  (staleUrl {d.get('staleUrl')}, ELI {d.get('eli')})"]
    if d.get("datumZruseni"):
        r = d.get("rusiciDokumentSbirky") or {}
        lines.append(f"ZRUŠEN k {cz_date(d['datumZruseni'])}" + (f" předpisem {r.get('kodDokumentuSbirky')}" if r else ""))
    if d.get("novely"):
        lines.append("novely tohoto znění: " + ", ".join(n.get("kodDokumentuSbirky", "") for n in d["novely"]))
    return "\n".join(lines)


# ───────────────────────── příkazy ─────────────────────────

def cmd_search(c, a):
    body = {"fulltext": a.dotaz, "start": a.start, "pocet": a.pocet}
    d = c.call("POST", "/jednoducha-vyhledavani", body=body)
    if a.json:
        return print_json(d)
    print(f"Nalezeno celkem: {d.get('pocetCelkem')}  (zobrazeno {a.start + 1}–{a.start + len(d.get('seznam', []))})")
    for r in d.get("seznam", []):
        print(f"- {r.get('kodDokumentuSbirky'):<22} {r.get('nazev')}  [{r.get('stavDokumentuSbirky')}, {cz_date(r.get('datum'))}]  {r.get('staleUrl')}")


def cmd_info(c, a):
    # Datum jde do staleUrl (…/RRRR-MM-DD): funguje na API i v cache. Parametr predmetneDatum API s klíčem ignoruje.
    su = parse_predpis(a.predpis, a.k)
    d = c.dok(su)
    if a.json:
        return print_json(d)
    print(head_info(d))
    print(f"vyhlášen: {cz_date(d.get('datumCasVyhlaseni'))}, částka {d.get('cisloCastky')}/{d.get('rokCastky')}, "
          f"účinnost předpisu od {cz_date(d.get('datumUcinnostiOd'))}")
    if d.get("uplnaCitaceSNovelami"):
        print("\nÚplná citace s novelami:\n" + d["uplnaCitaceSNovelami"])


def cmd_zneni(c, a):
    su = parse_predpis(a.predpis)
    d = c.dok(su, "historie")
    hist = d.get("historie", [])
    if a.json:
        return print_json(d)
    print(f"Časová znění {su} ({len(hist)}):")
    for h in hist:
        od, do = h.get("datumUcinnostiZneniOd"), h.get("datumUcinnostiZneniDo")
        novely = ", ".join(n.get("kodDokumentuSbirky", "") for n in h.get("novely", []))
        typ = {"AKTUALNI": "AKTUÁLNÍ", "MINULE": "minulé", "BUDOUCI": "BUDOUCÍ", "VYHLASENE": "vyhlášené"}.get(h.get("typZneni"), h.get("typZneni"))
        print(f"- č. {h.get('cisloZneni', '?'):>3}  {cz_date(od):>13} – {cz_date(do) if do else '…':<13} {typ:<9} {h.get('staleUrl')}"
              + (f"   novely: {novely}" if novely else ""))
        for p in h.get("poznamky", []) or []:
            print(f"        ⚠ {p}")


def cmd_obsah(c, a):
    su = parse_predpis(a.predpis, a.k)
    d = c.dok(su, "obsah/" + str(a.uzel) if a.uzel else "obsah")
    if a.json:
        return print_json(d)
    for p in d.get("polozkyObsahu", []):
        print(f"- {p.get('oznaceniUstanoveni', ''):<14} {p.get('nazev', '')}  [{p.get('rozsah', '')}]"
              f"  fragmentId={p.get('fragmentId')} uzel={p.get('id')}{' +' if p.get('maPotomky') else ''}")


def _resolve_par(c, su, text):
    # API vyžaduje značku § — na holé číslo ("2079") vrací prázdný seznam,
    # zatímco "§ 2079" najde ustanovení. Ověřeno 9/2026 na /sb/2012/89.
    q = (text or "").strip()
    if q[:1].isdigit():
        q = "§ " + q
    hits = find_ustanoveni(c, su, q)
    if not hits and q != text:
        hits = find_ustanoveni(c, su, text)  # fallback na původní zadání
        q = text
    if not hits:
        raise SystemExit(f"Ustanovení {text!r} v {su} nenalezeno.")
    exact = [h for h in hits if h.get("identifikaceUstanoveni", "").lower().startswith(q.lower())]
    return (exact or hits)[0], hits


def cmd_par(c, a):
    su = parse_predpis(a.predpis, a.k)
    d = c.dok(su)
    su = d.get("staleUrl", su)  # normalizace na konkrétní znění
    hit, hits = _resolve_par(c, su, a.ustanoveni)
    frags = all_fragments(c, su)
    sub = subtree(frags, hit["fragmentId"])
    if a.format != "json":
        print(head_info(d))
        print(f"\n{hit.get('identifikaceUstanoveni')}" + (f" — {hit.get('nazev')}" if hit.get("nazev") else ""))
        if len(hits) > 1:
            print("  (další shody: " + "; ".join(h.get("identifikaceUstanoveni", "") for h in hits[1:5]) + ")")
        print()
    print(render_fragments(sub, a.format))


def cmd_text(c, a):
    su = parse_predpis(a.predpis, a.k)
    d = c.dok(su)
    su = d.get("staleUrl", su)
    frags = all_fragments(c, su)
    if a.od or a.do:
        ids = [f.get("id") for f in frags]
        i0, i1 = 0, len(frags)
        if a.od:
            h, _ = _resolve_par(c, su, a.od)
            i0 = ids.index(h["fragmentId"])
        if a.do:
            h, _ = _resolve_par(c, su, a.do)
            last = subtree(frags, h["fragmentId"])[-1]
            i1 = ids.index(last["id"]) + 1
        frags = frags[i0:i1]
    if a.format != "json":
        print(head_info(d))
        print()
    print(render_fragments(frags, a.format))


def cmd_diff(c, a):
    su_from = parse_predpis(a.predpis, a.z)
    su_to = parse_predpis(a.predpis, a.k)
    d_from = c.dok(su_from)
    d_to = c.dok(su_to)
    su_from, su_to = d_from.get("staleUrl", su_from), d_to.get("staleUrl", su_to)
    path = "/dokumenty-sbirky/" + urllib.parse.quote(su_from, safe="") + "/rozdilove-fragmenty/" + urllib.parse.quote(su_to, safe="")
    d = c.call("GET", path)
    if a.json:
        return print_json(d)
    print(f"Srovnání znění {su_from} (účinné od {cz_date(d_from.get('datumUcinnostiZneniOd'))}) → {su_to} (účinné od {cz_date(d_to.get('datumUcinnostiZneniOd'))})")
    print("Značení: **vloženo**, ~~vypuštěno~~; typRozdilu = UPRAVA | VLOZENO | ZRUSENO")
    items = d.get("seznam") if isinstance(d, dict) else d
    if not isinstance(items, list):
        return print_json(d)
    # Odpověď = kompletní seznam fragmentů cílového znění; změněné mají typRozdilu a v xhtml <ins>/<del>.
    shown, cur_par, last_hdr = 0, "", None
    want = a.par.replace(" ", "").lower() if a.par else None
    for it in items:
        typ_frag = it.get("kodTypuFragmentu", "")
        if typ_frag.startswith("Paragraf") or typ_frag.startswith("Clanek"):
            cur_par = xhtml_to_text(it.get("xhtml"))
        typ = it.get("typRozdilu")
        if not typ:
            continue
        cit = it.get("zkracenaCitace", "") or ""
        if want and want not in cit.replace(" ", "").lower() and want not in cur_par.replace(" ", "").lower():
            continue
        def _mark(m, l, r):
            inner = m.group(1)
            core = inner.strip()
            if not core:
                return inner
            lead = inner[: len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            return f"{lead}{l}{core}{r}{trail}"
        x = it.get("xhtml") or ""
        x = re.sub(r"<ins>(.*?)</ins>", lambda m: _mark(m, "**", "**"), x, flags=re.S)
        x = re.sub(r"<del>(.*?)</del>", lambda m: _mark(m, "~~", "~~"), x, flags=re.S)
        txt = xhtml_to_text(x)
        hdr = cur_par or cit
        if hdr != last_hdr:
            print(f"\n### {hdr}")
            last_hdr = hdr
        print(f"[{typ}] {cit}\n{txt}")
        shown += 1
    print(f"\nZměněných fragmentů: {shown}" + (" (žádné – zkuste --json)" if shown == 0 else ""))


def cmd_souvislosti(c, a):
    su = parse_predpis(a.predpis)
    d = c.dok(su, "souvislosti")
    if a.json:
        return print_json(d)
    for s in d.get("souvislosti", []):
        if a.typ and s.get("typ") != a.typ:
            continue
        print(f"\n{s.get('typ')} ({s.get('pocetDokumentuSbirky')}):")
        for x in s.get("dokumentySbirky", [])[: a.limit]:
            print(f"- {x.get('kodDokumentuSbirky'):<20} {x.get('nazev')}  [{x.get('stavDokumentuSbirky')}] {x.get('staleUrl')}")
        if len(s.get("dokumentySbirky", [])) > a.limit:
            print(f"  … a dalších {len(s['dokumentySbirky']) - a.limit} (zvyšte --limit)")


def cmd_castka(c, a):
    d = c.call("GET", f"/castky/{a.sbirka}/{a.rok}/{a.cislo}")
    if a.json:
        return print_json(d)
    print(f"Částka {a.cislo}/{a.rok} {a.sbirka}: vyhlášena {cz_date(d.get('datumCasVyhlaseni'))} (sada {d.get('sadaDokumentuKod')})")
    pz = d.get("pravneZavazneZneni") or {}
    for k, v in pz.items():
        if isinstance(v, dict) and v.get("dokumentId"):
            print(f"- {k}: právně závazné PDF https://e-sbirka.gov.cz/sbr-externi/stahni/overena-zneni/{v['dokumentId']}")
    for x in d.get("dokumentySbirky", []) or d.get("seznam", []) or []:
        print(f"- {x.get('kodDokumentuSbirky'):<20} {x.get('nazev')}  {x.get('staleUrl')}")
    print("Seznam aktů v částce: search \"<číslo>/<rok> Sb.\" nebo raw GET /castky/…/opravy pro redakční opravy.")


def cmd_raw(c, a):
    body = json.loads(a.body) if a.body else None
    d = c.call(a.metoda.upper(), a.cesta if a.cesta.startswith("/") else "/" + a.cesta, body=body)
    print_json(d)


def cmd_diagnose(c, a):
    cfg = load_env()
    print(f"env soubor: {ENV_FILE} {'(existuje)' if os.path.exists(ENV_FILE) else '(CHYBÍ)'}")
    print(f"klíč: {'nastaven (' + str(len(cfg.get('ESBIRKA_API_KEY', ''))) + ' znaků)' if cfg.get('ESBIRKA_API_KEY') else 'NENÍ – používá se veřejná cache portálu'}")
    print(f"aktivní base: {c.base}")
    if not cfg.get("ESBIRKA_API_KEY"):
        st, raw = c._do(c._build("GET", "/sbirky", None, None, None))
        print(f"veřejná cache: HTTP {st}  {raw[:80]!r}")
        return
    ok = None
    for mode, name in AUTH_CANDIDATES:
        req = c._build("GET", "/sbirky", None, None, (mode, name))
        req.full_url = req.full_url.replace(c.base, API_BASE, 1)
        st, raw = c._do(req)
        print(f"  {mode:6} {name:15} → HTTP {st}  {raw[:70]!r}")
        if st == 200 and ok is None:
            ok = (mode, name)
    if ok:
        save_auth_memo(*ok)
        print(f"\n✓ Funguje: {ok[0]}:{ok[1]} (zapamatováno v {auth_memo_path()}). "
              f"Napevno lze nastavit řádkem ESBIRKA_AUTH={ok[0]}:{ok[1]} v {ENV_FILE}.")
    else:
        print("\n✗ Žádný způsob nefunguje. Zkontrolujte klíč (NEPLATNY_API_KLIC) – skript mezitím používá veřejnou cache.")


# ───────────────────────── main ─────────────────────────

def main(argv=None):
    ap = argparse.ArgumentParser(description="Dotazy na e-Sbírku – zákony a jejich časová znění.")
    ap.add_argument("--base", help="jiná základní URL (výchozí: API s klíčem, jinak veřejná cache)")
    ap.add_argument("--verejne", action="store_true", help="vynutit veřejnou cache portálu (bez klíče)")
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--no-cache", action="store_true", help="nepoužívat lokální cache stránek fragmentů")
    sp = ap.add_subparsers(dest="cmd", required=True)

    p = sp.add_parser("search", help="fulltextové vyhledání předpisů"); p.add_argument("dotaz")
    p.add_argument("--pocet", type=int, default=10); p.add_argument("--start", type=int, default=0)
    p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_search)

    p = sp.add_parser("info", help="metadata předpisu / znění k datu"); p.add_argument("predpis")
    p.add_argument("--k", help="rozhodné datum (RRRR-MM-DD nebo D. M. RRRR)"); p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_info)

    p = sp.add_parser("zneni", help="historie časových znění"); p.add_argument("predpis")
    p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_zneni)

    p = sp.add_parser("obsah", help="systematika (části, hlavy, díly…)"); p.add_argument("predpis")
    p.add_argument("--k"); p.add_argument("--uzel", help="id nadřazeného uzlu pro rozbalení"); p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_obsah)

    p = sp.add_parser("par", help="text konkrétního ustanovení"); p.add_argument("predpis"); p.add_argument("ustanoveni", help='např. "§ 2079" nebo "§ 2079 odst. 2"')
    p.add_argument("--k"); p.add_argument("--format", choices=["md", "text", "html", "json"], default="md"); p.set_defaults(fn=cmd_par)

    p = sp.add_parser("text", help="celý text znění nebo rozsah ustanovení"); p.add_argument("predpis")
    p.add_argument("--k"); p.add_argument("--od"); p.add_argument("--do", dest="do")
    p.add_argument("--format", choices=["md", "text", "html", "json"], default="md"); p.set_defaults(fn=cmd_text)

    p = sp.add_parser("diff", help="rozdíly mezi dvěma zněními"); p.add_argument("predpis")
    p.add_argument("--z", required=True, help="datum výchozího znění"); p.add_argument("--k", required=True, help="datum cílového znění")
    p.add_argument("--par", help="omezit na ustanovení (např. '§ 2079')"); p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_diff)

    p = sp.add_parser("souvislosti", help="novelizuje / je novelizován / ruší / provádí …"); p.add_argument("predpis")
    p.add_argument("--typ", help="MENI, JE_MENEN, RUSI, JE_RUSEN, ODKAZUJE, JE_ODKAZOVAN, PROVADI, JE_PROVADEN, NALEZY_US, …")
    p.add_argument("--limit", type=int, default=30); p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_souvislosti)

    p = sp.add_parser("castka", help="obsah částky"); p.add_argument("sbirka", help="sb | sm"); p.add_argument("rok"); p.add_argument("cislo")
    p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_castka)

    p = sp.add_parser("raw", help="libovolné volání API"); p.add_argument("metoda", choices=["GET", "POST", "get", "post"]); p.add_argument("cesta"); p.add_argument("body", nargs="?")
    p.set_defaults(fn=cmd_raw)

    p = sp.add_parser("diagnose", help="ověření klíče a způsobu autentizace"); p.set_defaults(fn=cmd_diagnose)

    a = ap.parse_args(argv)
    c = Client(base=a.base, verejne=a.verejne, verbose=a.verbose, no_cache=a.no_cache)
    a.fn(c, a)


if __name__ == "__main__":
    main()
