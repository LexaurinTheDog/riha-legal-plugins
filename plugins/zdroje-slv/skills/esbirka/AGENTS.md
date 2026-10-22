# e-Sbírka skill — průvodce pro agenty

Tento dokument je určen AI agentům a automatizacím (Claude Code, Codex, vlastní skripty, n8n), které mají
odpovídat na otázky o znění českých právních předpisů. Popisuje, kdy skill použít, jaké příkazy volat,
jak číst výstup a jak formulovat odpověď pro právníka. Uživatelská dokumentace je v `README.md`,
katalog REST endpointů v `reference/api.md`.

## 1. Kdy skill použít

Použij `esbirka`, když dotaz obsahuje kterýkoli z těchto prvků:

- označení předpisu (`89/2012 Sb.`, „občanský zákoník“, „insolvenční zákon“, „OZ“, „IZ“, „o. s. ř.“),
- ustanovení (`§ 2079`, `§ 108 odst. 1`, `čl. 5`),
- časové určení („k 1. 5. 2020“, „v době uzavření smlouvy“, „ve znění účinném do“, „dnes platné“),
- otázku na změny („novela“, „co se změnilo“, „od kdy platí“, „budoucí znění“, „zrušen čím“),
- potřebu citovat přesný text zákona do podání, smlouvy, stanoviska.

Nepoužívej ho pro judikaturu (MCP SLV), pro důvodové zprávy návrhů v legislativním procesu
(e-Legislativa) ani pro právo EU (EUR-Lex). Neoficiální zdroje textu (zakonyprolidi.cz) použij jen jako
doplněk, e-Sbírka je úřední zdroj a má přednost.

## 2. Volání

```bash
python3 <adresář skillu>/scripts/esbirka.py <příkaz> [argumenty]
```

Skript nepotřebuje žádné závislosti ani proměnné prostředí. Klíč čte z `~/.claude/esbirka.env`; není-li,
běží proti veřejné cache portálu se stejnými daty. Nikdy klíč nevypisuj, neloguj ani nepřenášej jinam.

Každý příkaz umí strojově čitelný výstup: `--json` (search, info, zneni, obsah, diff, souvislosti, castka)
nebo `--format json` (par, text). Pro odpověď člověku používej výchozí textový výstup, pro další zpracování JSON.

## 3. Rozhodovací strom

```
Znám číslo předpisu?
├─ ne  → search "<název nebo číslo>" --pocet 5
│        vyber řádek s kodDokumentuSbirky a stavem AKTUALNE_PLATNY (nálezy ÚS a sdělení mají VYHLASENY_BEZ_UCINNOSTI)
└─ ano → Je otázka časově určená?
         ├─ ne  → aktuální znění: info PŘEDPIS, pak par / text
         │        V odpovědi výslovně uveď, že jde o aktuální znění, a datum, od kdy platí.
         └─ ano → info PŘEDPIS --k DATUM  (dá interval účinnosti a zakládající novely)
                  par PŘEDPIS "§ N" --k DATUM  /  text … --k DATUM --od … --do …
Otázka na změny?
├─ „co se změnilo“           → zneni PŘEDPIS (vyber dvě znění) → diff PŘEDPIS --z D1 --k D2 [--par "§ N"]
├─ „kdo novelizoval / ruší“  → souvislosti PŘEDPIS --typ JE_MENEN | JE_RUSEN | MENI | RUSI
├─ „platí to ještě / od kdy“ → info (datumZruseni, rusiciDokumentSbirky) a zneni (BUDOUCI)
└─ „nález ÚS k ustanovení“   → souvislosti PŘEDPIS --typ NALEZY_US, pak SLV pro text nálezu
Potřebuji strukturu předpisu? → obsah PŘEDPIS [--uzel ID]
Nestandardní dotaz?          → raw GET/POST podle reference/api.md
```

## 4. Recepty

### 4.1 Text ustanovení k rozhodnému dni

```bash
python3 <adresář skillu>/scripts/esbirka.py info 89/2012 --k 15.3.2019
python3 <adresář skillu>/scripts/esbirka.py par 89/2012 "§ 2079" --k 15.3.2019
```

První příkaz vrátí hlavičku (interval účinnosti, novely), druhý text. `par` hlavičku opakuje, takže pro
jednoduché dotazy stačí sám. Pro odstavec zadej `"§ 2079 odst. 2"`, pro písmeno `"§ 310 písm. c)"`,
u předpisů členěných na články `"čl. 5"`.

### 4.2 Souvislý úsek (např. celý díl o kupní smlouvě)

```bash
python3 <adresář skillu>/scripts/esbirka.py obsah 89/2012 --uzel 645208419      # najdi rozsah § v dílu
python3 <adresář skillu>/scripts/esbirka.py text 89/2012 --od "§ 2079" --do "§ 2183" --format text
```

Celý text kodexu (`text` bez `--od/--do`) má desítky tisíc řádků; do kontextu jej nevkládej, ulož do souboru
a pracuj s výřezy.

### 4.3 Co změnila konkrétní novela

```bash
python3 <adresář skillu>/scripts/esbirka.py zneni 89/2012                       # najdi znění založené novelou (sloupec novely)
python3 <adresář skillu>/scripts/esbirka.py diff 89/2012 --z 2025-07-01 --k 2026-01-01
```

`--z` je datum staršího znění, `--k` novějšího. Výstup má pro každý změněný fragment `[UPRAVA|VLOZENO|ZRUSENO]`,
citaci a text, kde `**tučné**` je vloženo a `~~přeškrtnuté~~` vypuštěno. Zúžení na ustanovení: `--par "§ 757"`.

### 4.4 Ověření platnosti citovaného předpisu

```bash
python3 <adresář skillu>/scripts/esbirka.py info 40/1964
```

U zrušeného předpisu hlavička obsahuje `ZRUŠEN k <datum> předpisem <kód>`; e-Sbírka vrátí poslední znění
před zrušením. Pokud protistrana cituje zrušený nebo nesprávně datovaný předpis, toto je důkaz.

### 4.5 Sledování budoucích změn

```bash
python3 <adresář skillu>/scripts/esbirka.py zneni 182/2006 | grep BUDOUCÍ
```

Řádky `BUDOUCÍ` obsahují datum účinnosti a novelu. Poznámka „Toto znění může být dotčené dosud
nezpracovanou novelou“ znamená, že MV ještě nezapracovalo vyhlášenou novelu; upozorni na to.

### 4.6 Strojové zpracování

```bash
python3 <adresář skillu>/scripts/esbirka.py info 182/2006 --k 2019-06-01 --json | python3 -c '
import json,sys; d=json.load(sys.stdin)
print(d["staleUrl"], d["datumUcinnostiZneniOd"], d.get("datumUcinnostiZneniDo"), [n["kodDokumentuSbirky"] for n in d["novely"]])'
python3 <adresář skillu>/scripts/esbirka.py par 182/2006 "§ 108" --k 2019-06-01 --format json   # seznam fragmentů s xhtml a ELI
```

## 5. Tvar výstupů

### 5.1 Hlavička znění (info, par, text)

```
Zákon č. 182/2006 Sb., o úpadku a způsobech jeho řešení (insolvenční zákon)
minulé znění, účinné od 1. 5. 2020 do 12. 11. 2020  (staleUrl /sb/2006/182/2020-05-01, ELI /eli/cz/sb/2006/182/2020-05-01)
novely tohoto znění: 119/2020 Sb.
```

Typ znění: `aktuální`, `minulé`, `budoucí`, `vyhlášené`. Interval bez „do“ znamená znění dosud účinné.

### 5.2 Klíčová pole JSON

| Pole | Význam |
|---|---|
| `staleUrl` | `/sb/2006/182/2020-05-01`; identifikátor znění, základ veřejného odkazu `https://e-sbirka.gov.cz` + staleUrl |
| `eli` | evropský identifikátor legislativy, u fragmentů obsahuje hierarchii (`…/par_108/odst_1`) |
| `typZneni` | `AKTUALNI`, `MINULE`, `BUDOUCI`, `VYHLASENE` |
| `datumUcinnostiZneniOd/Do` | interval účinnosti znění |
| `datumUcinnostiOd` | účinnost předpisu jako celku |
| `datumZruseni`, `rusiciDokumentSbirky` | zrušení předpisu |
| `novely[]` | novely, které založily toto znění (`kodDokumentuSbirky`, `staleUrl`) |
| `uplnaCitace`, `uplnaCitaceSNovelami`, `zkracenaCitace` | citace k přímému použití v textu |
| `stavDokumentuSbirky` (search, souvislosti) | `AKTUALNE_PLATNY`, `ZRUSENY`, `VYHLASENY_BEZ_UCINNOSTI`, `VYHLASENY_BUDOUCI` |
| fragment: `kodTypuFragmentu` | `Paragraf`, `Odstavec_*`, `Pismeno_*`, `Bod_*`, `Nadpis_nad/pod`, `Cast`, `Hlava`, `Dil`, `Oddil`, `Pododdil`, `Prefix_*` |
| fragment: `xhtml` | text s `<var>` označením a `<czechvoc-termin>`; `render` skriptu značky odstraňuje |
| fragment: `maDerogace`, `maNalezyUS`, `maNovelizace`, `maVykladovaStanoviska` | příznaky, že k ustanovení existuje další kontext |

## 6. Pravidla pro formulaci odpovědi

1. **Rozhodné datum je věcí právního posouzení, ne uživatelského pohodlí.** Pokud dotaz nemá datum, ale
   týká se konkrétního případu (smlouva, řízení, skutek), zeptej se na datum nebo odpověz pro aktuální znění
   a výslovně upozorni, že pro případ může být rozhodné znění jiné.
2. **Vždy uveď interval účinnosti znění**, ze kterého cituješ, a novelu, která je založila. Vzor citace:
   „§ 108 odst. 1 zákona č. 182/2006 Sb., insolvenční zákon, ve znění účinném od 1. 6. 2019 do 30. 9. 2019
   (novela č. 31/2019 Sb.)“.
3. **Text cituj doslova** z výstupu `par`/`text`; nepřepisuj, neparafrázuj. Vlastní výklad odděl.
4. **Upozorni na budoucí znění a nezapracované novely**, jsou-li ve výstupu `zneni`.
5. **Nezaměňuj vyhlášení a účinnost.** `datumCasVyhlaseni` je den vyhlášení v částce; právně relevantní je účinnost.
6. **Zrušený předpis** označ jako zrušený s datem a rušícím předpisem; text lze citovat jen historicky.
7. **Do podání dávej veřejný odkaz** `https://e-sbirka.gov.cz` + staleUrl, nikoli interní cestu API.
8. Neuváděj v odpovědi API klíč, cesty ke konfiguraci ani technické detaily, pokud se na ně uživatel neptá.

## 7. Chyby a jejich řešení

| Zpráva | Význam | Reakce agenta |
|---|---|---|
| `e-Sbírka HTTP 400: DOKUMENT_NENALEZEN … staleUrl: …/2026-01-01` | k datu předpis nebyl účinný | zavolej `zneni`, vyber správný interval, vysvětli uživateli (předpis zrušen / dosud neúčinný) |
| `Ustanovení '§ 5' v … nenalezeno` | špatné označení nebo ustanovení v tomto znění neexistuje | zkus `"čl. 5"`, ověř přes `obsah`, případně `text --od --do` sousedních § |
| `e-Sbírka HTTP 401: NEPLATNY_API_KLIC` | klíč nebo hlavička | skript se sám přepne na veřejnou cache a pokračuje; uživateli doporuč `diagnose` |
| `CHYBI_VSTUPNI_PARAMETR` (raw) | rozšířené vyhledávání vyžaduje `kontextVyhledavani` a další povinná pole | použij `search` (jednoduché vyhledávání) nebo doplň tělo podle `reference/api.md` |
| `Chyba spojení` | síť / výpadek | opakuj s `--verejne`; pokud selže i to, řekni, že e-Sbírka je nedostupná, a nabídni neoficiální zdroj s výhradou |
| dlouhý běh `par`/`text` | první stažení textu kodexu | normální (5–15 s), neopakuj volání paralelně |

## 8. Omezení

- API s klíčem (`api.e-sbirka.gov.cz`, služba „daver“) nemá všechny endpointy portálové cache: chybí `obsah`,
  `rozdilove-fragmenty` (diff) a `zneni-ke-srovnani`, parametr `predmetneDatum` ignoruje. Skript tyto dotazy
  automaticky a jednorázově posílá do veřejné cache (`-v` to vypíše); datum proto vždy vkládá do staleUrl.
- Data API jsou podle podmínek MV informativní; právně závazné je vyhlášené znění v částce (PDF z `castka`).
- Do 15. 1. 2027 může MV rozhraní měnit (příprava e-Legislativy). Při neznámé chybě zkontroluj `reference/api.md`
  proti aktuálnímu chování a aktualizuj dokumentaci.
- Fulltext `search` neumí filtrovat podle data ani typu aktu; pro přesné filtry použij `raw POST /rozsirena-vyhledavani/pravni-akt-esbirka`.
- Fulltextové parametry u fragmentů (`fulltext*`) text nefiltrují, pouze zvýrazňují; skript proto ustanovení
  hledá přes `nabidka-ustanoveni` a hierarchii ELI.
- Limity počtu volání nejsou zveřejněny; MV může klienta při zátěži odpojit. Neprocházej hromadně celé sbírky.
- Věcný rejstřík (CzechVoc), důvodové zprávy a výkladová stanoviska skript zatím nevypisuje; jsou dostupné přes `raw`.

## 9. Spolupráce s dalšími nástroji

| Potřeba | Nástroj |
|---|---|
| judikatura k ustanovení | MCP SLV: `search_decisions` s `reg_num=89`, `reg_year=2012`, `reg_par=2079` |
| komentář, souvislosti, EU právo | MCP SLV (judikatura), EUR-Lex (EU právo) |
| insolvenční rejstřík | skill `isir` |
| formátování výstupu do podání | agent `legal-document-formatter`, skill `format-awra` |
| lhůty z data účinnosti | skill `jednani` (`lhuta.py`) |

Doporučený řetězec pro právní rešerši: `esbirka` (přesný text a znění k datu) → SLV (judikatura k témuž
ustanovení a období) → syntéza s citacemi obou zdrojů.
