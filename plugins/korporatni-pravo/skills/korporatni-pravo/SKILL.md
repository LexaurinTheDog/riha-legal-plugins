---
uuid: 4161bc8f-7865-4571-86c7-2d805a98a43e
name: korporatni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Korporátní právo ČR"
    summary: "Založení a fungování s.r.o. a a.s. - valná hromada, převod podílu, odpovědnost jednatelů, akcionářské dohody, rozdělení zisku, obchodní rejstřík, skuteční majitelé, přeměny, likvidace."
    examplePrompts:
      - "Investor vstupuje do s.r.o. se třetinovým podílem a chce ochranu proti přehlasování. Jak nastavit společenskou smlouvu a dohodu společníků?"
      - "Jednatel uzavřel smlouvu bez souhlasu valné hromady, který vyžaduje společenská smlouva. Je smlouva platná a kdo odpovídá?"
      - "Připrav postup převodu obchodního podílu na třetí osobu včetně zápisu do rejstříku."
  en:
    displayName: "Czech Corporate Law"
    summary: "Formation and operation of s.r.o. and a.s. - general meetings, share transfers, directors' liability, shareholder agreements, profit distribution, commercial register, beneficial owners, transformations, liquidation."
    examplePrompts:
      - "An investor joins an s.r.o. with a one-third share and wants protection against being outvoted. How to set up the articles and the shareholders' agreement?"
      - "A director signed a contract without the general meeting's consent required by the articles. Is the contract valid and who is liable?"
      - "Prepare the procedure for transferring a share to a third party including the register filing."
  sk:
    displayName: "Korporátne právo ČR"
    summary: "Založenie a fungovanie českej s.r.o. a a.s. - valné zhromaždenie, prevod podielu, zodpovednosť konateľov, akcionárske dohody, rozdelenie zisku, obchodný register, koneční užívatelia výhod, premeny, likvidácia."
    examplePrompts:
      - "Investor vstupuje do s.r.o. s tretinovým podielom a chce ochranu proti prehlasovaniu. Ako nastaviť spoločenskú zmluvu a dohodu spoločníkov?"
      - "Konateľ uzavrel zmluvu bez súhlasu valného zhromaždenia, ktorý vyžaduje spoločenská zmluva. Je zmluva platná a kto zodpovedá?"
      - "Priprav postup prevodu obchodného podielu na tretiu osobu vrátane zápisu do registra."
description: Use when the user's matter involves Czech company or corporate law - zákon o obchodních korporacích (90/2012 Sb.), občanský zákoník o právnických osobách, s.r.o., a.s., družstvo, založení společnosti, společenská smlouva, stanovy, základní kapitál, vklad, příplatek, podíl, kmenový list, akcie, převod podílu, zástava podílu, valná hromada, svolání, neplatnost usnesení, per rollam, jednatel, představenstvo, dozorčí rada, způsob jednání, prokura, smlouva o výkonu funkce, péče řádného hospodáře, střet zájmů, zákaz konkurence, odpovědnost a ručení členů orgánů, vyloučení z funkce, rozdělení zisku, test insolvence, akcionářská / společnická dohoda, drag along, tag along, vetoprávo, squeeze-out, koncern, obchodní rejstřík (304/2013 Sb.), sbírka listin, evidence skutečných majitelů (37/2021 Sb.), přeměny (125/2008 Sb.), fúze, rozdělení, likvidace, jednočlenná společnost. Standalone skill - bundles CODEXIS methodology with corporate-practice method; no need to load the general codexis skill.
---

# Korporátní právo ČR

Samostatný oborový skill pro obchodní korporace. Základní reflex: **kdo rozhoduje, jakou většinou, v jaké formě a co se zapisuje** - a ke každé osobě a společnosti aktuální výpis z rejstříku, nikdy údaje z paměti.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/90/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf208'`, `cdx-cli get cdx://cz_law/304/2013/versions`, `cdx-cli search JD --query "péče řádného hospodáře jednatel odpovědnost" --court "Nejvyšší soud" --limit 5`.
- ZOK byl zásadně novelizován k 1. 1. 2021 (odpovědnost při úpadku, monistická a.s., rozdělení zisku, smlouva o výkonu funkce). Judikatura a komentáře před tímto datem mohou být překonané. **Každý §, většinu, lhůtu a částku ověř v aktuálním znění**, nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| ZOK | 90/2012 Sb. | `cz_law/90/2012` | Obecná část (§ 1-§ 94: vklady, podíl, orgány, péče řádného hospodáře § 51-§ 53, střet zájmů § 54-§ 57, smlouva o výkonu funkce § 59-§ 61, vyloučení § 63-§ 65, ručení při úpadku § 66, koncern § 71-§ 91), s.r.o. (§ 132-§ 242), a.s. (§ 243-§ 551), družstvo (§ 552+) |
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Právnické osoby (§ 118-§ 209: jednání § 161-§ 167, péče řádného hospodáře § 159, likvidace § 187-§ 209), korporace (§ 210-§ 213), neplatnost rozhodnutí orgánu (§ 245, § 258-§ 260), inominátní smlouvy (§ 1746 odst. 2) |
| Zákon o veřejných rejstřících | 304/2013 Sb. | `cz_law/304/2013` | Zápisy, materiální publicita (§ 8), sbírka listin (§ 66+), rejstříkové řízení, přímý zápis notářem (§ 108+) |
| Zákon o evidenci skutečných majitelů | 37/2021 Sb. | `cz_law/37/2021` | Zápis skutečného majitele, sankce - zákaz výplaty zisku a hlasování (§ 53-§ 54) |
| Zákon o přeměnách | 125/2008 Sb. | `cz_law/125/2008` | Fúze, rozdělení, převod jmění, změna právní formy, přeshraniční přeměny |
| Notářský řád | 358/1992 Sb. | `cz_law/358/1992` | Notářské zápisy o rozhodnutích orgánů, osvědčení |
| ZŘS | 292/2013 Sb. | `cz_law/292/2013` | Statusové věci právnických osob, rejstříkové řízení (§ 85 - krajský soud) |
| Insolvenční zákon | 182/2006 Sb. | `cz_law/182/2006` | Povinnost podat insolvenční návrh (§ 98), odpovědnost statutárů |
| Živnostenský zákon | 455/1991 Sb. | `cz_law/455/1991` | Předmět podnikání a obory živností |

## Rešeršní strategie

1. Paragraf známý → `/versions` (pozor na 1. 1. 2021) → `/toc` → `/text?part=`.
2. Judikatura NS: senát **27 Cdo** (obchodní korporace, dříve 29 Cdo) - `--court "Nejvyšší soud"`; klíčová témata: neplatnost usnesení VH, péče řádného hospodáře, převod podílu, jednání za společnost, předmět podnikání, vypořádací podíl. Vrchní soudy pro rejstříkovou praxi.
3. Komentář (`COMMENT`) k dispozitivnosti ZOK (co lze ve společenské smlouvě změnit) a k pojmům (péče řádného hospodáře, podstatná změna poměrů).
4. **Skutečný stav společnosti nikdy z CODEXIS ani z paměti**: aktuální výpis z veřejného rejstříku (jednající osoby, způsob jednání, podíly, zástavy, insolvence), **společenská smlouva/stanovy ze sbírky listin** (výpis nestačí - většiny, souhlasy, předkupní práva a omezení převodu jsou jen tam), evidence skutečných majitelů, ISIR. ARES vrací i vymazané záznamy - filtrovat, autoritativní je výpis rejstříkového soudu.

## Workflow korporátního praktika

1. **Kdo je klient a jaký je cíl.** Společnost × společník (většinový/menšinový/investor) × člen orgánu × věřitel × nabyvatel podílu. Zájmy se rozcházejí a rada musí odpovídat straně.
2. **Podklady.** Výpis z OR, zakladatelské dokumenty ze sbírky listin (aktuální úplné znění), seznam společníků, smlouvy o výkonu funkce, dohody společníků, účetní závěrky, zápisy z VH, evidence skutečných majitelů. Neověřené údaje `[DOPLNIT]`.
3. **Kompetence a většiny.** Působnost VH (§ 190 s.r.o., § 421 a.s.) × jednatel/představenstvo × dozorčí rada; kvórum (§ 169 - polovina všech hlasů, ledaže SS jinak), prostá většina **přítomných** (§ 170), kvalifikované většiny (§ 171 - změna SS, zrušení, přeměny; ověř výčet), formy - notářský zápis, kde ho zákon vyžaduje; per rollam (§ 175). **Past § 169-§ 170:** menšinový společník s třetinovým podílem je bez úpravy SS přehlasovatelný ve všem - řešení: odlišný počet hlasů (§ 169 odst. 2), kvalifikované většiny, vetoprávní matice, druhy podílů (§ 135-§ 136).
4. **Jednání za společnost.** Způsob jednání z výpisu k datu úkonu (§ 164 OZ), omezení jednatelského oprávnění vůči třetím osobám neúčinné (§ 47 ZOK), souhlas VH jako vnitřní podmínka - porušení = odpovědnost jednatele, ne neplatnost; překročení (§ 440 OZ), střet zájmů (§ 54-§ 57 - informační povinnost, možnost zákazu), smlouva s jediným společníkem písemně (§ 13).
5. **Podíly a jejich převody.** Převod na společníka (§ 207) × na třetí osobu (§ 208 - souhlas VH, ledaže SS jinak); účinnost vůči společnosti doručením smlouvy s úředně ověřenými podpisy (§ 209); přechod, dědění (lze u s.r.o. vyloučit § 42), zástava podílu (§ 32 ZOK, § 1320+ OZ), kmenový list (§ 137 - volná převoditelnost), vypořádací podíl (§ 36, § 213-§ 215), uvolněný podíl (§ 212), zrušení účasti a vyloučení (§ 204-§ 205). Dohoda společníků (SHA) je inominát - zavazuje strany, ne společnost; klíčové mechanismy do SS.
6. **Orgány a odpovědnost.** Péče řádného hospodáře a pravidlo podnikatelského úsudku (§ 51-§ 53 ZOK, § 159 OZ), smlouva o výkonu funkce (§ 59-§ 61 - písemná, schválená VH, bez schválené odměny bezplatný výkon § 59 odst. 3), zákaz konkurence (§ 199, § 441), vyloučení z funkce (§ 63-§ 65), ručení a doplnění pasiv při úpadku (§ 66), povinnost podat insolvenční návrh (§ 98 IZ), D&O.
7. **Kapitál a zisk.** Vklady a správce vkladu (§ 18-§ 24), příplatky (§ 162-§ 163), rozdělení zisku (§ 34 - na základě závěrky, § 40 - test insolvence a bilanční test, zálohy § 35), pevný podíl na zisku a odchylné rozdělení (§ 161), nezapsaný skutečný majitel = zákaz výplaty (§ 53 zákona 37/2021 Sb.).
8. **Rejstřík a formality.** Návrh na zápis na formuláři nebo přímý zápis notářem, přílohy s ověřenými podpisy, lhůta rozhodnutí (ověř), sbírka listin (účetní závěrky - sankce za nezakládání až zrušení společnosti), evidence skutečných majitelů, živnostenská oprávnění (obory konkrétně - obecná formule předmětu podnikání je podle NS neurčitá).
9. **Životní cyklus.** Založení (§ 8 ZOK - notářský zápis, § 146 náležitosti SS), změny, přeměny (projekt, znalec, ochrana věřitelů, lhůty dle 125/2008 Sb.), zrušení a likvidace (§ 187+ OZ - likvidátor, výzva věřitelům, konečná zpráva, výmaz), zrušení soudem.

## Časté pasti

- Přejímání jednajících osob, sídla nebo IČO ze staré smlouvy místo z aktuálního výpisu; u korporátních úkonů navíc nutná společenská smlouva ze sbírky listin.
- Převod podílu bez úředně ověřených podpisů nebo bez souhlasu VH vyžadovaného SS - neúčinný vůči společnosti.
- Menšinový investor spoléhající na výši vkladu místo na hlasovací práva a vetoprávo v SS (§ 169-§ 170).
- Rozdělení zisku bez testů § 40 nebo při nezapsaném skutečném majiteli - rozhodnutí VH bez právních účinků, jednatel odpovídá.
- Smlouva o výkonu funkce neschválená VH - odměna nevymahatelná, výkon bezplatný.
- Spoléhání na dohodu společníků (SHA) proti společnosti - zavazuje jen strany.
- Per rollam bez formy notářského zápisu tam, kde ji rozhodnutí vyžaduje.
- Citace ZOK nebo judikatury ze znění před 1. 1. 2021 (zejména odpovědnost při úpadku, rozdělení zisku po 6 měsících - překonáno).
- Obecný předmět podnikání „výroba, obchod a služby…" ve společenské smlouvě - podle NS neurčitý, uvádět obory konkrétně.
- Předpoklad, že souhlas VH je podmínkou platnosti smlouvy se třetí osobou - je to vnitřní omezení (§ 47 ZOK).
- Založení s.r.o. bez kontroly, zda zvolený název není zaměnitelný (§ 132 OZ, § 424 OZ) - rejstřík odmítne.
- Doplňování údajů z ARES bez filtrování vymazaných záznamů.

## Struktura odpovědi

1. **Závěr** (lze/nelze, kdo rozhoduje, jakou většinou, v jaké formě, co se zapisuje).
2. **Strana a její zájem.**
3. **Právní rámec** - ZOK/OZ/rejstříkový zákon v aktuálním znění, s odkazy; co říká společenská smlouva (nebo `[DOPLNIT ze sbírky listin]`).
4. **Postup krok za krokem** (svolání, usnesení, notář, podpisy, rejstřík, lhůty, poplatky).
5. **Rizika a odpovědnost** (neplatnost usnesení, odpovědnost orgánů, sankce).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 27 Cdo 3549/2020 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („většinou hlasů přítomných“, „ledaže společenská smlouva určí jinak“, „s úředně ověřenými podpisy“).
- Jeden časový řez; u rozhodnutí orgánů znění účinné v den rozhodnutí.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Údaje o společnostech a osobách výhradně z veřejného rejstříku (or.justice.cz), sbírky listin, ESM a ISIR - nikdy z paměti; neověřené `[DOPLNIT]`.
- Většiny, lhůty a částky nikdy z paměti - vždy z aktuálního znění a ze společenské smlouvy s odkazem.
