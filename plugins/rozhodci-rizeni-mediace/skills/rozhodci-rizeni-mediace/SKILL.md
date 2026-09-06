---
uuid: 60fe1869-fc73-4ca2-aa57-b279e54c6746
name: rozhodci-rizeni-mediace
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Rozhodčí řízení a mediace ČR"
    summary: "Platnost rozhodčích doložek, spotřebitelské a pracovní limity, stálé rozhodčí soudy a ad hoc rozhodci, průběh řízení, zrušení a výkon nálezů, Newyorská úmluva, zákon o mediaci, mediační dohody a soudem nařízené první setkání."
    examplePrompts:
      - "Protistrana podala žalobu u soudu, ačkoli smlouva má rozhodčí doložku. Jak a do kdy namítnout nedostatek pravomoci?"
      - "Klientovi byl doručen rozhodčí nález vydaný ad hoc rozhodcem podle doložky ve smlouvě o úvěru z roku 2011. Lze nález zrušit nebo zastavit exekuci?"
      - "Soud nařídil první setkání s mediátorem. Co to znamená, co hrozí při neúčasti a jak se liší mediační dohoda od smíru?"
  en:
    displayName: "Czech Arbitration & Mediation"
    summary: "Validity of arbitration clauses, consumer and employment limits, permanent courts of arbitration and ad hoc tribunals, conduct of proceedings, setting aside and enforcement of awards, New York Convention, mediation act, mediation agreements and court-ordered first meetings."
    examplePrompts:
      - "The other party sued in court although the contract contains an arbitration clause. How and by when do we object to lack of jurisdiction?"
      - "My client received an award by an ad hoc arbitrator under a clause in a 2011 loan agreement. Can the award be set aside or enforcement stopped?"
      - "The court ordered a first meeting with a mediator. What does it mean, what are the consequences of not attending, and how does a mediation agreement differ from a settlement?"
  sk:
    displayName: "Rozhodcovské konanie a mediácia ČR"
    summary: "Platnosť rozhodcovských doložiek, spotrebiteľské a pracovné limity, stále rozhodcovské súdy a ad hoc rozhodcovia, priebeh konania, zrušenie a výkon nálezov, Newyorský dohovor, zákon o mediácii, mediačné dohody a súdom nariadené prvé stretnutie."
    examplePrompts:
      - "Protistrana podala žalobu na súd, hoci zmluva má rozhodcovskú doložku. Ako a dokedy namietnuť nedostatok právomoci?"
      - "Klientovi bol doručený rozhodcovský nález vydaný ad hoc rozhodcom podľa doložky v zmluve o úvere z roku 2011. Možno nález zrušiť alebo zastaviť exekúciu?"
      - "Súd nariadil prvé stretnutie s mediátorom. Čo to znamená, čo hrozí pri neúčasti a ako sa líši mediačná dohoda od zmieru?"
description: Use when the user's matter involves out-of-court dispute resolution in the Czech Republic - rozhodčí řízení, arbitráž, rozhodčí doložka, rozhodčí smlouva, zákon o rozhodčím řízení (216/1994 Sb.), platnost rozhodčí doložky, spotřebitelská rozhodčí doložka, zákaz ve spotřebitelských smlouvách, pracovněprávní spory, arbitrabilita, Rozhodčí soud při HK ČR a AK ČR, stálý rozhodčí soud, ad hoc rozhodce, jmenování rozhodce, podjatost rozhodce, námitka nedostatku pravomoci, rozhodčí nález, zrušení rozhodčího nálezu, žaloba na zrušení, tříměsíční lhůta, zastavení výkonu rozhodnutí, exekuce rozhodčího nálezu, uznání cizího rozhodčího nálezu, Newyorská úmluva, mezinárodní arbitráž, ICC, VIAC, mediace, zákon o mediaci (202/2012 Sb.), zapsaný mediátor, první setkání s mediátorem nařízené soudem, mediační dohoda, smír, ADR spotřebitelských sporů u ČOI, finanční arbitr. Standalone skill - bundles CODEXIS methodology with ADR-practice method; no need to load the general codexis skill.
---

# Rozhodčí řízení a mediace ČR

Samostatný oborový skill pro mimosoudní řešení sporů. Dva reflexy: **rozhodčí doložka se nejdřív prověřuje na platnost a arbitrabilitu podle práva a data uzavření** (spotřebitel po 1. 12. 2016 = doložka zakázána; před tím přísné náležitosti § 3 odst. 3-6 ZRŘ; ad hoc rozhodce „ze seznamu soukromé společnosti" = neplatnost dle judikatury NS) a **námitky se uplatňují včas, jinak zanikají** (nedostatek pravomoci nejpozději při prvním úkonu ve věci; žaloba na zrušení do 3 měsíců od doručení nálezu). Mediace je dobrovolná i tam, kde soud nařídí první setkání - nařízeno je setkání, ne dohoda.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/216/1994/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf31'`, `cdx-cli get cdx://cz_law/202/2012/versions`, `cdx-cli search JD --query "rozhodčí doložka spotřebitel neplatnost ad hoc rozhodce seznam" --court "Nejvyšší soud" --limit 5`, `cdx-cli search JD --query "zastavení exekuce rozhodčí nález neplatná doložka 268" --court "Nejvyšší soud" --limit 5`.
- ZRŘ byl zásadně novelizován (2012 - spotřebitelské doložky, 2016 - zákaz spotřebitelských doložek, přesun na finančního arbitra a ČOI); **vždy `/versions` k datu uzavření rozhodčí smlouvy a k datu zahájení řízení** - přechodná ustanovení určují, který režim platí. Řády stálých rozhodčích soudů (lhůty, poplatky, jmenování) ověř na jejich webu k datu zahájení; nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o rozhodčím řízení a o výkonu rozhodčích nálezů | 216/1994 Sb. | `cz_law/216/1994` | Arbitrabilita (§ 1-§ 2), rozhodčí smlouva a forma (§ 3), rozhodci (§ 4-§ 12: způsobilost, jmenování soudem § 9, vyloučení § 11-§ 12), řízení (§ 13-§ 30: pravomoc § 15, doručování § 19a, zásady § 19, smír § 24), nález (§ 23-§ 28), zrušení nálezu soudem (§ 31-§ 35: důvody, lhůta 3 měsíce § 32, odklad vykonatelnosti, zastavení výkonu § 35), cizí nálezy (§ 38-§ 40), stálé rozhodčí soudy (§ 13) |
| Newyorská úmluva o uznání a výkonu cizích rozhodčích nálezů | vyhl. 74/1959 Sb. | `cz_law/74/1959` | Uznání a výkon, důvody odepření (čl. V), forma doložky (čl. II) |
| Evropská úmluva o mezinárodní obchodní arbitráži | vyhl. 176/1964 Sb. | `cz_law/176/1964` | Doplňuje NY úmluvu mezi smluvními státy |
| Zákon o mediaci | 202/2012 Sb. | `cz_law/202/2012` | Zapsaný mediátor, smlouva o provedení mediace (§ 4), mlčenlivost (§ 9), mediační dohoda (§ 7), zahájení a ukončení (§ 4, § 6), stavení promlčení (§ 647 OZ), první setkání nařízené soudem (§ 100 odst. 2 o. s. ř.), zkoušky a seznam mediátorů (MSp), sankce |
| Občanský soudní řád | 99/1963 Sb. | `cz_law/99/1963` | Námitka rozhodčí smlouvy a zastavení řízení (§ 106), smír a jeho schválení (§ 67-§ 69, § 99), první setkání s mediátorem (§ 100 odst. 2, náklady § 150), přerušení řízení (§ 110), výkon rozhodnutí (§ 274) |
| Exekuční řád | 120/2001 Sb. | `cz_law/120/2001` | Rozhodčí nález jako exekuční titul (§ 40), zastavení exekuce pro neplatnou doložku (§ 55, § 268 odst. 1 písm. h) o. s. ř.), náklady při zastavení |
| Občanský zákoník | 89/2012 Sb. | `cz_law/89/2012` | Spotřebitel (§ 419, § 1810+), zneužívající ujednání (§ 1813-§ 1815), promlčení a jeho stavení mediací a rozhodčím řízením (§ 647-§ 648), narovnání (§ 1903+) |
| Zákon o ochraně spotřebitele | 634/1992 Sb. | `cz_law/634/1992` | Mimosoudní řešení spotřebitelských sporů (§ 20d-§ 20y - ČOI, finanční arbitr, ČTÚ, ERÚ, ČAK), informační povinnost podnikatele |
| Zákon o finančním arbitrovi | 229/2002 Sb. | `cz_law/229/2002` | Působnost (úvěry, platby, pojištění, investice), řízení a nález, přezkum soudem |
| Zákoník práce | 262/2006 Sb. | `cz_law/262/2006` | Pracovněprávní spory a arbitrabilita (ověř judikaturu), kolektivní spory a zprostředkovatel/rozhodce (zákon o kolektivním vyjednávání 2/1991 Sb.) |
| ZMPS | 91/2012 Sb. | `cz_law/91/2012` | Rozhodčí řízení s cizím prvkem (§ 117-§ 122), rozhodné právo pro doložku |
| Zákon o advokacii / etický kodex | 85/1996 Sb. | `cz_law/85/1996` | Advokát jako rozhodce a mediátor, střet zájmů, mlčenlivost |

## Rešeršní strategie

1. Paragraf známý → `/versions` **k datu uzavření doložky i zahájení řízení** → `/toc` → `/text?part=`; přechodná ustanovení novel 19/2012 Sb. a 258/2016 Sb. (ověř čísla) rozhodují o režimu.
2. Judikatura: **NS** senáty 23 Cdo / 33 Cdo (platnost doložek, ad hoc rozhodce určený „seznamem" soukromé společnosti, spotřebitelské doložky, zrušení nálezu, arbitrabilita), 20 Cdo (zastavení exekuce pro neplatnou doložku, nicotný nález, promlčení po zastavení), velký senát a stanoviska (R) k rozhodčím doložkám; **ÚS** (spravedlivý proces v rozhodčím řízení, nezávislost rozhodce); **SDEU** (`ES`) ke směrnici 93/13 (soud zkoumá zneužívající doložku z úřední povinnosti i ve fázi výkonu). Ověř datum a zda rozhodnutí nevychází ze znění ZRŘ před novelou.
3. Komentář (`COMMENT`) k ZRŘ a zákonu o mediaci; řády Rozhodčího soudu při HK ČR a AK ČR, VIAC, ICC a UNCITRAL pravidla mimo CODEXIS z oficiálních webů.

## Workflow

1. **Kvalifikace sporu a doložky.** Strany (podnikatel × spotřebitel × zaměstnanec × stát/obec), předmět (majetkový spor, o němž lze uzavřít smír - § 2 ZRŘ; vyloučeny incidenční spory v insolvenci, výkon rozhodnutí, statusové věci; obecné pochybnosti u pracovněprávních sporů - ověř judikaturu), datum a forma rozhodčí smlouvy (písemná; ve VOP jen při odkazu v hlavní smlouvě § 3 odst. 2; e-mail/DS ověř), určení rozhodce nebo stálého soudu (**stálý rozhodčí soud jen zřízený zákonem** § 13; „rozhodčí centra" a „seznamy rozhodců" soukromých společností = neplatná doložka podle judikatury NS a R), počet rozhodců, sídlo, jazyk, rozhodné právo, možnost přezkumu jinými rozhodci (§ 27).
2. **Spotřebitelský a pracovní režim.** Doložka ve spotřebitelské smlouvě uzavřená **po 1. 12. 2016 - zakázána** (§ 2 odst. 1 ZRŘ ve znění novely - ověř); uzavřená mezi 1. 4. 2012 a 30. 11. 2016 - jen na samostatné listině s povinnými informacemi (§ 3 odst. 3-6), rozhodce ze seznamu MSp, přezkum nálezu i pro rozpor s hmotným právem (§ 31 písm. g)); před 1. 4. 2012 - judikatura NS a ÚS o zneužívajících doložkách (nerovnováha, netransparentní určení rozhodce, ad hoc rozhodce od věřitele). Spotřebitel: dnes ADR u ČOI / finančního arbitra / ČTÚ / ERÚ / ČAK (§ 20d+ ZOS) a podnikatel musí spotřebitele o ADR informovat. Zaměstnanec: individuální pracovní spory - rozhodčí doložka sporná, kolektivní spory dle zák. 2/1991 Sb.
3. **Obrana proti řízení / u soudu.** Žaloba podaná u soudu přes doložku: žalovaný namítne rozhodčí smlouvu **nejpozději při prvním úkonu ve věci samé** (§ 106 odst. 1 o. s. ř.), jinak pravomoc soudu zůstává; soud zastaví, ledaže doložka je neplatná, zanikla nebo věc nelze rozhodovat v rozhodčím řízení. Před rozhodci: námitka nedostatku pravomoci **nejpozději při prvním úkonu ve věci** (§ 15 odst. 2 ZRŘ) - s výjimkou nearbitrability a neplatnosti pro spotřebitele (§ 33 - ověř); námitka podjatosti rozhodce (§ 12) bez zbytečného odkladu po zjištění; návrh soudu na vyloučení rozhodce nebo jmenování (§ 9, § 12 odst. 2). Nečinnost = riziko nálezu pro zmeškání podle řádu.
4. **Vedení rozhodčího řízení.** Zahájení doručením žaloby stálému soudu / rozhodci (§ 14 - stavení promlčení jako u soudu), poplatek podle sazebníku, ustavení tribunálu (jmenování, náhradní jmenování soudem § 9), rovnost stran a možnost uplatnit práva (§ 18 - jediná kogentní procesní zásada), postup dle dohody stran / řádu / uvážení rozhodců (§ 19), ústní jednání × písemné řízení, dokazování (rozhodci nemohou nutit svědky - dožádání soudu § 20), předběžné opatření jen soud (§ 22), rozhodování podle práva nebo ex aequo et bono jen na výslovný pokyn (§ 25 odst. 3), **rozhodčí nález** (písemný, podepsaný většinou, odůvodnění, nestanoví-li strany jinak § 25; doručení § 23 - okamžik právní moci a vykonatelnosti), smír formou nálezu (§ 24), náklady (řád), úschova nálezu u soudu (§ 29 - 20 let). Mezinárodní: sídlo řízení určuje lex arbitri; ICC/VIAC pravidla; nouzový rozhodce.
5. **Zrušení nálezu soudem (§ 31-§ 35 ZRŘ).** Žaloba k okresnímu / krajskému soudu podle příslušnosti (§ 41, § 43 - ověř) **do 3 měsíců od doručení nálezu** (§ 32 odst. 1); důvody taxativně: nearbitrabilita (a), neplatná doložka nebo její zrušení / nevztahuje se na věc (b), rozhodce nepovolaný nebo nezpůsobilý (c), nález nepřijat většinou (d), straně odepřena možnost věc projednat (e), odsouzení k plnění nežádanému nebo nemožnému (f), spotřebitel - rozpor s hmotným právem a ochrannými normami (g), důvody obnovy (h); důvody b) a c) jen pokud strana namítla včas v rozhodčím řízení (§ 33). Soud může odložit vykonatelnost (§ 32 odst. 2). Po zrušení pro a)/b) rozhoduje soud; pro ostatní nové rozhodčí řízení (§ 34). Nález nelze zrušit pro věcnou nesprávnost (mimo spotřebitele) - to je nejčastější omyl.
6. **Výkon a exekuce.** Tuzemský nález = exekuční titul (§ 40 písm. c) EŘ) bez doložky vykonatelnosti soudu (potvrzení o vykonatelnosti od rozhodce/soudu); povinný může navrhnout **zastavení exekuce** pro neplatnou doložku / nedostatek pravomoci (§ 268 odst. 1 písm. h) o. s. ř. - judikatura NS: exekuční soud zkoumá pravomoc rozhodce i po lhůtě pro žalobu na zrušení, u spotřebitele z úřední povinnosti) a **§ 35 ZRŘ** (návrh na zastavení výkonu z důvodů § 31 písm. a)-c) a f)-h) i bez žaloby na zrušení - lhůta 30 dnů pro podání žaloby na zrušení po zastavení - ověř); náklady exekuce při zastavení jdou zpravidla za oprávněným; promlčení po zastavení (judikatura NS - běh promlčecí doby během rozhodčího řízení s neplatnou doložkou). Cizí nález: uznání a výkon podle NY úmluvy (čl. IV listiny, čl. V důvody odepření - nedostatek platné doložky, vada řízení, překročení, veřejný pořádek), v ČR bez zvláštního výroku o uznání, jako součást exekuce/výkonu (§ 38-§ 40 ZRŘ - ověř).
7. **Mediace.** Zapsaný mediátor (seznam MSp, advokát-mediátor přes ČAK) × nezapsaný (bez účinků zákona - promlčení se nestaví, mlčenlivost bez zákonné opory); **smlouva o provedení mediace** (§ 4: písemná, identifikace, předmět, odměna, doba) zahajuje mediaci a **staví promlčení a prekluzi** (§ 647 OZ); mlčenlivost mediátora (§ 9 - i vůči soudu, trestní výjimky); **mediační dohoda** (§ 7 - podpisy stran, mediátor jen potvrzuje datum a podpisy, **není exekučním titulem** - vykonatelnost přes smír schválený soudem § 99 o. s. ř., notářský zápis se svolením k vykonatelnosti, nebo rozhodčí nález o smíru); ukončení (§ 6); **první setkání nařízené soudem** (§ 100 odst. 2 o. s. ř. - až 3 hodiny, přerušení řízení do 3 měsíců, neúčast = možný důvod nepřiznání nákladů § 150, hradí se dle vyhlášky 277/2012 Sb.); mediace v rodinných věcech (§ 474 ZŘS - soud může uložit setkání s mediátorem u dětí), přeshraniční mediace (směrnice 2008/52/ES). Advokát v mediaci: příprava klienta, BATNA, drafting dohody, kontrola zpeněžitelnosti.
8. **Drafting doložek.** Volba stálého soudu (Rozhodčí soud při HK ČR a AK ČR - doporučená formulace z jeho řádu; pro mezinárodní obchod VIAC/ICC/LCIA), počet rozhodců (1 do určité hodnoty, 3 nad), sídlo a jazyk, rozhodné právo hmotné i doložky, pravidla (řád v aktuálním znění), zrychlené řízení, vyloučení přezkumu jinými rozhodci, mlčenlivost, eskalační schéma (jednání → mediace → arbitráž s lhůtami, aby nebylo překážkou přístupu k soudu), oddělitelnost doložky, podpisy a forma; **nikdy** pro spotřebitele; u obcí/veřejných zadavatelů schválení orgánem a registr smluv; u insolvence počítat s tím, že incidenční spory doložka nepokryje.

## Časté pasti

- Doložka odkazující na „rozhodce ze seznamu vedeného společností XY" nebo „rozhodčí centrum" - neplatná; nález nicotný; exekuci lze zastavit i po letech.
- Spotřebitelská doložka po 1. 12. 2016 - zakázána; před tím bez samostatné listiny a informací - neplatná.
- Námitka nedostatku pravomoci vznesená až po prvním úkonu ve věci - zanikla (výjimka spotřebitel a nearbitrabilita).
- Žaloba na zrušení nálezu opřená o věcnou nesprávnost - zamítnuta; lhůta 3 měsíce zmeškána, protože běžela od doručení, ne od právní moci.
- Mediační dohoda předložená k exekuci - není titulem; nutný schválený smír nebo notářský zápis.
- Mediace s nezapsaným mediátorem - promlčení se nestaví, mlčenlivost bez zákonné ochrany.
- Neúčast na soudem nařízeném prvním setkání bez omluvy - nepřiznání nákladů (§ 150).
- Rozhodčí nález nedoručený řádně (doručování dle řádu / § 19a) - nenabyl právní moci, exekuce zastavena.
- Předběžné opatření požadované po rozhodcích - jen soud (§ 22).
- Zahraniční nález bez ověřené doložky a překladu podle čl. IV NY úmluvy; námitka veřejného pořádku užitá jako přezkum merita.
- Rozhodčí doložka v pracovní smlouvě nebo ve smlouvě obce bez schválení orgánem.
- Doplňování názvů rozhodčích institucí, čísel řádů, sazeb poplatků a dat doručení z paměti - vždy z řádu, spisu nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co podat, kam, do kdy - první úkon ve věci / 3 měsíce / 30 dnů; výpočet).
2. **Kvalifikace doložky** - datum, strany, forma, určení rozhodce, režim (podnikatelský × spotřebitelský × pracovní × mezinárodní).
3. **Právní rámec** - ZRŘ k datu / o. s. ř. / zákon o mediaci / NY úmluva v aktuálním znění, s odkazy.
4. **Postup a nároky** - tabulka: krok | právní základ | fórum (soud × rozhodci × mediátor × exekuční soud) | lhůta | riziko.
5. **Alternativy a strategie** (namítat × nechat běžet × smír × ADR u ČOI/finančního arbitra).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 23 Cdo 1234/2024 - …`, `NS - 20 Cdo 1234/2024 - …`, `SDEU - C-40/08 - 06.10.2009`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nejpozději při prvním úkonu ve věci samé“, „do tří měsíců od doručení rozhodčího nálezu“, „stálý rozhodčí soud zřízený zákonem“, „majetkový spor, o němž lze uzavřít smír“).
- Jeden časový řez; u doložky znění ZRŘ k datu jejího uzavření, u řízení k datu zahájení, u zrušení k datu doručení nálezu.

## Hard Rules

- Paragraf známý → žádný broad search; změny zákona → `/versions` k rozhodnému datu.
- `/toc` → `elementId` → `/text?part=`; `docId` jen z API.
- Lhůty, poplatky a náležitosti nikdy z paměti - vždy z aktuálního znění ZRŘ / řádu s odkazem; přechodná ustanovení novel vždy zkontrolovat.
- Údaje o rozhodcích, institucích a mediátorech výhradně ze seznamů MSp, ČAK a webů stálých soudů; mimo CODEXIS jen oficiální zdroje (justice.cz, soud.cz, coi.cz, finarbitr.cz) když CODEXIS neodpovídá.
