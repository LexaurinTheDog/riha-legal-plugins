---
uuid: 1a3eb1c5-cdd8-4dbf-8eaf-f75e9f969525
name: mezinarodni-pravo-soukrome
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Mezinárodní právo soukromé ČR"
    summary: "Přeshraniční spory a smlouvy - pravomoc soudů a rozhodné právo podle nařízení EU a ZMPS, doručování a dokazování do ciziny, uznání a výkon cizích rozhodnutí a rozhodčích nálezů, ověřování listin, doložky o volbě práva a soudu."
    examplePrompts:
      - "Německý odběratel nezaplatil faktury české firmě; ve smlouvě není nic o soudu ani právu. Kde žalovat a podle jakého práva?"
      - "Máme pravomocný rozsudek českého soudu proti dlužníkovi s majetkem v Rakousku a ve Velké Británii. Jak ho vykonat?"
      - "Klient se rozvedl na Ukrajině a chce se v ČR znovu oženit. Co je třeba k uznání rozvodu?"
  en:
    displayName: "Czech Cross-border Private Law"
    summary: "Cross-border disputes and contracts - jurisdiction and applicable law under EU regulations and the PIL Act, service and evidence abroad, recognition and enforcement of foreign judgments and awards, legalisation of documents, choice-of-law and forum clauses."
    examplePrompts:
      - "A German buyer has not paid invoices to a Czech company; the contract says nothing about courts or law. Where to sue and under which law?"
      - "We hold a final Czech judgment against a debtor with assets in Austria and the UK. How to enforce it?"
      - "My client divorced in Ukraine and wants to remarry in Czechia. What is needed to have the divorce recognised?"
  sk:
    displayName: "Medzinárodné právo súkromné ČR"
    summary: "Cezhraničné spory a zmluvy z pohľadu ČR - právomoc súdov a rozhodné právo podľa nariadení EÚ a ZMPS, doručovanie a dokazovanie do cudziny, uznanie a výkon cudzích rozhodnutí a rozhodcovských nálezov, overovanie listín, doložky o voľbe práva a súdu."
    examplePrompts:
      - "Nemecký odberateľ nezaplatil faktúry českej firme; v zmluve nie je nič o súde ani práve. Kde žalovať a podľa akého práva?"
      - "Máme právoplatný rozsudok českého súdu proti dlžníkovi s majetkom v Rakúsku a vo Veľkej Británii. Ako ho vykonať?"
      - "Klient sa rozviedol na Ukrajine a chce sa v ČR znovu oženiť. Čo treba na uznanie rozvodu?"
description: Use when the user's matter has a foreign element involving Czech courts, parties or assets - mezinárodní právo soukromé, cizí prvek, zákon o mezinárodním právu soukromém (91/2012 Sb.), pravomoc soudů, Brusel I bis (1215/2012), Lugano, prorogace, volba soudu, litispendence, rozhodné právo, volba práva, Řím I (593/2008), Řím II (864/2007), imperativní normy, veřejný pořádek, CISG (Vídeňská úmluva o mezinárodní koupi zboží), doručování do ciziny (2020/1784, Haagská úmluva 1965), dokazování v cizině, uznání a výkon cizího rozhodnutí, evropský exekuční titul, evropský platební rozkaz, drobné nároky, evropský příkaz k obstavení účtů, uznání cizího rozhodčího nálezu, Newyorská úmluva, uznání cizího rozvodu, apostila, superlegalizace, soudní tlumočník a překlad, zahraniční společnost, Brexit a Spojené království, Ukrajina, sankce EU, přeshraniční dědictví, únos dítěte. Standalone skill - bundles CODEXIS methodology with cross-border method; no need to load the general codexis skill.
---

# Mezinárodní právo soukromé ČR

Samostatný oborový skill pro věci s cizím prvkem. Pořadí otázek je pevné a nesmí se přehodit: **1) pravomoc a příslušnost (kde) → 2) rozhodné právo (podle čeho) → 3) doručování a dokazování (jak vést řízení) → 4) uznání a výkon (jak vymoci) → 5) listiny (jak prokázat)**. Pramen se vybírá v hierarchii **nařízení EU → mezinárodní smlouva → ZMPS**; vnitrostátní zákon se použije jen tam, kde nadřazený pramen mlčí.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/91/2012/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf15'`, `cdx-cli search EU --query "nařízení 1215/2012 příslušnost uznávání výkon" --limit 5`, `cdx-cli search EU --query "nařízení 593/2008 Řím I rozhodné právo smluvní" --limit 5`, `cdx-cli search JD --query "uznání cizího rozhodnutí vzájemnost veřejný pořádek" --court "Nejvyšší soud" --limit 5`.
- Unijní nařízení čti ze zdroje `EU` v české verzi, mezinárodní smlouvy ze zdroje `CR` (sdělení MZV); judikaturu SDEU ze zdroje `ES`. Stav ratifikací (Haagské úmluvy, Lugano, bilaterální smlouvy, Spojené království po Brexitu) a sankční seznamy **se mění - ověř k datu úkonu na oficiálních zdrojích**; nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| ZMPS - zákon o mezinárodním právu soukromém | 91/2012 Sb. | `cz_law/91/2012` | Subsidiární úprava: pravomoc (§ 6+), uznání a výkon cizích rozhodnutí (§ 14-§ 18), osobní stav a uznání rozvodů (§ 51+), věcná práva (§ 69+), rodina (§ 47+), dědictví (§ 74+), závazky (§ 84+), rozhodčí řízení (§ 117+), zpětný odkaz (§ 21), výhrada veřejného pořádku (§ 4) |
| Brusel I bis | (EU) 1215/2012 | zdroj `EU` | Příslušnost (čl. 4 bydliště žalovaného, čl. 7 zvláštní, čl. 17-23 spotřebitel a zaměstnanec, čl. 24 výlučná, čl. 25 prorogace, čl. 26 podřízení), litispendence (čl. 29+), uznání a výkon bez prohlášení vykonatelnosti (čl. 36+, čl. 39+, osvědčení čl. 53, odepření čl. 45-46) |
| Luganská úmluva 2007 | sdělení MZV | zdroj `CR` | Švýcarsko, Norsko, Island |
| Řím I / Řím II | (ES) 593/2008 / 864/2007 | zdroj `EU` | Smluvní závazky (volba čl. 3, hierarchie čl. 4, spotřebitel čl. 6, zaměstnanec čl. 8, imperativní normy čl. 9, forma čl. 11, promlčení čl. 12); mimosmluvní (čl. 4 místo škody, čl. 5-9 zvláštní, volba čl. 14) |
| Evropské procesní nástroje | (ES) 1896/2006, 861/2007, 805/2004, (EU) 655/2014, 2020/1784, 2020/1783 | zdroj `EU` | Evropský platební rozkaz, drobné nároky, evropský exekuční titul, obstavení účtů, doručování, dokazování |
| Rodinná a dědická nařízení | (EU) 2019/1111, 4/2009, 650/2012, 2016/1103-1104 | zdroj `EU` | Rodičovská odpovědnost a únosy, výživné, dědictví, majetkové režimy manželů |
| Insolvenční nařízení | (EU) 2015/848 | zdroj `EU` | Přeshraniční insolvence (viz insolvenční skill) |
| Haagské úmluvy | apostila 1961, doručování 1965, dokazování 1970, únosy 1980, prorogace 2005, uznávání rozsudků 2019 | zdroj `CR` | Třetí státy a Spojené království; stav smluvních stran ověř |
| Newyorská úmluva 1958 / zákon o rozhodčím řízení | vyhl. 74/1959 Sb. / 216/1994 Sb. | `cz_law/74/1959`, `cz_law/216/1994` | Uznání a výkon cizích rozhodčích nálezů (§ 38-§ 40 ZRŘ) |
| CISG - Vídeňská úmluva | sdělení 160/1991 Sb. | `cz_law/160/1991` | Mezinárodní koupě zboží mezi podnikateli (automatická aplikace, opt-out) |
| CMR | vyhl. 11/1975 Sb. | `cz_law/11/1975` | Mezinárodní silniční přeprava |
| Bilaterální smlouvy o právní pomoci | např. Ukrajina 123/2002 Sb. m. s., Vietnam, Rusko (stav ověř) | zdroj `CR` | Pravomoc, uznání, doručování mimo EU |
| Nařízení o veřejných listinách | (EU) 2016/1191 | zdroj `EU` | Osvobození od apostily uvnitř EU pro vybrané listiny (matriční, bezúhonnost) |
| Zákon o soudních tlumočnících a překladatelích | 354/2019 Sb. | `cz_law/354/2019` | Úřední překlady a tlumočení |
| o. s. ř. / ZŘS | 99/1963 / 292/2013 Sb. | `cz_law/99/1963`, `cz_law/292/2013` | Řízení s cizím prvkem, uznání rozhodnutí o osobním stavu (NS), výkon rozhodnutí |
| Sankční nařízení EU | (EU) 833/2014, 269/2014 a další | zdroj `EU` | Zákazy plnění, zmrazení majetku, screening protistran |

## Rešeršní strategie

1. Nejprve urči pramen podle hierarchie (nařízení → smlouva → ZMPS) a **datum** (zahájení řízení, uzavření smlouvy, vydání rozhodnutí - přechodná ustanovení nařízení a Brexit); pak `/versions` → `/toc` → `/text?part=` u ZMPS a zdroj `EU` u nařízení.
2. Judikatura: **SDEU** (`ES`) je pro výklad nařízení závazná - autonomní pojmy (bydliště, místo plnění, místo škody, spotřebitel, prorogace ve VOP, litispendence); **NS** (uznání cizích rozhodnutí, rozvody, rozhodčí nálezy, vzájemnost), **ÚS** (veřejný pořádek, spravedlivý proces při doručování). Ověř datum a to, zda rozhodnutí nevychází z předchůdce nařízení (Brusel I 44/2001, Řím před 2009).
3. Komentář (`COMMENT`) k ZMPS a literatura (`LT`) k nařízením; stav ratifikací a prohlášení k Haagským úmluvám z hcch.net, Evropský justiční atlas / e-justice pro přijímající orgány a formuláře.

## Workflow

1. **Cizí prvek a datum.** Kde má bydliště/sídlo žalovaný, kde se plnilo nebo vznikla škoda, kde je majetek, státní příslušnost, obvyklý pobyt (u rodiny a dědictví), datum uzavření smlouvy a zahájení řízení. Zjisti, zda protistrana není na sankčním seznamu (zákaz plnění, zmrazení).
2. **Pravomoc a příslušnost.** V EU **Brusel I bis**: obecná (čl. 4 - bydliště žalovaného v členském státě), zvláštní (čl. 7 - místo plnění závazku podle druhu smlouvy; místo, kde škoda nastala nebo může nastat), ochranné režimy (spotřebitel čl. 17-19, zaměstnanec čl. 20-23, pojištění - prorogace jen omezeně), **výlučná** (čl. 24 - nemovitosti, společnosti, rejstříky, výkon), prorogace (čl. 25 - písemně nebo v obchodních zvyklostech, ve VOP jen při prokazatelném souhlasu - judikatura SDEU), podřízení se (čl. 26), **litispendence** (čl. 29 - dříve zahájené řízení má přednost i při prorogaci třetího soudu, výjimka čl. 31 odst. 2), související řízení. Mimo EU: Lugano (CH, NO, IS), Haag 2005 (výlučná prorogace), bilaterální smlouvy, jinak **ZMPS § 6** (pravomoc, je-li dána místní příslušnost podle o. s. ř.). Rodina, dědictví, výživné, insolvence - zvláštní nařízení (Brusel II ter, 650/2012, 4/2009, 2015/848). Spojené království: Brusel I bis se od 2021 nepoužije - Haag 2005 (výlučné doložky), Haag 2019 (uznání rozsudků od data účinnosti pro UK - ověř), jinak národní právo.
3. **Rozhodné právo.** Smlouvy - **Řím I**: volba práva (čl. 3, i konkludentní; nelze obejít kogentní ochranu spotřebitele čl. 6 a zaměstnance čl. 8), bez volby hierarchie čl. 4 (charakteristické plnění, obvyklé bydliště poskytovatele, úniková doložka), imperativní normy fóra (čl. 9 - sankce, devizové, ochrana), forma (čl. 11), rozsah (čl. 12 - včetně promlčení a výkladu), **CISG** se u koupě zboží mezi podnikateli z různých smluvních států aplikuje automaticky - vyloučit lze jen výslovně. Mimosmluvní - **Řím II** (čl. 4 místo vzniku škody, společné bydliště, úzká vazba; výrobek čl. 5, nekalá soutěž čl. 6, životní prostředí čl. 7, duševní vlastnictví čl. 8, volba čl. 14 jen ex post nebo mezi podnikateli). Nepokryté oblasti - ZMPS (způsobilost § 29, věcná práva § 69-§ 73, manželství § 48+, dědictví mimo nařízení, právnické osoby § 30 - uznání zahraniční společnosti), zpětný odkaz (§ 21 - jen kde ZMPS připouští), výhrada veřejného pořádku (§ 4).
4. **Doručování a dokazování do ciziny.** V EU nařízení 2020/1784 (odesílající a přijímající subjekty, formuláře, jazyk a právo odmítnout, doručení poštou s dodejkou, elektronické doručování za podmínek) a 2020/1783 (dožádání důkazů, videokonference); mimo EU Haagské úmluvy 1965 a 1970 nebo bilaterální smlouvy přes Ministerstvo spravedlnosti; překlady (soudní tlumočník), fikce doručení a náhradní doručení jen podle použitelného nástroje; nedoručení do ciziny podle pravidel = důvod odepření uznání (čl. 45 odst. 1 písm. b) Brusel I bis).
5. **Uznání a výkon.** V EU **bez prohlášení vykonatelnosti** (čl. 36, čl. 39 Brusel I bis - osvědčení podle čl. 53 od soudu původu + překlad, výkon přímo exekutorem; povinný může navrhnout odepření podle čl. 45-46 u soudu; přizpůsobení opatření čl. 54); evropský exekuční titul (805/2004 - nesporné nároky), evropský platební rozkaz (1896/2006 - odpor 30 dnů), drobné nároky (861/2007 - do 5 000 EUR), evropský příkaz k obstavení účtů (655/2014 - ex parte, jistota); rozhodnutí o osobním stavu z EU se uznávají bez řízení (Brusel II ter). Mimo EU: **ZMPS § 14-§ 16** (uznání cizího rozhodnutí - podmínky: vzájemnost, pravomoc cizího soudu, řádné doručení a možnost účasti, nepřekážka res iudicata, veřejný pořádek; u majetkových věcí bez zvláštního výroku, u osobního stavu **zvláštní řízení o uznání u Nejvyššího soudu** (§ 51+ - rozvody, určení rodičovství; výjimky pro státy s bilaterální smlouvou a rozhodnutí ve věcech občanů daného státu - ověř); **rozhodčí nálezy** - Newyorská úmluva (§ 38-§ 40 ZRŘ; důvody odepření čl. V - neplatná doložka, vada řízení, veřejný pořádek; výkon jako tuzemský nález).
6. **Listiny.** Cizí veřejné listiny: **apostila** (Haag 1961 - vydává MZV/MSp státu původu; v ČR ověřuje MZV a MSp) × **superlegalizace** (státy mimo úmluvu - konzulární ověření) × osvobození (bilaterální smlouvy o právní pomoci, nařízení 2016/1191 uvnitř EU pro matriční a další vybrané listiny s vícejazyčným formulářem); **úřední překlad** soudním tlumočníkem (354/2019 Sb.); výpisy z cizích rejstříků (aktuálnost, ekvivalent OR), plné moci ze zahraničí (forma podle místa vystavení nebo ZMPS § 42 - ověř), notářské zápisy a jejich ekvivalence.
7. **Drafting doložek s cizím prvkem.** Volba práva (výslovná, celá smlouva, včetně mimosmluvních nároků a promlčení; CISG opt-in/out; imperativní normy a sankce), volba soudu (výlučná × nevýlučná; písemná forma čl. 25; pro třetí státy Haag 2005; u spotřebitelů a zaměstnanců jen v mezích nařízení) × rozhodčí doložka (instituce - Rozhodčí soud při HK ČR a AK ČR, VIAC, ICC, LCIA; místo, jazyk, počet rozhodců; NY úmluva pro výkon), jazyk smlouvy a rozhodná verze, měna a kurz, Incoterms, doručovací adresy a e-mail, GDPR přenosy mimo EU, sankční a exportní doložky, escrow a zajištění vykonatelné v cílovém státě.
8. **Zvláštní agendy (odkaz na oborové skilly).** Rodinné věci (Brusel II ter, únosy - Haag 1980, výživné 4/2009 s ústředním orgánem ÚMPOD), dědictví (650/2012, evropské dědické osvědčení), insolvence (2015/848), pracovní právo (vysílání 96/71/ES, Řím I čl. 8), přeshraniční přeměny společností, mezinárodní přeprava (CMR, Montrealská úmluva), evropský platební rozkaz při vymáhání, cizinecké právo.

## Časté pasti

- Prorogace na cizí soud nebo volba cizího práva ve spotřebitelské či pracovní smlouvě - neúčinná proti slabší straně v rozsahu ochranných norem.
- Příslušnost posuzovaná podle ZMPS nebo o. s. ř. tam, kde platí Brusel I bis (a naopak u třetích států).
- Volba práva brána jako volba soudu (a naopak) - jsou to dvě samostatné doložky.
- CISG přehlédnuta u mezinárodní koupě mezi podnikateli - platí automaticky, i když smlouva volí české právo (české právo CISG zahrnuje).
- Torpédová žaloba: protistrana zahájila řízení jinde dřív - litispendence, český soud přeruší; u výlučné prorogace platí výjimka.
- Doručení do ciziny poštou nebo e-mailem mimo nařízení/úmluvu - vada řízení a odepření uznání.
- Odpor proti evropskému platebnímu rozkazu po 30 dnech - rozkaz vykonatelný v celé EU.
- Rozvod ze třetího státu bez uznání Nejvyšším soudem - v ČR trvá manželství (bigamie, dědictví).
- Apostila požadována u státu mimo Haagskou úmluvu (nutná superlegalizace) nebo naopak zbytečně uvnitř EU u listin podle 2016/1191.
- Spojené království posuzované podle Brusel I bis po roce 2020 - použij Haag 2005 / Haag 2019 (stav ověř) nebo národní právo a exequatur.
- Rozhodčí doložka odkazující na neexistující nebo nesprávně označenou instituci - patologická doložka.
- Promlčení posuzované podle českého práva jako lex fori - řídí se rozhodným právem smlouvy (Řím I čl. 12).
- Plnění protistraně ze sankčního seznamu - trestní a správní odpovědnost bez ohledu na smlouvu.
- Doplňování názvů cizích společností, rejstříkových čísel, dat a částek z paměti - vždy z výpisů, listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší krok** (kde žalovat / jak vykonat / co ověřit; lhůty).
2. **Cizí prvek, datum a hierarchie pramenů** (nařízení → smlouva → ZMPS).
3. **Pravomoc a příslušnost** s článkem/paragrafem a odkazem.
4. **Rozhodné právo** s článkem/paragrafem, imperativní normy a veřejný pořádek.
5. **Procesní cesta** - tabulka: krok | nástroj (nařízení/úmluva/ZMPS) | orgán | lhůta | formulář/listina.
6. **Rizika a alternativy** (litispendence, výkon v cílovém státě, náklady, arbitráž).
7. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace vč. SDEU; **podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Článek/paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `SDEU - C-352/13 - 21.05.2015`, `NS - 30 Cdo 1234/2024 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („bydliště na území členského státu“, „místo, kde škoda vznikla“, „výslovně vyloučit“, „vzájemnost je zaručena“).
- Jeden časový řez; u smluv datum uzavření, u řízení datum zahájení, u uznání datum rozhodnutí; u Spojeného království výslovně uveď, který režim platí a proč.

## Hard Rules

- Nejprve hierarchie pramenů, teprve pak paragraf; nařízení ze zdroje `EU`, ZMPS přes `/versions` → `/toc` → `/text?part=`.
- `docId` jen z API.
- Stav smluvních stran úmluv, sankční seznamy, přijímající orgány a formuláře nikdy z paměti - vždy z hcch.net, e-justice.europa.eu, eur-lex, sanctionsmap.eu, justice.cz k datu úkonu.
- Nikdy neradit obcházení sankcí ani doručování způsobem, který nástroj nepřipouští.
