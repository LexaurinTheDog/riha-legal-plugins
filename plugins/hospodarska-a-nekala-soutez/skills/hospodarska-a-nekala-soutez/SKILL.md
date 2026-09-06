---
uuid: 2914684d-f296-46fe-b4a9-452343588299
name: hospodarska-a-nekala-soutez
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Hospodářská a nekalá soutěž ČR"
    summary: "Kartely, zneužití dominance, spojování soutěžitelů a řízení před ÚOHS, náhrada škody, nekalá soutěž a její nároky, regulace reklamy a nekalé obchodní praktiky."
    examplePrompts:
      - "Distributor nám v e-mailu píše, ať nedáváme cenu pod jeho doporučenou. Je to problém a co s tím?"
      - "Konkurent v reklamě tvrdí, že náš výrobek je nebezpečný. Jaké nároky máme a jak rychle?"
      - "ÚOHS provedl u klienta místní šetření. Jaká má klient práva a co dělat v prvních dnech?"
  en:
    displayName: "Czech Competition and Unfair Competition"
    summary: "Cartels, abuse of dominance, merger control and ÚOHS proceedings, damages, unfair competition claims, advertising regulation and unfair commercial practices."
    examplePrompts:
      - "A distributor e-mails us not to price below its recommended price. Is that a problem and what to do?"
      - "A competitor's advertising claims our product is dangerous. Which claims do we have and how fast?"
      - "The ÚOHS carried out a dawn raid at the client's premises. What are the client's rights and what to do in the first days?"
  sk:
    displayName: "Hospodárska a nekalá súťaž ČR"
    summary: "Kartely, zneužitie dominancie, koncentrácie a konanie pred ÚOHS, náhrada škody, nekalá súťaž a jej nároky, regulácia reklamy a nekalé obchodné praktiky v ČR."
    examplePrompts:
      - "Distribútor nám v e-maile píše, aby sme nedávali cenu pod jeho odporúčanú. Je to problém a čo s tým?"
      - "Konkurent v reklame tvrdí, že náš výrobok je nebezpečný. Aké nároky máme a ako rýchlo?"
      - "ÚOHS vykonal u klienta miestne šetrenie. Aké má klient práva a čo robiť v prvých dňoch?"
description: Use when the user's matter involves Czech or EU competition law, unfair competition, advertising or consumer practices - zákon o ochraně hospodářské soutěže (143/2001 Sb.), kartel, zakázaná dohoda, horizontální, vertikální dohoda, určování cen, RPM, bid rigging, výměna informací, dominantní postavení, zneužití, predátorské ceny, odmítnutí dodávek, spojení soutěžitelů, fúze, notifikace ÚOHS, gun jumping, místní šetření, dawn raid, leniency, narovnání, pokuta, náhrada škody z porušení soutěžního práva (262/2017 Sb.), významná tržní síla (395/2009 Sb.), čl. 101 a 102 SFEU, bloková výjimka, DMA, nekalá soutěž (§ 2976-§ 2990 OZ), klamavá reklama, srovnávací reklama, parazitování, vyvolání nebezpečí záměny, zlehčování, obchodní tajemství, regulace reklamy (40/1995 Sb.), nekalé obchodní praktiky, ČOI, RRTV, influencer marketing, greenwashing, konkurenční doložka. Standalone skill - bundles CODEXIS methodology with competition-practice method; no need to load the general codexis skill.
---

# Hospodářská a nekalá soutěž ČR

Samostatný oborový skill pro soutěžní právo v obou větvích. První otázka: **veřejnoprávní soutěžní právo (ÚOHS, Komise, pokuty) × soukromoprávní nekalá soutěž (soud, nároky) × ochrana spotřebitele a reklama (ČOI, RRTV)** - tentýž skutek často spadá do dvou nebo tří větví s různými orgány, lhůtami a důkazním břemenem.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/143/2001/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf3'`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2976'`, `cdx-cli search JD --query "parazitování na pověsti nekalá soutěž 2982" --court "Nejvyšší soud" --limit 5`, `cdx-cli search EU --query "nařízení 2022/720 vertikální dohody bloková výjimka" --limit 5`.
- Prahy obratů pro notifikaci, podíly pro domněnku dominance a de minimis, výše pokut a lhůty **ověř v aktuálním znění**; nikdy z paměti. Rozhodovací praxe ÚOHS a Komise je v CODEXIS jen zčásti - odkazuj na uohs.gov.cz a eur-lex.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| ZOHS - zákon o ochraně hospodářské soutěže | 143/2001 Sb. | `cz_law/143/2001` | Zakázané dohody (§ 3-§ 4), dominance a zneužití (§ 10-§ 11), spojení (§ 12-§ 19), ÚOHS a řízení (§ 20-§ 21c), místní šetření (§ 21f-§ 21g), pokuty, leniency, narovnání (§ 22-§ 22bb) |
| Zákon o náhradě škody v oblasti hospodářské soutěže | 262/2017 Sb. | `cz_law/262/2017` | Soukromé vymáhání - domněnky, zpřístupnění důkazů, promlčení, solidarita |
| Zákon o významné tržní síle | 395/2009 Sb. | `cz_law/395/2009` | Nekalé praktiky v potravinovém řetězci, ÚOHS |
| OZ - nekalá soutěž | 89/2012 Sb. | `cz_law/89/2012` | Generální klauzule (§ 2976), skutkové podstaty (§ 2977-§ 2987), nároky (§ 2988), důkazní břemeno (§ 2989), obchodní tajemství (§ 504), konkurenční doložka (§ 2975) |
| Zákon o regulaci reklamy | 40/1995 Sb. | `cz_law/40/1995` | Zakázaná a regulovaná reklama, dozorové orgány, sankce |
| Zákon o ochraně spotřebitele | 634/1992 Sb. | `cz_law/634/1992` | Nekalé obchodní praktiky (§ 4-§ 5b, přílohy), ČOI |
| SFEU + nařízení 1/2003 | čl. 101-102 | zdroj `EU` | Unijní soutěžní právo, přímá aplikace, spolupráce s Komisí |
| Blokové výjimky | (EU) 2022/720 (vertikální), 2023/1066 (technologie), 1218/2010, 1217/2010 | zdroj `EU` | Bezpečné přístavy pro dohody |
| Nařízení o spojování | (ES) 139/2004 | zdroj `EU` | Spojení s unijním rozměrem |
| DMA - akt o digitálních trzích | (EU) 2022/1925 | zdroj `EU` | Strážci přístupu |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Porušení předpisů o pravidlech hospodářské soutěže (§ 248), pletichy (§ 257) |
| o. s. ř. / s. ř. s. | 99/1963 / 150/2002 Sb. | `cz_law/99/1963`, `cz_law/150/2002` | Krajský soud pro nekalou soutěž (§ 9 odst. 2), předběžné opatření; žaloby proti ÚOHS (KS Brno) |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`; unijní předpisy a pokyny Komise ze zdroje `EU`.
2. Judikatura: **NS** senát 23 Cdo (nekalá soutěž, konkurenční doložky), **VS Praha / VS Olomouc** (odvolací v nekalé soutěži), **NSS** a **KS Brno** (přezkum ÚOHS - dawn raid, pokuty, spojení), **SDEU / Tribunál** (`ES` - Intel, Google, Cartes Bancaires, Budapest Bank, Super Bock k RPM). Ověř, zda rozhodnutí nevychází z předchozího znění blokové výjimky.
3. Komentář (`COMMENT`) k pojmům (soutěžitel, relevantní trh, dobré mravy soutěže, způsobilost přivodit újmu); pokyny Komise a ÚOHS (de minimis, vertikální pokyny) jsou soft law s vysokou praktickou váhou.

## Workflow

1. **Kvalifikace a větev.** Dohoda mezi soutěžiteli / jednostranné jednání dominanta / spojení × jednání v hospodářském styku v rozporu s dobrými mravy soutěže způsobilé přivodit újmu (§ 2976) × praktika vůči spotřebiteli × reklama. Urči orgán (ÚOHS, Komise, soud, ČOI, RRTV, živnostenský úřad) a všechny souběžné cesty.
2. **Nekalá soutěž - nároky.** Generální klauzule + zvláštní podstata (klamavá reklama § 2977, klamavé označení § 2978, srovnávací reklama § 2980 - kumulativní podmínky, nebezpečí záměny § 2981, parazitování § 2982, podplácení § 2983, zlehčování § 2984, obchodní tajemství § 2985, dotěrné obtěžování § 2986). Nároky § 2988: zdržení, odstranění, přiměřené zadostiučinění, náhrada škody, bezdůvodné obohacení; aktivní legitimace soutěžitele, zákazníka i spolku; **obrácené důkazní břemeno** u některých podstat vůči spotřebiteli (§ 2989 odst. 2). Předběžné opatření (jistota § 75b o. s. ř.), zajištění důkazů, **krajský soud** (§ 9 odst. 2 o. s. ř.), promlčení majetkových nároků (§ 629). Důkazy zajistit hned (notářský zápis, screenshoty, svědci).
3. **Zakázané dohody.** Horizontální tvrdá omezení (ceny, rozdělení trhu, omezení výroby, bid rigging, výměna citlivých informací - i přes asociaci nebo „hub and spoke") × vertikální (RPM per se; ostatní - bloková výjimka 2022/720 s podíly do 30 %, ověř; internetový prodej, dual pricing, MFN); de minimis (§ 3 odst. 1 ZOHS, sdělení Komise - podíly ověř); výjimka § 3 odst. 4 / čl. 101 odst. 3 (efektivnost, přenos na spotřebitele, nezbytnost, nevyloučení soutěže). Následek: absolutní neplatnost dohody (§ 3 odst. 1, § 588 OZ), pokuta, náhrada škody.
4. **Dominance.** Relevantní trh (produktový, geografický - SSNIP), podíl a domněnka (§ 10 odst. 3 - ověř práh), zneužití (§ 11 - nepřiměřené ceny a podmínky, vázání, odmítnutí dodávek, predátorské ceny, věrnostní rabaty, marže squeeze), objektivní ospravedlnění a efektivnost; DMA pro strážce přístupu.
5. **Spojení soutěžitelů.** Notifikace ÚOHS před uskutečněním při dosažení obratových prahů (§ 13 - ověř částky) nebo Komisi (nařízení 139/2004); zákaz uskutečnění před povolením (gun jumping); zjednodušené × plné řízení, lhůty (ověř), závazky, výjimka ze zákazu; call-in u pod-prahových spojení (ověř aktuální úpravu).
6. **Řízení před ÚOHS a obrana.** Předběžné šetření, zahájení řízení, **místní šetření (§ 21f-§ 21g)** - rozsah pověření, právo na přítomnost advokáta bez přerušení šetření, ochrana komunikace s externím advokátem (LPP), kopie zajištěných dokumentů, sektorové šetření; leniency (§ 22ba - úplná imunita jen pro prvního, úplná spolupráce), narovnání (snížení pokuty, ověř %), závazky (§ 7 odst. 2, § 11 odst. 3), pokuta až 10 % čistého obratu (§ 22a - ověř), zákaz plnění veřejných zakázek, odpovědnost FO; rozklad 15 dnů, žaloba ke KS Brno, kasační stížnost.
7. **Náhrada škody (private enforcement).** Zákon 262/2017 Sb.: domněnka škody u kartelu, přenesení navýšení ceny (passing-on), solidární odpovědnost, zpřístupnění důkazů soudem, závaznost rozhodnutí ÚOHS/Komise, **promlčení 5 let** (ověř počátek a stavění po dobu řízení), příslušnost, hromadné žaloby (zákon o hromadném občanském řízení soudním 179/2024 Sb. - ověř).
8. **Reklama a spotřebitel.** Nekalé obchodní praktiky (klamavé × agresivní × černá listina), dozor ČOI a další orgány (RRTV vysílání, KHS, SÚKL u léčiv), srovnávací reklama (§ 2980 OZ + § 2 zák. 40/1995 Sb.), influencer marketing (označení reklamy), greenwashing (směrnice 2024/825 - ověř transpozici), regulované produkty (alkohol, tabák, léčiva, hazard), sankce; souběh s nekalou soutěží.
9. **Compliance.** Soutěžní compliance program (školení, pravidla pro asociace a výměnu informací, kontrola distribučních smluv na RPM, protokol pro dawn raid), M&A due diligence, konkurenční doložky (§ 2975 OZ - přiměřenost, § 310 ZP u zaměstnanců).

## Časté pasti

- Žaloba z nekalé soutěže podaná k okresnímu soudu - věcně příslušný je krajský soud.
- Záměna větví: stížnost k ÚOHS na klamavou reklamu konkurenta (patří k soudu / ČOI), nebo žaloba o zdržení proti kartelu bez ÚOHS.
- „Doporučená cena" s hrozbou sankce za podkročení = RPM (tvrdé omezení), i v e-mailu, i vůči e-shopům.
- Výměna cenových nebo obchodních informací na jednání asociace nebo přes společného dodavatele - kartel bez „dohody".
- Uskutečnění fúze (výkon hlasovacích práv, integrace) před povolením ÚOHS - gun jumping.
- Při místním šetření zdržování, mazání dat nebo odmítnutí přístupu - samostatná pokuta; naopak vydání komunikace s externím advokátem bez námitky LPP.
- Leniency žádost podaná jako druhá v pořadí - jen snížení, ne imunita.
- Srovnávací reklama posuzovaná jen podle pravdivosti - podmínky § 2980 jsou kumulativní (objektivnost, srovnatelné výrobky, nezlehčování, nezneužití pověsti).
- Nárok na náhradu škody z kartelu promlčený, protože se počítalo od rozhodnutí ÚOHS místo od vědomosti (a naopak) - ověř § 9 zák. 262/2017 Sb.
- Konkurenční doložka mezi podnikateli bez územního, časového nebo věcného omezení - neplatná (§ 2975).
- Rozhodnutí SDEU nebo pokyny citované k předchozí blokové výjimce (330/2010) po jejím nahrazení (2022/720).
- Doplňování podílů na trhu, obratů a čísel jednacích z paměti - vždy z dat klienta, rejstříků nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší krok** (která větev, jaký nárok/podání, kam, do kdy; důkazy zajistit hned).
2. **Kvalifikace jednání** (dohoda / dominance / spojení / nekalá soutěž / praktika) a orgán.
3. **Právní rámec** - ZOHS / OZ / unijní předpisy a blokové výjimky v aktuálním znění, s odkazy.
4. **Nároky nebo postup** - tabulka: nárok/krok | právní základ | orgán | lhůta | riziko.
5. **Rizika** (pokuta, neplatnost smlouvy, náhrada škody, trestní rovina, reputační) a **obrana** (výjimka, efektivnost, de minimis, leniency, narovnání).
6. **Judikatura a rozhodovací praxe** - jen ověřená v CODEXIS / uohs.gov.cz / eur-lex, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 23 Cdo 1234/2024 - …`, `NSS - 5 As 123/2025 - …`, `SDEU - C-211/22 - 29.06.2023`) z metadat, nikdy vymyšlené; rozhodnutí ÚOHS s číslem jednacím z uohs.gov.cz.
- Zachovej kvalifikátory („způsobilé přivodit újmu“, „v rozporu s dobrými mravy soutěže“, „citelné narušení“, „před uskutečněním spojení“).
- Jeden časový řez; u dohod znění a bloková výjimka účinné v době uzavření a trvání dohody.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Prahy, podíly, pokuty a lhůty nikdy z paměti - vždy z aktuálního znění a platné blokové výjimky s odkazem.
- Mimo CODEXIS jen oficiální zdroje (uohs.gov.cz, eur-lex, competition-policy.ec.europa.eu, coi.cz, rrtv.gov.cz) když CODEXIS neodpovídá.
