---
uuid: 87ba06bb-dbca-425b-a949-e59074af597d
name: pojistne-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Pojistné právo ČR"
    summary: "Pojistná smlouva podle OZ, předsmluvní povinnosti a pravdivé odpovědi, lhůty likvidace, odmítnutí a snížení plnění, povinné ručení a garanční fond, majetkové, odpovědnostní, životní a cestovní pojištění, distribuce pojištění, ombudsman a finanční arbitr, promlčení."
    examplePrompts:
      - "Pojišťovna odmítla plnění z pojištění domácnosti, protože klient při sjednání neuvedl dřívější škodu. Je odmítnutí oprávněné a co lze namítat?"
      - "Po dopravní nehodě pojišťovna viníka krátí náhradu za totální škodu o amortizaci a neplatí náhradní vozidlo. Jaké nároky má poškozený a v jakých lhůtách?"
      - "Klient dostal výzvu ČKP k úhradě příspěvku za nepojištěné vozidlo, které měl v depozitu. Jak se bránit?"
  en:
    displayName: "Czech Insurance Law"
    summary: "Insurance contract under the Civil Code, pre-contractual duties and disclosure, claims handling deadlines, refusal and reduction of indemnity, motor third-party liability and the guarantee fund, property, liability, life and travel insurance, distribution rules, ombudsman and financial arbiter, limitation."
    examplePrompts:
      - "The insurer refused a household claim because my client failed to disclose an earlier loss when contracting. Is the refusal justified and what can we argue?"
      - "After a car accident the liable driver's insurer reduces the total-loss indemnity for depreciation and refuses a replacement car. What can the victim claim and within what deadlines?"
      - "My client received a demand from the Czech Insurers' Bureau for a contribution for an uninsured vehicle that was deregistered. How to defend?"
  sk:
    displayName: "Poistné právo ČR"
    summary: "Poistná zmluva podľa OZ, predzmluvné povinnosti a pravdivé odpovede, lehoty likvidácie, odmietnutie a zníženie plnenia, povinné zmluvné poistenie a garančný fond, majetkové, zodpovednostné, životné a cestovné poistenie, distribúcia poistenia, ombudsman a finančný arbiter, premlčanie."
    examplePrompts:
      - "Poisťovňa odmietla plnenie z poistenia domácnosti, lebo klient pri dojednaní neuviedol skoršiu škodu. Je odmietnutie oprávnené a čo možno namietať?"
      - "Po dopravnej nehode poisťovňa vinníka kráti náhradu za totálnu škodu o amortizáciu a neplatí náhradné vozidlo. Aké nároky má poškodený a v akých lehotách?"
      - "Klient dostal výzvu ČKP na úhradu príspevku za nepoistené vozidlo, ktoré mal v depozite. Ako sa brániť?"
description: Use when the user's matter involves an insurance relationship in the Czech Republic - pojištění, pojistná smlouva, pojistitel, pojistník, pojištěný, pojistné podmínky, pojistná událost, pojistné plnění, likvidace pojistné události, lhůta tři měsíce, odmítnutí plnění, snížení plnění, hrubá nedbalost, porušení povinnosti pojistníka, pravdivé odpovědi, zatajení, odstoupení pojistitele, výpověď pojištění, zánik pojištění, nezaplacení pojistného, podpojištění, pojištění majetku, havarijní pojištění, totální škoda, amortizace, pojištění odpovědnosti, profesní odpovědnost, povinné ručení, zákon 30/2024 Sb., Česká kancelář pojistitelů, garanční fond, příspěvek za nepojištěné vozidlo, regres pojistitele, životní pojištění, úrazové pojištění, cestovní pojištění, pojišťovací zprostředkovatel, distribuce pojištění (170/2018 Sb.), ombudsman ČAP, finanční arbitr, promlčení pojistného plnění. Standalone skill - bundles CODEXIS methodology with insurance-practice method; no need to load the general codexis skill.
---

# Pojistné právo ČR

Samostatný oborový skill pro spory z pojištění a poradenství při sjednávání. Základní reflex: **pojistné podmínky a dotazník jsou součástí smlouvy** - většina sporů se rozhoduje na výlukách, na tom, co pojistník při sjednání uvedl, a na tom, zda pojistitel snížil, nebo odmítl plnění v mezích zákona (snížení musí být přiměřené vlivu porušení, odmítnutí jen při zatajení rozhodné skutečnosti). Druhý reflex: **lhůty běží proti oběma** - pojistitel musí skončit šetření do tří měsíců, oprávněná osoba má promlčení plnění tři roky s ročním odkladem od pojistné události.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2758'`, `cdx-cli get cdx://cz_law/30/2024/versions`, `cdx-cli search JD --query "snížení pojistného plnění porušení povinnosti pojistníka přiměřenost" --court "Nejvyšší soud" --limit 5`, `cdx-cli search JD --query "totální škoda vozidla obvyklá cena amortizace pojistitel" --court "Nejvyšší soud" --limit 5`.
- Povinné ručení má nový zákon **30/2024 Sb.** (nahradil 168/1999 Sb.; limity plnění, rozšíření na další vozidla, provozovatel × vlastník) - u nehod před jeho účinností platí starý zákon; **datum pojistné události určuje režim**. Limity, lhůty, sazby příspěvků ČKP a výše pokut **ověř v aktuálním znění**; nikdy z paměti. Smlouvy uzavřené před 1. 1. 2014 se řídí zákonem o pojistné smlouvě 37/2004 Sb. (§ 3028 OZ - ověř přechodné ustanovení).

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Občanský zákoník - pojištění | 89/2012 Sb. | `cz_law/89/2012` | Pojistná smlouva (§ 2758-§ 2872): forma a podmínky (§ 2758-§ 2760), pojistný zájem (§ 2761-§ 2765), předsmluvní dotazy a pravdivost (§ 2788-§ 2789), následky porušení - odstoupení a odmítnutí (§ 2808-§ 2809), zánik (§ 2802-§ 2811: nezaplacení pojistného § 2804, výpověď § 2805-§ 2807), šetření a lhůty (§ 2796-§ 2798), snížení plnění (§ 2800), zachraňovací náklady (§ 2819), přechod práva na pojistitele (§ 2820), škodové × obnosové pojištění (§ 2811+), pojištění osob (§ 2824+), majetku (§ 2849+), odpovědnosti (§ 2861+), právní ochrany (§ 2856+); promlčení (§ 626, § 635) |
| Zákon o pojistné smlouvě (starý) | 37/2004 Sb. | `cz_law/37/2004` | Smlouvy před 1. 1. 2014 (přechodná ustanovení OZ) |
| Zákon o pojištění odpovědnosti z provozu vozidla | 30/2024 Sb. | `cz_law/30/2024` | Povinnost pojistit (provozovatel), rozsah a limity, ČKP a garanční fond, příspěvek nepojištěných, regres, přímý nárok poškozeného, lhůty likvidace, likvidační zástupce, zelená karta; starý zákon 168/1999 Sb. pro dřívější události |
| Zákon o pojišťovnictví | 277/2009 Sb. | `cz_law/277/2009` | Dohled ČNB, mlčenlivost, výměna informací, sankce, likvidace pojišťovny |
| Zákon o distribuci pojištění a zajištění | 170/2018 Sb. | `cz_law/170/2018` | Zprostředkovatelé, odbornost, informační povinnosti, záznam z jednání, střet zájmů, odpovědnost za škodu způsobenou při distribuci, dohled ČNB |
| Zákon o ochraně spotřebitele / finanční arbitr | 634/1992 / 229/2002 Sb. | `cz_law/634/1992`, `cz_law/229/2002` | Nekalé praktiky, ADR - finanční arbitr pro životní pojištění (ověř působnost), ČOI pro neživotní, ombudsman ČAP (mimozákonný) |
| OZ - náhrada újmy | 89/2012 Sb. | `cz_law/89/2012` | Nároky poškozeného (§ 2894+, § 2951-§ 2971), provoz dopravních prostředků (§ 2927-§ 2932), Metodika NS k nemajetkové újmě |
| Zákon o silničním provozu / registr vozidel | 361/2000 / 56/2001 Sb. | `cz_law/361/2000`, `cz_law/56/2001` | Nehoda a oznámení, záznam o nehodě, registr - vyřazení a zánik vozidla (depozit) |
| Zákon o DPH / ZDP | 235/2004 / 586/1992 Sb. | `cz_law/235/2004`, `cz_law/586/1992` | Náhrada škody bez/s DPH podle plátcovství poškozeného, zdanění plnění z životního pojištění, daňová uznatelnost pojistného |
| Solvency II / IDD / GDPR | směrnice 2009/138/ES, 2016/97 | zdroj `EU` | Distribuce, informace pro zákazníka (IPID), zpracování zdravotních údajů |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu uzavření smlouvy a k datu pojistné události** → `/toc` → `/text?part=`; u smluv před 2014 zákon 37/2004 Sb.
2. Judikatura: **NS** senáty 23 Cdo (pojistná smlouva, výluky, snížení a odmítnutí plnění, promlčení, výklad podmínek), 25 Cdo (náhrada újmy z provozu vozidla, totální škoda, náhradní vozidlo, nemajetková újma, regres ČKP a pojistitele), 32 Cdo (podnikatelské pojištění, zajištění); **ÚS** (výklad podmínek contra proferentem, přiměřenost snížení, náhrada za ztrátu na výdělku); **SDEU** (`ES`) k motorovým směrnicím (pojem provoz vozidla, rozsah krytí, garanční fond). Ověř datum a to, zda rozhodnutí nevychází ze zákona 37/2004 Sb. nebo 168/1999 Sb.
3. Komentář (`COMMENT`) k § 2758+ OZ; metodiky ČAP (likvidace, totální škoda), Metodika NS k § 2958 OZ, sdělení ČNB k distribuci - mimo CODEXIS oficiální zdroje.

## Workflow

1. **Kvalifikace vztahu.** Kdo je pojistník × pojištěný × oprávněná osoba × poškozený (přímý nárok u odpovědnosti jen ze zákona - povinné ručení § 9 zák. 30/2024 Sb. - ověř; jinak vůči škůdci), typ pojištění (škodové × obnosové; majetek / odpovědnost / osoby / právní ochrana), datum uzavření a účinnosti smlouvy, **datum pojistné události**, znění pojistných podmínek a dotazníku k datu sjednání (ne aktuální na webu pojistitele), spotřebitel × podnikatel (kogentní ochrana § 2758+ vs. dispozitivita), zprostředkovatel a záznam z jednání.
2. **Sjednání a předsmluvní rovina.** Písemná forma při pojistné době nad 1 rok (§ 2758 odst. 2 - ověř), pojistné podmínky musí být seznámeny před uzavřením (§ 2774), povinnost odpovědět pravdivě a úplně na písemné dotazy (§ 2788 pojistník i pojištěný; § 2789 pojistitel), nadbytečné otázky a otázky nepoložené = riziko pojistitele, právo odstoupit pro porušení (§ 2808 - do 2 měsíců od zjištění, pojistník při porušení pojistitele obdobně), **odmítnutí plnění** (§ 2809 - jen když příčinou pojistné události byla zatajená skutečnost, kterou by pojistitel při pravdivé odpovědi nepojistil nebo pojistil jinak; oznámení odmítnutí = zánik pojištění), pojistný zájem (§ 2761 - bez něj neplatnost), spotřebitelské informace a právo odstoupit (§ 2806-§ 2807, § 1846 u distančního sjednání), IDD - záznam z jednání a analýza potřeb, odpovědnost zprostředkovatele za chybně sjednané krytí (§ 2950, zák. 170/2018 Sb.).
3. **Pojistná událost a likvidace.** Oznámení bez zbytečného odkladu (§ 2796 - pojistník / oprávněná osoba; pojistitel nemůže odmítnout jen pro pozdní oznámení, ale může snížit při prokázaném vlivu), povinnost pojistitele **zahájit šetření bez zbytečného odkladu a ukončit do 3 měsíců** od oznámení (§ 2797-§ 2798; překročení = **záloha** na žádost, prodloužení jen z důvodů nezávislých na pojistiteli, úrok z prodlení), plnění splatné **do 15 dnů od skončení šetření** (§ 2798 odst. 1 - ověř), zachraňovací náklady nad rámec pojistné částky (§ 2819), součinnost a mlčenlivost, znalecký posudek × prohlídka pojistitele, zpřístupnění spisu likvidace (§ 2797 odst. 3 - ověř), přechod práva na náhradu na pojistitele (§ 2820 - subrogace, ne u osob blízkých).
4. **Snížení a odmítnutí.** **Snížení plnění** (§ 2800 - porušení povinnosti pojistníka/pojištěného, které mělo podstatný vliv na vznik, průběh, zvětšení nebo zjištění výše; **úměrně vlivu** - důkazní břemeno pojistitel; hrubá nedbalost a alkohol podle podmínek; podpojištění § 2854 - poměrné krácení; nedodržení bezpečnostních opatření), **výluky** (výklad restriktivní, nejasnosti k tíži pojistitele § 1812, § 557; překvapivé ujednání § 1753), pojistný podvod (§ 210 TZ) × pouhé nesprávné údaje, odmítnutí podle § 2809 vs. neplatnost pro nedostatek pojistného zájmu, promlčení (**§ 626 - promlčecí lhůta plnění začíná běžet za rok od pojistné události**, obecná 3 roky; u odpovědnosti od uplatnění nároku poškozeným - ověř § 635), stavení promlčení uplatněním u pojistitele (ne), reklamace a ombudsman ČAP / finanční arbitr / ČOI, žaloba (příslušnost, SOP, znalec, úrok z prodlení od 16. dne po skončení šetření).
5. **Povinné ručení a nehody.** Povinnost pojistit má **provozovatel** (nový zákon), zánik povinnosti až vyřazením z registru / zánikem vozidla - vozidlo „v garáži" bez vyřazení = nepojištěné (příspěvek ČKP § 24+ zák. 30/2024 Sb. - ověř, obrana: prokázání pojištění, vyřazení, výzva doručena?, promlčení příspěvku), limity plnění (újma na zdraví × věcná škoda - ověř částky), **přímý nárok poškozeného vůči pojistiteli**, likvidační zástupce pro nehody v zahraničí, zelená karta, garanční fond ČKP (nezjištěné / nepojištěné vozidlo, insolvence pojistitele), nároky poškozeného: skutečná škoda (**totální škoda = obvyklá cena vozidla před nehodou minus zbytky, ne amortizované náklady opravy; DPH podle plátcovství**; oprava do výše obvyklé ceny; snížení hodnoty po opravě), náhradní vozidlo po dobu nezbytnou k opravě/pořízení (judikatura NS - i bez faktického pronájmu ne), ušlý zisk, odtah a parkovné, újma na zdraví (bolestné a ztížení dle Metodiky NS, ztráta na výdělku, péče, nemajetková újma blízkých § 2959), **regres pojistitele vůči řidiči** (alkohol, bez oprávnění, ujetí, nepojištěné vozidlo, nepravdivé údaje - lhůta a rozsah ověř § 10 zák. 30/2024 Sb. / dřívější § 10 zák. 168/1999 Sb.), promlčení nároku poškozeného vůči pojistiteli (§ 635 OZ - navázáno na promlčení vůči škůdci), trestní a přestupková rovina (viz skill dopravního práva).
6. **Majetek a odpovědnost podnikatelů.** Pojištění nemovitosti (pojistná hodnota nová × časová, indexace, podpojištění, zabezpečení, katastrofické výluky - povodeň 10letá voda, zóny), domácnost (cennosti a limity, krádež vs. loupež, doklad o zabezpečení), podnikatelské pojištění majetku a přerušení provozu (all-risk × vyjmenovaná nebezpečí, čekací doby), pojištění odpovědnosti (obecná, výrobek, profesní - advokáti, lékaři, projektanti, správci; claims-made × occurrence, retroaktivita, dodatečná lhůta, spoluúčast), D&O (péče řádného hospodáře), stavebně-montážní (CAR/EAR), pojištění přepravy (CMR), kybernetické, právní ochrany (§ 2856 - svobodná volba advokáta), zajištění a soupojištění (vedoucí pojistitel), makléřská smlouva a odpovědnost makléře.
7. **Pojištění osob.** Životní pojištění (obnosové, oprávněná osoba § 2831, změna obmyšleného, výluky sebevražda do 2 let - ověř, odkupné, investiční složka a poplatky - spory o TÚM/„zprostředkovatelské" smlouvy, daňové odpočty a dodanění při předčasném zrušení § 15 odst. 5-6 ZDP), úrazové (definice úrazu, trvalé následky, oceňovací tabulky, hrubá nedbalost), pojištění schopnosti splácet u úvěru (výluky, čekací doba, souhlas s výkonem), cestovní (asistence, léčebné výlohy, storno, výluky sport a alkohol), zdravotní údaje a GDPR, pojištění dětí, pojistné plnění v dědictví (mimo pozůstalost při určené oprávněné osobě).
8. **Zánik, změna a spor.** Nezaplacení pojistného (§ 2804 - upomínka s lhůtou nejméně 1 měsíc, jinak nezaniká), výpověď (§ 2805 - do 2 měsíců od uzavření, ke konci pojistného období 6 týdnů předem, do 3 měsíců od oznámení události - ověř), odstoupení, dohoda, zánik pojistného zájmu, změna vlastníka (§ 2812 - zánik dnem oznámení / u vozidel zákon), insolvence pojistitele (garanční systémy), převod kmene; procesní: reklamace → ombudsman ČAP / finanční arbitr (životní, ověř rozsah) / ČOI → žaloba (věcná příslušnost okresní soud; u regresu a náhrady újmy typicky 25 Cdo judikatura), důkazní břemeno (vznik události a výše - oprávněná osoba; výluka a porušení povinnosti - pojistitel), znalecké posudky, mediace.

## Časté pasti

- Nepravdivá odpověď v dotazníku bez příčinné souvislosti s událostí - pojistitel nemůže odmítnout (§ 2809), jen případně odstoupit ve lhůtě 2 měsíců od zjištění.
- Snížení plnění paušálně „o 50 %" bez prokázání vlivu porušení - nepřiměřené; hrubá nedbalost jen podle podmínek a s důkazem.
- Šetření prodlužované přes 3 měsíce bez důvodu - nárok na zálohu a úrok z prodlení; klient nepožádal písemně.
- Promlčení počítané od pojistné události místo od uplynutí roku po ní (§ 626); u odpovědnosti navázáno na promlčení vůči škůdci.
- Totální škoda krácená o amortizaci nebo počítaná z nákladů opravy - judikatura NS: obvyklá cena minus zbytky; DPH u neplátce se hradí.
- Vozidlo nepoužívané, ale nevyřazené z registru - příspěvek ČKP; „depozit" bez vyřazení nestačí.
- Nový zákon 30/2024 Sb. aplikovaný na nehodu před jeho účinností (a naopak) - limity a regres se liší.
- Pojistné podmínky brané z webu pojistitele místo verze účinné při sjednání.
- Podpojištění nemovitosti (pojistná částka pod novou hodnotou) - poměrné krácení i u malých škod.
- Claims-made odpovědnostní pojištění ukončené bez dodatečné lhůty - pozdější nárok nekrytý.
- Oprávněná osoba z životního pojištění zaměněná s dědici; odkupné považované za pojistnou částku.
- Regres pojistitele vůči řidiči odmítán jako promlčený bez ověření lhůty a data, kdy pojistitel plnil.
- Doplňování čísel smluv, pojistných částek, limitů, dat událostí a názvů pojistitelů z paměti - vždy ze smlouvy, podmínek, likvidačního spisu nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co uplatnit, u koho, do kdy - promlčení, lhůta pro odstoupení/výpověď, lhůta pojistitele).
2. **Kvalifikace vztahu** - role, typ pojištění, datum smlouvy a události, použitelný zákon (OZ × 37/2004 × 30/2024 × 168/1999).
3. **Právní rámec** - OZ / zákon o povinném ručení / distribuce / zvláštní předpisy v aktuálním znění, s odkazy.
4. **Nároky a obrana** - tabulka: nárok | právní základ (zákon × podmínky čl.) | důkazní břemeno | lhůta | výše/riziko.
5. **Procesní cesta** (reklamace, ombudsman/arbitr/ČOI, žaloba, znalec, úroky).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky** (smlouva, podmínky k datu, dotazník, likvidační spis), placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 23 Cdo 1234/2024 - …`, `NS - 25 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („podstatný vliv na vznik, průběh nebo zvětšení rozsahu“, „úměrně tomu, jaký vliv mělo porušení“, „za jeden rok od pojistné události“, „do tří měsíců po oznámení“).
- Jeden časový řez; znění OZ / zákona o povinném ručení účinné k datu pojistné události, podmínky k datu sjednání.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu (smlouva, událost).
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity plnění, sazby příspěvků ČKP, lhůty a daňové limity nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o pojistitelích, zprostředkovatelích a vozidlech výhradně z registru ČNB, ČKP a registru vozidel; mimo CODEXIS jen oficiální zdroje (cnb.cz, ckp.cz, cap.cz, finarbitr.cz) když CODEXIS neodpovídá.
