---
uuid: 0b290d1c-3e5c-4ec8-80ad-01d4bf6e40ba
name: cizinecke-a-azylove-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Cizinecké a azylové právo ČR"
    summary: "Víza a pobytová oprávnění, zaměstnanecké a modré karty, občané EU a rodinní příslušníci, vyhoštění a zajištění, mezinárodní a dočasná ochrana, státní občanství, zaměstnávání cizinců."
    examplePrompts:
      - "Zaměstnanci z Ukrajiny končí za tři týdny zaměstnanecká karta a chce změnit zaměstnavatele. Co a v jakém pořadí podat?"
      - "Klientovi bylo uloženo správní vyhoštění se zákazem vstupu na 2 roky. Jaké lhůty běží a jak se bránit?"
      - "Firma chce zaměstnat programátora z Indie. Jaké oprávnění potřebuje a jak dlouho to trvá?"
  en:
    displayName: "Czech Immigration and Asylum Law"
    summary: "Visas and residence permits, employee and blue cards, EU citizens and family members, expulsion and detention, international and temporary protection, citizenship, employment of foreigners."
    examplePrompts:
      - "A Ukrainian employee's employee card expires in three weeks and she wants to change employer. What to file and in what order?"
      - "My client received administrative expulsion with a 2-year entry ban. Which deadlines run and how to defend?"
      - "A company wants to hire a programmer from India. Which permit is needed and how long does it take?"
  sk:
    displayName: "Cudzinecké a azylové právo ČR"
    summary: "Víza a pobytové oprávnenia v ČR, zamestnanecké a modré karty, občania EÚ a rodinní príslušníci, vyhostenie a zaistenie, medzinárodná a dočasná ochrana, štátne občianstvo, zamestnávanie cudzincov."
    examplePrompts:
      - "Zamestnankyni z Ukrajiny končí o tri týždne zamestnanecká karta a chce zmeniť zamestnávateľa. Čo a v akom poradí podať?"
      - "Klientovi bolo uložené správne vyhostenie so zákazom vstupu na 2 roky. Aké lehoty bežia a ako sa brániť?"
      - "Firma chce zamestnať programátora z Indie. Aké oprávnenie potrebuje a ako dlho to trvá?"
description: Use when the user's matter involves foreigners in the Czech Republic - zákon o pobytu cizinců (326/1999 Sb.), zákon o azylu (325/1999 Sb.), vízum, krátkodobé, dlouhodobé vízum, dlouhodobý pobyt, přechodný pobyt, trvalý pobyt, zaměstnanecká karta, modrá karta, karta vnitropodnikově převedeného zaměstnance, sloučení rodiny, studium, podnikání cizince, občan EU, rodinný příslušník občana EU, fikce pobytu, překlenovací štítek, Komise pro rozhodování ve věcech pobytu cizinců, OAMP, zastupitelský úřad, správní vyhoštění, zákaz vstupu, zajištění cizince, návrat, Dublin, mezinárodní ochrana, azyl, doplňková ochrana, dočasná ochrana, Ukrajina, Lex Ukrajina, státní občanství (186/2013 Sb.), zaměstnávání cizinců (435/2004 Sb.), povolení k zaměstnání, nelegální práce, agenturní zaměstnávání cizinců, schengenský prostor, cestovní doklad, ohlašovací povinnost. Standalone skill - bundles CODEXIS methodology with immigration-practice method; no need to load the general codexis skill.
---

# Cizinecké a azylové právo ČR

Samostatný oborový skill pro pobyt, zaměstnávání a ochranu cizinců. Dvě věci před vším ostatním: **status osoby** (občan EU / rodinný příslušník / třetizemec / žadatel o ochranu / držitel dočasné ochrany) a **den, kdy končí stávající oprávnění** - cizinecké lhůty jsou krátké, žaloby mají dny, ne měsíce, a žádost podaná o den později ztrácí fikci pobytu.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/326/1999/versions`, `cdx-cli get 'cdx://doc/<versionId>/toc'`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf42g'`, `cdx-cli get cdx://cz_law/325/1999/versions`, `cdx-cli search JD --query "správní vyhoštění přiměřenost zásah do soukromého a rodinného života" --court "Nejvyšší správní soud" --limit 5`.
- Zákon o pobytu cizinců je jeden z nejčastěji novelizovaných předpisů (dočasná ochrana, digitalizace, migrační a azylový pakt EU použitelný od roku 2026, případná rekodifikace). **Každý §, lhůtu, poplatek a podmínku ověř přes `/versions` k datu podání**; číslování paragrafů s písmeny (§ 42g, § 169t) dohledávej přes `/toc`. Aktuální formuláře, poplatky a objednávkové systémy čerpej z mvcr.gov.cz a mzv.gov.cz.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o pobytu cizinců | 326/1999 Sb. | `cz_law/326/1999` | Víza, dlouhodobý pobyt a karty (§ 42+), trvalý pobyt (§ 65+), občané EU a rodinní příslušníci (§ 87a+), vyhoštění (§ 118+), zajištění (§ 124+), řízení a lhůty (§ 168-§ 172), přestupky |
| Zákon o azylu | 325/1999 Sb. | `cz_law/325/1999` | Azyl (§ 12), doplňková ochrana (§ 14a), řízení, nepřípustnost a zjevná nedůvodnost, lhůty pro žalobu (§ 32), kasační stížnost (§ 104a s. ř. s.) |
| Zákon o dočasné ochraně cizinců | 221/2003 Sb. + zákony „Lex Ukrajina" (65/2022 Sb. a novely) | `cz_law/221/2003`, `cz_law/65/2022` | Dočasná ochrana, prodlužování, přechod na jiný pobyt |
| Zákon o státním občanství | 186/2013 Sb. | `cz_law/186/2013` | Udělení (§ 14 - pobyt, jazyk, bezúhonnost, příjmy), prohlášení, pozbytí |
| Zákon o zaměstnanosti | 435/2004 Sb. | `cz_law/435/2004` | Povolení k zaměstnání, volný přístup na trh práce (§ 98), informační povinnost zaměstnavatele, nelegální práce a sankce, agentury |
| Správní řád / s. ř. s. | 500/2004 / 150/2002 Sb. | `cz_law/500/2004`, `cz_law/150/2002` | Subsidiárně; žaloby a kasační stížnosti, odkladný účinek |
| Schengenský hraniční kodex / vízový kodex | (EU) 2016/399 / (ES) 810/2009 | zdroj `EU` | Vstup, krátkodobá víza, 90/180 |
| Směrnice o volném pohybu / o dlouhodobě pobývajících rezidentech / návratová | 2004/38/ES, 2003/109/ES, 2008/115/ES | zdroj `EU` | Občané EU, rezidenti, návrat a zajištění |
| Nařízení Dublin III + migrační a azylový pakt | (EU) 604/2013, balík 2024 | zdroj `EU` | Příslušný stát, přemístění, nový azylový rámec (ověř použitelnost) |
| Zákon o správních poplatcích | 634/2004 Sb. | `cz_law/634/2004` | Poplatky za žádosti (položky - ověř) |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Trest vyhoštění (§ 80), maření výkonu (§ 337), napomáhání k nedovolenému pobytu (§ 341) |

## Rešeršní strategie

1. `/versions` k datu podání → `/toc` (paragrafy s písmeny!) → `/text?part=`; unijní předpisy ze zdroje `EU`.
2. Judikatura: **NSS** (`--court "Nejvyšší správní soud"`, senáty Azs - azyl i pobyt) - přiměřenost vyhoštění (čl. 8 Úmluvy), účelové sňatky, fikce pobytu, zajištění, nepřijatelnost kasační stížnosti; **ÚS** a **ESLP** (`ES` - čl. 3, čl. 5, čl. 8 Úmluvy), **SDEU** (`ES` - směrnice o volném pohybu, návratová, Dublin). Ověř, zda rozhodnutí nevychází z předchozího znění.
3. Komentář (`COMMENT`) k pojmům (rodinný příslušník, přiměřenost, pronásledování, vážná újma); metodiky a informace MV jsou administrativní výklad - u lhůt a formulářů však praktický zdroj.

## Workflow

1. **Status a cíl.** Občan EU × rodinný příslušník občana EU (vč. českého občana - ověř režim) × třetizemec s pobytem × žadatel o mezinárodní ochranu × držitel dočasné ochrany × bez oprávnění. Cíl: vstup, pobyt, zaměstnání, podnikání, sloučení rodiny, studium, trvalý pobyt, občanství, obrana proti vyhoštění/zajištění.
2. **Časová osa.** Den konce oprávnění, **žádost o prodloužení / změnu podat před uplynutím** (fikce oprávněného pobytu do rozhodnutí; překlenovací štítek; cestování v době fikce omezené), lhůty ministerstva pro rozhodnutí (§ 169t - ověř), nečinnost (§ 80 SŘ, žaloba § 79 s. ř. s.), doba zpracování na zastupitelském úřadu, objednání termínu.
3. **Pobytová oprávnění.** Krátkodobé vízum (90/180) × dlouhodobé vízum (účel) × dlouhodobý pobyt: zaměstnanecká karta (§ 42g - duální, vázaná na pracovní místo, změna zaměstnavatele oznámením v zákonné lhůtě - ověř), modrá karta (§ 42i - vysoká kvalifikace, mzdový práh), ICT karta, sloučení rodiny (§ 42a), studium, vědecký výzkum, podnikání; přechodný pobyt občana EU a rodinného příslušníka (§ 87a+, § 87b); trvalý pobyt po 5 letech nepřetržitého pobytu (§ 68 - přerušení, nepřítomnost, zkouška z jazyka - ověř) / po 2 letech u rodinných příslušníků; dlouhodobě pobývající rezident EU. Náležitosti: cestovní doklad, doklad o ubytování, prostředky, bezúhonnost, pojištění (komplexní zdravotní), poplatky.
4. **Zaměstnávání cizinců.** Volný přístup na trh práce (§ 98 zák. 435/2004 Sb. - trvalý pobyt, dočasná ochrana, studenti, sloučení…) × povolení k zaměstnání × zaměstnanecká/modrá karta; informační povinnost zaměstnavatele vůči ÚP, evidence; **nelegální práce** (výkon bez oprávnění k pobytu nebo k práci) - pokuty zaměstnavateli (ověř výši), úhrada nákladů vyhoštění, vyloučení z dotací; agenturní zaměstnávání cizinců (omezení - ověř); vysílání pracovníků (směrnice 96/71/ES).
5. **Řízení a opravné prostředky.** OAMP MV / zastupitelský úřad / Komise pro rozhodování ve věcech pobytu cizinců (odvolání 15 dnů); **žaloba ve zkrácených lhůtách** (§ 172 - 30 dnů; proti vyhoštění 10 dnů; ověř), vyloučení soudního přezkumu u některých rozhodnutí (§ 171 - krátkodobá víza), odkladný účinek ze zákona × na návrh, kasační stížnost (2 týdny, advokát), nepřijatelnost u azylu (§ 104a s. ř. s.); ústavní stížnost; ESLP (rule 39).
6. **Vyhoštění, zajištění, návrat.** Správní vyhoštění (§ 118-§ 120a - důvody, doba zákazu vstupu, přiměřenost dopadů do soukromého a rodinného života § 174a, závazné stanovisko k možnosti vycestování), dobrovolný návrat, **zajištění** (§ 124+ - důvody, maximální doba, soudní přezkum žalobou v krátké lhůtě, mírnější opatření § 123b, zvláštní ochrana zranitelných), Dublin přemístění, trest vyhoštění (§ 80 TZ), evidence nežádoucích osob, SIS.
7. **Mezinárodní ochrana.** Žádost a pohovor u OAMP, azyl (§ 12 - pronásledování) × doplňková ochrana (§ 14a - vážná újma) × humanitární azyl (§ 14), nepřípustnost / zjevná nedůvodnost (§ 10a, § 16), **žaloba ve lhůtě 15 dnů, u zjevně nedůvodných kratší** (§ 32 - ověř), pobyt po dobu řízení, práce po 6 měsících (ověř), zranitelné osoby, děti bez doprovodu, dočasná ochrana (Ukrajina) - prodlužování, zaměstnání volné, přechod na dlouhodobý pobyt zvláštního typu (ověř aktuální „Lex Ukrajina").
8. **Státní občanství.** Udělení (§ 14 zák. 186/2013 Sb. - trvalý pobyt 5/3 roky, nepřítomnost, bezúhonnost, jazyk B1 a reálie, příjmy, plnění povinností; bez nároku), prohlášení (§ 31+ - děti, druhá generace), nabytí narozením, pozbytí; správní uvážení a přezkum.

## Časté pasti

- Žádost o prodloužení nebo změnu podaná po uplynutí platnosti (i o den) - ztráta fikce, pobyt bez oprávnění, přestupek, riziko vyhoštění.
- Odvolání ke Komisi po 15 dnech, žaloba po 30 dnech (nebo po 10 dnech u vyhoštění) - počítáno „jako ve správním soudnictví" 2 měsíce je pozdě.
- Změna zaměstnavatele u zaměstnanecké karty bez včasného oznámení ministerstvu - práce bez oprávnění = nelegální práce obou stran.
- Pobytové oprávnění považováno za oprávnění k práci - u některých pobytů je nutné samostatné povolení nebo volný přístup podle § 98.
- Cestování mimo ČR v době fikce pobytu bez překlenovacího štítku / s prošlým vízem - nemožnost návratu.
- Trvalý pobyt počítaný bez zohlednění přerušení a nepřítomnosti; občanství žádané bez splnění příjmů a jazykové zkoušky.
- Dočasná ochrana zaměněna za azyl - jiný režim, jiné lhůty, jiný přechod na trvalý pobyt.
- Azylová žaloba podaná ve „standardní" lhůtě - lhůty 15 / 7 dnů (ověř), kasační stížnost bez advokáta nepřípustná.
- Zajištění napadené až po propuštění nebo bez využití mírnějších opatření.
- Sňatek nebo otcovství bez skutečného rodinného života - posuzováno jako účelové, zamítnutí a vyhoštění.
- Neověřené překlady, chybějící apostila / superlegalizace u zahraničních listin - žádost nepřijata.
- Doplňování čísel jednacích, dat konce platnosti a údajů z dokladů z paměti - vždy z listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co podat, kam, do kdy; co se stane při zmeškání).
2. **Status osoby a cíl.**
3. **Právní rámec** - zákon o pobytu cizinců / azylu / zaměstnanosti v aktuálním znění k datu podání, s odkazy.
4. **Postup krok za krokem** (formulář, náležitosti, poplatek, místo podání, lhůta rozhodnutí, fikce).
5. **Rizika a alternativy** (jiný pobytový titul, dobrovolný návrat, přiměřenost, ochrana rodinného života).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. NSS, ÚS, ESLP, SDEU.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf/článek jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NSS - 1 Azs 123/2025 - …`, `ESLP - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („před uplynutím platnosti“, „do 30 dnů ode dne doručení“, „nepřetržitě“, „přiměřený z hlediska zásahu do soukromého a rodinného života“).
- Jeden časový řez; znění účinné k datu podání žádosti / vydání rozhodnutí.
- Osobní údaje a údaje o zdravotním stavu či pronásledování uváděj jen v nezbytném rozsahu.

## Hard Rules

- Paragraf známý → žádný broad search; paragrafy s písmeny dohledávej přes `/toc`; změny → `/versions`.
- `docId` jen z API.
- Lhůty, poplatky, mzdové prahy, doby pobytu a maximální doby zajištění nikdy z paměti - vždy z aktuálního znění s odkazem.
- Mimo CODEXIS jen oficiální zdroje (mvcr.gov.cz, mzv.gov.cz, mpsv.cz, uradprace.cz, nssoud.cz, unhcr) když CODEXIS neodpovídá; nikdy neradit obcházení kontrol, účelová jednání ani nepravdivá tvrzení v žádostech.
