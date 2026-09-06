---
uuid: 2615c2b4-1f93-4647-a845-157740ee62ba
name: dedicke-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dědické právo ČR"
    summary: "Závěť a dědická smlouva, nepominutelní dědici, vydědění, odmítnutí a výhrada soupisu, dluhy zůstavitele, pozůstalostní řízení u notáře, spory, plánování majetku."
    examplePrompts:
      - "Zemřel otec, zanechal závěť jen ve prospěch družky a dluhy z podnikání. Co mají děti udělat a do kdy?"
      - "Připrav alografní závěť s vyděděním syna pro trvalé neprojevování zájmu - jaké jsou náležitosti a rizika?"
      - "Notář odkázal klienta k žalobě o dědické právo. Jak formulovat petit a jaká běží lhůta?"
  en:
    displayName: "Czech Inheritance Law"
    summary: "Wills and inheritance contracts, forced heirs, disinheritance, renunciation and inventory reservation, estate debts, probate before the notary, disputes, estate planning."
    examplePrompts:
      - "A father died leaving a will only in favour of his partner and business debts. What should the children do and by when?"
      - "Draft a witnessed will disinheriting a son for persistent lack of interest - requirements and risks?"
      - "The notary referred my client to file an action on the right of inheritance. How to phrase the claim and what deadline runs?"
  sk:
    displayName: "Dedičské právo ČR"
    summary: "Závet a dedičská zmluva, neopomenuteľní dedičia, vydedenie, odmietnutie a výhrada súpisu, dlhy poručiteľa, dedičské konanie u notára v ČR, spory, plánovanie majetku."
    examplePrompts:
      - "Zomrel otec, zanechal závet len v prospech družky a dlhy z podnikania. Čo majú deti urobiť a dokedy?"
      - "Priprav alografný závet s vydedením syna pre trvalé neprejavovanie záujmu - aké sú náležitosti a riziká?"
      - "Notár odkázal klienta na žalobu o dedičské právo. Ako formulovať petit a aká lehota beží?"
description: Use when the user's matter involves Czech inheritance or succession - dědictví, pozůstalost, zůstavitel, dědic, závěť (holografní, alografní, notářská), dědická smlouva, odkaz, dovětek, náhradnictví, svěřenské nástupnictví, zákonná posloupnost, dědické třídy, nepominutelný dědic, povinný díl, vydědění, dědická nezpůsobilost, zřeknutí se dědictví, odmítnutí dědictví, vzdání se dědictví, výhrada soupisu, dluhy zůstavitele, likvidace pozůstalosti, odúmrť, správa pozůstalosti, vykonavatel závěti, pozůstalostní řízení, notář jako soudní komisař, usnesení o dědictví, spor o dědické právo, dodatečné projednání, vypořádání SJM v pozůstalosti, dědění podílu ve společnosti, evropské dědické osvědčení, nařízení 650/2012, plánování majetku pro případ smrti, svěřenský fond, darování pro případ smrti. Standalone skill - bundles CODEXIS methodology with inheritance-practice method; no need to load the general codexis skill.
---

# Dědické právo ČR

Samostatný oborový skill pro dědění a pozůstalostní řízení. Pořadí je pevné: **rozhodné právo a titul → okruh dědiců → rozhodnutí dědice (odmítnout / výhrada soupisu) → pasiva → řízení u notáře**. Nejdražší chyby vznikají v prvním měsíci po vyrozumění o dědickém právu.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf1485'`, `cdx-cli get cdx://cz_law/292/2013/versions`, `cdx-cli search JD --query "vydědění neprojevování zájmu 1646" --court "Nejvyšší soud" --limit 5`.
- Lhůty, zlomky povinného dílu, poplatky a odměnu notáře **vždy ověř v aktuálním znění**; nikdy z paměti. U úmrtí před 1. 1. 2014 platí přechodná ustanovení (§ 3069+ OZ) - dědění se řídí právem účinným v den smrti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - dědické právo | 89/2012 Sb. | `cz_law/89/2012` | § 1475-§ 1720: dědické tituly (§ 1476), nezpůsobilost (§ 1481), zřeknutí (§ 1484), odmítnutí (§ 1485-§ 1490), závěť (§ 1494-§ 1581), dědická smlouva (§ 1582+), odkaz (§ 1594+), zákonná posloupnost (§ 1635-§ 1641), nepominutelný dědic (§ 1642-§ 1645, § 1654), vydědění (§ 1646-§ 1649), započtení (§ 1658+), výhrada soupisu (§ 1674+), správa (§ 1677+), dohoda dědiců (§ 1694+), dluhy (§ 1701-§ 1713) |
| ZŘS - řízení o pozůstalosti | 292/2013 Sb. | `cz_law/292/2013` | § 98-§ 288: notář soudní komisař (§ 100+), předběžné šetření, soupis, spor o dědické právo (§ 168-§ 170), usnesení (§ 184-§ 185), likvidace (§ 195+), dodatečné projednání (§ 192-§ 193), evropské dědické osvědčení (§ 288a) |
| Nařízení o dědictví | (EU) 650/2012 | zdroj `EU` | Příslušnost a rozhodné právo podle obvyklého pobytu, volba práva, evropské dědické osvědčení |
| ZMPS | 91/2012 Sb. | `cz_law/91/2012` | Mimo dosah nařízení |
| Notářský řád + notářský tarif | 358/1992 Sb., vyhl. 196/2001 Sb. | `cz_law/358/1992`, `cz_law/196/2001` | Závěti a smlouvy notářským zápisem, Evidence právních jednání pro případ smrti, odměna komisaře |
| ZOK | 90/2012 Sb. | `cz_law/90/2012` | Dědění podílu (§ 42 - lze u s.r.o. vyloučit), družstevní podíl |
| Katastrální zákon | 256/2013 Sb. | `cz_law/256/2013` | Záznam dědice podle usnesení |
| ZDP / daň z nemovitých věcí | 586/1992 / 338/1992 Sb. | `cz_law/586/1992`, `cz_law/338/1992` | Bezúplatné nabytí děděním osvobozeno (§ 4a ZDP - ověř), přiznání nového vlastníka |
| Insolvenční zákon | 182/2006 Sb. | `cz_law/182/2006` | Insolvence zůstavitele / dědice, likvidace předlužené pozůstalosti |

## Rešeršní strategie

1. Paragraf známý → `/versions` k datu úmrtí → `/toc` → `/text?part=`. Dědické právo OZ 2012 má přechodná ustanovení (§ 3069-§ 3072) - závěť pořízená před 2014 se posuzuje co do formy podle tehdejšího práva.
2. Judikatura NS: senát **24 Cdo** (dědické právo) - `--court "Nejvyšší soud"`; témata: platnost závěti a svědci, vydědění, neprojevování zájmu, započtení, výhrada soupisu, spor o dědické právo; ÚS k právu na spravedlivý proces v pozůstalostním řízení.
3. Komentář (`COMMENT`) k neurčitým pojmům (trvalé neprojevování zájmu, opomenutí, přiměřený zájem); vzory (`VS`) závětí a dohod - sladit s aktuálním zněním a formou.

## Workflow dědického praktika

1. **Rozhodné právo a příslušnost.** Datum úmrtí (před/po 1. 1. 2014 a 17. 8. 2015), obvyklý pobyt zůstavitele (nařízení 650/2012 - příslušnost i rozhodné právo; volba práva státní příslušnosti), majetek v zahraničí (evropské dědické osvědčení).
2. **Dědické tituly a jejich hierarchie.** Dědická smlouva > závěť > zákon (§ 1476); pozdější závěť ruší dřívější v rozsahu rozporu (§ 1576); kontrola platnosti: forma (vlastnoruční § 1533; alografní § 1534 - dva současně přítomní svědci, kteří nesmí být dědici, odkazovníky ani osobami jim blízkými § 1539-§ 1540; notářský zápis § 1537; s úlevami § 1542), pořizovací způsobilost (§ 1525-§ 1528), určitost, podmínky a příkazy (§ 1551+), Evidence právních jednání pro případ smrti u Notářské komory.
3. **Okruh dědiců.** Zákonné třídy (§ 1635-§ 1641, šest tříd, reprezentace), nepominutelný dědic - jen potomci (§ 1643), povinný díl v penězích (§ 1654 - nezletilý a zletilý mají odlišný zlomek; ověř), započtení darů (§ 1658-§ 1664 - u zákonné posloupnosti jen na příkaz zůstavitele nebo u nepominutelného), vydědění (důvody § 1646 taxativní, zadlužení § 1647, opomenutí nepominutelného dědice § 1651), dědická nezpůsobilost (§ 1481-§ 1483), zřeknutí se smlouvou se zůstavitelem (§ 1484 - notářský zápis).
4. **Rozhodnutí dědice - první lhůta.** Odmítnutí (§ 1485-§ 1490): do **1 měsíce** od vyrozumění o dědickém právu (3 měsíce při jediném bydlišti v zahraničí - ověř), výslovným prohlášením u notáře, nelze po projevu přijetí ani po nakládání s pozůstalostí (§ 1489), nepominutelný dědic může odmítnout s výhradou povinného dílu; vzdání se ve prospěch jiného dědice (§ 1490); **výhrada soupisu** (§ 1674-§ 1676) - jediná ochrana před dluhy nad hodnotu nabytého majetku; bez ní dědic hradí dluhy plně (§ 1701).
5. **Pasiva.** Dluhy zůstavitele a náklady pohřbu (§ 1701-§ 1713), solidarita dědiců, věřitelé (výzva, svolání § 1711), ISIR zůstavitele, předlužení → likvidace pozůstalosti (§ 195+ ZŘS) nebo insolvence; ručení za dluhy manžela (SJM).
6. **SJM a jiné vypořádání.** Vypořádání SJM při zániku smrtí (§ 764 OZ, § 162-§ 163 ZŘS) předchází určení pozůstalosti; podíl v s.r.o. (§ 42 ZOK - dědění lze vyloučit, pak vypořádací podíl), družstevní podíl, autorská práva, bankovní účty, pojistky s obmyšleným (mimo pozůstalost).
7. **Řízení u notáře.** Zahájení z úřední povinnosti (§ 138 ZŘS), předběžné šetření (§ 139), soupis / společné prohlášení / seznam, spor o dědické právo - notář odkáže toho, jehož právo se jeví méně pravděpodobné, k žalobě ve lhůtě (§ 168-§ 170 ZŘS; zmeškání = pokračuje se bez něj), dohoda dědiců (§ 1694+ OZ, schválení § 185 ZŘS), usnesení o dědictví, odvolání 15 dnů, odměna notáře podle hodnoty (tarif), dodatečné projednání nově najevo vyšlého majetku (§ 192-§ 193 ZŘS).
8. **Po skončení.** Katastr (záznam na základě usnesení), obchodní rejstřík, banky, daňové přiznání k dani z nemovitých věcí, příjem z dědictví osvobozen od daně z příjmů (ověř § 4a ZDP), evidence skutečných majitelů.
9. **Plánování pro případ smrti.** Závěť × dědická smlouva (§ 1582+ - nejvýše 3/4 pozůstalosti, notářský zápis) × darování pro případ smrti (§ 2063) × svěřenský fond (§ 1448+) × pojištění s obmyšleným; vykonavatel závěti (§ 1553), správce pozůstalosti (§ 1556), náhradnictví a svěřenské nástupnictví (§ 1507, § 1512), ochrana povinného dílu.

## Časté pasti

- Zmeškání měsíční lhůty k odmítnutí nebo konkludentní přijetí nakládáním s majetkem (§ 1489) - dědic ručí za dluhy.
- Neuplatnění výhrady soupisu u zadluženého zůstavitele - odpovědnost za dluhy bez omezení.
- Alografní závěť se svědkem, který je dědicem nebo osobou blízkou dědice - neplatná v této části.
- Vydědění bez zákonného důvodu nebo bez jeho uvedení - nepominutelný dědic má povinný díl.
- Nepominutelný dědic brán jako dědic s podílem na věcech - má jen právo na peněžitý povinný díl (§ 1654).
- Závěť z doby před 2014 posuzovaná podle OZ 2012 co do formy (přechodná ustanovení).
- Dědění podílu v s.r.o. bez kontroly společenské smlouvy (§ 42 ZOK) - podíl nemusí přejít.
- Opomenutí vypořádání SJM před rozdělením pozůstalosti.
- Zmeškání lhůty k žalobě o dědické právo po odkazu notářem - řízení pokračuje bez odkázaného.
- Majetek v jiném státě EU řešený jen českým usnesením bez evropského dědického osvědčení.
- Doplňování dat úmrtí, jmen a hodnot majetku z paměti - vždy z listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (odmítnout / přijmout s výhradou soupisu / napadnout titul - do kdy).
2. **Rozhodné právo, tituly a okruh dědiců.**
3. **Právní rámec** - OZ/ZŘS v aktuálním znění k datu úmrtí, s odkazy.
4. **Postup v řízení** (co u notáře, jaké listiny, jaká prohlášení, jaké spory).
5. **Pasiva a rizika** (dluhy, SJM, insolvence, podíly ve společnostech).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 24 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do jednoho měsíce ode dne, kdy byl vyrozuměn“, „ledaže“, „za současné přítomnosti“).
- Jeden časový řez; u dědění znění účinné v den smrti zůstavitele.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (Notářská komora, justice.cz, katastr, ISIR) když CODEXIS neodpovídá.
- Zlomky, lhůty, sazby a odměny nikdy z paměti - vždy z aktuálního znění s odkazem.
