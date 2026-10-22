---
name: esbirka
description: "Dotazy na e-Sbírku (oficiální elektronická Sbírka zákonů a mezinárodních smluv, api.e-sbirka.gov.cz): vyhledání předpisu, přehled časových znění, znění účinné k zadanému datu, text konkrétního § / odstavce, srovnání dvou znění, novely a souvislosti, obsah částky. Triggers: /esbirka, e-Sbírka, eSbírka, znění k datu, časové znění, platné znění, účinné znění k, ve znění účinném do, text zákona, text §, novela, novelizace, Sb., Sb. m. s., co říká zákon, jak zněl paragraf."
---

# Skill: e-Sbírka – zákony a jejich časová znění

Oficiální zdroj českého práva: **e-Sbírka** (Ministerstvo vnitra). Od 1. 1. 2024 je elektronická
Sbírka zákonů a mezinárodních smluv právně závazná; konsolidovaná (úplná) znění jsou *informativní*,
ale jde o úřední konsolidaci, kterou lze v podání citovat jako zdroj znění.

Skill odpovídá na otázky typu:
- „Jak zněl § 2079 OZ k 1. 5. 2020?“ / „Co říká § 108 insolvenčního zákona dnes?“
- „Kolik znění má insolvenční zákon a od kdy platí to současné?“
- „Co se změnilo v § 2079 mezi 1. 7. 2025 a 1. 1. 2026?“
- „Které předpisy novelizovaly zákon č. 182/2006 Sb.?“ / „Čím byl zrušen zákon č. 40/1964 Sb.?“
- „Co vyšlo v částce 100/2025 Sb.?“

## Konfigurace

| Co | Kde |
|---|---|
| API klíč (volitelný) | `~/.claude/esbirka.env`, řádek `ESBIRKA_API_KEY=…` (chmod 600, mimo repozitář) |
| Skript | `scripts/esbirka.py` v adresáři tohoto skillu (base directory, kterou Claude Code sdělí při načtení skillu) |
| Lokální cache stránek textu | `~/.cache/esbirka/` (7 dní; smazat při podezření na zastaralý text) |

Zdroj dat vybírá skript sám:
1. **S klíčem** → veřejné API `https://api.e-sbirka.gov.cz` (registrace u MV ČR).
2. **Bez klíče** → veřejná cache portálu `https://e-sbirka.gov.cz/sbr-cache` (bez autentizace, stejná data
   a stejné cesty; ji používá samotný portál). Vynutit lze přepínačem `--verejne`.

Klíč se posílá v HTTP hlavičce **`esel-api-access-key`** (v dopise MV to není uvedeno; ověřeno 9/2026).
Bez ní API vrací `401 NEPLATNY_API_KLIC: Nezaslán API klíč`. Kdyby MV název změnilo, skript při 401 vyzkouší
záložní varianty, funkční si zapamatuje a jinak přepne na veřejnou cache. Ověření: `python3 <adresář skillu>/scripts/esbirka.py diagnose`.
Napevno lze způsob zadat řádkem `ESBIRKA_AUTH=header:esel-api-access-key` v env souboru.

Skript používá pouze standardní knihovnu Pythonu 3 – žádné závislosti.

## Identifikace předpisu

Skript přijímá: `89/2012`, `89/2012 Sb.`, `č. 89/2012 Sb.`, `6/2021 Sb. m. s.`, `/sb/2012/89`,
`/sb/2012/89/2026-01-01`. Datum lze psát `2020-05-01` i `1. 5. 2020`.

Interní identifikátor e-Sbírky je **staleUrl** `/{sbirka}/{rok}/{cislo}[/{datum}]` (`sb` = Sb., `sm` = Sb. m. s.);
s datem označuje **časové znění účinné k tomuto dni** (server datum normalizuje na začátek znění,
např. `/sb/2012/89/2020-05-01` → znění `/sb/2012/89/2018-12-01`). ELI: `/eli/cz/sb/2012/89/2026-01-01`.
Odkaz pro klienta / do podání: `https://e-sbirka.gov.cz` + staleUrl (např. `https://e-sbirka.gov.cz/sb/2012/89/2026-01-01`),
na ustanovení `…/2026-01-01#par_2079`.

## Příkazy

```bash
E="python3 <adresář skillu>/scripts/esbirka.py"   # base directory skillu

$E search "insolvenční zákon" --pocet 5          # fulltext → kód, název, stav, staleUrl
$E info 182/2006                                  # metadata aktuálního znění + úplná citace s novelami
$E info 182/2006 --k 1.5.2020                     # které znění bylo účinné k datu (od–do, novely)
$E zneni 182/2006                                 # historie všech časových znění (minulá, aktuální, BUDOUCÍ)
$E obsah 89/2012 [--uzel 645208419]               # systematika: části → hlavy → díly (rozbalení uzlem)
$E par 89/2012 "§ 2079"                           # text ustanovení (aktuální znění)
$E par 89/2012 "§ 2079 odst. 2" --k 2020-05-01    # text odstavce ve znění k datu
$E text 89/2012 --od "§ 2079" --do "§ 2084"       # souvislý rozsah ustanovení
$E text 89/2012 --k 2014-01-01 --format text      # celý text znění (velké kodexy = desítky tisíc řádků!)
$E diff 89/2012 --z 2025-07-01 --k 2026-01-01     # rozdíly mezi zněními (--par "§ 2079" zúží výstup)
$E souvislosti 182/2006 --typ JE_MENEN            # kdo novelizuje (MENI / JE_MENEN / RUSI / JE_RUSEN / PROVADI / NALEZY_US …)
$E castka sb 2025 100                             # obsah částky
$E raw GET "/dokumenty-sbirky/%2Fsb%2F2006%2F182/historie"        # libovolný endpoint (viz reference/api.md)
$E raw POST /jednoducha-vyhledavani '{"fulltext":"nadace","start":0,"pocet":5}'
```

Každý příkaz má `--json` (surová odpověď) nebo `--format json|html|text|md`; `-v` vypíše volané URL.

## Pracovní postup

1. **Ztotožni předpis.** Zná-li uživatel číslo, jdi rovnou na `info`; jinak `search` a vyber podle kódu a stavu
   (`AKTUALNE_PLATNY` / `ZRUSENY` / `VYHLASENY_BEZ_UCINNOSTI` – to jsou zejména nálezy ÚS a sdělení).
2. **Urči rozhodné datum.** Pro právní posouzení je určující znění účinné v den rozhodné skutečnosti
   (uzavření smlouvy, zahájení řízení, spáchání skutku, podání návrhu), nikoli dnešní. Bez data použij
   aktuální znění a výslovně to uveď. `info --k DATUM` vrátí přesný interval účinnosti znění a novely, které jej založily.
3. **Načti text** (`par` / `text`). U kodexů první stažení trvá několik sekund (text je stránkován po 1000 fragmentech),
   další dotazy jdou z cache.
4. **Cituj přesně.** V odpovědi vždy uveď: úplnou citaci předpisu, označení ustanovení, *znění účinné od … do …*
   a případně novelu, která znění založila. Vzor: „§ 2079 odst. 1 zákona č. 89/2012 Sb., občanský zákoník,
   ve znění účinném od 1. 12. 2018 do 30. 6. 2020 (novela č. 171/2018 Sb.)“.
5. **Změny v čase** řeš `zneni` (přehled) + `diff` (konkrétní rozdíly) nebo dvojím `par --k`. Upozorni na
   **budoucí znění** (`BUDOUCI`) a na poznámku „znění může být dotčené dosud nezpracovanou novelou“.
6. **Nálezy ÚS a derogace**: `souvislosti --typ NALEZY_US`, resp. fragmenty s `maDerogace`/`maNalezyUS` (`--format json`).

## Omezení a pasti

- Konsolidovaná znění před rokem 2024 jsou informativní (úřední konsolidace MV); pro autentický text
  novely použij vyhlášené znění částky (`castka`, `souvislosti --typ MENI`).
- Fulltext `search` hledá i v nálezech ÚS, sděleních a mezinárodních smlouvách – filtruj podle kódu a stavu.
- `nabidka-ustanoveni` (použitá v `par`) našeptává podle označení; u předpisů členěných na články zadej `"čl. 5"`.
- Datum ve staleUrl **před účinností předpisu** nebo po zrušení vrací `DOKUMENT_NENALEZEN` – použij `zneni` a vyber platný interval.
- Veřejné API je určeno pro čtení; limity nejsou publikovány – neprocházej hromadně celé sbírky, stahuj cíleně.
- Klíč nikdy nevkládej do SKILL.md, příkladů ani do gitu (pravidla repozitáře law-skills).

## Související zdroje

- `AGENTS.md` – rozhodovací strom, recepty, tvar výstupů, chyby a pravidla formulace odpovědi (pro agenty a automatizace).
- `README.md` – uživatelská dokumentace: instalace, získání klíče, přehled příkazů, řešení potíží.
- `reference/api.md` – katalog endpointů, tvary filtrů, číselníky (`RozsahVyhledavani`, `TypSouvislosti`, typy fragmentů).
- Judikatura k ustanovení: MCP **SLV** (`search_decisions` s `reg_num`/`reg_year`/`reg_par`).
- Alternativní neoficiální text: MCP `zakonyprolidi` – pro podání upřednostni e-Sbírku jako úřední zdroj.
