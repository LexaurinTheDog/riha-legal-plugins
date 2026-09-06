---
uuid: 68b2a19b-42d1-4372-9078-585514ff420f
name: skolske-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Školské právo ČR"
    summary: "Přijímání do škol a odvolání, spádovost, speciální vzdělávací potřeby a podpůrná opatření, kázeňská opatření a vyloučení, šikana a bezpečnost, pracovní vztahy pedagogů, škola jako právnická osoba a zřizovatel, ČŠI, úplata a školné, vysoké školy a studenti."
    examplePrompts:
      - "Dítě nebylo přijato do spádové základní školy pro naplněnou kapacitu. Jak podat odvolání a jaké jsou šance?"
      - "Ředitel střední školy chce vyloučit žáka za opakované porušení školního řádu. Jaký je postup, lhůty a jak se žák může bránit?"
      - "Učitelka bez plné kvalifikace má smlouvu na dobu určitou potřetí za sebou. Je to v souladu se zákonem o pedagogických pracovnících a zákoníkem práce?"
  en:
    displayName: "Czech Education Law"
    summary: "School admissions and appeals, catchment areas, special educational needs and support measures, discipline and expulsion, bullying and safety, teachers' employment, school as a legal entity and its founder, school inspection, tuition and fees, universities and students."
    examplePrompts:
      - "A child was not admitted to the catchment primary school due to full capacity. How to appeal and what are the chances?"
      - "A secondary school principal wants to expel a pupil for repeated breaches of school rules. What is the procedure, the deadlines, and how can the pupil defend?"
      - "A teacher without full qualification has a third consecutive fixed-term contract. Is this compliant with the pedagogical staff act and the Labour Code?"
  sk:
    displayName: "Školské právo ČR"
    summary: "Prijímanie do škôl a odvolania, spádovosť, špeciálne výchovno-vzdelávacie potreby a podporné opatrenia, disciplinárne opatrenia a vylúčenie, šikana a bezpečnosť, pracovné vzťahy pedagógov, škola ako právnická osoba a zriaďovateľ, ČŠI, úplata a školné, vysoké školy a študenti."
    examplePrompts:
      - "Dieťa nebolo prijaté do spádovej základnej školy pre naplnenú kapacitu. Ako podať odvolanie a aké sú šance?"
      - "Riaditeľ strednej školy chce vylúčiť žiaka za opakované porušenie školského poriadku. Aký je postup, lehoty a ako sa žiak môže brániť?"
      - "Učiteľka bez plnej kvalifikácie má zmluvu na dobu určitú tretíkrát za sebou. Je to v súlade so zákonom o pedagogických zamestnancoch a zákonníkom práce?"
description: Use when the user's matter involves schools, pupils, teachers or universities in the Czech Republic - školské právo, školský zákon (561/2004 Sb.), přijímací řízení, nepřijetí, odvolání proti nepřijetí, spádová škola, odklad školní docházky, povinná školní docházka, individuální vzdělávání, speciální vzdělávací potřeby, podpůrná opatření, školní řád, kázeňská opatření, podmínečné vyloučení, vyloučení ze školy, maturita, přezkoumání maturity, šikana, bezpečnost a ochrana zdraví žáků, odpovědnost školy za škodu, zákon o pedagogických pracovnících (563/2004 Sb.), ředitel školy, odvolání ředitele, zřizovatel školy, Česká školní inspekce, ČŠI, úplata za vzdělávání, školné soukromé školy, zákon o vysokých školách (111/1998 Sb.), student, disciplinární řízení VŠ, poplatky za studium. Standalone skill - bundles CODEXIS methodology with education-practice method; no need to load the general codexis skill.
---

# Školské právo ČR

Samostatný oborový skill pro vzdělávací vztahy. Základní reflex: **škola rozhoduje ve správním řízení jen tam, kde to školský zákon výslovně říká** (§ 165 odst. 2 - přijetí, odklad, vyloučení, uznání vzdělání, přezkoumání apod.) - tam platí správní řád, odvolání ke krajskému úřadu a soudní přezkum; všude jinde jde o faktický postup školy, proti němuž se brání stížností řediteli, zřizovateli a ČŠI. Druhý reflex: **lhůty u přijímacího řízení jsou krátké** (odvolání 15 dnů od doručení, zápisový lístek 10 pracovních dnů - ověř); jejich zmeškání nelze zhojit. Třetí: v oblasti dětí vždy rozlišit, kdo jedná - zákonný zástupce × zletilý žák × student.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/561/2004/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf165'`, `cdx-cli get cdx://cz_law/563/2004/versions`, `cdx-cli get cdx://cz_law/111/1998/versions`, `cdx-cli search JD --query "nepřijetí do základní školy spádová kapacita odvolání" --court "Nejvyšší správní soud" --limit 5`, `cdx-cli search JD --query "vyloučení žáka ze střední školy správní řízení" --court "Nejvyšší správní soud" --limit 5`.
- Školský zákon i zákon o pedagogických pracovnících jsou často novelizovány (přijímací řízení na SŠ - jednotný systém DiPSy od 2024, kvalifikace, financování, digitalizace); **lhůty, termíny, kapacitní kritéria, výši úplaty a čísla vyhlášek ověř v aktuálním znění k datu**; nikdy z paměti. Prováděcí vyhlášky (o základním vzdělávání, o SŠ, o přijímacím řízení, o vzdělávání žáků se SVP) hledej ve zdroji `CR`.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Školský zákon | 561/2004 Sb. | `cz_law/561/2004` | Zásady a práva (§ 2, § 21-§ 22), SVP a podpůrná opatření (§ 16-§ 16b), nadaní (§ 17), individuální vzdělávání (§ 41), povinná docházka a spádovost (§ 36-§ 38, odklad § 37), přijímání ZŠ (§ 46), SŠ (§ 59-§ 62), MŠ (§ 34), hodnocení (§ 51-§ 53, § 69), školní řád (§ 30), kázeňská opatření a vyloučení (§ 31), maturita (§ 77-§ 82: přezkoumání § 82), ředitel (§ 164-§ 166: konkurz, odvolání § 166), rozhodování ve správním řízení (§ 165 odst. 2, § 183), školská rada (§ 167-§ 168), zřizovatelé a rejstřík (§ 141-§ 150), ČŠI (§ 173-§ 176), úplata (§ 123), bezpečnost (§ 29), přestupky (§ 182a) |
| Zákon o pedagogických pracovnících | 563/2004 Sb. | `cz_law/563/2004` | Předpoklady výkonu (§ 3), odborná kvalifikace (§ 6-§ 22), výjimky a uznání (§ 22, § 32), pracovní doba a přímá pedagogická činnost (§ 22a-§ 23, NV 75/2005 Sb.), doba určitá u pedagogů (§ 23a - nejméně 12 měsíců, max. 3x - ověř), další vzdělávání, kariérní systém |
| Zákoník práce | 262/2006 Sb. | `cz_law/262/2006` | Pracovní poměr pedagogů a ostatních zaměstnanců, výpověď, platové tarify (NV 341/2017 Sb.), dovolená pedagogů 8 týdnů, FKSP, přechod práv |
| Zákon o vysokých školách | 111/1998 Sb. | `cz_law/111/1998` | Přijímání (§ 48-§ 50: přezkum rozhodnutí rektorem), studium a jeho ukončení (§ 54-§ 56: přerušení, nesplnění požadavků), poplatky (§ 58 - za delší studium, odvolání), disciplinární řízení (§ 64-§ 69), rozhodování o právech studentů (§ 68 - správní řád vyloučen? ověř, soudní přezkum), akademické tituly, vnitřní předpisy, akreditace (NAÚ), zahraniční VŠ |
| Správní řád | 500/2004 Sb. | `cz_law/500/2004` | Řízení před ředitelem (§ 165 odst. 2 ŠZ), odvolání ke KÚ (15 dnů), autoremedura, přezkum, nečinnost |
| Soudní řád správní | 150/2002 Sb. | `cz_law/150/2002` | Žaloba proti rozhodnutí KÚ / rektora (2 měsíce), zásahová žaloba (faktický postup školy), nezákonný zásah |
| Občanský zákoník | 89/2012 Sb. | `cz_law/89/2012` | Rodičovská odpovědnost a zastupování (§ 858+, § 876-§ 877 - neshoda rodičů, § 892), svéprávnost nezletilého (§ 31+), odpovědnost za újmu (§ 2910+, § 2920-§ 2921 nezletilý a dohled), škola jako zařízení s dohledem, smluvní vztahy soukromých škol (§ 1810+ spotřebitel) |
| Zákon o sociálně-právní ochraně dětí | 359/1999 Sb. | `cz_law/359/1999` | Oznamovací povinnost školy (§ 10 odst. 4), spolupráce s OSPOD, zanedbávání docházky |
| Zákon o ochraně veřejného zdraví + vyhláška o hygienických požadavcích | 258/2000 Sb. + 410/2005 Sb. | `cz_law/258/2000`, `cz_law/410/2005` | Očkování jako podmínka MŠ (§ 50), hygiena, školní stravování (vyhláška 107/2005 Sb.) |
| Prováděcí vyhlášky MŠMT | 48/2005 (ZŠ), 13/2005 (SŠ), 422/2023 (přijímací řízení SŠ - ověř), 27/2016 (SVP), 14/2005 (MŠ), 74/2005 (zájmové), 72/2005 (poradenství), 16/2005 (organizace roku) | `cz_law/48/2005` atd. | Podrobnosti hodnocení, přijímání, podpůrných opatření, poradenských zařízení |
| Zákon o svobodném přístupu k informacím / GDPR | 106/1999 Sb. / (EU) 2016/679 | `cz_law/106/1999`, zdroj `EU` | Škola jako povinný subjekt, osobní údaje žáků, fotografie, kamery, souhlasy |
| Trestní zákoník / přestupkový zákon | 40/2009 / 250/2016 Sb. | `cz_law/40/2009`, `cz_law/250/2016` | Ohrožování výchovy dítěte (§ 201), šikana jako TČ (§ 353-§ 354, § 146), přestupek zákonného zástupce (§ 182a ŠZ - záškoláctví) |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu rozhodnutí / školního roku** → `/toc` → `/text?part=`; přijímací řízení podle znění účinného pro daný školní rok.
2. Judikatura: **NSS** - klíčové (nepřijetí do spádové ZŠ/MŠ a kritéria při naplnění kapacity, losování, přednost spádových; vyloučení žáka; odklad; maturita - přezkoumání; individuální vzdělávání; povinné očkování v MŠ; zásahová žaloba proti postupu školy; VŠ - poplatky za delší studium, ukončení studia, disciplinární), **ÚS** (očkování - Pl. ÚS 19/14, inkluze, právo na vzdělání čl. 33 Listiny, náboženské symboly, domácí vzdělávání), **NS** (odpovědnost školy za úraz žáka - dohled, šikana a náhrada nemajetkové újmy; pracovní spory pedagogů - kvalifikace, doba určitá; odvolání ředitele), **ESLP** (segregace romských dětí D. H. proti ČR). Ověř datum a znění.
3. Komentář (`COMMENT`) ke školskému zákonu; **metodické pokyny a výklady MŠMT** (šikana, přijímací řízení, podpůrná opatření, doba určitá pedagogů), stanoviska ČŠI a ombudsmana (spádovost, inkluze) - mimo CODEXIS oficiální zdroje s praktickou váhou.

## Workflow

1. **Kvalifikace.** Kdo je klient (zákonný zástupce, zletilý žák, student, škola/ředitel, zřizovatel - obec/kraj/soukromý/církevní, pedagog), druh školy (MŠ, ZŠ, SŠ, konzervatoř, VOŠ, VŠ; veřejná × soukromá × církevní), o co jde: **rozhodnutí ředitele ve správním řízení** (§ 165 odst. 2 - výčet: přijetí/nepřijetí, odklad, přestup, přerušení, opakování ročníku, podmínečné vyloučení a vyloučení, uznání vzdělání, změna oboru, individuální vzdělávání, snížení úplaty) × **faktický postup** (hodnocení, kázeňská opatření pod vyloučením, školní řád, dohled, přístup rodiče k informacím) × pracovněprávní × smluvní (soukromá škola). Datum a lhůty.
2. **Přijímání a spádovost.** MŠ: povinné předškolní pro 5leté (§ 34 odst. 1, spádovost), kritéria při převisu (spádové děti, věk, sourozenci - kritéria musí být předem zveřejněná, transparentní, nediskriminační; losování přípustné až po objektivních kritériích - judikatura NSS), očkování (§ 50 zák. 258/2000 - výjimky), zápis květen. ZŠ: **spádová škola musí přijmout spádové dítě do naplnění kapacity** (§ 36 odst. 7), přednost spádových; nespádoví podle kritérií; zápis duben, odklad (§ 37 - žádost do 30. 4., doporučení PPP + lékař), přípravné třídy; přestup (§ 49). SŠ: jednotná přijímací zkouška (Cermat), **DiPSy** - až 3 přihlášky s prioritizací, výsledky, odvolání (od 2024 nový systém - lhůty a kroky ověř ve vyhlášce), zápisový lístek zrušen? - ověř; kritéria ředitele, talentové zkoušky; nezletilý žák - podává zákonný zástupce; cizinci (jazykové úlevy). **Odvolání proti nepřijetí**: do 15 dnů od doručení rozhodnutí řediteli, rozhoduje KÚ (u soukromých a církevních - ověř § 183 odst. 3, autoremedura ředitelem při uvolnění místa - § 183 - přijetí na uvolněná místa), důvody: chybná kritéria, nesprávný výpočet, diskriminace, kapacita neprokázána; žaloba k soudu (2 měsíce; předběžné opatření na zatímní zařazení). Individuální vzdělávání (§ 41 - povolení, podmínky, přezkoušení, zrušení), vzdělávání v zahraničí (§ 38).
3. **Speciální vzdělávací potřeby a podpora.** Podpůrná opatření 1.-5. stupně (§ 16, vyhláška 27/2016 Sb.): 1. stupeň škola sama (plán pedagogické podpory), 2.-5. na základě **doporučení ŠPZ** (PPP/SPC - vyšetření se souhlasem zákonného zástupce, doporučení do 3 měsíců - ověř, platnost, revize; nesouhlas s doporučením → revizní pracoviště NPI), škola má povinnost opatření poskytnout (IVP, asistent pedagoga, úpravy obsahu, pomůcky, tlumočník), financování normativní; obrana při neposkytnutí: stížnost řediteli/ČŠI/zřizovateli, zásahová žaloba, antidiskriminační žaloba (přístup ke vzdělání - § 1 odst. 1 písm. i) ADZ, sdílené důkazní břemeno); žáci nadaní (§ 17), žáci s odlišným mateřským jazykem, ukrajinští žáci (lex Ukrajina - ověř platnost), domácí výuka ze zdravotních důvodů, přípravný stupeň ZŠ speciální, vzdělávání ve třídě zřízené dle § 16 odst. 9 (souhlas rodiče), přezkoumání „diagnózy", speciální školy.
4. **Kázeň, hodnocení, vyloučení.** Školní řád (§ 30 - povinný obsah, schválení školskou radou, seznámení; nesmí ukládat povinnosti nad zákon - mobily, oblečení, náboženské symboly - judikatura), výchovná opatření (napomenutí, důtka - vyhláška 48/2005, nejsou rozhodnutím), **podmínečné vyloučení a vyloučení (§ 31 odst. 2-4)**: jen u žáka, který splnil povinnou docházku (ne ZŠ), za závažné zaviněné porušení povinností, zvláště hrubé slovní/fyzické útoky = vždy zvláště závažné porušení (§ 31 odst. 3 - oznámení OSPOD/státnímu zástupci), **rozhodnutí do 2 měsíců od zjištění, nejpozději do 1 roku** (ověř), správní řízení (zahájení, možnost vyjádřit se, dokazování, projednání v pedagogické radě není rozhodnutí), odvolání ke KÚ 15 dnů, odkladný účinek; hodnocení (§ 51-§ 53, § 69 - pochybnosti → **žádost o komisionální přezkoušení do 3 pracovních dnů od vydání vysvědčení** - ověř; opravné zkoušky; opakování ročníku), maturita (§ 82 - žádost o přezkoumání do 20 dnů - ověř; KÚ / MŠMT u didaktických testů; soudní přezkum), zletilý žák × informace rodičům (§ 21 odst. 3 - rodiče zletilého žáka mají právo na informace, pokud plní vyživovací povinnost - ověř), absence a omlouvání (školní řád; neomluvené hodiny → OSPOD, přestupek § 182a, TČ § 201).
5. **Šikana, bezpečnost, odpovědnost.** Škola: povinnost zajišťovat bezpečnost a ochranu zdraví (§ 29), prevence (metodický pokyn MŠMT k šikaně, minimální preventivní program, školní metodik prevence), **dohled** (vyhláška 48/2005 - před vyučováním, přestávky, akce; pedagog zodpovídá; poměr na akcích), úrazy (evidence, záznam do 24 h - ověř, hlášení ČŠI/zřizovateli/pojišťovně), **odpovědnost za újmu** (NS: škola odpovídá za porušení dohledu - § 2910/§ 2921 OZ; objektivní prvky u zařízení; pojištění odpovědnosti školy; regres vůči učiteli podle ZP § 250 - max. 4,5násobek), šikana - postup (vyšetření, oddělení, výchovná opatření, informování rodičů obou stran, OSPOD, policie u TČ - § 353, § 354, § 146, § 185 - i kyberšikana), nároky oběti (nemajetková újma § 2956+ OZ vůči škole i rodičům agresora § 2920-§ 2921), přeřazení agresora × oběti, stížnost ČŠI, zásahová žaloba při nečinnosti, GDPR (kamery, fotografie na webu - souhlas, oprávněný zájem; záznamy o žácích, matrika), náboženská svoboda a symboly, mobilní telefony (zákaz v ŠŘ - ověř novelu), zdravotní péče ve škole (podávání léků, diabetes - metodika), alergie a stravování.
6. **Pedagogové a ředitel.** Předpoklady (§ 3 ZPP - způsobilost, bezúhonnost, zdravotní, znalost ČJ), **kvalifikace** (§ 6-§ 22; nekvalifikovaný - výjimky § 22 odst. 7 - ověř: pracovní smlouva jen na dobu určitou? doplnění do 3 let), **doba určitá u pedagogů** (§ 23a ZPP - nejméně 12 měsíců, nejvýše 3× po sobě - ověř, výjimky zástup, nekvalifikovaný; při porušení → doba neurčitá při oznámení podle § 39 odst. 5 ZP - lhůta 2 měsíce), přímá pedagogická činnost (NV 75/2005), plat (NV 341/2017, platové třídy, příplatky za třídnictví/specializaci), dovolená 8 týdnů, další vzdělávání (12 dnů volna), pracovní úrazy, výpověď (organizační změny, nekvalifikovanost § 52 písm. f) ZP - jen pokud nelze převést), **ředitel**: jmenování zřizovatelem po konkurzu (§ 166 ŠZ, vyhláška 54/2005 Sb. - konkurzní komise, doporučení nezávazné - ověř judikaturu), funkční období 6 let, **odvolání** (§ 166 odst. 4 a 5 - důvody: pozbytí předpokladů, nesplnění povinností, závažné porušení; nebo po 6 letech s konkurzem; přezkum soudem - pracovněprávní spor, ne správní), ředitel jako statutární orgán a orgán státní správy ve školství, střet zájmů, kontrola zřizovatele × autonomie školy (§ 164).
7. **Škola, zřizovatel, ČŠI, financování.** Právní formy (příspěvková organizace obce/kraje, školská právnická osoba § 124+, s.r.o./o.p.s. soukromé, církevní), rejstřík škol a školských zařízení (§ 141+ - zápis, změny kapacity, výmaz; rozhoduje KÚ/MŠMT), zřizovací listina, financování (§ 160+ - PHmax, normativy, soukromé školy dotace § 162 - podmínky, církevní), **úplata** (§ 123 - MŠ, družina, ZUŠ, VOŠ; osvobození; od 2024 stanoví zřizovatel - ověř), školné soukromých škol (smlouva o vzdělávání - spotřebitelské právo, změny, výpověď, vrácení), stravování (vyhláška 107/2005), školská rada (§ 167-§ 168 - volby, pravomoci, schvalování ŠŘ), **ČŠI** (§ 173-§ 176 - inspekční činnost, protokol, stížnosti - vyřízení a zaslání zřizovateli, opatření, návrh na výmaz), obec: zajištění podmínek docházky (§ 178 - spádové obvody vyhláškou, kapacita, výjimky, dohody obcí, doprava), spory obcí o spádovost, kraj (§ 181), ministerstvo.
8. **Vysoké školy.** Přijímací řízení (§ 48-§ 50 ZVŠ - podmínky zveřejněny předem, **přezkum rozhodnutí o nepřijetí rektorem do 30 dnů** - ověř, žaloba k soudu), studium (studijní a zkušební řád, uznávání předmětů, přerušení, **ukončení pro nesplnění požadavků § 56 odst. 1 písm. b)** - rozhodnutí, přezkum rektorem/žaloba), **poplatky za delší studium** (§ 58 odst. 3 - výpočet doby, odvolání, snížení/prominutí, promlčení, exekuce), stipendia, disciplinární řízení (§ 64-§ 69 - komise, sankce až vyloučení, plagiátorství, odvolání k rektorovi, soudní přezkum), statut studenta (zdravotní/sociální pojištění do 26 let, DPP/DPČ), zahraniční studenti (víza - skill cizinecké), uznávání zahraničního vzdělání (nostrifikace § 89-§ 90, MŠMT), akademické tituly a jejich odnětí (§ 47c), habilitace a profesury, akreditace (NAÚ - žádost, odnětí), vnitřní předpisy (registrace MŠMT), akademická samospráva a její soudní přezkum (rozhodování o právech studentů - správní soudnictví; interní spory), VOŠ (§ 92+ ŠZ - absolutorium, školné).

## Časté pasti

- Odvolání proti nepřijetí podáno po 15 dnech nebo ke KÚ místo řediteli - opožděné / zmatečné; naopak nečekat na odvolání a paralelně žádat o přijetí na uvolněná místa.
- Spádová ZŠ „odmítne" spádové dítě bez rozhodnutí - nezákonný zásah; obec musí zajistit místo (§ 178).
- Kritéria přijetí do MŠ/ZŠ oznámena až po zápisu, nebo losování bez objektivních kritérií - NSS ruší.
- Vyloučení žáka základní školy - nepřípustné (povinná docházka); vyloučení bez správního řízení nebo po lhůtě - zrušeno.
- Podpůrná opatření neposkytnuta s odkazem na „nedostatek financí" - povinnost školy; rodič ale nedodal doporučení ŠPZ.
- Doba určitá pedagoga kratší než 12 měsíců nebo počtvrté - vzniká doba neurčitá, ale zaměstnanec musí oznámit do 2 měsíců (§ 39 odst. 5 ZP).
- Odvolání ředitele „bez důvodu" v průběhu 6letého období - neplatné (pracovněprávní žaloba, lhůta 2 měsíce § 72 ZP).
- Stížnost na šikanu vyřízena jen „domluvou" bez záznamu, informování rodičů a OSPOD - odpovědnost školy a ředitele.
- Úraz žáka bez záznamu do lhůty - problém s pojištěním a důkazy; regres vůči učiteli nad 4,5násobek.
- Zákaz mobilů nebo oblečení ve školním řádu bez opory - napadnutelné; naopak ŠŘ neschválený školskou radou.
- Rodič v rozvodovém sporu žádá informace/ vyzvednutí dítěte - oba rodiče mají rovná práva, nestanoví-li soud jinak; škola nesmí rozhodovat spor.
- Poplatek za delší studium napaden po lhůtě - vykonatelný; studium ukončeno bez doručeného rozhodnutí - lze napadnout.
- Doplňování termínů zápisů, lhůt, výše úplaty a čísel vyhlášek z paměti - vždy z aktuálního znění nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co podat, komu - ředitel/KÚ/zřizovatel/ČŠI/rektor/soud, do kdy).
2. **Kvalifikace** - druh školy, role, správní řízení × faktický postup × pracovněprávní × smluvní; znění k datu.
3. **Právní rámec** - školský zákon / ZPP / ZVŠ / vyhlášky / SŘ v aktuálním znění, s odkazy.
4. **Postup a nároky** - tabulka: krok | právní základ | orgán | lhůta | riziko.
5. **Strategie a alternativy** (odvolání × autoremedura × stížnost ČŠI × zásahová žaloba × mediace se školou).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. NSS a ÚS.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 As 123/2024 - …`, `ÚS - Pl. ÚS 19/14 - 27.01.2015`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do naplnění kapacity“, „zvláště závažné zaviněné porušení povinností“, „do 15 dnů ode dne doručení“, „nejméně 12 měsíců“).
- Jeden časový řez; znění zákona a vyhlášek účinné pro daný školní rok / k datu rozhodnutí.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty, termíny, kapacity, výše úplaty a čísla vyhlášek nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o školách a kapacitách výhradně z rejstříku škol (MŠMT) a zřizovacích listin; mimo CODEXIS jen oficiální zdroje (msmt.gov.cz, csicr.cz, cermat.cz, nauvs.cz) když CODEXIS neodpovídá.
- U dětí vždy rozlišit zákonného zástupce a dítě; nikdy neradit postup obcházející rodičovskou odpovědnost druhého rodiče.
