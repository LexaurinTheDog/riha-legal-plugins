---
uuid: 5a185893-07b1-47f4-afdd-4a65fb787ab0
name: aml-compliance
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "AML compliance ČR"
    summary: "Povinné osoby, identifikace a kontrola klienta, skutečný majitel a PEP, sankční screening, oznámení podezřelého obchodu FAÚ, systém vnitřních zásad a školení, zvláštní povinnosti advokáta a mlčenlivost, spouštěče u nemovitostí a úschov, evidence skutečných majitelů, kontroly a sankce, AML balíček EU."
    examplePrompts:
      - "Advokát přebírá do úschovy kupní cenu 12 mil. Kč od zahraniční společnosti s nejasnou strukturou. Jaké AML povinnosti má a kdy může/musí obchod odmítnout?"
      - "Realitní kancelář dostala od FAÚ výzvu k předložení dokumentů. Co musí mít v pořádku a jaké hrozí pokuty?"
      - "Připrav checklist kontroly klienta pro s.r.o. se skutečným majitelem v evidenci a jednatelem PEP."
  en:
    displayName: "Czech AML Compliance"
    summary: "Obliged persons, customer identification and due diligence, beneficial owner and PEP checks, sanctions screening, suspicious transaction reports to FAÚ, internal policies and training, attorney-specific duties and privilege, real-estate and escrow triggers, beneficial owner register, inspections and penalties, EU AML package."
    examplePrompts:
      - "A lawyer is taking CZK 12 million purchase price into escrow from a foreign company with an unclear structure. What AML duties apply and when may or must the transaction be refused?"
      - "A real-estate agency received a request for documents from the FAÚ. What must be in order and what fines apply?"
      - "Prepare a customer due-diligence checklist for an s.r.o. with a registered beneficial owner and a PEP managing director."
  sk:
    displayName: "AML compliance ČR"
    summary: "Povinné osoby, identifikácia a kontrola klienta, konečný užívateľ výhod a PEP, sankčný screening, hlásenie podozrivého obchodu FAÚ, systém vnútorných zásad a školenia, osobitné povinnosti advokáta a mlčanlivosť, spúšťače pri nehnuteľnostiach a úschovách, evidencia skutočných majiteľov, kontroly a sankcie, AML balík EÚ."
    examplePrompts:
      - "Advokát preberá do úschovy kúpnu cenu 12 mil. Kč od zahraničnej spoločnosti s nejasnou štruktúrou. Aké AML povinnosti má a kedy môže/musí obchod odmietnuť?"
      - "Realitná kancelária dostala od FAÚ výzvu na predloženie dokumentov. Čo musí mať v poriadku a aké hrozia pokuty?"
      - "Priprav checklist kontroly klienta pre s.r.o. s konečným užívateľom výhod v evidencii a konateľom PEP."
description: Use when the user's matter involves anti-money-laundering or sanctions duties in the Czech Republic - AML, praní špinavých peněz, financování terorismu, zákon 253/2008 Sb., povinná osoba, advokát jako povinná osoba, realitní kancelář, účetní, daňový poradce, virtuální aktiva, identifikace klienta, kontrola klienta, zesílená kontrola, skutečný majitel, evidence skutečných majitelů (37/2021 Sb.), politicky exponovaná osoba, PEP, sankce, mezinárodní sankce (69/2006 Sb.), sankční seznam EU, screening, hodnocení rizik, systém vnitřních zásad, kontaktní osoba, školení, oznámení podezřelého obchodu, Finanční analytický úřad, FAÚ, mlčenlivost advokáta, Česká advokátní komora, kontrola ČAK, hotovostní limit 270 000 Kč, zákon o omezení plateb v hotovosti, úschova, escrow, nemovitostní transakce, uchovávání záznamů, přestupky a pokuty, AML nařízení EU 2024/1624, AMLA. Standalone skill - bundles CODEXIS methodology with AML-compliance method; no need to load the general codexis skill.
---

# AML compliance ČR

Samostatný oborový skill pro povinnosti proti legalizaci výnosů z trestné činnosti a financování terorismu a pro sankční compliance. Základní reflex: **nejprve zjisti, zda a od kdy je klient (nebo sám advokát) povinnou osobou pro daný obchod** - povinnosti se spouštějí typem činnosti, ne velikostí subjektu; u advokáta a notáře jen pro vyjmenované úkony (úschovy, nemovitosti, správa majetku, zakládání společností). Druhý reflex: **identifikace a kontrola klienta jsou dva různé úkony s různými prahy a hloubkou**; nesplnitelná kontrola znamená povinnost obchod odmítnout, ne „provést s rezervou". Třetí: **sankční povinnosti platí pro každého**, nejen pro povinné osoby.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/253/2008/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf9'`, `cdx-cli get cdx://cz_law/37/2021/versions`, `cdx-cli get cdx://cz_law/69/2006/versions`, `cdx-cli search EU --query "nařízení 2024/1624 předcházení využívání finančního systému" --limit 5`, `cdx-cli search JD --query "povinná osoba identifikace klienta pokuta FAÚ" --court "Nejvyšší správní soud" --limit 5`.
- AML zákon je novelizován téměř každý rok a **AML balíček EU (nařízení 2024/1624 - přímo použitelné od 10. 7. 2027, směrnice 2024/1640, AMLA)** přesouvá pravidla z národního zákona do nařízení; **prahy (hotovost, příležitostný obchod), lhůty, výši pokut a seznam povinných osob ověř v aktuálním znění k datu obchodu**; nikdy z paměti. Sankční seznamy se mění denně - screening vždy k datu úkonu na oficiálních zdrojích.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| AML zákon | 253/2008 Sb. | `cz_law/253/2008` | Povinné osoby (§ 2), výjimky (§ 2 odst. 2, § 27 advokát/notář), identifikace (§ 7-§ 8, zprostředkovaná § 10, převzatá § 11), kontrola klienta (§ 9, zesílená § 9a, zjednodušená § 13), PEP (§ 4 odst. 5, § 9a), neuskutečnění obchodu (§ 15), uchovávání (§ 16), oznámení podezřelého obchodu (§ 18, lhůta; odklad § 20), mlčenlivost (§ 38-§ 40), systém vnitřních zásad a hodnocení rizik (§ 21-§ 21a), kontaktní osoba (§ 22), školení (§ 23), FAÚ a kontrola (§ 29+, ČAK u advokátů § 37), přestupky (§ 43-§ 52) |
| Zákon o evidenci skutečných majitelů | 37/2021 Sb. | `cz_law/37/2021` | Definice skutečného majitele (§ 2-§ 6), automatický průpis (§ 37+), návrh na zápis, nesrovnalost a její oznámení (§ 42+ - povinná osoba musí oznámit), sankce (nemožnost výplaty podílu na zisku, zákaz hlasování § 53-§ 54, pokuty) |
| Zákon o provádění mezinárodních sankcí | 69/2006 Sb. | `cz_law/69/2006` | Povinnosti každého: oznamovací, zákaz plnění, zmrazení; vnitrostátní sankční seznam (§ 3a - „Magnitského" novela), přestupky |
| Zákon o omezení plateb v hotovosti | 254/2004 Sb. | `cz_law/254/2004` | Limit 270 000 Kč / den pro hotovostní platbu (ověř), výjimky, sankce |
| Zákon o advokacii + usnesení ČAK | 85/1996 Sb. | `cz_law/85/1996` | Mlčenlivost (§ 21) × AML výjimky, kontrola ČAK, advokátní úschova (usnesení ČAK o úschovách - povinnost evidence v elektronické knize úschov, oznámení ČAK), kárná odpovědnost |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Legalizace výnosů (§ 216-§ 217 - včetně nedbalostní), financování terorismu (§ 312d), zatajení; trestní odpovědnost PO (418/2011 Sb.) |
| Zákon o platebním styku / o bankách | 370/2017 / 21/1992 Sb. | `cz_law/370/2017`, `cz_law/21/1992` | Platební instituce jako povinné osoby, bankovní tajemství a součinnost |
| Zákon o realitním zprostředkování | 39/2020 Sb. | `cz_law/39/2020` | Realitní zprostředkovatel - povinná osoba, úschova jen přes advokáta/notáře/banku (§ 4) |
| EU AML balíček | (EU) 2024/1624, směrnice (EU) 2024/1640, (EU) 2024/1620 (AMLA), nařízení (EU) 2023/1113 (travel rule) | zdroj `EU` | Jednotná pravidla od 2027, limit hotovosti 10 000 EUR, krypto, AMLA; přechodné použití |
| Sankční nařízení EU | (EU) 269/2014, 833/2014, 2580/2001, 881/2002 a další | zdroj `EU` | Seznamy osob, sektorové sankce, zákaz obcházení, oznamovací povinnosti |
| GDPR / zákon o zpracování osobních údajů | (EU) 2016/679 / 110/2019 Sb. | zdroj `EU`, `cz_law/110/2019` | Právní základ zpracování pro AML (právní povinnost), doba uchování, kopie dokladů |
| Daňový řád / zákon o mezinárodní spolupráci (DAC) | 280/2009 / 164/2013 Sb. | `cz_law/280/2009`, `cz_law/164/2013` | Součinnost, CRS/DAC6 oznamování, přístup FÚ k AML údajům (DAC5) |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu obchodu** → `/toc` → `/text?part=`; u novel AML zákona přechodná ustanovení (dokončení kontrol u stávajících klientů).
2. Judikatura: **NSS** (pokuty FAÚ - přiměřenost, vymezení povinné osoby, kontrola klienta, systém vnitřních zásad; nesrovnalosti v ESM), **ÚS** (mlčenlivost advokáta vs. AML - nález k oznamování, prohlídky advokátních kanceláří), **SDEU** (`ES`) - veřejný přístup k rejstříku skutečných majitelů (C-37/20 a C-601/20 zrušil veřejný přístup - dopad na české ESM ověř), povinnosti advokátů (C-305/05), **ESLP** (Michaud proti Francii). Ověř datum a znění zákona, ze kterého rozhodnutí vychází.
3. Komentář (`COMMENT`) k AML zákonu; **metodické pokyny FAÚ** (výklad pojmů, PEP, hodnocení rizik, podezřelý obchod, virtuální aktiva), **usnesení a stanoviska ČAK** (AML pro advokáty, úschovy), Národní hodnocení rizik (NRA), FATF doporučení, EBA guidelines - mimo CODEXIS oficiální zdroje s praktickou váhou.

## Workflow

1. **Kdo je povinná osoba a pro co.** Prověř § 2 AML zákona k datu: úvěrové a finanční instituce, platební instituce, směnárny, poskytovatelé služeb s virtuálními aktivy, **realitní zprostředkovatelé**, **auditoři, daňoví poradci, účetní**, **advokáti a notáři jen při** úschově peněz/cenných papírů, jednání za klienta při nákupu/prodeji nemovitosti nebo podniku, správě majetku/účtů, zakládání a správě společností a svěřenských fondů (§ 2 odst. 1 písm. g), § 27), **poskytovatelé služeb pro PO a svěřenské fondy**, obchodníci s uměním, dražebníci, **osoby přijímající hotovost nad limit** (ověř - dnes 10 000 EUR v EU balíčku), provozovatelé hazardu, zastavárny, exekutoři při úschově. Advokát v běžném zastupování a poradenství NENÍ povinnou osobou - ale mlčenlivost neplatí u aktivního napomáhání legalizaci.
2. **Identifikace klienta (§ 7-§ 8).** Kdy: obchod nad 1 000 EUR, vždy u podezřelého obchodu, obchodního vztahu, úschovy, PEP, nemovitostí, hotovosti nad limit (ověř prahy). Jak: **fyzicky za přítomnosti** (FO: jméno, RČ/datum narození, místo narození, pohlaví, bydliště, státní občanství, druh a číslo dokladu, vydavatel, platnost - z průkazu totožnosti; PO: název, sídlo, IČO, identifikace jednající FO + ověření oprávnění; zastoupení - plná moc s ověřeným podpisem), **zprostředkovaně** (§ 10 - notář, obecní úřad, jiná povinná osoba - listina o identifikaci), **převzatá** (§ 11 - od úvěrové instituce, advokáta apod. s dokumentací), **dálkově** (§ 8a - bankovní identita, ověřená kopie dokladu + platba z účtu na jméno + další ověření; ověř podmínky), kopie dokladů (§ 8 odst. 9 - lze pořídit bez souhlasu pro AML). Zaznamenat, kdo, kdy, jak; uchovat 10 let (§ 16).
3. **Kontrola klienta (§ 9).** Kdy: obchod nad 15 000 EUR, vždy u obchodního vztahu, PEP, nemovitosti, úschovy, podezřelého obchodu, hotovosti nad limit, vysoce rizikové země (ověř § 9 odst. 1). Co: (a) účel a povaha obchodu/vztahu, (b) **skutečný majitel** (ověření z ESM + vlastní šetření struktury - ESM není jediný zdroj; u nesrovnalosti oznámení podle § 42 zák. 37/2021 Sb.), (c) vlastnická a řídicí struktura (trust, offshore, nominee), (d) průběžné sledování obchodního vztahu včetně **zdroje peněžních prostředků** a u vyšší rizikovosti **zdroje majetku**, (e) PEP status a sankce, (f) aktualizace údajů. **Zesílená** (§ 9a - PEP, třetí země s vysokým rizikem, korespondenční vztahy, vysoce rizikový profil: souhlas statutárního orgánu / vedení, původ majetku, zesílené sledování), **zjednodušená** (§ 13 - nízké riziko: orgány veřejné moci, kótované společnosti, banky z EU - stále nutná identifikace). Výstup: **rizikový profil klienta** (zeměpisný, produktový, klientský, distribuční faktor) navázaný na hodnocení rizik povinné osoby (§ 21a) a NRA.
4. **Neuskutečnění, odmítnutí, oznámení.** Povinnost **odmítnout obchod** (§ 15), když se klient odmítne podrobit identifikaci/kontrole, neposkytne součinnost, identifikace/kontrola nelze provést, nebo má povinná osoba pochybnost o pravdivosti údajů; u PEP bez zjištění původu majetku; u zesílené kontroly bez souhlasu. **Podezřelý obchod** (§ 6 - demonstrativní znaky: nestandardní struktura, hotovost, sankcionované země, neodpovídá profilu, virtuální aktiva bez původu, náhlé změny, zdánlivá bezúčelnost; vždy podezřelý u sankcí a osob z FAÚ výzvy): **oznámení FAÚ bez zbytečného odkladu, nejpozději do 5 kalendářních dnů** od zjištění (§ 18 - ověř; elektronicky přes formulář FAÚ, obsah § 18 odst. 2), **odklad splnění příkazu klienta** až 24 hodin (§ 20 - pokud hrozí zmaření; FAÚ může prodloužit na 72 hodin a dále policie), **zákaz informovat klienta** (§ 38 - tipping off; výjimka: advokát může klienta odradit od protiprávního jednání - ověř § 27), mlčenlivost i po skončení. U advokáta oznámení **výhradně prostřednictvím ČAK** (§ 27 odst. 3 - ověř mechanismus a lhůty), ne přímo FAÚ; výjimka z oznamování u informací získaných při zastupování v řízení nebo poskytování právního poradenství k procesnímu postavení (§ 27 odst. 1 - ověř). Dokumentovat úvahu i tam, kde se neoznámí.
5. **Systém vnitřních zásad a organizace (§ 21-§ 23).** Písemný **systém vnitřních zásad** (u advokátů dle vzoru ČAK; obsah § 21 odst. 5: rizika, postupy identifikace a kontroly, znaky podezřelých obchodů, postup oznámení, odklad, uchovávání, školení, kontrolní mechanismy), **hodnocení rizik** (§ 21a - písemné, aktualizované, zohledňuje NRA a metodiku FAÚ), **kontaktní osoba** (§ 22 - oznámit FAÚ do 60 dnů - ověř; u advokáta lze sám), **školení zaměstnanců** nejméně jednou za 12 měsíců + při nástupu, doložitelně (§ 23), nezávislý audit u větších subjektů, **uchovávání** 10 let od ukončení vztahu / obchodu (§ 16 - identifikační údaje, kopie, kontroly, oznámení), GDPR základ a informace pro klienta, whistleblowing (zákon 171/2023 Sb.), skupinové politiky.
6. **Sankční compliance (pro každého).** Zákon 69/2006 Sb. a přímo použitelná nařízení EU: **screening** klientů, skutečných majitelů, protistran a plateb proti sankčním seznamům EU (Consolidated list), OFAC (relevantní při USD/US nexus), UK, **vnitrostátnímu seznamu ČR** (§ 3a); povinnost **oznámit FAÚ** zjištění sankcionované osoby / majetku **bez zbytečného odkladu** (§ 10 - ověř), **zmrazit** a **neplnit** (včetně nepřímého plnění a obcházení přes prostředníky - vlastnictví 50 %+ / kontrola), sektorové sankce (zákaz poskytovat právní služby ruské vládě a společnostem - čl. 5n nařízení 833/2014 - výjimky pro soudní řízení a compliance; ověř aktuální balíček), výjimky a **povolení FAÚ** (§ 9 - humanitární, právní služby, základní potřeby), nesplnění = přestupek s pokutou v mil. Kč a trestný čin (§ 410 TZ). Dokumentovat každý screening (datum, seznamy, výsledek, falešné shody).
7. **Kontroly a sankce.** Kontrola FAÚ (§ 35 - kontrolní řád 255/2012 Sb.; předložení SVZ, hodnocení rizik, záznamů o klientech, školení), u advokátů **kontrola ČAK** (§ 37), u bank ČNB; přestupky (§ 43-§ 52: neprovedení identifikace/kontroly, neoznámení, porušení mlčenlivosti, chybějící SVZ/školení - pokuty až desítky mil. Kč, u opakování zákaz činnosti/odnětí oprávnění - ověř sazby), **obrana**: liberace (vynaložení veškerého úsilí § 21 přestupkového zákona), přiměřenost, nesprávné vymezení povinné osoby, včasná náprava; správní žaloba (s. ř. s.). ESM sankce (37/2021 Sb.): nezapsaný skutečný majitel - zákaz výplaty podílu na zisku a hlasování, pokuta, nesrovnalost z podnětu povinné osoby. Kárná odpovědnost advokáta (ČAK). Trestní rovina: legalizace i z nedbalosti (§ 217 TZ), neoznámení sankcí.
8. **Typové situace v praxi advokáta a RK.** (a) **Úschova kupní ceny**: vždy identifikace + kontrola obou stran, zdroj prostředků (výpis, úvěrová smlouva, prodej předchozí nemovitosti), platba z účtu na jméno klienta (ne třetí osoba bez vysvětlení), zápis do elektronické knihy úschov ČAK, žádná hotovost nad limit, u cizinců/offshore zesílená kontrola; (b) **prodej nemovitosti** přes RK: RK i advokát každý za sebe; (c) **zakládání s.r.o./svěřenského fondu pro klienta** - poskytovatel služeb pro PO, zápis skutečného majitele; (d) **správa majetku / účtů klienta** - obchodní vztah, průběžné sledování; (e) **hotovost** - limit 270 000 Kč za den (ověř) + AML práh; (f) **virtuální aktiva** - VASP registrace, travel rule, původ; (g) **PEP klient** (i rodinní příslušníci a blízcí spolupracovníci, tuzemští PEP od 2021, 12 měsíců po skončení funkce) - souhlas vedení, původ majetku; (h) **klient odmítá doklady** - obchod neuskutečnit, zvážit oznámení.

## Časté pasti

- Advokát považuje celou činnost za AML-vyňatou (mlčenlivost) - u úschov, nemovitostí a zakládání společností je povinnou osobou; naopak oznamuje FAÚ přímo místo přes ČAK.
- Identifikace „z kopie občanky poslané e-mailem" bez zákonného dálkového postupu - neprovedená identifikace.
- Skutečný majitel převzat jen z ESM bez vlastního ověření struktury; nesrovnalost neoznámena.
- Kontrola klienta zúžena na identifikaci - chybí účel obchodu, zdroj prostředků a průběžné sledování.
- PEP screening jen u zahraničních osob - tuzemští PEP jsou zahrnuti; rodinní příslušníci a blízcí spolupracovníci opomenuti.
- Sankční screening jen při navázání vztahu, ne při každé platbě a změně seznamů; 50% pravidlo vlastnictví ignorováno.
- Podezřelý obchod „vyřešen" odmítnutím bez oznámení; nebo oznámen po lhůtě; nebo klient informován (tipping off).
- Hotovost přijatá nad limit 270 000 Kč (nebo AML práh) „ve splátkách" v jednom dni - obcházení.
- Systém vnitřních zásad stažený jako vzor bez vlastního hodnocení rizik a bez doložených školení - první nález při kontrole.
- Uchovávání dokladů kratší než 10 let nebo bez záznamu o způsobu identifikace; naopak neoprávněné zpracování údajů mimo AML účel.
- Právní služby ruské společnosti bez posouzení čl. 5n a výjimek - porušení sankcí.
- Doplňování prahů, lhůt, sazeb pokut a čísel paragrafů z paměti - vždy z aktuálního znění nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší povinnost** (je/není povinná osoba pro tento obchod; co provést před obchodem; lhůta oznámení).
2. **Kvalifikace** - typ obchodu, klient (FO/PO/trust, PEP, země), spouštěče (prahy, hotovost, sankce), rizikový profil.
3. **Právní rámec** - AML zákon / ESM / sankce / ČAK v aktuálním znění, s odkazy; EU balíček, pokud relevantní.
4. **Checklist kroků** - tabulka: krok | právní základ | doklad/záznam | kdo | lhůta.
5. **Rozhodnutí o obchodu** (provést × zesílená kontrola × odmítnout × oznámit; odklad).
6. **Rizika a sankce** (pokuty, kárná, trestní) a **judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 As 123/2024 - …`, `SDEU - C-37/20 - 22.11.2022`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („bez zbytečného odkladu, nejpozději do 5 kalendářních dnů“, „za fyzické přítomnosti“, „neuskuteční obchod“, „skutečný majitel = každá fyzická osoba, která v konečném důsledku vlastní nebo kontroluje“).
- Jeden časový řez; znění AML zákona a sankčních seznamů k datu obchodu; u EU balíčku výslovně uvést datum použitelnosti.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k datu obchodu.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Prahy, lhůty, sazby pokut a seznam povinných osob nikdy z paměti - vždy z aktuálního znění s odkazem.
- Sankční screening a ESM výhradně z oficiálních zdrojů k datu úkonu (sanctionsmap.eu, EU Consolidated list, financnianalytickyurad.cz, esm.justice.cz, cak.cz); mimo CODEXIS jen tyto.
- Nikdy neradit, jak obejít identifikaci, rozdělit hotovost pod limit, obejít sankce nebo informovat klienta o oznámení FAÚ.
