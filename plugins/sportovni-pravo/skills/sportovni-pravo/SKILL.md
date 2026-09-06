---
uuid: 51c7259c-9474-4e02-9fe2-60f87af0d188
name: sportovni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Sportovní právo ČR"
    summary: "Smlouvy sportovců a klubů, svazové řády a přezkum disciplinárních rozhodnutí, přestupy a arbitráž, odpovědnost za sportovní úrazy, pořádání akcí, sponzoring, dary a veřejná podpora, antidoping, mládež."
    examplePrompts:
      - "Klub chce s hráčem uzavřít profesionální smlouvu jako s OSVČ. Jaká jsou rizika a co musí smlouva obsahovat?"
      - "Disciplinární komise svazu zastavila klientovi činnost na rok. Lze rozhodnutí napadnout u soudu a do kdy?"
      - "Nadace nabízí klubu příspěvek na vybavení výměnou za logo na dresech. Je to dar, nebo reklama, a jak se zdaní?"
  en:
    displayName: "Czech Sports Law"
    summary: "Athlete and club contracts, federation rules and disciplinary review, transfers and arbitration, liability for sports injuries, event organisation, sponsorship, donations and public funding, anti-doping, minors."
    examplePrompts:
      - "A club wants to sign a player as a self-employed professional. What are the risks and what must the contract contain?"
      - "A federation disciplinary committee suspended my client for a year. Can the decision be challenged in court and by when?"
      - "A foundation offers a club a contribution for equipment in exchange for a logo on jerseys. Is it a donation or advertising, and how is it taxed?"
  sk:
    displayName: "Športové právo ČR"
    summary: "Zmluvy športovcov a klubov v ČR, zväzové poriadky a preskúmanie disciplinárnych rozhodnutí, prestupy a arbitráž, zodpovednosť za športové úrazy, organizácia podujatí, sponzoring, dary a verejná podpora, antidoping, mládež."
    examplePrompts:
      - "Klub chce s hráčom uzavrieť profesionálnu zmluvu ako so SZČO. Aké sú riziká a čo musí zmluva obsahovať?"
      - "Disciplinárna komisia zväzu zastavila klientovi činnosť na rok. Možno rozhodnutie napadnúť na súde a dokedy?"
      - "Nadácia ponúka klubu príspevok na vybavenie výmenou za logo na dresoch. Je to dar alebo reklama a ako sa zdaní?"
description: Use when the user's matter involves sport in the Czech Republic - sportovec, profesionální sportovec, hráčská smlouva, smlouva o výkonu sportovní činnosti, OSVČ nebo zaměstnanec, klub, sportovní svaz, FAČR, ČOV, stanovy a řády svazu, disciplinární řízení, zastavení činnosti, přezkum rozhodnutí spolku, přestup, hostování, výchovné, FIFA, UEFA, agent, zprostředkovatel, rozhodčí komise, sportovní arbitráž, CAS, sportovní úraz, odpovědnost za újmu při sportu, pravidla sportu, pořádání sportovní akce, pořadatelská služba, diváci, vstupenky, přenosová a marketingová práva, sponzoring, reklama, dar klubu, nadační příspěvek, dotace NSA, zákon o podpoře sportu (115/2001 Sb.), sportovní infrastruktura, veřejná podpora, antidoping, WADA, mládež a nezletilí sportovci, trenér, e-sport, hazard a sázky ve sportu. Standalone skill - bundles CODEXIS methodology with sports-practice method; no need to load the general codexis skill.
---

# Sportovní právo ČR

Samostatný oborový skill pro právo ve sportu. Sport nemá vlastní kodex - je to **průnik spolkového, smluvního, pracovního, daňového a odpovědnostního práva se svazovými řády**, které členy zavazují jako smlouva. Rozhoduje proto vždy: kdo je klient, jaký má vztah ke svazu a která lhůta (svazová, arbitrážní, soudní) běží.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/115/2001/versions`, `cdx-cli get cdx://cz_law/89/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf258'`, `cdx-cli search JD --query "sportovec OSVČ závislá práce profesionální smlouva" --court "Nejvyšší správní soud" --limit 5`, `cdx-cli search JD --query "odpovědnost za úraz při sportu porušení pravidel" --court "Nejvyšší soud" --limit 5`.
- Svazové řády (FAČR, ČSLH, ČOV…), pravidla FIFA/UEFA/IIHF, Kodex WADA a pravidla CAS **nejsou v CODEXIS** - čerpej je z oficiálních webů svazů a organizací k datu úkonu a cituj s verzí. Lhůty svazové arbitráže a CAS jsou krátké a mění se - ověř v aktuálním řádu. Zákon o podpoře sportu a dotační podmínky NSA se mění každoročně.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o podpoře sportu | 115/2001 Sb. | `cz_law/115/2001` | Národní sportovní agentura, rejstřík sportu, dotace, povinnosti pořadatelů, bezpečnost na akcích |
| OZ - spolky a smlouvy | 89/2012 Sb. | `cz_law/89/2012` | Spolky (§ 214-§ 302: členství, orgány, vyloučení § 239-§ 242, přezkum rozhodnutí soudem § 258-§ 260, rozhodčí komise § 265-§ 267), nadace a příspěvky (§ 353+), inominátní smlouvy (§ 1746 odst. 2), podoba a soukromí (§ 84-§ 90), náhrada újmy (§ 2894+, prevence § 2900, § 2910), nezletilí (§ 31-§ 36) |
| Zákoník práce / zákon o zaměstnanosti | 262/2006 / 435/2004 Sb. | `cz_law/262/2006`, `cz_law/435/2004` | Závislá práce (§ 2-§ 3 ZP), nelegální práce, DPP/DPČ u trenérů, cizinci-sportovci |
| Zákon o rozhodčím řízení | 216/1994 Sb. | `cz_law/216/1994` | Rozhodčí doložky, svazová a mezinárodní arbitráž, uznání nálezů |
| ZDP / ZDPH | 586/1992 / 235/2004 Sb. | `cz_law/586/1992`, `cz_law/235/2004` | Sportovec § 6 × § 7 ZDP, veřejně prospěšný poplatník (§ 17a), dary (§ 19b, § 20 odst. 8), sponzoring jako reklama, osvobození sportovních služeb (§ 61 ZDPH) |
| Zákon o hazardních hrách / o regulaci reklamy | 186/2016 / 40/1995 Sb. | `cz_law/186/2016`, `cz_law/40/1995` | Sázkové partnerství, reklama na hazard a alkohol, ochrana mládeže |
| Zákon o vysílání | 231/2001 Sb. | `cz_law/231/2001` | Události zásadního významu, přístup k vysílání |
| Rozpočtová pravidla | 218/2000 / 250/2000 Sb. | `cz_law/218/2000`, `cz_law/250/2000` | Dotace NSA a obcí, porušení rozpočtové kázně |
| Zákon o obcích | 128/2000 Sb. | `cz_law/128/2000` | Podpora sportu obcí, schvalování zastupitelstvem, sportoviště |
| Trestní zákoník / zákon o přestupcích | 40/2009 / 250/2016 Sb. | `cz_law/40/2009`, `cz_law/250/2016` | Ublížení na zdraví při sportu, zákaz vstupu na sportovní akce (§ 76 TZ), diváckě násilí, doping (§ 288 TZ) |
| Vyhláška o zdravotní způsobilosti k tělesné výchově a sportu | 391/2013 Sb. | `cz_law/391/2013` | Sportovní prohlídky, výkonnostní a vrcholový sport |
| Unijní právo | čl. 45, 56, 101-102 SFEU; SDEU Bosman, Super League, ISU | zdroj `EU`, `ES` | Volný pohyb sportovců, soutěžní právo a svazová pravidla, kolektivní prodej práv |

## Rešeršní strategie

1. Paragraf známý → `/versions` → `/toc` → `/text?part=`; unijní judikatura ze zdroje `ES`.
2. Judikatura: **NS** (25 Cdo - odpovědnost při sportu, lyžování, pořadatel; 23 Cdo / 28 Cdo - smlouvy a spolky; 27 Cdo - přezkum rozhodnutí spolků), **NSS** (sportovec jako OSVČ × zaměstnanec, dotace, daně), **ÚS** (autonomie spolků × soudní ochrana člena), **SDEU** (`ES` - Bosman C-415/93, ISU C-124/21 P, Super League C-333/21, Royal Antwerp C-680/21). Ověř datum a novely.
3. Svazové řády, pravidla FIFA/UEFA, kodex WADA, řád CAS - z oficiálních zdrojů s uvedením verze; komentář (`COMMENT`) k § 258-§ 260 OZ a k § 2900+ OZ.

## Workflow

1. **Role a vztah ke svazu.** Sportovec (profesionál / amatér / mládež) × klub (spolek, s.r.o., a.s.) × svaz × agent × sponzor / dárce × pořadatel × divák × obec. Členství ve spolku a registrace u svazu = podřízení stanovám a řádům (smluvní základ); zjisti, které řády a v jaké verzi se použijí a jaké lhůty v nich běží.
2. **Vztah sportovec - klub.** Zaměstnanec (ZP - kogentní ochrana, skončení, odstupné, pojistné) × OSVČ (smlouva o výkonu sportovní činnosti - inominát § 1746 odst. 2; judikatura NSS připouští u profesionálů za konkrétních podmínek, riziko překvalifikace na závislou práci a nelegální práci) × amatér (registrace, bez odměny). Obsah smlouvy: doba a prodloužení, odměna a bonusy, přestupní a výstupní klauzule, práva k podobě a marketingu (§ 84-§ 85 OZ), zdravotní péče a pojištění, disciplinární sankce klubu, mlčenlivost, konkurenční omezení, rozhodčí doložka, ukončení a odstupné; u cizinců pobyt a povolení k práci; u nezletilých souhlas zákonného zástupce a limity FIFA pro délku smluv (ověř).
3. **Svazové právo a přezkum.** Stanovy a řády (disciplinární, přestupní, licenční, registrační), disciplinární řízení (právo být slyšen, přezkum uvnitř svazu, lhůty), **soudní přezkum rozhodnutí spolku** (§ 258-§ 260 OZ - návrh člena do 3 měsíců od dozvědění, nejpozději do 1 roku; jen rozpor se zákonem nebo stanovami, ne přezkum sportovního uvážení; soud nevysloví neplatnost při malicherném zásahu), vyloučení člena (§ 239-§ 242 - výzva, přezkum orgánem, soud 3 měsíce), rozhodčí komise spolku (§ 265-§ 267 - přezkum soudem podle zákona o rozhodčím řízení), svazová arbitráž (Sbor rozhodců FAČR, ČOV) a **CAS Lausanne** (odvolací lhůta 21 dnů od doručení rozhodnutí - ověř v řádu CAS), střet zájmů a vlastnictví více klubů (UEFA pravidla × český svaz), licenční řízení.
4. **Přestupy a agenti.** Přestupní řád svazu (registrace, výchovné a solidarita, hostování, ochranná období), FIFA RSTP (mezinárodní přestupy, nezletilí čl. 19, training compensation), agenti a zprostředkovatelé (řád svazu, pravidla FIFA - ověř aktuální platnost), smlouvy o přestupu mezi kluby (§ 1746 odst. 2 OZ, DPH), volný pohyb (Bosman).
5. **Odpovědnost za újmu při sportu.** Účastníci: dodržení pravidel sportu a míra přijatého rizika - odpovědnost zpravidla jen při porušení pravidel nad rámec běžné hry (judikatura NS, u lyžování pravidla FIS jako standard); pořadatel a provozovatel sportoviště (§ 2900, § 2910, § 2924? - ověř; bezpečnost, dozor, vybavení), trenér a dozor nad mládeží, zdravotní prohlídky (vyhl. 391/2013 Sb.), pojištění; trestní rovina (§ 146-§ 148 TZ jen při hrubém porušení pravidel); nároky § 2958+ OZ (Metodika NS jako orientace).
6. **Pořádání akcí.** Povinnosti pořadatele (§ 7a+ zák. 115/2001 Sb. - pořadatelská služba, spolupráce s policií - ověř), zábor a uzavírky (obec, silniční správní úřad), hluk (KHS), autorská práva k hudbě (OSA, INTERGRAM), vstupenky (spotřebitel, přeprodej, storno), divácké násilí (zákaz vstupu § 76 TZ, přestupky), přenosová práva (smluvní; události zásadního významu § 33 zák. 231/2001 Sb.; kolektivní prodej - soutěžní právo), GDPR (kamery, akreditace), pojištění.
7. **Financování a daně.** **Sponzoring = reklama** (protiplnění; zdanitelný příjem klubu, DPH, daňový náklad sponzora) × **dar** (§ 2055 OZ; osvobození u veřejně prospěšného poplatníka § 19b ZDP - spolek ano, obchodní společnost ne; odpočet dárce § 15 / § 20 odst. 8 ZDP) × **nadační příspěvek** (§ 353+ OZ - účel, vyúčtování, zákaz příspěvku členům orgánů) - u smíšených smluv (logo za příspěvek) hrozí překvalifikace na reklamu; dotace NSA (výzvy, rejstřík sportu, PRK a odvod - viz skill veřejných zakázek a dotací), podpora obcí (§ 85 zák. 128/2000 Sb. schvalování, veřejnoprávní smlouva § 10a zák. 250/2000 Sb.), veřejná podpora EU (GBER čl. 55 sportovní infrastruktura - ověř), sázkové partnerství (zák. 186/2016 Sb., reklama na hazard), DPH u sportovních služeb (§ 61 ZDPH u neziskových), sportovec § 6 × § 7 ZDP, hlavní × vedlejší činnost spolku (§ 217 OZ, § 18a ZDP).
8. **Antidoping.** Kodex WADA a pravidla Antidopingového výboru ČR (kontroly, zákaz, sankce, přezkum u svazové arbitráže a CAS), trestní odpovědnost (§ 288 TZ - výroba a jiné nakládání s látkami s dopingovým účinkem), pracovněprávní a smluvní následky.
9. **Mládež a ochrana.** Souhlas zákonného zástupce (§ 31-§ 36 OZ), smlouvy s nezletilými (přiměřenost, limity svazů), přestupy nezletilých, bezúhonnost trenérů, ochrana před zneužíváním (zák. 359/1999 Sb., interní pravidla), školní sport, sportovní gymnázia.

## Časté pasti

- Rozhodnutí svazu napadané u soudu po 3 měsících nebo s argumentací „špatné sportovní posouzení" - soud zkoumá jen zákonnost a soulad se stanovami a v zákonné lhůtě.
- Odvolání k CAS po uplynutí lhůty podle řádu CAS - nepřípustné, bez ohledu na soudní lhůty.
- Profesionál jako OSVČ s pevnou pracovní dobou, pokyny a výhradností - riziko závislé práce, doměrků a nelegální práce klubu.
- Sponzorská smlouva nazvaná „dar" nebo „nadační příspěvek" - daňová překvalifikace na reklamu; dar obchodní společnosti není osvobozen.
- Nadační příspěvek podmíněný logem na dresu bez řešení, kdo o použití rozhoduje a jak se vyúčtuje.
- Dotace NSA čerpaná bez souladu s rejstříkem sportu a podmínkami výzvy - odvod za porušení rozpočtové kázně.
- Smlouva s nezletilým na dobu přesahující limity svazu nebo bez souhlasu zákonného zástupce.
- Úraz při zápase žalovaný jako běžná náhrada újmy bez prokázání porušení pravidel nad rámec hry.
- Pořadatel bez pořadatelské služby a bez pojištění - odpovědnost i za diváky a třetí osoby.
- Přenosová práva prodaná kolektivně bez posouzení soutěžního práva; vysílání „události zásadního významu" omezené v rozporu se zákonem.
- Vlastnictví více klubů v téže soutěži posuzované jen podle českých řádů - UEFA pravidla pro evropské poháry.
- Doplňování názvů klubů, IČO, výše odměn a dat z paměti - vždy z rejstříků, smluv nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (svazová / arbitrážní / soudní; co podat a kam).
2. **Role, vztah ke svazu a použitelné řády** (s verzí).
3. **Právní rámec** - OZ / ZP / ZDP / 115/2001 + řády svazu, s odkazy.
4. **Postup nebo nároky** - tabulka: krok/nárok | právní základ (zákon × řád) | orgán | lhůta | riziko.
5. **Rizika a alternativy** (smír, dohoda se svazem, daňový dopad, veřejná podpora).
6. **Judikatura** - jen ověřená v CODEXIS / oficiálních zdrojích, kompaktní citace vč. SDEU a CAS.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 25 Cdo 1234/2024 - …`, `NSS - 2 Afs 123/2025 - …`, `SDEU - C-333/21 - 21.12.2023`) z metadat, nikdy vymyšlené; rozhodnutí CAS s číslem věci.
- Svazové řády cituj s názvem, článkem a verzí (datum účinnosti).
- Zachovej kvalifikátory („do tří měsíců ode dne, kdy se dozvěděl“, „nejpozději do jednoho roku“, „nad rámec pravidel hry“).
- Jeden časový řez; u disciplinárních věcí znění řádu účinné v den provinění.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions`.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty svazů, CAS a dotační podmínky nikdy z paměti - vždy z aktuálního řádu / výzvy s odkazem a verzí.
- Mimo CODEXIS jen oficiální zdroje (facr.cz, olympijskatym.cz, agenturasport.cz, tas-cas.org, fifa.com, uefa.com, antidoping.cz) když CODEXIS neodpovídá; nikdy neradit obcházení antidopingových nebo bezpečnostních pravidel.
