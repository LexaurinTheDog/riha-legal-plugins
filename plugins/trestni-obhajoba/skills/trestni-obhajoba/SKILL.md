---
uuid: 8816d448-3893-4cdd-84e7-de45a5eafe98
name: trestni-obhajoba
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Trestní právo a obhajoba ČR"
    summary: "Obhajoba a zastupování poškozeného ve všech fázích trestního řízení - lhůty, vazba, zajištění majetku, odklony, opravné prostředky, trestní odpovědnost právnických osob."
    examplePrompts:
      - "Klientovi bylo dnes doručeno usnesení o zahájení trestního stíhání pro podvod. Co má obhájce udělat v prvních dnech?"
      - "Policie zajistila peníze na účtu klienta podle § 79a. Jak se bránit a jaké lhůty běží?"
      - "Připrav osnovu odvolání proti odsuzujícímu rozsudku - procesní vady a nesprávné hodnocení důkazů."
  en:
    displayName: "Czech Criminal Law and Defence"
    summary: "Defence and victim representation at every stage of Czech criminal proceedings - deadlines, custody, asset seizure, diversions, remedies, corporate liability."
    examplePrompts:
      - "My client was served today with a resolution commencing prosecution for fraud. What must defence counsel do in the first days?"
      - "Police froze funds on the client's account under § 79a. How do we challenge it and which deadlines run?"
      - "Draft an outline of an appeal against a conviction - procedural defects and flawed evaluation of evidence."
  sk:
    displayName: "Trestné právo a obhajoba ČR"
    summary: "Obhajoba a zastupovanie poškodeného vo všetkých fázach českého trestného konania - lehoty, väzba, zaistenie majetku, odklony, opravné prostriedky, zodpovednosť právnických osôb."
    examplePrompts:
      - "Klientovi bolo dnes doručené uznesenie o začatí trestného stíhania pre podvod. Čo má obhajca urobiť v prvých dňoch?"
      - "Polícia zaistila peniaze na účte klienta podľa § 79a. Ako sa brániť a aké lehoty bežia?"
      - "Priprav osnovu odvolania proti odsudzujúcemu rozsudku - procesné vady a nesprávne hodnotenie dôkazov."
description: Use for Czech criminal defence from suspicion and investigation through charging, custody, searches, asset seizure, trial, negotiated outcomes, remedies and execution; include victims, witnesses, juveniles, corporate defendants and compensation claims where connected. Research legal sources only through native CODEXIS in the application.
---

# Trestní obhajoba

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

## Oborový postup: trestní obhajoba

### Role, fáze a bezprostřední riziko

Nejprve urči, zda klient je podezřelý, obviněný, obžalovaný, odsouzený, poškozený, svědek nebo právnická osoba. Zaznamenej věk, zastoupení, omezení osobní svobody, zajištěný majetek a skutečný procesní stav podle dodaných listin. Samotná informace o prověřování není důkazem zahájeného stíhání. Ověř případ nutné obhajoby, oprávnění zástupce a konflikt zájmů mezi více klienty.

Sestav chronologii skutku, úkonů a doručení klientovi i obhájci. U naléhavých opatření pracuj s doloženými hodinami a minutami; k zákonné době nepřidávej další kalendářní den. Rozliš včasné podání opravného prostředku a jeho odůvodnění, možnost doplnění i zvláštní požadavky konkrétního prostředku. Ověř přesný orgán, formu, počátek a konec lhůty.

### Skutek a právní kvalifikace

Ke každému skutku sestav matici zákonných znaků, tvrzení obžaloby, skutečně doložených důkazů a sporných nebo chybějících podmínek. Odděl jednání, následek, příčinnou souvislost a zavinění. Podle věci prověř pokus, přípravu, účastenství, pokračování, souběh, okolnosti vylučující protiprávnost, trestní odpovědnost a promlčení.

V CODEXIS ověř znění k rozhodnému jednání i případné pozdější příznivější právo jako souvislý použitelný režim. Nemíchej výhodné části různých verzí bez právní opory. Ověř totožnost skutku, dostatečnou konkrétnost usnesení o zahájení stíhání a možnost odlišné kvalifikace. Civilní neplnění, správní pochybení nebo neúspěšné podnikání nepovažuj bez doložení znaků za trestný čin.

### Důkazy a obhajoba

U každého důkazu odděl získání, uchování, provedení a hodnocení. Prověř výslechy, rekognici, znalecké závěry, listiny, odposlechy, sledování, prohlídky a digitální data. Zjišťuj konkrétní zákonný podklad, oprávněný orgán, rozsah povolení, poučení a možnost účinného zpochybnění. Vadu jednoho úkonu nepřeváděj automaticky na nepoužitelnost všech dalších důkazů; ověř rozhodné pravidlo a judikaturu.

U elektronických zařízení zvlášť zkoumej titul zajištění zařízení, oprávnění k prohlídce jeho obsahu, možné zákonné výjimky a ochranu důvěrné komunikace. Nepředpokládej, že každý přístup vždy vyžaduje nové povolení, ani že původní zajištění dovoluje neomezené čtení. U privilegovaného obsahu určuj konkrétní ochranný postup, adresáta námitek a přezkumný prostředek.

Vyhodnoť přístup do spisu, právo na obhájce, překlad, kontradiktornost a možnost navrhnout důkazy. Sestav hlavní i eventuální obhajobu, očekávanou reakci státního zástupce a nejúčinnější způsob jejího vyvrácení. Rozliš doložený rozpor od pouhé alternativní hypotézy; nepřisuzuj klientovi nové skutkové doznání kvůli rétorické přesvědčivosti.

### Svoboda a zajištění

U zadržení a vazby přiřaď každé omezení ke konkrétnímu důvodu, důkazu, času a rozhodnutí. Ověř aktuálnost obavy, proporcionalitu, mírnější alternativy, přezkum trvání, opravný prostředek a proces předání soudu. Návrh na propuštění nebo náhradu vazby musí reagovat na skutečné důvody, ne pouze citovat obecné právo na svobodu.

U majetku rozliš zajištění konkrétního výnosu či věci, náhradní hodnoty, nároku poškozeného a budoucí sankce. Ověř osobu vlastníka, rozsah dispozičního zákazu, pravomoc, odůvodnění a přípustné přezkoumání. Zkoumej délku, hodnotový poměr, provozní potřeby, práva třetích osob a možnost částečného uvolnění. U nakládání se zajištěnými penězi nebo jinou úschovou ověř zákonný způsob a určeného příjemce; nenavrhuj vlastní neověřený mechanismus.

### Alternativy, zvláštní osoby a rozhodnutí

U dohody o vině a trestu, prohlášení viny, spolupracujícího obviněného a odklonů ověř všechny předpoklady, důsledky pro dokazování a opravné prostředky. Srovnej reálný trestní, majetkový, profesní a reputační dopad. Přiznání, náhradu újmy nebo souhlas s postupem nepředpokládej bez klientova informovaného rozhodnutí.

U právnické osoby posuzuj přičitatelnost, funkčnost compliance, samostatné zastoupení a střet s obhajobou konkrétních fyzických osob. U mladistvého zohledni zvláštní režim řízení a sankcí. U poškozeného rozliš majetkovou škodu, nemajetkovou újmu a bezdůvodné obohacení; dolož uplatnění, výši, lhůtu, zajištění a podmínky rozhodnutí v adhezním řízení nebo odkazu jinam.

### Procesní výstup a kontrola

Podle fáze připrav skutečnou stížnost, důkazní návrh, vyjádření, závěrečnou řeč, odvolání, dovolání, návrh obnovy nebo podání ve výkonu rozhodnutí. Každý prostředek musí mít vlastní přípustnost, důvody a odpovídající petit. Ústavní rovinu odliš od dalšího běžného skutkového odvolání.

Připoj důkazní a časovou tabulku, silné i slabé stránky, klientova rozhodnutí a nákladový rozpočet. Rozliš smluvní odměnu, ustanovenou obhajobu, náklady státu a náhradu poškozenému. Žádný strategický krok nesmí spočívat v ničení důkazů, ovlivňování svědků nebo maření řízení. Připravený text není podaným prostředkem; jeho skutkové i právní mezery označ konkrétně.
