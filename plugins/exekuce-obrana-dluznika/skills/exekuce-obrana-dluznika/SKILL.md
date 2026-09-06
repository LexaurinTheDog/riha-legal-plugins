---
uuid: 52b7f277-741b-453a-8643-8781e5c870ee
name: exekuce-obrana-dluznika
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Exekuce - obrana povinného ČR"
    summary: "Audit exekučního titulu, návrhy na odklad a zastavení, nezabavitelné minimum a chráněný účet, mobiliární exekuce, nemovitost a SJM, vylučovací žaloby třetích osob, náklady, stížnosti, oddlužení jako východisko."
    examplePrompts:
      - "Klientovi přišlo vyrozumění o zahájení exekuce pro dluh z roku 2012 podle rozhodčího nálezu. Co zkontrolovat a jaké návrhy podat?"
      - "Exekutor zablokoval účet, na který chodí mzda a přídavky na děti. Jak rychle uvolnit prostředky?"
      - "Exekutor sepsal v bytě věci, které patří přítelkyni povinného. Jak je dostat ze soupisu?"
  en:
    displayName: "Czech Enforcement Defence"
    summary: "Auditing the enforcement title, motions to stay and stop, protected minimum and protected account, seizure of movables, real estate and marital property, third-party claims, costs, complaints, debt relief as an exit."
    examplePrompts:
      - "My client received a notice of enforcement for a 2012 debt based on an arbitration award. What to check and which motions to file?"
      - "The bailiff froze an account receiving wages and child benefits. How to release funds quickly?"
      - "The bailiff inventoried items in the flat that belong to the debtor's girlfriend. How to get them off the inventory?"
  sk:
    displayName: "Exekúcia - obrana povinného ČR"
    summary: "Audit exekučného titulu v ČR, návrhy na odklad a zastavenie, nezabaviteľné minimum a chránený účet, mobiliárna exekúcia, nehnuteľnosť a BSM, vylučovacie žaloby tretích osôb, trovy, sťažnosti, oddlženie ako východisko."
    examplePrompts:
      - "Klientovi prišlo upovedomenie o začatí exekúcie pre dlh z roku 2012 podľa rozhodcovského nálezu. Čo skontrolovať a aké návrhy podať?"
      - "Exekútor zablokoval účet, na ktorý chodí mzda a prídavky na deti. Ako rýchlo uvoľniť prostriedky?"
      - "Exekútor spísal v byte veci, ktoré patria priateľke povinného. Ako ich dostať zo súpisu?"
description: Use when the user defends a debtor (povinný), a debtor's spouse or a third party against Czech enforcement, or advises a debtor with multiple debts - exekuce, exekutor, exekuční řád (120/2001 Sb.), výkon rozhodnutí (§ 251+ o. s. ř.), vyrozumění o zahájení exekuce, exekuční příkaz, exekuční titul, rozhodčí nález, promlčení vykonatelného práva, návrh na zastavení exekuce, návrh na odklad, nemajetnost, srážky ze mzdy, nezabavitelná částka, přikázání pohledávky z účtu, chráněný účet, mobiliární exekuce, soupis movitých věcí, vyškrtnutí věci ze soupisu, vylučovací žaloba, obydlí povinného, exekuce na SJM, manžel povinného, náklady exekuce, odměna exekutora, příkaz k úhradě nákladů, splátkový kalendář s exekutorem, centrální evidence exekucí, stížnost na exekutora, daňová exekuce, správní exekuce, oddlužení jako řešení, milostivé léto. Standalone skill - bundles CODEXIS methodology with debtor-defence method; no need to load the general codexis skill.
---

# Exekuce - obrana povinného ČR

Samostatný oborový skill pro obranu dlužníka a třetích osob v exekuci a výkonu rozhodnutí. Pořadí je pevné: **fáze a běžící lhůta → audit titulu → co nesmí být postiženo → návrhy (zastavení / odklad / vyškrtnutí) → náklady → dlouhodobé řešení (dohoda, oddlužení)**. Vymáhání z pohledu věřitele řeší jiný skill.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/120/2001/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf55'`, `cdx-cli get cdx://cz_law/99/1963/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf268'`, `cdx-cli get cdx://cz_law/595/2006/versions`, `cdx-cli search JD --query "zastavení exekuce rozhodčí nález spotřebitel neplatná doložka" --court "Nejvyšší soud" --limit 5`.
- Exekuční řád i o. s. ř. byly opakovaně novelizovány (2021 - chráněný účet, bezvýsledné exekuce, sloučení; 2022 - obydlí a milostivé léto; další změny průběžně). **Lhůty, částky (nezabavitelné minimum, násobky životního minima, limity pro prodej obydlí), sazby odměny a čísla odstavců ověř v aktuálním znění k datu úkonu**; nikdy z paměti. Nezabavitelnou částku počítej výhradně podle aktuálního nařízení vlády a aktuálního životního minima a normativních nákladů.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| EŘ - exekuční řád | 120/2001 Sb. | `cz_law/120/2001` | Exekuční návrh a pověření (§ 37-§ 43a), vyrozumění a dobrovolné plnění (§ 44, § 46), exekuční příkazy (§ 47+), odklad (§ 54), zastavení (§ 55 vč. bezvýsledné exekuce), způsoby provedení (§ 58+), soupis a vyškrtnutí věci (§ 66-§ 68), SJM (§ 42), náklady (§ 87-§ 90), kárná odpovědnost |
| o. s. ř. - výkon rozhodnutí | 99/1963 Sb. | `cz_law/99/1963` | Subsidiárně (§ 52 EŘ): zastavení (§ 268-§ 269), SJM a manžel (§ 262a-§ 262b), vylučovací žaloba (§ 267), srážky ze mzdy (§ 276-§ 302), přikázání pohledávky a chráněný účet (§ 303-§ 311), věci nepodléhající výkonu (§ 321-§ 322), prodej nemovitostí a dražba (§ 335-§ 337h), vyklizení (§ 340+) |
| NV o nezabavitelných částkách | 595/2006 Sb. | `cz_law/595/2006` | Výpočet nezabavitelné částky a hranice plně zabavitelného zbytku |
| Vyhláška o odměně exekutora | 330/2001 Sb. | `cz_law/330/2001` | Odměna, náhrada hotových výdajů, snížení při dobrovolném plnění |
| Vyhláška o centrální evidenci exekucí | 329/2008 Sb. | `cz_law/329/2008` | Zápis a výmaz, dálkový přístup |
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Promlčení vykonatelného práva (§ 640), započítávání plateb (§ 1932-§ 1933), SJM a dluhy (§ 731-§ 732), odpovědnost nezletilých za dluhy (§ 899a) |
| Insolvenční zákon | 182/2006 Sb. | `cz_law/182/2006` | Účinky zahájení na exekuci (§ 109), oddlužení (§ 389+) |
| Daňový řád / správní řád | 280/2009 / 500/2004 Sb. | `cz_law/280/2009`, `cz_law/500/2004` | Daňová exekuce (§ 175+ DŘ - odvolání proti exekučnímu příkazu, zastavení § 181), správní exekuce (§ 103+ SŘ) |
| Zákon o rozhodčím řízení | 216/1994 Sb. | `cz_law/216/1994` | Rozhodčí nálezy jako titul, neplatné spotřebitelské doložky, zrušení nálezu (§ 31) |
| Zákony „milostivé léto" | 286/2021, 214/2022 Sb. a navazující | `cz_law/286/2021`, `cz_law/214/2022` | Historické akce oddlužení příslušenství - ověř, zda probíhá nová |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu zahájení exekuce a k datu úkonu** → `/toc` → `/text?part=`.
2. Judikatura: **NS** senát 20 Cdo (exekuce a výkon rozhodnutí - zastavení pro neplatnou rozhodčí doložku, promlčení, SJM, náklady), **ÚS** (proporcionalita nákladů, ochrana obydlí, spotřebitel v exekuci), **NSS** (daňová exekuce). Ověř datum a novelu.
3. Komentář (`COMMENT`) k pojmům (důvod zastavení „jiný důvod“ § 268 odst. 1 písm. h), nemajetnost, obvyklé vybavení domácnosti); metodiky Exekutorské komory jsou orientace.

## Workflow obrany

1. **Fáze a lhůty.** Vyrozumění o zahájení (§ 44 EŘ) → **30 dnů k dobrovolnému splnění se sníženými náklady** (§ 46 odst. 6 - ověř) a zároveň k podání návrhu na zastavení; exekuční příkazy (mzda, účet, movité věci, nemovitost, řidičský průkaz u výživného) → dražba → skončení. Zjisti datum doručení každé listiny, spisovou značku, exekutora a oprávněného; stáhni výpis z centrální evidence exekucí (všechny exekuce, pořadí).
2. **Audit titulu.** Vykonatelnost (právní moc, doložka), řádné doručení titulu povinnému (fikce, rozsudek pro zmeškání, platební rozkaz doručený na neaktuální adresu → odvolání / návrh na prominutí zmeškání § 58 o. s. ř. + návrh na odklad exekuce), **promlčení vykonatelného práva** (§ 640 OZ - 10 let od právní moci, u starších titulů podle OZ 1964; jen na námitku), rozhodčí nález (spotřebitelská doložka neplatná → zastavení podle § 268 odst. 1 písm. h) o. s. ř. i bez zrušení nálezu - judikatura NS), notářský zápis, správní/daňový titul, exekuce pro pohledávku vzniklou v nezletilosti (§ 899a OZ, zastavení), zánik pohledávky splněním/započtením (§ 268 odst. 1 písm. g)), oprávněný bez aktivní legitimace (postoupení bez doložení).
3. **Návrhy.** **Návrh na zastavení** (§ 55 EŘ - povinný do 15 dnů ode dne, kdy se dozvěděl o důvodu; exekutor vyhoví nebo do 15 dnů postoupí soudu; důvody § 268 o. s. ř. a § 55 EŘ), **návrh na odklad** (§ 54 EŘ - přechodně nepříznivé postavení bez vlastní viny, nebo očekávané zastavení), návrh na zastavení bezvýsledné exekuce (§ 55 odst. 7+ - po 6 letech bez výtěžku, záloha oprávněného - ověř), námitky proti příkazu k úhradě nákladů (§ 88 odst. 3 EŘ - 8 dnů), návrh na vyškrtnutí věci ze soupisu (§ 68 EŘ - do 30 dnů od soupisu, třetí osoba) a vylučovací žaloba (§ 267 o. s. ř.), návrh manžela na zastavení pro majetek mimo SJM nebo dluh nespadající do SJM (§ 262b o. s. ř., § 42 EŘ), odvolání proti rozhodnutí exekutora/soudu 15 dnů.
4. **Co nesmí být postiženo.** Srážky ze mzdy - nezabavitelná částka (NV 595/2006 Sb. + § 278-§ 279 o. s. ř.: základní částka, na vyživované osoby, hranice plně zabavitelného zbytku - vypočti podle aktuálních hodnot), přednostní pohledávky (§ 279 odst. 2), více plátců mzdy (soud určí), dávky a příjmy vyloučené (§ 317 o. s. ř. - ověř výčet: dávky pomoci v hmotné nouzi, příspěvek na bydlení, dávky pěstounské péče…); účet - **chráněný účet** (§ 304c-§ 304e - zřízení bankou na žádost, chráněný příjem z exekučně chráněných zdrojů) a výplata dvojnásobku životního minima (§ 304b), zákaz postižení prostředků z dávek na účtu (prokázat původ); movité věci - § 322 o. s. ř. (obvyklé vybavení domácnosti, zdravotní pomůcky, snubní prsten, zvířata, hotovost do zákonného násobku životního minima, nástroje k výkonu povolání do limitu - ověř); nemovitost - **ochrana obydlí povinného** u nižších pohledávek (§ 66 EŘ - ověř limit a podmínky) a zásada přiměřenosti způsobu exekuce (§ 58 odst. 3 EŘ).
5. **Náklady exekuce.** Odměna exekutora (vyhl. 330/2001 Sb. - procento z vymoženého, minimum, snížení při splnění do 30 dnů od vyrozumění), náhrada výdajů, náklady oprávněného; příkaz k úhradě nákladů a námitky (8 dnů); přezkum proporcionality (ÚS); při zastavení pro nemajetnost náklady nese oprávněný zpravidla; u zastavení z důvodu na straně oprávněného (neplatný titul) náklady oprávněný.
6. **Dohoda a dlouhodobé řešení.** Splátkový kalendář s exekutorem (nezastavuje exekuci, ale odloží dražbu), dohoda s oprávněným o prominutí příslušenství, sloučení exekucí (§ 37 odst. 4 EŘ), milostivé léto (jen v době platné akce - ověř), **oddlužení** (§ 389+ IZ - zahájení insolvenčního řízení blokuje provedení exekuce § 109 odst. 1 písm. c) IZ; podání jen advokátem/notářem/akreditovanou osobou) - odkaž na insolvenční skill; předlužení versus dočasná platební neschopnost.
7. **Dozor a stížnosti.** Stížnost na exekutora Exekutorské komoře / Ministerstvu spravedlnosti (kárná odpovědnost), podnět k dohledu exekučního soudu, náhrada škody za nesprávný úřední postup exekutora (§ 32 EŘ, zákon 82/1998 Sb. - ověř).
8. **Daňová a správní exekuce.** Jiný režim: exekuční příkaz správce daně (§ 178 DŘ) - odvolání 15 dnů bez odkladného účinku, námitka (§ 159 DŘ), zastavení (§ 181 DŘ), posečkání (§ 156 DŘ) a splátky, prominutí příslušenství (§ 259+ DŘ); správní exekuce (§ 103+ SŘ).

## Časté pasti

- Zmeškání 30 dnů od vyrozumění - ztráta snížených nákladů a dražší exekuce.
- Návrh na zastavení podaný po 15 dnech od dozvědění - exekutor ho může odmítnout; zbývá jen zastavení z úřední povinnosti.
- Rozsudek pro zmeškání nebo platební rozkaz doručený fikcí na starou adresu - řešit v nalézacím řízení (odvolání, prominutí zmeškání) souběžně s odkladem, ne jen v exekuci.
- Promlčení titulu neuplatněné námitkou - soud ho nezkoumá sám.
- Rozhodčí nález brán jako nedotknutelný - u spotřebitelských doložek zastavení exekuce.
- Nezabavitelná částka spočtená ze zastaralých hodnot nebo bez vyživovaných osob; více exekucí u více plátců bez určení soudem.
- Chráněný účet nezřízen - dávky a zbytek mzdy zablokovány; prostředky z dávek na běžném účtu bez prokázání původu.
- Soupis věcí třetí osoby bez včasného návrhu na vyškrtnutí (30 dnů) - zbývá jen vylučovací žaloba a věci mohou být prodány.
- Manžel povinného nereaguje na exekuci na SJM nebo na jeho výlučný majetek - ztráta obrany podle § 262b.
- Splátkový kalendář s exekutorem považován za zastavení - dražba jen odložena, náklady rostou.
- Oddlužení navrhované bez kontroly poctivého záměru a bez akreditované osoby / advokáta.
- Milostivé léto uváděné jako dostupné bez ověření, zda aktuálně probíhá.
- Daňová exekuce bráněna návrhy podle exekučního řádu - jiné lhůty a prostředky.
- Doplňování spisových značek, částek a dat doručení z paměti - vždy z listin, CEE nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (jaký návrh, komu, do kdy; co zaplatit / nezaplatit).
2. **Fáze, titul a jeho vady.**
3. **Právní rámec** - EŘ / o. s. ř. / NV v aktuálním znění, s odkazy; výpočet nezabavitelné částky s uvedením použitých hodnot a jejich zdroje.
4. **Návrhy a postup** - tabulka: úkon | právní základ | adresát | lhůta | očekávaný účinek.
5. **Rizika a alternativy** (dohoda, splátky, oddlužení, náklady).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 20 Cdo 1234/2024 - …`, `ÚS - II. ÚS 123/25 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do 15 dnů ode dne, kdy se dozvěděl“, „do 30 dnů od doručení vyrozumění“, „nemohl-li bez své viny“).
- Jeden časový řez; u částek uveď datum účinnosti použitých hodnot.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Nezabavitelné částky, násobky životního minima, limity a sazby nikdy z paměti - vždy z aktuálního nařízení vlády a zákona s odkazem a datem.
- Mimo CODEXIS jen oficiální zdroje (ekcr.cz, justice.cz, CEE, mpsv.cz pro životní minimum) když CODEXIS neodpovídá; nikdy neradit zatajování majetku ani maření exekuce (§ 337 TZ).
