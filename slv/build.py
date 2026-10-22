"""Varianta skillů z plugins/ pro Claude Code nad MCP SLV (Salvia), skillem e-Sbírka a MCP Sagasu.

Mění jen: větu o CODEXIS v popisech, oddíl „Výhradní zdrojový režim“, oddíl „### 2a.“ a zbylé zmínky
o CODEXIS v těle. Zbytek metodiky zůstává 1:1 se zdrojem.
Zdroj: větev main (plugins/*/skills/*/SKILL.md pro CODEXIS AI). Výstup: plugins/ na větvi slv-esbirka-sagasu.
Spuštění (na větvi slv-esbirka-sagasu): python3 slv/build.py
Vzor: cowork-evolio/build.py na větvi cowork-evolio.
"""
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REF = "main"  # zdrojové (CODEXIS) texty skillů
# orchestrátor R10 zatím není na main; až tam bude, položku smaž
EXTRA = {"legal-general-cee": "9921934"}
MARKETPLACE_REF = EXTRA["legal-general-cee"]  # = main + orchestrátor

SECTION_RE = re.compile(r"## Výhradní zdrojový režim.*?(?=^## Pracovní postup)", re.S | re.M)
SECTION_2A_RE = re.compile(r"^### 2a\..*?(?=^### 3\.)", re.S | re.M)
CDX_SENTENCE_RE = re.compile(
    r"\s*(?:Research legal sources|Právní (?:zdroje|rešerše|prameny))[^.;]*CODEXIS[^.;]*[.;]"
)

# Názvy nástrojů Sagasu ověřeny přes tools/list (viz README, oddíl Zdroje)
SAGASU_MAP = 'ekonomický subjekt podle IČO nebo názvu `firma_vyhledat` → `firma_detail` (ARES, jen aktivní; slovenské `firma_sk_vyhledat` → `firma_sk_detail`); výpis z obchodního rejstříku se statutárními orgány, společníky a kapitálem `obchodni_rejstrik`; zaniklé a vymazané osoby `verejny_rejstrik`, angažmá fyzické osoby `verejny_rejstrik_osoba`, angažmá právnické osoby `verejny_rejstrik_angazma_po`; listiny ze sbírky listin a jejich text `sbirka_listin` → `listina_text`; živnosti `zivnostensky_rejstrik`, `zivnostnik_vyhledat`; nespolehlivý plátce DPH a zveřejněné účty `dph_status`; adresa podle RÚIAN `standardizace_adresy`; ID datové schránky `datova_schranka_vyhledat` (nejjistěji podle IČO); advokáti `advokat_cz_vyhledat` → `advokat_cz_detail`; insolvence `insolvence_vyhledat` → `insolvence_detail` (události) → `insolvence_dokument_text`; výpočty `urok_z_prodleni`, `odmena_advokata`, `soudni_poplatek`. Postup je vždy vyhledání → detail → text. Když ARES nic nevrátí, subjekt může být zaniklý — ověř ve `verejny_rejstrik` dřív, než uzavřeš, že neexistuje.'

SOURCE_SECTION = f"""## Zdrojový režim: SLV, e-Sbírka a Sagasu

Právní prameny získávej těmito nástroji v uvedeném pořadí; jiné zdroje jen tehdy, když tyto pramen nemají:

1. **MCP SLV (Salvia)** — česká judikatura a vyhledání předpisu. Indexy `ns` (Nejvyšší soud), `nss` (Nejvyšší správní soud), `us` (Ústavní soud), `justice` (okresní, krajské a vrchní soudy), `isir` (insolvenční rejstřík). Nástroje: `search_decisions`, `search_by_case_number`, `fetch_decision`; předpisy `search_regulations`, `fetch_regulation_info`, `fetch_regulation_text`.
2. **Skill e-Sbírka** (`/esbirka`, skript `scripts/esbirka.py` v adresáři skillu) — úřední znění předpisu účinné k rozhodnému dni (`info --k`, `par --k`, `text`), historie znění (`zneni`), rozdíly mezi zněními (`diff`), novely, přechodná ustanovení a nálezy ÚS (`souvislosti`). Znění citované v odpovědi ber odsud, ne z paměti ani z textu rozhodnutí.
3. **MCP Sagasu** — subjekty, rejstříky a výpočty: {{SAGASU}}
4. Komentáře, literatura a webové zdroje slouží jen jako navigace, nikdy jako citovaná opora; jejich odkazy na normy a rozhodnutí ověř načtením v SLV nebo e-Sbírce.

Výpočty Sagasu (úrok z prodlení, odměna advokáta, soudní poplatek) přeber i s rozpisem a citací předpisu a přepočítej je druhou cestou (např. repo sazba + 8 p. b. = sazba a zpět); nesoulad je chyba. Údaje o právnické osobě do externího dokumentu (název, IČO, sídlo, statutární orgán, způsob jednání) ověř v Sagasu v reálném čase, vymazané osoby vynech; nelze-li ověřit, použij `[DOPLNIT z OR]`. Údaje fyzických osob přebírej jen z listin ve spisu.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán. Rozliš prázdný výsledek, odmítnutý přístup (SLV i Sagasu vyžadují přihlášení), nedostupný nástroj a neúplný obsah. Identický neúspěšný dotaz neopakuj bez změny; zkus věcně odůvodněnou alternativu (jiný index, jiný režim hledání, kratší dotaz), pak mezeru přesně označ `[DOPLNIT]`. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením. Znění, soud, spisovou značku a datum přebírej jen z načteného zdroje.

Je-li pro dílčí práci použit další agent nebo skill, předej mu výslovně tento zdrojový režim, rozhodné skutky a časové otázky. Vyžádej konkrétní zdrojové pasáže; jeho shrnutí nenahrazuje načtený pramen.

"""

SECTION_2A = """### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, vyhledej pro každý nosný paragraf rozhodnutí, která ho citují: `search_decisions` s `reg_num`, `reg_year` a `reg_par` (bez dotazu vrátí všechna rozhodnutí citující ustanovení, nejnovější první; s krátkým dotazem je seřadí podle relevance uvnitř této množiny). Fulltext je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje vazbu na paragraf.

1. **Kandidáti:** hledej přes indexy `ns`, `nss` a `us` (podle oboru i `justice`, v insolvenci `isir`) — jedno volání = jeden index. Projdi alespoň prvních 20 kandidátů a relevantní zařaď do výběru. Zvlášť dohledej nejnovější rozhodnutí (`date_from` na poslední roky), aby ti neunikl pozdější vývoj. Druhé ustanovení lze přidat přes `reg_num2`/`reg_year2`/`reg_par2`.
2. **Skutková shoda:** doplň fulltextem. Režim `bm25`: 2–5 výrazných právních pojmů, všechna slova musí v textu být (nula výsledků znamená vypustit slovo, ne absenci judikatury). Režim `knn`: jedna právní otázka formulovaná jako právní věta; víc otázek rozděl do více dotazů. Známou spisovou značku dohledej `search_by_case_number`.
3. **Třídění kandidátů** (před načtením celého textu podle kroku 4):
   - **citační graf:** `fetch_decision` vrací `citedBy` (pozdější rozhodnutí, která ho citují) a `citedCaseLaw`; sleduj `citedBy` 1–2 skoky k nejnovějšímu vyjádření téže právní věty a k případnému odklonu. Chybějící negativní signál nevylučuje pozdější odklon;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (výsledky s `date_from` z bodu 1 a fulltext `velký senát <právní pojem>`). Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované v oficiální sbírce má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření v e-Sbírce (`diff`, `par --k`), že se pravidlo věcně nezměnilo; ustanovení, která rozhodnutí skutečně aplikovalo, jsou v `regulations[]` z `fetch_decision`.
4. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf nic nevrací, uveď to a pokračuj fulltextem.
5. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

"""

DECDX_EXACT = [
    ("V dokumentovaném členění CODEXIS jsou české předpisy CR, česká judikatura JD, unijní předpisy EU, evropská judikatura ES, slovenské předpisy SK, komentáře COMMENT, literatura LT a vzory VS; globální ALL použij jen k orientaci a poté ověř konkrétní pramen.",
     "Judikaturu hledej v SLV přes indexy `ns`, `nss`, `us`, `justice` a `isir`, předpisy přes `search_regulations` a jejich znění v e-Sbírce; unijní předpisy a judikaturu SDEU a ESLP ověř v oficiálních databázích (EUR-Lex, CURIA, HUDOC)."),
    ("Komentář, literatura a vzor nalezené v CODEXIS slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v CODEXIS.",
     "Komentář, literatura a vzor slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v SLV nebo e-Sbírce."),
]
# pořadí: specifické před obecnými; zachovat velké písmeno na začátku věty
DECDX_RE = [
    (r"výhradně nativním CODEXIS", "nástroji SLV a e-Sbírky"),
    (r"([Vv]) nativním CODEXIS", r"\1 SLV a e-Sbírce"),
    (r"(dostupn\w+) nativně v CODEXIS", r"\1 v SLV nebo e-Sbírce"),
    (r"nativně v CODEXIS", "v SLV nebo e-Sbírce"),
    (r"([Nn])ativním CODEXIS", lambda m: ("N" if m.group(1) == "N" else "n") + "ástroji SLV a e-Sbírky"),
    (r"(pouze|jen) z CODEXIS", r"\1 z SLV a e-Sbírky"),
    (r"(dostupn\w+) v CODEXIS", r"\1 v SLV nebo e-Sbírce"),
    (r"([Vv]) CODEXIS", r"\1 SLV a e-Sbírce"),
    (r"mimo CODEXIS", "mimo SLV a e-Sbírku"),
    (r"\bCODEXIS\b", "SLV a e-Sbírka"),
]


# pasáže orchestrátoru (role, kontrakt delegovaného úkolu, přejímka) — přesné náhrady před obecnými regexy
ORCH_EXACT = [
    (" v aplikaci vm.codexis.ai", ""),
    ("# Všeobecný právní specialista a orchestrátor CODEXIS", "# Všeobecný právní specialista a orchestrátor"),
    ("výhradní zdrojový režim CODEXIS uvedený níže", "zdrojový režim SLV, e-Sbírka a Sagasu uvedený níže"),
    ("Podpůrný `codexis` slouží k dokumentovanému přístupu k nativní právní databázi; `codexis-dane` a `codexis-ucetnictvi` použij podle skutečné dostupnosti a jen pokud dotčený postup zůstává uvnitř téhož CODEXIS.",
     "Zdroje dodává plugin `zdroje-slv`: MCP SLV pro judikaturu a vyhledání předpisů, skill `esbirka` pro úřední znění k rozhodnému dni, MCP Sagasu pro rejstříky, insolvenci, datové schránky a výpočty."),
    ("Konektory k externím rejstříkům či jiným právním databázím, byť jsou v katalogu aplikace, do tohoto zdrojového režimu nepatří. Nepoužívej je jako náhradu CODEXIS.",
     "Jiné právní databáze a webové zdroje do tohoto zdrojového režimu nepatří jako citovaná opora; slouží nejvýš k navigaci."),
    ("„Právní předpisy, judikaturu, komentáře a vzory těž pouze nativním CODEXIS uvnitř vm.codexis.ai. Žádný externí web, rejstřík, databáze, vlastní API klient ani externí fallback, včetně odkazů uvnitř dokumentů. Vestavěný konektor použij jen jeho dokumentovaným rozhraním pro CODEXIS. Nedostupnost přiznej; mezeru nedoplňuj z paměti.“",
     "„Judikaturu a vyhledání předpisů těž z MCP SLV, znění předpisu k rozhodnému dni ze skillu e-Sbírka, údaje o subjektech, insolvenci a výpočty z MCP Sagasu. Web, komentáře a jiné databáze jen k navigaci, nikdy jako citovaná opora, včetně odkazů uvnitř dokumentů. Nevymýšlej názvy nástrojů ani parametry. Nedostupnost přiznej; mezeru nedoplňuj z paměti.“"),
    ("uloženým plným výsledkem CODEXIS; není-li dostupný hlavnímu zpracovateli, načti pramen nativně znovu",
     "uloženým plným výsledkem nástroje; není-li dostupný hlavnímu zpracovateli, načti pramen znovu"),
    ("Nedostupnost CODEXIS pravdivě", "Nedostupnost zdroje pravdivě"),
    ("tohoto senátu z CODEXIS", "tohoto senátu ze SLV"),
]

# manifesty orchestrátoru (plugin.json, marketplace.json)
JSON_EXACT = [
    ("ověří jejich prameny v CODEXIS", "ověří jejich prameny v SLV a e-Sbírce"),
    ("verifies their CODEXIS sources", "verifies their sources in SLV and e-Sbírka"),
    ("overí ich pramene v CODEXIS", "overí ich pramene v SLV a e-Sbírke"),
]


# pravidla z kontroly výstupu (Workflow review-slv-skills, 22. 10. 2026): {target, skills, old, new, reason}
RULES = json.loads((Path(__file__).parent / "rules.json").read_text())
USED = [0] * len(RULES)


def apply_rules(text, slug, targets):
    for i, r in enumerate(RULES):
        if r["target"] in targets and (r["skills"] == "*" or slug in r["skills"].split(",")) and r["old"] in text:
            text = text.replace(r["old"], r["new"])
            USED[i] += 1
    return text


def exact(text, pairs):
    for a, b in pairs:
        text = text.replace(a, b)
    return text


def decodexis(body):
    body, n = SECTION_2A_RE.subn(lambda _: SECTION_2A, body)
    assert n == 1, "oddíl 2a nenalezen"
    for a, b in DECDX_EXACT:
        body = body.replace(a, b)
    for pat, rep in DECDX_RE:
        body = re.sub(pat, rep, body)
    return body


def split(text):
    _, fm, body = text.split("---", 2)
    return fm, body


def git_main(path, ref=SOURCE_REF):
    return subprocess.run(["git", "show", f"{ref}:{path}"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def strip_cdx_sentence(text):
    # tečka v doméně by větu usekla dřív (aml-compliance: „… výhradně nativním CODEXIS ve vm.codexis.ai.“)
    text, n = CDX_SENTENCE_RE.subn("", text.replace("vm.codexis.ai", "vm_codexis_ai"))
    assert n <= 1, f"věta o CODEXIS nalezena {n}×"
    return text


def build_domain(skill_md, ref=SOURCE_REF):
    slug = skill_md.split("/")[1]
    # pravidla kontroly mají přednost před obecnými náhradami (ověřena proti zdrojovému textu)
    raw = apply_rules(git_main(skill_md, ref), slug, {"ORCH_EXACT", "DECDX_EXACT"})
    fm, body = split(exact(raw, ORCH_EXACT))
    # frontmatter zůstává ve formátu Claude Code; jen bez věty o CODEXIS
    fm = strip_cdx_sentence(fm)
    section = SOURCE_SECTION.replace("{SAGASU}", SAGASU_MAP)
    body, n = SECTION_RE.subn(lambda _: section, body)
    assert n == 1, f"{skill_md}: oddíl zdrojového režimu nalezen {n}×"
    body = decodexis(body)
    body = apply_rules(body, slug, {"SECTION"})
    return "---" + fm + "---" + body


def en_description(text):
    out, n = re.subn(r",? on top of the CODEXIS legal database", " on top of SLV case law, e-Sbírka and Sagasu", text)
    assert n == 1 or "CODEXIS" not in text, f"neznámá věta o CODEXIS: {text}"
    return out


ZDROJE = {
    "name": "zdroje-slv",
    "description": "Legal sources for the Czech practice skills: SLV (Salvia) case law and legislation MCP, Sagasu registries and legal calculators MCP, and the e-Sbírka skill for official statute versions at a given date.",
    "source": "./plugins/zdroje-slv",
    "category": "legal",
    "icon": "./plugins/zdroje-slv/icon.svg",
}


def build_marketplace():
    m = json.loads(exact(git_main(".claude-plugin/marketplace.json", MARKETPLACE_REF), JSON_EXACT))
    for p in m["plugins"]:
        p["description"] = en_description(p["description"])
    m["plugins"].insert(0, ZDROJE)
    out = json.dumps(m, ensure_ascii=False, indent=2) + "\n"
    assert not re.search(r"codexis|cdx", out, re.I), "marketplace.json zmiňuje CODEXIS"
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(out)


def main():
    assert "__SAGASU_MAP__" not in SAGASU_MAP, "doplň SAGASU_MAP z tools/list"
    paths = subprocess.run(["git", "ls-tree", "-r", "--name-only", SOURCE_REF, "plugins"], cwd=ROOT,
                           check=True, capture_output=True, text=True).stdout.split()
    n = 0
    paths = [(p, SOURCE_REF) for p in paths] + [
        (f"plugins/{s}/skills/{s}/SKILL.md", ref) for s, ref in EXTRA.items()]
    for path, ref in sorted(p for p in paths if re.fullmatch(r"plugins/[^/]+/skills/[^/]+/SKILL.md", p[0])):
        slug = path.split("/")[1]
        if slug == "lhutnik":
            continue  # lhůtník CODEXIS nepoužívá, zůstává beze změny
        md = build_domain(path, ref)
        yaml.safe_load(split(md)[0])  # frontmatter musí jít naparsovat
        assert not re.search(r"codexis|cdx", md, re.I), f"{slug}: zbyla zmínka o CODEXIS/cdx"
        (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / path).write_text(md)
        pj = ROOT / "plugins" / slug / ".claude-plugin" / "plugin.json"
        meta = json.loads(exact(git_main(f"plugins/{slug}/.claude-plugin/plugin.json", ref), JSON_EXACT))
        meta["description"] = en_description(meta["description"])
        out = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
        assert not re.search(r"codexis|cdx", out, re.I), f"{slug}: plugin.json zmiňuje CODEXIS"
        pj.parent.mkdir(parents=True, exist_ok=True)
        pj.write_text(out)
        icon = ROOT / "plugins" / slug / "icon.svg"
        if not icon.exists():
            icon.write_text(git_main(f"plugins/{slug}/icon.svg", ref))
        n += 1
    unused = [r["old"][:80] for r, n in zip(RULES, USED) if not n]
    assert not unused, f"pravidla bez shody: {unused}"
    build_marketplace()
    print(n, "skillů zapsáno do plugins/")


if __name__ == "__main__":
    main()
