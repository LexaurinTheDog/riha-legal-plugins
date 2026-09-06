---
uuid: 015058f2-7c5f-4934-91d7-c119db1e640c
name: zdravotnicke-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Zdravotnické právo ČR"
    summary: "Práva pacienta a informovaný souhlas, zdravotnická dokumentace, újma na zdraví a postup non lege artis, stížnosti a disciplinární řízení, úhrady z veřejného zdravotního pojištění, provoz poskytovatelů."
    examplePrompts:
      - "Po operaci zůstaly klientce trvalé následky a nikdo ji nepoučil o rizicích. Jaké nároky má, proti komu a jaká běží promlčecí lhůta?"
      - "Pojišťovna zamítla úhradu léčby podle § 16. Jak se odvolat a s jakou argumentací?"
      - "Nemocnice odmítá vydat kopii zdravotnické dokumentace zemřelého otce. Kdo má na ni právo a v jaké lhůtě?"
  en:
    displayName: "Czech Medical and Health Law"
    summary: "Patient rights and informed consent, medical records, malpractice and injury claims, complaints and disciplinary proceedings, public health insurance coverage, provider licensing and compliance."
    examplePrompts:
      - "After surgery my client has permanent consequences and nobody informed her about the risks. Which claims, against whom, and what limitation period runs?"
      - "The insurer rejected coverage of treatment under § 16. How to appeal and with what arguments?"
      - "A hospital refuses to release a copy of the medical records of a deceased father. Who is entitled and within what period?"
  sk:
    displayName: "Zdravotnícke právo ČR"
    summary: "Práva pacienta a informovaný súhlas, zdravotná dokumentácia, ujma na zdraví a postup non lege artis, sťažnosti a disciplinárne konania, úhrady z verejného zdravotného poistenia, prevádzka poskytovateľov v ČR."
    examplePrompts:
      - "Po operácii zostali klientke trvalé následky a nikto ju nepoučil o rizikách. Aké nároky má, proti komu a aká beží premlčacia lehota?"
      - "Poisťovňa zamietla úhradu liečby podľa § 16. Ako sa odvolať a s akou argumentáciou?"
      - "Nemocnica odmieta vydať kópiu zdravotnej dokumentácie zosnulého otca. Kto má na ňu právo a v akej lehote?"
description: Use when the user's matter involves Czech health care, patients or providers - zákon o zdravotních službách (372/2011 Sb.), zákon o veřejném zdravotním pojištění (48/1997 Sb.), pacient, práva pacienta, informovaný souhlas, negativní revers, dříve vyslovené přání, nezletilý pacient, zdravotnická dokumentace, nahlížení, kopie dokumentace, mlčenlivost, postup lege artis, non lege artis, pochybení lékaře, újma na zdraví, bolestné, ztížení společenského uplatnění, nemajetková újma pozůstalých, ztráta šance, znalecký posudek, stížnost na poskytovatele, krajský úřad, Česká lékařská komora, disciplinární řízení, úhrada péče, § 16 mimořádná úhrada, smlouva s pojišťovnou, oprávnění k poskytování zdravotních služeb, pracovnělékařské služby, lékařský posudek, trestní odpovědnost lékaře. Standalone skill - bundles CODEXIS methodology with health-law method; no need to load the general codexis skill.
---

# Zdravotnické právo ČR

Samostatný oborový skill pro vztahy pacient - poskytovatel - pojišťovna - stát. Nejčastější chyba je záměna cest: **stížnost, disciplinární řízení, trestní oznámení a žaloba o náhradu újmy jsou čtyři nezávislé cesty s různými lhůtami**, a žádná z nich není podmínkou ostatních. Promlčení se počítá od vědomosti o újmě a škůdci, ne od zákroku.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/372/2011/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf34'`, `cdx-cli get cdx://cz_law/48/1997/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2958'`, `cdx-cli search JD --query "informovaný souhlas absence poučení odpovědnost poskytovatele" --court "Nejvyšší soud" --limit 5`.
- Lhůty, sazby, bodová hodnocení a podmínky úhrad **ověř v aktuálním znění**; Metodika Nejvyššího soudu k § 2958 OZ je doporučující pomůcka, ne právní předpis - uváděj ji jako orientaci. Nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o zdravotních službách | 372/2011 Sb. | `cz_law/372/2011` | Práva pacienta (§ 28+), informace a souhlas (§ 31-§ 36), péče bez souhlasu (§ 38), povinnosti poskytovatele (§ 45+), odmítnutí pacienta (§ 48), mlčenlivost (§ 51), dokumentace (§ 53-§ 69), stížnosti (§ 93-§ 97), oprávnění (§ 11+), přestupky (§ 114+) |
| Zákon o specifických zdravotních službách | 373/2011 Sb. | `cz_law/373/2011` | Pracovnělékařské služby a posudky (§ 41+, přezkum § 46), sterilizace, asistovaná reprodukce, genetika |
| Zákon o veřejném zdravotním pojištění | 48/1997 Sb. | `cz_law/48/1997` | Práva pojištěnce (§ 11), hrazené služby (§ 13+), mimořádná úhrada (§ 16), smlouvy (§ 17), revizní činnost (§ 42), regres (§ 55) |
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Zásahy do integrity (§ 91-§ 103), smlouva o péči o zdraví (§ 2636-§ 2651), náhrada újmy (§ 2894+, § 2910, § 2913), újma na zdraví (§ 2958-§ 2968), promlčení (§ 620, § 636) |
| Úmluva o lidských právech a biomedicíně | 96/2001 Sb. m. s. | `cz_law/96/2001` | Souhlas (čl. 5+), informace (čl. 10), nadřazenost nad zákonem |
| Zákon o ochraně veřejného zdraví | 258/2000 Sb. | `cz_law/258/2000` | Očkování, epidemická opatření, KHS |
| Zákon o léčivech / o zdravotnických prostředcích | 378/2007 / 375/2022 Sb. | `cz_law/378/2007`, `cz_law/375/2022` | SÚKL, předepisování, reklama, vigilance |
| Zákony o způsobilosti zdravotnických pracovníků | 95/2004, 96/2004 Sb. | `cz_law/95/2004`, `cz_law/96/2004` | Kvalifikace, specializace, odborný dohled |
| Zákon o komorách | 220/1991 Sb. | `cz_law/220/1991` | ČLK, ČSK, ČLnK - disciplinární pravomoc |
| Vyhlášky o dokumentaci, personálním a věcném vybavení | 98/2012, 99/2012, 92/2012 Sb. | `cz_law/98/2012`, `cz_law/99/2012`, `cz_law/92/2012` | Obsah a uchovávání dokumentace, minimální požadavky |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Usmrcení a ublížení z nedbalosti (§ 143, § 147-§ 148), neposkytnutí pomoci (§ 150), neoprávněné nakládání s údaji (§ 180) |
| GDPR + zákon 110/2019 Sb. | (EU) 2016/679 | zdroj `EU`, `cz_law/110/2019` | Zvláštní kategorie údajů (čl. 9), incidenty, práva subjektu |

## Rešeršní strategie

1. Paragraf známý → `/versions` k datu zákroku / rozhodnutí → `/toc` → `/text?part=`.
2. Judikatura: **NS** senát 25 Cdo (újma na zdraví, lege artis, informovaný souhlas, ztráta šance, Metodika), **ÚS** (práva pacienta, § 16, očkování, autonomie), **NSS** (§ 16 úhrady, oprávnění poskytovatelů, KHS, posudky), **ESLP** (`ES` - čl. 8 Úmluvy, biomedicína). Ověř datum a zda rozhodnutí nevychází ze zrušené právní úpravy (zákon 20/1966 Sb.).
3. Komentář (`COMMENT`) k pojmům (náležitá odborná úroveň, přiměřené poučení, osoba blízká, neodkladná péče); Metodika NS a stanoviska ČLK jako orientace, ne pramen.

## Workflow

1. **Role a cesta.** Pacient / pozůstalí × poskytovatel × zdravotnický pracovník × pojišťovna × zaměstnavatel × orgán (KÚ, KHS, SÚKL, ČLK). Věc: náhrada újmy × práva pacienta a dokumentace × úhrada péče × stížnost / disciplína × přestupek / trestní odpovědnost × provoz a smlouvy × posudková péče. Cesty se nevylučují - navrhni pořadí a promlčení pro každou.
2. **Důkazy hned.** Kopie zdravotnické dokumentace (§ 65-§ 66 - právo pacienta, osob určených pacientem a osob blízkých u zemřelého; lhůta poskytovatele pro pořízení kopie - ověř), záznam poučení a souhlasu, operační protokol, výsledky, svědci; u úmrtí pitevní protokol; datum vědomosti o újmě zaznamenat pro promlčení.
3. **Odpovědnost za újmu na zdraví.** Titul: smluvní (§ 2913 ve spojení se smlouvou o péči o zdraví § 2636+) × deliktní (§ 2910); postup **lege artis** (§ 4 odst. 5 zák. 372/2011 Sb. - náležitá odborná úroveň podle pravidel vědy a uznávaných postupů, s ohledem na individualitu a konkrétní podmínky); **absence informovaného souhlasu** (§ 31, § 34 - poučení o povaze, účelu, rizicích, alternativách; písemná forma kde zákon nebo poskytovatel stanoví) = protiprávní zásah do integrity i při lege artis postupu; příčinná souvislost (znalecký posudek z oboru zdravotnictví, teorie ztráty šance - ověř aktuální judikaturu NS), zavinění (domněnka nedbalosti § 2911), exkulpace, spoluzavinění pacienta (§ 2918). Odpovídá poskytovatel (za zaměstnance § 2914), pojištění odpovědnosti poskytovatele (§ 45 odst. 2).
4. **Nároky a jejich výše.** Bolestné a ztížení společenského uplatnění (§ 2958 - plné odčinění, Metodika NS jako pomůcka: bodové hodnocení bolesti, ztížení podle MKF), duševní útrapy osob blízkých (§ 2959), náklady léčení a péče (§ 2960), ztráta na výdělku a důchodu (§ 2962-§ 2964), výživa pozůstalým (§ 2966), náklady pohřbu (§ 2961), nemajetková újma za neoprávněný zásah (§ 2956-§ 2957); renta; úroky z prodlení od výzvy. **Promlčení**: subjektivní od vědomosti o újmě a škůdci, objektivní 10 let od události, u úmyslu 15 (§ 620, § 636 - ověř; § 636 odst. 3 u újmy na zdraví bez objektivní lhůty - ověř).
5. **Procesní cesta.** Předžalobní výzva (§ 142a o. s. ř.) a jednání s pojistitelem poskytovatele, mediace, žaloba u okresního soudu, soudní poplatek (osvobození u újmy na zdraví - ověř § 11 ZSOP), znalec (§ 127 o. s. ř., seznam znalců, obor zdravotnictví - správné odvětví), předběžné opatření na výživné/rentu; souběžně stížnost a trestní oznámení jako důkazní páky (trestní spis se znaleckým posudkem).
6. **Stížnost a disciplína.** Stížnost poskytovateli (§ 93 - lhůta pro vyřízení 30 dnů - ověř) → krajskému úřadu (§ 94 - nezávislý odborník / komise) → správní žaloba jen výjimečně; stížnost komoře (ČLK, ČSK - disciplinární řízení podle zákona 220/1991 Sb., lhůty pro zahájení - ověř); přestupky poskytovatele (§ 114+ zák. 372/2011 Sb.); trestní odpovědnost lékaře (§ 143, § 147-§ 148 TZ - nedbalost, subsidiarita trestní represe).
7. **Práva pacienta a dokumentace.** Právo na informace a druhý názor (§ 31), odmítnutí péče a negativní revers (§ 34 odst. 3), dříve vyslovené přání (§ 36 - forma, platnost), nezletilí (§ 35 - souhlas zákonného zástupce, názor dítěte, jeden × oba rodiče - ověř), pacienti s omezenou svéprávností, hospitalizace bez souhlasu (§ 38, soudní přezkum § 75+ ZŘS - detenční řízení), určení osob s právem na informace (§ 33), mlčenlivost a výjimky (§ 51), nahlížení a kopie (§ 65-§ 66), uchovávání a skartace (vyhláška 98/2012 Sb.), GDPR čl. 9.
8. **Úhrady a pojišťovna.** Hrazené služby (§ 13+ zák. 48/1997 Sb.), **§ 16 mimořádná úhrada** (jediná možnost z hlediska zdravotního stavu, výjimečnost; správní řízení, lhůty pro rozhodnutí, odvolání, žaloba - ověř aktuální procesní úpravu a judikaturu NSS/ÚS), léčiva a prostředky (SÚKL, úhradová vyhláška), regulační poplatky a doplatky, regres pojišťovny (§ 55 - proti tomu, kdo újmu zavinil), smlouvy poskytovatelů (§ 17 - výběrové řízení, rámcová smlouva, úhradová vyhláška), revizní činnost a vratky.
9. **Provoz poskytovatele.** Oprávnění (§ 11+ - žádost KÚ, odborný zástupce, personální a věcné vybavení), změny a převod praxe (přechod dokumentace § 57), pracovnělékařské služby a posudky (§ 41+ zák. 373/2011 Sb. - přezkum posudku 10 pracovních dnů - ověř), kontrola KÚ/KHS/SÚKL, reklama na léčiva, mlčenlivost personálu, kamery a GDPR, smlouvy s lékaři (výkon funkce × pracovní poměr), odpovědnostní pojištění.

## Časté pasti

- Promlčení počítané od zákroku místo od vědomosti o újmě a škůdci (a naopak objektivní lhůta u pozdě projevené újmy - ověř § 636 odst. 3).
- Žaloba jen na non lege artis postup, ač chybí doložený informovaný souhlas - samostatný a často snadněji prokazatelný důvod.
- Stížnost nebo disciplinární řízení bráno jako podmínka žaloby - není; naopak jejich výsledek nezavazuje civilní soud.
- Metodika NS aplikovaná jako tabulka s nárokem - jen pomůcka; soud může vybočit oběma směry.
- Kopie dokumentace požadována osobou, kterou pacient neurčil, nebo bez doložení postavení osoby blízké u zemřelého.
- Znalec z nesprávného odvětví nebo bez specializace - posudek napadnutelný.
- § 16 žádost bez lékařské zprávy o „jediné možnosti" a bez vyčerpání hrazených alternativ; zmeškání lhůty k odvolání.
- Nezletilý pacient a souhlas jen jednoho rodiče u závažného zákroku - ověř § 35 a judikaturu.
- Dříve vyslovené přání bez zákonné formy nebo ignorované bez zápisu důvodu.
- Hospitalizace bez souhlasu neoznámená soudu ve lhůtě 24 hodin (ověř § 40 zák. 372/2011 Sb.).
- Pracovnělékařský posudek napadený u soudu místo přezkumu u poskytovatele a KÚ.
- Doplňování diagnóz, dat zákroků, jmen lékařů a bodů z paměti - vždy z dokumentace nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (které cesty, v jakém pořadí, do kdy; důkazy zajistit hned).
2. **Role a kvalifikace věci** (odpovědnost / práva / úhrada / disciplína / provoz).
3. **Právní rámec** - 372/2011, 48/1997, OZ v aktuálním znění, s odkazy.
4. **Nároky nebo postup** - tabulka: nárok/krok | právní základ | adresát | lhůta | důkaz.
5. **Rizika a alternativy** (mimosoudní dohoda s pojistitelem, mediace, náklady znalce, délka řízení).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace; Metodika NS jako orientace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 25 Cdo 1234/2024 - …`, `ÚS - I. ÚS 123/25 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („náležitá odborná úroveň“, „s vysokou pravděpodobností“, „jediná možnost z hlediska zdravotního stavu“, „ode dne, kdy se dozvěděl“).
- Jeden časový řez; u zákroku znění účinné v den zákroku.
- Zdravotní údaje uváděj jen v nezbytném rozsahu; lékařské závěry nikdy nenahrazuj vlastním úsudkem - odkazuj na znalce.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty, body, sazby a podmínky úhrad nikdy z paměti - vždy z aktuálního znění s odkazem.
- Mimo CODEXIS jen oficiální zdroje (mzcr.gov.cz, sukl.cz, uzis.cz, vzp.cz a další pojišťovny, lkcr.cz, nsoud.cz - Metodika) když CODEXIS neodpovídá.
