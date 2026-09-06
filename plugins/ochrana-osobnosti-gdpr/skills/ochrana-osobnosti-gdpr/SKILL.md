---
uuid: adc40233-d8bf-43c4-a7fb-513592cd9c72
name: ochrana-osobnosti-gdpr
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Ochrana osobnosti a GDPR ČR"
    summary: "Zásahy do cti, soukromí a podoby, pomluva, právo na odpověď, omluva a peněžité zadostiučinění, práva subjektu údajů, GDPR compliance, ÚOOÚ, DSA."
    examplePrompts:
      - "O klientovi vyšel článek s nepravdivým tvrzením o trestním stíhání. Jaké nároky má, v jakém pořadí a s jakými lhůtami?"
      - "Bývalý zaměstnanec zveřejnil na síti fotografie z firemního večírku s urážlivými komentáři. Co lze požadovat po něm a po platformě?"
      - "Firma chce nasadit kamery se záznamem na pracovišti. Jaké má povinnosti podle GDPR a zákoníku práce?"
  en:
    displayName: "Czech Personality Rights and GDPR"
    summary: "Interference with honour, privacy and likeness, defamation, right of reply, apology and monetary satisfaction, data subject rights, GDPR compliance, ÚOOÚ, DSA."
    examplePrompts:
      - "An article falsely claimed my client is criminally prosecuted. Which claims, in what order, with which deadlines?"
      - "A former employee posted photos from a company party with abusive comments. What can be demanded from him and from the platform?"
      - "A company wants recorded CCTV at the workplace. What are its GDPR and Labour Code duties?"
  sk:
    displayName: "Ochrana osobnosti a GDPR ČR"
    summary: "Zásahy do cti, súkromia a podoby, ohováranie, právo na odpoveď, ospravedlnenie a peňažné zadosťučinenie, práva dotknutej osoby, GDPR compliance, ÚOOÚ, DSA v ČR."
    examplePrompts:
      - "O klientovi vyšiel článok s nepravdivým tvrdením o trestnom stíhaní. Aké nároky má, v akom poradí a s akými lehotami?"
      - "Bývalý zamestnanec zverejnil na sieti fotografie z firemného večierka s urážlivými komentármi. Čo možno žiadať od neho a od platformy?"
      - "Firma chce nasadiť kamery so záznamom na pracovisku. Aké má povinnosti podľa GDPR a zákonníka práce?"
description: Use when the user's matter involves Czech personality rights, reputation, privacy, media or personal data - ochrana osobnosti (§ 81-§ 117 OZ), čest, důstojnost, dobrá pověst, soukromí, podoba, jméno, pomluva, nepravdivé tvrzení, hodnotící soud, kritika, zveřejnění fotografie, zpravodajská licence, právo na odpověď, dodatečné sdělení, tiskový zákon, omluva, zdržení se, odstranění, výmaz článku, peněžité zadostiučinění, nemajetková újma (§ 2951, § 2956), pověst právnické osoby (§ 135), předběžné opatření, GDPR (nařízení 2016/679), zákon 110/2019 Sb., osobní údaje, správce, zpracovatel, souhlas, oprávněný zájem, právo na přístup, výmaz, námitku, právo být zapomenut, kamerový systém, monitoring zaměstnanců, cookies, obchodní sdělení, únik dat, incident, DPIA, pověřenec, ÚOOÚ, stížnost, pokuta, DSA, odstranění obsahu z platformy, pomluva § 184 TZ. Standalone skill - bundles CODEXIS methodology with personality-and-privacy method; no need to load the general codexis skill.
---

# Ochrana osobnosti a GDPR ČR

Samostatný oborový skill pro zásahy do osobnosti, mediální právo a ochranu osobních údajů. Dvě otázky před vším ostatním: **je to skutkové tvrzení, nebo hodnotící soud** - a **která krátká lhůta už běží** (tiskový zákon, předběžné opatření, promlčení zadostiučinění, 72 hodin u incidentu).

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf82'`, `cdx-cli get cdx://cz_law/46/2000/versions`, `cdx-cli search JD --query "hodnotící soud skutkové tvrzení ochrana osobnosti" --court "Ústavní soud" --limit 5`, `cdx-cli search EU --query "GDPR článek 17 výmaz" --limit 5`.
- Lhůty, sazby pokut, výši jistoty a čísla článků **vždy ověř v aktuálním znění**; nikdy z paměti. GDPR čti v české verzi ze zdroje `EU`, vnitrostátní odchylky v zákoně 110/2019 Sb.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - osobnost | 89/2012 Sb. | `cz_law/89/2012` | Osobnostní práva (§ 81-§ 83), podoba a soukromí (§ 84-§ 90, zákonné licence § 88-§ 90), jméno (§ 77-§ 80), pověst PO (§ 135), zadostiučinění (§ 2951 odst. 2, § 2956-§ 2957), promlčení (§ 612) |
| Tiskový zákon | 46/2000 Sb. | `cz_law/46/2000` | Právo na odpověď (§ 10), dodatečné sdělení (§ 11), lhůty (§ 12-§ 14) |
| Zákon o vysílání | 231/2001 Sb. | `cz_law/231/2001` | Odpověď a dodatečné sdělení v rozhlase a TV (§ 35+) |
| GDPR | (EU) 2016/679 | zdroj `EU` | Zásady (čl. 5), tituly (čl. 6, čl. 9), práva subjektu (čl. 12-22), správce/zpracovatel (čl. 24-28), incidenty (čl. 33-34), DPIA (čl. 35), pověřenec (čl. 37), stížnost a žaloba (čl. 77-82), pokuty (čl. 83) |
| Zákon o zpracování osobních údajů | 110/2019 Sb. | `cz_law/110/2019` | Odchylky (novinářská a akademická výjimka, věk dítěte), přestupky a limity pokut pro veřejné subjekty |
| Zákon o službách informační společnosti | 480/2004 Sb. | `cz_law/480/2004` | Obchodní sdělení (§ 7), odpovědnost poskytovatelů |
| Nařízení o digitálních službách (DSA) | (EU) 2022/2065 | zdroj `EU` | Oznámení protiprávního obsahu (čl. 16), interní stížnosti, důvěryhodní oznamovatelé |
| Zákon o elektronických komunikacích | 127/2005 Sb. | `cz_law/127/2005` | Cookies a sledovací technologie (§ 89 - souhlas) |
| Zákoník práce | 262/2006 Sb. | `cz_law/262/2006` | Monitoring zaměstnanců (§ 316) |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Pomluva (§ 184), neoprávněné nakládání s osobními údaji (§ 180), nebezpečné pronásledování (§ 354) |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Příslušnost (§ 9), předběžné opatření a jistota (§ 74-§ 77a), předžalobní výzva (§ 142a) |
| Listina / Úmluva | 2/1993 Sb. / 209/1992 Sb. | `cz_law/2/1993`, `cz_law/209/1992` | Čl. 10 × čl. 17 Listiny, čl. 8 × čl. 10 Úmluvy - test proporcionality |

## Rešeršní strategie

1. Paragraf/článek známý → `/versions` → `/toc` → `/text?part=`; GDPR a DSA ze zdroje `EU`.
2. Judikatura: **ÚS** (svoboda projevu × ochrana osobnosti, veřejně činné osoby, kritéria proporcionality), **NS** senáty 30 Cdo / 25 Cdo (ochrana osobnosti, výše zadostiučinění), **NSS** (ÚOOÚ, pokuty, kamerové systémy), **SDEU** a **ESLP** (`ES` - právo být zapomenut, Google, von Hannover, Axel Springer). Vždy ověř datum a zda rozhodnutí nebylo překonáno.
3. Komentář (`COMMENT`) k rozlišení skutkového tvrzení a hodnotícího soudu, k zákonným licencím a k výši zadostiučinění; stanoviska ÚOOÚ a EDPB jako administrativní výklad, ne zákon.

## Workflow

1. **Kvalifikace zásahu.** Skutkové tvrzení (lze dokázat pravdivost - důkazní břemeno nese zpravidla ten, kdo tvrdil) × hodnotící soud (přiměřenost, skutkový základ, forma) × zveřejnění podoby/záznamu (souhlas § 85, licence § 88-§ 90 - zpravodajská licence má meze § 90) × soukromí × jméno × osobní údaje (GDPR) × pověst PO (§ 135 - jen název a pověst). Uchovej důkazy hned: notářský zápis o obsahu webu, screenshoty s URL a časem, archivace, svědci.
2. **Osoba a kontext.** Veřejně činná osoba / politik / podnikatel / soukromá osoba; veřejný zájem, forma sdělení, médium, dosah, úmysl, opakování, předchozí chování dotčeného. Test proporcionality podle ÚS a ESLP - argumentuj po kritériích, ne obecně.
3. **Nároky a jejich pořadí.** Zdržení se (§ 82), odstranění následků (výmaz, stažení, oprava), morální zadostiučinění - omluva (§ 2951 odst. 2; petit musí obsahovat přesné znění, formu a místo uveřejnění), peněžité zadostiučinění (§ 2956-§ 2957 - výše podle závažnosti, okolností zvláštního zřetele; bez tabulek, s judikaturou), náhrada škody, právo na odpověď / dodatečné sdělení u periodického tisku a vysílání (**žádost do 30 dnů od uveřejnění**, žaloba v krátké lhůtě po odmítnutí - ověř § 12-§ 14 tiskového zákona), práva podle GDPR (přístup čl. 15, výmaz čl. 17 vč. vyhledávačů, námitka čl. 21 - správce reaguje do 1 měsíce čl. 12), oznámení platformě podle DSA čl. 16, stížnost ÚOOÚ (čl. 77), trestní oznámení (§ 184 TZ - subsidiárně).
4. **Procesní cesta.** Předžalobní výzva (§ 142a o. s. ř.), věcná příslušnost - ochrana osobnosti fyzické osoby u **okresního soudu** (§ 9 odst. 1), spory o pověst a název právnické osoby a nekalá soutěž u krajského soudu (§ 9 odst. 2 - ověř), místní příslušnost (§ 87 - i místo zásahu), soudní poplatek (ověř sazebník), předběžné opatření (§ 74-§ 77a - jistota podle § 75b, ověř výši), promlčení: právo na ochranu se nepromlčuje, právo na zadostiučinění a náhradu ano (§ 612 - obecná lhůta), dovolání ve věcech ochrany osobnosti (ověř omezení § 238 o. s. ř.).
5. **GDPR pro správce (compliance).** Titul zpracování (čl. 6 - souhlas × smlouva × oprávněný zájem s balančním testem), informační povinnost (čl. 13-14), záznamy o činnostech (čl. 30), zpracovatelské smlouvy (čl. 28), DPIA (čl. 35 - kamery, monitoring, profilování), pověřenec (čl. 37), incident - oznámení ÚOOÚ do **72 hodin** (čl. 33) a subjektům (čl. 34), doba uchování, předávání mimo EU (kap. V), cookies (§ 89 zák. 127/2005 - souhlas), marketing (§ 7 zák. 480/2004), kamery a monitoring zaměstnanců (§ 316 ZP - závažný důvod, informace), zvláštní kategorie (čl. 9).
6. **Řízení před ÚOOÚ.** Kontrola (kontrolní řád), přestupkové řízení (zákon 250/2016 Sb., pokuty čl. 83 GDPR / § 62 zák. 110/2019 Sb. - limity pro veřejné subjekty), rozklad, správní žaloba; polehčující okolnosti (spolupráce, náprava, DPIA).

## Časté pasti

- Žaloba na omluvu bez přesného znění a formy omluvy v petitu - nevykonatelný výrok.
- Záměna hodnotícího soudu za skutkové tvrzení (a naopak) - u hodnotícího soudu se pravdivost nedokazuje, zkoumá se přiměřenost.
- Zmeškání lhůt tiskového zákona - právo na odpověď zaniká, zbývá jen obecná ochrana osobnosti.
- Žaloba fyzické osoby podaná ke krajskému soudu podle úpravy před rokem 2014.
- Peněžité zadostiučinění „podle tabulek" - neexistují; argumentovat kritérii § 2957 a srovnatelnou judikaturou.
- Nepodaný návrh na výmaz u vyhledávače (právo být zapomenut) vedle nároku proti autorovi.
- Oprávněný zájem uvedený bez balančního testu; souhlas vynucený jako podmínka služby.
- Incident ohlášený ÚOOÚ po 72 hodinách bez odůvodnění zpoždění.
- Kamerový systém se záznamem bez DPIA a informační tabule; monitoring zaměstnanců bez závažného důvodu (§ 316 ZP).
- Cookies lišta bez skutečné volby (opt-in) nebo s předzaškrtnutým souhlasem.
- Nárok PO na peněžité zadostiučinění za nemajetkovou újmu brán jako samozřejmý - sporný, ověř aktuální judikaturu.
- Doplňování citací článků, jmen a dat zveřejnění z paměti - vždy z důkazů nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co uplatnit, proti komu, do kdy; důkazy zajistit hned).
2. **Kvalifikace zásahu a test proporcionality** po kritériích.
3. **Nároky** - tabulka: nárok | právní základ | adresát | lhůta | šance.
4. **Procesní postup** (výzva, příslušnost, poplatek, předběžné opatření, ÚOOÚ/DSA paralelně).
5. **Rizika** (protinároky, náklady, svoboda projevu, veřejný zájem).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. SDEU/ESLP.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `ÚS - I. ÚS 453/03 - …`, `NS - 30 Cdo 1234/2024 - …`, `SDEU - C-131/12 - 13.05.2014`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do 30 dnů ode dne uveřejnění“, „bez zbytečného odkladu, nejpozději do 72 hodin“, „okolnosti zvláštního zřetele hodné“).
- Jeden časový řez; u zásahu znění účinné v den zásahu.
- Osobní údaje třetích osob v odpovědi jen v nezbytném rozsahu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (uoou.gov.cz, EDPB, justice.cz, curia.europa.eu, hudoc) když CODEXIS neodpovídá.
- Lhůty, jistoty, sazby pokut a částky zadostiučinění nikdy z paměti - vždy z aktuálního znění a ověřené judikatury.
