---
uuid: cda9fbb1-2613-40b9-9745-13974d2c8cd1
name: vecna-prava-sousedske-spory
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Věcná práva a sousedské spory ČR"
    summary: "Vlastnické a držební žaloby, spoluvlastnictví a jeho zrušení, hranice a sousedské imise, služebnosti a cesty, nezbytná cesta, stavba na cizím pozemku, superficiální zásada a přechodná ustanovení, vydržení, opravy a spory v katastru nemovitostí."
    examplePrompts:
      - "Soused vede přes klientův pozemek 30 let cestu k domu bez smlouvy. Vydržel služebnost, nebo lze cestu zahradit a co na to nezbytná cesta?"
      - "Tři sourozenci vlastní dům v podílech a nedohodnou se. Jak proběhne zrušení a vypořádání spoluvlastnictví, jaké jsou pořadí způsobů a náklady?"
      - "Ze sousedova pozemku padají větve a stíní, plot stojí 40 cm na klientově parcele podle nového zaměření. Jaké nároky a v jakém pořadí uplatnit?"
  en:
    displayName: "Czech Property Rights & Neighbour Disputes"
    summary: "Ownership and possession actions, co-ownership and its dissolution, boundaries and neighbour immissions, easements and rights of way, necessary access, building on another's land, superficies principle and transitional rules, acquisitive prescription, land registry corrections and disputes."
    examplePrompts:
      - "A neighbour has driven across my client's land to his house for 30 years without a contract. Has he acquired an easement by prescription, or can the road be closed, and what about necessary access?"
      - "Three siblings co-own a house and cannot agree. How does dissolution and settlement of co-ownership proceed, in what order of methods, and at what cost?"
      - "Branches fall and shade from the neighbour's plot, and the fence stands 40 cm on my client's parcel according to a new survey. Which claims to raise and in what order?"
  sk:
    displayName: "Vecné práva a susedské spory ČR"
    summary: "Vlastnícke a držobné žaloby, spoluvlastníctvo a jeho zrušenie, hranice a susedské imisie, služobnosti a cesty, nevyhnutná cesta, stavba na cudzom pozemku, superficiálna zásada a prechodné ustanovenia, vydržanie, opravy a spory v katastri nehnuteľností."
    examplePrompts:
      - "Sused vedie cez klientov pozemok 30 rokov cestu k domu bez zmluvy. Vydržal služobnosť, alebo možno cestu zahradiť a čo na to nevyhnutná cesta?"
      - "Traja súrodenci vlastnia dom v podieloch a nedohodnú sa. Ako prebehne zrušenie a vyporiadanie spoluvlastníctva, aké je poradie spôsobov a náklady?"
      - "Zo susedovho pozemku padajú konáre a tienia, plot stojí 40 cm na klientovej parcele podľa nového zamerania. Aké nároky a v akom poradí uplatniť?"
description: Use for Czech ownership, possession, acquisitive prescription, easements, necessary access, co-ownership, boundaries, structures on another's land, registry disputes and neighbour interference. Include claim-specific venue, enforceable remedies and complete fee calculations; use transaction-focused skills for a pure conveyance.
---

# Věcná práva a sousedské spory

## Zdrojový režim: SLV, e-Sbírka a Sagasu

Právní prameny získávej těmito nástroji v uvedeném pořadí; jiné zdroje jen tehdy, když tyto pramen nemají:

1. **MCP SLV (Salvia)** — česká judikatura a vyhledání předpisu. Indexy `ns` (Nejvyšší soud), `nss` (Nejvyšší správní soud), `us` (Ústavní soud), `justice` (okresní, krajské a vrchní soudy), `isir` (insolvenční rejstřík). Nástroje: `search_decisions`, `search_by_case_number`, `fetch_decision`; předpisy `search_regulations`, `fetch_regulation_info`, `fetch_regulation_text`.
2. **Skill e-Sbírka** (`/esbirka` z pluginu `zdroje-slv`, skript `scripts/esbirka.py` v adresáři skillu `esbirka`) — úřední znění předpisu účinné k rozhodnému dni (`info --k`, `par --k`, `text`), historie znění (`zneni`), rozdíly mezi zněními (`diff`), novely, přechodná ustanovení a nálezy ÚS (`souvislosti`). Znění citované v odpovědi ber odsud, ne z paměti ani z textu rozhodnutí.
3. **MCP Sagasu** — subjekty, rejstříky a výpočty: ekonomický subjekt podle IČO nebo názvu `firma_vyhledat` → `firma_detail` (ARES, jen aktivní; slovenské `firma_sk_vyhledat` → `firma_sk_detail`); výpis z obchodního rejstříku se statutárními orgány, společníky a kapitálem `obchodni_rejstrik`; zaniklé a vymazané osoby `verejny_rejstrik`, angažmá fyzické osoby `verejny_rejstrik_osoba`, angažmá právnické osoby `verejny_rejstrik_angazma_po`; listiny ze sbírky listin a jejich text `sbirka_listin` → `listina_text`; živnosti `zivnostensky_rejstrik`, `zivnostnik_vyhledat`; nespolehlivý plátce DPH a zveřejněné účty `dph_status`; adresa podle RÚIAN `standardizace_adresy`; ID datové schránky `datova_schranka_vyhledat` (nejjistěji podle IČO); advokáti `advokat_cz_vyhledat` → `advokat_cz_detail`; insolvence `insolvence_vyhledat` → `insolvence_detail` (události) → `insolvence_dokument_text`; výpočty `urok_z_prodleni`, `odmena_advokata`, `soudni_poplatek`. Postup je vždy vyhledání → detail → text. Když ARES nic nevrátí, subjekt může být zaniklý — ověř ve `verejny_rejstrik` dřív, než uzavřeš, že neexistuje.
4. Komentáře, literatura a webové zdroje slouží jen jako navigace, nikdy jako citovaná opora; jejich odkazy na normy a rozhodnutí ověř načtením v SLV nebo e-Sbírce.

Výpočty Sagasu (úrok z prodlení, odměna advokáta, soudní poplatek) přeber i s rozpisem a citací předpisu a přepočítej je druhou cestou (např. repo sazba + 8 p. b. = sazba a zpět); nesoulad je chyba. Údaje o právnické osobě do externího dokumentu (název, IČO, sídlo, statutární orgán, způsob jednání) ověř v Sagasu v reálném čase, vymazané osoby vynech; nelze-li ověřit, použij `[DOPLNIT z OR]`. Údaje fyzických osob jednajících za právnickou osobu (statutární orgán, prokurista, likvidátor) ověř týmž způsobem v `obchodni_rejstrik` nebo `verejny_rejstrik`; ostatní údaje fyzických osob přebírej jen z listin ve spisu.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán. Rozliš prázdný výsledek, odmítnutý přístup (SLV i Sagasu vyžadují přihlášení), nedostupný nástroj a neúplný obsah. Identický neúspěšný dotaz neopakuj bez změny; zkus věcně odůvodněnou alternativu (jiný index, jiný režim hledání, kratší dotaz), pak mezeru přesně označ `[DOPLNIT]`. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením. Znění, soud, spisovou značku a datum přebírej jen z načteného zdroje.

Je-li pro dílčí práci použit další agent nebo skill, předej mu výslovně tento zdrojový režim, rozhodné skutky a časové otázky. Vyžádej konkrétní zdrojové pasáže; jeho shrnutí nenahrazuje načtený pramen.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a z listin, které uživatel předložil; právní tvrzení v nich nejsou nezávisle ověřeným právem. Rejstříkové údaje (subjekt, statutární orgán, sbírka listin, insolvence, datová schránka) ověřuj v Sagasu podle oddílu Zdrojový režim; jiné externí databáze a místní archivy bez pokynu nenačítej. Chybějící skutkový doklad si vyžádej od uživatele a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v SLV a e-Sbírce. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v SLV a e-Sbírce. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. V SLV používej filtry podle jejich skutečného významu: index soudu (`idx`), vazbu na předpis (`reg_num`, `reg_year`, `reg_par`, případně `reg_num2`…), časový filtr `date_from` a režim hledání (`bm25`, `knn`, `hybrid`). Judikaturu hledej v SLV přes indexy `ns`, `nss`, `us`, `justice` a `isir`, předpisy přes `search_regulations` a jejich znění v e-Sbírce; unijní předpisy a judikaturu SDEU a ESLP ověř v oficiálních databázích (EUR-Lex, CURIA, HUDOC). Komentář, literatura a vzor slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v SLV nebo e-Sbírce.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Neomezuj se na první várku výsledků: rozšiř dotazy na další indexy, režimy a `date_from` a prověř související i navazující dokumenty (u rozhodnutí `citedBy` a `citedCaseLaw` z `fetch_decision`, u předpisu `souvislosti` v e-Sbírce). Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, vyhledej pro každý nosný paragraf rozhodnutí, která ho citují: `search_decisions` s `reg_num`, `reg_year` a `reg_par` (bez dotazu vrátí všechna rozhodnutí citující ustanovení, nejnovější první; s krátkým dotazem je seřadí podle relevance uvnitř této množiny). Fulltext je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje vazbu na paragraf.

1. **Kandidáti:** hledej přes indexy `ns`, `nss` a `us` (podle oboru i `justice`, v insolvenci `isir`) — jedno volání = jeden index. Projdi alespoň prvních 20 kandidátů a relevantní zařaď do výběru. Zvlášť dohledej nejnovější rozhodnutí (`date_from` na poslední roky), aby ti neunikl pozdější vývoj. Druhé ustanovení lze přidat přes `reg_num2`/`reg_year2`/`reg_par2`.
2. **Skutková shoda:** doplň fulltextem. Režim `bm25`: 2–5 výrazných právních pojmů, všechna slova musí v textu být (nula výsledků znamená vypustit slovo, ne absenci judikatury). Režim `knn`: jedna právní otázka formulovaná jako právní věta; víc otázek rozděl do více dotazů. Známou spisovou značku dohledej `search_by_case_number`.
3. **Třídění kandidátů** (před načtením celého textu podle kroku 4):
   - **citační graf:** `fetch_decision` vrací `citedBy` (pozdější rozhodnutí, která ho citují) a `citedCaseLaw`; sleduj `citedBy` 1–2 skoky k nejnovějšímu vyjádření téže právní věty a k případnému odklonu. Absence odklonu v `citedBy` pozdější odklon nevylučuje (citační graf nemusí být úplný), proto doplň i `search_decisions` s `date_from`;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (výsledky s `date_from` z bodu 1 a fulltext `velký senát <právní pojem>`). Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované v oficiální sbírce má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření v e-Sbírce (`diff`, `par --k`), že se pravidlo věcně nezměnilo; ustanovení, která rozhodnutí skutečně aplikovalo, jsou v `regulations[]` z `fetch_decision`.
4. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf nic nevrací, uveď to a pokračuj fulltextem.
5. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti v e-Sbírce (`par --k <datum>`, případně `text`) úplný text použitého ustanovení ve znění účinném k rozhodnému dni, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky; SLV použij jen k identifikaci předpisu. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v SLV relevantní pozdější, překonávající a nepříznivou judikaturu (`citedBy` z `fetch_decision`, `search_decisions` s `date_from`); nálezy ÚS rušící použité ustanovení ověř v e-Sbírce (`souvislosti`). Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástrojů, nikoli o tvrzení o automatickém ověření, které neproběhlo. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení v SLV a e-Sbírce.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí v SLV (`search_decisions` v příslušném indexu, `search_by_case_number`); obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej jen z odpovědí SLV, e-Sbírky a Sagasu, u unijních pramenů a judikatury SDEU a ESLP z EUR-Lex, CURIA a HUDOC; URL nesestavuj ani nedomýšlej. Ve výstupu uveď přesnou právní citaci (soud, spisová značka, datum, případně ECLI; předpis číslem ve Sbírce, §, odstavec, písmeno), nikoli interní ID nástroje. Pokud odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revizi či kontrolu, pokud skutečně neproběhly a nedokládá je výsledek nástroje.

Zkontroluj všechny požadované artefakty. Označ pracovní, neúplný či k revizi určený výstup pravdivě. Uložení, odeslání, doručení, podpis a podání jsou odlišné stavy; žádný nepředstírej. Bez výslovného pokynu nic neposílej ani nepodávej. Nedodané části a neověřené rozhodné zdroje nesmějí být skryty prohlášením „hotovo“ nebo „vše ověřeno“.

## Oborové otázky a požadované výstupy

## Oborový postup: věcná práva a sousedské spory

### Skutkový a právní předmět

Urči klientovu roli, cíl a skutečný zásah: zadržování věci, užívání bez titulu, imise, spornou hranici, chybějící přístup, spor spoluvlastníků nebo nesoulad evidence. Z dodaných listin identifikuj aktuální a historické vlastnictví, parcely, stavby, jednotky, podíly, mapy a skutečné užívání. Výpis, geometrický plán, fotografie a tvrzení souseda mají odlišnou vypovídací hodnotu.

Časovou osu veď pro nabytí, držbu, výstavbu, souhlas, vznik břemene a počátek zásahu. Rozliš doloženou skutečnost, tvrzení a neznámý údaj. Je-li poloha nemovitosti známa, neztrácej ji při právní analýze a nevytvářej umělou informační překážku vyžadováním nesouvisejícího bydliště. Připravená výzva není odeslaná, předpokládaná škoda není doložená a chybějící vyčíslení není nulou.

### Vlastnictví, držba a hranice

Podle cíle zvaž vydání nebo vyklizení, zdržení zásahu, odstranění následku, určení práva, ochranu držby, zřízení práva či vypořádání. U každé cesty ověř aktivní i pasivní legitimaci, případný naléhavý právní zájem, důkazní břemeno a vykonatelnost. Nezaměňuj žalobu na určení vlastnictví s opravou chyby evidence.

U vydržení zkoumej řádný a mimořádný režim, existenci a dobu držby, vlastnický úmysl, poctivost, právní důvod a návaznost předchůdců. Důkaz trvání držby nesmí nahradit pouhý odkaz na domněnku; dobrou víru a nepoctivý úmysl neztotožňuj. Ověř přechodné režimy a překážky. Nabytí od neoprávněného, spolehnutí na evidenci, opuštění věci a přírůstky posuď podle konkrétních podmínek, nikoli obecné preference zapsaného vlastníka.

U hranice rozliš technickou nepřesnost zobrazení, nejistou hranici a spor o vlastnictví určitého pásu. Zjisti potřebné zaměření, historické podklady a správné vymezení předmětu řízení. Pokud výrok vyžaduje geometrický plán, určuj jeho roli a návaznost na petit.

### Sousedství a přístup

U imisí ověř přímý či nepřímý charakter, místní poměry, míru zásahu, podstatné omezení užívání a právní význam povoleného provozu. Povolení není univerzální imunitou; prověř jeho rozsah, překročení a povahu dostupné nápravy. Rozliš zdržovací povinnost od příkazu provést konkrétní technické opatření a od peněžité kompenzace.

Samostatně řeš kořeny, větve, plody, stromy, vodu, oporu stavby, údržbu, vstup a nezbytné práce. U výsadby ověř rozhodné datum a relevantní výjimky. Požadavek na zásah do stromu musí počítat s odbornou proveditelností a veřejnoprávními omezeními. Obecný nárok souseda nenahrazuje potřebné povolení nebo bezpečný postup.

U nezbytné cesty odliš skutečnou potřebu řádného užívání od pohodlnějšího spojení. Vyhodnoť alternativy, rozsah zatížení, náhradu, jistotu, možnost smluvního řešení a veřejně přístupnou komunikaci. Nabytí nemovitosti bez přístupu neoznačuj samo o sobě za automatickou hrubou nedbalost. Ověř příslušný civilní nebo správní režim.

### Spoluvlastnictví, stavby a břemena

U správy společné věci zkoumej povahu rozhodnutí, hlasování, vyrozumění, ochranu přehlasovaného či opomenutého a rozhodnou lhůtu. Ověř nakládání s podílem, případné předkupní právo a jeho časový režim. Odděl náhradu za nadužívání, výnosy, investice, nutné náklady a odměnu správce.

U zrušení a vypořádání spoluvlastnictví prověř zákonné pořadí a podmínky jednotlivých způsobů, reálnou dělitelnost, solventnost zájemce, ocenění a potřebná břemena. Náklady řízení vyžadují posouzení konkrétních procesních okolností, nikoli automatickou poučku o vítězi. Společné jmění posuzuj odděleně.

U staveb na cizím pozemku, přestavku, práva stavby, podzemních sítí a dočasných staveb ověř časový režim, vlastnictví, souhlas, dobrou víru a dostupné vypořádání. Neoprávněnost soukromoprávní není totéž co absence stavebního povolení. U služebností a reálných břemen řeš vznik, obsah, osoby, rozsah chůze či jízdy, údržbu, změnu a zánik. Pouhá tolerance užívání nemusí být právním titulem. Veřejnoprávní práva sítí a soukromé břemeno nejsou zaměnitelné.

### Evidence a procesní cesta

U vkladu, záznamu, poznámky, opravy chyby, obnovy operátu, duplicity nebo pozemkových úprav ověř správný institut, orgán a prostředek ochrany. Poznámku spornosti propojuj s konkrétní žalobou, daty a účinky vůči dalším osobám; nevytvářej automatický závěr o ochraně bez splnění všech podmínek.

Před závěrem vytvoř tabulku všech konečně navržených nároků: obsah výroku, samostatný/kumulovaný/eventuální vztah, pravomoc, věcná a místní příslušnost, právní podklad, poplatková položka, základ, sazba a částka. Zahrň i peněžité nároky, které jsi doporučil dodatečně během zpracování. Tabulku po každém rozšíření návrhu aktualizuj.

U zápůrčí žaloby týkající se nemovitosti, včetně imisí, v SLV a e-Sbírce výslovně prověř zvláštní či výlučnou místní příslušnost podle polohy nemovitosti, nejen obecný soud žalovaného. Posuď hierarchii pravidel a skutečný charakter nároku. Je-li rozhodná poloha doložena, uveď odpovídající soud po ověření; nepodmiňuj odpověď automaticky bydlištěm žalovaného. U připojeného peněžitého nároku znovu ověř jeho příslušnost a podmínky společného projednání.

### Úplné náklady a konečný výstup

Příslušnost soudu neřeší poplatkovou kvalifikaci. U nepeněžitého nároku ověř skutečný předmět a odpovídající judikaturu k poplatku; neurčuj položku podle samotného názvu žaloby ani mechanicky podle počtu parcel. Odliš zdržení zásahu, provedení činnosti, určení a zřízení věcného práva. Při právně relevantní nejistotě dolož hlavní variantu a konkrétní alternativu.

Rozpočet musí zahrnout všechny konečně navržené peněžité i nepeněžité složky se správným pravidlem kumulace nebo eventuality. Odděl poplatek za prozatímní ochranu, jistotu, zastoupení, znalce a případnou daň; poplatky vypočti `soudni_poplatek` a odměnu za zastoupení `odmena_advokata`, obojí přepočítej druhou cestou. Neúplný dílčí součet neoznačuj jako celkové náklady.

Dodej použitelnou žalobu, předžalobní výzvu, dohodu nebo smluvní ustanovení, důkazy a hlavní protiargumenty. Předžalobní postup posuď zvlášť pro náhradu nákladů a zvlášť pro přípustnost žaloby. Petit musí přesně určit osobu, nemovitost, jednání a rozsah povinnosti; nevkládej nedoložené datum výzvy nebo částku.
