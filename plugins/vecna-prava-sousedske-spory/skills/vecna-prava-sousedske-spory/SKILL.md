---
uuid: cda9fbb1-2613-40b9-9745-13974d2c8cd1
name: vecna-prava-sousedske-spory
version: 1.1.0
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
description: Use for Czech ownership, possession, acquisitive prescription, easements, necessary access, co-ownership, boundaries, structures on another's land, registry disputes and neighbour interference. Include claim-specific venue, enforceable remedies and complete fee calculations; use transaction-focused skills for a pure conveyance. Research legal sources only through native CODEXIS in the application.
---

# Věcná práva a sousedské spory

## Výhradní zdrojový režim: nativní CODEXIS ve vm.codexis.ai

Tento skill pracuje pouze v aplikaci vm.codexis.ai. Právní předpisy, judikaturu, komentáře a vzory získávej výhradně jejím nativním nástrojem CODEXIS. Žádné externí vyhledávání, webové zdroje, náhradní databáze ani přímá API mimo tento nástroj. To platí i při výpadku, nenalezení dokumentu, potřebě historického nebo cizojazyčného znění a u podkladů správních orgánů. Pokud obecný návod jiného skillu dovoluje externí zdroje, pro tuto úlohu se tato možnost nepoužije. Odkaz na externí web nalezený uvnitř dokumentu není oprávněním přejít mimo CODEXIS.

Použij skutečně dostupné nativní rozhraní a jeho dokumentované parametry. V této aplikaci může být nativní CODEXIS zpřístupněn vestavěným aplikačním konektorem `cdx-cli`; jeho použití uvnitř aplikace výhradně pro CODEXIS je dovoleno. Není tím dovoleno spouštět CLI na uživatelově počítači, instalovat software, prohledávat přihlašovací údaje, konfigurovat vlastní klienty ani nahrazovat nativní konektor vlastními síťovými požadavky. Technickou syntaxi vezmi z dostupného návodu nativního nástroje; nevymýšlej názvy funkcí, identifikátory, parametry ani endpointy. Pokud je potřeba načíst dodávaný návod CODEXIS, použij z něj pouze technické rozhraní slučitelné s tímto výhradním zdrojovým režimem.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán; existence skillu nebo konektoru sama nedokládá funkční rešerši. Rozliš prázdné výsledky, odmítnutý přístup, nedostupný nástroj a neúplný obsah. Identický neúspěšný požadavek neopakuj bez změny okolností; zkus jen věcně odůvodněnou alternativu uvnitř CODEXIS, pak přesně označ mezeru. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením.

Je-li pro dílčí práci použit další dostupný agent nebo skill v aplikaci, předej mu výslovně stejný výhradní zdrojový režim, rozhodné skutky a časové otázky. Vyžádej jeho konkrétní zdrojové pasáže a omezení. Jeho shrnutí ani prohlášení o ověření nenahrazují skutečné výsledky nativního nástroje; za jejich sjednocení a kontrolu konečné citace odpovídá hlavní zpracovatel.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a příloh zpřístupněných uživatelem v aplikaci; právní tvrzení v nich nejsou nezávisle ověřeným právem. Nenačítej externí rejstříky ani místní archivy. Chybějící skutkový doklad si vyžádej jako podklad do aplikace a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v CODEXIS. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v CODEXIS. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. Používej dostupné oborové, soudní a časové filtry podle jejich skutečného významu. V dokumentovaném členění CODEXIS jsou české předpisy CR, česká judikatura JD, unijní předpisy EU, evropská judikatura ES, slovenské předpisy SK, komentáře COMMENT, literatura LT a vzory VS; globální ALL použij jen k orientaci a poté ověř konkrétní pramen. Komentář, literatura a vzor nalezené v CODEXIS slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v CODEXIS.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Projdi pokračování cílených výsledků, pokud je nativní nástroj zpřístupňuje, a prověř relevantní související i navazující dokumenty. Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf (R5)

Tato cesta je dokumentována ve schématu nativního konektoru (`cdx-cli schema related`, parametr `part`) a byla ověřena v aplikaci 25. 9. 2026. **Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf **oba** příkazy z bodů 1 a 2. Samotný počet z `/related/counts` nic nevybírá a krok nesplňuje. Fulltextové hledání v `JD` je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Počet navázané judikatury:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related/counts?part=paragraf<N>'` (např. `paragraf198`, `paragraf19c`; `elementId` ověř přes `/toc`).
2. **Kandidáti:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related?part=paragraf<N>&type=SOUVISEJICI_JUDIKATURA&limit=20'` - řazeno podle relevance; pro vývoj judikatury přidej `&sort=date`, další stránky `&offset=20`, `&offset=40` … Projdi alespoň prvních 20 kandidátů (titulek, `/meta`) a relevantní zařaď do výběru. Vrácená `docId` lze přímo použít v `cdx://doc/<docId>/meta` a `/text`.
3. **Skutková shoda:** doplň fulltextem `search JD` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2-5 slov). Filtr soudu používej jen s přesnými hodnotami facety: `Nejvyšší soud`, `Nejvyšší správní soud`, `Ústavní soud`, `Vrchní soud` (Praha × Olomouc přes `--city "Praha"` / `--city "Olomouc"`); jiné hodnoty ověř přes `--with-facets`. Pro novou úpravu omez stáří přes `--issued-from`.
4. **Třídění kandidátů podle `/meta`** (před načtením celého textu podle kroku 4):
   - `derogated: true` → rozhodnutí je v CODEXIS označeno jako překonané; jako oporu je nepoužij. `false` nevylučuje pozdější odklon - ten prověř podle kroku 4;
   - vyplněné `sbirkoveCislo` (např. `Rc 105/2013`) = publikováno v oficiální sbírce; má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření, že se pravidlo věcně nezměnilo.
5. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf vrací nulu, uveď to a pokračuj fulltextem.
6. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti v CODEXIS úplný text použitého ustanovení v dané verzi, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v CODEXIS relevantní pozdější, překonávající a nepříznivou judikaturu. Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástroje, nikoli o tvrzení, že aplikace provedla neexistující automatickou certifikaci. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení v CODEXIS.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí v CODEXIS; obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej ze zdrojového bloku nativního nástroje; nesestavuj neověřené URL a nepřecházej kvůli jejich ověření na externí web. Ve výstupu použij nástrojem vrácený uživatelský odkaz a přesnou právní citaci, nikoli interní ID či technickou adresu. Pokud uživatelský odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revize či kontrolu, pokud neproběhly dostupnými nástroji aplikace.

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

U zápůrčí žaloby týkající se nemovitosti, včetně imisí, v CODEXIS výslovně prověř zvláštní či výlučnou místní příslušnost podle polohy nemovitosti, nejen obecný soud žalovaného. Posuď hierarchii pravidel a skutečný charakter nároku. Je-li rozhodná poloha doložena, uveď odpovídající soud po ověření; nepodmiňuj odpověď automaticky bydlištěm žalovaného. U připojeného peněžitého nároku znovu ověř jeho příslušnost a podmínky společného projednání.

### Úplné náklady a konečný výstup

Příslušnost soudu neřeší poplatkovou kvalifikaci. U nepeněžitého nároku ověř skutečný předmět a odpovídající judikaturu k poplatku; neurčuj položku podle samotného názvu žaloby ani mechanicky podle počtu parcel. Odliš zdržení zásahu, provedení činnosti, určení a zřízení věcného práva. Při právně relevantní nejistotě dolož hlavní variantu a konkrétní alternativu.

Rozpočet musí zahrnout všechny konečně navržené peněžité i nepeněžité složky se správným pravidlem kumulace nebo eventuality. Odděl poplatek za prozatímní ochranu, jistotu, zastoupení, znalce a případnou daň. Neúplný dílčí součet neoznačuj jako celkové náklady.

Dodej použitelnou žalobu, předžalobní výzvu, dohodu nebo smluvní ustanovení, důkazy a hlavní protiargumenty. Předžalobní postup posuď zvlášť pro náhradu nákladů a zvlášť pro přípustnost žaloby. Petit musí přesně určit osobu, nemovitost, jednání a rozsah povinnosti; nevkládej nedoložené datum výzvy nebo částku.
