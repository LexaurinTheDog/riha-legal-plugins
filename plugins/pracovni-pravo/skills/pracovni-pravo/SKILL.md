---
uuid: 86ca962b-ddad-4712-a9ed-fb012f3fe23a
name: pracovni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Pracovní právo ČR"
    summary: "Pracovní poměr od vzniku po skončení - výpověď a její neplatnost, odstupné, mzda a pracovní doba, odpovědnost, konkurenční doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zaměstnavatel chce dát výpověď pro nadbytečnost zaměstnanci, který je 3 měsíce v pracovní neschopnosti. Lze to a jak?"
      - "Klient dostal okamžité zrušení pracovního poměru za pozdní příchody. Je to platné a do kdy se bránit?"
      - "Připrav konkurenční doložku pro obchodního ředitele tak, aby byla vymahatelná."
  en:
    displayName: "Czech Labour Law"
    summary: "Employment from formation to termination - notice and its invalidity, severance, pay and working time, liability, non-compete, agreements outside employment, disguised employment, disputes."
    examplePrompts:
      - "An employer wants to give redundancy notice to an employee who has been on sick leave for 3 months. Is it possible and how?"
      - "My client received an immediate termination for late arrivals. Is it valid and by when must they challenge it?"
      - "Draft a non-compete clause for a sales director so that it is enforceable."
  sk:
    displayName: "Pracovné právo ČR"
    summary: "Český pracovný pomer od vzniku po skončenie - výpoveď a jej neplatnosť, odstupné, mzda a pracovný čas, zodpovednosť, konkurenčná doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zamestnávateľ chce dať výpoveď pre nadbytočnosť zamestnancovi, ktorý je 3 mesiace práceneschopný. Dá sa to a ako?"
      - "Klient dostal okamžité zrušenie pracovného pomeru za neskoré príchody. Je platné a dokedy sa brániť?"
      - "Priprav konkurenčnú doložku pre obchodného riaditeľa tak, aby bola vymáhateľná."
description: Use when the user's matter involves Czech employment or labour law from either side (zaměstnavatel, zaměstnanec, HR, odbory) - zákoník práce (262/2006 Sb.), pracovní smlouva, zkušební doba, pracovní poměr na dobu určitou, DPP, DPČ, výpověď, výpovědní důvody, výpovědní doba, okamžité zrušení, dohoda o rozvázání, zrušení ve zkušební době, neplatnost rozvázání pracovního poměru, ochranná doba, odstupné, mzda, plat, minimální mzda, přesčasy, pracovní doba, dovolená, překážky v práci, home office, pracovní úraz, náhrada škody zaměstnancem, konkurenční doložka, mlčenlivost, přechod práv a povinností, hromadné propouštění, agenturní zaměstnávání, švarcsystém, nelegální práce, inspekce práce, diskriminace, whistleblowing, doručování písemností zaměstnanci, pracovněprávní spor. Standalone skill - bundles CODEXIS methodology with labour-law method; no need to load the general codexis skill.
---

# Pracovní právo ČR

Samostatný oborový skill pro pracovněprávní vztahy. Pracovní právo je jednostranně kogentní (§ 4a ZP - odchýlit se lze jen ve prospěch zaměstnance) a plné **prekluzivních lhůt** (§ 330 ZP) - proto nejprve lhůta a forma, teprve pak merit.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/262/2006/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf52'`, `cdx-cli search JD --query "neplatnost výpovědi nadbytečnost 52 c" --court "Nejvyšší soud" --limit 5`.
- Zákoník práce prošel rozsáhlými novelami (2023 - dohody a home office, tzv. flexinovela účinná od 1. 6. 2025 - zkušební doba, běh výpovědní doby, výpovědní důvody, rodičovská dovolená). **Každou lhůtu, násobek, limit hodin a číslo odstavce ověř v aktuálním znění a podle data právního jednání**, nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| ZP - zákoník práce | 262/2006 Sb. | `cz_law/262/2006` | Vznik (§ 33+), skončení (§ 48-§ 73a), pracovní doba (§ 78+), mzda (§ 109+), překážky (§ 191+), dovolená (§ 211+), náhrada škody (§ 248+), dohody (§ 74-§ 77), konkurenční doložka (§ 310), doručování (§ 334-§ 337), lhůty (§ 329-§ 333) |
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Subsidiárně (§ 4 ZP) - právní jednání, neplatnost, promlčení; zakázané instituty § 346d ZP |
| Zákon o zaměstnanosti | 435/2004 Sb. | `cz_law/435/2004` | Nelegální práce (švarcsystém), agenturní zaměstnávání, cizinci, hromadné propouštění - součinnost s ÚP |
| Zákon o inspekci práce | 251/2005 Sb. | `cz_law/251/2005` | Přestupky zaměstnavatele, kontrola, sankce |
| Antidiskriminační zákon | 198/2009 Sb. | `cz_law/198/2009` | Diskriminace, obrácené důkazní břemeno (§ 133a o. s. ř.) |
| NV o minimální mzdě | 567/2006 Sb. | `cz_law/567/2006` | Minimální a zaručená mzda (od 2025 valorizace dle § 111 ZP - ověř) |
| Zákon o ochraně oznamovatelů | 171/2023 Sb. | `cz_law/171/2023` | Whistleblowing, zákaz odvetných opatření |
| Zákon o nemocenském pojištění | 187/2006 Sb. | `cz_law/187/2006` | Nemocenská, ochranná doba, mateřská |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Pracovní spory u okresního soudu (§ 9 odst. 1), přesun důkazního břemene |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu právního jednání** (výpověď se posuzuje podle znění účinného v den doručení) → `/toc` → `/text?part=`.
2. Judikatura NS: senát **21 Cdo** (pracovní právo) - `--court "Nejvyšší soud"`; klíčová témata: nadbytečnost a příčinná souvislost, porušení povinnosti „zvlášť hrubým způsobem", doručování, konkurenční doložka, švarcsystém. Ověř, zda rozhodnutí nevychází ze znění před novelou.
3. Komentář (`COMMENT`) k pojmům bez legální definice („závažné porušení", „soustavné méně závažné", „organizační změna"); vzory (`VS`) pro pracovní smlouvu, výpověď, dohodu - vždy sladit s aktuálním zněním.

## Workflow pracovněprávního praktika

1. **Strana a cíl.** Zaměstnavatel × zaměstnanec × odbory; cíl (skončit vztah, ubránit se, vymoci mzdu, nastavit smlouvu). Totéž ustanovení radí každé straně opačně.
2. **Lhůta a forma nejdřív.** Neplatnost rozvázání - žaloba do **2 měsíců** od skončení (§ 72 ZP, prekluze § 330); okamžité zrušení - **2 měsíce** subjektivní / 1 rok objektivní (§ 58); výpověď a okamžité zrušení **písemně** a doručeny **do vlastních rukou** (§ 334-§ 337; e-mail jen se souhlasem a s uznávaným elektronickým podpisem), jinak zdánlivé/neplatné. Ověř aktuální znění lhůt i pravidel doručování.
3. **Kvalifikace vztahu.** Pracovní poměr × DPP/DPČ (§ 74-§ 77, limity hodin) × agenturní zaměstnání (§ 307a+) × OSVČ - test závislé práce (§ 2-§ 3 ZP): nadřízenost, jménem zaměstnavatele, pokyny, osobní výkon; nelegální práce dle § 5 zákona 435/2004 Sb. Zastřený pracovní poměr = sankce inspekce + doměrky.
4. **Skončení pracovního poměru** (§ 48+): dohoda (§ 49) × výpověď (§ 50-§ 54; zaměstnavatel jen z taxativních důvodů § 52; zaměstnanec bez důvodu) × okamžité zrušení (§ 55 zaměstnavatel, § 56 zaměstnanec) × zrušení ve zkušební době (§ 66) × uplynutí doby. Kontrola: důvod skutkově vymezený tak, aby nebyl zaměnitelný (§ 50 odst. 4), ochranná doba (§ 53 - PN, těhotenství, mateřská, vojenské cvičení; výjimky § 54), předchozí projednání s odbory / souhlas u funkcionáře (§ 61), výpovědní doba a její běh (§ 51 - po flexinovele od doručení; ověř), odstupné (§ 67 - násobky podle důvodu a délky), potvrzení o zaměstnání (§ 313), nárok na podporu.
5. **Neplatnost a její následky.** Žaloba § 72; oznámení, že zaměstnanec trvá na dalším zaměstnávání (§ 69 odst. 1) - bez něj jen fikce skončení dohodou (§ 69 odst. 3); náhrada mzdy od oznámení, moderace nad 6 měsíců (§ 69 odst. 2); u zaměstnance § 70-§ 71.
6. **Mzda, doba, dovolená.** Minimální/zaručená mzda, příplatky (§ 114-§ 118), přesčas - limity a náhradní volno (§ 93), pracovní pohotovost, evidence pracovní doby (§ 96 - důkazní břemeno zaměstnavatele), dovolená v hodinách (§ 213), překážky (§ 191+), home office (§ 317 - písemná dohoda, náhrada nákladů).
7. **Odpovědnost.** Zaměstnanec: obecná odpovědnost limitovaná násobkem průměrného výdělku (§ 257 - ověř násobek), schodek na svěřených hodnotách (§ 252 - dohoda), ztráta věcí (§ 255); zaměstnavatel: plná, pracovní úraz a nemoc z povolání (§ 269+, zákonné pojištění), nemajetková újma.
8. **Ochranné a soutěžní klauzule.** Konkurenční doložka (§ 310 - písemně, nejdéle 1 rok, přiměřené peněžité vyrovnání, smluvní pokuta, odstoupení zaměstnavatele jen za trvání PP - ověř), mlčenlivost, zákaz jiné výdělečné činnosti (§ 304), monitoring (§ 316), ochrana osobních údajů.
9. **Spor.** Okresní soud (§ 9 odst. 1 o. s. ř.), osvobození od poplatku a náhrada nákladů ověř v ZSOP a AT; předžalobní výzva; obrácené důkazní břemeno u diskriminace (§ 133a o. s. ř.); podnět inspekci práce jako paralelní páka; mediace.

## Časté pasti

- Zmeškaná dvouměsíční prekluzivní lhůta k žalobě na neplatnost (§ 72) - nelze prominout ani zhojit.
- Výpověď doručená e-mailem bez souhlasu a uznávaného podpisu, nebo „vhozením do schránky" - vadné doručení, lhůty neběží.
- Výpovědní důvod popsaný obecně („organizační důvody") bez konkrétní organizační změny a příčinné souvislosti.
- Výpověď v ochranné době (§ 53) bez zkoumání výjimek § 54.
- Okamžité zrušení za jednání, které je jen „závažným" (nikoli „zvlášť hrubým") porušením - správně výpověď § 52 písm. g).
- Aplikace znění zákoníku před flexinovelou 2025 (zkušební doba, běh výpovědní doby) nebo naopak na starší jednání.
- Smluvní pokuta nebo zajištění dluhu zaměstnance mimo konkurenční doložku - zakázáno (§ 346d).
- Konkurenční doložka bez peněžitého vyrovnání nebo delší než 1 rok - neplatná.
- DPP/DPČ nad zákonný limit hodin nebo bez rozvrhu směn po novele 2023.
- „Fakturující zaměstnanec" (švarcsystém) posuzovaný jen podle názvu smlouvy, ne podle znaků závislé práce.
- Doplňování mzdy, data doručení a názvů z paměti - vždy z listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a lhůta** v první větě (lze/nelze, co udělat, do kdy).
2. **Strana a kvalifikace vztahu.**
3. **Právní rámec** - ZP v aktuálním znění k datu jednání, s odkazy.
4. **Postup krok za krokem** (forma, doručení, odbory, obsah listiny, odstupné, potvrzení).
5. **Rizika a alternativy** (dohoda × výpověď, náhrada mzdy, sankce inspekce).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 21 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejpozději do“, „ode dne doručení“, „zvlášť hrubým způsobem“, „soustavně“).
- Jeden časový řez; u skončení PP znění účinné v den doručení.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (MPSV, SUIP, ČSSZ, justice.cz) když CODEXIS neodpovídá.
- Násobky, limity hodin, sazby a lhůty nikdy z paměti - vždy z aktuálního znění s odkazem.
