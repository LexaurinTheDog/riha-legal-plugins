---
uuid: d81b733a-368e-414d-9a58-7a527d2f8245
name: it-pravo-kyberbezpecnost
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "IT právo a kyberbezpečnost ČR"
    summary: "Smlouvy o vývoji a licencování software, SaaS a cloud, IT outsourcing a SLA, open source, NIS2 a nový zákon o kybernetické bezpečnosti, regulované subjekty a hlášení incidentů, DORA, odpovědnost za bezpečnostní incident, platformy a DSA, elektronické podpisy a eIDAS."
    examplePrompts:
      - "Dodavatel software nedodal systém včas a klient chce odstoupit a získat zpět zálohy. Co říká smlouva o dílo v IT a jak řešit zdrojové kódy a licenci?"
      - "Klient je střední výrobní firma s 60 zaměstnanci. Spadá pod nový zákon o kybernetické bezpečnosti a co musí do kdy udělat?"
      - "Po ransomware útoku unikla data zákazníků. Jaké oznamovací povinnosti (NÚKIB, ÚOOÚ, zákazníci) a lhůty běží a jak omezit odpovědnost?"
  en:
    displayName: "Czech IT Law & Cybersecurity"
    summary: "Software development and licensing contracts, SaaS and cloud, IT outsourcing and SLA, open source, NIS2 and the new Cybersecurity Act, regulated entities and incident reporting, DORA, security breach liability, platforms and DSA, electronic signatures and eIDAS."
    examplePrompts:
      - "A software vendor missed the delivery deadline and my client wants to withdraw and recover advances. What do IT work contracts say and how to handle source code and licence?"
      - "My client is a mid-sized manufacturer with 60 employees. Does it fall under the new Cybersecurity Act and what must it do by when?"
      - "After a ransomware attack customer data leaked. Which notification duties (NÚKIB, data protection authority, customers) and deadlines apply and how to limit liability?"
  sk:
    displayName: "IT právo a kyberbezpečnosť ČR"
    summary: "Zmluvy o vývoji a licencovaní softvéru, SaaS a cloud, IT outsourcing a SLA, open source, NIS2 a nový zákon o kybernetickej bezpečnosti, regulované subjekty a hlásenie incidentov, DORA, zodpovednosť za bezpečnostný incident, platformy a DSA, elektronické podpisy a eIDAS."
    examplePrompts:
      - "Dodávateľ softvéru nedodal systém včas a klient chce odstúpiť a získať späť zálohy. Čo hovorí zmluva o dielo v IT a ako riešiť zdrojové kódy a licenciu?"
      - "Klient je stredná výrobná firma so 60 zamestnancami. Spadá pod nový zákon o kybernetickej bezpečnosti a čo musí dokedy urobiť?"
      - "Po ransomware útoku unikli dáta zákazníkov. Aké oznamovacie povinnosti (NÚKIB, ÚOOÚ, zákazníci) a lehoty plynú a ako obmedziť zodpovednosť?"
description: Use when the user's matter involves information technology contracts or cybersecurity regulation in the Czech Republic - IT právo, smlouva o vývoji software, smlouva o dílo v IT, licenční smlouva k software, SaaS, cloudová smlouva, IT outsourcing, SLA, zdrojové kódy, open source licence, autorské právo k software, kybernetická bezpečnost, NIS2, zákon o kybernetické bezpečnosti (264/2025 Sb.), NÚKIB, regulovaná služba, režim vyšších a nižších povinností, hlášení kybernetického bezpečnostního incidentu, DORA, Cyber Resilience Act, odpovědnost za bezpečnostní incident, ransomware, únik dat, oznámení porušení zabezpečení, eIDAS, elektronický podpis, datové schránky, DSA, online platformy, odpovědnost poskytovatele, cookies, e-shop, IT ve veřejných zakázkách, umělá inteligence ve smlouvách. Standalone skill - bundles CODEXIS methodology with IT-practice method; no need to load the general codexis skill.
---

# IT právo a kyberbezpečnost ČR

Samostatný oborový skill pro smlouvy v informačních technologiích a regulaci kybernetické bezpečnosti. Základní reflex u smluv: **IT projekt selhává na akceptaci, změnovém řízení a licenci ke zdrojovým kódům** - odpověď musí vždy říct, co smlouva říká o milnících, akceptačních testech, vadách, změnách rozsahu a k čemu přesně objednatel získává práva. Základní reflex u regulace: **od účinnosti nového zákona o kybernetické bezpečnosti (transpozice NIS2) se povinnosti spouštějí registrací regulované služby** - nejdřív určit, zda a v jakém režimu klient spadá, a od kdy běží lhůty. Software je autorské dílo; práva vznikají autorovi/zaměstnavateli, ne tomu, kdo zaplatil.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/264/2025/versions`, `cdx-cli get cdx://cz_law/121/2000/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf58'`, `cdx-cli search EU --query "směrnice 2022/2555 NIS2 opatření k zajištění vysoké společné úrovně kybernetické bezpečnosti" --limit 5`, `cdx-cli search JD --query "smlouva o dílo software akceptace vady odstoupení" --court "Nejvyšší soud" --limit 5`.
- Nový zákon o kybernetické bezpečnosti (č. 264/2025 Sb. - **číslo a datum účinnosti ověř**; nahrazuje 181/2014 Sb.) a jeho prováděcí vyhlášky (regulované služby, bezpečnostní opatření, hlášení incidentů) jsou nové - **prahy, kategorie služeb, lhůty registrace a hlášení ověř v aktuálním znění a na nukib.gov.cz**; nikdy z paměti. Přímo použitelná nařízení (DORA, CRA, DSA, eIDAS 2.0, AI Act) čti ze zdroje `EU` a ověř data použitelnosti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o kybernetické bezpečnosti (nový, NIS2) | 264/2025 Sb. (ověř) | `cz_law/264/2025` | Regulované služby a poskytovatelé, registrace, režim vyšších × nižších povinností, bezpečnostní opatření, hlášení incidentů, mechanismus prověřování dodavatelů (bezpečnost dodavatelského řetězce), odpovědnost vrcholného vedení, NÚKIB - dohled, přestupky; starý zákon 181/2014 Sb. pro dobíhající povinnosti |
| Prováděcí vyhlášky NÚKIB | (čísla ověř) | `cz_law/...` | Kritéria regulovaných služeb, bezpečnostní opatření pro oba režimy, náležitosti hlášení, kritická infrastruktura |
| Směrnice NIS2 / DORA / CRA / CER | (EU) 2022/2555, (EU) 2022/2554, (EU) 2024/2847, (EU) 2022/2557 | zdroj `EU` | Rámec NIS2, digitální provozní odolnost finančního sektoru (DORA - přímo použitelné, ICT rizika, smlouvy s ICT poskytovateli, hlášení), bezpečnost produktů s digitálními prvky (CRA), odolnost kritických subjektů |
| Autorský zákon | 121/2000 Sb. | `cz_law/121/2000` | Software jako dílo (§ 2 odst. 2, § 65-§ 66 - výjimky, rozmnožování, dekompilace), zaměstnanecké dílo (§ 58 - vykonává zaměstnavatel; software vytvořený na objednávku se považuje za zaměstnanecké § 58 odst. 7), licence (§ 2358+ OZ), databáze (§ 88+), TDM výjimky |
| Občanský zákoník | 89/2012 Sb. | `cz_law/89/2012` | Smlouva o dílo (§ 2586-§ 2635: cena, změny, převzetí a vady § 2604+, odstoupení), licenční smlouva (§ 2358-§ 2389: výhradní/nevýhradní, podlicence, odměna, forma u výhradní), smlouva o poskytování služeb / příkaz, odpovědnost za újmu (§ 2894+), limitace náhrady (§ 2898 - nelze vyloučit úmysl a hrubou nedbalost), obchodní podmínky (§ 1751-§ 1753), adhezní smlouvy, spotřebitel a digitální obsah (§ 2389a+ - směrnice 2019/770) |
| Zákon o službách informační společnosti | 480/2004 Sb. | `cz_law/480/2004` | Odpovědnost poskytovatelů hostingu, obchodní sdělení (spam), doplněno DSA |
| DSA / DMA / P2B | (EU) 2022/2065, (EU) 2022/1925, (EU) 2019/1150 | zdroj `EU` | Povinnosti online zprostředkovatelů, platformy, notice-and-action, transparentnost, DSC v ČR (ČTÚ - ověř) |
| eIDAS + adaptační zákon | (EU) 910/2014 ve znění (EU) 2024/1183 / 297/2016 Sb. | zdroj `EU`, `cz_law/297/2016` | Elektronický podpis (prostý, zaručený, kvalifikovaný), pečeť, časové razítko, kvalifikovaní poskytovatelé, evropská peněženka digitální identity; podepisování vůči veřejné moci (§ 5-§ 6 zák. 297/2016) |
| Zákon o elektronických úkonech a datových schránkách | 300/2008 Sb. | `cz_law/300/2008` | Doručování, fikce, autorizovaná konverze |
| Zákon o právu na digitální služby / eGovernment | 12/2020 / 365/2000 Sb. | `cz_law/12/2020`, `cz_law/365/2000` | Digitální služby veřejné správy, ISVS, atestace, cloud computing ve veřejné správě (katalog cloud computingu) |
| GDPR / zákon 110/2019 Sb. | (EU) 2016/679 | zdroj `EU`, `cz_law/110/2019` | Zpracovatelská smlouva (čl. 28), bezpečnost (čl. 32), oznámení porušení (čl. 33-34 - 72 hodin), přenosy mimo EU, DPIA; viz skill GDPR |
| AI Act | (EU) 2024/1689 | zdroj `EU` | Zakázané praktiky, vysoce rizikové systémy, transparentnost, GPAI; fázovaná použitelnost (ověř data) |
| Zákon o zadávání veřejných zakázek | 134/2016 Sb. | `cz_law/134/2016` | IT zakázky, vendor lock-in, JŘBU, technické podmínky, změny závazku (viz skill VZ) |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Neoprávněný přístup (§ 230), opatření a přechovávání přístupového zařízení (§ 231), poškození dat (§ 232), porušení autorského práva (§ 270) |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu smlouvy / incidentu** → `/toc` → `/text?part=`; u nařízení EU zdroj `EU` a datum použitelnosti.
2. Judikatura: **NS** (smlouva o dílo v IT - akceptace, vady, prodlení, odstoupení a vrácení plnění; licence a rozsah užití; zaměstnanecké dílo; smluvní pokuty; limitace náhrady), **NSS** (pokuty NÚKIB/ÚOOÚ, přezkum rozhodnutí, veřejné zakázky IT - ÚOHS), **ÚS** (elektronické podání a podpis - doručení, autenticita), **SDEU** (`ES`) - software a vyčerpání práv (UsedSoft C-128/11), dekompilace (Top System C-13/20), databáze, odpovědnost platforem (YouTube/Cyando C-682/18), GDPR bezpečnost. Ověř datum a znění.
3. Komentář (`COMMENT`) k autorskému zákonu a OZ (dílo, licence); **metodiky a podpůrné materiály NÚKIB** (regulované služby, bezpečnostní opatření, hlášení), stanoviska ÚOOÚ, doporučení ČAK k eIDAS - mimo CODEXIS oficiální zdroje s praktickou váhou.

## Workflow

1. **Kvalifikace.** Typ vztahu: vývoj na zakázku (dílo) × licence k hotovému SW × SaaS/cloud (služba) × outsourcing/podpora (rámcová + SLA) × implementace ERP (kombinace) × HW/IoT × platforma. Strany (podnikatel, spotřebitel, veřejný zadavatel, finanční subjekt pod DORA, regulovaný subjekt pod ZKB), datum smlouvy, rozhodné právo a soud, verze OP/SLA k datu.
2. **Smlouva o vývoji a implementaci.** Předmět: specifikace (analýza, funkční × technická; agilní - backlog a sprinty vs. fixní rozsah), **milníky a akceptace** (kritéria, testy, lhůta na vytknutí vad, fikce akceptace, kategorie vad A/B/C, opakované testy), cena (fixní × T&M × cap; platby po milnících, zádržné), změnové řízení (change request - písemně, dopad na cenu a termín), **prodlení a odstoupení** (smluvní pokuta, podstatné porušení, částečné odstoupení, vypořádání rozpracovaného díla a záloh, povinnost součinnosti objednatele), vady a záruka (§ 2615+ OZ - oznámení bez zbytečného odkladu, nároky, záruční doba × maintenance), **práva k výsledkům** (licence výhradní/nevýhradní, územní a časová neomezenost, právo měnit a upravovat, podlicence, zdrojové kódy a dokumentace - předání, escrow, podmínky uvolnění; standardní komponenty a open source dodavatele - výčet a licence; zaměstnanecké dílo § 58 AZ - autor zaměstnanec × subdodavatel OSVČ → nutná licence od subdodavatele!), **limitace odpovědnosti** (cap na cenu, vyloučení ušlého zisku - v mezích § 2898 OZ; nelze pro úmysl/hrubou nedbalost, újmu na zdraví; spotřebitel), mlčenlivost a NDA, GDPR zpracovatelská smlouva (čl. 28), exit a migrace, ukončení, vendor lock-in.
3. **SaaS, cloud, outsourcing.** Služba, ne dílo: **SLA** (dostupnost v %, výpočet, výluky, plánovaná odstávka, kredity jako výlučná sankce?, RTO/RPO, podpora - reakční doby), bezpečnost (certifikace ISO 27001, SOC 2, penetrační testy, šifrování, právo auditu), **lokalizace dat a subdodavatelé** (EU/EHP, přenosy mimo EU - SCC, DPF; seznam subprocesorů), vlastnictví dat a **exit plán** (export ve strukturovaném formátu, doba, součinnost, výmaz), změny služby a cen (jednostranná změna OP - § 1752 OZ), ukončení a doba trvání (autoprolongace, výpovědní doba), odpovědnost a limitace, dostupnost zdrojových kódů (escrow u kritických systémů), veřejná správa - katalog cloud computingu a atestace (zák. 365/2000 Sb. - ověř), **DORA** u finančních subjektů (povinné náležitosti smluv s ICT poskytovateli čl. 30, registr smluv, testování, koncentrace), **NIS2/ZKB - bezpečnost dodavatelského řetězce** (smluvní požadavky na dodavatele, mechanismus prověřování rizikových dodavatelů u strategicky významné infrastruktury).
4. **Licence a open source.** Licenční smlouva (§ 2358+ OZ: rozsah, výhradnost - písemná forma, odměna, podlicence, převod; EULA/click-wrap platnost), vyčerpání práva u trvalé licence (UsedSoft - prodej „použitých" licencí), zákaz dekompilace mimo § 66 AZ, audit licencí (compliance u velkých vendorů), **open source** (GPL/AGPL copyleft × permissivní MIT/Apache; povinnosti při distribuci a SaaS (AGPL); kontaminace proprietárního kódu; SBOM - CRA), zaměstnanecké dílo a odměna autora (§ 58 odst. 6), díla vytvořená AI (bez autora - ověř aktuální výklad), databáze (zvláštní právo pořizovatele § 88+), API a jejich ochrana, ochranné známky a doména (viz skill IP).
5. **NIS2 / zákon o kybernetické bezpečnosti.** (a) **Určení regulované služby**: odvětví (energetika, doprava, bankovnictví, zdravotnictví, digitální infrastruktura, veřejná správa, výroba, potraviny, odpady, chemie, poštovní služby, výzkum atd.) + velikost (střední podnik 50+ zaměstnanců / obrat 10 mil. EUR - ověř; některé služby bez ohledu na velikost) → **režim vyšších × nižších povinností**; (b) **registrace u NÚKIB** do zákonné lhůty od splnění kritérií (ověř - typicky 60 dnů) přes portál; (c) **bezpečnostní opatření** podle vyhlášky pro daný režim (organizační: řízení rizik, politiky, role - manažer KB, architekt, auditor; technická: řízení přístupu, logování, šifrování, zálohování, BCM, bezpečnost dodavatelů) s implementační lhůtou (ověř - 1 rok od registrace); (d) **hlášení incidentů** (významný incident - včasné varování 24 h, hlášení 72 h, závěrečná zpráva 1 měsíc - ověř podle vyhlášky a režimu) přes portál NÚKIB; (e) **odpovědnost vrcholného vedení** (schválení opatření, školení, osobní odpovědnost), (f) **mechanismus prověřování rizikovosti dodavatelů** (strategicky významná infrastruktura - zákaz/omezení dodavatele rozhodnutím NÚKIB, dopad na existující smlouvy), (g) dohled, kontrola a **pokuty** (až 10 mil. EUR / 2 % obratu u vyšších - ověř), nápravná opatření, zveřejnění. Dokumentace: analýza rizik, prohlášení o aplikovatelnosti, plány, záznamy, smlouvy s dodavateli.
6. **Bezpečnostní incident - reakce.** Souběžné povinnosti a lhůty: **NÚKIB** (regulované subjekty - 24/72 h), **ÚOOÚ** (čl. 33 GDPR - 72 h od zjištění, když riziko pro práva subjektů; subjekty údajů čl. 34 - bez zbytečného odkladu při vysokém riziku), **ČNB** (DORA - finanční subjekty), **Policie ČR** (trestní oznámení - § 230-§ 232 TZ; ransomware), **smluvní partneři** (SLA, zpracovatelské smlouvy - zpracovatel hlásí správci bez zbytečného odkladu), pojišťovna (kybernetické pojištění - lhůty, souhlas s výdaji, zákaz platby výkupného bez souhlasu), burza/auditor; zajištění důkazů (forenzní kopie, řetězec důkazů, logy), komunikace (privilegovaná komunikace s advokátem, PR), **výkupné** (sankční screening příjemce - zákaz platby sankcionované osobě; daňová a trestní rovina; doporučení NÚKIB neplatit), regres vůči dodavateli (limitace, hrubá nedbalost), nároky poškozených (§ 2894+ OZ, čl. 82 GDPR - nemajetková újma), hromadné žaloby (zákon 179/2024 Sb.).
7. **Elektronické podpisy, identita, doručování.** Úrovně podpisu dle eIDAS (prostý - platný i ve smlouvách s písemnou formou § 562 OZ, ale důkazně slabší; zaručený; **kvalifikovaný = vlastnoruční podpis**); vůči veřejné moci jen kvalifikovaný/uznávaný (§ 6 zák. 297/2016 Sb.), pečeť PO, časové razítko (dlouhodobá platnost - LTV), ověřování platnosti (CRL/OCSP), podepisování přes DocuSign/Adobe (prostý × kvalifikovaný, důkazní hodnota - auditní stopa), **datové schránky** (fikce doručení 10 dnů, konverze § 22+ zák. 300/2008 Sb., podpis se u DS nevyžaduje - § 18 odst. 2), bankovní identita a NIA, evropská peněženka digitální identity (eIDAS 2.0 - data ověř), archivace elektronických dokumentů (důvěryhodné úložiště, § 69a AZ o archivnictví).
8. **Platformy, e-commerce, obsah.** DSA (poskytovatelé hostingu - notice-and-action, kontaktní místo, transparentnost; online platformy - reklama, doporučovací systémy, ochrana nezletilých; VLOP), odpovědnost za cizí obsah (§ 5 zák. 480/2004 Sb. + DSA čl. 6), obchodní sdělení (§ 7 - opt-in, soukromí a cookies - § 89 zák. 127/2005 Sb. - opt-in od 2022), P2B pro business uživatele, DMA gatekeepeři, smlouvy s influencery, geoblocking, spotřebitel a digitální obsah (§ 2389a+ OZ - aktualizace, shoda), e-shop povinnosti (viz skill spotřebitelského práva), Cyber Resilience Act pro výrobce produktů s digitálními prvky (CE, hlášení zranitelností - data ověř).
9. **AI ve smlouvách a compliance.** AI Act - klasifikace systému (zakázané, vysoce rizikové - příloha III, transparentnost, GPAI), role (poskytovatel × zavádějící subjekt), povinnosti a data použitelnosti (ověř), smlouvy o dodávce AI řešení (trénovací data a licence, výstupy a práva, halucinace a odpovědnost, zákaz použití dat pro trénink, audit), GDPR (právní základ, automatizované rozhodování čl. 22), autorské právo a TDM výjimky (§ 39c AZ - ověř), zaměstnanci a AI nástroje (interní politika, důvěrnost), veřejná správa a algoritmické rozhodování.

## Časté pasti

- Objednatel zaplatil za vývoj, ale nemá licenci ke zdrojovým kódům ani právo software měnit - smlouva mlčí, práva zůstávají dodavateli (a jeho subdodavatelům-OSVČ).
- Akceptace fikcí (uplynutím lhůty) přehlédnuta - vady se považují za vytknuté pozdě; naopak dodavatel bez fikce čeká na akceptaci roky.
- Agilní vývoj s fixní cenou a bez změnového řízení - spor o rozsah; T&M bez capu - spor o cenu.
- Limitace odpovědnosti na 100 % ceny bez výjimek - neúčinná pro úmysl/hrubou nedbalost, ale klient o tom neví a neuplatní.
- Subdodavatel dodavatele (freelancer) bez písemné licence - řetězec práv přerušen, objednatel nemá nic.
- GPL/AGPL komponenta v proprietárním produktu - povinnost zveřejnit zdroj, riziko při prodeji firmy (due diligence).
- Firma pod NIS2 „počká na výzvu NÚKIB" - registrace je povinnost subjektu ve lhůtě; pokuta i za neregistraci.
- Incident hlášen jen ÚOOÚ, ne NÚKIB (nebo naopak); lhůta 72 h počítána od „potvrzení", ne od zjištění.
- Výkupné zaplaceno bez sankčního screeningu - porušení sankcí.
- Kybernetické pojištění: platba/výdaje bez souhlasu pojistitele - odmítnutí plnění.
- Prostý elektronický podpis (klik) u smlouvy, kde zákon vyžaduje úředně ověřený podpis nebo kvalifikovaný - neplatnost/nevkladatelnost.
- SaaS bez exit plánu a formátu exportu - data „v zajetí" po výpovědi.
- DORA přehlédnuta u fintech/pojišťovacího klienta - smlouvy s ICT dodavateli bez povinných náležitostí.
- Doplňování čísel vyhlášek, prahů, lhůt a sazeb pokut z paměti - vždy z aktuálního znění nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat, komu hlásit / co vytknout, do kdy).
2. **Kvalifikace** - typ vztahu/služby, role stran, regulační režim (ZKB vyšší × nižší, DORA, GDPR), datum a znění.
3. **Právní rámec** - OZ / AZ / ZKB / EU nařízení v aktuálním znění, s odkazy.
4. **Smluvní analýza nebo checklist povinností** - tabulka: klauzule/povinnost | právní základ | stav (OK / riziko / chybí) | doporučení | lhůta.
5. **Rizika a odpovědnost** (limitace, sankce, trestní rovina, pojištění).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. SDEU.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 23 Cdo 1234/2024 - …`, `SDEU - C-128/11 - 03.07.2012`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („bez zbytečného odkladu, nejpozději do 72 hodin“, „považuje se za zaměstnanecké dílo“, „v rozsahu nezbytném“, „významný kybernetický bezpečnostní incident“).
- Jeden časový řez; znění ZKB a nařízení EU k datu incidentu / smlouvy; u nových předpisů výslovně uvést datum použitelnosti.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Prahy, lhůty hlášení, sazby pokut, čísla vyhlášek a data použitelnosti EU předpisů nikdy z paměti - vždy z aktuálního znění s odkazem.
- Mimo CODEXIS jen oficiální zdroje (nukib.gov.cz, uoou.gov.cz, eur-lex, digitalni-agentura.gov.cz, ctu.gov.cz) když CODEXIS neodpovídá.
- Nikdy neradit, jak obejít hlášení incidentu, zatajit únik dat nebo zaplatit výkupné sankcionované osobě.
