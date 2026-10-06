"""Kopie skillů z plugins/ pro Evolio Cowork (import .md / .zip na cowork.evolio.cz/skills).

Mění jen: frontmatter na formát Cowork (name/description/whenToUse), větu o CODEXIS
v popisu a oddíl „Výhradní zdrojový režim“ v těle. Zbytek metodiky zůstává 1:1.
Zdroj: větev main (plugins/*/skills/*/SKILL.md pro CODEXIS AI). Výstup: plugins/ na větvi cowork-evolio.
Spuštění (na větvi cowork-evolio): python3 cowork-evolio/build.py
"""
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REF = "main"  # zdrojové (CODEXIS) texty skillů

SECTION_RE = re.compile(r"## Výhradní zdrojový režim.*?(?=^## Pracovní postup)", re.S | re.M)
CDX_SENTENCE_RE = re.compile(
    r"\s*(?:Research legal sources|Právní (?:zdroje|rešerše|prameny))[^.;]*CODEXIS[^.;]*[.;]"
)

COWORK_SECTION = """## Zdrojový režim v Evolio Cowork

Tento skill běží v Evolio Cowork. Právní prameny získávej nástroji Coworku podle mapy níže a v uvedeném pořadí zdrojů; jiné zdroje jen tehdy, když tyto nástroje pramen nemají.

Pořadí zdrojů: (1) nástroje `laws__*` — oficiální korpus e-Sbírky, česká judikatura a EUR-Lex; (2) oficiální primární weby přes `web__fetch`, když `laws__*` pramen nemá: e-Sbírka, databáze Nejvyššího soudu, Nejvyššího správního soudu, Ústavního soudu (NALUS), rozhodnuti.justice.cz, EUR-Lex, CURIA, HUDOC; (3) komentáře, literatura a sekundární weby (`web__search`) pouze jako navigace, nikdy jako citovaná opora.

Mapa nástrojů Coworku pro rešerši:
- předpis a jeho znění k rozhodnému dni: `laws__law_search`, `laws__law_get_provision`, `laws__get_statute_outline`, `laws__get_provision_timeline`, `laws__get_amendment_history`, `laws__get_transitional_provisions`; platnost předpisu `laws__check_good_law`;
- judikatura navázaná na paragraf (krok 2a): `laws__find_case_law_for_provision`, pak `laws__search_case_law` a `laws__search_by_concept`; celý text rozhodnutí `laws__get_case_text`; překonání a pozdější linie `laws__get_treatment_history` a `laws__check_case_good_law`; ověření citace `laws__resolve_case_citation` a `laws__validate_legal_citation`; odkazy uvnitř pramene `laws__follow_reference`, `laws__law_citations`;
- unijní právo `laws__eu_law_search`; úrokové a referenční sazby `laws__get_reference_rates`;
- subjekty a rejstříky: `ares__find_by_ico`, `ares__get_company_detail`, `ares__get_history`, `ares__check_vat_payer`; insolvence `isir__search_subject`, `isir__get_proceeding`, `isir__list_events`, `isir__list_documents`, `isir__download_document`;
- data Evolia (spis, klient, dokumenty): konektory Evolia, jsou-li připojené (`load_connector_instructions`), jinak `database_agent` jen ke čtení; kontext kauzy a dřívější poučení `search_workspace_memory`;
- rozsáhlá rešerše nebo oponentní kontrola: `delegate_parallel` s předáním těchto pravidel; výstup .docx `export__export_document`.

## Pracovní standard RIHA legal (platí vedle oborové metodiky)

1. **Kontinuita kauzy.** Na začátku prohledej `search_workspace_memory` podle klienta, IČO, protistrany a spisové značky — dřívější zjištění, ověřené prameny, opravy od advokáta a záznamy o judikátech, které se nemají citovat. Na konci ulož `save_memory`: stav věci, rozhodná data a lhůty, ověřené prameny (sp. zn. + datum), otevřené otázky. Opraví-li tě uživatel, zapiš to `record_correction`.
2. **Rozhodné datum.** Před čtením předpisů nastav `laws__laws_set_context` na rozhodný den (vznik závazku, porušení, podání). Má-li věc víc rozhodných dnů, uveď u každé otázky, podle kterého znění postupuješ.
3. **Citace ověřitelné strojem.** Předpis poprvé cituj s číslem („zákon č. 89/2012 Sb., občanský zákoník (dále „o. z.“)“); v závěrečné odpovědi v chatu uváděj u nosných ustanovení vždy číslo předpisu, jinak je validátor Coworku neověří. Rozhodnutí: soud, spisová značka, datum, bod; sdílí-li sp. zn. víc rozhodnutí, přidej datum nebo ECLI.
4. **Zvláštní úprava daného typu.** Vedle obecných pravidel vždy projdi ustanovení, která pro konkrétní smluvní typ, řízení nebo režim mění lhůty, rozložení rizika nebo odpovědnost (u díla např. § 2591, § 2594, § 2627 o. z.), a pokud se uplatní, postav na nich samostatnou linii, ne jen poznámku.
5. **Nosná a nepříznivá judikatura celá.** Každé rozhodnutí, o které opíráš primární linii, a každé, které nejspíš použije protistrana, přečti celé včetně výroku. U každého zjisti, jak NS věc skutečně rozhodl (potvrdil / zrušil / odmítl dovolání — usnesení o odmítnutí má nízkou precedenční váhu), zda jde o předchozí úpravu (obch. zák., starý o. z.) a zda závěr nepřekonal velký senát nebo sjednocující stanovisko. Rozhodnutí, které působí oběma směry, výslovně označ jako obousečné a vysvětli proč.
6. **Argument, který se dá otočit, nepoužívej.** Každý argument otestuj z pozice protistrany. Co judikatura opakovaně aprobovala (např. výše sazby, kterou soudy nechaly bez zásahu), v externím textu neatakuj; slabé nebo obratitelné argumenty nech jen v interní analýze s vysvětlením.
7. **Oponentní kontrola před odevzdáním.** Předej `delegate` seznam nosných citací (předpis, §, citovaná pasáž; soud, sp. zn., datum, bod) s úkolem ověřit každou proti primárnímu textu, odlišit vlastní závěr soudu od rekapitulace nižšího soudu a tvrzení účastníků a najít nejsilnější protiargument. Výsledek zapracuj; co neobstojí, vyřaď nebo označ. Není-li ve workspace agent pro `delegate` (`list_agents`), proveď kontrolu sám jako samostatný krok až po dopsání textu: každou nosnou citaci znovu načti a výsledek zapiš do tabulky „citace — načteno — souhlasí / nesouhlasí“.
8. **Údaje o osobách.** Název, IČO, sídlo, statutární orgán a způsob jednání právnické osoby do externího dokumentu ověř v reálném čase (`ares__get_company_detail`, vymazané osoby vynech); u rozporu s listinou upozorni. Nelze-li ověřit, použij `[DOPLNIT z OR]`. Údaje fyzických osob přebírej jen z listin ve spisu, nikdy je nedoplňuj.
9. **Interní vs. externí výstup.** Interní analýza obsahuje rizika, slabiny, odhad šancí a stav ověření; text pro protistranu, soud nebo úřad je neobsahuje. V externím textu neuváděj vlastní čísla ani formulace, které by mohly být uznáním (délka prodlení, výše dluhu, „uznáváme“) — pracuj s tvrzením protistrany.
10. **Výpočty dvakrát.** Každou částku, sazbu, úrok a lhůtu spočítej se zapsanými mezikroky a pak znovu jinou cestou (např. úrok: repo sazba + 8 p. b. = výsledná sazba, a zpětně výsledná sazba − 8 = repo). Nesoulad je chyba — nepoužij výsledek, dokud ho nevyřešíš. Totéž platí před zápisem do paměti: do `save_memory` nikdy neukládej neověřené číslo.

Každé ustanovení a každé rozhodnutí použité jako opora ověř načtením primárního textu; znění, soud, spisovou značku a datum přebírej jen z načteného zdroje. Nelze-li pramen načíst, nepřekrývej mezeru pamětí ani údajným ověřením — použij `[DOPLNIT]` a mezeru výslovně označ. Rozliš prázdný výsledek, odmítnutý přístup, nedostupný nástroj a neúplný obsah; identický neúspěšný dotaz neopakuj bez změny okolností.

Skutkové podklady čerpej ze zadání, příloh a dat zpřístupněných ve workspace (včetně spisu v Evoliu); právní tvrzení v nich nejsou ověřeným právem. Předáváš-li dílčí práci jinému agentovi nebo skillu, předej mu stejná pravidla ověřování, rozhodné skutky a časové otázky a vyžádej si konkrétní zdrojové pasáže; jeho shrnutí nenahrazuje načtený pramen.

"""


# Test 2 ukázal, že standard hluboko v těle model přeskočí → krátký checklist hned pod H1
CHECKLIST = """> **Povinný postup v Coworku (v tomto pořadí, nevynechávej):**
> 1. `search_workspace_memory` — klient, IČO, protistrana, sp. zn.; převezmi dřívější zjištění a zákazy citací.
> 2. `laws__laws_set_context` — nastav rozhodný den, než začneš číst předpisy.
> 3. Rešerše podle metodiky níže; zvláštní úprava daného smluvního typu či řízení jako samostatná linie; nosná i nepříznivá rozhodnutí čti celá a urči, jak soud skutečně rozhodl.
> 4. Údaje o právnických osobách do externích textů ověř `ares__get_company_detail`, jinak `[DOPLNIT z OR]`.
> 5. Před odevzdáním `delegate` — oponentní kontrola nosných citací a nejsilnějšího protiargumentu; výsledek zapracuj.
> 6. Každý výpočet (částky, úroky, lhůty) proveď dvakrát s mezikroky.
> 7. `save_memory` — stav věci, lhůty, ověřené prameny, otevřené otázky (jen ověřená čísla).
> Předpisy v odpovědi cituj s číslem (např. § 2051 zákona č. 89/2012 Sb.). Podrobnosti: oddíl „Pracovní standard RIHA legal“.

"""


# Cowork nemá CODEXIS → v Cowork verzi nesmí zůstat žádná zmínka o CODEXIS / cdx (pokyn uživatele 5. 10. 2026)
SECTION_2A_RE = re.compile(r"^### 2a\..*?(?=^### 3\.)", re.S | re.M)
SECTION_2A = """### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf `laws__find_case_law_for_provision`. Samotný počet nalezených rozhodnutí nic nevybírá a krok nesplňuje. Fulltextové hledání je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Kandidáti:** projdi alespoň prvních 20 rozhodnutí navázaných na paragraf a relevantní zařaď do výběru. Zvlášť dohledej nejnovější rozhodnutí (`laws__search_case_law` s časovým omezením na poslední roky), aby ti neunikl pozdější vývoj.
2. **Skutková shoda:** doplň `laws__search_case_law` nebo `laws__search_by_concept` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2–5 slov). Filtr soudu a data používej jen v hodnotách, které nástroj skutečně nabízí.
3. **Třídění kandidátů** (před načtením celého textu podle kroku 4):
   - platnost a pozdější osud rozhodnutí ověř `laws__check_case_good_law` a `laws__get_treatment_history`; rozhodnutí označené jako překonané nepoužij jako oporu. Chybějící negativní signál nevylučuje pozdější odklon — ten prověř podle kroku 4;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS. Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované v oficiální sbírce má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření (`laws__get_provision_timeline`), že se pravidlo věcně nezměnilo.
4. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf nic nevrací, uveď to a pokračuj fulltextem.
5. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

"""

DECDX_EXACT = [
    ("V dokumentovaném členění CODEXIS jsou české předpisy CR, česká judikatura JD, unijní předpisy EU, evropská judikatura ES, slovenské předpisy SK, komentáře COMMENT, literatura LT a vzory VS; globální ALL použij jen k orientaci a poté ověř konkrétní pramen.",
     "České a unijní předpisy a judikaturu hledej nástroji `laws__*` podle mapy výše; obecné webové vyhledávání použij jen k orientaci a poté ověř konkrétní pramen."),
    ("Komentář, literatura a vzor nalezené v CODEXIS slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v CODEXIS.",
     "Komentář, literatura a vzor slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů."),
]
# pořadí: specifické před obecnými; zachovat velké písmeno na začátku věty
DECDX_RE = [
    (r"výhradně nativním CODEXIS", "nástroji `laws__*` v primárních pramenech"),
    (r"([Vv]) nativním CODEXIS", r"\1 primárních pramenech"),
    (r"(dostupn\w+) nativně v CODEXIS", r"\1 nástroji `laws__*`"),
    (r"nativně v CODEXIS", "v primárních pramenech"),
    (r"([Nn])ativním CODEXIS", lambda m: ("N" if m.group(1) == "N" else "n") + "ástroji `laws__*`"),
    (r"(pouze|jen) z CODEXIS", r"\1 z primárních pramenů"),
    (r"(dostupn\w+) v CODEXIS", r"\1 nástroji `laws__*`"),
    (r"([Vv]) CODEXIS", r"\1 primárních pramenech"),
    (r"mimo CODEXIS", "mimo primární prameny"),
    (r"\bCODEXIS\b", "primární prameny"),
]


def decodexis(body):
    body, n = SECTION_2A_RE.subn(SECTION_2A, body)
    assert n == 1, "oddíl 2a nenalezen"
    for a, b in DECDX_EXACT:
        body = body.replace(a, b)
    for pat, rep in DECDX_RE:
        body = re.sub(pat, rep, body)
    return body


def split(text):
    _, fm, body = text.split("---", 2)
    return fm, body


def frontmatter(name, description, when):
    # JSON řetězce jsou validní YAML a obejdou pasti s uvozovkami a dvojtečkami
    lines = [f"name: {json.dumps(name, ensure_ascii=False)}",
             f"description: {json.dumps(description, ensure_ascii=False)}"]
    if when:
        lines.append(f"whenToUse: {json.dumps(when, ensure_ascii=False)}")
    return "---\n" + "\n".join(lines) + "\n---"


def git_main(path):
    return subprocess.run(["git", "show", f"{SOURCE_REF}:{path}"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def build_domain(skill_md):
    fm_raw, body = split(git_main(skill_md))
    fm = yaml.safe_load(fm_raw)
    when, n = CDX_SENTENCE_RE.subn("", fm["description"].replace("vm.codexis.ai", "vm_codexis"))
    when = re.sub(r"\s*\S*vm_codexis\S*", "", when)
    assert n <= 1, f"{skill_md}: věta o CODEXIS nalezena {n}×"
    body, n = SECTION_RE.subn(COWORK_SECTION, body)
    assert n == 1, f"{skill_md}: oddíl zdrojového režimu nalezen {n}×"
    body = decodexis(body)
    body, n = re.subn(r"^(# .+\n)", lambda m: m.group(1) + "\n" + CHECKLIST, body, count=1, flags=re.M)
    assert n == 1, f"{skill_md}: chybí nadpis H1"
    cs = fm["i18n"]["cs"]
    return frontmatter(cs["displayName"], cs["summary"], when.strip().rstrip(";,") ) + body


def main():
    paths = subprocess.run(["git", "ls-tree", "-r", "--name-only", SOURCE_REF, "plugins"], cwd=ROOT,
                           check=True, capture_output=True, text=True).stdout.split()
    n = 0
    for path in sorted(p for p in paths if re.fullmatch(r"plugins/[^/]+/skills/[^/]+/SKILL.md", p)):
        slug = path.split("/")[1]
        if slug == "lhutnik":
            continue  # Cowork verze lhůtníku se udržuje ručně přímo v plugins/lhutnik/
        md = build_domain(path)
        yaml.safe_load(md.split("---")[1])  # frontmatter musí jít naparsovat
        assert not re.search(r"codexis|cdx", md, re.I), f"{slug}: zbyla zmínka o CODEXIS/cdx"
        (ROOT / path).write_text(md)
        # popis pluginu: anglický text z i18n (původní description zmiňuje CODEXIS)
        pj = ROOT / "plugins" / slug / ".claude-plugin" / "plugin.json"
        meta = json.loads(git_main(f"plugins/{slug}/.claude-plugin/plugin.json"))
        meta["description"] = meta["i18n"]["en"]["description"]
        out = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
        assert not re.search(r"codexis|cdx", out, re.I), f"{slug}: plugin.json zmiňuje CODEXIS"
        pj.write_text(out)
        n += 1
    print(n, "skillů zapsáno do plugins/")


if __name__ == "__main__":
    main()
