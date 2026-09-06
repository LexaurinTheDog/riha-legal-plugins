---
uuid: fe46b72f-b619-463b-93da-5998b1e7b6e0
name: smluvni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Smluvní právo ČR"
    summary: "Analýza, revize a tvorba smluv podle občanského zákoníku - vady, neplatnost, rizikové klauzule, B2B / spotřebitel / veřejný sektor."
    examplePrompts:
      - "Zreviduj přiloženou smlouvu o dílo z pohledu objednatele a roztřiď vady podle závažnosti."
      - "Je smluvní pokuta 0,5 % denně vymahatelná a lze ji vedle náhrady škody?"
      - "Protistrana tvrdí, že smlouva je neplatná pro neurčitost předmětu. Jak se bránit?"
  en:
    displayName: "Czech Contract Law"
    summary: "Contract analysis, revision and drafting under the Czech Civil Code - defects, invalidity, risk clauses, B2B / consumer / public sector."
    examplePrompts:
      - "Review the attached works contract from the customer's side and rank the defects by severity."
      - "Is a contractual penalty of 0.5 % per day enforceable, and can it be claimed alongside damages?"
      - "The other side claims the contract is void for an indefinite subject matter. How do we defend?"
  sk:
    displayName: "Zmluvné právo ČR"
    summary: "Analýza, revízia a tvorba zmlúv podľa českého občianskeho zákonníka - vady, neplatnosť, rizikové klauzuly, B2B / spotrebiteľ / verejný sektor."
    examplePrompts:
      - "Zreviduj priloženú zmluvu o dielo z pohľadu objednávateľa a roztrieď vady podľa závažnosti."
      - "Je zmluvná pokuta 0,5 % denne vymáhateľná a možno ju uplatniť popri náhrade škody?"
      - "Protistrana tvrdí, že zmluva je neplatná pre neurčitosť predmetu. Ako sa brániť?"
description: Use when the user asks to review, draft, revise, redline, compare or challenge a contract governed by Czech law, or when a question turns on občanský zákoník (89/2012 Sb.) contract rules - smlouva, návrh smlouvy, dodatek, revize smlouvy, připomínky ke smlouvě, vady smlouvy, neplatnost, zdánlivost, neurčitost, forma, podpis, jednání za právnickou osobu, obchodní podmínky, adhezní smlouva, spotřebitel, smluvní pokuta, limitace náhrady škody, odstoupení, výpověď, promlčení, započtení, postoupení, ručení, zástava, neúměrné zkrácení, lichva, změna okolností, smlouva o dílo, kupní, nájemní, úvěrová, licenční, nepojmenovaná smlouva, registr smluv (340/2015 Sb.), veřejné zakázky. Standalone skill - bundles CODEXIS methodology with contract-review method; no need to load the general codexis skill.
---

# Smluvní právo ČR

Samostatný oborový skill pro revizi, tvorbu a napadání smluv podle českého práva. Výstupem revize je vždy kategorizovaný seznam vad s právním základem a návrhem znění - ne obecný komentář.

## Operating Assumptions

- Pro CODEXIS používej výhradně `cdx-cli`; je nainstalovaný a přihlášený, nedělej preflight.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2048'`, `cdx-cli search JD --query "smluvní pokuta moderace" --court "Nejvyšší soud" --limit 5`, `cdx-cli search VS --query "smlouva o dílo" --limit 5`.
- Používej jen `search`, `get`, `schema`; preferuj flagy.
- Konkrétní prahy, lhůty a sazby (úrok z prodlení, hranice zkrácení, doba promlčení) **vždy ověř v aktuálním znění**, nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - občanský zákoník | 89/2012 Sb. | `cz_law/89/2012` | Právní jednání (§ 545+), neplatnost (§ 574-§ 588), závazky (§ 1721+), typové smlouvy (§ 2055+), náhrada škody (§ 2894+) |
| ZOK | 90/2012 Sb. | `cz_law/90/2012` | Jednání za korporaci, souhlasy orgánů, střet zájmů |
| Zákon o ochraně spotřebitele | 634/1992 Sb. | `cz_law/634/1992` | Spotřebitelské smlouvy vedle § 1810+ OZ |
| Nařízení vlády o úroku z prodlení | 351/2013 Sb. | `cz_law/351/2013` | Výše úroku z prodlení a paušál nákladů |
| Zákon o registru smluv | 340/2015 Sb. | `cz_law/340/2015` | Smlouvy s veřejným subjektem - účinnost zveřejněním, sankce zrušení |
| ZZVZ | 134/2016 Sb. | `cz_law/134/2016` | Smlouvy z veřejných zakázek - změny závazku, limity |
| Zákon o rozhodčím řízení | 216/1994 Sb. | `cz_law/216/1994` | Rozhodčí doložky a jejich přípustnost |
| Nařízení Řím I | (ES) 593/2008 | zdroj `EU` | Volba práva u přeshraničních smluv |

## Rešeršní strategie

1. **Paragraf první:** OZ přes `/versions` → `/toc` → `/text?part=paragrafNNNN`. Přechodná ustanovení (§ 3028+ OZ) rozhodují, zda smlouva uzavřená před 1. 1. 2014 podléhá starému zákoníku.
2. **Judikatura NS** k výkladu klauzulí (`--court "Nejvyšší soud"`; senáty 23 Cdo obchodní, 33 Cdo občanské, 31 Cdo velký senát, 26 Cdo nájmy). Preferuj rozhodnutí kategorie A a rozhodnutí velkého senátu; ověř, zda se týkají OZ 2012, nebo starého ObchZ/OZ 1964.
3. **Komentář** (`COMMENT`) k dispozitivnosti ustanovení (§ 1 odst. 2 OZ) a ke kogentním limitům.
4. **Vzory** (`VS`) jen jako kostru - každý vzor přizpůsob a ověř paragrafové odkazy, staré vzory citují neplatná čísla.

## Workflow revize smlouvy

1. **Za koho revidujeme.** Určit klientovu stranu a její komerční cíl; revize bez strany je nepoužitelná.
2. **Strany a zastoupení.** Identifikace (název, IČO, sídlo) a osoba jednající za právnickou osobu se ověřují ve veřejném rejstříku k datu podpisu - způsob jednání, prokura, plná moc, souhlas orgánu (§ 161-§ 167 OZ, § 440 OZ překročení, ZOK). Neověřené údaje označ `[DOPLNIT]`, nikdy nedoplňuj z paměti.
3. **Režim smlouvy.** B2B × spotřebitel (§ 419, § 1810-§ 1867 OZ, § 1815 nepřihlíží se) × slabší strana / adheze (§ 433, § 1798-§ 1801) × veřejný subjekt (registr smluv - účinnost až zveřejněním, ZZVZ) × přeshraniční (Řím I, volba práva a soudu). Režim určuje, co je zakázané, a co jen nevýhodné.
4. **Typ a předmět.** Typová smlouva × inominát (§ 1746 odst. 2); smíšená smlouva; určitost předmětu a ceny (§ 553, § 1792); forma (§ 559-§ 564 - písemná forma u nemovitostí § 560, změny jen písemně § 564).
5. **Platnost a vymahatelnost.** Zdánlivost (§ 551-§ 554) × absolutní neplatnost (§ 588 - dobré mravy, veřejný pořádek, nemožné plnění) × relativní neplatnost (§ 586 - námitka, promlčení) × částečná neplatnost (§ 576). Přednost výkladu zachovávajícího platnost (§ 574).
6. **Klauzulový audit** (viz seznam níže) - každou klauzuli posuď: co říká, co chybí, kogentní limit, riziko pro klienta, návrh znění.
7. **Kategorizace vad:** 🔴 kritická (neplatnost, nevymahatelnost, otevřená odpovědnost, ztráta nároku), 🟠 závažná (nevyvážená, chybí ochrana, nejasný výklad), 🟡 formální (terminologie, odkazy, číslování). Ke každé: klauzule → problém → právní základ → závažnost → návrh znění.
8. **Stress test.** Co se stane při prodlení, vadě, insolvenci protistrany, změně okolností, sporu o výklad - a zda smlouva na každý scénář odpovídá.

## Klauzulový audit - kontrolní seznam

- **Cena a platební podmínky:** splatnost (§ 1963 - dispozitivní 30 dnů u podnikatelů, hrubě nespravedlivá ujednání § 1972), DPH, zálohy, zádržné, valorizace.
- **Prodlení a sankce:** úrok z prodlení (§ 1970, NV 351/2013), smluvní pokuta (§ 2048-§ 2052; ujednání o vztahu k náhradě škody § 2050; moderace § 2051 jen na návrh; forma), paušál nákladů.
- **Odpovědnost:** limitace náhrady škody (§ 2898 - nelze předem vyloučit úmysl, hrubou nedbalost, újmu na přirozených právech), vzdání se práv z vad (§ 1916 odst. 2 - jako vzdání se práva kupujícího, nezhojí zamlčené vady), záruka × odpovědnost za vady, vyšší moc (§ 2913 odst. 2).
- **Ukončení:** výpověď (§ 1998-§ 2000), odstoupení (§ 2001-§ 2005 - podstatné porušení, účinky ex tunc/ex nunc, přetrvávající ujednání), vypořádání.
- **Zajištění a utvrzení:** ručení (§ 2018), zástava (§ 1309), finanční záruka (§ 2029), uznání dluhu (§ 2053), ztráta výhody splátek (§ 1931).
- **Obchodní podmínky:** inkorporace (§ 1751), překvapivá ujednání (§ 1753), jednostranná změna (§ 1752), pořadí dokumentů při rozporu.
- **Změna okolností a hardship:** § 1765-§ 1766, převzetí nebezpečí změny okolností.
- **Postoupení a započtení:** § 1879+, § 1982+, zákaz postoupení, zákaz započtení.
- **Mlčenlivost, IP, konkurenční doložka** (§ 2975 - přiměřenost, územní a časové omezení).
- **Řešení sporů:** volba práva, prorogace (§ 89a o. s. ř.), rozhodčí doložka (u spotřebitele nepřípustná - ověř § 2 zákona 216/1994 Sb.), mediace.
- **Formality:** doručování, jazyk, počet vyhotovení, podpisy (elektronický podpis, úředně ověřené podpisy tam, kde to zákon vyžaduje), salvátorská klauzule, úplnost ujednání, přílohy.
- **Zvláštní režimy:** neúměrné zkrácení (§ 1793 - jen zrušení smlouvy, hranice cca poloviny, restriktivní výklad, nepoužije se na podnikatele § 1797), lichva (§ 1796), předsmluvní odpovědnost (§ 1728-§ 1729).

## Časté pasti

- Aplikace OZ 2012 na smlouvu z doby před 1. 1. 2014 bez kontroly přechodných ustanovení (§ 3028 OZ).
- Vyloučení odpovědnosti za vady formulované jako omezení prodávajícího místo vzdání se práva kupujícího (§ 1916 odst. 2).
- Smluvní pokuta bez ujednání o vztahu k náhradě škody - § 2050 pak náhradu škody vylučuje.
- Přenesení judikatury k ObchZ na OZ 2012 bez ověření, zda závěr obstál.
- Spoléhání na salvátorskou klauzuli u vady, která zasahuje podstatu smlouvy (§ 576).
- Smlouva s veřejným subjektem podepsaná, ale nezveřejněná v registru smluv - neúčinná, po lhůtě zrušená od počátku.
- Opsání identifikace a jednajících osob ze staré smlouvy místo z aktuálního výpisu.
- Citování § z paměti nebo ze starého vzoru - čísla odstavců se novelami mění; před finalizací dokumentu ověř každý odkaz.
- Rozhodčí doložka nebo prorogace v neprospěch spotřebitele.
- Záměna „doba trvání“ × „po uplynutí“, „nejpozději“ × „do“ - operativní kvalifikátory měnit jen vědomě.

## Struktura výstupu revize

1. **Shrnutí pro klienta** - 3 až 5 vět: lze podepsat / jen po úpravách / nepodepisovat, hlavní důvod.
2. **Tabulka vad** - sloupce: článek smlouvy | problém | právní základ (§ s odkazem) | závažnost 🔴🟠🟡 | návrh znění.
3. **Chybějící ujednání**, která by klient měl doplnit.
4. **Otázky na klienta** a předpoklady (komerční cíl, vyjednávací pozice).
5. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.

Při draftingu: nejprve osnova (strany, preambule, předmět, cena, plnění, odpovědnost, ukončení, závěrečná ujednání), pak text; placeholdery v hranatých závorkách pro každý neověřený údaj.

## Pravidla výstupu

- Odkazy MUSÍ používat resolvovanou `https://` URL ze source bloku tool outputu; `cdx://` nikdy do výstupu; žádná raw ID ani API suffixy.
- Paragraf je klikací referencí: `[§ 2050 OZ](https://…#paragraf2050)`.
- Rozhodnutí cituj `SOUD - SP. ZN. / Č. J. - DD.MM.RRRR` (např. `NS - 23 Cdo 1234/2024 - 15.01.2025`) z metadat; spisové značky nikdy nevymýšlej.
- Při parafrázi zákona zachovej kvalifikátory („nepřihlíží se“, „ledaže“, „bez zbytečného odkladu“).
- Všechny paragrafy resolvuj ve stejné verzi OZ k datu dotazu; při smlouvě z jiného data uveď, které znění se použilo.

## Hard Rules

- Znáš-li paragraf, nezačínej broad searchem; pro změny zákona začni `/versions`.
- `/toc` → `elementId` → `/text?part=`; nehádej `docId`.
- Nepoužívej web, když CODEXIS odpovídá; pro údaje o firmách jen veřejný rejstřík / ARES.
- Neupravuj, nedoplňuj ani nevymýšlej názvy, IČO, sídla a jednající osoby - jen ověřené nebo `[DOPLNIT]`.
