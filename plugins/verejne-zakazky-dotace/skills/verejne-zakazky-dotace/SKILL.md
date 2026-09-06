---
uuid: 1b215851-806f-46bb-8852-55dd0ca229c4
name: verejne-zakazky-dotace
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Veřejné zakázky a dotace ČR"
    summary: "Režimy a druhy zadávacích řízení, námitky a návrh k ÚOHS, změny závazku, dotační podmínky, nesrovnalosti, porušení rozpočtové kázně a odvody, audity veřejného sektoru."
    examplePrompts:
      - "Obec chce rozdělit rekonstrukci školy na tři zakázky malého rozsahu. Je to přípustné a co hrozí?"
      - "Byli jsme vyloučeni ze zadávacího řízení pro nesplnění kvalifikace. Jaké lhůty běží pro námitky a návrh k ÚOHS a kolik je kauce?"
      - "Poskytovatel dotace vyměřil odvod 100 % za chybu ve výběrovém řízení dodavatele. Jak se bránit?"
  en:
    displayName: "Czech Public Procurement and Subsidies"
    summary: "Procurement regimes and procedures, objections and ÚOHS review, contract modifications, subsidy conditions, irregularities, budget discipline breaches and levies, public-sector audits."
    examplePrompts:
      - "A municipality wants to split a school reconstruction into three small-scale contracts. Is it permissible and what are the risks?"
      - "We were excluded from a tender for failing qualification. Which deadlines run for objections and the ÚOHS petition, and how much is the deposit?"
      - "The subsidy provider levied a 100 % repayment for an error in the supplier selection. How to defend?"
  sk:
    displayName: "Verejné zákazky a dotácie ČR"
    summary: "Režimy a druhy zadávacích konaní v ČR, námietky a návrh na ÚOHS, zmeny záväzku, dotačné podmienky, nezrovnalosti, porušenie rozpočtovej disciplíny a odvody, audity verejného sektora."
    examplePrompts:
      - "Obec chce rozdeliť rekonštrukciu školy na tri zákazky malého rozsahu. Je to prípustné a čo hrozí?"
      - "Boli sme vylúčení zo zadávacieho konania pre nesplnenie kvalifikácie. Aké lehoty bežia pre námietky a návrh na ÚOHS a aká je kaucia?"
      - "Poskytovateľ dotácie vyrubil odvod 100 % za chybu vo výberovom konaní dodávateľa. Ako sa brániť?"
description: Use when the user's matter involves Czech public procurement, subsidies or public-sector spending control from any side (zadavatel, dodavatel, příjemce dotace, poskytovatel, auditor) - zákon o zadávání veřejných zakázek (134/2016 Sb.), veřejná zakázka, zakázka malého rozsahu, podlimitní, nadlimitní, předpokládaná hodnota, dělení zakázky, zjednodušené podlimitní řízení, JŘBU, zadávací dokumentace, kvalifikace, hodnocení, mimořádně nízká nabídková cena, vyloučení, námitky, návrh k ÚOHS, kauce, zákaz uzavření smlouvy, změna závazku ze smlouvy, profil zadavatele, registr smluv, střet zájmů, sankce, dotace, rozhodnutí o poskytnutí dotace, veřejnoprávní smlouva, rozpočtová pravidla (218/2000, 250/2000 Sb.), porušení rozpočtové kázně, odvod, penále, prominutí, nesrovnalost, finanční oprava, korekce, kontrola, audit, finanční kontrola, NKÚ, dotační podvod. Standalone skill - bundles CODEXIS methodology with procurement-and-subsidy method; no need to load the general codexis skill.
---

# Veřejné zakázky a dotace ČR

Samostatný oborový skill pro zadávání zakázek, dotace a kontrolu veřejných výdajů. Dvě pravidla nad ostatními: **lhůty pro námitky a návrh jsou prekluzivní a krátké** a **u dotací platí vždy přísnější z pravidel (zákon × podmínky poskytovatele)**.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/134/2016/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf222'`, `cdx-cli get cdx://cz_law/218/2000/versions`, `cdx-cli search JD --query "porušení rozpočtové kázně odvod proporcionalita" --court "Nejvyšší správní soud" --limit 5`.
- Finanční limity (nařízení vlády o limitech), výše kauce, lhůty, procenta změn závazku a sazba penále **se mění** - vždy ověř v aktuálním znění k datu zahájení řízení / poskytnutí dotace; nikdy z paměti. Pravidla poskytovatele dotace (metodické pokyny, výzva, rozhodnutí) čti z dokumentů případu - CODEXIS je neobsahuje.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| ZZVZ | 134/2016 Sb. | `cz_law/134/2016` | Zásady (§ 6), zadavatel (§ 4), předpokládaná hodnota a zákaz dělení (§ 16-§ 23), režimy (§ 24-§ 31), druhy řízení (§ 52+), lhůty (§ 54+), zadávací podmínky (§ 36+), kvalifikace (§ 73+), vyloučení (§ 48), hodnocení (§ 114+), MNNC (§ 113), uveřejňování (§ 211+), změny závazku (§ 222), námitky (§ 241-§ 245), dozor ÚOHS (§ 248-§ 273), přestupky (§ 268+) |
| NV o finančních limitech | (aktuální nařízení vlády - ověř číslo) | zdroj `CR` | Hranice nadlimitní zakázky |
| Zákon o registru smluv | 340/2015 Sb. | `cz_law/340/2015` | Účinnost smluv zveřejněním, zrušení |
| Rozpočtová pravidla | 218/2000 Sb. | `cz_law/218/2000` | Dotace ze státního rozpočtu (§ 14+), pozastavení a výzva k vrácení (§ 14e-§ 14f), porušení rozpočtové kázně (§ 44), odvod a penále (§ 44a), prominutí |
| Rozpočtová pravidla územních rozpočtů | 250/2000 Sb. | `cz_law/250/2000` | Dotace obcí a krajů (§ 10a-§ 10d veřejnoprávní smlouva), PRK (§ 22) |
| Zákon o finanční kontrole | 320/2001 Sb. | `cz_law/320/2001` | Veřejnosprávní kontrola, interní audit |
| Kontrolní řád | 255/2012 Sb. | `cz_law/255/2012` | Průběh kontroly, protokol, námitky |
| Daňový řád | 280/2009 Sb. | `cz_law/280/2009` | Řízení o odvodu a penále (platební výměr, odvolání, lhůty) |
| Zákon o NKÚ | 166/1993 Sb. | `cz_law/166/1993` | Kontrola hospodaření se státním majetkem |
| Nařízení o společných ustanoveních (CPR) | (EU) 2021/1060 | zdroj `EU` | Fondy EU 2021-2027, nesrovnalosti, finanční opravy, střet zájmů |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Dotační podvod (§ 212), zjednání výhody (§ 256), pletichy (§ 257) |
| Správní řád / s. ř. s. | 500/2004 / 150/2002 Sb. | `cz_law/500/2004`, `cz_law/150/2002` | Řízení před ÚOHS, rozklad, žaloba (KS Brno), kasační stížnost |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu zahájení zadávacího řízení / vydání rozhodnutí o dotaci** → `/toc` → `/text?part=`.
2. Judikatura: **NSS** (`--court "Nejvyšší správní soud"`, senáty Afs u odvodů, As u zakázek; rozšířený senát k proporcionalitě odvodu a k povaze výzvy k vrácení dotace), **KS Brno** (správní žaloby proti ÚOHS), **SDEU** (`ES` - zadávací směrnice 2014/24/EU, in-house, změny smluv). Rozhodovací praxe ÚOHS je v CODEXIS jen zčásti - odkaz na uohs.gov.cz.
3. Komentář (`COMMENT`) k pojmům (funkční celek, jediný zadavatel, podstatná změna, střet zájmů); metodiky MMR a poskytovatelů jsou administrativní výklad, u dotací však smluvně závazný.

## Workflow

1. **Role a cíl.** Zadavatel (obec, příspěvková organizace, ministerstvo, sektorový zadavatel, dotovaný zadavatel § 4 odst. 2) × dodavatel × příjemce dotace × poskytovatel × auditor. Rada se liší podle strany; u veřejného sektoru vždy zkontroluj, které režimy se překrývají (ZZVZ × pravidla dotace × rozpočtová pravidla × registr smluv × zákon o obcích).
2. **Zadavatel - před zahájením.** Předpokládaná hodnota (§ 16-§ 23 - funkční celek, časová souvislost, **zákaz dělení § 18**), režim (VZMR mimo zákon, ale zásady § 6 a pravidla dotace; podlimitní; nadlimitní - limity dle nařízení vlády), druh řízení (ZPŘ § 53, otevřené § 56, užší, JŘSU, **JŘBU § 63 - jen taxativní důvody, zadavatel prokazuje**), výjimky (§ 29-§ 31, in-house § 11), předběžné tržní konzultace (§ 33), zadávací podmínky (§ 36 - nediskriminace, § 89 technické podmínky bez odkazu na výrobky), kvalifikace přiměřená (§ 73-§ 88), hodnoticí kritéria (§ 114-§ 118), lhůty (§ 54-§ 57), elektronizace (§ 211).
3. **Zadavatel - průběh a smlouva.** Vysvětlení a změny zadávací dokumentace (§ 98-§ 99 - prodloužení lhůty), otevírání, posouzení a hodnocení, MNNC (§ 113), vyloučení (§ 48 - fakultativní × obligatorní), oznámení o výběru (§ 123), **zákaz uzavření smlouvy** v blokační lhůtě (§ 246), písemná zpráva (§ 217), uveřejnění smlouvy (§ 219, registr smluv), skutečně uhrazená cena, **změny závazku (§ 222 - de minimis, vyhrazené, nepředvídané, záměna dodavatele; překročení = nová zakázka)**, střet zájmů (§ 44), sankční omezení (nařízení EU 833/2014 - ověř).
4. **Dodavatel - obrana.** Námitky (§ 241-§ 245): lhůta **15 dnů** od doručení / uveřejnění / dozvědění (u zadávacích podmínek nejpozději do konce lhůty pro nabídky - ověř), náležitosti (§ 244), zadavatel rozhodne do 15 dnů; **návrh k ÚOHS do 10 dnů** od doručení rozhodnutí o námitkách (§ 251), **kauce** (§ 255 - 1 % z nabídkové ceny v zákonných mezích, jinak paušál; ověř částky), návrh na zákaz plnění smlouvy (§ 254), předběžné opatření (§ 61 SŘ), rozklad 15 dnů, žaloba ke KS Brno; podnět (§ 258 - bez kauce, bez postavení účastníka). Náhrada škody proti zadavateli až po zrušení rozhodnutí.
5. **Dotace - životní cyklus.** Výzva → žádost → rozhodnutí / veřejnoprávní smlouva (podmínky = závazná pravidla vč. metodiky pro výběr dodavatele) → realizace (zakázky v dotaci: přísnější z ZZVZ a pravidel poskytovatele; publicita; udržitelnost; archivace) → kontrola (kontrolní řád, finanční kontrola, audit EU) → nesrovnalost / finanční oprava (tabulka oprav podle závažnosti) → **porušení rozpočtové kázně**: výzva k vrácení (§ 14f zák. 218/2000 Sb. - dobrovolné vrácení bez penále), platební výměr na odvod (finanční úřad / poskytovatel u územních rozpočtů) v režimu daňového řádu - odvolání 30 dnů, výše odvodu podle závažnosti (proporcionalita - NSS), penále (§ 44a - sazba za den, strop; ověř), prominutí (§ 44a - žádost, důvody hodné zvláštního zřetele), lhůta pro vyměření (ověř), správní žaloba.
6. **Audit veřejného sektoru.** Kolize režimů (zákon o obcích - schvalování zastupitelstvem, ZZVZ, rozpočtová pravidla, registr smluv, účetnictví); protokol a námitky (§ 13-§ 14 kontrolního řádu - lhůta 15 dnů, ověř); odpovědnost osob (zákon o obcích § 38 péče řádného hospodáře, trestní § 220-§ 221, § 256-§ 257 TZ); NKÚ bez sankční pravomoci, ale s podnětem.
7. **Trestní a sankční rovina.** Dotační podvod (§ 212 TZ), poškození finančních zájmů EU (§ 260), zjednání výhody (§ 256), pletichy (§ 257); přestupky zadavatele (§ 268-§ 270 ZZVZ - pokuta do 10 % ceny / 20 mil. Kč - ověř); zákaz plnění smlouvy (§ 264).

## Časté pasti

- Dělení zakázky pod limit (§ 18) - nejčastější důvod odvodu dotace i pokuty ÚOHS.
- VZMR brána jako „bez pravidel" - platí § 6 ZZVZ, pravidla poskytovatele a vnitřní směrnice zadavatele.
- Námitky podané po 15denní lhůtě nebo návrh bez předchozích námitek / bez kauce - ÚOHS zastaví řízení.
- Smlouva uzavřená v blokační lhůtě nebo bez uveřejnění v registru smluv - neúčinná, riziko zákazu plnění.
- Dodatek nad limity § 222 podepsaný „protože se to nestihlo" - nová zakázka bez řízení.
- JŘBU odůvodněné „jediným možným dodavatelem" bez průzkumu trhu a bez prokázání technických důvodů.
- Odvod za porušení rozpočtové kázně přijatý jako automaticky 100 % - NSS vyžaduje proporcionalitu k závažnosti; napadnout výši, ne jen důvod.
- Dobrovolné vrácení dotace po výzvě § 14f bez posouzení, zda porušení vůbec nastalo - vrácené prostředky se obtížně získávají zpět.
- Odvolání proti platebnímu výměru počítané podle správního řádu (15 dnů) místo daňového řádu (30 dnů).
- Kvalifikační požadavky opsané z předchozí zakázky bez přiměřenosti k předmětu - diskriminace.
- Střet zájmů člena hodnoticí komise nebo příjemce (čl. 61 finančního nařízení EU, § 44 ZZVZ) neošetřen.
- Doplňování limitů, sazeb, čísel jednacích a IČO dodavatelů z paměti - vždy z aktuálního znění, dokumentů nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a lhůta** (lze/nelze, jaký prostředek, kam, do kdy, kauce).
2. **Role, režim a překrývající se pravidla** (ZZVZ × dotace × rozpočtová pravidla × registr smluv).
3. **Právní rámec** - ZZVZ / rozpočtová pravidla / DŘ v aktuálním znění, s odkazy; co říkají podmínky dotace (`[DOPLNIT z rozhodnutí o dotaci]`).
4. **Postup krok za krokem** (podání, náležitosti, lhůty, poplatky, důkazy).
5. **Rizika** (odvod, penále, pokuta ÚOHS, zákaz plnění, trestní rovina) a **alternativy** (dobrovolná náprava, prominutí, dohoda).
6. **Judikatura a rozhodovací praxe** - jen ověřená v CODEXIS / na uohs.gov.cz, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 2 Afs 123/2025 - …`, `KS Brno - 62 Af 12/2025 - …`) z metadat, nikdy vymyšlené; rozhodnutí ÚOHS s číslem jednacím z uohs.gov.cz.
- Zachovej kvalifikátory („do 15 dnů ode dne, kdy se dozvěděl“, „nejpozději do skončení lhůty pro podání nabídek“, „podstatná změna“).
- Jeden časový řez; u zakázky znění účinné k zahájení řízení, u dotace k datu rozhodnutí.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity, kauce, procenta změn, sazby penále a lhůty nikdy z paměti - vždy z aktuálního znění s odkazem a datem účinnosti.
- Mimo CODEXIS jen oficiální zdroje (uohs.gov.cz, portal-vz.cz, mmr.gov.cz, mfcr.cz, dotační portály poskytovatelů) když CODEXIS neodpovídá; podmínky dotace vždy z dokumentů případu.
