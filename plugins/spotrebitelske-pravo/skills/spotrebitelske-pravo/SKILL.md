---
uuid: fae0824e-fc7a-47b3-a8db-fda0bbe4aff2
name: spotrebitelske-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Spotřebitelské právo ČR"
    summary: "Spotřebitelské smlouvy a e-shopy, odstoupení, vady a reklamace, zakázaná ujednání a nekalé praktiky, spotřebitelský úvěr, mimosoudní řešení a hromadné řízení, compliance obchodníka."
    examplePrompts:
      - "E-shop odmítá vrátit peníze za zboží vrácené 13. den s tím, že bylo rozbalené. Má spotřebitel nárok?"
      - "Klient podepsal na prezentační akci smlouvu o úvěru na 150 000 Kč bez posouzení příjmů. Jak z toho ven?"
      - "Zreviduj obchodní podmínky e-shopu z pohledu spotřebitelského práva a ČOI."
  en:
    displayName: "Czech Consumer Law"
    summary: "Consumer contracts and e-commerce, withdrawal, defects and complaints, unfair terms and practices, consumer credit, ADR and collective redress, trader compliance."
    examplePrompts:
      - "An e-shop refuses to refund goods returned on day 13 because the package was opened. Is the consumer entitled to a refund?"
      - "My client signed a CZK 150,000 credit agreement at a sales event without any income assessment. How to get out of it?"
      - "Review an e-shop's terms and conditions from the consumer-law and ČOI perspective."
  sk:
    displayName: "Spotrebiteľské právo ČR"
    summary: "Spotrebiteľské zmluvy a e-shopy v ČR, odstúpenie, vady a reklamácie, zakázané dojednania a nekalé praktiky, spotrebiteľský úver, mimosúdne riešenie a hromadné konanie, compliance obchodníka."
    examplePrompts:
      - "E-shop odmieta vrátiť peniaze za tovar vrátený 13. deň s tým, že bol rozbalený. Má spotrebiteľ nárok?"
      - "Klient podpísal na prezentačnej akcii zmluvu o úvere na 150 000 Kč bez posúdenia príjmov. Ako z toho von?"
      - "Zreviduj obchodné podmienky e-shopu z pohľadu spotrebiteľského práva a ČOI."
description: Use when the user's matter involves a consumer (spotřebitel) against a trader under Czech or EU law, or a trader's consumer compliance - spotřebitelská smlouva (§ 1810+ OZ), e-shop, distanční smlouva, smlouva mimo obchodní prostory, předsmluvní informace, obchodní podmínky, zakázaná ujednání, odstoupení do 14 dnů, vrácení zboží, prodej zboží spotřebiteli (§ 2158+ OZ), vady, reklamace, 30 dnů, záruka, digitální obsah, zákon o ochraně spotřebitele (634/1992 Sb.), nekalé obchodní praktiky, klamavé slevy, recenze, ČOI, spotřebitelský úvěr (257/2016 Sb.), úvěruschopnost, RPSN, předčasné splacení, finanční arbitr, mimosoudní řešení sporů, ADR, hromadné řízení (179/2024 Sb.), rozhodčí doložka, prorogace, zájezd, letecká kompenzace, energie, telekomunikace, spotřebitel v exekuci či insolvenci. Standalone skill - bundles CODEXIS methodology with consumer-practice method; no need to load the general codexis skill.
---

# Spotřebitelské právo ČR

Samostatný oborový skill pro vztahy spotřebitel - podnikatel z obou stran. První otázka: **je to spotřebitel a jakým kanálem smlouva vznikla** - od toho se odvíjí informační povinnosti, právo odstoupit, režim vad i to, co soud musí zkoumat z úřední povinnosti.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf1829'`, `cdx-cli get cdx://cz_law/634/1992/versions`, `cdx-cli get cdx://cz_law/257/2016/versions`, `cdx-cli search JD --query "spotřebitel odstoupení od smlouvy 14 dnů poučení" --court "Nejvyšší soud" --limit 5`, `cdx-cli search EU --query "směrnice 2011/83 práva spotřebitelů" --limit 5`.
- Spotřebitelské právo OZ i zákon o ochraně spotřebitele byly zásadně novelizovány k 6. 1. 2023 (transpozice směrnic 2019/770, 2019/771, 2019/2161) - **lhůty, domněnky, informační povinnosti a čísla paragrafů ověř v aktuálním znění k datu uzavření smlouvy**; nikdy z paměti. Smlouvy před novelou se posuzují podle tehdejšího znění.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - spotřebitelské smlouvy | 89/2012 Sb. | `cz_law/89/2012` | Spotřebitel (§ 419), obecná ochrana (§ 1810-§ 1819 - zakázaná ujednání § 1814, § 1815), distanční a mimo prostory (§ 1820-§ 1840 - informace, odstoupení § 1829-§ 1837), finanční služby (§ 1841+), timeshare (§ 1852+), prodej zboží spotřebiteli (§ 2158-§ 2174b), digitální obsah (§ 2389a+), zájezd (§ 2521+), promlčení (§ 629+) |
| Zákon o ochraně spotřebitele | 634/1992 Sb. | `cz_law/634/1992` | Nekalé obchodní praktiky (§ 4-§ 5b + přílohy), informační povinnosti a ceny (§ 9-§ 13, slevy § 12a), reklamace (§ 19), ADR (§ 20d+), dozor a sankce (§ 23+) |
| Zákon o spotřebitelském úvěru | 257/2016 Sb. | `cz_law/257/2016` | Předsmluvní informace, posouzení úvěruschopnosti (§ 86-§ 87), odstoupení (§ 118), předčasné splacení (§ 117), sankce za prodlení (§ 122), dozor ČNB/ČOI |
| Zákon o finančním arbitrovi | 229/2002 Sb. | `cz_law/229/2002` | Bezplatné řízení, vykonatelný nález, úvěry a platební služby |
| Zákon o hromadném občanském řízení soudním | 179/2024 Sb. | `cz_law/179/2024` | Hromadné žaloby spotřebitelů (spolky, opt-in) |
| Zákon o rozhodčím řízení | 216/1994 Sb. | `cz_law/216/1994` | Nepřípustnost rozhodčích doložek ve spotřebitelských smlouvách (ověř § 2) |
| Zákon o službách informační společnosti / o elektronických komunikacích | 480/2004 / 127/2005 Sb. | `cz_law/480/2004`, `cz_law/127/2005` | Obchodní sdělení, cookies, smlouvy o službách elektronických komunikací (§ 63) |
| Energetický zákon | 458/2000 Sb. | `cz_law/458/2000` | Zákazník v domácnosti, změna dodavatele, ERÚ |
| Zákon o některých podmínkách podnikání v cestovním ruchu | 159/1999 Sb. | `cz_law/159/1999` | Zájezd, pojištění proti úpadku CK |
| Směrnice a nařízení EU | 2011/83, 2019/771, 2019/770, 2005/29, 93/13, (ES) 261/2004, (EU) 1215/2012 | zdroj `EU` | Eurokonformní výklad, letecká kompenzace, fórum spotřebitele |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Příslušnost, prorogace (§ 89a - jen mezi podnikateli), předžalobní výzva (§ 142a), náklady (§ 14b AT) |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu uzavření smlouvy** (pozor na 6. 1. 2023) → `/toc` → `/text?part=`; směrnice ze zdroje `EU` pro eurokonformní výklad.
2. Judikatura: **SDEU** (`ES`) je v spotřebitelském právu primární - zkoumání nepřiměřených ujednání z úřední povinnosti, transparentnost, sankce za nesplnění informační povinnosti; **NS** senáty 33 Cdo / 23 Cdo (spotřebitelské smlouvy, úvěry, rozhodčí doložky), **ÚS** (ochrana slabší strany), **NSS** (ČOI pokuty, nekalé praktiky). Ověř, zda rozhodnutí nevychází ze znění před novelou 2023.
3. Komentář (`COMMENT`) k pojmům (spotřebitel a smíšený účel, průměrný spotřebitel, podstatná nerovnováha, přiměřená doba); stanoviska ČOI a Komise jsou administrativní výklad.

## Workflow

1. **Strany a kanál.** Spotřebitel = fyzická osoba mimo podnikání (§ 419; smíšený účel - převažující účel, judikatura); podnikatel (§ 420 - i ten, kdo tak vystupuje). Kanál: v provozovně × distančně (e-shop, telefon) × mimo obchodní prostory (prezentační akce, podomní prodej) × finanční služba na dálku. Kanál určuje informační povinnosti (§ 1811, § 1820, § 1824) a právo odstoupit.
2. **Předsmluvní informace a jejich sankce.** Nesplnění informační povinnosti o právu odstoupit **prodlužuje lhůtu k odstoupení** (§ 1829 odst. 2 - ověř délku), neúčtované náklady nelze požadovat (§ 1821), tlačítko „objednávka zavazující k platbě" (§ 1826a), potvrzení smlouvy v textové podobě (§ 1827), poplatky za platbu a telefon (§ 1817, § 1818).
3. **Odstoupení do 14 dnů (§ 1829-§ 1837).** Běh od převzetí zboží (u služeb od uzavření), stačí odeslat v poslední den, formulář nepovinný; vrácení peněz do 14 dnů (podnikatel může počkat na vrácení zboží), náklady vrácení nese spotřebitel jen po poučení; odpovědnost za snížení hodnoty jen nad rámec vyzkoušení (§ 1833); **výjimky § 1837** (zboží na míru, hygienické v zapečetěném obalu, digitální obsah po souhlasu s dodáním, ubytování a doprava na termín, alkohol, noviny…) - vykládat restriktivně.
4. **Vady a reklamace (§ 2158-§ 2174b OZ, § 19 ZOS).** Odpovědnost 2 roky (u použitého lze zkrátit na 1 rok), **domněnka vady při projevení do 1 roku od převzetí** (ověř), jakost při převzetí (§ 2161 - objektivní a subjektivní požadavky, aktualizace digitálních prvků), nároky v pořadí: oprava/výměna → sleva/odstoupení při neodstranění, opakování nebo podstatné vadě (§ 2169-§ 2171), náklady reklamace (§ 1924), reklamace u prodávajícího nebo v provozovně, písemné potvrzení, **vyřízení do 30 dnů včetně odstranění - marné uplynutí zakládá právo odstoupit nebo na slevu** (§ 19 ZOS - ověř), záruka za jakost (§ 2113 - dobrovolná, nad rámec), náhradní díly a servis.
5. **Zakázaná ujednání a nekalé praktiky.** Nepřiměřená ujednání (§ 1813 - významná nerovnováha; § 1814 demonstrativní seznam) - nepřihlíží se (§ 1815), soud zkoumá **z úřední povinnosti** (SDEU), transparentnost; rozhodčí doložka nepřípustná, prorogace neúčinná (§ 89a o. s. ř.); nekalé obchodní praktiky (§ 4-§ 5b ZOS - klamavé, agresivní, černá listina; klamavé slevy - nejnižší cena za 30 dnů § 12a; falešné recenze; dark patterns), následek: možnost odstoupit (§ 5d ZOS - ověř), pokuta ČOI, nekalá soutěž.
6. **Spotřebitelský úvěr (257/2016 Sb.).** Předsmluvní informace (formulář), **posouzení úvěruschopnosti - bez řádného posouzení je smlouva neplatná (námitka spotřebitele, promlčení) a úročí se jen diskontní sazbou** (§ 86-§ 87 - ověř), RPSN, odstoupení 14 dnů (§ 118), předčasné splacení s omezenou náhradou nákladů (§ 117), limity sankcí za prodlení (§ 122), zajištění (§ 113 - zákaz směnky, nepřiměřené zajištění), zprostředkovatelé, oprávnění ČNB; obrana u finančního arbitra (bezplatně, vykonatelný nález).
7. **Mimosoudní řešení a spory.** ADR u ČOI (§ 20d+ ZOS - 90 dnů, informace na webu podnikatele), finanční arbitr (úvěry, platby, pojištění), ČTÚ (telekomunikace), ERÚ (energie); evropská platforma ODR ukončena (ověř); soud: obecný soud spotřebitele, u přeshraničních smluv fórum spotřebitele (nařízení 1215/2012 čl. 17-19), EPR, předžalobní výzva, náklady u formulářových žalob (§ 14b AT); **hromadné řízení** (179/2024 Sb. - spolek, opt-in, přihlášení nároků); promlčení 3 roky (§ 629).
8. **Zvláštní sektory.** Zájezd (§ 2521+ OZ - změna ceny, odstoupení, pomoc, pojištění CK proti úpadku), letecká doprava (nařízení 261/2004 - kompenzace při zpoždění a zrušení, mimořádné okolnosti, ČOI/ÚCL), energie (změna dodavatele, výpověď, ERÚ), telekomunikace (§ 63 zák. 127/2005 Sb. - závazek max. 24 měsíců, výpověď, automatická prolongace), timeshare, finanční služby na dálku.
9. **Compliance obchodníka.** Obchodní podmínky (inkorporace § 1751, jazyk, změny), informace o zboží a ceně vč. slev, proces objednávky, poučení o odstoupení a formulář, reklamační řád, ADR informace, cookies a obchodní sdělení, recenze, GDPR, sankce ČOI (§ 24 ZOS - ověř výše), audit před spuštěním e-shopu.

## Časté pasti

- Lhůta k odstoupení počítaná od uzavření smlouvy místo od převzetí zboží; přehlédnuté prodloužení při chybějícím poučení.
- Odmítnutí vrácení peněz kvůli rozbalení nebo vyzkoušení - přípustné jen u výjimek § 1837 nebo jako náhrada snížení hodnoty nad rámec vyzkoušení.
- Reklamace „vyřízena" po 30 dnech nebo bez písemného potvrzení - spotřebitel může odstoupit.
- Domněnka vady a 2letá odpovědnost zaměněna se „zárukou 24 měsíců" ze staré úpravy; použití znění před 6. 1. 2023 na novou smlouvu.
- Rozhodčí doložka nebo prorogace uplatněná proti spotřebiteli; nepřiměřené ujednání přehlédnuté, ač soud musí z úřední povinnosti.
- Úvěr bez posouzení úvěruschopnosti vymáhaný v plné výši - námitka neplatnosti a úročení diskontní sazbou.
- Nekalé praktiky řešené jen stížností ČOI bez uplatnění soukromoprávních nároků (a naopak).
- Smíšený účel nákupu (OSVČ) automaticky brán jako nespotřebitelský.
- Odkaz na evropskou platformu ODR v obchodních podmínkách po jejím ukončení.
- „Sleva" počítaná z ceny, která 30 dnů před slevou neplatila (§ 12a ZOS).
- Zájezd × samostatné služby; letecká kompenzace promlčená podle nesprávného práva.
- Doplňování dat převzetí, částek a čísel objednávek z paměti - vždy z dokladů nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co spotřebitel / podnikatel může, do kdy; co poslat a komu).
2. **Kvalifikace** (spotřebitel? kanál? typ smlouvy? datum uzavření a rozhodné znění).
3. **Právní rámec** - OZ / ZOS / 257/2016 / směrnice v aktuálním znění, s odkazy.
4. **Nároky nebo postup** - tabulka: nárok/krok | právní základ | adresát | lhůta | důkaz.
5. **Rizika a alternativy** (ADR, arbitr, hromadné řízení, náklady, dozorový orgán).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. SDEU.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 33 Cdo 1234/2024 - …`, `SDEU - C-260/18 - 03.10.2019`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („ode dne převzetí zboží“, „bez zbytečného odkladu, nejpozději do 14 dnů“, „nepřihlíží se“, „průměrný spotřebitel“).
- Jeden časový řez; znění účinné v den uzavření smlouvy, u praktik v den jednání.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty, domněnky, sazby a limity nikdy z paměti - vždy z aktuálního znění s odkazem a datem účinnosti.
- Mimo CODEXIS jen oficiální zdroje (coi.cz, finarbitr.cz, cnb.cz, ctu.gov.cz, eru.cz, eur-lex) když CODEXIS neodpovídá.
