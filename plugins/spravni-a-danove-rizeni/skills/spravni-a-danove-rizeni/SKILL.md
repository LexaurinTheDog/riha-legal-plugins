---
uuid: 14ac3e62-b159-48c8-8ae6-4919f615132d
name: spravni-a-danove-rizeni
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Správní a daňové řízení ČR"
    summary: "Obrana proti rozhodnutím a postupům úřadů a správce daně - odvolání, přezkum, správní žaloba, kasační stížnost, daňová kontrola, sankce, prekluze, lhůty."
    examplePrompts:
      - "Finanční úřad doměřil DPH po kontrole a vyměřil penále. Jaké procesní námitky máme a do kdy podat odvolání?"
      - "Odvolací orgán potvrdil rozhodnutí stavebního úřadu. Připrav osnovu správní žaloby a posuď odkladný účinek."
      - "Úřad je rok nečinný v řízení o žádosti. Jaké prostředky obrany máme a v jakém pořadí?"
  en:
    displayName: "Czech Administrative and Tax Procedure"
    summary: "Challenging decisions and conduct of authorities and tax administrators - appeals, review, judicial review, cassation, tax audits, penalties, time bars, deadlines."
    examplePrompts:
      - "The tax office assessed additional VAT after an audit and imposed a penalty. Which procedural objections do we have and by when to appeal?"
      - "The appellate body upheld the building authority's decision. Draft an outline of the judicial review action and assess suspensive effect."
      - "An authority has been inactive for a year on our application. Which remedies do we have and in what order?"
  sk:
    displayName: "Správne a daňové konanie ČR"
    summary: "Obrana proti rozhodnutiam a postupom úradov a správcu dane v ČR - odvolanie, preskúmanie, správna žaloba, kasačná sťažnosť, daňová kontrola, sankcie, preklúzia, lehoty."
    examplePrompts:
      - "Finančný úrad dorubil DPH po kontrole a vyrubil penále. Aké procesné námietky máme a dokedy podať odvolanie?"
      - "Odvolací orgán potvrdil rozhodnutie stavebného úradu. Priprav osnovu správnej žaloby a posúď odkladný účinok."
      - "Úrad je rok nečinný v konaní o žiadosti. Aké prostriedky obrany máme a v akom poradí?"
description: Use when the user challenges or responds to a Czech public authority or tax administrator - správní řízení, správní řád (500/2004 Sb.), daňový řád (280/2009 Sb.), soudní řád správní (150/2002 Sb.), rozhodnutí úřadu, výzva, usnesení, opatření obecné povahy, nečinnost, nezákonný zásah, odvolání, rozklad, přezkumné řízení, obnova řízení, správní žaloba, žaloba proti rozhodnutí, kasační stížnost, Nejvyšší správní soud, odkladný účinek, daňová kontrola, postup k odstranění pochybností, doměření daně, dodatečný platební výměr, penále, úrok z prodlení, pokuta za opožděné tvrzení, zajišťovací příkaz, daňová exekuce, lhůta pro stanovení daně (prekluze), prominutí, přestupek, stavební úřad, katastrální úřad, živnostenský úřad, úřad práce, celní správa, ÚOHS, ČNB, doručování úřadem, fikce doručení, poplatek, správní poplatek. Standalone skill - bundles CODEXIS methodology with the administrative-defence method; no need to load the general codexis skill. For substantive tax questions combine with the tax-law skill.
---

# Správní a daňové řízení ČR

Samostatný oborový skill pro procesní obranu proti úřadům a správci daně. Klíčová otázka není „má úřad pravdu“, ale **v jakém režimu, proti jakému aktu, jakým prostředkem a do kdy** - odpověď na ni určuje všechno ostatní.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/500/2004/versions`, `cdx-cli get cdx://cz_law/280/2009/versions`, `cdx-cli get cdx://cz_law/150/2002/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf148'`, `cdx-cli search JD --query "lhůta pro stanovení daně prekluze 148" --court "Nejvyšší správní soud" --limit 5`.
- Lhůty, sazby sankcí a číslování odstavců **vždy ověř v aktuálním znění**; nikdy z paměti. Zvláštní zákon může obecnou lhůtu měnit - vždy zkontroluj i předpis, podle kterého úřad rozhodoval.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| SŘ - správní řád | 500/2004 Sb. | `cz_law/500/2004` | Obecné správní řízení: doručování (§ 19-§ 26), lhůty (§ 39-§ 41), podání (§ 37), vyjádření (§ 36), rozhodnutí (§ 67-§ 76), odvolání (§ 81-§ 93), přezkum (§ 94+), obnova (§ 100+), nečinnost (§ 80), stížnost (§ 175), OOP (§ 171+) |
| DŘ - daňový řád | 280/2009 Sb. | `cz_law/280/2009` | Daňové řízení: lhůty (§ 32-§ 38), doručování (§ 39-§ 51), kontrola (§ 85-§ 88), POP (§ 89-§ 90), odvolání (§ 109-§ 116), obnova a přezkum (§ 117-§ 123), lhůta pro stanovení daně (§ 148), placení a exekuce (§ 149+, § 175+), sankce (§ 250-§ 254), prominutí (§ 259+) |
| s. ř. s. - soudní řád správní | 150/2002 Sb. | `cz_law/150/2002` | Žaloba proti rozhodnutí (§ 65-§ 78), nečinnostní (§ 79), zásahová (§ 82), OOP (§ 101a), kasační stížnost (§ 102-§ 110), odkladný účinek (§ 73), předběžné opatření (§ 38) |
| Zákon o odpovědnosti za přestupky | 250/2016 Sb. | `cz_law/250/2016` | Přestupkové řízení, promlčení (§ 29-§ 32), sankce, opravné prostředky |
| Kontrolní řád | 255/2012 Sb. | `cz_law/255/2012` | Kontroly mimo daňové řízení, námitky proti protokolu |
| Zákon o odpovědnosti státu za škodu | 82/1998 Sb. | `cz_law/82/1998` | Nezákonné rozhodnutí, nesprávný úřední postup, předběžné uplatnění |
| Zákon o správních poplatcích | 634/2004 Sb. | `cz_law/634/2004` | Poplatky, výzva k zaplacení (režim DŘ) |
| Zákon o Ústavním soudu | 182/1993 Sb. | `cz_law/182/1993` | Ústavní stížnost po vyčerpání prostředků (§ 72, § 75) |
| Listina základních práv a svobod | 2/1993 Sb. | `cz_law/2/1993` | Čl. 36-čl. 38 spravedlivý proces, čl. 11 vlastnictví |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`. Nejprve zvláštní zákon (stavební, živnostenský, daňový hmotný…), pak obecný procesní předpis - zvláštní úprava má přednost (§ 1 odst. 2 SŘ, § 4 DŘ).
2. Judikatura: **NSS** (`--court "Nejvyšší správní soud"`; rozšířený senát má nejvyšší váhu - hledej „rozšířený senát“), krajské soudy (správní senáty), ÚS. U daní senáty Afs, u ostatních As, Ads, Azs. Vždy ověř datum a to, zda rozhodnutí nebylo překonáno rozšířeným senátem nebo novelou.
3. Komentář (`COMMENT`) pro výklad pojmů (rozhodnutí × jiný úkon, zásah, nečinnost); literatura (`LT`) jen doplňkově.

## Workflow procesní obrany

1. **Režim.** SŘ × DŘ × zvláštní zákon × s. ř. s. Poučení úřadu režim neurčuje - určuje ho zákon (např. výzva k zaplacení správního poplatku je rozhodnutím v režimu daňového řádu, byť ji vydá „správní“ úřad).
2. **Povaha aktu.** Rozhodnutí (§ 67 SŘ / § 101 DŘ) × usnesení × výzva × sdělení/osvědčení × opatření obecné povahy × faktický zásah × nečinnost. Povaha určuje prostředek: odvolání/rozklad × námitky/stížnost × žaloba proti rozhodnutí × zásahová žaloba (subsidiární) × nečinnostní žaloba (po vyčerpání § 80 SŘ / § 38 DŘ) × návrh na zrušení OOP.
3. **Lhůta.** Odvolání SŘ 15 dnů (§ 83), DŘ 30 dnů (§ 109 odst. 4), rozklad stejně; žaloba proti rozhodnutí 2 měsíce od doručení (§ 72 s. ř. s.), zásahová 2 měsíce subjektivní / 2 roky objektivní (§ 84), kasační stížnost 2 týdny (§ 106 odst. 2), ústavní stížnost 2 měsíce - **vše ověř v aktuálním znění**, zvláštní zákon může lhůtu měnit. Počátek běhu odvis od doručení - zkontroluj fikci doručení (§ 24 SŘ / § 47 DŘ), doručování zástupci, datovou schránku.
4. **Procesní audit rozhodnutí.** Příslušnost (věcná, místní, funkční), podjatost (§ 14 SŘ / § 77 DŘ), účastenství a práva účastníka (§ 36 odst. 3 SŘ seznámení s podklady; § 88 DŘ projednání zprávy o kontrole), dokazování a hodnocení důkazů, odůvodnění (§ 68 odst. 3 SŘ / § 102 odst. 2-4 DŘ), výrok (určitost, právní základ), poučení, podpis a doručení. **Prekluze** (lhůta pro stanovení daně § 148 DŘ; zánik odpovědnosti za přestupek § 29 zákona 250/2016 Sb.) - soud ji zkoumá z úřední povinnosti, uplatni ji vždy.
5. **Věcná argumentace.** Výklad zvláštního zákona + hierarchie pramenů (zákon → vyhláška → metodika/pokyn GFŘ, který váže správu, ne soud → judikatura NSS/ÚS/SDEU). U daní odděluj hmotné právo (co se zdaňuje) od procesu (jak se doměřuje) a sankce (penále § 251 × úrok z prodlení § 252 × pokuta § 250 - odlišné podmínky a možnost prominutí § 259a-§ 259c).
6. **Odkladný účinek a předběžná ochrana.** Odvolání v SŘ má odkladný účinek ze zákona (§ 85), lze vyloučit; v DŘ odvolání odkladný účinek zpravidla nemá (§ 109 odst. 5). Žaloba ve správním soudnictví odkladný účinek nemá - navrhnout podle § 73 odst. 2 s. ř. s. s tvrzením nepoměrně větší újmy; předběžné opatření § 38.
7. **Řetězec prostředků.** Žaloba proti rozhodnutí vyžaduje vyčerpání řádných opravných prostředků (§ 68 písm. a) s. ř. s.); kasační stížnost jen prostřednictvím advokáta (§ 105 odst. 2); ústavní stížnost po vyčerpání všech prostředků včetně kasační stížnosti. Náhrada škody podle zákona 82/1998 Sb. až po zrušení rozhodnutí pro nezákonnost; předběžně uplatnit u úřadu (§ 14).
8. **Náklady a poplatky.** Soudní poplatek za žalobu a kasační stížnost (sazebník, ověř), náhrada nákladů podle úspěchu (§ 60 s. ř. s.), advokátní tarif; v odvolacím správním řízení se náklady zpravidla nepřiznávají.

## Časté pasti

- Podání odvolání podle SŘ lhůty (15 dnů) tam, kde platí DŘ (30 dnů), nebo naopak; režim určuje zákon, ne hlavička rozhodnutí.
- Žaloba podaná bez vyčerpání odvolání - odmítnutí pro nepřípustnost.
- Zásahová žaloba místo žaloby proti rozhodnutí (nebo naopak) - subsidiarita a rozdílné lhůty.
- Spolehnutí na odkladný účinek, který zákon nedává (daňové odvolání, správní žaloba).
- Přehlédnutí prekluze - nejsilnější námitka, kterou lze uplatnit kdykoli.
- Zacházení s pokynem GFŘ nebo metodikou ministerstva jako se zákonem.
- Kasační stížnost sepsaná bez advokáta nebo mimo důvody § 103 s. ř. s.
- Citování rozhodnutí NSS, které bylo překonáno rozšířeným senátem - ověř datum a navazující judikaturu.
- Záměna penále, úroku z prodlení a pokuty za opožděné tvrzení - různé podmínky a různá cesta k prominutí.
- Doplňování čísel jednacích, dat doručení a názvů úřadů z paměti - vždy z listiny nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a lhůta** v první větě (jaký prostředek, kam, do kdy).
2. **Režim a povaha aktu** s odůvodněním.
3. **Procesní vady** - seznam s § a důsledkem (nezákonnost × nicotnost × vada bez vlivu).
4. **Věcné argumenty** s hierarchií pramenů a judikaturou NSS/ÚS.
5. **Odkladný účinek / předběžná ochrana** - zda a jak žádat.
6. **Další kroky a řetězec prostředků** včetně nákladů a poplatků.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 Afs 123/2025 - …`, `ÚS - Pl. ÚS 1/26 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („ode dne doručení“, „nejpozději“, „po marném uplynutí“, „z úřední povinnosti“).
- Jeden časový řez; u procesních úkonů znění účinné v době úkonu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (nssoud.cz, usoud.cz, financnisprava.cz, justice.cz) když CODEXIS neodpovídá.
- Lhůty a sazby nikdy z paměti - vždy z aktuálního znění s odkazem a datem účinnosti.
