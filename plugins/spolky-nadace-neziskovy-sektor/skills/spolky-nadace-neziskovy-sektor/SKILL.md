---
uuid: 787c59aa-e879-4541-9781-67649e743f04
name: spolky-nadace-neziskovy-sektor
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Spolky, nadace a neziskový sektor ČR"
    summary: "Spolky, nadace, nadační fondy a ústavy - založení a rejstříky, vnitřní správa a spory členů, přezkum rozhodnutí orgánů, dary, veřejné sbírky, dotace, daňový režim, účetní povinnosti, zánik a odpovědnost."
    examplePrompts:
      - "Členská schůze spolku vyloučila klienta bez předchozí výzvy a bez možnosti se vyjádřit. Jak se bránit a do kdy?"
      - "Chceme založit nadační fond na podporu regionálních talentů. Co potřebujeme, kolik to stojí a jaké budou průběžné povinnosti?"
      - "Spolek přijal dar 800 000 Kč od firmy a chce jí za to dát reklamu na webu. Jaké jsou daňové dopady pro obě strany?"
  en:
    displayName: "Czech Non-profit Law"
    summary: "Associations, foundations, endowment funds and institutes - formation and registers, governance and member disputes, review of body decisions, donations, public collections, grants, tax status, accounting duties, dissolution and liability."
    examplePrompts:
      - "The general meeting of an association expelled my client without prior warning or a chance to respond. How to defend and by when?"
      - "We want to set up an endowment fund for regional talent. What is needed, what does it cost and what are the ongoing duties?"
      - "An association accepted a CZK 800,000 donation from a company and wants to give it advertising on its website. What are the tax consequences for both sides?"
  sk:
    displayName: "Spolky, nadácie a neziskový sektor ČR"
    summary: "Spolky, nadácie, nadačné fondy a ústavy v ČR - založenie a registre, vnútorná správa a spory členov, preskúmanie rozhodnutí orgánov, dary, verejné zbierky, dotácie, daňový režim, účtovné povinnosti, zánik a zodpovednosť."
    examplePrompts:
      - "Členská schôdza spolku vylúčila klienta bez predchádzajúcej výzvy a bez možnosti sa vyjadriť. Ako sa brániť a dokedy?"
      - "Chceme založiť nadačný fond na podporu regionálnych talentov. Čo potrebujeme, koľko to stojí a aké budú priebežné povinnosti?"
      - "Spolok prijal dar 800 000 Kč od firmy a chce jej za to dať reklamu na webe. Aké sú daňové dopady pre obe strany?"
description: Use when the user's matter involves a Czech non-profit legal person or civic activity - spolek, pobočný spolek, nadace, nadační fond, ústav, obecně prospěšná společnost, sociální družstvo, nezisková organizace, NNO, založení spolku, stanovy, spolkový rejstřík, nadační rejstřík, rejstřík ústavů, členství, členská schůze, statutární orgán, kontrolní komise, rozhodčí komise, vyloučení člena, neplatnost rozhodnutí orgánu spolku, přezkum soudem, nadační listina, nadační jistina, správní rada, nadační příspěvek, výroční zpráva, dar, darovací smlouva, veřejná sbírka, dotace pro NNO, veřejně prospěšný poplatník, hlavní a vedlejší činnost, členské příspěvky, jednoduché účetnictví, sbírka listin, evidence skutečných majitelů, likvidace spolku, fúze spolků, odpovědnost členů orgánů, status veřejné prospěšnosti. Standalone skill - bundles CODEXIS methodology with non-profit practice method; no need to load the general codexis skill.
---

# Spolky, nadace a neziskový sektor ČR

Samostatný oborový skill pro neziskové právnické osoby. Základní reflex: **forma určuje pravidla** (spolek × nadace × nadační fond × ústav × sociální družstvo) a **rozhodnutí orgánu se napadá v krátké prekluzivní lhůtě** - většina sporů členů končí na zmeškaných třech měsících. Daňově je nezisková osoba zvýhodněna jen tehdy, když skutečně plní znaky veřejně prospěšného poplatníka a odděluje hlavní a vedlejší činnost.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf258'`, `cdx-cli get cdx://cz_law/304/2013/versions`, `cdx-cli get cdx://cz_law/586/1992/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf17a'`, `cdx-cli search JD --query "vyloučení člena spolku přezkum soudem 242" --court "Nejvyšší soud" --limit 5`.
- Výše nadační jistiny, prahy pro audit a účetnictví, daňové limity a rejstříkové poplatky **ověř v aktuálním znění**; nikdy z paměti. Status veřejné prospěšnosti (§ 146-§ 150 OZ) nebyl proveden zvláštním zákonem - nenabízej jeho zápis.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| OZ - právnické osoby a korporace | 89/2012 Sb. | `cz_law/89/2012` | Obecně (§ 118-§ 209: orgány, péče řádného hospodáře § 159, likvidace § 187+), veřejná prospěšnost (§ 146-§ 150), spolky (§ 214-§ 302), nadace (§ 306-§ 393), nadační fondy (§ 394-§ 401), ústavy (§ 402-§ 418), přechodná ustanovení (§ 3041-§ 3051) |
| Zákon o veřejných rejstřících | 304/2013 Sb. | `cz_law/304/2013` | Spolkový a nadační rejstřík, rejstřík ústavů a o.p.s., zápis, sbírka listin (§ 66+), sankce (§ 104+) |
| ZOK - sociální družstvo | 90/2012 Sb. | `cz_law/90/2012` | § 758-§ 773 |
| Zákon o evidenci skutečných majitelů | 37/2021 Sb. | `cz_law/37/2021` | Automatický průpis u spolků a nadací (ověř), sankce |
| ZDP | 586/1992 Sb. | `cz_law/586/1992` | Veřejně prospěšný poplatník (§ 17a), předmět daně (§ 18a), osvobození členských příspěvků a bezúplatných příjmů (§ 19, § 19b), snížení základu (§ 20 odst. 7), odpočet dárce (§ 15 odst. 1, § 20 odst. 8), přiznání (§ 38mb) |
| ZDPH | 235/2004 Sb. | `cz_law/235/2004` | Osvobození (§ 57-§ 61), obrat a registrace, ekonomická činnost |
| Zákon o účetnictví + vyhláška pro NNO | 563/1991 Sb. + 504/2002 Sb. | `cz_law/563/1991`, `cz_law/504/2002` | Jednoduché účetnictví (§ 1f), účetní závěrka, audit, výroční zpráva |
| Zákon o veřejných sbírkách | 117/2001 Sb. | `cz_law/117/2001` | Oznámení krajskému úřadu, sbírkový účet, vyúčtování, sankce |
| Rozpočtová pravidla | 218/2000 / 250/2000 Sb. | `cz_law/218/2000`, `cz_law/250/2000` | Dotace NNO, veřejnoprávní smlouva, porušení rozpočtové kázně |
| Zákon o dobrovolnické službě | 198/2002 Sb. | `cz_law/198/2002` | Akreditace, pojištění, postavení dobrovolníků |
| Zákon o sociálních službách | 108/2006 Sb. | `cz_law/108/2006` | Registrace poskytovatelů, financování |
| Zákon o církvích | 3/2002 Sb. | `cz_law/3/2002` | Církevní právnické osoby, evidence MK |
| TOPO / trestní zákoník | 418/2011 / 40/2009 Sb. | `cz_law/418/2011`, `cz_law/40/2009` | Trestní odpovědnost neziskových PO, dotační podvod (§ 212), zpronevěra (§ 206) |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`; u organizací vzniklých před 2014 přechodná ustanovení (§ 3041+ OZ - občanská sdružení jsou spolky, o.p.s. pokračují podle zrušeného zákona 248/1995 Sb.).
2. Judikatura: **NS** senát 27 Cdo (spolky - vyloučení, neplatnost rozhodnutí, svolání, členství, nadace), **NSS** (daně NNO, dotace, veřejné sbírky), **ÚS** (spolková autonomie × ochrana člena). Ověř datum a znění.
3. Komentář (`COMMENT`) k pojmům (hlavní × vedlejší činnost, důležitý zájem, malicherný zásah, veřejně prospěšný účel); metodiky MF a GFŘ k NNO jsou administrativní výklad.

## Workflow

1. **Volba a kvalifikace formy.** Spolek (členská základna, samosprávný a dobrovolný, **hlavní činností nesmí být podnikání** § 217; vedlejší hospodářská činnost jen na podporu hlavní) × ústav (služby veřejnosti bez členů, zakladatel a ředitel) × nadace (trvalý účel, nadační jistina v zákonné minimální výši - ověř, správní rada, dozorčí rada nebo revizor) × nadační fond (bez jistiny, pružnější) × sociální družstvo × existující o.p.s. (novou nelze založit) × církevní PO × s.r.o. se sociálním cílem. U existující osoby ověř formu, stanovy/statut a stav zápisu v rejstříku a sbírce listin.
2. **Založení a zápis.** Spolek: zakladatelé (nejméně 3 osoby) shodou na stanovách nebo ustavující schůze (§ 218-§ 225), náležitosti stanov (název s „spolek"/„z. s.", sídlo, účel, práva a povinnosti členů, statutární orgán), zápis do spolkového rejstříku (formulář, listiny, souhlas s umístěním sídla, ověřené podpisy; osvobození od poplatku - ověř), vznik zápisem (§ 226). Nadace: nadační listina notářským zápisem, jistina, orgány, zápis; nadační fond a ústav obdobně bez jistiny. Následně: IČO, datová schránka (povinná pro PO), účet, evidence skutečných majitelů (automatický průpis - ověř), účetnictví, registrace k daním, případně živnost pro vedlejší činnost.
3. **Vnitřní správa spolku.** Nejvyšší orgán (členská schůze § 248-§ 257: svolání nejméně 30 dnů předem s pozvánkou a programem, usnášeníschopnost většina členů, rozhodování většinou přítomných, zápis do 30 dnů - ověř; shromáždění delegátů, dílčí schůze), statutární orgán (funkční období 5 let, není-li určeno jinak § 246; jednání a zápis změn; péče řádného hospodáře § 159), kontrolní a rozhodčí komise (§ 262-§ 267), seznam členů (§ 236 - GDPR, zveřejnění jen se souhlasem), členství (vznik, příspěvky, zánik, **vyloučení § 239-§ 242** - jen po výzvě k nápravě, s možností vyjádřit se, přezkum rozhodčí komisí, soud do 3 měsíců), pobočné spolky (§ 228-§ 231 - odvozená právní osobnost, ručení hlavního spolku za dluhy pobočného - ověř § 229).
4. **Přezkum rozhodnutí orgánů (§ 258-§ 260 OZ).** Člen nebo ten, kdo má zájem hodný ochrany, navrhne soudu vyslovení neplatnosti rozhodnutí pro rozpor se zákonem nebo stanovami **do 3 měsíců od dozvědění, nejpozději do 1 roku**; soud neplatnost nevysloví, jde-li o malicherný zásah nebo bylo-li by to v rozporu se zájmem spolku hodným ochrany; přiměřené zadostiučinění při zásahu do práva člena (§ 261). U nadací a ústavů obdobně podle obecných ustanovení o právnických osobách (§ 245 - ověř). Statusové věci rozhoduje krajský soud (§ 85 ZŘS).
5. **Nadace, nadační fond, ústav.** Nadace: nadační jistina a kapitál, zákaz zcizení jistiny mimo zákon, správní rada (nejméně 3 členové), dozorčí rada (povinná nad zákonnou hranicí kapitálu - ověř § 368) nebo revizor, **nadační příspěvky** (§ 353-§ 355 - podle statutu, zákaz příspěvku osobám tvořícím orgány a jim blízkým, vyúčtování účelu, vrácení při porušení), výroční zpráva do 6 měsíců a její zveřejnění ve sbírce listin (§ 358-§ 361), změna účelu (§ 321+), přidružený fond. Nadační fond: bez jistiny, možnost přeměny na nadaci. Ústav: zakladatelské právní jednání, ředitel, správní rada, výroční zpráva, audit při překročení obratu (§ 415 - ověř).
6. **Financování.** Členské příspěvky (osvobozeny § 19 odst. 1 písm. a) ZDP - podle stanov), **dary** (darovací smlouva, účel; u příjemce osvobození § 19b odst. 2 písm. b) ZDP při použití na veřejně prospěšné účely - ověř; u dárce odpočet § 15 odst. 1 / § 20 odst. 8 ZDP v zákonných limitech), **sponzoring = reklama** (protiplnění, zdanitelný příjem, DPH), dotace (rozpočtová pravidla, veřejnoprávní smlouva, porušení rozpočtové kázně a odvod - viz skill veřejných zakázek a dotací), **veřejné sbírky** (zákon 117/2001 Sb. - oznámení krajskému úřadu předem, sbírkový účet, doba, vyúčtování, sankce za neoznámenou sbírku; crowdfunding a dárcovské SMS), vedlejší hospodářská činnost (živnost, DPH), nadační příspěvky od jiných nadací, evropské fondy, dobrovolnická služba (198/2002 Sb.).
7. **Daně a účetnictví.** Veřejně prospěšný poplatník (§ 17a ZDP - hlavní činnost není podnikání; vyloučené osoby), předmět daně (§ 18a - ztrátová hlavní činnost není předmětem, vedlejší vždy), snížení základu daně (§ 20 odst. 7 - ověř výši), přiznání (§ 38mb - povinnost podat jen při zdanitelných příjmech - ověř), DPH (osvobozené plnění § 57-§ 61, obrat a registrace, ekonomická činnost), účetnictví: jednoduché (§ 1f zák. 563/1991 Sb. - spolky s příjmy do zákonného limitu, ne plátci DPH) × podvojné, výroční zpráva (nadace, ústav povinně; spolek podle stanov), **uložení účetní závěrky do sbírky listin** (§ 66 zák. 304/2013 Sb. - sankce až zrušení), audit u nadací/ústavů nad prahy, evidence skutečných majitelů.
8. **Odpovědnost a trestní rovina.** Členové orgánů - péče řádného hospodáře (§ 159 OZ; ručení věřiteli při nenahrazení škody § 159 odst. 3), smlouva o výkonu funkce a odměna (u spolků bezplatný výkon, není-li stanoveno jinak - ověř § 246), pojištění odpovědnosti; trestní odpovědnost PO (418/2011 Sb. se vztahuje i na spolky a nadace), dotační podvod, zpronevěra darů, porušení povinnosti při správě cizího majetku; osobní odpovědnost při nezákonném zrušení.
9. **Změny, přeměny a zánik.** Změna stanov (forma, zápis), fúze a rozdělení spolků (§ 274-§ 302 - projekt, zpráva, věřitelé), změna právní formy (spolek na ústav / sociální družstvo), zrušení dobrovolné × soudem (§ 268 - nezákonná činnost, nesplnění povinností, nečinnost; výzva soudu), likvidace (§ 269-§ 273 - likvidátor, výzva věřitelům, **likvidační zůstatek podle stanov, u veřejně prospěšného spolku jen obdobnému účelu - ověř**), výmaz; neaktivní spolky a rejstříkový soud.

## Časté pasti

- Vyloučení člena bez výzvy k nápravě a bez možnosti se vyjádřit; napadení až po 3 měsících - právo zaniklo.
- Členská schůze svolaná bez 30denní lhůty nebo mimo program - usnesení napadnutelná; per rollam bez opory ve stanovách.
- Hlavní činnost spolku fakticky podnikání (pronájem, prodej) - ztráta postavení veřejně prospěšného poplatníka, riziko zrušení soudem.
- Sponzoring vedený jako dar - dodanění u obou stran; dar použitý mimo veřejně prospěšný účel - ztráta osvobození.
- Veřejná sbírka bez oznámení krajskému úřadu (i online) - přestupek a povinnost vydat výtěžek.
- Nadační příspěvek členovi správní rady nebo osobě blízké - zakázán; nadace bez dozorčího orgánu nad zákonnou hranicí.
- Účetní závěrka neuložená do sbírky listin roky po sobě - pokuta, u opakování zrušení spolku.
- Datová schránka nezřízena/nesledována - fikce doručení rozhodnutí úřadů a soudů.
- Stanovy z doby „občanského sdružení" bez přizpůsobení OZ (název, orgány, sídlo) - problémy v rejstříku a při jednání.
- Pobočný spolek zadlužen - hlavní spolek ručí; naopak hlavní spolek zrušen → zanikají pobočné.
- Dotace čerpaná bez splnění podmínek programu - odvod a penále (viz skill veřejných zakázek a dotací).
- Status veřejné prospěšnosti nabízený jako zápis do rejstříku - zvláštní zákon neexistuje.
- Doplňování názvů, IČO, dat schůzí a částek z paměti - vždy z rejstříku, stanov nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat, kam, do kdy; u přezkumu rozhodnutí 3 měsíce).
2. **Forma osoby, orgán a použitelné dokumenty** (stanovy/statut - `[DOPLNIT ze sbírky listin]`).
3. **Právní rámec** - OZ / rejstříkový zákon / ZDP / zvláštní zákony v aktuálním znění, s odkazy.
4. **Postup nebo nároky** - tabulka: krok/nárok | právní základ (zákon × stanovy) | orgán | lhůta | riziko.
5. **Daňový a účetní dopad** (VPP, dary × reklama, DPH, povinnosti ve sbírce listin).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 27 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („do tří měsíců ode dne, kdy se o rozhodnutí dozvěděl“, „nejpozději do jednoho roku“, „nesmí být podnikání“, „malicherný zásah“).
- Jeden časový řez; u rozhodnutí orgánu znění zákona a stanov účinné v den rozhodnutí.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Výše jistiny, prahy pro audit, daňové limity a poplatky nikdy z paměti - vždy z aktuálního znění s odkazem.
- Údaje o osobách a organizacích výhradně z veřejného rejstříku (justice.cz), ESM a sbírky listin; mimo CODEXIS jen oficiální zdroje (financnisprava.cz, mvcr.gov.cz pro sbírky, mfcr.cz) když CODEXIS neodpovídá.
