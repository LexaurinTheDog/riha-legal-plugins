# e-Sbírka — zákony a jejich časová znění (uživatelská dokumentace)

> V pluginu `zdroje-slv` je skript v `skills/esbirka/scripts/esbirka.py`; instalace níže platí pro samostatné použití mimo plugin.

Skill `esbirka` odpovídá na otázky o českém právu přímo z **e-Sbírky**, oficiální elektronické Sbírky
zákonů a mezinárodních smluv provozované Ministerstvem vnitra. Jádro tvoří jeden skript bez závislostí,
`scripts/esbirka.py`, který volá veřejné REST rozhraní e-Sbírky a výsledky vypisuje jako přehledný text,
Markdown nebo surový JSON.

Typické otázky:

| Otázka | Příkaz |
|---|---|
| Jak zněl § 2079 občanského zákoníku k 1. 5. 2020? | `par 89/2012 "§ 2079" --k 1.5.2020` |
| Které znění insolvenčního zákona platilo 1. 6. 2019 a jaká novela ho založila? | `info 182/2006 --k 1.6.2019` |
| Kolik znění má zákon a kdy začne platit budoucí? | `zneni 182/2006` |
| Co se změnilo v § 757 OZ mezi 1. 7. 2025 a 1. 1. 2026? | `diff 89/2012 --z 2025-07-01 --k 2026-01-01 --par "§ 757"` |
| Které předpisy novelizují zákon o advokacii? | `souvislosti 85/1996 --typ JE_MENEN` |
| Čím byl zrušen starý občanský zákoník? | `info 40/1964` |
| Jak se jmenuje zákon č. 250/2016 Sb.? | `search "250/2016"` |

## Obsah adresáře

| Soubor | Účel |
|---|---|
| `SKILL.md` | Instrukce pro Claude Code (kdy skill použít, postup, pravidla citace) |
| `AGENTS.md` | Průvodce pro jiné agenty a automatizace: rozhodovací strom, recepty, tvar výstupů, chyby |
| `README.md` | Tento soubor — dokumentace pro člověka |
| `scripts/esbirka.py` | CLI klient (Python 3.9+, pouze standardní knihovna) |
| `reference/api.md` | Katalog REST endpointů, filtrů a číselníků e-Sbírky |
| `agents/openai.yaml` | Metadata pro prostředí kompatibilní s OpenAI/Codex skilly |
| `.claude-skill` | Metadata skillu (název, popis, triggery) |

## Instalace

Skill je součástí repozitáře `law-skills`. Instalátor repozitáře jej nakopíruje do `~/.claude/skills/esbirka`
a skript nasymlinkuje jako `~/.claude/esbirka.py`:

```bash
cd ~/law-skills && git pull && ./install.sh
```

Ruční instalace bez instalátoru:

```bash
cp -R esbirka ~/.claude/skills/esbirka
ln -sfn ~/.claude/skills/esbirka/scripts/esbirka.py ~/.claude/esbirka.py
```

Požadavky: Python 3.9 nebo novější (macOS: `python3` z Xcode Command Line Tools nebo Homebrew stačí),
přístup na internet k `api.e-sbirka.gov.cz` a `e-sbirka.gov.cz`. Žádné balíčky se neinstalují.

## Konfigurace

### API klíč (doporučeno)

Klíč přiděluje Ministerstvo vnitra, odbor strategického rozvoje a koordinace veřejné správy, na základě žádosti
o registraci odběru dat REST API zaslané datovou schránkou. Odpověď přijde jako dopis s podmínkami užití a klíčem.
Technická podpora API: esel@spcss.cz.

Klíč uložte do souboru `~/.claude/esbirka.env`:

```env
ESBIRKA_API_KEY=<klíč z dopisu MV>
```

```bash
chmod 600 ~/.claude/esbirka.env
python3 ~/.claude/esbirka.py diagnose
```

Očekávaný výstup diagnostiky:

```
env soubor: /Users/…/.claude/esbirka.env (existuje)
klíč: nastaven (65 znaků)
aktivní base: https://api.e-sbirka.gov.cz
  header esel-api-access-key → HTTP 200  …
✓ Funguje: header:esel-api-access-key (zapamatováno v ~/.cache/esbirka/auth.json)
```

Klíč se posílá v HTTP hlavičce `esel-api-access-key`. Dopis MV název hlavičky neuvádí; jiná hlavička
vrací `401 NEPLATNY_API_KLIC: Nezaslán API klíč`. Skript má tuto hlavičku jako výchozí, při 401 vyzkouší záložní
varianty a funkční si zapamatuje.

Podmínky užití z dopisu MV ve zkratce: klíč jen pro vlastní organizaci a účel z žádosti, nesdílet, nepřetěžovat
API nad nahlášený počet volání, data jsou informativní a mohou se měnit, do 15. 1. 2027 může MV rozhraní upravovat.

### Bez klíče

Bez souboru s klíčem skript automaticky použije veřejnou cache portálu `https://e-sbirka.gov.cz/sbr-cache`,
kterou čte samotný web e-Sbírky. Cesty i data jsou totožné, rozhraní ale není určeno pro strojové odběry
a MV k němu neposkytuje podporu. Vynutit ji lze přepínačem `--verejne` (užitečné pro srovnání nebo při výpadku API).

I s klíčem skript část dotazů posílá do cache portálu: API s klíčem nenabízí systematiku (`obsah`), srovnání znění
(`diff`) ani přehled znění ke srovnání. Skript to pozná podle odpovědi 404 a dotaz jednorázově zopakuje v cache;
s přepínačem `-v` to vypíše na chybový výstup.

### Další proměnné

| Proměnná (env soubor nebo prostředí) | Význam |
|---|---|
| `ESBIRKA_API_KEY` | klíč k API |
| `ESBIRKA_BASE` | jiná základní URL (výchozí `https://api.e-sbirka.gov.cz`, bez klíče cache portálu) |
| `ESBIRKA_AUTH` | napevno způsob autentizace, např. `header:esel-api-access-key` |

Lokální cache stažených stránek textu je v `~/.cache/esbirka/` (platnost 7 dní). Při podezření na zastaralý
text ji smažte nebo použijte `--no-cache`.

## Rychlý start

```bash
E="python3 $HOME/.claude/esbirka.py"

$E search "insolvenční zákon" --pocet 5
$E info 182/2006 --k 1.6.2019
$E zneni 182/2006
$E par 89/2012 "§ 2079 odst. 2" --k 1.5.2020
$E text 89/2012 --od "§ 2079" --do "§ 2084"
$E diff 89/2012 --z 2025-07-01 --k 2026-01-01 --par "§ 757"
$E souvislosti 85/1996 --typ JE_MENEN
```

## Jak zadávat předpis a datum

Předpis lze zapsat kterýmkoli z těchto způsobů: `89/2012`, `89/2012 Sb.`, `č. 89/2012 Sb.`, `zák. č. 89/2012 Sb.`,
`6/2021 Sb. m. s.`, `/sb/2012/89`, `/sb/2012/89/2026-01-01`.

Datum přijímá `2020-05-01` i `1. 5. 2020`. Zadané datum znamená **znění účinné k tomuto dni**; e-Sbírka je sama
převede na počátek příslušného znění (například `--k 1.5.2020` u občanského zákoníku vrátí znění účinné od
1. 12. 2018 do 30. 6. 2020). Bez data se pracuje s aktuálním zněním.

## Přehled příkazů

| Příkaz | Co dělá | Důležité volby |
|---|---|---|
| `search DOTAZ` | fulltextové vyhledání předpisů, nálezů ÚS, sdělení a smluv | `--pocet`, `--start`, `--json` |
| `info PŘEDPIS` | metadata znění: úplná citace, interval účinnosti, novely, zrušení, částka | `--k DATUM`, `--json` |
| `zneni PŘEDPIS` | historie všech časových znění včetně budoucích | `--json` |
| `obsah PŘEDPIS` | systematika (části, hlavy, díly) s rozsahem paragrafů | `--k`, `--uzel ID` pro rozbalení |
| `par PŘEDPIS "§ N"` | text ustanovení včetně podřízených odstavců a písmen | `--k`, `--format md/text/html/json` |
| `text PŘEDPIS` | celý text znění nebo souvislý rozsah | `--od "§ A" --do "§ B"`, `--k`, `--format` |
| `diff PŘEDPIS --z D1 --k D2` | rozdíly mezi zněními s vyznačením vloženého a vypuštěného textu | `--par "§ N"`, `--json` |
| `souvislosti PŘEDPIS` | vazby: novelizuje, je novelizován, ruší, je rušen, provádí, nálezy ÚS | `--typ`, `--limit` |
| `castka SBÍRKA ROK ČÍSLO` | metadata částky a odkaz na právně závazné PDF | `--json` |
| `raw GET/POST CESTA [JSON]` | libovolný endpoint (viz `reference/api.md`) | |
| `diagnose` | ověření klíče, hlavičky a dostupnosti | |

Globální přepínače před názvem příkazu: `--verejne`, `--base URL`, `--no-cache`, `-v` (vypíše volané URL).

## Ukázky výstupu

`info 40/1964 --k 2013-06-01`:

```
Zákon č. 40/1964 Sb., Občanský zákoník
minulé znění, účinné od 1. 1. 2013 do 31. 12. 2013  (staleUrl /sb/1964/40/2013-01-01, ELI /eli/cz/sb/1964/40/2013-01-01)
ZRUŠEN k 1. 1. 2014 předpisem 89/2012 Sb.
novely tohoto znění: 428/2011 Sb.
vyhlášen: 5. 3. 1964, částka 19/1964, účinnost předpisu od 1. 4. 1964
```

`zneni 182/2006` (zkráceno):

```
Časová znění /sb/2006/182 (52):
- č.  51    10. 1. 2030 – …             BUDOUCÍ   /sb/2006/182/2030-01-10   novely: 317/2025 Sb.
- č.  50     1. 1. 2027 – 9. 1. 2030    BUDOUCÍ   /sb/2006/182/2027-01-01   novely: 360/2025 Sb.
- č.  49     1. 1. 2026 – 31. 12. 2026  AKTUÁLNÍ  /sb/2006/182/2026-01-01   novely: 268/2025 Sb.
- č.  48    15. 2. 2025 – 31. 12. 2025  minulé    /sb/2006/182/2025-02-15   novely: 32/2025 Sb.
```

`diff 89/2012 --z 2025-07-01 --k 2026-01-01 --par "§ 757"` (zkráceno):

```
### § 757
[UPRAVA] § 757 odst. 1 písm. a) zákona č. 89/2012 Sb.
a) ke dni zahájení řízení o rozvod trvalo manželství nejméně jeden rok ~~a manželé spolu déle než šest měsíců nežijí~~,
```

## Odkazy pro klienty a podání

Každý výstup obsahuje `staleUrl`. Veřejný odkaz vznikne připojením k doméně portálu:
`https://e-sbirka.gov.cz/sb/2012/89/2026-01-01`, na ustanovení `https://e-sbirka.gov.cz/sb/2012/89/2026-01-01#par_2079`.
Právně závazné PDF částky vrací příkaz `castka`.

## Řešení potíží

| Projev | Příčina a řešení |
|---|---|
| `401 NEPLATNY_API_KLIC: Nezaslán API klíč` | klíč se posílá špatnou hlavičkou; spusťte `diagnose`, případně `ESBIRKA_AUTH=header:esel-api-access-key` |
| `400 DOKUMENT_NENALEZEN … staleUrl: /sb/1964/40/2026-01-01` | k zadanému datu předpis nebyl účinný (před účinností nebo po zrušení); `zneni` ukáže platné intervaly |
| `Ustanovení '§ 5' v /sb/… nenalezeno` | předpis je členěn na články (`"čl. 5"`) nebo ustanovení v daném znění neexistuje |
| `search` vrací desítky tisíc výsledků | tělo dotazu bylo prázdné nebo příliš obecné; hledejte číslem předpisu nebo přesnějším názvem |
| první `par`/`text` u kodexu trvá 5–15 s | text se stahuje po stránkách o 1000 fragmentech; další dotazy jdou z cache |
| `Chyba spojení` | výpadek sítě nebo API; zkuste `--verejne` |

## Bezpečnost

- Klíč patří pouze do `~/.claude/esbirka.env` s právy 600. Nikdy do repozitáře, do příkladů ani do chatu.
- Dopis MV s klíčem (PDF) uložte do správce hesel a odstraňte ze složky Stažené.
- Skript neodesílá nikam nic kromě dotazů na e-Sbírku; cache v `~/.cache/esbirka/` obsahuje jen veřejné texty předpisů.

## Právní upozornění

Konsolidovaná znění v e-Sbírce jsou úřední konsolidací MV a podle podmínek užití API jsou informativní.
Právně závazné je vyhlášené znění v částce Sbírky (od 1. 1. 2024 elektronické PDF s podpisem, dostupné přes `castka`).
Pro podání citujte předpis, ustanovení a interval účinnosti znění, které skript vypíše v hlavičce každé odpovědi.
