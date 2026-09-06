---
uuid: d43ced1e-7f34-4e5c-a810-17bcda834398
name: ustavni-stiznost-lidska-prava
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Ústavní stížnost a lidská práva"
    summary: "Přípustnost a vyčerpání opravných prostředků, dvouměsíční lhůta, sepis ústavní stížnosti, argumentace základními právy, test proporcionality, stížnost k ESLP, Listina EU a předběžná otázka."
    examplePrompts:
      - "Nejvyšší soud odmítl dovolání klienta pro nepřípustnost. Běží lhůta pro ústavní stížnost a proti čemu ji podat?"
      - "Připrav strukturu ústavní stížnosti proti rozsudku, který nereagoval na klíčovou námitku - jaké právo namítat a jakou judikaturu ÚS?"
      - "Ústavní soud stížnost odmítl jako zjevně neopodstatněnou. Do kdy a jak podat stížnost k ESLP a co musí obsahovat formulář?"
  en:
    displayName: "Czech Constitutional Complaint & Human Rights"
    summary: "Admissibility and exhaustion of remedies, the two-month deadline, drafting the petition, fundamental-rights argumentation, proportionality test, ECHR application, EU Charter and preliminary references."
    examplePrompts:
      - "The Supreme Court rejected my client's appeal on points of law as inadmissible. Is the constitutional complaint deadline running and what should it target?"
      - "Draft the structure of a constitutional complaint against a judgment that ignored a key objection - which right to invoke and which Constitutional Court case law?"
      - "The Constitutional Court dismissed the complaint as manifestly unfounded. By when and how do we apply to the ECHR and what must the form contain?"
  sk:
    displayName: "Ústavná sťažnosť a ľudské práva ČR"
    summary: "Prípustnosť a vyčerpanie opravných prostriedkov, dvojmesačná lehota, spísanie ústavnej sťažnosti, argumentácia základnými právami, test proporcionality, sťažnosť na ESĽP, Charta EÚ a prejudiciálna otázka."
    examplePrompts:
      - "Najvyšší súd odmietol dovolanie klienta pre neprípustnosť. Plynie lehota na ústavnú sťažnosť a proti čomu ju podať?"
      - "Priprav štruktúru ústavnej sťažnosti proti rozsudku, ktorý nereagoval na kľúčovú námietku - aké právo namietať a akú judikatúru ÚS?"
      - "Ústavný súd sťažnosť odmietol ako zjavne neopodstatnenú. Dokedy a ako podať sťažnosť na ESĽP a čo musí obsahovať formulár?"
description: Use when the user's matter involves fundamental rights or review by the Czech Constitutional Court or Strasbourg - ústavní stížnost, Ústavní soud, zákon o Ústavním soudu (182/1993 Sb.), Listina základních práv a svobod, lhůta dvou měsíců, vyčerpání opravných prostředků, přípustnost, zjevná neopodstatněnost, nález, usnesení, odklad vykonatelnosti, návrh na zrušení zákona, právo na spravedlivý proces, právo na soudní ochranu, překvapivé rozhodnutí, nepřezkoumatelnost, opomenutý důkaz, extrémní rozpor, libovůle, právo na zákonného soudce, právo vlastnit majetek, ochrana soukromí, svoboda projevu, test proporcionality, test racionality, Evropský soud pro lidská práva, ESLP, stížnost do Štrasburku, Úmluva o ochraně lidských práv, čtyřměsíční lhůta, spravedlivé zadostiučinění, Listina základních práv EU, předběžná otázka SDEU, ústavní stížnost obce. Standalone skill - bundles CODEXIS methodology with constitutional-litigation method; no need to load the general codexis skill.
---

# Ústavní stížnost a lidská práva ČR

Samostatný oborový skill pro ústavněprávní rovinu sporu. Základní reflex: **ústavní stížnost není další odvolání** - Ústavní soud nepřezkoumává podústavní správnost, ale jen zásah do základního práva; stížnost musí říct **které právo, jakým aktem, proč ústavně relevantně**. Druhý reflex: **lhůta dvou měsíců běží od doručení posledního rozhodnutí o posledním procesním prostředku** - a co je „poslední prostředek", je nejčastější důvod odmítnutí.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/182/1993/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf72'`, `cdx-cli get cdx://cz_law/2/1993/versions`, `cdx-cli search JD --query "ústavní stížnost přípustnost vyčerpání dovolání 75" --court "Ústavní soud" --limit 5`, `cdx-cli search ES --query "spravedlivý proces článek 6 Česká republika" --limit 5`.
- Judikaturu ÚS hledej primárně ve zdroji `JD` s filtrem na Ústavní soud, ESLP ve zdroji `ES`; u nálezů rozlišuj **nález (závazný čl. 89 odst. 2 Ústavy) × usnesení (odmítnutí, bez precedenční síly)** a **plénum × senát**. Lhůty, poplatky a náležitosti **ověř v aktuálním znění zákona o ÚS a jednacího řádu ESLP**; nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Ústava ČR | 1/1993 Sb. | `cz_law/1/1993` | Pravomoci ÚS (čl. 87), závaznost (čl. 89 odst. 2), mezinárodní smlouvy (čl. 10, čl. 10a), samospráva (čl. 100+) |
| Listina základních práv a svobod | 2/1993 Sb. | `cz_law/2/1993` | Katalog práv: rovnost (čl. 1, čl. 3), omezení práv (čl. 4), vlastnictví (čl. 11), soukromí (čl. 10, čl. 13), projev (čl. 17), podnikání (čl. 26), soudní ochrana (čl. 36), zákonný soudce (čl. 38), obhajoba (čl. 40) |
| Zákon o Ústavním soudu | 182/1993 Sb. | `cz_law/182/1993` | Ústavní stížnost (§ 72-§ 84: oprávnění, lhůta § 72 odst. 3-5, náležitosti § 34, přípustnost § 75, odmítnutí § 43, odklad § 79, nález § 82), návrh na zrušení zákona (§ 64+, akcesorický § 74), kompetenční spory (§ 120+), povinné zastoupení advokátem (§ 30), obnova řízení (§ 119) |
| Úmluva o ochraně lidských práv a základních svobod | sdělení 209/1992 Sb. | `cz_law/209/1992` | Čl. 3, 5, 6, 8, 10, 13, čl. 1 Protokolu 1; podmínky přijatelnosti (čl. 35 - lhůta 4 měsíce od konečného rozhodnutí, vyčerpání, významná újma), spravedlivé zadostiučinění (čl. 41) |
| Listina základních práv EU / SFEU | Úř. věst. C 202 / SFEU | zdroj `EU` | Čl. 47 Listiny EU, působnost čl. 51 (jen při provádění unijního práva), předběžná otázka čl. 267 SFEU |
| o. s. ř. / tr. ř. / s. ř. s. | 99/1963 / 141/1961 / 150/2002 Sb. | `cz_law/99/1963`, `cz_law/141/1961`, `cz_law/150/2002` | Poslední procesní prostředky (dovolání § 236+ o. s. ř., § 265a+ tr. ř., kasační stížnost § 102+ s. ř. s.), obnova řízení po nálezu / rozsudku ESLP (§ 228 o. s. ř., § 119 ZÚS, § 277 tr. ř.) |
| Zákon o odpovědnosti za škodu při výkonu veřejné moci | 82/1998 Sb. | `cz_law/82/1998` | Nezákonné rozhodnutí a nesprávný úřední postup po zrušujícím nálezu, nepřiměřená délka řízení (§ 13, § 31a), předběžné projednání (§ 14) |
| Zákon o soudech a soudcích | 6/2002 Sb. | `cz_law/6/2002` | Návrh na určení lhůty (§ 174a) jako prostředek proti průtahům - nutno vyčerpat před ÚS i ESLP |
| Antidiskriminační zákon | 198/2009 Sb. | `cz_law/198/2009` | Rovné zacházení, sdílené důkazní břemeno (§ 133a o. s. ř.) |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`; u lhůty a přípustnosti vždy aktuální § 72 a § 75 ZÚS (novely měnily počítání lhůty při odmítnutém dovolání).
2. Judikatura: **ÚS** - u každé námitky dohledej nález (ne jen usnesení) k danému právu: soudní ochrana a odůvodnění (překvapivost, opomenutý důkaz, extrémní rozpor mezi důkazy a závěry, přepjatý formalismus, libovůle), zákonný soudce, kontradiktornost, náklady řízení jako zásah, vlastnictví a legitimní očekávání, proporcionalita; **stanoviska pléna** (Pl. ÚS-st.) k přípustnosti a lhůtám; **ESLP** (`ES`) proti ČR i obecné leading cases k čl. 6 a čl. 8; **SDEU** k Listině EU. Ověř datum a zda nález nebyl překonán plénem (§ 23 ZÚS).
3. Komentář (`COMMENT`) a literatura (`LT`) k ZÚS a Listině; NALUS a databáze HUDOC jsou mimo CODEXIS oficiální zdroje pro plné texty a stav řízení.

## Workflow

1. **Kvalifikace zásahu.** Co je napadeno: rozhodnutí soudu/orgánu (§ 72 odst. 1 písm. a) ZÚS) × jiný zásah orgánu veřejné moci (nečinnost, faktický úkon, průtahy) × zákon nebo jeho ustanovení (jen akcesoricky s ústavní stížností § 74, samostatně jen privilegovaní navrhovatelé). Kdo stěžovatel (FO, PO, obec - § 72 odst. 1 písm. b) proti nezákonnému zásahu státu do samosprávy; stát a jeho orgány zpravidla ne). Které **základní právo** (Listina, Ústava, Úmluva, Listina EU v působnosti čl. 51) a jaký ústavně relevantní důvod - ne pouhá nesprávnost, ale kvalifikovaná vada (viz judikaturní typologie výše).
2. **Přípustnost a vyčerpání (§ 75 ZÚS).** Před ÚS musí být vyčerpány všechny procesní prostředky, které zákon k ochraně práva poskytuje, včetně **mimořádných** (dovolání, kasační stížnost; ne obnova řízení, ne stížnost pro porušení zákona, ne podnět k přezkumu) - a **odvolání i dovolání musí být řádně a přípustně podané** (dovolání odmítnuté pro vady nebo pro nevymezení přípustnosti = nevyčerpání → odmítnutí stížnosti). Proti průtahům nejprve návrh na určení lhůty (§ 174a ZSS). Výjimky § 75 odst. 2 (podstatný přesah vlastních zájmů, průtahy v řízení o opravném prostředku) jsou vykládány restriktivně. Stížnost směřuje proti **všem** rozhodnutím v řetězci (dovolací + odvolací + prvostupňové), ne jen proti poslednímu.
3. **Lhůta (§ 72 odst. 3-5 ZÚS).** **Dva měsíce od doručení rozhodnutí o posledním procesním prostředku**; při dovolání odmítnutém jako nepřípustné z důvodů závisejících na uvážení NS lze napadnout i předchozí rozhodnutí ve lhůtě běžící od doručení rozhodnutí o dovolání (§ 72 odst. 4 - ověř znění); u jiného zásahu od dne, kdy se stěžovatel dozvěděl, nejpozději do 1 roku (ověř). Lhůta je **procesní, nelze ji prominout**; podání u ÚS (datová schránka, e-podání s uznávaným podpisem, pošta - den podání). Počítej podle § 72 a obecných pravidel; před podáním vždy sepsat řetězec: rozhodnutí → datum doručení advokátovi (fikce) → konec lhůty.
4. **Náležitosti podání (§ 34, § 72 ZÚS).** Povinné zastoupení advokátem (§ 30 - speciální plná moc pro řízení před ÚS, advokát nemůže být sám stěžovatelem bez zastoupení - ověř judikaturu), označení napadených rozhodnutí a orgánů, tvrzení, které právo a jak bylo porušeno, **petit** (zrušení rozhodnutí; u zásahu zákaz pokračování a příkaz obnovit stav; návrh na odklad vykonatelnosti § 79 odst. 2; akcesorický návrh na zrušení zákona § 74; náhrada nákladů § 62 odst. 4 jen výjimečně), přílohy (kopie napadených rozhodnutí, plná moc), bez soudního poplatku. Struktura: I. rekapitulace řízení a lhůta, II. napadená rozhodnutí, III. přípustnost a vyčerpání, IV. ústavněprávní argumentace po jednotlivých právech (skutkový základ → norma → judikatura ÚS/ESLP → subsumpce), V. petit.
5. **Argumentační jádro.** U procesních práv (čl. 36 odst. 1, čl. 38 odst. 2 Listiny, čl. 6 Úmluvy): nedostatek odůvodnění a nevypořádání námitek, překvapivé rozhodnutí bez poučení (§ 118a o. s. ř.), opomenuté důkazy, extrémní rozpor skutkových zjištění, svévolný výklad, odepření přístupu k soudu přepjatým formalismem, nesprávné obsazení soudu, nerovnost zbraní, nepřiměřená délka. U hmotných práv: **test proporcionality** (legitimní cíl, vhodnost, potřebnost, přiměřenost v užším smyslu) u střetu práv (soukromí × projev, vlastnictví × veřejný zájem), **test racionality** u sociálních práv (čl. 41 odst. 1 Listiny), zákaz diskriminace (čl. 3 odst. 1), legitimní očekávání (čl. 1 Protokolu 1). Vždy: proč jde o ústavní, ne podústavní rovinu - a proč se nejedná o „čtvrtou instanci".
6. **Průběh řízení u ÚS.** Přidělení soudci zpravodaji (rozvrh práce), možnost odmítnutí bez jednání (§ 43 - opožděná, nepřípustná, neoprávněný navrhovatel, zjevně neopodstatněná, neodstraněné vady po výzvě), vyjádření účastníků a vedlejších účastníků (protistrana z původního řízení), replika, zpravidla bez ústního jednání (§ 44), **nález** (vyhovující - zrušení; zamítavý) × **usnesení** (odmítnutí). Odklad vykonatelnosti (§ 79) jen výjimečně - navrhnout s konkrétními důvody (nevratná újma). Po vyhovujícím nálezu: obecný soud vázán právním názorem (čl. 89 odst. 2), pokračuje v řízení; náhrada škody podle 82/1998 Sb. (nezákonné rozhodnutí = zrušené pro nezákonnost, předběžné projednání u ministerstva 6 měsíců, promlčení).
7. **ESLP.** Po vyčerpání (ústavní stížnost je poslední prostředek; odmítnutí pro zjevnou neopodstatněnost se počítá jako vyčerpání, odmítnutí pro nepřípustnost/opožděnost ne): **stížnost do 4 měsíců od doručení rozhodnutí ÚS** (čl. 35 odst. 1 Úmluvy - ověř, dříve 6 měsíců), výhradně na formuláři Soudu s přílohami, podaná poštou (datum odeslání), v úředním nebo národním jazyce; podmínky: významná újma, oběť porušení, ne totožná věc. Fáze: jednosoudcová filtrace (bez odůvodnění), komunikace vládě, smírné urovnání a jednostranné prohlášení, rozsudek; **spravedlivé zadostiučinění** čl. 41 (nároky vyčíslit ve stanovené lhůtě po komunikaci, jinak nepřiznáno); po rozsudku ESLP obnova řízení před ÚS (§ 119 ZÚS) nebo obecnými soudy (tr. ř.). Zástupce vlády ČR před ESLP je Ministerstvo spravedlnosti.
8. **Unijní rovina.** Listina EU se použije jen v působnosti unijního práva (čl. 51); u spotřebitele, DPH, azylu, GDPR, hospodářské soutěže apod. namítat čl. 47 Listiny EU a navrhnout **předběžnou otázku** (čl. 267 SFEU - soud poslední instance má povinnost s výjimkami CILFIT; nepoložení bez odůvodnění = porušení práva na zákonného soudce dle judikatury ÚS) - v ústavní stížnosti výslovně vytknout. Přednost unijního práva a povinnost eurokonformního výkladu.
9. **Prevence v nalézacím řízení.** Ústavní argumentaci uplatnit už u obecných soudů (zásada subsidiarity - ÚS odmítá námitky poprvé vznesené až před ním); v dovolání správně vymezit přípustnost (§ 237, § 241a odst. 2 o. s. ř.) včetně otázky ústavní konformity; v trestním řízení dovolací důvody § 265b tr. ř. + ústavní rozměr; uchovávat důkazy o doručení pro počítání lhůt.

## Časté pasti

- Dovolání odmítnuté pro vady nebo nevymezení přípustnosti = nevyčerpání prostředků → ústavní stížnost odmítnuta jako nepřípustná (a lhůta proti odvolacímu rozhodnutí mezitím uplynula).
- Stížnost jen proti rozhodnutí NS bez napadení rozhodnutí nižších soudů - ÚS nemůže zrušit, co nebylo napadeno.
- Lhůta počítaná od právní moci nebo od doručení klientovi místo od doručení zástupci; podání poslední den e-mailem bez uznávaného podpisu.
- Stížnost jako „čtvrtá instance": polemika se skutkovými zjištěními a výkladem podústavního práva bez ústavního rozměru → zjevná neopodstatněnost.
- Ústavní námitka poprvé až u ÚS (subsidiarita) nebo nová skutková tvrzení.
- Průtahy napadeny bez předchozího návrhu na určení lhůty (§ 174a ZSS) - nepřípustnost; u skončeného řízení jen náhrada podle 82/1998 Sb.
- Zastoupení obecnou plnou mocí nebo advokát-stěžovatel bez vlastního zástupce.
- Stížnost k ESLP po lhůtě čtyř měsíců, mimo formulář, bez kopií rozhodnutí, nebo po odmítnutí ÚS pro opožděnost (nevyčerpání).
- Listina EU namítána mimo působnost unijního práva.
- Odklad vykonatelnosti navrhován bez konkrétní nevratné újmy - nepřiznán.
- Spoléhání na usnesení ÚS jako „judikaturu" - závazný je nález; překonaná rozhodnutí bez kontroly plenárních stanovisek.
- Doplňování čísel jednacích, dat doručení a spisových značek z paměti - vždy ze spisu, doručenek nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a lhůta** (proti čemu, které právo, do kdy - výpočet z data doručení; co hrozí při nepodání).
2. **Přípustnost** - řetězec prostředků a jejich vyčerpání, rizika odmítnutí.
3. **Ústavněprávní argumentace** - tabulka: základní právo (čl.) | vada rozhodnutí | judikatura ÚS/ESLP | důkaz ve spise.
4. **Petit a návrhy** (zrušení, odklad, akcesorický návrh, náklady).
5. **Další kroky** (ESLP, obnova, náhrada škody, předběžná otázka).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace s rozlišením nález/usnesení.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Článek/paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `ÚS - I. ÚS 1234/24 - …`, `ÚS - Pl. ÚS 12/25 - …`, `ESLP - stížnost č. 12345/20 - …`) z metadat, nikdy vymyšlené; u ÚS uveď, zda jde o nález, nebo usnesení.
- Zachovej kvalifikátory („do dvou měsíců od doručení rozhodnutí o posledním procesním prostředku“, „všechny procesní prostředky, které zákon poskytuje“, „zjevně neopodstatněná“, „podstatně přesahuje vlastní zájmy“).
- Jeden časový řez; znění ZÚS a Úmluvy účinné v den doručení napadeného rozhodnutí.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty a podmínky přijatelnosti nikdy z paměti - vždy z aktuálního znění § 72, § 75 ZÚS a čl. 35 Úmluvy s odkazem; výpočet lhůty vždy ukázat.
- Nález × usnesení vždy rozlišit; usnesení nikdy nevydávat za závaznou judikaturu.
- Mimo CODEXIS jen oficiální zdroje (nalus.usoud.cz, hudoc.echr.coe.int, curia.europa.eu, justice.cz) když CODEXIS neodpovídá.
