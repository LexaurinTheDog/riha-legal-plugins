---
uuid: 8816d448-3893-4cdd-84e7-de45a5eafe98
name: trestni-obhajoba
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Trestní právo a obhajoba ČR"
    summary: "Obhajoba a zastupování poškozeného ve všech fázích trestního řízení - lhůty, vazba, zajištění majetku, odklony, opravné prostředky, trestní odpovědnost právnických osob."
    examplePrompts:
      - "Klientovi bylo dnes doručeno usnesení o zahájení trestního stíhání pro podvod. Co má obhájce udělat v prvních dnech?"
      - "Policie zajistila peníze na účtu klienta podle § 79a. Jak se bránit a jaké lhůty běží?"
      - "Připrav osnovu odvolání proti odsuzujícímu rozsudku - procesní vady a nesprávné hodnocení důkazů."
  en:
    displayName: "Czech Criminal Law and Defence"
    summary: "Defence and victim representation at every stage of Czech criminal proceedings - deadlines, custody, asset seizure, diversions, remedies, corporate liability."
    examplePrompts:
      - "My client was served today with a resolution commencing prosecution for fraud. What must defence counsel do in the first days?"
      - "Police froze funds on the client's account under § 79a. How do we challenge it and which deadlines run?"
      - "Draft an outline of an appeal against a conviction - procedural defects and flawed evaluation of evidence."
  sk:
    displayName: "Trestné právo a obhajoba ČR"
    summary: "Obhajoba a zastupovanie poškodeného vo všetkých fázach českého trestného konania - lehoty, väzba, zaistenie majetku, odklony, opravné prostriedky, zodpovednosť právnických osôb."
    examplePrompts:
      - "Klientovi bolo dnes doručené uznesenie o začatí trestného stíhania pre podvod. Čo má obhajca urobiť v prvých dňoch?"
      - "Polícia zaistila peniaze na účte klienta podľa § 79a. Ako sa brániť a aké lehoty bežia?"
      - "Priprav osnovu odvolania proti odsudzujúcemu rozsudku - procesné vady a nesprávne hodnotenie dôkazov."
description: Use when the user's matter is Czech criminal law or procedure in any role - obhájce, obviněný, obžalovaný, podezřelý, odsouzený, poškozený, zmocněnec, svědek, právnická osoba - or when a question touches trestní řád (141/1961 Sb.), trestní zákoník (40/2009 Sb.), zákon o trestní odpovědnosti právnických osob (418/2011 Sb.), trestní oznámení, prověřování, zahájení trestního stíhání, obvinění, výslech, vazba, zajištění majetku / peněžních prostředků (§ 79a+), domovní prohlídka, obžaloba, hlavní líčení, dohoda o vině a trestu, podmíněné zastavení, narovnání, trestní příkaz, odpor, stížnost, odvolání, dovolání, obnova řízení, ústavní stížnost, náhrada škody poškozenému (adhezní řízení), nutná obhajoba, trestné činy hospodářské, majetkové, daňové, dopravní, promlčení trestní odpovědnosti. Standalone skill - bundles CODEXIS methodology with defence-counsel method; no need to load the general codexis skill.
---

# Trestní právo a obhajoba ČR

Samostatný oborový skill pro trestní řízení. V trestním právu rozhodují dny: **nejprve fáze řízení a běžící lhůta, potom postavení klienta, teprve pak hmotné právo a strategie.**

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/141/1961/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf79a'`, `cdx-cli get cdx://cz_law/40/2009/versions`, `cdx-cli search JD --query "zajištění peněžních prostředků 79a stížnost" --court "Nejvyšší soud" --limit 5`.
- Trestní řád byl mnohokrát novelizován a **paragrafy o zajištění (§ 79a-§ 79h) byly přečíslovány novelou 55/2017 Sb.** - starší judikatura a komentáře cituje staré číslování. Hranice škody (§ 138 TZ) se měnily. **Každé číslo ověř v aktuálním znění**, nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| TŘ - trestní řád | 141/1961 Sb. | `cz_law/141/1961` | Celé řízení, vazba (§ 67+), zajištění (§ 79a+), obhájce (§ 33-§ 41), poškozený (§ 43+), opravné prostředky (§ 141+, § 245+, § 265a+, § 277+) |
| TZ - trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Skutkové podstaty, zavinění, promlčení (§ 34), hranice škody (§ 138), tresty a zásady ukládání |
| ZTOPO | 418/2011 Sb. | `cz_law/418/2011` | Trestní odpovědnost právnických osob, přičitatelnost (§ 8), vyvinění, tresty |
| ZSVM | 218/2003 Sb. | `cz_law/218/2003` | Mladiství |
| Zákon o obětech | 45/2013 Sb. | `cz_law/45/2013` | Práva obětí, peněžitá pomoc |
| Zákon o výkonu zajištění majetku | 279/2003 Sb. | `cz_law/279/2003` | Správa zajištěného majetku |
| Zákon o mezinárodní justiční spolupráci | 104/2013 Sb. | `cz_law/104/2013` | EZR, právní pomoc, uznávání |
| Zákon o Ústavním soudu | 182/1993 Sb. | `cz_law/182/1993` | Ústavní stížnost (§ 72 - lhůta, vyčerpání prostředků) |
| Advokátní tarif | 177/1996 Sb. | `cz_law/177/1996` | Odměna ustanoveného obhájce, náklady poškozeného |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`. U TŘ vždy zkontroluj `/versions` k datu úkonu - procesní úkony se posuzují podle znění účinného v době, kdy byly učiněny.
2. Judikatura: NS (`--court "Nejvyšší soud"`, senáty Tdo, Tz; sjednocující stanoviska Tpjn), ÚS (nálezy k vazbě, zajištění, právu na obhajobu, spravedlivý proces), vrchní soudy (To). Vždy ověř, zda rozhodnutí vychází z aktuálního číslování.
3. Komentář (`COMMENT`) pro znaky skutkových podstat a výklad procesních institutů; u zajištění majetku porovnej se zněním zákona - komentáře bývají zkratkovité (např. odkladný účinek stížnosti podle § 79f se týká jen některých rozhodnutí, § 79b připouští i „jiné určené místo“, nejen úschovu).

## Workflow obhájce

1. **Fáze a lhůty.** Prověřování (§ 158) → zahájení trestního stíhání (§ 160, usnesení - **stížnost 3 dny** § 143) → vyšetřování → vazba (§ 68, rozhodování soudce; stížnost) → seznámení se spisem (§ 166) → obžaloba (§ 176) / návrh na schválení dohody (§ 175a) → předběžné projednání (§ 185) → hlavní líčení (§ 196+) → rozsudek (**odvolání 8 dnů** § 248) / trestní příkaz (**odpor 8 dnů** § 314g) → odvolací řízení → **dovolání 2 měsíce** (§ 265e, jen prostřednictvím obhájce, jen z důvodů § 265b) → ústavní stížnost (2 měsíce, § 72 zákona 182/1993 Sb.) → obnova (§ 277+). Každou lhůtu ověř a uveď, od čeho běží (oznámení × doručení opisu).
2. **Postavení klienta.** Podezřelý / obviněný / obžalovaný / odsouzený / poškozený / svědek / zúčastněná osoba / právnická osoba (ZTOPO). Nutná obhajoba (§ 36) - kdy musí mít klient obhájce. Plná moc (§ 37), substituce, více obviněných = střet zájmů.
3. **Kvalifikace skutku.** Skutek × právní kvalifikace; znaky skutkové podstaty (objekt, objektivní stránka, subjekt, subjektivní stránka - úmysl × nedbalost § 15-§ 16 TZ); výše škody podle hranic § 138 TZ (ověř aktuální částky); pokus, příprava, spolupachatelství, účastenství; souběh; promlčení (§ 34 TZ - délka podle horní hranice sazby, přerušení); subsidiarita trestní represe (§ 12 odst. 2 TZ); zánik trestnosti (účinná lítost § 33, zvláštní případy - daňové § 242 TZ).
4. **Procesní audit.** Náležitosti usnesení o zahájení stíhání (§ 160 odst. 1 - popis skutku, zákonné znaky); zákonnost důkazů (§ 89 odst. 3, § 2 odst. 5, domovní prohlídka § 82-§ 85, odposlechy § 88, prostorové odposlechy § 158d); doručování obhájci (§ 62, § 64); právo nahlížet do spisu (§ 65); totožnost skutku (§ 220); vazební lhůty a důvody (§ 67, § 72-§ 72a); poučení. Každou vadu zapiš s § a důsledkem (nepoužitelnost důkazu × vada bez vlivu).
5. **Zajištění majetku a peněz (§ 79a-§ 79h TŘ).** Kdo rozhodl (policejní orgán se souhlasem SZ × SZ × soud), lhůta a povaha stížnosti, žádost o zrušení nebo omezení (§ 79f - opakování po lhůtě), náhradní hodnota, výjimky pro nutné výdaje, složení peněz do úschovy nebo na jiné určené místo (§ 79b). Zajištění není trest - argumentuj přiměřeností a délkou.
6. **Strategie.** Aktivní × pasivní obhajoba; návrhy na doplnění dokazování (§ 166, § 215); odklony (podmíněné zastavení § 307, narovnání § 309, trestní příkaz, dohoda o vině a trestu § 175a - výhody a nevratnost); spolupracující obviněný (§ 178a); polehčující okolnosti (§ 41 TZ), náhrada škody jako faktor; u PO compliance a vyvinění (§ 8 odst. 5 ZTOPO).
7. **Poškozený.** Nárok na náhradu škody / nemajetkové újmy / bezdůvodného obohacení uplatnit **nejpozději před zahájením dokazování v hlavním líčení** (§ 43 odst. 3); zajištění nároku (§ 47); zmocněnec (§ 51); práva podle zákona o obětech; odkaz na občanskoprávní řízení (§ 229) a jeho důsledky.

## Časté pasti

- Zmeškání třídenní lhůty ke stížnosti (počítá se od oznámení usnesení, ne od doručení obhájci - ověř § 137, § 143).
- Odvolání bez odůvodnění nebo bez vymezení výroků (§ 249) - výzva a riziko odmítnutí.
- Dovolání podané obviněným osobně nebo mimo důvody § 265b - odmítnutí.
- Citace § 79a-§ 79h ve starém číslování (před novelou 55/2017 Sb.) převzatá z komentáře nebo judikatury.
- Hranice škody § 138 TZ z paměti - částky se novelou změnily.
- Nárok poškozeného uplatněný až po zahájení dokazování - soud o něm nerozhodne.
- Záměna „skutek“ × „právní kvalifikace“ při argumentaci o totožnosti skutku.
- Přehlédnutí nutné obhajoby nebo střetu zájmů při obhajobě více obviněných.
- Předpoklad, že zajištění peněz je nezákonné jen kvůli délce - argumentovat přiměřeností s judikaturou ÚS.
- Doplňování jmen, spisových značek a dat z paměti - vždy ze spisu nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Nejbližší lhůta a úkon** v první větě (co, do kdy, komu).
2. **Fáze řízení a postavení klienta.**
3. **Právní rámec** - TŘ/TZ/ZTOPO v aktuálním znění, s odkazy.
4. **Procesní vady a argumenty** - seznam s § a důsledkem.
5. **Strategie a alternativy** (odklon × hlavní líčení, dohoda, náhrada škody), rizika každé cesty.
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 8 Tdo 123/2025 - …`, `ÚS - II. ÚS 123/25 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejpozději před zahájením dokazování“, „ode dne oznámení“, „jen prostřednictvím obhájce“).
- Jeden časový řez; u procesních úkonů znění účinné v době úkonu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (justice.cz, NS, ÚS, PČR) když CODEXIS neodpovídá.
- Nikdy neradit, jak mařit řízení nebo ovlivňovat svědky; obhajoba je procesní, ne obstrukční.
