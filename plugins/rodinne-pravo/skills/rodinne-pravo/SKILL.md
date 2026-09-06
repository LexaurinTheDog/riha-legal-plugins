---
uuid: ed3d46b9-393e-4191-8f9f-9102f46a7b61
name: rodinne-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Rodinné právo ČR"
    summary: "Rozvod, péče o děti a styk, výživné, vypořádání SJM, rodičovství, domácí násilí, přeshraniční věci - hmotné právo OZ i řízení podle ZŘS."
    examplePrompts:
      - "Klientka chce nesporný rozvod se dvěma nezletilými dětmi. Jaké dokumenty a v jakém pořadí připravit?"
      - "Otec neplatí výživné 8 měsíců a odstěhoval se do Rakouska. Jak postupovat?"
      - "Manžel převedl před rozvodem firmu na bratra. Lze to zohlednit při vypořádání SJM?"
  en:
    displayName: "Czech Family Law"
    summary: "Divorce, custody and contact, maintenance, matrimonial property settlement, parentage, domestic violence, cross-border cases - substantive Civil Code rules and ZŘS proceedings."
    examplePrompts:
      - "My client wants an uncontested divorce with two minor children. Which documents to prepare and in what order?"
      - "The father has not paid maintenance for 8 months and moved to Austria. How to proceed?"
      - "The husband transferred his company to his brother before the divorce. Can this be reflected in the property settlement?"
  sk:
    displayName: "Rodinné právo ČR"
    summary: "Rozvod, starostlivosť o deti a styk, výživné, vyporiadanie SJM, rodičovstvo, domáce násilie, cezhraničné veci v ČR - hmotné právo OZ aj konanie podľa ZŘS."
    examplePrompts:
      - "Klientka chce nesporný rozvod s dvoma maloletými deťmi. Aké dokumenty a v akom poradí pripraviť?"
      - "Otec neplatí výživné 8 mesiacov a odsťahoval sa do Rakúska. Ako postupovať?"
      - "Manžel previedol pred rozvodom firmu na brata. Dá sa to zohľadniť pri vyporiadaní SJM?"
description: Use when the user's matter involves Czech family law - rozvod (sporný, nesporný), manželství, registrované partnerství, nesezdané soužití, péče o nezletilé dítě, výlučná / střídavá / společná péče, styk s dítětem, rodičovská odpovědnost, výživné (na dítě, mezi manžely, rozvedeného manžela, neprovdané matky), neplacení výživného, společné jmění manželů (SJM), vypořádání SJM, smluvený režim, určení a popření otcovství, osvojení, poručenství, opatrovnictví, pěstounská péče, domácí násilí, vykázání, předběžné opatření, OSPOD, kolizní opatrovník, Cochemská praxe, mediace, mezinárodní únos dítěte, Brusel II ter, Haagská úmluva, řízení podle zákona o zvláštních řízeních soudních (292/2013 Sb.), občanský zákoník část druhá (§ 655-§ 975). Standalone skill - bundles CODEXIS methodology with family-law method; no need to load the general codexis skill.
---

# Rodinné právo ČR

Samostatný oborový skill pro rodinné věci. Rozhoduje **zájem dítěte a pořadí kroků**: u rozvodu s nezletilými se nejdřív upraví poměry dětí, teprve pak lze rozvést; dohody o dětech bez schválení soudem nejsou vykonatelné.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf907'`, `cdx-cli get cdx://cz_law/292/2013/versions`, `cdx-cli search JD --query "střídavá péče zájem dítěte" --court "Ústavní soud" --limit 5`.
- **Novela OZ účinná od 1. 1. 2026 přepsala rodičovskou odpovědnost a styk (§ 858, § 887-§ 891 - styk = osobní, nepřímý i informace).** Starší vzory a judikatura citují neplatné paragrafy. Každý § a lhůtu ověř přes `/versions` k datu, nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - část druhá | 89/2012 Sb. | `cz_law/89/2012` | Manželství (§ 655+), SJM (§ 708-§ 753), rozvod (§ 755-§ 758), výživné manželů (§ 697, § 760-§ 763), rodičovství (§ 775-§ 793), osvojení (§ 794+), rodičovská odpovědnost a styk (§ 858+, § 887-§ 891), péče (§ 906-§ 908), výživné dítěte (§ 910-§ 923), poručenství, opatrovnictví, pěstounství (§ 928+) |
| ZŘS - zákon o zvláštních řízeních soudních | 292/2013 Sb. | `cz_law/292/2013` | Rozvod (§ 383+), péče o nezletilé (§ 466+), předběžná opatření (§ 452+), domácí násilí (§ 400+), opatrovník, rychlost řízení, mediace (§ 474) |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Sporné řízení (vypořádání SJM, výživné zletilých), výkon rozhodnutí o výživném a styku |
| Zákon o sociálně-právní ochraně dětí | 359/1999 Sb. | `cz_law/359/1999` | OSPOD - kolizní opatrovník, šetření, případové konference |
| Zákon o mediaci | 202/2012 Sb. | `cz_law/202/2012` | Nařízené první setkání s mediátorem |
| Zákon o policii | 273/2008 Sb. | `cz_law/273/2008` | Vykázání ze společného obydlí (§ 44+) |
| ZMPS | 91/2012 Sb. | `cz_law/91/2012` | Mezinárodní prvek mimo EU |
| Nařízení Brusel II ter | (EU) 2019/1111 | zdroj `EU` | Příslušnost a uznávání ve věcech manželských a rodičovské odpovědnosti, únosy |
| Haagská úmluva o únosech | 1980 (sdělení 34/1998 Sb.) | zdroj `CR` | Návrat dítěte, ne rozhodování o péči |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Zanedbání povinné výživy (§ 196), týrání osoby žijící ve společném obydlí (§ 199) |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu** (pozor na 1. 1. 2026) → `/toc` → `/text?part=`.
2. Judikatura: **ÚS** (zájem dítěte, střídavá péče, styk, právo na spravedlivý proces v opatrovnických věcech) má v rodinných věcech mimořádnou váhu; **NS** senát 24 Cdo / 30 Cdo (SJM, výživné, rodičovství). Filtr `--court "Ústavní soud"` / `"Nejvyšší soud"`. Ověř datum a zda rozhodnutí neřeší již přepsané ustanovení.
3. Komentář (`COMMENT`) k pojmům (zájem dítěte, změna poměrů, potencialita příjmů); orientační tabulka výživného Ministerstva spravedlnosti je doporučující, ne závazná - uvádět jen jako orientaci.

## Workflow rodinného praktika

1. **Oblast a naléhavost.** Rozvod × děti × majetek × násilí × rodičovství × mezinárodní prvek - často současně. Nejprve ohrožení (násilí, únos, zadržení dítěte) → předběžné opatření (§ 452 ZŘS - soud rozhodne do 24 hodin; § 400+ ZŘS - ochrana proti domácímu násilí do 48 hodin; policejní vykázání § 44 zákona 273/2008 Sb.).
2. **Děti první.** U nezletilých dětí nelze rozvést, dokud není rozhodnuto o péči a výživném (§ 755 odst. 3 OZ). Formy péče (§ 907): výlučná, střídavá, společná - kritéria zájmu dítěte (§ 906, § 907 odst. 2 - vazby, stabilita, názor dítěte § 867, výchovné schopnosti); střídavá péče není podmíněna souhlasem druhého rodiče. Styk (§ 887-§ 891 v novém znění) - osobní, nepřímý, informace; výkon rozhodnutí o styku (§ 500+ ZŘS). Dohoda rodičů vyžaduje schválení soudem (§ 906 odst. 2).
3. **Výživné.** Nezletilé dítě: odůvodněné potřeby × schopnosti, možnosti a majetkové poměry rodiče vč. potenciálního příjmu (§ 913), stejná životní úroveň (§ 915), tvorba úspor (§ 917), zpětně nejdéle 3 roky (§ 922 - ověř), změna poměrů (§ 923). Zletilé dítě - sporné řízení, návrh dítěte. Manžel (§ 697), rozvedený manžel (§ 760-§ 763 - sankční výživné do 3 let), neprovdaná matka (§ 920). Neplacení: výkon rozhodnutí/exekuce, § 196 TZ (trestní oznámení jako páka), náhradní výživné (zákon 588/2020 Sb.).
4. **Rozvod.** Nesporný (§ 757 - manželství alespoň 1 rok, alespoň 6 měsíců nežijí, dohody o dětech schválené soudem, dohoda o majetku a bydlení s úředně ověřenými podpisy) × sporný (§ 755-§ 756 - kvalifikovaný rozvrat, tvrdostní klauzule § 755 odst. 2). Řízení § 383+ ZŘS, soudní poplatek ověř.
5. **SJM.** Rozsah (§ 709-§ 710) a výluky; smluvený režim notářským zápisem (§ 716+, Seznam listin o manželském majetkovém režimu); vypořádání: dohoda (§ 738-§ 739, u nemovitostí písemně) × soud (§ 740, zásady § 742 - rovné podíly, vnosy, potřeby dětí) × **domněnka po 3 letech** (§ 741). Zohlednění jednání zkracujícího SJM (§ 742 odst. 1 písm. f), relativní neplatnost § 714, odporovatelnost). Dluhy a ručení § 731-§ 732.
6. **Rodičovství.** Domněnky otcovství (§ 776-§ 778), souhlasné prohlášení (§ 779), určení soudem (§ 783), popření - **šestiměsíční lhůty** (§ 785, § 789-§ 790) a zásah soudu ve výjimečných případech (§ 792); osvojení (§ 794+), poručenství, pěstounství.
7. **Mezinárodní prvek.** Příslušnost podle obvyklého bydliště dítěte (Brusel II ter), únos - řízení o navrácení (Haagská úmluva, § 478+ ZŘS, výlučně Městský soud v Brně), uznání a výkon; přemístění dítěte do ciziny bez souhlasu druhého rodiče = protiprávní.
8. **Řízení a taktika.** Nesporné řízení ZŘS (soud zjišťuje z úřední povinnosti), OSPOD kolizní opatrovník (§ 469 ZŘS), Cochemská praxe / nařízená mediace (§ 474 ZŘS), znalecký posudek, výslech dítěte (§ 867 OZ, § 100 odst. 3 o. s. ř.), odvolání 15 dnů, dovolání ve většině rodinných věcí nepřípustné (§ 30 ZŘS - ověř výjimky), ústavní stížnost.

## Časté pasti

- Citace § 888 / § 891 OZ ve znění před 1. 1. 2026 (staré vzory) - styk je nyní upraven jinak, ověř aktuální znění.
- Návrh na rozvod podaný dřív, než je pravomocně upravena péče o nezletilé.
- Dohoda o výživném nebo styku bez schválení soudem - nevykonatelná.
- Nárok na výživné uplatněný zpětně nad zákonnou hranici nebo bez tvrzení o změně poměrů.
- Zmeškání tříleté domněnky vypořádání SJM (§ 741) - nemovitosti do podílového spoluvlastnictví, movité podle užívání.
- Vypořádání SJM smlouvou bez písemné formy u nemovitostí nebo bez řešení dluhů.
- Popření otcovství po uplynutí šestiměsíční lhůty bez argumentace § 792.
- Předběžné opatření podle o. s. ř. tam, kde platí zvláštní režim § 452 ZŘS (a naopak).
- Řešení „únosu" dítěte v rámci EU žalobou o péči místo návrhu na navrácení.
- Trestní oznámení pro zanedbání výživy bez předchozího výkonu rozhodnutí nebo bez ověření, že povinný objektivně mohl plnit.
- Doplňování dat narození, příjmů a adres z paměti - vždy z listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší krok** (co, kam, do kdy; u ohrožení dítěte předběžné opatření na prvním místě).
2. **Oblast a pořadí řízení** (děti → rozvod → majetek).
3. **Právní rámec** - OZ/ZŘS v aktuálním znění, s odkazy.
4. **Postup a dokumenty** (návrhy, dohody, přílohy, podpisy, poplatky).
5. **Argumentace zájmem dítěte / zásadami vypořádání** s judikaturou ÚS a NS.
6. **Rizika a alternativy** (dohoda × spor, mediace, náklady, délka řízení).
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `ÚS - I. ÚS 123/25 - …`, `NS - 24 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejdéle za dobu tří let“, „alespoň“, „v zájmu dítěte“, „bez zbytečného odkladu“).
- Jeden časový řez; u styku a rodičovské odpovědnosti výslovně uveď, že se použilo znění po 1. 1. 2026.
- Citlivé údaje o dětech a obětech násilí uváděj jen v nezbytném rozsahu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (justice.cz, MSp tabulka výživného jako orientace, ÚMPOD pro mezinárodní věci).
- Částky výživného nikdy neurčuj jako jistotu - jen rozpětí s uvedením kritérií a orientační tabulky.
