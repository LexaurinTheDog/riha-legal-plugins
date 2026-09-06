---
uuid: b8def4ff-b6cd-4650-8e27-5baeb96c8a6e
name: vymahani-pohledavek
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Vymáhání pohledávek ČR"
    summary: "Od promlčení a předžalobní výzvy přes platební rozkaz a žalobu po exekuci - příslušenství, náklady, poplatky, insolvenční křižovatka."
    examplePrompts:
      - "Dlužník nezaplatil tři faktury po 80 000 Kč z roku 2024. Navrhni postup vymáhání a spočítej, co lze požadovat."
      - "Přišel odpor proti elektronickému platebnímu rozkazu. Co teď a jaké lhůty běží?"
      - "Máme pravomocný rozsudek, dlužník neplatí. Jak podat exekuční návrh a co když je v insolvenci?"
  en:
    displayName: "Czech Debt Recovery"
    summary: "From limitation and pre-action notice through payment orders and litigation to enforcement - interest, costs, fees, insolvency crossover."
    examplePrompts:
      - "A debtor has not paid three invoices of CZK 80,000 from 2024. Propose the recovery path and calculate what can be claimed."
      - "An objection against the electronic payment order arrived. What now and which deadlines run?"
      - "We have a final judgment and the debtor does not pay. How to file for enforcement, and what if they are insolvent?"
  sk:
    displayName: "Vymáhanie pohľadávok ČR"
    summary: "Od premlčania a predžalobnej výzvy cez platobný rozkaz a žalobu po exekúciu v ČR - príslušenstvo, trovy, poplatky, insolvenčná križovatka."
    examplePrompts:
      - "Dlžník nezaplatil tri faktúry po 80 000 Kč z roku 2024. Navrhni postup vymáhania a vypočítaj, čo možno požadovať."
      - "Prišiel odpor proti elektronickému platobnému rozkazu. Čo teraz a aké lehoty bežia?"
      - "Máme právoplatný rozsudok, dlžník neplatí. Ako podať exekučný návrh a čo ak je v insolvencii?"
description: Use when the user wants to recover, enforce, secure or defend against a monetary claim under Czech law - vymáhání pohledávky, nezaplacená faktura, dluh, dlužník, věřitel, promlčení, uznání dluhu, splátkový kalendář, předžalobní výzva (§ 142a o. s. ř.), platební rozkaz, elektronický platební rozkaz (EPR), směnečný platební rozkaz, odpor, žaloba o zaplacení, rozsudek pro uznání / pro zmeškání, úrok z prodlení, smluvní pokuta, náklady řízení, soudní poplatek, advokátní tarif, exekuce, exekuční návrh, exekutor, exekuční titul, notářský zápis se svolením k vykonatelnosti, postoupení pohledávky, započtení, ručitel, zástava, insolvence dlužníka, lustrace dlužníka (ISIR, CEE, ARES). Standalone skill - bundles CODEXIS methodology with the debt-recovery workflow; no need to load the general codexis skill.
---

# Vymáhání pohledávek ČR

Samostatný oborový skill pro vymáhání peněžitých pohledávek. Pořadí je pevné: **promlčení → solventnost dlužníka → titul a výpočet → předžalobní výzva → volba řízení → exekuce**. Přeskočení kroku typicky stojí náklady řízení nebo celou pohledávku.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/99/1963/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf142a'`, `cdx-cli get cdx://cz_law/351/2013/versions`, `cdx-cli search JD --query "předžalobní výzva náklady řízení 142a" --court "Nejvyšší soud" --limit 5`.
- Sazby, limity, poplatky a lhůty (repo sazba, paušál nákladů, limit EPR, sazby soudního poplatku a tarifu) **vždy ověř v aktuálním znění**; nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Promlčení (§ 609-§ 653), prodlení a úrok (§ 1968-§ 1971), splatnost (§ 1963), uznání dluhu (§ 2053), smluvní pokuta (§ 2048+), postoupení (§ 1879+), započtení (§ 1982+), ručení (§ 2018+) |
| NV o úroku z prodlení | 351/2013 Sb. | `cz_law/351/2013` | Sazba úroku z prodlení, paušální náhrada nákladů uplatnění |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Předžalobní výzva (§ 142a), platební rozkaz (§ 172), EPR (§ 174a), směnečný PR (§ 175), kvalifikovaná výzva (§ 114b), rozsudek pro uznání / zmeškání (§ 153a, § 153b), náklady (§ 137-§ 151) |
| Zákon o soudních poplatcích | 549/1991 Sb. | `cz_law/549/1991` | Sazebník, splatnost, následky nezaplacení (§ 9), osvobození |
| Advokátní tarif | 177/1996 Sb. | `cz_law/177/1996` | Sazby (§ 7), paušál u formulářových žalob (§ 14b), režijní paušál (§ 13) |
| Exekuční řád | 120/2001 Sb. | `cz_law/120/2001` | Exekuční titul (§ 40), exekuční návrh (§ 37-§ 39), náklady exekuce, zastavení (§ 55) |
| Notářský řád | 358/1992 Sb. | `cz_law/358/1992` | Notářský zápis se svolením k vykonatelnosti (§ 71a-§ 71c) |
| Zákon směnečný a šekový | 191/1950 Sb. | `cz_law/191/1950` | Směnka jako zajištění a titul směnečného PR |
| Insolvenční zákon | 182/2006 Sb. | `cz_law/182/2006` | Účinky zahájení (§ 109), přihláška místo žaloby (§ 173), zákaz exekuce |
| Nařízení o evropském platebním rozkazu | (ES) 1896/2006 | zdroj `EU` | Přeshraniční dlužník v EU |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`. Pro sazby (NV 351/2013, sazebník poplatků, tarif) vždy verze účinná k datu rozhodné události (vznik prodlení, podání žaloby).
2. Judikatura NS k nákladům a předžalobní výzvě: `--court "Nejvyšší soud"`, senáty 23 Cdo, 33 Cdo, 20 Cdo (exekuce), 29 Cdo (směnky, insolvence); ústavní rovina (ÚS - náklady u formulářových žalob).
3. Pro stav dlužníka mimo CODEXIS: ISIR (insolvence), centrální evidence exekucí, ARES / veřejný rejstřík (existence, likvidace, sídlo), katastr (majetek). Údaje nikdy nedoplňuj z paměti.

## Workflow vymáhání

1. **Titul a promlčení nejdřív.** Právní důvod (smlouva, faktura není titul - jen důkaz, bezdůvodné obohacení, směnka), splatnost (§ 1963 - dispozitivní lhůta u podnikatelů, ověř), počátek promlčecí lhůty (§ 619 - kdy mohlo být právo uplatněno poprvé), délka (§ 629 subjektivní tříletá, § 629 odst. 2 objektivní, § 639 uznání, § 640 rozhodnuté právo, § 630 ujednání délky). Promlčení soud zkoumá jen k námitce (§ 610) - ale promlčenou pohledávku klientovi vymáhat nedoporučuj bez upozornění.
2. **Dlužník.** Existence a stav (ARES, likvidace, výmaz), insolvence (ISIR - po zahájení řízení se pohledávka uplatňuje přihláškou, žaloba/exekuce nelze - § 109 IZ), exekuce (CEE - vícenásobná = nízká dobytnost), majetek. Výsledek rozhoduje, zda vůbec vymáhat.
3. **Výpočet.** Jistina; úrok z prodlení ode dne po splatnosti (§ 1970 OZ, sazba dle NV 351/2013 - repo sazba ČNB k rozhodnému dni + zákonné navýšení, ověř aktuální mechanismus) nebo smluvní úrok; paušální náhrada nákladů uplatnění (NV 351/2013 - jen u podnikatelských vztahů, ověř); smluvní pokuta; dílčí platby započítávat podle § 1932-§ 1933 OZ. Vždy uveď rozhodné datum a sazbu, ze které výpočet vychází.
4. **Předžalobní výzva (§ 142a o. s. ř.).** Odeslat na poslední známou adresu dlužníka nejméně 7 dnů před podáním žaloby (ověř), jinak soud náhradu nákladů zpravidla nepřizná. Obsah: identifikace pohledávky, částka, lhůta, číslo účtu, upozornění na náklady. Uchovat doklad o odeslání.
5. **Volba řízení.** Elektronický platební rozkaz (§ 174a - formulář, horní limit jistiny, nižší poplatek; ověř limit a sazbu) × platební rozkaz (§ 172) × žaloba × směnečný platební rozkaz (§ 175 - námitky v krátké lhůtě) × evropský platební rozkaz × rozhodčí řízení (doložka). Před podáním zvážit uznání dluhu s notářským zápisem se svolením k vykonatelnosti - exekuční titul bez soudu.
6. **Řízení.** Odpor proti PR/EPR (lhůta 15 dnů - ověř) ruší rozkaz, věc jde do standardního řízení; kvalifikovaná výzva § 114b → rozsudek pro uznání (§ 153a); rozsudek pro zmeškání (§ 153b). Změna žaloby (rozšíření) = doplatek soudního poplatku splatný podáním, nezaplacení vede k zastavení řízení v rozsahu rozšíření (ověř § 9 ZSOP). Náklady: soudní poplatek, tarif (§ 7 AT, u formulářových žalob § 14b), režijní paušál, DPH jen u plátce (§ 137 odst. 3 o. s. ř.).
7. **Exekuce.** Po právní moci a marném uplynutí lhůty k plnění: exekuční návrh exekutorovi (§ 37-§ 38 EŘ, přílohy - titul s doložkou vykonatelnosti), volba exekutora, náklady exekuce hradí povinný; před podáním znovu ISIR (zahájení insolvence exekuci blokuje). Alternativně soudní výkon rozhodnutí (§ 251+ o. s. ř.) u vybraných titulů.
8. **Zajištění do budoucna.** Uznání dluhu, splátkový kalendář se ztrátou výhody splátek (§ 1931), ručitel, zástava, směnka, notářský zápis, smluvní pokuta - navrhni klientovi standard pro další obchody.

## Časté pasti

- Vymáhání promlčené pohledávky bez upozornění klienta - námitka promlčení v odporu žalobu shodí i s náklady.
- Chybějící nebo špatně adresovaná předžalobní výzva - ztráta náhrady nákladů řízení.
- Podání žaloby nebo exekučního návrhu proti dlužníkovi v insolvenci - nutná přihláška v insolvenční lhůtě, jinak pohledávka propadá.
- Připočtení DPH k nákladům řízení u zástupce, který není plátcem, nebo použití starých vzorů s ×1,21.
- Rozšíření žaloby bez doplatku poplatku splatného podáním - zastavení řízení v rozšířeném rozsahu.
- Výpočet úroku z prodlení jednou sazbou za celé období nebo z nesprávného rozhodného dne.
- Faktura brána jako právní titul - bez smlouvy/objednávky/dodacího listu soud důvod pohledávky neuzná.
- EPR nad zákonný limit nebo bez formuláře - odmítnutí.
- Zapomenutý dlužník-spotřebitel: zvláštní pravidla pro náklady, rozhodčí doložky a smluvní pokuty.
- Doplňování názvu, IČO nebo adresy dlužníka z paměti - vždy z rejstříku; neověřené `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr** - vymáhat / nevymáhat / nejprve zajistit, s hlavním důvodem a nejbližší lhůtou.
2. **Kontrola promlčení a stavu dlužníka** s datem, k němuž byla provedena.
3. **Výpočet nároku** - tabulka: položka | základ | sazba/§ | období | částka; uvést rozhodná data a verzi předpisu.
4. **Doporučený postup** krok za krokem (výzva → řízení → exekuce) s lhůtami, poplatky a náklady.
5. **Rizika a alternativy** (odpor, insolvence, nedobytnost, mimosoudní dohoda).
6. **Judikatura a předpisy** - ověřené odkazy.
7. **Podklady a placeholdery** `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejméně 7 dnů před“, „ode dne následujícího po splatnosti“, „splatný podáním“).
- Jeden časový řez pro všechny paragrafy; u sazeb uveď datum účinnosti.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Mimo CODEXIS jen oficiální zdroje (ISIR, justice.cz, ARES, ČNB pro repo sazbu, CEE).
- Číselné hodnoty (sazby, limity, poplatky) nikdy z paměti - vždy z aktuálního znění s odkazem.
