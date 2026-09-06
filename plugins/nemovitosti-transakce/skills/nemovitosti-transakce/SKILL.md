---
uuid: 55665ffa-e806-496c-b152-e679f7cce014
name: nemovitosti-transakce
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Nemovitosti a realitní transakce ČR"
    summary: "Převody nemovitostí od prověrky listu vlastnictví po vklad - kupní smlouva, úschova, zástavní a předkupní práva, spoluvlastnictví, SVJ, nájem, daně."
    examplePrompts:
      - "Připrav postup prodeje ideální poloviny domu, na kterém vázne hypotéka, včetně podmínek úschovy."
      - "Kupujeme chatu na cizím pozemku. Kdo má předkupní právo a jak dlouho trvá nabídka?"
      - "Jaké jsou náležitosti návrhu na vklad a co se stane, když katastr zjistí vadu?"
  en:
    displayName: "Czech Real Estate Transactions"
    summary: "Property transfers from title check to registration - purchase contract, escrow, liens and pre-emption rights, co-ownership, HOA, leases, taxes."
    examplePrompts:
      - "Prepare the procedure for selling a half share of a mortgaged house, including escrow conditions."
      - "We are buying a cottage on someone else's land. Who holds a pre-emption right and how long does the offer run?"
      - "What are the requirements of a cadastral registration application and what if the registry finds a defect?"
  sk:
    displayName: "Nehnuteľnosti a realitné transakcie ČR"
    summary: "Prevody nehnuteľností v ČR od previerky listu vlastníctva po vklad - kúpna zmluva, úschova, záložné a predkupné práva, spoluvlastníctvo, SVJ, nájom, dane."
    examplePrompts:
      - "Priprav postup predaja ideálnej polovice domu, na ktorom viazne hypotéka, vrátane podmienok úschovy."
      - "Kupujeme chatu na cudzom pozemku. Kto má predkupné právo a ako dlho trvá ponuka?"
      - "Aké sú náležitosti návrhu na vklad a čo sa stane, keď kataster zistí vadu?"
description: Use when the user's matter involves Czech real estate - koupě, prodej, převod nemovitosti, kupní smlouva, smlouva o smlouvě budoucí, rezervační smlouva, advokátní úschova, návrh na vklad, katastr nemovitostí (256/2013 Sb.), list vlastnictví, plomba, zástavní právo, hypotéka, výmaz zástavy, věcné břemeno, služebnost, předkupní právo (spoluvlastníci, stavba na cizím pozemku § 3056, obec), spoluvlastnictví, ideální podíl, SJM, bytová jednotka, SVJ, prohlášení vlastníka, právo stavby, nájem bytu / prostor sloužících podnikání, pacht, developerská smlouva, PENB, daň z příjmů při prodeji, daň z nemovitých věcí, DPH u nemovitostí, realitní zprostředkování (39/2020 Sb.), AML identifikace při úschově. Standalone skill - bundles CODEXIS methodology with real-estate transaction method; no need to load the general codexis skill.
---

# Nemovitosti a realitní transakce ČR

Samostatný oborový skill pro převody a užívání nemovitostí. Vede transakci od prověrky listu vlastnictví po vklad a výplatu úschovy a hlídá pořadí úkonů, na kterém převody nejčastěji selhávají.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2128'`, `cdx-cli get cdx://cz_law/256/2013/versions`, `cdx-cli search JD --query "předkupní právo stavba pozemek 3056" --court "Nejvyšší soud" --limit 5`.
- Lhůty, poplatky, daňové testy a hranice **vždy ověř v aktuálním znění** - nikdy z paměti.
- Údaje z katastru (vlastník, zatížení, plomby) čerpej z aktuálního výpisu LV nebo z katastrálního doplňku, ne z tvrzení stran; CODEXIS katastr neobsahuje.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Věci a součásti (§ 498-§ 509), nabytí zápisem (§ 1099-§ 1105), dobrá víra v katastr (§ 980-§ 986), spoluvlastnictví (§ 1115+), bytové spoluvlastnictví (§ 1158+), právo stavby (§ 1240+), věcná břemena (§ 1257+), zástavní právo (§ 1309+), koupě nemovité věci (§ 2128-§ 2131), předkupní právo (§ 2140-§ 2149, § 3056), nájem (§ 2201+, byt § 2235+), pacht (§ 2332+), SJM (§ 708+) |
| Katastrální zákon | 256/2013 Sb. | `cz_law/256/2013` | Vklad, záznam, poznámka, plomba, ochranná lhůta, náležitosti listin, ověřené podpisy |
| Katastrální vyhláška | 357/2013 Sb. | `cz_law/357/2013` | Formuláře, náležitosti návrhu na vklad |
| Zákon o advokacii | 85/1996 Sb. | `cz_law/85/1996` | Advokátní úschova (§ 56a), prohlášení o pravosti podpisu (§ 25a) |
| AML zákon | 253/2008 Sb. | `cz_law/253/2008` | Identifikace a kontrola klienta u úschovy a realitní činnosti (údaje § 5) |
| Zákon o realitním zprostředkování | 39/2020 Sb. | `cz_law/39/2020` | Rezervační a zprostředkovatelské smlouvy, úschova u RK |
| Zákon o hospodaření energií | 406/2000 Sb. | `cz_law/406/2000` | PENB při prodeji a pronájmu (§ 7a) |
| ZDP / ZDPH / daň z nemovitých věcí | 586/1992 / 235/2004 / 338/1992 Sb. | `cz_law/586/1992`, `cz_law/235/2004`, `cz_law/338/1992` | Osvobození prodeje (§ 4 ZDP), DPH u nemovitostí (§ 56 ZDPH), daňové přiznání nového vlastníka |

Daň z nabytí nemovitých věcí byla zrušena zákonem 386/2020 Sb. - nikdy ji nepočítej.

## Rešeršní strategie

1. **Paragraf první** (OZ, katastrální zákon) → `/versions` → `/toc` → `/text?part=`. U předkupního práva a spoluvlastnictví pozor na novelu 163/2020 Sb. (zákonné předkupní právo spoluvlastníků od 1. 7. 2020 zúženo) - vždy ověř znění k datu.
2. **Judikatura NS** k nemovitostem: senát 22 Cdo (věcná práva, spoluvlastnictví, neoprávněná stavba), 26 Cdo (nájem), 33 Cdo (kupní smlouva, vady), 21 Cdo (zástavní právo). Filtr `--court "Nejvyšší soud"`.
3. **Komentář** k výkladu § 3056, § 1124, § 2128, § 984; **vzory** (`VS`) jako kostru kupní smlouvy a úschovy.

## Workflow transakce

1. **Předmět.** Z listu vlastnictví: parcely, budovy (součást pozemku × samostatná stavba § 3054-§ 3061), jednotky (zákon 72/1994 × OZ 2012), podíly, příslušenství. Zkontroluj soulad LV se skutečným stavem (černé stavby, přístavby, přístup k pozemku).
2. **Vlastník a zatížení.** Vlastník, SJM, plomby, zástavní práva, věcná břemena, exekuce, poznámky spornosti, předkupní práva, nájmy (přecházejí na nabyvatele § 2221). Insolvenci prodávajícího ověř v ISIR, exekuce v centrální evidenci exekucí.
3. **Předkupní práva.** Spoluvlastníci (§ 1124 v aktuálním znění - jen zbytkové případy), vlastník pozemku × stavby (§ 3056 - věcné právo, nabídka až po uzavření smlouvy, lhůta k přijetí § 2148 odst. 1), obec/stát podle zvláštních zákonů, smluvní předkupní právo zapsané v katastru. Nesprávný adresát nabídky = předkupní právo nezaniká.
4. **Strany.** Svéprávnost, SJM (souhlas manžela § 714, jinak relativní neplatnost), právnická osoba - jednající osoba z aktuálního výpisu z rejstříku k datu podpisu, cizinci (doklady, ověření podpisu, apostila), zastoupení plnou mocí (s ověřeným podpisem pro vklad). AML identifikace u úschovy před přijetím peněz.
5. **Struktura obchodu.** Rezervační smlouva (39/2020 Sb.) → smlouva o smlouvě budoucí / kupní smlouva → úschova (advokát § 56a, notář, banka) → návrh na vklad → výplata. Podmínky výplaty vázat na **vklad vlastnického práva**, případně na výmaz zástavy; nikdy cirkulárně (výmaz zástavy věřitel provede až po zaplacení).
6. **Zástavní právo prodávajícího.** Vyžádat vyčíslení dluhu a souhlas s výmazem; při převodu podílu zástavní právo sleduje podíl - správné pořadí: 1) vklad vlastnického práva kupujícího, 2) výmaz zástavy z podílu; výplatu bance z úschovy nekondicionovat výmazem.
7. **Vklad.** Návrh na vklad na formuláři (vyhl. 357/2013), listiny s úředně ověřenými podpisy (jen jeden stejnopis pro katastr; doložky se počítají podle podpisů, ne dokumentů), správní poplatek, plomba, ochranná lhůta (§ 18 kat. zákona - ověř délku), účinky vkladu zpětně k okamžiku podání (§ 10). Vada listiny → zamítnutí, ne výzva k opravě - kontroluj před podáním.
8. **Po vkladu.** Předání, přepis energií, daňové přiznání k dani z nemovitých věcí novým vlastníkem, ohlášení SVJ/pronajímateli, PENB předán.
9. **Daně a poplatky.** Daň z příjmů prodávajícího (§ 4 odst. 1 ZDP - časové testy, bydliště; ověř), DPH (§ 56 ZDPH - lhůta od kolaudace, volba zdanění), daň z nemovitých věcí, správní poplatek za vklad. Daň z nabytí neexistuje.

## Kupní smlouva - kontrolní seznam

- Přesná specifikace nemovitosti podle LV (parc. č., k. ú., LV, výměra, druh, č. p./č. e., jednotka + podíl na společných částech).
- Kupní cena, splatnost, úschova, případné DPH; zápočet rezervačního poplatku.
- Prohlášení prodávajícího (bez dluhů, bez nájmů, bez sporů, technický stav), sankce za nepravdivost.
- Vady: oznámení skrytých vad (§ 2129 odst. 2 - pětiletá lhůta), vzdání se práv z vad jako vzdání se práva kupujícího (§ 1916 odst. 2).
- Nebezpečí škody, předání, vyklizení, stav měřidel.
- Odstoupení a vypořádání při nezavkladování, kdo podává návrh na vklad, plná moc k opravám návrhu.
- Podpisy, ověření, počet vyhotovení, doložka o registru smluv u veřejného subjektu.

## Časté pasti

- Počítání daně z nabytí nemovitých věcí (zrušena od roku 2020).
- Předkupní právo spoluvlastníků citované podle znění před 1. 7. 2020.
- Tříměsíční lhůta k přijetí nabídky citovaná jako § 2148 odst. 2 - správně **odst. 1**; nabídka až po podpisu kupní smlouvy, ne před.
- Ústní ujednání o zpětné koupi nemovitosti je platné (§ 2128 odst. 1 nevyžaduje formu pro zpětnou koupi) - bránit se absencí zápisu v katastru, ne formou; past § 2137 (10 let).
- Výplata prodávajícímu podmíněná výmazem zástavy, kterou banka vymaže až po výplatě - obchod se zasekne.
- Vklad podán na základě listiny bez ověřených podpisů nebo se starým jednatelem prodávající společnosti.
- Stavba na cizím pozemku prodávaná bez řešení práva k pozemku (podnájem, nájem, právo stavby) - kupující nemá právo pozemek užívat.
- Nájemní vztahy „přecházejí“ na kupujícího (§ 2221) - kontrola nájemních smluv před podpisem.
- PENB: vzory často citují neplatné odstavce § 7a; zproštění se lze jen v zákonem uvedených případech.
- Doplňování vlastníka pozemku z tvrzení realitní kanceláře místo z výpisu LV.

## Struktura výstupu

1. **Závěr** - lze obchod uskutečnit / za jakých podmínek / co blokuje.
2. **Harmonogram** krok za krokem s pořadím úkonů (podpis → úschova → vklad → výmaz → výplata → předání) a odhadem lhůt.
3. **Rizika a jejich ošetření** (předkupní práva, zástavy, SJM, insolvence, daně).
4. **Seznam podkladů** k vyžádání (LV, nabývací titul, výpis z rejstříku, PENB, potvrzení bezdlužnosti SVJ, vyčíslení dluhu banky, doklady totožnosti pro AML).
5. **Právní rámec a judikatura** - ověřené odkazy.
6. **Otázky na klienta a placeholdery** `[DOPLNIT]` pro každý neověřený údaj.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 22 Cdo 2886/2023 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („ode dne doručení nabídky“, „nejpozději“, „k okamžiku podání“).
- Jeden časový řez pro všechny citované paragrafy.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Údaje o osobách, firmách a nemovitostech nikdy nevymýšlet - jen výpis LV, veřejný rejstřík, ARES nebo `[DOPLNIT]`.
- Web jen pro oficiální zdroje (ČÚZK, justice.cz, ISIR, finanční správa), když CODEXIS neodpovídá.
