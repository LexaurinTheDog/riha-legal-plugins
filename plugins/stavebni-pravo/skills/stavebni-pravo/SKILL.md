---
uuid: 88553864-a872-42ab-bca4-26512542631b
name: stavebni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Stavební právo ČR"
    summary: "Povolování staveb podle nového stavebního zákona a přechodný režim, účastníci a sousedé, černé stavby a odstranění, kolaudace, imise a hranice, smlouva o dílo na stavbu a vady."
    examplePrompts:
      - "Soused staví bez povolení 1,5 m od hranice a stíní nám zahradu. Co můžeme udělat u stavebního úřadu a u soudu?"
      - "Stavební úřad zamítl žádost o povolení záměru pro rozpor s územním plánem. Připrav osnovu odvolání a posuď šance."
      - "Zhotovitel předal dům s vadami střechy a fakturuje doplatek. Jak postupovat podle smlouvy o dílo?"
  en:
    displayName: "Czech Construction Law"
    summary: "Permitting under the new Building Act and the transitional regime, participants and neighbours, unauthorised structures and removal, occupancy, nuisance and boundaries, construction contracts and defects."
    examplePrompts:
      - "A neighbour is building without a permit 1.5 m from the boundary and shading our garden. What can we do before the building authority and the court?"
      - "The building authority rejected the permit application for conflict with the zoning plan. Draft an appeal outline and assess the chances."
      - "The contractor handed over a house with roof defects and invoices the balance. How to proceed under the works contract?"
  sk:
    displayName: "Stavebné právo ČR"
    summary: "Povoľovanie stavieb podľa nového českého stavebného zákona a prechodný režim, účastníci a susedia, čierne stavby a odstránenie, kolaudácia, imisie a hranice, zmluva o dielo na stavbu a vady."
    examplePrompts:
      - "Sused stavia bez povolenia 1,5 m od hranice a tieni nám záhradu. Čo môžeme urobiť na stavebnom úrade a na súde?"
      - "Stavebný úrad zamietol žiadosť o povolenie zámeru pre rozpor s územným plánom. Priprav osnovu odvolania a posúď šance."
      - "Zhotoviteľ odovzdal dom s vadami strechy a fakturuje doplatok. Ako postupovať podľa zmluvy o dielo?"
description: Use when the user's matter involves Czech construction, planning or building disputes - stavební zákon (283/2021 Sb., dříve 183/2006 Sb.), stavební úřad, povolení záměru, stavební povolení, územní rozhodnutí, ohlášení, drobná / jednoduchá / vyhrazená stavba, územní plán, regulační plán, územní studie, plánovací smlouva, závazné stanovisko, dotčený orgán, jednotné environmentální stanovisko, EIA, účastník řízení, soused, spolek, kolaudace, změna v užívání, odstranění stavby, dodatečné povolení, černá stavba, přestupek stavebníka, stavební dozor, autorizovaný projektant, dokumentace, památková ochrana, vyvlastnění, věcné břemeno pro sítě, sousedské spory, imise, hluk, stínění, stromy u hranice, plot, oplocení, přístup k pozemku, neoprávněná stavba na cizím pozemku, právo stavby, smlouva o dílo na stavbu, vady stavby, převzetí díla, zádržné, vícepráce, developer, developerská smlouva. Standalone skill - bundles CODEXIS methodology with construction-practice method; no need to load the general codexis skill.
---

# Stavební právo ČR

Samostatný oborový skill pro povolování staveb a spory kolem nich. První otázka u každého řízení: **podle kterého stavebního zákona běží** - nový zákon 283/2021 Sb. se plně použije od 1. 7. 2024, řízení zahájená dříve se dokončují podle zákona 183/2006 Sb. (přechodná ustanovení). Druhá: **veřejnoprávní cesta (úřad) × soukromoprávní cesta (soud)** - obvykle obě souběžně.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/283/2021/versions`, `cdx-cli get 'cdx://doc/<versionId>/toc'`, `cdx-cli get cdx://cz_law/183/2006/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf1013'`, `cdx-cli search JD --query "neoprávněná stavba souhlas vlastníka pozemku" --court "Nejvyšší soud" --limit 5`.
- Nový stavební zákon byl před účinností několikrát novelizován a prováděcí vyhlášky jsou nové - **paragrafy nového zákona vždy dohledávej přes `/toc`, nikdy z paměti**; u starého zákona ověř, zda se ještě použije. Lhůty, vzdálenosti, limity a sazby ověř v aktuálním znění.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Nový stavební zákon | 283/2021 Sb. | `cz_law/283/2021` | Stavební správa, územní plánování, povolení záměru, zrychlené a rámcové povolení, kolaudace, odstranění, dodatečné povolení, přestupky, přechodná ustanovení |
| Starý stavební zákon | 183/2006 Sb. | `cz_law/183/2006` | Řízení zahájená před 1. 7. 2024, dokončení, kolaudace dříve povolených staveb |
| Prováděcí vyhlášky k novému SZ | vyhl. o požadavcích na výstavbu, o dokumentaci staveb (ověř čísla) | zdroj `CR` | Odstupy, technické požadavky, obsah dokumentace |
| Správní řád | 500/2004 Sb. | `cz_law/500/2004` | Účastenství (§ 27), doručování, závazná stanoviska (§ 149), odvolání, opomenutý účastník (§ 84), přezkum |
| Soudní řád správní | 150/2002 Sb. | `cz_law/150/2002` | Žaloba proti rozhodnutí, odkladný účinek, návrh na zrušení územního plánu (§ 101a) |
| Zákon o jednotném environmentálním stanovisku | 148/2023 Sb. | `cz_law/148/2023` | JES nahrazující dílčí stanoviska |
| EIA | 100/2001 Sb. | `cz_law/100/2001` | Posuzování vlivů, navazující řízení, dotčená veřejnost |
| Vyvlastňovací zákon | 184/2006 Sb. | `cz_law/184/2006` | Vyvlastnění a náhrada |
| Liniový zákon | 416/2009 Sb. | `cz_law/416/2009` | Dopravní, vodní, energetická infrastruktura |
| Zákon o ochraně přírody / vodní / ZPF / památkový | 114/1992, 254/2001, 334/1992, 20/1987 Sb. | `cz_law/…` | Dotčené orgány a jejich závazná stanoviska |
| OZ - sousedství a stavby | 89/2012 Sb. | `cz_law/89/2012` | Imise (§ 1013), zadržení výstavby (§ 1004), stromy a hranice (§ 1016-§ 1017), vstup na pozemek (§ 1021-§ 1023), stavba jako součást pozemku (§ 506, § 3054+), neoprávněná stavba (§ 1084-§ 1086), právo stavby (§ 1240+), smlouva o dílo - stavba (§ 2623-§ 2630) |
| OZ 1964 | 40/1964 Sb. | `cz_law/40/1964` | Neoprávněná stavba zřízená před 2014 (§ 135c) |

## Rešeršní strategie

1. Nejprve `/versions` obou stavebních zákonů k datu zahájení řízení, pak `/toc` nového zákona a teprve `/text?part=` - číslování nového zákona nehádej.
2. Judikatura: **NSS** (`--court "Nejvyšší správní soud"`, senáty As) - účastenství sousedů, závazná stanoviska, dodatečné povolení, územní plány (rozšířený senát); **NS** senát 22 Cdo - imise, neoprávněná stavba, hranice; ÚS k ochraně vlastnictví. Ověř, zda rozhodnutí k zákonu 183/2006 Sb. přenositelně platí i pro nový zákon.
3. Komentář (`COMMENT`) k pojmům (stavba, záměr, účastník, imise nad míru přiměřenou poměrům); metodiky MMR jsou administrativní výklad.

## Workflow stavebního praktika

1. **Režim.** Datum zahájení řízení / provedení stavby → starý × nový zákon; typ stavebního úřadu (obecní, krajský, jiný podle nového zákona - ověř příslušnost); u přestupků datum spáchání.
2. **Klasifikace záměru.** Drobná stavba (bez povolení) × jednoduchá × vyhrazená × ostatní; změna dokončené stavby, změna v užívání, terénní úpravy, odstranění. Klasifikace určuje, zda a jaké povolení, jaká dokumentace a kdo ji zpracuje (autorizovaná osoba).
3. **Soulad s územním plánováním.** Územní plán, regulační plán, územní studie, stavební uzávěra, plánovací smlouva s obcí; rozpor s ÚP nelze zhojit v řízení - řešit změnou ÚP nebo návrhem na zrušení jeho části (§ 101a s. ř. s., lhůty a aktivní legitimace ověř).
4. **Dotčené orgány a stanoviska.** Závazná stanoviska (památková péče, ochrana přírody, vodoprávní, hygiena, hasiči), jednotné environmentální stanovisko, EIA; závazné stanovisko lze napadnout jen v odvolání proti rozhodnutí (§ 149 SŘ), ne samostatnou žalobou - ověř výjimky.
5. **Účastníci.** Stavebník, vlastník pozemku/stavby, sousedé přímo dotčení, obec, spolky (EIA/ochrana přírody); opomenutý účastník - odvolání ve lhůtě od dozvědění (§ 84 SŘ, objektivní limit). Námitky uplatnit včas v řízení - koncentrace.
6. **Řízení o povolení.** Žádost, dokumentace, lhůty úřadu (nový zákon stanoví lhůty a mechanismus při nečinnosti - ověř), rozhodnutí, odvolání 15 dnů, přezkum, správní žaloba 2 měsíce, odkladný účinek na návrh; elektronické podání přes portál stavebníka (ověř aktuální stav).
7. **Černé stavby.** Řízení o odstranění × dodatečné povolení (jen při souladu s územním plánem a splnění požadavků - stavebník prokazuje), přestupky, pokuty, výkon rozhodnutí; užívání bez kolaudace = přestupek.
8. **Sousedské spory u soudu.** Imise (§ 1013 - nad míru přiměřenou poměrům; přímé imise zakázány), zadržení výstavby (§ 1004 - jen před dokončením, jinak úřad), stromy a kořeny (§ 1016-§ 1017), přístup na pozemek (§ 1021-§ 1023), hranice (§ 1028), neoprávněná stavba (po 2014 § 1084-§ 1086; před 2014 § 135c OZ 1964 - souhlas vlastníka pozemku není nabývacím titulem, soud musí věc vypořádat, žalobu nelze zamítnout jen pro neochotu). Předběžné opatření, znalecký posudek (stínění, hluk - hygienické limity).
9. **Smluvní vrstva.** Smlouva o dílo na stavbu (§ 2623-§ 2630 OZ): předání a převzetí s výhradami, vady - oznámení bez zbytečného odkladu, skryté vady stavby do 5 let (§ 2629), zádržné, vícepráce jen písemným dodatkem (§ 2622 rozpočet), harmonogram a smluvní pokuty, odstoupení, odpovědnost projektanta a dozoru (§ 2630 - solidarita subdodavatelů, projektanta a dozoru), FIDIC odchylky; developerské smlouvy (rezervace, budoucí kupní, katastr).

## Časté pasti

- Aplikace nového stavebního zákona na řízení zahájené před 1. 7. 2024 (nebo starého na nové).
- Paragrafy nového zákona citované z paměti nebo z metodik - číslování se během legislativního procesu měnilo.
- Soused, který nepodal námitky v řízení, je uplatňuje až v odvolání nebo žalobě - koncentrace.
- Samostatná žaloba proti závaznému stanovisku místo odvolání proti rozhodnutí.
- Žaloba na zadržení výstavby (§ 1004) po dokončení stavby - patří na úřad.
- Neoprávněná stavba posuzovaná podle OZ 2012, ač byla zřízena před 2014 (a naopak).
- Vlastník pozemku převzatý z tvrzení klienta místo z výpisu z katastru.
- Vícepráce provedené bez písemného dodatku - zhotovitel bez nároku na cenu, objednatel bez záruky.
- Převzetí stavby bez výhrad a bez soupisu vad - ztížené uplatnění zjevných vad.
- Spoléhání na dodatečné povolení černé stavby v rozporu s územním plánem.
- Užívání stavby před kolaudací „na zkoušku" - přestupek a problém s pojištěním.
- Doplňování parcelních čísel, vzdáleností a dat z paměti - vždy z listin, katastru nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a lhůta** (která cesta - úřad / soud / obojí, co podat, do kdy).
2. **Režim a klasifikace záměru.**
3. **Právní rámec** - správný stavební zákon + OZ, s odkazy dohledanými přes `/toc`.
4. **Postup krok za krokem** (podání, účastníci, stanoviska, opravné prostředky, důkazy).
5. **Rizika a alternativy** (dodatečné povolení, dohoda se sousedem, změna ÚP, náklady a délka).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 As 123/2025 - …`, `NS - 22 Cdo 2886/2023 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nad míru přiměřenou poměrům“, „bez zbytečného odkladu“, „nejpozději do“).
- Jeden časový řez; výslovně uveď, který stavební zákon se použil a proč.

## Hard Rules

- Paragraf nového stavebního zákona nikdy z paměti - vždy `/toc` → `/text?part=`; změny → `/versions`.
- `docId` jen z API.
- Údaje o pozemcích a vlastnících výhradně z katastru nemovitostí; mimo CODEXIS jen oficiální zdroje (ČÚZK, MMR, nssoud.cz) když CODEXIS neodpovídá.
- Vzdálenosti, limity, lhůty a sazby nikdy z paměti - vždy z aktuálního znění s odkazem.
