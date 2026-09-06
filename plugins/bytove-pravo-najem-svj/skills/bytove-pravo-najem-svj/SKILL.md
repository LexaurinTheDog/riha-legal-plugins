---
uuid: 7dcc8498-c468-472f-b815-09073e97daa9
name: bytove-pravo-najem-svj
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Bytové právo - nájem a SVJ ČR"
    summary: "Nájem bytu a prostor sloužících podnikání, výpověď a vyklizení, nájemné a vyúčtování služeb, společenství vlastníků, bytová družstva, krátkodobé pronájmy."
    examplePrompts:
      - "Nájemce neplatí tři měsíce a v bytě bydlí i osoby, které nenahlásil. Jak dát platnou výpověď a jak rychle ho vystěhovat?"
      - "Shromáždění SVJ schválilo úvěr na zateplení a klient byl přehlasován. Může se bránit a do kdy?"
      - "Pronajímatel vrátil jistotu sníženou o 'opotřebení' bez dokladů. Jaké má nájemce nároky?"
  en:
    displayName: "Czech Housing Law - Leases and HOAs"
    summary: "Residential and commercial leases, termination and eviction, rent and service charges, owners' associations (SVJ), housing cooperatives, short-term rentals."
    examplePrompts:
      - "A tenant has not paid for three months and unregistered persons live in the flat. How to give a valid notice and evict quickly?"
      - "The owners' meeting approved a loan for insulation and my client was outvoted. Can he challenge it and by when?"
      - "The landlord returned the deposit reduced for 'wear and tear' without receipts. What claims does the tenant have?"
  sk:
    displayName: "Bytové právo - nájom a SVJ ČR"
    summary: "Nájom bytu a priestorov slúžiacich podnikaniu v ČR, výpoveď a vypratanie, nájomné a vyúčtovanie služieb, spoločenstvá vlastníkov, bytové družstvá, krátkodobé prenájmy."
    examplePrompts:
      - "Nájomca neplatí tri mesiace a v byte bývajú aj osoby, ktoré nenahlásil. Ako dať platnú výpoveď a ako rýchlo ho vysťahovať?"
      - "Zhromaždenie SVJ schválilo úver na zateplenie a klient bol prehlasovaný. Môže sa brániť a dokedy?"
      - "Prenajímateľ vrátil zábezpeku zníženú o 'opotrebenie' bez dokladov. Aké má nájomca nároky?"
description: Use when the user's matter involves Czech housing, leases or condominium governance - nájem bytu, nájem domu, nájemní smlouva, pronajímatel, nájemce, nájemné, zvyšování nájemného, jistota, kauce, služby spojené s užíváním bytu, vyúčtování služeb (67/2013 Sb.), drobné opravy, podnájem, členové domácnosti, přechod nájmu, výpověď z nájmu, výpověď bez výpovědní doby, přezkum výpovědi, vyklizení, automatické obnovení nájmu, prostor sloužící podnikání, náhrada za převzetí zákaznické základny, pacht, ubytování, Airbnb, krátkodobý pronájem, společenství vlastníků jednotek (SVJ), shromáždění, přehlasovaný vlastník, prohlášení vlastníka, příspěvky na správu, potvrzení o dluzích, nucený prodej jednotky, bytové družstvo, družstevní byt, převod družstevního podílu, vyloučení z družstva, bytové spoluvlastnictví (§ 1158+ OZ), nájem (§ 2201-§ 2331 OZ). Standalone skill - bundles CODEXIS methodology with housing-law method; no need to load the general codexis skill.
---

# Bytové právo - nájem a SVJ ČR

Samostatný oborový skill pro nájemní vztahy a správu domů. Dvě věci před vším ostatním: **kvalifikace vztahu** (nájem bytu s kogentní ochranou × prostor sloužící podnikání × obecný nájem × pacht × ubytování × družstevní nájem) a **formální náležitosti výpovědi** - většina výpovědí z nájmu bytu padá na chybějícím poučení, formě nebo zmeškané dvouměsíční lhůtě k přezkumu.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2288'`, `cdx-cli get cdx://cz_law/67/2013/versions`, `cdx-cli get cdx://cz_law/90/2012/versions`, `cdx-cli search JD --query "výpověď z nájmu bytu poučení námitky přezkum 2290" --court "Nejvyšší soud" --limit 5`.
- Nájemní a bytové právo OZ bylo novelizováno (2020 - předkupní právo, SVJ, smluvní pokuta u nájmu bytu; další změny průběžně) a limity (drobné opravy, jistota, zvyšování) závisí na nařízeních a datech. **Každý §, lhůtu, limit a násobek ověř v aktuálním znění k datu uzavření smlouvy nebo úkonu**; nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - nájem | 89/2012 Sb. | `cz_law/89/2012` | Obecný nájem (§ 2201-§ 2234), nájem bytu a domu (§ 2235-§ 2301: forma § 2237, nájemné § 2246-§ 2250, jistota § 2254, práva a povinnosti § 2255-§ 2270, domácnost a podnájem § 2272-§ 2278, přechod nájmu § 2279+, obnovení § 2285, skončení § 2286-§ 2296), prostor sloužící podnikání (§ 2302-§ 2315), ubytování (§ 2326+), pacht (§ 2332+) |
| OZ - bytové spoluvlastnictví | 89/2012 Sb. | `cz_law/89/2012` | Jednotka a prohlášení (§ 1158-§ 1173), práva a povinnosti vlastníka (§ 1175-§ 1188), SVJ (§ 1189-§ 1216: shromáždění § 1206-§ 1209, per rollam § 1210+, příspěvky § 1180-§ 1181), nucený prodej (§ 1184), převod (§ 1186 potvrzení o dluzích) |
| NV o úpravě některých záležitostí bytového spoluvlastnictví | 366/2013 Sb. | `cz_law/366/2013` | Společné části, podíly, rozúčtování |
| Zákon o službách | 67/2013 Sb. | `cz_law/67/2013` | Zálohy, rozúčtování, vyúčtování (§ 7 - lhůta), námitky (§ 8), doplatky a přeplatky, pokuta za prodlení (§ 13) |
| NV o drobných opravách | 308/2015 Sb. | `cz_law/308/2015` | Vymezení drobných oprav a běžné údržby, limity částek |
| ZOK - bytové družstvo | 90/2012 Sb. | `cz_law/90/2012` | Družstevní byt a nájem (§ 727-§ 757), převod podílu (§ 736), vyloučení (§ 734), vypořádací podíl (§ 748) |
| Zákon o vlastnictví bytů (starý) | 72/1994 Sb. | `cz_law/72/1994` | Jednotky vymezené před 2014 (dvojí režim) |
| Katastrální zákon | 256/2013 Sb. | `cz_law/256/2013` | Zápis prohlášení, jednotek, SVJ |
| o. s. ř. / ZŘS | 99/1963 / 292/2013 Sb. | `cz_law/99/1963`, `cz_law/292/2013` | Přezkum výpovědi, žaloba na vyklizení a výkon vyklizením (§ 340+), statusové věci SVJ a družstev |
| Zákon o hospodaření energií / živnostenský zákon | 406/2000 / 455/1991 Sb. | `cz_law/406/2000`, `cz_law/455/1991` | PENB při pronájmu, ubytovací služby jako živnost |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu uzavření smlouvy / úkonu** (pozor na novelu 2020 a přechodná ustanovení § 3074 OZ pro nájmy z doby před 2014) → `/toc` → `/text?part=`.
2. Judikatura: **NS** senát 26 Cdo (nájem bytu a prostor, SVJ, družstva) - výpovědní důvody, poučení a přezkum, krátkodobé pronájmy nájemcem, jistota a její úročení, přehlasovaný vlastník, potvrzení o dluzích; **ÚS** k ochraně nájemce a vlastníka. Ověř datum a znění.
3. Komentář (`COMMENT`) k pojmům (hrubé × zvlášť závažné porušení, obvyklé nájemné, důležitý důvod u § 1209, drobné opravy); vzory (`VS`) nájemních smluv a výpovědí sladit s aktuálním zněním - staré vzory citují neplatná čísla a smluvní pokuty.

## Workflow

1. **Kvalifikace vztahu.** Nájem bytu/domu k bydlení (kogentní ochrana § 2235 - k ujednáním zkracujícím práva nájemce se nepřihlíží) × prostor sloužící podnikání (§ 2302+) × obecný nájem (chata, garáž) × pacht (výnos) × ubytování (§ 2326 - krátkodobé, Airbnb) × družstevní nájem (ZOK + stanovy) × podnájem × výprosa/výpůjčka. Datum uzavření a rozhodné znění; nájmy před 2014 (§ 3074 OZ).
2. **Smlouva a její nastavení.** Písemná forma (§ 2237 - nedostatek nelze namítat proti nájemci), předmět a stav (§ 2242 protokol), nájemné a služby (§ 2246-§ 2247; není-li sjednáno - obvyklé), zvyšování (§ 2248 dohoda / § 2249 zákonný postup - limit a interval ověř / soud), **jistota** (§ 2254 - nejvýše trojnásobek měsíčního nájemného, úrok, vrácení při skončení se započtením), smluvní pokuta (po novele 2020 přípustná v limitu jistoty - ověř § 2239), drobné opravy a údržba (§ 2257, NV 308/2015 Sb.), zvířata (§ 2258), úpravy bytu (§ 2263), členové domácnosti (§ 2272 - právo přijímat, oznamovací povinnost, limit počtu), podnájem (§ 2274-§ 2275 - bez souhlasu jen když nájemce v bytě sám trvale bydlí), PENB.
3. **Skončení nájmu bytu.** Dohoda; uplynutí doby + **automatické obnovení** (§ 2285 - nevyzve-li pronajímatel do 3 měsíců, obnovuje se na stejnou dobu, nejvýše 2 roky - ověř); výpověď nájemce (bez důvodu u doby neurčité, 3 měsíce; u doby určité jen při změně okolností § 2287); **výpověď pronajímatele** (§ 2288 - taxativní důvody: hrubé porušení, odsouzení za úmyslný TČ, vyklizení domu ve veřejném zájmu, jiný obdobně závažný důvod; u doby neurčité navíc potřeba bytu pro sebe/příbuzné), **písemně, s výpovědním důvodem a poučením o právu podat námitky a návrh na přezkum do 2 měsíců** (§ 2286 odst. 2, § 2290) - jinak neplatná; **výpověď bez výpovědní doby** (§ 2291 - zvlášť závažné porušení: neplacení nájemného a nákladů za 3 měsíce, poškozování, neoprávněné užívání; předchozí výzva k nápravě s přiměřenou lhůtou); přechod nájmu při smrti (§ 2279-§ 2284 - členové domácnosti, 2 roky); skončení ex lege (zánik bytu).
4. **Vyklizení a vypořádání.** Odevzdání bytu (§ 2292-§ 2293 - stav podle protokolu, běžné opotřebení), po skončení nájmu **jen ujednané nájemné do vyklizení** (§ 2295), náhrada škody, vrácení jistoty se započtením, žaloba na vyklizení (okresní soud, bytová náhrada už není), výkon rozhodnutí vyklizením (§ 340+ o. s. ř. - exekutor, uskladnění věcí), nedovolené svépomocné vystěhování (odpovědnost, § 14 OZ jen výjimečně).
5. **Služby (67/2013 Sb.).** Rozsah služeb a zálohy, rozúčtování (podle podlahové plochy, osob, měřidel), **vyúčtování do 4 měsíců po skončení zúčtovacího období** (§ 7), doložení nákladů (§ 8 - nahlédnutí do podkladů, námitky do 30 dnů, vyřízení do 30 dnů - ověř), splatnost přeplatku/nedoplatku (4 měsíce po doručení vyúčtování), pokuta za prodlení (§ 13 - 50 Kč/den, snížení - ověř), řádné vyúčtování jako podmínka splatnosti nedoplatku.
6. **Prostor sloužící podnikání (§ 2302-§ 2315).** Účel a jeho změna, převod nájmu s podnikem (§ 2307), výpověď u doby určité (§ 2308 nájemce, § 2309 pronajímatel - důvody), u doby neurčité (§ 2312 - 6 měsíců), **námitky proti výpovědi do 1 měsíce** (§ 2314 - jinak právo na přezkum zaniká), náhrada za převzetí zákaznické základny (§ 2315), obchodní podmínky, stavební úpravy a odpisy, podnájem.
7. **SVJ a bytové spoluvlastnictví.** Prohlášení vlastníka a jeho změna (§ 1169 - souhlas dotčených), vznik SVJ a zápis do rejstříku, stanovy (§ 1200), orgány (výbor / předseda, kontrolní komise), **shromáždění** (svolání § 1207 - 30 dnů předem s pozvánkou a podklady; usnášeníschopnost nadpoloviční většina hlasů § 1206; rozhoduje většina hlasů přítomných, ledaže zákon nebo stanovy vyšší), per rollam (§ 1210-§ 1214), **přehlasovaný vlastník** (§ 1209 - návrh soudu do 3 měsíců od dozvědění, důležitý důvod), příspěvky a zálohy (§ 1180-§ 1181, vyúčtování), dluhy vlastníka (žaloba, přednostní uspokojení části pohledávky SVJ v dražbě jednotky - ověř § 337c o. s. ř.), **nucený prodej jednotky** (§ 1184 - soud na návrh SVJ při závažném porušení a po výzvě), převod jednotky (§ 1186 - potvrzení o dluzích, přechod dluhů na nabyvatele), stavební úpravy a společné části (NV 366/2013), krátkodobé pronájmy a domovní řád, pojištění, GDPR a kamery, rejstřík SVJ a sbírka listin.
8. **Bytové družstvo.** Nájem družstevního bytu (ZOK § 741+, stanovy - nájemné = účelně vynaložené náklady), **převod družstevního podílu bez souhlasu** (§ 736 - účinnost doručením smlouvy družstvu; daňový a poplatkový režim × jednotka), vyloučení člena (§ 734 - výstraha, rozhodnutí, námitky, soud), vypořádací podíl (§ 748), převod jednotky do vlastnictví (§ 1188 OZ - bezúplatně po splacení anuity), anuita a úvěry, shromáždění delegátů.
9. **Krátkodobé pronájmy (Airbnb).** Ubytování (§ 2326) × nájem; pronájem třetím osobám nájemcem = porušení nájmu a výpovědní důvod (judikatura NS), souhlas vlastníka, SVJ stanovy a domovní řád, živnost (ubytovací služby), daně a poplatky obce, evidence hostů (cizinecká policie), obecní regulace a evidenční systémy (ověř aktuální úpravu).
10. **Spory.** Přezkum výpovědi (2 měsíce - prekluze), žaloba na vyklizení, žaloba na zaplacení nájemného a služeb, žaloba přehlasovaného vlastníka (3 měsíce), určení neplatnosti usnesení shromáždění, předběžné opatření, exekuce vyklizením; okresní soud, u SVJ/družstev statusové věci krajský soud (§ 85 ZŘS).

## Časté pasti

- Výpověď bez písemného poučení o námitkách a přezkumu, bez uvedení důvodu nebo bez písemné formy - neplatná; nájemce zmeškal 2 měsíce k přezkumu - výpověď platí i s vadami.
- Výpověď bez výpovědní doby bez předchozí výzvy k nápravě nebo za pouhé „hrubé" (ne „zvlášť závažné") porušení.
- Nájem na dobu určitou skončil, nájemce dál bydlí a pronajímatel do 3 měsíců nevyzval - nájem se obnovil.
- Jistota nad trojnásobek nájemného; jistota nevrácená bez vyúčtování; úrok z jistoty.
- Zvyšování nájemného nad zákonný limit nebo častěji než zákon dovoluje.
- Vyúčtování služeb po lhůtě nebo bez doložení - nedoplatek není splatný, hrozí pokuta; námitky zmeškány.
- Po skončení nájmu účtováno „nájemné" navýšené o sankce - § 2295 dovoluje jen ujednané nájemné.
- Podnájem nebo Airbnb nájemcem bez souhlasu brán jako bez následků - výpovědní důvod.
- Prostor sloužící podnikání: námitky proti výpovědi po 1 měsíci - právo na přezkum zaniklo.
- Přehlasovaný vlastník žaluje po 3 měsících nebo bez důležitého důvodu.
- Převod jednotky bez potvrzení o dluzích - nabyvatel přebírá dluhy na správě domu.
- Shromáždění svolané bez 30denní lhůty nebo bez podkladů - napadnutelnost usnesení; per rollam bez formy vyžadované stanovami.
- Starý vzor nájemní smlouvy se smluvní pokutou nad limit nebo se zákazem chovu zvířat - nepřihlíží se.
- Doplňování čísel jednotek, podílů, dat a částek z paměti - vždy z LV, smlouvy nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat, do kdy; u výpovědi přesné náležitosti).
2. **Kvalifikace vztahu a rozhodné znění.**
3. **Právní rámec** - OZ / 67/2013 / ZOK v aktuálním znění, s odkazy.
4. **Postup nebo nároky** - tabulka: krok/nárok | právní základ | forma a lhůta | důkaz.
5. **Rizika a alternativy** (dohoda o skončení, splátky, mediace, náklady a délka vyklizení).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 26 Cdo 2128/2023 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do dvou měsíců ode dne, kdy mu byla výpověď doručena“, „zvlášť závažným způsobem“, „nejvýše trojnásobek“, „do 3 měsíců od uplynutí doby“).
- Jeden časový řez; u výpovědi znění účinné v den doručení.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity (jistota, zvyšování, drobné opravy, pokuty za vyúčtování) a lhůty nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o jednotkách a vlastnících výhradně z katastru a rejstříku SVJ; mimo CODEXIS jen oficiální zdroje (justice.cz, ČÚZK, mmr.gov.cz) když CODEXIS neodpovídá.
