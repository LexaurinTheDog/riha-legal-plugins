---
uuid: 4e1b642c-1332-469b-8d06-72075b71159d
name: energeticke-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Energetické právo ČR"
    summary: "Licence a regulace ERÚ, smlouvy o dodávce elektřiny a plynu a změna dodavatele, podpora a povolování OZE, komunitní energetika a sdílení, připojení k síti, cenová regulace a spory, teplárenství, energetická náročnost budov."
    examplePrompts:
      - "Dodavatel elektřiny jednostranně zvýšil cenu a klient chce odejít bez sankce. Jaké jsou lhůty a jak správně vypovědět smlouvu?"
      - "Obec chce postavit FVE na střechách škol a sdílet elektřinu mezi budovami. Jaký režim (energetické společenství, sdílení) a jaká povolení?"
      - "Distributor odmítl připojit výrobnu 500 kW pro nedostatek kapacity. Lze se bránit a u koho?"
  en:
    displayName: "Czech Energy Law"
    summary: "Energy Act licences and ERÚ regulation, electricity and gas supply contracts and switching, renewable support and permitting, community energy and self-consumption, grid connection, price regulation and disputes, heat supply, energy performance of buildings."
    examplePrompts:
      - "An electricity supplier unilaterally raised the price and my client wants to leave without penalty. What are the deadlines and how to terminate properly?"
      - "A municipality wants rooftop PV on schools and to share electricity between buildings. Which regime (energy community, sharing) and which permits?"
      - "The distributor refused to connect a 500 kW plant for lack of capacity. Can we challenge it and where?"
  sk:
    displayName: "Energetické právo ČR"
    summary: "Licencie a regulácia ERÚ, zmluvy o dodávke elektriny a plynu a zmena dodávateľa, podpora a povoľovanie OZE, komunitná energetika a zdieľanie, pripojenie do siete, cenová regulácia a spory, teplárenstvo, energetická náročnosť budov."
    examplePrompts:
      - "Dodávateľ elektriny jednostranne zvýšil cenu a klient chce odísť bez sankcie. Aké sú lehoty a ako správne vypovedať zmluvu?"
      - "Obec chce postaviť FVE na strechách škôl a zdieľať elektrinu medzi budovami. Aký režim (energetické spoločenstvo, zdieľanie) a aké povolenia?"
      - "Distribútor odmietol pripojiť výrobňu 500 kW pre nedostatok kapacity. Možno sa brániť a u koho?"
description: Use when the user's matter involves energy supply, generation or regulation in the Czech Republic - energetika, energetický zákon (458/2000 Sb.), Energetický regulační úřad, ERÚ, licence na výrobu a obchod, dodavatel elektřiny, dodavatel plynu, změna dodavatele, výpověď smlouvy o dodávce, jednostranná změna ceny, dodavatel poslední instance, distributor, připojení k distribuční soustavě, smlouva o připojení, nedostatek kapacity, obnovitelné zdroje, fotovoltaika, FVE, větrná elektrárna, podpora OZE (165/2012 Sb.), zelený bonus, výkupní cena, komunitní energetika, energetické společenství, sdílení elektřiny, EDC, aktivní zákazník, teplárenství, odpojení od CZT, energetický audit a PENB (406/2000 Sb.), cenová rozhodnutí ERÚ, spor s dodavatelem u ERÚ, přestupky SEI, RED III, EU energetická legislativa. Standalone skill - bundles CODEXIS methodology with energy-practice method; no need to load the general codexis skill.
---

# Energetické právo ČR

Samostatný oborový skill pro energetiku. Základní reflex: energetika je **odvětví s trojím právním režimem** - soukromoprávní smlouva (OZ + energetický zákon jako lex specialis) × veřejnoprávní regulace (licence, cenová rozhodnutí a vyhlášky ERÚ, dohled SEI) × unijní právo (směrnice o trhu s elektřinou, RED III, nařízení) - a odpověď musí říct, ve které rovině klient stojí. Druhý reflex: **energetický zákon se novelizuje několikrát ročně** (LEX OZE I–III, komunitní energetika, dynamické tarify, akumulace); nikdy nevycházet z čísla paragrafu z paměti, vždy `/versions` k datu.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/458/2000/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf11a'`, `cdx-cli get cdx://cz_law/165/2012/versions`, `cdx-cli search JD --query "jednostranná změna ceny dodavatel elektřiny výpověď zákazník" --court "Nejvyšší soud" --limit 5`, `cdx-cli search JD --query "připojení k distribuční soustavě odmítnutí kapacita ERÚ" --court "Nejvyšší správní soud" --limit 5`.
- Cenová rozhodnutí ERÚ, vyhlášky (o pravidlech trhu, o připojení, o měření), limity výkonu pro výrobny bez licence, lhůty pro změnu dodavatele a výši podpory **ověř v aktuálním znění k datu**; nikdy z paměti. Sekundární předpisy hledej ve zdroji `CR` podle čísla vyhlášky, cenová rozhodnutí na eru.gov.cz.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Energetický zákon | 458/2000 Sb. | `cz_law/458/2000` | Licence (§ 3-§ 10; výrobna bez licence do limitu § 3 odst. 3 - ověř), ERÚ (§ 17+; spory § 17 odst. 7), práva a povinnosti zákazníka (§ 11a - jednostranná změna, výpověď, odstoupení; § 28), dodavatel poslední instance (§ 12a), elektroenergetika (§ 22-§ 54: výrobce § 23, distributor § 25, připojení § 28, obchodník § 30, aktivní zákazník, sdílení a EDC § 28a+, akumulace, agregace), plynárenství (§ 55+), teplárenství (§ 76+: odpojení § 77), SEI a přestupky (§ 90+), neoprávněný odběr (§ 51) |
| Zákon o podporovaných zdrojích energie | 165/2012 Sb. | `cz_law/165/2012` | Formy podpory (výkupní cena, zelený bonus, aukce), podmínky a doba, OTE, kontrola přiměřenosti podpory (§ 30+), odvod z elektřiny ze slunečního záření (§ 14+), záruky původu, komunitní energetika (energetická společenství § 2 - ověř umístění) |
| Zákon o hospodaření energií | 406/2000 Sb. | `cz_law/406/2000` | PENB, energetický audit a posudek, povinnosti při prodeji/pronájmu budov, energetický specialista, sankce SEI |
| Vyhlášky ERÚ a MPO | 408/2015, 16/2016, 359/2020, 490/2021, 404/2016 Sb. a další | `cz_law/408/2015` atd. (ověř čísla) | Pravidla trhu s elektřinou, připojení k soustavě, měření, dispečerské řízení, pravidla trhu s plynem, vyúčtování |
| Cenová rozhodnutí ERÚ | roční | mimo CODEXIS (eru.gov.cz) | Regulované ceny distribuce, přenosu, POZE, systémové služby; podpora OZE |
| Zákon o cenách | 526/1990 Sb. | `cz_law/526/1990` | Věcné usměrňování cen tepla, cenová kontrola |
| Stavební zákon + EIA | 283/2021 / 100/2001 Sb. | `cz_law/283/2021`, `cz_law/100/2001` | Povolení výroben, FVE na střechách bez povolení do limitu (ověř), EIA pro větrné a velké FVE, územní plánování |
| Zákon o urychlení výstavby + LEX OZE | 416/2009 Sb. a novely | `cz_law/416/2009` | Zrychlené povolování OZE, převažující veřejný zájem, go-to zóny (RED III) |
| Zákon o ochraně spotřebitele + OZ | 634/1992 / 89/2012 Sb. | `cz_law/634/1992`, `cz_law/89/2012` | Podomní prodej energií, energetičtí šmejdi, odstoupení, zneužívající ujednání, smlouva uzavřená mimo obchodní prostory |
| EU: směrnice (EU) 2019/944, nařízení (EU) 2019/943, RED III (EU) 2023/2413, EED (EU) 2023/1791, nařízení o velkoobchodním trhu REMIT | Úř. věst. | zdroj `EU` | Práva zákazníků, energetická společenství, aktivní zákazníci, cíle OZE, povolování, energetická účinnost |
| Zákon o opatřeních k přechodu ČR k nízkouhlíkové energetice | 367/2021 Sb. | `cz_law/367/2021` | Jaderné zdroje, smlouvy o výkupu |
| Krizová opatření (cenové stropy, mimořádné tržní situace) | NV 298/2022 Sb. a další (ověř platnost) | `cz_law/298/2022` | Cenové stropy 2023, odvody z nadměrných příjmů - historicky, pro spory z toho období |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu smlouvy / události** → `/toc` → `/text?part=`; novely energetického zákona přečíslovávají § (LEX OZE) - vždy zkontrolovat, že § existuje v daném znění.
2. Judikatura: **NSS** (licence, spory u ERÚ, přezkum rozhodnutí ERÚ a SEI, solární odvod, podpora OZE - odnětí, sankce, připojení), **NS** (smlouvy o dodávce, neoprávněný odběr, náhrada škody z přerušení dodávek, teplo - odpojení a cena, smluvní pokuty za předčasné ukončení, podomní prodej), **ÚS** (solární odvod - Pl. ÚS 17/11, retroaktivita, legitimní očekávání), **SDEU** (`ES`) k unbundlingu, státní podpoře a právům zákazníků. Ověř datum a znění zákona.
3. Komentář (`COMMENT`) k energetickému zákonu; výkladová stanoviska ERÚ, metodiky OTE a SEI, Pravidla provozování distribuční soustavy (PPDS) - mimo CODEXIS oficiální zdroje s vysokou praktickou váhou.

## Workflow

1. **Kvalifikace.** Kdo je klient: zákazník (domácnost × podnikatel × obec), výrobce (licencovaný × bez licence), obchodník, distributor, provozovatel lokální soustavy, energetické společenství, developer OZE, dodavatel tepla; komodita (elektřina, plyn, teplo); smluvní typ (sdružené služby × oddělená dodávka a distribuce); datum smlouvy a události; regulační rok.
2. **Smlouvy o dodávce a ochrana zákazníka.** Náležitosti smlouvy (§ 11a EZ - ověř), **jednostranná změna ceny nebo podmínek**: povinnost oznámit nejméně 30 dnů předem a právo zákazníka **odstoupit/vypovědět bez sankce do 10 dnů před účinností** (ověř § 11a odst. 3-5 - lhůty se novelizovaly), fixace × spotový produkt, změna dodavatele (proces OTE, lhůty, smluvní pokuta za předčasné ukončení jen v mezích zákona - ověř, výpověď smlouvy na dobu neurčitou 3 měsíce), smlouva uzavřená distančně / mimo obchodní prostory (odstoupení 14 dnů, podomní prodej - obce mohou zakázat), zprostředkovatelé („energetičtí šmejdi" - registrace u ERÚ, zákaz plných mocí bez lhůt - ověř), dodavatel poslední instance (DPI - 6 měsíců, povinnost přejít), vyúčtování a zálohy (vyhláška o vyúčtování), reklamace, přerušení a obnovení dodávky (neoprávněný odběr § 51 - náhrada dle vyhlášky, výše bez měření), přeplatky, zákaznická linka. Spory zákazník × dodavatel: **ERÚ rozhoduje spory o plnění smluv a uzavření smlouvy (§ 17 odst. 7)**, alternativně soud; pro spotřebitele ADR u ERÚ.
3. **Připojení k soustavě.** Žádost o připojení podle vyhlášky o připojení (ověř č.), posouzení distributora, **smlouva o připojení** (rezervovaný příkon/výkon, podíl na nákladech, lhůty), odmítnutí pro nedostatek kapacity - povinnost odůvodnit, alternativy (omezení výkonu, přetoky 0, akumulace), **spor o uzavření smlouvy o připojení rozhoduje ERÚ** (§ 17 odst. 7 písm. a) - ověř), mikrozdroje zjednodušený režim, dynamický tarif a chytré měření, změna rezervovaného příkonu, přeložky (§ 47 - hradí ten, kdo ji vyvolal), věcná břemena a vstupy na pozemky (§ 24-§ 25 - oprávnění provozovatele soustavy, náhrada).
4. **Výroba a licence.** Licence ERÚ (§ 4-§ 10: podmínky, odborná způsobilost, majetkoprávní vztah k výrobně, změna, zrušení), **výrobna bez licence** do stanoveného výkonu pro vlastní spotřebu (limit ověř - zvýšen LEX OZE I na 50 kW), registrace u OTE, měření, přetoky do sítě (výkup obchodníkem, smlouva), fakturace a DPH/daň z příjmů z přetoků, provozní řád, revize, požární bezpečnost, pojištění; velké výrobny: územní řízení a stavební povolení (FVE na budovách do limitu bez povolení - ověř § stavebního zákona), EIA (větrné parky), ochranná pásma, zemědělská půda (vynětí ze ZPF, agrivoltaika), památková ochrana, hlukové limity, přístup k pozemkům (pacht, věcná břemena), připojení, LEX OZE II - převažující veřejný zájem, go-to zóny.
5. **Podpora OZE.** Nárok na podporu (zákon 165/2012 Sb. - forma, výše dle cenového rozhodnutí ERÚ pro rok uvedení do provozu, doba 15/20 let), podmínky (měření, registrace OTE, roční výkaz, kombinace s investiční dotací - **překompenzace** a kontrola přiměřenosti podpory § 30+ s možností snížení), změna vlastníka výrobny (přechod podpory), odnětí podpory, **solární odvod** (u zdrojů 2009-2010, ústavnost potvrzena, individuální rdousící efekt jen výjimečně), aukce, záruky původu, nový režim pro modernizace; dotace (Modernizační fond, NZÚ, OP TAK) - podmínky a udržitelnost; spory: NSS k odnětí, SEI kontroly.
6. **Komunitní energetika a sdílení.** Energetické společenství / společenství pro obnovitelné zdroje (právní formy - spolek, družstvo, s.r.o.; registrace u ERÚ; členové - FO, obce, malé podniky; zákaz, aby hlavní činností byl zisk - ověř), **sdílení elektřiny** přes EDC (Elektroenergetické datové centrum) - skupiny sdílení, alokační klíč, limity počtu odběrných míst a distribučních území (ověř § 28a+ EZ / LEX OZE II), aktivní zákazník, bytové domy (společná výrobna, rozúčtování SVJ), obce (FVE na budovách + sdílení mezi příspěvkovými organizacemi; veřejné zakázky na výrobnu, koncese na provoz, veřejná podpora), smlouvy o sdílení, fakturace, distribuční poplatky u sdílené elektřiny.
7. **Teplárenství a budovy.** Dodávka tepla (§ 76+ EZ - smlouva, měření, věcně usměrňovaná cena dle zákona o cenách a cenových rozhodnutí ERÚ, kalkulace, kontrola), **odpojení od CZT** (§ 77 odst. 5 - podmínky, souhlas, náklady; územní energetická koncepce), rozúčtování nákladů na teplo v domech (vyhláška 269/2015 Sb., zákon 67/2013 Sb.), PENB při prodeji a pronájmu (406/2000 Sb. - povinnost, výjimky, sankce; viz skill nemovitostí), energetický audit velkých podniků, ESCO/EPC smlouvy, tepelná čerpadla a hluk, kotlíkové dotace.
8. **Regulace, dohled, spory.** ERÚ: cenová rozhodnutí (přezkum jen omezeně - obecné povahy), licenční řízení (správní řád), **rozhodování sporů** (§ 17 odst. 7 - o uzavření smlouvy o připojení, o plnění smluv, o splnění povinností; lhůty; přezkum soudem - civilní část V o. s. ř. u sporů o plnění, správní žaloba u licencí/pokut), přestupky (§ 90+ - dodavatelé, výrobci; pokuty v desítkách mil. Kč), SEI (kontrola, pokuty za PENB a audity, podpora OZE), ÚOHS (veřejná podpora, hospodářská soutěž na trhu s energií), REMIT (manipulace s trhem), OTE (registrace, odchylka). Krizové období 2022-2023: cenové stropy, odvod z nadměrných příjmů, úsporný tarif - jen pro dobíhající spory.
9. **Transakce a smlouvy v energetice.** Koupě/prodej výrobny (due diligence: licence, podpora, připojení, pozemky, dotace, přechod smluv), PPA (power purchase agreement - fyzická × virtuální, cena, profil, záruky původu, akontace, změna regulace), smlouva o výkupu přetoků, O&M smlouvy, EPC/ESCO, smlouvy o pachtu pozemku pro FVE (doba, výpověď, obnovení pozemku, věcné břemeno, předkupní právo), financování (zástava výrobny a pohledávek z podpory, step-in), pojištění, dotace a udržitelnost.

## Časté pasti

- Výpověď smlouvy o dodávce podaná pozdě (po 10denní lhůtě před účinností změny) - fixace dál trvá, smluvní pokuta.
- Smluvní pokuta za předčasné ukončení nad zákonný limit nebo u smlouvy uzavřené podomně bez řádného poučení - napadnutelná, ale klient musí namítat.
- Spor o připojení hnán k soudu - pravomoc má ERÚ (§ 17 odst. 7); a naopak spor o náhradu škody k ERÚ.
- Výrobna nad limit bez licence - neoprávněné podnikání, přestupek, ztráta podpory.
- FVE postavená bez povolení na budově, kde limit neplatí (památka, změna vzhledu) - odstranění.
- Kombinace dotace + provozní podpora bez přepočtu - překompenzace a vrácení.
- Sdílení elektřiny bez registrace v EDC nebo nad limit odběrných míst - nefunguje, distribuční poplatky v plné výši.
- Energetické společenství založené jako podnikatelská s.r.o. - nesplní podmínky registrace.
- Odpojení od CZT bez souhlasu a bez úhrady - spor s teplárnou, nutnost splnit podmínky § 77.
- PENB chybějící při prodeji - pokuta SEI, riziko slevy z ceny.
- Pacht pozemku pro FVE na 10 let s automatickým prodloužením bez souhlasu vlastníka - neplatné části, nedostatek zajištění pro banku.
- Cenové rozhodnutí ERÚ přepsané z paměti nebo předchozího roku - vždy aktuální rok.
- Doplňování čísel vyhlášek, limitů výkonu, sazeb podpory a dat z paměti - vždy z aktuálního znění nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat, u koho - dodavatel/distributor/ERÚ/SEI/soud, do kdy).
2. **Kvalifikace** - role, komodita, smluvní typ, datum, regulační rok, použitelné znění EZ.
3. **Právní rámec** - energetický zákon / POZE / vyhlášky / cenové rozhodnutí / EU v aktuálním znění, s odkazy.
4. **Postup a nároky** - tabulka: krok/nárok | právní základ | orgán/protistrana | lhůta | riziko.
5. **Regulační a dotační dopady** (licence, podpora, překompenzace, veřejná podpora).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. NSS a ÚS.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 As 123/2024 - …`, `ÚS - Pl. ÚS 17/11 - 15.05.2012`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejméně 30 dnů před účinností“, „nejpozději desátý den před účinností“, „pro vlastní spotřebu“, „převažující veřejný zájem“).
- Jeden časový řez; znění EZ a cenové rozhodnutí účinné k datu smlouvy / události / regulačního roku.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu (EZ se mění několikrát ročně).
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Limity výkonu, lhůty, sazby podpory, ceny a čísla vyhlášek nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o licencích, výrobnách a dodavatelích výhradně z registrů ERÚ a OTE; mimo CODEXIS jen oficiální zdroje (eru.gov.cz, ote-cr.cz, mpo.gov.cz, cr-sei.cz) když CODEXIS neodpovídá.
