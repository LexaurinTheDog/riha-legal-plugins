---
uuid: a0694e49-04e3-430c-89d7-4202875d068f
name: obce-a-verejna-sprava
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Obce a veřejná správa ČR"
    summary: "Působnost orgánů obce, nakládání s obecním majetkem a záměr, vyhlášky a jejich přezkum, svobodný přístup k informacím, dotace a obecní společnosti, referendum, dozor a přezkoumání hospodaření, odpovědnost zastupitelů."
    examplePrompts:
      - "Obec prodala pozemek bez zveřejnění záměru a za cenu pod znaleckým posudkem. Je smlouva platná a kdo za to odpovídá?"
      - "Občan žádá podle infozákona o smlouvy a platy vedoucích úředníků. Co musíme vydat, co odmítnout a v jakých lhůtách?"
      - "Zastupitelstvo chce vyhláškou zakázat konzumaci alkoholu na celém území obce. Obstojí to před ministerstvem a Ústavním soudem?"
  en:
    displayName: "Czech Municipal Law"
    summary: "Competences of municipal bodies, disposal of municipal property and publication of intent, by-laws and their review, freedom of information, municipal grants and companies, referendum, supervision and audit, liability of councillors."
    examplePrompts:
      - "A municipality sold a plot without publishing its intent and below the appraised price. Is the contract valid and who is liable?"
      - "A citizen requests contracts and salaries of senior officials under the freedom-of-information act. What must we disclose, what may we refuse, and by when?"
      - "The council wants a by-law banning alcohol consumption across the whole municipality. Will it survive ministry review and the Constitutional Court?"
  sk:
    displayName: "Obce a verejná správa ČR"
    summary: "Pôsobnosť orgánov obce v ČR, nakladanie s obecným majetkom a zámer, vyhlášky a ich preskúmanie, slobodný prístup k informáciám, dotácie a obecné spoločnosti, referendum, dozor a preskúmanie hospodárenia, zodpovednosť poslancov."
    examplePrompts:
      - "Obec predala pozemok bez zverejnenia zámeru a za cenu pod znaleckým posudkom. Je zmluva platná a kto za to zodpovedá?"
      - "Občan žiada podľa infozákona o zmluvy a platy vedúcich úradníkov. Čo musíme vydať, čo odmietnuť a v akých lehotách?"
      - "Zastupiteľstvo chce vyhláškou zakázať konzumáciu alkoholu na celom území obce. Obstojí to pred ministerstvom a Ústavným súdom?"
description: Use when the user's matter involves a Czech municipality, region or public body as actor or counterparty - obec, kraj, zákon o obcích (128/2000 Sb.), zastupitelstvo, rada obce, starosta, samostatná a přenesená působnost, vyhrazená pravomoc zastupitelstva, záměr obce, zveřejnění záměru, prodej a pronájem obecního majetku, cena obvyklá, neplatnost smlouvy obce, obecně závazná vyhláška, nařízení obce, dozor ministerstva vnitra, zrušení vyhlášky Ústavním soudem, svobodný přístup k informacím (106/1999 Sb.), infožádost, platy úředníků, dotace obce, veřejnoprávní smlouva o dotaci, příspěvková organizace, obecní společnost, in-house, místní referendum (22/2004 Sb.), místní poplatky, přezkoumání hospodaření, rozpočet obce, střet zájmů (159/2006 Sb.), odpovědnost zastupitelů, petice, shromáždění, náhrada škody za nesprávný úřední postup (82/1998 Sb.). Standalone skill - bundles CODEXIS methodology with municipal-practice method; no need to load the general codexis skill.
---

# Obce a veřejná správa ČR

Samostatný oborový skill pro právo územní samosprávy a jednání s veřejnými subjekty. Dvě otázky před vším ostatním: **v jaké působnosti obec jedná** (samostatná × přenesená - jiný orgán, jiný dozor, jiná odpovědnost) a **zda byl dodržen zákonný postup před právním jednáním** (záměr, příslušný orgán, cena obvyklá, registr smluv) - jeho porušení znamená absolutní neplatnost, nikoli jen vadu.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/128/2000/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf39'`, `cdx-cli get cdx://cz_law/106/1999/versions`, `cdx-cli get cdx://cz_law/250/2000/versions`, `cdx-cli search JD --query "záměr obce zveřejnění neplatnost smlouvy 39" --court "Nejvyšší soud" --limit 5`, `cdx-cli search JD --query "obecně závazná vyhláška test čtyř kroků" --court "Ústavní soud" --limit 5`.
- Zákon o obcích, rozpočtová pravidla územních rozpočtů i infozákon jsou průběžně novelizovány (limity pro dotace, lhůty, digitalizace úřední desky). **Lhůty, limity, kvóra a čísla odstavců ověř v aktuálním znění k datu úkonu**; nikdy z paměti. U hlavního města Prahy a statutárních měst zkontroluj zvláštní zákon a statut.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o obcích | 128/2000 Sb. | `cz_law/128/2000` | Působnost (§ 7, § 35, § 61+), občan obce (§ 16), vyhlášky a nařízení (§ 10-§ 12), majetek a záměr (§ 38-§ 41), zastupitelstvo (§ 67-§ 98, vyhrazená pravomoc § 84-§ 85), rada (§ 99-§ 102), starosta (§ 103+), úřad a tajemník (§ 109+), dozor a kontrola (§ 123-§ 129) |
| Zákon o krajích / o hlavním městě Praze | 129/2000 / 131/2000 Sb. | `cz_law/129/2000`, `cz_law/131/2000` | Obdobná úprava pro kraje a Prahu (statut, městské části) |
| Rozpočtová pravidla územních rozpočtů | 250/2000 Sb. | `cz_law/250/2000` | Rozpočet a jeho zveřejnění (§ 11+), dotace a návratné výpomoci (§ 10a-§ 10d), porušení rozpočtové kázně (§ 22), příspěvkové organizace (§ 27-§ 37) |
| Zákon o přezkoumávání hospodaření | 420/2004 Sb. | `cz_law/420/2004` | Přezkoumání auditorem nebo krajským úřadem, nápravná opatření |
| Zákon o svobodném přístupu k informacím | 106/1999 Sb. | `cz_law/106/1999` | Povinné subjekty, lhůty (§ 14), úhrada (§ 17), omezení (§ 7-§ 11), rozhodnutí o odmítnutí (§ 15), odvolání a stížnost (§ 16-§ 16a), zveřejňování (§ 5) |
| Zákon o střetu zájmů | 159/2006 Sb. | `cz_law/159/2006` | Veřejní funkcionáři, oznámení, registr, zákazy, přestupky |
| Zákon o místním referendu | 22/2004 Sb. | `cz_law/22/2004` | Návrh přípravného výboru, přípustnost, vyhlášení, platnost a závaznost, soudní ochrana |
| Zákon o místních poplatcích / daňový řád | 565/1990 / 280/2009 Sb. | `cz_law/565/1990`, `cz_law/280/2009` | Poplatky obce, jejich správa a opravné prostředky |
| Správní řád | 500/2004 Sb. | `cz_law/500/2004` | Přenesená působnost, úřední deska (§ 26), opatření obecné povahy (§ 171+), veřejnoprávní smlouvy (§ 159+) |
| Zákon o úřednících ÚSC / služební zákon | 312/2002 / 234/2014 Sb. | `cz_law/312/2002`, `cz_law/234/2014` | Postavení úředníků obcí a krajů × státní správa |
| Zákon o obecní policii | 553/1991 Sb. | `cz_law/553/1991` | Oprávnění strážníků, dohled |
| Zákon o odpovědnosti za škodu při výkonu veřejné moci | 82/1998 Sb. | `cz_law/82/1998` | Odpovědnost obce v samostatné působnosti (§ 19+) × státu v přenesené |
| Zákon o registru smluv / ZZVZ | 340/2015 / 134/2016 Sb. | `cz_law/340/2015`, `cz_law/134/2016` | Uveřejňování smluv, zadávání zakázek obcí (viz skill veřejných zakázek) |
| Zákon o právu petičním / shromažďovacím | 85/1990 / 84/1990 Sb. | `cz_law/85/1990`, `cz_law/84/1990` | Petice a odpověď, oznámení shromáždění, zákaz a soudní přezkum |
| Ústava a Listina | 1/1993 / 2/1993 Sb. | `cz_law/1/1993`, `cz_law/2/1993` | Právo na samosprávu (čl. 99-§ 105 Ústavy), zásah státu jen zákonem, ústavní stížnost obce |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu úkonu** → `/toc` → `/text?part=`; u vyhlášek i zvláštní zmocňovací zákon.
2. Judikatura: **NS** senáty 26 Cdo / 30 Cdo / 33 Cdo (neplatnost smluv obcí - záměr, orgán, cena; nájmy obecních bytů), 5 Tdo (trestní odpovědnost zastupitelů), **ÚS** (vyhlášky - test čtyř kroků; samospráva; platy úředníků), **NSS** (infozákon, referendum, dozor, opatření obecné povahy, místní poplatky). Ověř datum a novely.
3. Komentář (`COMMENT`) k pojmům (záměr, cena obvyklá, důvod zvláštního zřetele, veřejný funkcionář); metodiky Ministerstva vnitra (odbor veřejné správy, dozoru a kontroly) jsou administrativní výklad s vysokou praktickou váhou.

## Workflow

1. **Role a působnost.** Obec/kraj (starosta, zastupitel, rada, tajemník, úředník, příspěvková organizace, obecní společnost) × občan obce × smluvní partner × kontrolní orgán. **Samostatná působnost** (§ 35 - majetek, rozpočet, vyhlášky, dotace; orgány obce, dozor MV, odpovědnost obce) × **přenesená působnost** (§ 61+ - správní řízení, stavební úřad, matrika, přestupky; správní řád, dozor krajského úřadu, odpovědnost státu podle 82/1998 Sb.).
2. **Právní jednání obce - povinný postup.** (a) **Záměr** prodat, směnit, darovat, pronajmout, propachtovat nebo vypůjčit nemovitost - zveřejnit na úřední desce **nejméně 15 dnů před rozhodnutím** (§ 39 odst. 1 - jinak absolutní neplatnost; obsah záměru - identifikace nemovitosti, ne nutně cena a nabyvatel; výjimky § 39 odst. 3 - ověř); (b) **rozhodnutí příslušného orgánu** - vyhrazená pravomoc zastupitelstva (§ 84-§ 85: nabytí a převod nemovitostí, dotace a dary nad zákonný limit, úvěry, zakládání PO, peněžité vklady - ověř částky) × rada (§ 102 - nájmy, zbytková působnost) × starosta; jednání bez schválení nebo v rozporu s ním je neplatné (§ 41 odst. 2); (c) **cena obvyklá** - odchylka jen zdůvodněná (§ 39 odst. 2 - jinak neplatnost; znalecký posudek, důvody zvláštního zřetele); (d) doložka o splnění podmínek (§ 41 odst. 1); (e) uveřejnění v registru smluv (účinnost); (f) ZZVZ; (g) střet zájmů - oznámení o osobním zájmu (§ 8 zák. 159/2006 Sb.) a zákaz účasti; (h) zápis ze zasedání (§ 95) a možnost občana nahlížet (§ 16 odst. 2).
3. **Zastupitelstvo a rada.** Zasedání zastupitelstva veřejné, program zveřejněn na úřední desce **7 dnů předem** (§ 93), usnášeníschopnost nadpoloviční většina všech členů (§ 87), rozhodování nadpoloviční většinou všech (§ 87 - ověř), právo občana vyjadřovat se (§ 16 odst. 2 písm. c)), zápis do 10 dnů (§ 95), rada neveřejná, jednací řády; odměny zastupitelů (NV o odměnách), neslučitelnost, zánik mandátu (§ 55 zák. 491/2001 Sb.), kompetenční spory rada × zastupitelstvo.
4. **Normotvorba.** Obecně závazné vyhlášky v samostatné působnosti (§ 10 - veřejný pořádek, zábavy, veřejná prostranství, hřbitovy, odpady, místní poplatky a zmocnění zvláštními zákony; **test ÚS: pravomoc, působnost, zneužití, nerozumnost**), nařízení v přenesené působnosti (§ 11 - jen na základě zákona), vyhlášení (Sbírka právních předpisů ÚSC), **dozor MV** (§ 123 - výzva, pozastavení účinnosti, návrh ÚS), tržní řády, územní plán jako opatření obecné povahy (přezkum § 101a s. ř. s.).
5. **Transparentnost a informace.** Úřední deska (elektronická § 26 SŘ), povinně zveřejňované informace (§ 5 zák. 106/1999 Sb.), **infožádost** - vyřízení do 15 dnů (prodloužení o 10 dnů § 14), úhrada nákladů (§ 17 - předem oznámit, jinak nelze), omezení (osobní údaje § 8a, obchodní tajemství § 9, vnitřní pokyny § 11), platy úředníků a odměny (test ÚS/NSS - veřejný zájem × soukromí), odmítnutí jen rozhodnutím (§ 15) s odvoláním 15 dnů (§ 16) a stížností na postup (§ 16a), soudní přezkum; rozpočet, střednědobý výhled a závěrečný účet - zveřejnění návrhu nejméně 15 dnů před projednáním (§ 11 zák. 250/2000 Sb.), zápisy ze zasedání, registr smluv, registr oznámení (střet zájmů).
6. **Dotace, organizace, společnosti.** Dotace z rozpočtu obce (§ 10a-§ 10d zák. 250/2000 Sb. - žádost, **veřejnoprávní smlouva**, program a výzva, zveřejnění smluv nad zákonný limit, porušení rozpočtové kázně a odvod § 22, spory o dotační smlouvu ve správním řízení), veřejná podpora EU (de minimis, GBER, SGEI), příspěvkové organizace (§ 27+ - zřizovací listina, svěřený majetek, kontrola), obecní s.r.o. a a.s. (ZOK; zastupitelstvo schvaluje založení a zástupce; in-house zadávání § 11 ZZVZ - podmínky ověř), dobrovolné svazky obcí (§ 49+), veřejné služby (doprava, odpady, vodovody).
7. **Kontrola, dozor, občan.** Přezkoumání hospodaření (zák. 420/2004 Sb. - auditor / KÚ, zpráva, nápravná opatření do 15 dnů - ověř), finanční kontrola (320/2001 Sb.), dozor MV nad samostatnou působností (§ 123-§ 124) a KÚ nad přenesenou (§ 125-§ 126), NKÚ (rozsah vůči ÚSC - ověř), finanční úřad (odvody za PRK), kontrolní a finanční výbor zastupitelstva (§ 117-§ 119), **místní referendum** (zák. 22/2004 Sb. - přípravný výbor, podpisy podle velikosti obce, nepřípustné otázky § 7, rozhodnutí zastupitelstva, soudní ochrana § 57-§ 58 s. ř. s., závaznost při zákonné účasti - ověř), petice (odpověď do 30 dnů), shromáždění (oznámení, zákaz, soud), stížnosti (§ 175 SŘ), ombudsman.
8. **Odpovědnost.** Zastupitelé - péče řádného hospodáře (§ 38 odst. 1) a slib; **trestní odpovědnost** (§ 220-§ 221 TZ porušení povinnosti při správě cizího majetku, § 329 zneužití pravomoci - judikatura NS: hlasování bez podkladů, prodej pod cenou; obhajoba: znalecký posudek, odborné stanovisko, důvod zvláštního zřetele); starosta při překročení; úředníci (zák. 312/2002 Sb.); obec za škodu v samostatné působnosti (zák. 82/1998 Sb. § 19-§ 24 - nesprávný úřední postup, nezákonné rozhodnutí; předběžné projednání), stát v přenesené; náhrada škody obci po zastupitelích (regres, promlčení).
9. **Občan × obec.** Místní poplatky (daňový řád - odvolání 30 dnů, promlčení), přestupky (obecní policie, komise), obecní byty (nájem - skill bytového práva), školy (spádovost, zřizovatel), sociální služby, odpady a poplatky, stavební úřad (skill stavebního práva), pohřebnictví, ochrana před hlukem, zábory a uzavírky, pokuty za neplnění vyhlášek.

## Časté pasti

- Záměr nezveřejněný, zveřejněný kratší dobu, neurčitý nebo odlišný od uzavřené smlouvy - absolutní neplatnost, kterou soud zkoumá z úřední povinnosti a namítne ji každý.
- Převod nemovitosti nebo dotace nad limit schválené radou místo zastupitelstvem - neplatnost (§ 41 odst. 2).
- Cena pod obvyklou bez zdůvodnění v usnesení - neplatnost a trestní riziko pro hlasující.
- Starosta podepsal smlouvu, kterou orgán neschválil nebo schválil v jiném znění.
- Smlouva neuveřejněná v registru smluv - neúčinná, po lhůtě zrušená.
- Vyhláška mimo zákonné zmocnění nebo duplikující zákon - pozastavení MV a zrušení ÚS.
- Infožádost odložená bez rozhodnutí, úhrada účtovaná bez předchozího oznámení, platy odmítnuté paušálně.
- Referendum k otázce, o níž se referendum konat nemůže (rozpočet, poplatky) - zamítnutí; zastupitelstvo nerozhodlo o vyhlášení ve lhůtě - soud vyhlásí.
- Dotace bez veřejnoprávní smlouvy nebo bez zveřejnění - porušení rozpočtové kázně na straně obce i příjemce.
- Příspěvková organizace nakládá s majetkem nad rámec zřizovací listiny; obecní společnost zadává in-house bez splnění podmínek.
- Střet zájmů zastupitele neoznámen před hlasováním - přestupek a napadnutelnost usnesení.
- Zastupitel hlasuje pro prodej „podle doporučení komise" bez podkladů - judikatura NS odpovědnost nevylučuje.
- Doplňování čísel usnesení, parcel, částek a dat zveřejnění z paměti - vždy z úřední desky, zápisů, katastru nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat / co nepodepsat, který orgán, do kdy).
2. **Působnost a orgán** (samostatná × přenesená; zastupitelstvo × rada × starosta).
3. **Právní rámec** - zákon o obcích / 250/2000 / 106/1999 / zvláštní zákony v aktuálním znění, s odkazy.
4. **Postup krok za krokem** - tabulka: krok | právní základ | orgán | lhůta | zveřejnění.
5. **Rizika** (neplatnost, dozor, PRK, trestní odpovědnost) a **alternativy**.
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. ÚS a NSS.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 26 Cdo 1234/2024 - …`, `ÚS - Pl. ÚS 12/25 - …`, `NSS - 8 As 123/2025 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejméně 15 dnů před rozhodnutím“, „nadpoloviční většinou všech členů“, „cena obvyklá“, „důvod hodný zvláštního zřetele“).
- Jeden časový řez; znění účinné v den rozhodnutí orgánu / úkonu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity, lhůty, kvóra a sazby nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o usneseních, záměrech a smlouvách výhradně z úřední desky, registru smluv, zápisů a katastru; mimo CODEXIS jen oficiální zdroje (mvcr.gov.cz - odbor dozoru, mfcr.cz, nssoud.cz, usoud.cz) když CODEXIS neodpovídá.
