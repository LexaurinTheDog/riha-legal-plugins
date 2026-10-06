<img src="icon.svg" width="56" alt="">

# riha-legal-plugins — verze pro Evolio Cowork

Právní skilly pro českou advokátní praxi upravené pro **Evolio Cowork** (cowork.evolio.cz): **50 oborových skillů** a **Lhůtník**. Skilly se do Coworku nahrávají jako jednotlivé soubory `SKILL.md` (Skills → Importovat), aktualizace jdou jako nová verze skillu.

## Jak skilly pracují

Právní prameny berou z nástrojů Coworku: `laws__*` (e-Sbírka se zněním k rozhodnému dni, česká judikatura, EUR-Lex, kontrola platnosti a pozdějšího osudu rozhodnutí, referenční sazby), `ares__*` pro údaje o právnických osobách a `isir__*` pro insolvence. Komentáře a weby slouží jen k orientaci, citovat se smí jen ověřený primární pramen; co ověřit nejde, zůstává jako `[DOPLNIT]`.

Každý oborový skill začíná povinným postupem:

1. hledání v paměti workspace (klient, protistrana, spisová značka),
2. nastavení rozhodného data rešerše,
3. rešerše podle oborové metodiky — zvláštní úprava daného typu jako samostatná linie, nosná i nepříznivá rozhodnutí celá,
4. ověření právnických osob v ARES,
5. oponentní kontrola nosných citací před odevzdáním,
6. každý výpočet dvakrát s mezikroky,
7. uložení stavu věci do paměti workspace (jen ověřená čísla).

Interní analýza a text pro protistranu, soud či úřad jsou vždy oddělené; nic se neodesílá bez pokynu.

**Lhůtník** spočítá konce lhůt z poznámek po jednání (s mezikroky, dvakrát, s tabulkou svátků) a po schválení je založí jako události a úkoly ke spisu v Evoliu.

## Skilly

### Civilní právo (11)

| Skill v Coworku | Obor |
|---|---|
| Dědické právo ČR | Závěť a dědická smlouva, nepominutelní dědici, vydědění, odmítnutí a výhrada soupisu, dluhy zůstavitele, pozůstalostní řízení u notáře, spory, plánování majetku. |
| Mezinárodní právo soukromé ČR | Přeshraniční spory a smlouvy - pravomoc soudů a rozhodné právo podle nařízení EU a ZMPS, doručování a dokazování do ciziny, uznání a výkon cizích rozhodnutí a rozhodčích nálezů, ověřování listin, doložky o volbě práva a soudu. |
| Náhrada újmy a odpovědnost ČR | Obecná a objektivní odpovědnost podle OZ, škoda na věci a čistě ekonomická újma, újma na zdraví a Metodika NS k nemajetkové újmě, usmrcení a sekundární oběti, odpovědnost za výrobek, odpovědnost zaměstnavatelů, profesionálů a státu, příčinná souvislost a spoluzavinění, promlčení, vazba na pojištění a vyčíslení. |
| Občanské procesní právo ČR | Pravomoc a příslušnost, sepis žaloby a petitu, soudní poplatky, doručování a lhůty, dokazování a důkazní břemeno, rozsudek pro zmeškání a platební rozkaz, předběžná opatření, odvolání a mimořádné opravné prostředky včetně přípustnosti dovolání, náklady řízení a advokátní tarif, nesporná řízení. |
| Ochrana osobnosti a GDPR ČR | Zásahy do cti, soukromí a podoby, pomluva, právo na odpověď, omluva a peněžité zadostiučinění, práva subjektu údajů, GDPR compliance, ÚOOÚ, DSA. |
| Opatrovnictví a svéprávnost ČR | Omezení svéprávnosti a jeho přezkum, podpůrná opatření (nápomoc při rozhodování, zastoupení členem domácnosti, předběžné prohlášení), opatrovnictví dospělých a dohled, povinnosti opatrovníka a schvalování soudem, veřejný opatrovník, detence ve zdravotnickém zařízení, ochrana zranitelných dospělých, demence a plánování majetku. |
| Rodinné právo ČR | Rozvod, péče o děti a styk, výživné, vypořádání SJM, rodičovství, domácí násilí, přeshraniční věci - hmotné právo OZ i řízení podle ZŘS. |
| Rozhodčí řízení a mediace ČR | Platnost rozhodčích doložek, spotřebitelské a pracovní limity, stálé rozhodčí soudy a ad hoc rozhodci, průběh řízení, zrušení a výkon nálezů, Newyorská úmluva, zákon o mediaci, mediační dohody a soudem nařízené první setkání. |
| Smluvní právo ČR | Analýza, revize a tvorba smluv podle občanského zákoníku - vady, neplatnost, rizikové klauzule, B2B / spotřebitel / veřejný sektor. |
| Spotřebitelské právo ČR | Spotřebitelské smlouvy a e-shopy, odstoupení, vady a reklamace, zakázaná ujednání a nekalé praktiky, spotřebitelský úvěr, mimosoudní řešení a hromadné řízení, compliance obchodníka. |
| Věcná práva a sousedské spory ČR | Vlastnické a držební žaloby, spoluvlastnictví a jeho zrušení, hranice a sousedské imise, služebnosti a cesty, nezbytná cesta, stavba na cizím pozemku, superficiální zásada a přechodná ustanovení, vydržení, opravy a spory v katastru nemovitostí. |

### Nemovitosti a stavebnictví (4)

| Skill v Coworku | Obor |
|---|---|
| Bytové právo - nájem a SVJ ČR | Nájem bytu a prostor sloužících podnikání, výpověď a vyklizení, nájemné a vyúčtování služeb, společenství vlastníků, bytová družstva, krátkodobé pronájmy. |
| Nemovitosti a realitní transakce ČR | Převody nemovitostí od prověrky listu vlastnictví po vklad - kupní smlouva, úschova, zástavní a předkupní práva, spoluvlastnictví, SVJ, nájem, daně. |
| Stavební právo ČR | Povolování staveb podle nového stavebního zákona a přechodný režim, účastníci a sousedé, černé stavby a odstranění, kolaudace, imise a hranice, smlouva o dílo na stavbu a vady. |
| Zemědělské právo ČR | Zemědělský pacht a jeho výpověď, pozemkové úpravy, ochrana zemědělského půdního fondu a vynětí, přímé platby SZP a podmíněnost, sankce a odvolání u dotací, LPIS a evidence zemědělského podnikatele, škody zvěří a myslivost, vodní právo a hnojiva, welfare zvířat a veterinární právo, prvovýroba potravin a prodej ze dvora, ekologické zemědělství, agrovoltaika, předání farmy a zdanění zemědělců. |

### Obchod a korporace (10)

| Skill v Coworku | Obor |
|---|---|
| Duševní vlastnictví ČR | Autorské právo a software, zaměstnanecká díla a díla na objednávku, licence, ochranné známky, patenty, vzory, domény, obchodní tajemství, vymáhání a řízení před ÚPV. |
| E-commerce a digitální služby ČR | E-shopy a distanční smlouvy, informační povinnosti a 14denní odstoupení, obchodní podmínky, shoda a záruka u zboží a digitálního obsahu, reklamace a ADR, nekalé praktiky a pravidla slev, online tržiště a povinnosti platforem dle DSA a P2B, cookies a přímý marketing, platební služby a chargeback, bezpečnost výrobků, přístupnost, přeshraniční prodej, příslušnost a DPH OSS. |
| Franchising, distribuce a obchodní zastoupení ČR | Franšízové smlouvy a předsmluvní informace, licence know-how a značky, výhradní a selektivní distribuce, vertikální omezení a bloková výjimka, určování cen pro další prodej a zákazy online prodeje, provize obchodního zástupce, ukončení a zvláštní odměna, konkurenční doložky, riziko zastřeného zaměstnání, přeshraniční rozhodné právo a příslušnost, DPH a srážková daň z licenčních poplatků. |
| Fúze a akvizice ČR | Share deal a asset deal, letter of intent a exkluzivita, due diligence, struktura SPA s cenovými mechanismy, prohlášení a záruky, odškodnění a escrow, odkládací podmínky, akcionářské dohody, přeměny dle zákona o přeměnách, kontrola spojení u ÚOHS a Komise, prověřování zahraničních investic, přechod zaměstnanců, regulatorní souhlasy, daňové strukturování, closing a spory po closingu. |
| Hospodářská a nekalá soutěž ČR | Kartely, zneužití dominance, spojování soutěžitelů a řízení před ÚOHS, náhrada škody, nekalá soutěž a její nároky, regulace reklamy a nekalé obchodní praktiky. |
| IT právo a kyberbezpečnost ČR | Smlouvy o vývoji a licencování software, SaaS a cloud, IT outsourcing a SLA, open source, NIS2 a nový zákon o kybernetické bezpečnosti, regulované subjekty a hlášení incidentů, DORA, odpovědnost za bezpečnostní incident, platformy a DSA, elektronické podpisy a eIDAS. |
| Korporátní právo ČR | Založení a fungování s.r.o. a a.s. - valná hromada, převod podílu, odpovědnost jednatelů, akcionářské dohody, rozdělení zisku, obchodní rejstřík, skuteční majitelé, přeměny, likvidace. |
| Mediální právo a reklama ČR | Tiskový zákon a právo na odpověď, regulace vysílání a audiovizuálních služeb na vyžádání, regulace reklamy včetně léčiv, alkoholu, tabáku, hazardu a potravin, klamavá a srovnávací reklama, nekalé obchodní praktiky a ochrana spotřebitele, influencer marketing, difamace a ochrana osobnosti versus svoboda projevu, ochrana zdroje novináře, DSA a EMFA, přímý marketing a spam. |
| Sportovní právo ČR | Smlouvy sportovců a klubů, svazové řády a přezkum disciplinárních rozhodnutí, přestupy a arbitráž, odpovědnost za sportovní úrazy, pořádání akcí, sponzoring, dary a veřejná podpora, antidoping, mládež. |
| Startupy, investice a ESOP ČR | Založení a cap table, zakladatelské dohody a vesting, konvertibilní zápůjčky a SAFE, seed a VC kola s akcionářskou dohodou, likvidační preference, anti-dilution a drag/tag, zaměstnanecké akcie a opční plány včetně českého daňového odkladu, převod IP a zaměstnanecká díla, zákaz konkurence a mlčenlivost, dotace a odpočet na výzkum, crowdfunding a limity veřejné nabídky, exit a zdanění zakladatelů. |

### Finance a pohledávky (8)

| Skill v Coworku | Obor |
|---|---|
| AML compliance ČR | Povinné osoby, identifikace a kontrola klienta, skutečný majitel a PEP, sankční screening, oznámení podezřelého obchodu FAÚ, systém vnitřních zásad a školení, zvláštní povinnosti advokáta a mlčenlivost, spouštěče u nemovitostí a úschov, evidence skutečných majitelů, kontroly a sankce, AML balíček EU. |
| Bankovnictví a úvěry ČR | Smlouvy o úvěru a zápůjčce, zákon o spotřebitelském úvěru a posouzení úvěruschopnosti, předčasné splacení a prodlení, hypotéky a zajištění, ručení a akcesorická zajištění, platební služby a neautorizované transakce, bankovní tajemství a blokace účtů, finanční arbitr, dohled a licence ČNB, nebankovní poskytovatelé. |
| Daňové právo hmotné ČR | Daň z příjmů FO a PO, DPH včetně odpočtu, reverse charge a řetězových podvodů, daň z nemovitých věcí, daňová rezidence a smlouvy o zamezení dvojího zdanění, převodní ceny, zneužití práva, daňové aspekty transakcí a přeměn, zaměstnanec × OSVČ, kryptoaktiva. |
| Exekuce - obrana povinného ČR | Audit exekučního titulu, návrhy na odklad a zastavení, nezabavitelné minimum a chráněný účet, mobiliární exekuce, nemovitost a SJM, vylučovací žaloby třetích osob, náklady, stížnosti, oddlužení jako východisko. |
| Insolvenční právo ČR | Insolvenční řízení z pohledu věřitele, dlužníka i správce - přihlášky, přezkum a popření, incidenční spory, oddlužení, konkurs, moratorium, ISIR. |
| Kapitálový trh a investice ČR | Obchodníci s cennými papíry a zprostředkovatelé dle MiFID II, vhodnost a přiměřenost, nároky investorů vůči obchodníkům, veřejná nabídka a výjimky z prospektu, dluhopisy a schůze vlastníků, investiční fondy a režimy ZISIF, crowdfunding, kryptoaktiva dle MiCA, zneužití trhu a insider dealing, informační povinnosti emitentů a oznámení podílů, nabídky převzetí a squeeze-out, dohled a sankce ČNB, finanční arbitr, zdanění investičních příjmů. |
| Pojistné právo ČR | Pojistná smlouva podle OZ, předsmluvní povinnosti a pravdivé odpovědi, lhůty likvidace, odmítnutí a snížení plnění, povinné ručení a garanční fond, majetkové, odpovědnostní, životní a cestovní pojištění, distribuce pojištění, ombudsman a finanční arbitr, promlčení. |
| Vymáhání pohledávek ČR | Od promlčení a předžalobní výzvy přes platební rozkaz a žalobu po exekuci - příslušenství, náklady, poplatky, insolvenční křižovatka. |

### Trestní a správní trestání (4)

| Skill v Coworku | Obor |
|---|---|
| Hospodářské trestní právo ČR | Podvod, úvěrový a dotační podvod, zpronevěra, porušení povinnosti při správě cizího majetku, úpadkové a věřitelské delikty, zkrácení daně a účinná lítost, korupce a zakázkové delikty, legalizace, trestní odpovědnost právnických osob a compliance obhajoba, zajištění majetku, strategie obhajoby a spolupráce s orgány. |
| Oběti trestných činů a poškození ČR | Práva obětí dle zákona 45/2013, zvlášť zranitelná oběť, poškozený v trestním řízení, adhezní nárok na náhradu škody a nemajetkové újmy, peněžitá pomoc státu, předběžná a ochranná opatření, ochrana při výslechu, důvěrník a zmocněnec, stížnost proti odložení, narovnání a mediace, domácí a sexuální násilí. |
| Přestupkové právo a správní trestání ČR | Odpovědnost za přestupek dle zákona 250/2016, přestupky fyzických osob, podnikatelů a právnických osob s liberací, promlčení, správní tresty a jejich výměra, příkaz a odpor, příkazový blok, ústní jednání a dokazování, dopravní přestupky a bodový systém, odvolání se zákazem reformationis in peius, přezkumné řízení, správní žaloba a moderace trestu, ne bis in idem s trestním právem. |
| Trestní právo a obhajoba ČR | Obhajoba a zastupování poškozeného ve všech fázích trestního řízení - lhůty, vazba, zajištění majetku, odklony, opravné prostředky, trestní odpovědnost právnických osob. |

### Veřejná správa a regulace (11)

| Skill v Coworku | Obor |
|---|---|
| Cizinecké a azylové právo ČR | Víza a pobytová oprávnění, zaměstnanecké a modré karty, občané EU a rodinní příslušníci, vyhoštění a zajištění, mezinárodní a dočasná ochrana, státní občanství, zaměstnávání cizinců. |
| Dopravní právo a nehody ČR | Odpovědnost a náhrada újmy z dopravní nehody, pojistné plnění z povinného ručení, dopravní přestupky a bodový systém, zadržení řidičského průkazu, trestné činy v dopravě, dopravci a cestující. |
| Energetické právo ČR | Licence a regulace ERÚ, smlouvy o dodávce elektřiny a plynu a změna dodavatele, podpora a povolování OZE, komunitní energetika a sdílení, připojení k síti, cenová regulace a spory, teplárenství, energetická náročnost budov. |
| Obce a veřejná správa ČR | Působnost orgánů obce, nakládání s obecním majetkem a záměr, vyhlášky a jejich přezkum, svobodný přístup k informacím, dotace a obecní společnosti, referendum, dozor a přezkoumání hospodaření, odpovědnost zastupitelů. |
| Právo životního prostředí ČR | EIA a integrované povolování, vodní právo a povolení k vypouštění, ochrana ovzduší, odpady a obaly, ochrana přírody a krajiny, lesy a zemědělská půda, hluk, ekologická újma a sanace, kontroly a pokuty ČIŽP, účast veřejnosti a spolků. |
| Spolky, nadace a neziskový sektor ČR | Spolky, nadace, nadační fondy a ústavy - založení a rejstříky, vnitřní správa a spory členů, přezkum rozhodnutí orgánů, dary, veřejné sbírky, dotace, daňový režim, účetní povinnosti, zánik a odpovědnost. |
| Správní a daňové řízení ČR | Obrana proti rozhodnutím a postupům úřadů a správce daně - odvolání, přezkum, správní žaloba, kasační stížnost, daňová kontrola, sankce, prekluze, lhůty. |
| Veřejné zakázky a dotace ČR | Režimy a druhy zadávacích řízení, námitky a návrh k ÚOHS, změny závazku, dotační podmínky, nesrovnalosti, porušení rozpočtové kázně a odvody, audity veřejného sektoru. |
| Zdravotnické právo ČR | Práva pacienta a informovaný souhlas, zdravotnická dokumentace, újma na zdraví a postup non lege artis, stížnosti a disciplinární řízení, úhrady z veřejného zdravotního pojištění, provoz poskytovatelů. |
| Ústavní stížnost a lidská práva | Přípustnost a vyčerpání opravných prostředků, dvouměsíční lhůta, sepis ústavní stížnosti, argumentace základními právy, test proporcionality, stížnost k ESLP, Listina EU a předběžná otázka. |
| Školské právo ČR | Přijímání do škol a odvolání, spádovost, speciální vzdělávací potřeby a podpůrná opatření, kázeňská opatření a vyloučení, šikana a bezpečnost, pracovní vztahy pedagogů, škola jako právnická osoba a zřizovatel, ČŠI, úplata a školné, vysoké školy a studenti. |

### Práce a sociální zabezpečení (2)

| Skill v Coworku | Obor |
|---|---|
| Pracovní právo ČR | Pracovní poměr od vzniku po skončení - výpověď a její neplatnost, odstupné, mzda a pracovní doba, odpovědnost, konkurenční doložka, dohody, švarcsystém, spory. |
| Sociální zabezpečení ČR | Starobní, invalidní a pozůstalostní důchody, nemocenské a mateřská, státní sociální podpora a hmotná nouze, příspěvek na péči a dávky pro OZP, pojistné a penále, námitky a žaloby proti ČSSZ a úřadu práce, přezkum posudků, koordinace sociálního zabezpečení v EU. |
### Nástroje

| Skill v Coworku | Obor |
|---|---|
| Lhůtník – záznam z jednání | Lhůty ze záznamu z jednání → události a úkoly v Evoliu |

## Generování

Oborové skilly vznikají skriptem `cowork-evolio/build.py` z hlavní větve repozitáře a zapisují se do `plugins/*/skills/*/SKILL.md`; skript odmítne výstup, který by obsahoval odkaz na jinou právní databázi. Lhůtník se udržuje ručně v `plugins/lhutnik/skills/jednani/SKILL.md`.

```
git switch cowork-evolio
python3 cowork-evolio/build.py
```

Testováno na reálné kauze (smluvní pokuta ze smlouvy o dílo) s modelem Claude Sonnet 5.5 v Coworku.
