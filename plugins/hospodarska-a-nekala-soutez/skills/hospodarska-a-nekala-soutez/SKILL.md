---
uuid: 2914684d-f296-46fe-b4a9-452343588299
name: hospodarska-a-nekala-soutez
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Hospodářská a nekalá soutěž ČR"
    summary: "Kartely, zneužití dominance, spojování soutěžitelů a řízení před ÚOHS, náhrada škody, nekalá soutěž a její nároky, regulace reklamy a nekalé obchodní praktiky."
    examplePrompts:
      - "Distributor nám v e-mailu píše, ať nedáváme cenu pod jeho doporučenou. Je to problém a co s tím?"
      - "Konkurent v reklamě tvrdí, že náš výrobek je nebezpečný. Jaké nároky máme a jak rychle?"
      - "ÚOHS provedl u klienta místní šetření. Jaká má klient práva a co dělat v prvních dnech?"
  en:
    displayName: "Czech Competition and Unfair Competition"
    summary: "Cartels, abuse of dominance, merger control and ÚOHS proceedings, damages, unfair competition claims, advertising regulation and unfair commercial practices."
    examplePrompts:
      - "A distributor e-mails us not to price below its recommended price. Is that a problem and what to do?"
      - "A competitor's advertising claims our product is dangerous. Which claims do we have and how fast?"
      - "The ÚOHS carried out a dawn raid at the client's premises. What are the client's rights and what to do in the first days?"
  sk:
    displayName: "Hospodárska a nekalá súťaž ČR"
    summary: "Kartely, zneužitie dominancie, koncentrácie a konanie pred ÚOHS, náhrada škody, nekalá súťaž a jej nároky, regulácia reklamy a nekalé obchodné praktiky v ČR."
    examplePrompts:
      - "Distribútor nám v e-maile píše, aby sme nedávali cenu pod jeho odporúčanú. Je to problém a čo s tým?"
      - "Konkurent v reklame tvrdí, že náš výrobok je nebezpečný. Aké nároky máme a ako rýchlo?"
      - "ÚOHS vykonal u klienta miestne šetrenie. Aké má klient práva a čo robiť v prvých dňoch?"
description: Veřejnoprávní ochrana hospodářské soutěže, soukromoprávní nekalá soutěž a navazující reklamní regulace. Kartely, vertikální omezení, dominance, spojování soutěžitelů, místní šetření, compliance, náhrada soutěžní škody, významná tržní síla a smluvní náprava ve prospěch klienta.
---

# Hospodářská a nekalá soutěž

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

## Vymezení větví a rozhodných skutečností

Rozliš veřejnoprávní soutěžní dohled, soukromoprávní ochranu před nekalou soutěží a ochranu spotřebitele či regulaci reklamy. Stejné jednání může vyžadovat více samostatných testů, příslušných orgánů a procesních prostředků. Zjisti postavení klienta: vyšetřovaný soutěžitel, dodavatel, distributor, dominantní podnik, poškozený konkurent, zákazník, asociace nebo účastník spojení. Definuj požadovaný výsledek, naléhavost a obchodní zájem, který má být zachován.

Zmapuj produkty, geografii, zákazníky, distribuční model, skupinu, tok informací, dohodnuté a skutečné chování, relevantní období a důkazy. Obraty, podíly, dominanci, cenový dopad ani účast na kartelu nedoplňuj odhadem bez označení. V nativním CODEXIS vyhledej rozhodné české a unijní normy, prováděcí úpravu a výklad pro příslušné období; u soft law odděl právní sílu od závazných předpisů.

## Dohody, výjimky a obchodní omezení

U horizontální dohody, bid riggingu, výměny informací, rozhodnutí asociace, hub-and-spoke a vertikálního vztahu zjisti, zda existuje dohoda či koordinace, mezi jakými subjekty a o čem. Jde o omezení podle cíle, nebo je třeba dokazovat účinky? Je dotčen obchod mezi členskými státy? Jak jsou vymezeny relevantní trh, hospodářská jednotka a případná agentura nesoucí skutečné riziko?

U blokové výjimky vyhledej její aktuální věcnou, osobní a časovou působnost, podmínky, zakázaná omezení a relevantní přechodná pravidla. Ztráta výjimky není sama závěrem o protiprávnosti ani neplatnosti celé smlouvy. Samostatně zvaž individuální výjimku, prokázané efektivity, prospěch zákazníků, nezbytnost a zachování soutěže; pravidlo zanedbatelnosti nepoužívej plošně na zakázané cíle.

U cen dalšího prodeje prověř nejen znění, ale i pobídky, sankce, monitoring, e-maily a vynucování. U doporučené nebo maximální ceny nestačí název. Rozliš aktivní a pasivní prodej, výhradní a selektivní systém, zákazníky, území, tržiště a účinné využívání internetu. Prověř dvojí ceny, parity a sdílení informací při duální distribuci. U zákazu konkurence odděl trvání a období po skončení, automatické obnovování, skutečnou možnost výpovědi, náklady změny dodavatele a ochranu know-how. Navrhni proveditelnou náhradu každé problematické klauzule.

## Dominance, spojování a zvláštní trhy

Relevantní trh vymez podle zastupitelnosti, poptávky, nabídky a dostupných dat; případný cenový test označ za metodický nástroj, nikoli fiktivně provedené měření. Jaké skutečnosti podporují dominanci vedle podílu a jaký význam mají bariéry vstupu či vyjednávací síla odběratelů? Prověř diskriminaci, nepřiměřené ceny a podmínky, predaci, věrnostní slevy, vázání, odmítnutí dodávek a stlačení marží podle jejich samostatných znaků a objektivních ospravedlnění.

U digitálních trhů odděl soutěžní právo od zvláštního režimu určených poskytovatelů. U významné tržní síly a potravinových obchodních praktik ověř osoby, produkty, vztah stran, zakázané praktiky a smluvní požadavky; nepřenášej závěry automaticky na jiné sektory.

U spojení prověř vznik či změnu kontroly, společný podnik, správný rozsah skupinových obratů a rozhodné období. Zjisti českou a unijní příslušnost, postoupení, případné další přezkumné mechanismy, zákaz uskutečňování před povolením, výjimky a závazky. Nezaměňuj právní podpis smlouvy s převzetím faktické kontroly.

## Šetření, obhajoba a sankce

Při místním šetření navrhni okamžitý protokol: ověření pověření a rozsahu, přítomnost právní pomoci, odpovědné osoby, záznam úkonů, ochrana důvěrných materiálů a kontrola kopií. Jaké pravomoci má orgán ke vstupu, vysvětlením, elektronickým datům a vzdáleným úložištím? Jak se v konkrétním režimu chrání komunikace s advokátem? Nenavrhuj mazání, ukrývání ani maření důkazů. Sporný postup řeš doloženou námitkou a příslušným přezkumem.

Odděl sektorové šetření od řízení proti konkrétnímu subjektu. U leniency vyhledej pořadí, rozsah spolupráce, překážky a podmínky výsledku; bez rozhodnutí neslibuj imunitu. Narovnání a závazky porovnej podle uznání skutku, procesních práv, sankce, soukromých žalob a publicity. Sankční výpočet vyžaduje ověřený základ, období, přičitatelnost, přitěžující a polehčující okolnosti; odděl odpovědnost právnických a fyzických osob a dopady do veřejných zakázek. Připrav řádné a soudní opravné prostředky včetně lhůt a případné dočasné ochrany.

## Nekalá soutěž, reklama a náhrada škody

U nekalé soutěže nejdříve ověř obecné předpoklady, potom konkrétní skutkovou podstatu. Prověř klamavou a srovnávací reklamu, vyvolání záměny, parazitování, podplácení, zlehčování, obchodní tajemství, dotěrné či agresivní praktiky. Pravdivost jednotlivého údaje neprokazuje přípustnost celé reklamy. Zvlášť řeš influencery, environmentální tvrzení a výrobkové sektory s vlastními reklamními omezeními; budoucí unijní změnu neprezentuj jako již použitelnou.

Kdo má aktivní legitimaci a proti komu nárok směřuje? Kdy se mění důkazní břemeno? Odděl zdržení, odstranění závadného stavu, přiměřené zadostiučinění, škodu a bezdůvodné obohacení. Navrhni určitý petit, předběžné opatření a zajištění důkazu s ověřenými podmínkami jistoty, příslušnosti a nákladů.

U soutěžní škody vyhledej účinky rozhodnutí orgánu, případnou domněnku újmy, zpřístupnění důkazů, přenesení navýšení ceny, solidaritu a regres. Výši újmy založ na vysvětleném kontrafaktuálním scénáři a skutečných datech. Ověř počátek a stavění promlčení i vztah kolektivního, veřejnoprávního a individuálního řízení.

## Požadovaný výstup

Dodej oddělené závěry pro každou právní větev, důkazní mapu, nejsilnější protiargumenty, realistické nápravné varianty a přesné podání nebo smluvní redline podle zadání. Každá klauzule musí mít použitelnou náhradu, která chrání legitimní obchodní účel klienta; pouhé označení rizika nestačí. Compliance plán pokryje cenovou komunikaci, asociace, školení, šetření, hlášení incidentů a soutěžní DD. U praxe příslušného senátu uváděj jen skutečně prověřené rozhodování, jeho relevantní odlišnosti a nevyplněná místa.
