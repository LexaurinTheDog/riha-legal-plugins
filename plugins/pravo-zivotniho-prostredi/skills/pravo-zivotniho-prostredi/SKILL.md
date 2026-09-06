---
uuid: f5a03fe0-0212-4d96-9350-debb036e07eb
name: pravo-zivotniho-prostredi
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Právo životního prostředí ČR"
    summary: "EIA a integrované povolování, vodní právo a povolení k vypouštění, ochrana ovzduší, odpady a obaly, ochrana přírody a krajiny, lesy a zemědělská půda, hluk, ekologická újma a sanace, kontroly a pokuty ČIŽP, účast veřejnosti a spolků."
    examplePrompts:
      - "ČIŽP uložila klientovi pokutu 800 000 Kč za nakládání s odpady bez povolení. Jaké jsou lhůty a důvody pro odvolání a lze pokutu snížit?"
      - "Spolek chce napadnout záměr skladové haly u obce. V jaké fázi (EIA, územní řízení, povolení) se může účastnit a jak založit aktivní legitimaci?"
      - "Klient koupil pozemek se starou ekologickou zátěží. Kdo odpovídá za sanaci a jak se bránit uložení nápravných opatření?"
  en:
    displayName: "Czech Environmental Law"
    summary: "EIA and integrated permitting, water law and discharge permits, air protection, waste and packaging, nature and landscape protection, forests and agricultural land, noise, environmental liability and remediation, inspections and penalties by ČIŽP, public participation and NGO standing."
    examplePrompts:
      - "The Environmental Inspectorate fined my client CZK 800,000 for handling waste without a permit. What are the deadlines and grounds for appeal and can the fine be reduced?"
      - "An association wants to challenge a warehouse project near the village. At which stage (EIA, zoning, permit) can it participate and how to establish standing?"
      - "My client bought land with historical contamination. Who is liable for remediation and how to defend against remedial orders?"
  sk:
    displayName: "Právo životného prostredia ČR"
    summary: "EIA a integrované povoľovanie, vodné právo a povolenie na vypúšťanie, ochrana ovzdušia, odpady a obaly, ochrana prírody a krajiny, lesy a poľnohospodárska pôda, hluk, ekologická ujma a sanácia, kontroly a pokuty ČIŽP, účasť verejnosti a spolkov."
    examplePrompts:
      - "ČIŽP uložila klientovi pokutu 800 000 Kč za nakladanie s odpadmi bez povolenia. Aké sú lehoty a dôvody na odvolanie a možno pokutu znížiť?"
      - "Spolok chce napadnúť zámer skladovej haly pri obci. V akej fáze (EIA, územné konanie, povolenie) sa môže zúčastniť a ako založiť aktívnu legitimáciu?"
      - "Klient kúpil pozemok so starou ekologickou záťažou. Kto zodpovedá za sanáciu a ako sa brániť uloženiu nápravných opatrení?"
description: Use when the user's matter involves environmental regulation, permitting or liability in the Czech Republic - životní prostředí, právo životního prostředí, EIA, posuzování vlivů na životní prostředí (100/2001 Sb.), integrované povolení, IPPC (76/2002 Sb.), vodní zákon (254/2001 Sb.), povolení k nakládání s vodami, vypouštění odpadních vod, ochrana ovzduší (201/2012 Sb.), zákon o odpadech (541/2020 Sb.), nakládání s odpady bez povolení, obaly, ochrana přírody a krajiny (114/1992 Sb.), kácení dřevin, zvláště chráněné druhy, Natura 2000, lesní zákon, odnětí lesa, zemědělský půdní fond, vynětí ze ZPF, hluk, hlukové limity, ekologická újma (167/2008 Sb.), sanace, nápravná opatření, Česká inspekce životního prostředí, ČIŽP, přestupky, účast veřejnosti, spolek jako účastník řízení, Aarhuská úmluva, změna klimatu, ESG a CSRD. Standalone skill - bundles CODEXIS methodology with environmental-practice method; no need to load the general codexis skill.
---

# Právo životního prostředí ČR

Samostatný oborový skill pro environmentální regulaci, povolování a odpovědnost. Základní reflex: environmentální právo je **složkové** (voda, ovzduší, odpady, příroda, les, půda, hluk) a **procesní vrstvy se skládají** (EIA → územní plánování → povolení záměru dle nového stavebního zákona s integrovanými závaznými stanovisky → provozní povolení → kontrola ČIŽP) - vždy určit, ve které složce a vrstvě klient je a kdo je příslušný orgán. Druhý reflex: **lhůty pro účast veřejnosti a pro napadení jsou krátké a prekluzivní** (připomínky k EIA, přihlášení spolku do řízení do 8 dnů od informace - ověř, odvolání 15 dnů, žaloba 2 měsíce). Třetí: sankce ČIŽP jsou vysoké, ale často napadnutelné na přiměřenosti a na vymezení skutku.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/100/2001/versions`, `cdx-cli get cdx://cz_law/541/2020/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf70'`, `cdx-cli get cdx://cz_law/114/1992/versions`, `cdx-cli search JD --query "účastenství spolku řízení ochrana přírody 70 aktivní legitimace" --court "Nejvyšší správní soud" --limit 5`, `cdx-cli search JD --query "pokuta ČIŽP odpady přiměřenost výše" --court "Nejvyšší správní soud" --limit 5`.
- Nový stavební zákon (283/2021 Sb.) a zákon o jednotném environmentálním stanovisku (148/2023 Sb.) změnily integraci složkových stanovisek do povolování; **čísla paragrafů, lhůty, limity (kácení, ZPF odvody, hluk), sazby pokut a příslušnost orgánů ověř v aktuálním znění k datu**; nikdy z paměti. Přechodná ustanovení určují, zda řízení běží podle starého nebo nového režimu.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o posuzování vlivů na ŽP (EIA) | 100/2001 Sb. | `cz_law/100/2001` | Záměry (příloha 1 - kategorie I povinně, II zjišťovací řízení), zjišťovací řízení (§ 7), dokumentace, posudek, veřejné projednání, **závazné stanovisko** (§ 9a - platnost 7 let, ověření změn § 9a odst. 6), navazující řízení a dotčená veřejnost (§ 3 písm. i), § 9c - účast, § 9d - žaloba), SEA koncepcí (§ 10a+), přeshraniční |
| Zákon o integrované prevenci (IPPC) | 76/2002 Sb. | `cz_law/76/2002` | Integrované povolení pro zařízení dle přílohy 1, BAT/BREF, změny povolení, přezkum, účast veřejnosti, sankce |
| Zákon o jednotném environmentálním stanovisku | 148/2023 Sb. | `cz_law/148/2023` | JES nahrazuje složková stanoviska pro povolení záměru (rozsah, výjimky, lhůty) |
| Vodní zákon | 254/2001 Sb. | `cz_law/254/2001` | Nakládání s vodami a povolení (§ 8+), odběr a studny (§ 8, § 55), vypouštění odpadních vod (§ 8, § 38 - limity NV 401/2015 Sb.), vodní díla (§ 55+, stavební povolení vodoprávním úřadem), záplavová území (§ 66+), ochranná pásma vodních zdrojů (§ 30), havárie (§ 40-§ 42), poplatky (§ 88+), přestupky (§ 116+), správce toku |
| Zákon o ochraně ovzduší | 201/2012 Sb. | `cz_law/201/2012` | Stacionární zdroje (vyjmenované × nevyjmenované - příloha 2), povolení provozu (§ 11), emisní limity a stropy, provozní řád, měření, poplatky, nízkoemisní zóny, kotle (třídy), přestupky (§ 25) |
| Zákon o odpadech + obaly + VUŽ | 541/2020 / 477/2001 / 542/2020 Sb. | `cz_law/541/2020`, `cz_law/477/2001`, `cz_law/542/2020` | Pojem odpad × vedlejší produkt × neodpad (§ 4-§ 10), původce a jeho povinnosti (§ 15), obchodník, zařízení a povolení KÚ (§ 21), skládkování a poplatek (§ 36+, zákaz skládkování využitelných odpadů 2030), evidence a ISPOP, přeshraniční přeprava (nařízení 1013/2006), přestupky (§ 117+ - pokuty až desítky mil.), obaly - EKO-KOM, VUŽ - baterie, elektro, pneumatiky, vozidla |
| Zákon o ochraně přírody a krajiny | 114/1992 Sb. | `cz_law/114/1992` | Obecná ochrana (VKP § 4, dřeviny - kácení § 8-§ 9, krajinný ráz § 12, ÚSES), zvláštní ochrana (ZCHÚ § 14+, Natura 2000 § 45a+ - hodnocení vlivu § 45i), zvláště chráněné druhy (§ 48+, výjimky § 56), **účast spolků (§ 70 - žádost o informování, přihlášení do 8 dnů)**, náhrada újmy (§ 58), ČIŽP, orgány (OOP, KÚ, AOPK, správy NP), přestupky (§ 87-§ 88) |
| Lesní zákon | 289/1995 Sb. | `cz_law/289/1995` | Pozemky určené k plnění funkcí lesa, odnětí a omezení (§ 15-§ 18, poplatek), ochranné pásmo 50 m (§ 14 odst. 2 - souhlas), hospodaření, LHP, škody |
| Zákon o ochraně ZPF | 334/1992 Sb. | `cz_law/334/1992` | Vynětí ze ZPF (§ 9 - souhlas, odvody § 11-§ 11b dle tříd ochrany), výjimky (fotovoltaika - LEX OZE), skrývka ornice, rekultivace |
| Zákon o ochraně veřejného zdraví + NV o hluku | 258/2000 Sb. + NV 272/2011 Sb. | `cz_law/258/2000`, `cz_law/272/2011` | Hlukové limity (chráněný venkovní prostor, staré hlukové zátěže), povinnosti provozovatele zdroje hluku (§ 30), KHS - měření, časově omezené povolení (§ 31), stavby v hluku, vibrace |
| Zákon o předcházení ekologické újmě | 167/2008 Sb. | `cz_law/167/2008` | Provozní činnosti (příloha 1 - objektivní odpovědnost), preventivní a nápravná opatření, finanční zajištění, náklady; vztah k § 42 vodního zákona a starým zátěžím (sanace - metodika MŽP, ekologické smlouvy MF) |
| Zákon o ČIŽP + kontrolní řád | 282/1991 / 255/2012 Sb. | `cz_law/282/1991`, `cz_law/255/2012` | Působnost inspekce, kontrola, protokol, námitky (15 dnů), přestupkové řízení (250/2016 Sb.) |
| Stavební zákon | 283/2021 Sb. | `cz_law/283/2021` | Povolení záměru s integrovanými stanovisky, územní plánování, DTM; přechodná ustanovení × starý 183/2006 Sb. |
| EU: směrnice EIA 2011/92, IED 2010/75, rámcová o vodě 2000/60, o stanovištích 92/43, o ptácích 2009/147, rámcová o odpadech 2008/98, nařízení ETS, CSRD 2022/2464, taxonomie 2020/852 | Úř. věst. | zdroj `EU` | Eurokonformní výklad, přímý účinek, Natura 2000, emisní obchodování, ESG reporting |
| Aarhuská úmluva | sdělení 124/2004 Sb. m. s. | `cz_law/124/2004` | Přístup k informacím, účast veřejnosti, přístup k právní ochraně (čl. 9) |
| Zákon o právu na informace o ŽP | 123/1998 Sb. | `cz_law/123/1998` | Speciální infozákon pro environmentální informace (lhůta 30 dnů), CENIA |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu rozhodnutí / skutku** → `/toc` → `/text?part=`; u povolování zkontrolovat přechodná ustanovení nového stavebního zákona a JES.
2. Judikatura: **NSS** - klíčové (účastenství spolků § 70 ZOPK a § 9c EIA - rozsah námitek, lhůty; přezkum závazných stanovisek § 149 SŘ v odvolání a v žalobě; pokuty ČIŽP - vymezení skutku, přiměřenost, liberace; pojem odpad; kácení; Natura; hluk - staré zátěže; vynětí ze ZPF; opatření obecné povahy - územní plány a § 101a s. ř. s.), **ÚS** (účast veřejnosti, vlastnické právo × ochrana přírody, náhrada za omezení), **SDEU** (`ES`) - pojem odpad (autonomní, široký), Natura (odchylky, kumulace), EIA (přímý účinek, náprava vad), Aarhus (přístup k soudu spolků - C-240/09, C-664/15, C-873/19), IED. Ověř datum a znění.
3. Komentář (`COMMENT`) ke složkovým zákonům; **metodické pokyny MŽP** (odpad × vedlejší produkt, EIA, kácení, ekologická újma), BREF dokumenty, stanoviska KHS - mimo CODEXIS oficiální zdroje s praktickou váhou.

## Workflow

1. **Kvalifikace.** Role klienta: investor/provozovatel × vlastník pozemku × obec × spolek/dotčená veřejnost × soused; složka (voda, ovzduší, odpady, příroda, les, ZPF, hluk, ekologická újma, klima) a fáze (záměr - povolování - provoz - kontrola - sankce - nápravná opatření - soud); příslušný orgán (KÚ, ORP, ČIŽP, KHS, AOPK, správa NP, MŽP, vodoprávní úřad, stavební úřad); datum a přechodná ustanovení.
2. **Povolování záměru.** (a) Screening: je záměr v příloze 1 EIA (kategorie I - vždy; II - zjišťovací řízení; podlimitní - oznámení podlimitního záměru § 6 odst. 5)? Kumulace se souvisejícími záměry, salámová metoda (judikatura); (b) **zjišťovací řízení** (§ 7 - závěr do 45 dnů, veřejnost může podat vyjádření do 30 dnů; závěr „nepodléhá" je rozhodnutí napadnutelné dotčenou veřejností - ověř); (c) dokumentace, posudek, veřejné projednání, **závazné stanovisko EIA** (§ 9a - podmínky přecházejí do navazujících řízení, platnost 7 let, coherence stamp § 9a odst. 6 při změně záměru); (d) **navazující řízení** (povolení záměru dle SZ, vodoprávní, IPPC) - dotčená veřejnost jako účastník (§ 9c - spolek s 3 lety existence nebo 200 podpisů - ověř), námitky, přezkum závazných stanovisek (§ 149 odst. 7 SŘ - v odvolání nadřízeným orgánem), **JES** (148/2023 Sb. - jedno stanovisko za složkové zákony, výjimky pro EIA, IPPC, Natura), Natura hodnocení (§ 45i ZOPK - vyloučení vlivu / naturové posouzení, kompenzace), výjimky ze ZCHD (§ 56 - důvody, převažující veřejný zájem, alternativy), kácení (§ 8 - povolení OOP, obvod nad 80 cm, náhradní výsadba; oznámení; havarijní), vynětí ze ZPF (souhlas, odvody, třídy ochrany I-II jen ve veřejném zájmu), odnětí lesa a ochranné pásmo 50 m, vodoprávní povolení (nakládání s vodami - odběr, vypouštění; stavební povolení vodního díla), hluková studie a stanovisko KHS, ovzduší (povolení provozu vyjmenovaného zdroje § 11 odst. 2 písm. d), rozptylová studie, odborný posudek), územní plán (soulad; změna ÚP; § 101a s. ř. s. návrh na zrušení OOP - lhůta 1 rok - ověř), IPPC (integrované povolení nahrazuje složková; BAT; změna podstatná × nepodstatná).
3. **Provoz a compliance.** Odpady: **kvalifikace odpad × vedlejší produkt × neodpad** (§ 4-§ 10 zák. 541/2020 - kritéria, judikatura SDEU: široký pojem, úmysl se zbavit), povinnosti původce (třídění, evidence, ISPOP hlášení do 28. 2., předání jen oprávněné osobě - kontrola povolení!, identifikační listy NO, smlouvy s odpadovou firmou), zařízení k nakládání (povolení KÚ § 21, provozní řád, finanční rezerva u skládek), stavební a demoliční odpady (dokumentace, recykláty), obaly (EKO-KOM, evidence, zpětný odběr), VUŽ (kolektivní systémy); voda: podmínky povolení (množství, limity vypouštění, měření, hlášení), havarijní plán (§ 39), poplatky, kontrola vodoprávního úřadu; ovzduší: provozní řád, měření emisí, poplatky, hlášení ISPOP, nízkoemisní zóny, kotle; hluk: limity dle NV 272/2011 (den/noc, korekce), měření akreditovanou laboratoří, časově omezené povolení (§ 31 odst. 1 zák. 258/2000), protihluková opatření; ETS (emisní povolenky - vyřazení, sankce), F-plyny, chemické látky (REACH, CLP - ověř gestora), ESG/CSRD reporting (velké podniky - data ověř), taxonomie.
4. **Kontrola a sankce.** Kontrola ČIŽP/KÚ/KHS podle kontrolního řádu (oznámení nebo bez, protokol, **námitky do 15 dnů**), přestupkové řízení (zákon 250/2016 Sb. - vymezení skutku, promlčení 1/3 roky - ověř § 30, liberace - vynaložení veškerého úsilí § 21, přitěžující/polehčující, výše pokuty do zákonného rozpětí a přiměřenost - **NSS: povinnost odůvodnit výši a majetkové poměry**), souběh složkových přestupků (absorpce), **nápravná opatření** (§ 42 vodního zákona - odstranění závadného stavu, i vlastník pozemku bez zavinění; § 125 odpadového zákona; ekologická újma - preventivní a nápravná opatření, náklady), zákaz činnosti, odnětí povolení, zveřejnění; obrana: odvolání 15 dnů → správní žaloba 2 měsíce (s. ř. s. - odkladný účinek na návrh), moderace pokuty soudem (§ 78 odst. 2 s. ř. s. - zjevná nepřiměřenost); trestní rovina (§ 293-§ 301 TZ - poškození a ohrožení ŽP, neoprávněné nakládání s odpady § 298, s chráněnými organismy § 299-§ 300; TOPO).
5. **Ekologická újma a staré zátěže.** Zákon 167/2008 Sb.: provozní činnosti přílohy 1 - objektivní odpovědnost za újmu na chráněných druzích/stanovištích, vodě, půdě; ostatní jen při zavinění; **preventivní a nápravná opatření** (rozhodnutí ČIŽP), úhrada nákladů, finanční zajištění (hodnocení rizik), promlčení 30 let, vztah k náhradě škody (OZ § 2894+, § 2925 provoz zvlášť nebezpečný, § 2926 stavba, sousedské imise § 1013), **staré ekologické zátěže** (před 2007): odpovědnost dle § 42 vodního zákona (původce / nabyvatel - kdo závadný stav způsobil; vlastník pozemku jen subsidiárně - ověř), ekologické smlouvy MF s privatizovanými podniky, SEKM databáze, kupní smlouvy - prohlášení, indemnita, escrow na sanaci, environmental due diligence (fáze I/II), rekultivace a sanace (metodika MŽP, limity - MP MŽP), brownfieldy; havárie (§ 40-§ 41 vodního zákona - ohlášení HZS/ČIŽP ihned, likvidace).
6. **Sousedské a soukromoprávní spory.** Imise (§ 1013 OZ - hluk, prach, pach, stínění: míra nepřiměřená poměrům; zdroj s úředním povolením - jen náhrada § 1013 odst. 2), zápůrčí žaloba, náhrada škody (kontaminace, zápach, snížení hodnoty), předběžné opatření, hlukové limity jako měřítko, dřeviny a kořeny (§ 1016-§ 1017), voda ze sousedního pozemku (§ 1019), zvířata a včely, provoz závodu (§ 2924), kolektivní/hromadné žaloby.
7. **Veřejnost, spolky, informace.** Nástroje: **§ 70 ZOPK** (spolek s hlavním posláním ochrana přírody - žádost o informace o zahajovaných řízeních u orgánu předem; přihlášení do 8 dnů od informace - účastník řízení, kde mohou být dotčeny zájmy ochrany přírody; rozsah námitek omezen na tyto zájmy - judikatura NSS), **§ 9c EIA** (dotčená veřejnost v navazujících řízeních - podmínky 3 roky / 200 podpisů - ověř; **žaloba § 9d** proti rozhodnutí v navazujícím řízení i bez účasti), § 115 vodního zákona (spolky ve vodoprávních řízeních - ověř), územní plán (připomínky a námitky zástupce veřejnosti § 23 SZ, návrh na zrušení OOP), petice a místní referendum (viz skill obcí), právo na informace o ŽP (123/1998 Sb. - 30 dnů, aktivní zveřejňování), Aarhus čl. 9 odst. 3 - přístup k soudu i mimo EIA (judikatura SDEU a NSS), kárná/trestní oznámení, mediální strategie; pro investora: jak s veřejností jednat, aby řízení nespadlo (včasné informace, vypořádání námitek).
8. **Transakce a smlouvy.** Environmental due diligence (povolení a jejich převoditelnost - přechod na nabyvatele zařízení ex lege × nutnost změny; zátěže; odpady; ETS; sankce běžící), kupní smlouvy (prohlášení a záruky, indemnity, cap, zádržné), pachty a nájmy (kdo je původce odpadu - ověř § 15 zák. 541/2020 - nájemce/provozovatel), smlouvy s odpadovými firmami (odpovědnost za nezákonné nakládání přechází? ne bez ověření oprávnění), věcná břemena pro vodní díla a přírodní prvky, kompenzace za omezení hospodaření (§ 58 ZOPK, lesní zákon - náhrada újmy vlastníkům).

## Časté pasti

- Spolek se přihlásí po lhůtě 8 dnů nebo bez předchozí žádosti o informace - není účastníkem; nebo namítá nad rámec zájmů ochrany přírody - námitky nepřípustné.
- Závazné stanovisko EIA/JES nenapadeno v odvolání proti povolení - v žalobě už jen omezeně; naopak stanovisko není samostatně žalovatelné.
- Salámování záměru (rozdělení pod limity EIA) - NSS ruší; nebo změna záměru po EIA bez ověření § 9a odst. 6.
- Odpad předán firmě bez ověření povolení v registru zařízení - původce odpovídá dál (pokuta i za černou skládku jinde).
- Vedlejší produkt / recyklát nakládaný jako neodpad bez splnění kritérií - přestupek za nakládání s odpady bez povolení.
- Kácení „na vlastním" bez povolení nad obvod 80 cm / v památkové zóně / mimo vegetační klid - pokuta až 1 mil. Kč (FO 100 tis.) - ověř.
- Studna nebo odběr vody bez povolení (i historická před 1955 × po) - přestupek; vypouštění přečištěné vody do vod bez povolení.
- Hlukové měření zadané neakreditované laboratoři - nepoužitelné; obrana proti KHS bez vlastního měření.
- Nápravné opatření dle § 42 vodního zákona uloženo vlastníkovi pozemku - bránit se nedostatkem příčinné souvislosti/původce, ale ne nečinností.
- Koupě brownfieldu bez fáze II průzkumu a bez indemnity - kupující nese sanaci a nemůže se zhojit.
- Pokuta ČIŽP napadena jen „je vysoká" bez argumentace ke skutku, promlčení, liberaci, souběhu a poměrům - odvolání neúspěšné.
- Odvolání proti pokutě zapomenuto v 15denní lhůtě; žaloba bez návrhu na odkladný účinek - pokuta vykonatelná.
- Doplňování limitů, sazeb pokut, lhůt a čísel příloh z paměti - vždy z aktuálního znění nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co podat/nepodávat, ke kterému orgánu, do kdy).
2. **Kvalifikace** - složka, fáze, role, příslušný orgán, použitelné znění a přechodný režim.
3. **Právní rámec** - složkové zákony / EIA / SZ / EU v aktuálním znění, s odkazy.
4. **Postup a nároky** - tabulka: krok | právní základ | orgán | lhůta | riziko/sankce.
5. **Strategie** (investor: jak projít; veřejnost: kde a jak vstoupit; obviněný: obrana proti pokutě a nápravným opatřením).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. NSS a SDEU.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 As 123/2024 - …`, `SDEU - C-240/09 - 08.03.2011`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do 8 dnů ode dne, kdy mu bylo oznámeno zahájení řízení“, „mohou být dotčeny zájmy ochrany přírody“, „vynaložil veškeré úsilí, které bylo možno požadovat“, „převažující veřejný zájem“).
- Jeden časový řez; znění zákona účinné k datu skutku / vydání rozhodnutí; přechodná ustanovení SZ a JES vždy zmínit.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity, sazby pokut, lhůty, obsah příloh (EIA, IPPC, ekologická újma) nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o povoleních, zařízeních a zátěžích výhradně z registrů (ISPOP, registr zařízení odpadů, SEKM, CENIA, EIA informační systém); mimo CODEXIS jen oficiální zdroje (mzp.gov.cz, cizp.cz, portal.cenia.cz, khs) když CODEXIS neodpovídá.
