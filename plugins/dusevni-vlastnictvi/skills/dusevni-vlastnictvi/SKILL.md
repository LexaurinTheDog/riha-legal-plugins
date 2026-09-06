---
uuid: 39e7f908-07ff-4776-bc2c-06c9f7057326
name: dusevni-vlastnictvi
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Duševní vlastnictví ČR"
    summary: "Autorské právo a software, zaměstnanecká díla a díla na objednávku, licence, ochranné známky, patenty, vzory, domény, obchodní tajemství, vymáhání a řízení před ÚPV."
    examplePrompts:
      - "Externí vývojář nám napsal software bez licenční smlouvy. Kdo je vlastníkem a co můžeme s kódem dělat?"
      - "Konkurent začal používat logo zaměnitelné s naší ochrannou známkou. Jaké nároky máme a jak rychle lze zasáhnout?"
      - "Připrav strategii registrace ochranné známky pro nový produkt v ČR a EU včetně rešerše a tříd."
  en:
    displayName: "Czech Intellectual Property"
    summary: "Copyright and software, employee and commissioned works, licences, trade marks, patents, designs, domains, trade secrets, enforcement and ÚPV proceedings."
    examplePrompts:
      - "An external developer wrote our software without a licence agreement. Who owns it and what can we do with the code?"
      - "A competitor started using a logo confusingly similar to our trade mark. Which claims do we have and how fast can we act?"
      - "Prepare a trade mark registration strategy for a new product in CZ and the EU including clearance search and classes."
  sk:
    displayName: "Duševné vlastníctvo ČR"
    summary: "Autorské právo a softvér, zamestnanecké diela a diela na objednávku, licencie, ochranné známky, patenty, vzory, domény, obchodné tajomstvo, vymáhanie a konanie pred ÚPV v ČR."
    examplePrompts:
      - "Externý vývojár nám napísal softvér bez licenčnej zmluvy. Kto je vlastníkom a čo môžeme s kódom robiť?"
      - "Konkurent začal používať logo zameniteľné s našou ochrannou známkou. Aké nároky máme a ako rýchlo možno zasiahnuť?"
      - "Priprav stratégiu registrácie ochrannej známky pre nový produkt v ČR a EÚ vrátane rešerše a tried."
description: Use when the user's matter involves Czech or EU intellectual property - autorské právo, autorský zákon (121/2000 Sb.), dílo, autor, spoluautoři, zaměstnanecké dílo, dílo na objednávku, software, počítačový program, databáze, fotografie, licenční smlouva (§ 2358+ OZ), podlicence, výhradní licence, odměna, kolektivní správa, OSA, DILIA, INTERGRAM, ochranná známka (441/2003 Sb., EUTM), přihláška, rešerše, třídy, námitky, zrušení, neplatnost, užívání známky, patent, vynález, užitný vzor, průmyslový vzor, označení původu, ÚPV, EUIPO, EPO, obchodní firma, doménové jméno, obchodní tajemství, know-how, porušení práv, padělky, celní opatření, bezdůvodné obohacení dvojnásobek licence, předběžné opatření, zajištění důkazů, vymáhání práv z průmyslového vlastnictví (221/2006 Sb.), umělá inteligence a autorství, text and data mining, parazitování, nebezpečí záměny. Standalone skill - bundles CODEXIS methodology with IP-practice method; no need to load the general codexis skill.
---

# Duševní vlastnictví ČR

Samostatný oborový skill pro autorské právo, průmyslová práva a jejich vymáhání. První krok je vždy **klasifikace předmětu ochrany a nositele práv** - stejný obrázek může být dílem, ochrannou známkou i průmyslovým vzorem a každý režim má jiného vlastníka, jinou dobu ochrany a jiný soud.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/121/2000/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf58'`, `cdx-cli get cdx://cz_law/441/2003/versions`, `cdx-cli search JD --query "dílo na objednávku licence účel smlouvy 61" --court "Nejvyšší soud" --limit 5`, `cdx-cli search EU --query "nařízení 2017/1001 ochranná známka EU" --limit 5`.
- Autorský zákon byl zásadně novelizován v roce 2023 (implementace směrnice DSM - text and data mining, platformy, tiskové publikace) a známkový zákon v roce 2019. **Každý §, lhůtu, dobu ochrany a poplatek ověř v aktuálním znění**, nikdy z paměti. Stav rejstříků (ÚPV, EUIPO, WIPO, CZ.NIC) čerpej z rejstříků, ne z CODEXIS.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Autorský zákon | 121/2000 Sb. | `cz_law/121/2000` | Dílo (§ 2), autor a spoluautoři (§ 5-§ 8), práva (§ 10-§ 12), trvání (§ 27), výjimky (§ 29-§ 39d vč. citace, parodie, TDM), nároky (§ 40), zaměstnanecké dílo (§ 58), dílo na objednávku (§ 61), software (§ 65-§ 66), databáze (§ 88+), kolektivní správa (§ 95+) |
| OZ - licence a nekalá soutěž | 89/2012 Sb. | `cz_law/89/2012` | Licenční smlouva (§ 2358-§ 2389 - forma, výhradnost, podlicence, odměna, odstoupení), obchodní firma (§ 423+), obchodní tajemství (§ 504), nekalá soutěž (§ 2976-§ 2990) |
| Zákon o ochranných známkách | 441/2003 Sb. | `cz_law/441/2003` | Způsobilost a důvody zamítnutí, práva ze známky, vyčerpání, užívání a zrušení, námitky, neplatnost, řízení před ÚPV |
| Zákon o vymáhání práv z průmyslového vlastnictví | 221/2006 Sb. | `cz_law/221/2006` | Nároky (zdržení, odstranění, informace, náhrada, bezdůvodné obohacení, zadostiučinění), výlučná příslušnost soudu |
| Patentový zákon | 527/1990 Sb. | `cz_law/527/1990` | Vynálezy, patenty, licence, nucené licence |
| Zákon o užitných vzorech | 478/1992 Sb. | `cz_law/478/1992` | Užitné vzory - bez věcného průzkumu |
| Zákon o ochraně průmyslových vzorů | 207/2000 Sb. | `cz_law/207/2000` | Průmyslové vzory |
| Nařízení o ochranné známce EU / o průmyslových vzorech Společenství | (EU) 2017/1001 / (ES) 6/2002 | zdroj `EU` | EUTM, RCD, nezapsaný vzor Společenství |
| Směrnice DSM | (EU) 2019/790 | zdroj `EU` | Výjimky TDM, platformy, tiskové publikace |
| Nařízení o celním vymáhání práv | (EU) 608/2013 | zdroj `EU` | Zadržení padělků celní správou |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Porušení práv k ochranné známce (§ 268), průmyslovým právům (§ 269), autorského práva (§ 270) |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Příslušnost (§ 9 odst. 2), předběžné opatření a jistota (§ 74-§ 77a), zajištění důkazu (§ 78b+) |

## Rešeršní strategie

1. Paragraf známý → `/versions` (pozor na novelu AutZ 2023 a ZOZ 2019) → `/toc` → `/text?part=`; unijní předpisy ze zdroje `EU`.
2. Judikatura: **NS** (`--court "Nejvyšší soud"`, senáty 30 Cdo / 23 Cdo - autorské právo, známky, nekalá soutěž), **Vrchní soud v Praze** (odvolací pro Městský soud v Praze), **NSS** a **Městský soud v Praze** (správní žaloby proti ÚPV), **SDEU** (`ES` - výklad směrnic a nařízení: Infopaix, Cofemel, Sky/SkyKick, Louboutin). Ověř, zda rozhodnutí nevychází ze znění před novelou.
3. Komentář (`COMMENT`) k pojmům (jedinečný výsledek tvůrčí činnosti, účel smlouvy u díla na objednávku, rozlišovací způsobilost); metodiky ÚPV jsou administrativní výklad.

## Workflow

1. **Klasifikace předmětu.** Autorské dílo (§ 2 AutZ - jedinečnost; fotografie a software chráněny i bez jedinečnosti) × vynález / užitný vzor × průmyslový vzor × ochranná známka × obchodní firma × doména × obchodní tajemství / know-how (§ 504 OZ - vyžaduje opatření k utajení) × databáze. Jeden předmět může spadat do více režimů - řeš každý zvlášť.
2. **Nositel práv.** Autor je vždy fyzická osoba (§ 5); zaměstnanecké dílo - majetková práva vykonává zaměstnavatel (§ 58, i software, i po skončení PP - ověř podmínky); dílo na objednávku - objednatel má licenci jen **k účelu smlouvy** (§ 61, domněnka úzká); spoluautoři (§ 8 - nakládání jednomyslně, díla souborná × spojená); přihlašovatel / majitel průmyslového práva podle rejstříku; výstupy AI bez lidského tvůrčího vkladu nejsou dílem. Ověř řetězec titulů až k původnímu autorovi.
3. **Rozsah a trvání.** Autorská majetková práva 70 let po smrti (§ 27); ochranná známka 10 let s obnovou; patent 20 let; užitný vzor 10 let; průmyslový vzor 25 let; nezapsaný vzor Společenství 3 roky - vše ověř. Výjimky a omezení (§ 29-§ 39d AutZ - třístupňový test, citace, osobní užití, parodie, TDM s výhradou), vyčerpání práv.
4. **Titul užití.** Licence (§ 2358+ OZ): písemně u výhradní licence a u práv zapsaných v rejstříku (ověř § 2358 odst. 2), rozsah (způsob, území, čas, množství), výhradnost, podlicence a postoupení jen se souhlasem, odměna (i podíl z výnosů), povinnost licenci využít u výhradní (§ 2375 odstoupení), zápis licence do rejstříku ÚPV pro účinky vůči třetím osobám; autorská majetková práva jsou nepřevoditelná - jen licence (§ 26); průmyslová práva převoditelná písemnou smlouvou se zápisem. Zaměstnanecké a objednané dílo řešit smluvně předem (rozšíření § 61, postoupení práva výkonu § 58 odst. 1).
5. **Registrace průmyslových práv.** Rešerše před přihláškou (ÚPV, TMview, Espacenet, DesignView), třídy niceské klasifikace, absolutní × relativní důvody zamítnutí, přihláška (ÚPV / EUIPO / WIPO), zveřejnění, **námitky ve lhůtě od zveřejnění** (ověř), připomínky, zápis, obnova, povinnost užívání (zrušení pro neužívání po 5 letech - ověř), řízení o zrušení/neplatnosti, rozklad, správní žaloba (Městský soud v Praze), kasační stížnost.
6. **Porušení a vymáhání.** Nároky (§ 40 AutZ, § 4-§ 5 zák. 221/2006 Sb., § 2988 OZ): zdržení, odstranění (stažení, zničení), informace o původu a distribuci, náhrada škody, **bezdůvodné obohacení ve výši dvojnásobku obvyklé licenční odměny** (ověř podmínky), přiměřené zadostiučinění, zveřejnění rozsudku; předběžné opatření s jistotou (§ 75b o. s. ř.), zajištění důkazu a předmětu (§ 78b+), celní opatření (nařízení 608/2013), ADR pro domény .cz (CZ.NIC) a .eu, trestní oznámení (§ 268-§ 270 TZ) subsidiárně. Příslušnost: spory z průmyslového vlastnictví a nekalé soutěže **Městský soud v Praze / krajské soudy** (§ 9 odst. 2 o. s. ř., § 6 zák. 221/2006 Sb. - ověř), EUTM soud = Městský soud v Praze.
7. **Obrana žalovaného.** Neplatnost / zrušení známky (neužívání, nedostatek rozlišovací způsobilosti, zlá víra), vyčerpání práv, výjimky z autorského práva, nezávislá tvorba u software, popis × funkce (ochrana kódu, ne myšlenky § 65 odst. 2), promlčení majetkových nároků (§ 629 OZ), starší právo (nezapsané označení, obchodní firma), koexistence.
8. **Smluvní a compliance vrstva.** IP audit, smlouvy s vývojáři a agenturami (postoupení výkonu práv, licence, escrow, open source licence a jejich kompatibilita), NDA a obchodní tajemství, ochrana AI datasetů (TDM výhrada), kolektivní správa (OSA, DILIA, INTERGRAM - divadelní provozování mimo kolektivní správu), franchising a merchandising.

## Časté pasti

- „Koupili jsme software, tak je náš" - bez smlouvy má objednatel jen licenci k účelu (§ 61), zdrojový kód a další užití zůstávají autorovi.
- Převod autorských práv ve smlouvě - nepřevoditelná, platí jen jako licence; průmyslová práva naopak převést lze.
- Výhradní licence uzavřená ústně nebo e-mailem bez podpisu - forma (ověř § 2358 odst. 2).
- Ochranná známka neužívaná 5 let - návrh na zrušení protistranou shodí celou žalobu.
- Zapomenutá obnova známky / patentu nebo nezaplacený udržovací poplatek - zánik práva.
- Přihláška bez rešerše - námitky starších majitelů a zlá víra.
- Doména zaměněná s ochrannou známkou - registrace domény nezakládá právo k označení.
- Obchodní tajemství bez interních opatření k utajení - nechráněno (§ 504 OZ).
- Výstup generativní AI prezentovaný jako autorské dílo klienta; trénink na chráněných datech bez kontroly TDM výhrady.
- Zaměstnanecké dílo vytvořené mimo pracovní úkoly nebo OSVČ „zaměstnancem" - režim § 58 se nepoužije.
- Žaloba z průmyslového vlastnictví u okresního soudu - nepříslušný.
- Doplňování čísel zápisů, tříd a dat priority z paměti - vždy z rejstříku nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší krok** (kdo je nositelem, co lze / nelze, do kdy - námitky, předběžné opatření, obnova).
2. **Klasifikace předmětu a řetězec titulů.**
3. **Právní rámec** - AutZ / ZOZ / OZ / unijní předpisy v aktuálním znění, s odkazy.
4. **Nároky nebo postup registrace** - tabulka: nárok/krok | právní základ | adresát/orgán | lhůta | poplatek.
5. **Rizika a obrana protistrany** (neplatnost, neužívání, výjimky, promlčení).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. SDEU.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 30 Cdo 1234/2024 - …`, `SDEU - C-683/17 - 12.09.2019`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („k účelu vyplývajícímu ze smlouvy“, „nepřetržitě po dobu pěti let“, „dvojnásobek odměny, která by byla obvyklá“).
- Jeden časový řez; u licencí a děl znění účinné v den vzniku díla / uzavření smlouvy.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Stav zápisů výhradně z rejstříků (upv.gov.cz, euipo.europa.eu, wipo.int, nic.cz); mimo CODEXIS jen oficiální zdroje.
- Doby ochrany, lhůty, poplatky a násobky nikdy z paměti - vždy z aktuálního znění s odkazem.
