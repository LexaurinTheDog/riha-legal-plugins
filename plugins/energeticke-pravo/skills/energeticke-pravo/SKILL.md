---
uuid: 4e1b642c-1332-469b-8d06-72075b71159d
name: energeticke-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Energetické právo ČR"
    summary: "Licence a regulace ERÚ, smlouvy o dodávce elektřiny a plynu a změna dodavatele, podpora a povolování OZE, komunitní energetika a sdílení, připojení k síti, cenová regulace a spory, teplárenství, energetická náročnost budov."
    examplePrompts:
      - "Dodavatel elektřiny jednostranně zvýšil cenu a klient chce odejít bez sankce. Jaké jsou lhůty a jak správně vypovědět smlouvu?"
      - "Obec chce postavit FVE na střechách škol a sdílet elektřinu mezi budovami. Jaký režim (energetické společenství, sdílení) a jaká povolení?"
      - "Distributor odmítl připojit výrobnu 500 kW pro nedostatek kapacity. Lze se bránit a u koho?"
  en:
    displayName: "Czech Energy Law"
    summary: "Energy Act licences and ERÚ regulation, electricity and gas supply contracts and switching, renewable support and permitting, community energy and self-consumption, grid connection, price regulation and disputes, heat supply, energy performance of buildings."
    examplePrompts:
      - "An electricity supplier unilaterally raised the price and my client wants to leave without penalty. What are the deadlines and how to terminate properly?"
      - "A municipality wants rooftop PV on schools and to share electricity between buildings. Which regime (energy community, sharing) and which permits?"
      - "The distributor refused to connect a 500 kW plant for lack of capacity. Can we challenge it and where?"
  sk:
    displayName: "Energetické právo ČR"
    summary: "Licencie a regulácia ERÚ, zmluvy o dodávke elektriny a plynu a zmena dodávateľa, podpora a povoľovanie OZE, komunitná energetika a zdieľanie, pripojenie do siete, cenová regulácia a spory, teplárenstvo, energetická náročnosť budov."
    examplePrompts:
      - "Dodávateľ elektriny jednostranne zvýšil cenu a klient chce odísť bez sankcie. Aké sú lehoty a ako správne vypovedať zmluvu?"
      - "Obec chce postaviť FVE na strechách škôl a zdieľať elektrinu medzi budovami. Aký režim (energetické spoločenstvo, zdieľanie) a aké povolenia?"
      - "Distribútor odmietol pripojiť výrobňu 500 kW pre nedostatok kapacity. Možno sa brániť a u koho?"
description: Použij pro dodávky elektřiny, plynu a tepla, zákazníky a dodavatele, ukončení a změny smluv, připojení, licence a výrobny, FVE a OZE, podporu, komunitní energetiku a sdílení, akumulaci, teplárenství, PENB, cenovou regulaci, ERÚ a SEI, energetické transakce a spory. Právní zdroje jen nativním CODEXIS.
---

# Energetické právo ČR

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

## Oborový postup: energetika

### Komodita, role a časové vrstvy
Urči zákazníka domácnost, podnikatele či obec, výrobce, obchodníka, distributora, provozovatele lokální soustavy, společenství, developera nebo dodavatele tepla. Odděl elektřinu, plyn a teplo, vlastní spotřebu, přetok, akumulaci a agregaci. Ze smluv zjisti sdruženou službu nebo oddělenou dodávku a distribuci, typ produktu, rozhodná oznámení a regulační rok. V CODEXIS prověř energetický zákon, občanské a spotřebitelské právo, prováděcí předpisy, cenová rozhodnutí a unijní vrstvu. Nenačtené roční ceny nedoplňuj z jiné sezony ani externě.

### Dodávka, cena a ukončení
Zkoumej smluvní náležitosti, fixní a dynamickou cenu, změnu podmínek, povinnost oznámení, předání ceníku, zálohy, měření a vyúčtování. U zprostředkovatele ověř oprávnění, rozsah plné moci a smluvní ochranu. Prověř distanční a mimo provozovnu uzavřený vztah, obecní omezení, předčasné ukončení, dobu neurčitou, prolongaci a dodavatele poslední instance. U reklamace a přerušení či obnovení dodávky zjisti vlastní podmínky a termíny.

Nejprve odděl zákonné bezsankční ukončení od porušení smlouvy. Teprve v druhé větvi zkoumej platnost pokuty, zákonný strop a případnou moderaci. Ověř konkrétní spouštěč a délku práva ukončit při změně ceny; historické lhůty nejsou instrukcí pro nový případ. Prokázanou nulovou škodu, neznámou škodu a doloženou škodu drž jako rozdílné kategorie také v závěru a klientské výzvě. Neznámou škodu nepřepisuj na absenci škody. Před navržením ukončení popiš kontinuitu nové dodávky a možné riziko přerušení.

### Připojení a majetkový rámec
Prověř žádost, potřebné podklady, posouzení kapacity, smlouvu, rezervovaný příkon či výkon, podíl na nákladech, měření a termíny. U odmítnutí zjisti povinnost odůvodnění, dostupné alternativy omezení výkonu, akumulace či provozu bez přetoků a příslušný prostředek ochrany. Odděl mikrozdroj, změnu parametrů a novou výrobnu; limity výkonu nikdy nepředpokládej. Zahrň přeložky, vstup na pozemek, ochranná pásma, věcná práva, náhrady a spory o uzavření smlouvy.

### Výroba, podpora a povolování
Ověř potřebu licence a výjimky, odbornou způsobilost, vztah k výrobně, změnu držitele, registraci, revize, bezpečnost a pojištění. Soukromou FVE nepovažuj automaticky za osvobozenou od všech povolení. Prověř stavební, územní a environmentální vrstvu, EIA, zemědělskou půdu a agrivoltaiku, památky, hluk, požární podmínky, přístup k pozemku a zrychlené povolovací mechanismy.

U podpory zjisti formu, vznik nároku, rok uvedení do provozu, délku, měření, výkazy, cenové rozhodnutí, změnu vlastníka, modernizaci a záruky původu. Odděl provozní podporu, investiční dotaci a překompenzaci. Zkoumej odnětí, snížení, kontrolu přiměřenosti, solární odvod, veřejnou podporu a legitimní očekávání podle konkrétního zdroje a období. Dotaci nepovažuj za přislíbenou nebo vyplacenou bez podkladu. Historické krizové stropy, odvody či tarif posuzuj jen v jejich časové působnosti.

### Sdílení, teplo a budovy
U energetického společenství ověř přípustnou formu, členy, účel, kontrolu, registraci a pravidla výstupu. U sdílení prověř datové centrum, skupinu, alokaci, odběrná místa, územní omezení, měření, poplatky a smlouvy. U SVJ nebo obce navazuj na souhlasy, rozúčtování, veřejné zakázky, koncesi a veřejnou podporu. Právní přípustnost sdílení není důkaz jeho technického spuštění.

U tepla zkoumej smlouvu, měření, kalkulaci a věcné usměrňování ceny. Odpojení od centrálního zásobování posuzuj podle konkrétních zákonných podmínek, potřebných souhlasů a nákladů. Zahrň rozúčtování v domě, PENB, audit a posudek, energetického specialistu, energetickou koncepci, ESCO/EPC, tepelná čerpadla a související hluk či dotace.

### Pravomoc a nároky
Každý požadavek kvalifikuj samostatně: splnění smluvní povinnosti, existence, trvání či zánik vztahu, negativní určení jednotlivého dluhu, připojení, škoda nebo veřejnoprávní licence a sankce. Z úplného textu ověř rozsah pravomoci ERÚ; negativní určení pokuty nezaměňuj s určením zániku smluvního vztahu. Soudní přezkum a procesní předpis odvoď od povahy rozhodnutí, nikoli názvu orgánu.

U dohledu ERÚ a SEI prověř kontrolu, povinnosti, skutkovou podstatu, sankci, nápravu, opravný prostředek a lhůty. Podle věci zahrň ÚOHS, REMIT, manipulaci s trhem, OTE a odpovědnost za odchylku. U neoprávněného odběru ověř skutečný základ a způsob výpočtu náhrady, ne pouze paušální tvrzení dodavatele.

### Transakce a výstupy
U koupě výrobny, PPA, výkupu přetoků, údržby, EPC, pachtu a financování vytvoř mapu licence, podpory, pozemků, připojení, dotací a převoditelnosti smluv. Vymez cenu, profil dodávky, regulační změnu, záruky původu, odpovědnost, step-in, zástavy a obnovu pozemku. Ekonomické a daňové varianty opři o uvedené vstupy.

Dodej konkrétní návrh nebo smluvní znění, tabulku nárok–pramen–adresát–lhůta–důkaz, náklady řízení odděleně od energetického vyúčtování a plán nepřerušeného provozu. Všechny právní a judikatorní opory získávej výhradně nativním CODEXIS.
