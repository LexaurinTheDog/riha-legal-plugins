---
uuid: 780180e9-2aca-4484-b30a-6e8c2bd28510
name: startupy-investice-esop
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Startupy, investice a ESOP ČR"
    summary: "Založení a cap table, zakladatelské dohody a vesting, konvertibilní zápůjčky a SAFE, seed a VC kola s akcionářskou dohodou, likvidační preference, anti-dilution a drag/tag, zaměstnanecké akcie a opční plány včetně českého daňového odkladu, převod IP a zaměstnanecká díla, zákaz konkurence a mlčenlivost, dotace a odpočet na výzkum, crowdfunding a limity veřejné nabídky, exit a zdanění zakladatelů."
    examplePrompts:
      - "Tři zakladatelé s.r.o. chtějí nastavit vesting 4 roky s 1 rokem cliff, ochranu při odchodu „bad leaver“ a přípravu na seed kolo. Jak to strukturovat v české s.r.o. a co dát do společenské smlouvy versus akcionářské dohody?"
      - "Angel investor nabízí konvertibilní zápůjčku 5 mil. Kč s 20% slevou a cap 60 mil. Kč. Zreviduj term sheet, navrhni mechanismus konverze v s.r.o. a daňové dopady pro obě strany."
      - "Klient chce zavést ESOP pro 15 zaměstnanců v s.r.o. Jaké jsou varianty (opce na podíl, phantom, nová třída podílu), jak funguje daňový odklad od 2024/2025 a co musí zaměstnavatel oznámit?"
  en:
    displayName: "Czech Startups, Investments & ESOP"
    summary: "Founding and cap table, founders' agreements and vesting, convertible loans and SAFE-type instruments, seed and VC rounds with shareholders' agreements, liquidation preference, anti-dilution and drag/tag, employee share and option plans including Czech tax deferral, IP assignment and employee works, non-compete and confidentiality, grants and R&D deductions, crowdfunding and public-offer limits, exits and founder taxation."
    examplePrompts:
      - "Three founders of an s.r.o. want 4-year vesting with a 1-year cliff, bad-leaver protection and preparation for a seed round. How to structure it in a Czech s.r.o. and what belongs in the articles versus the shareholders' agreement?"
      - "An angel offers a CZK 5m convertible loan with a 20% discount and a CZK 60m cap. Review the term sheet, propose the conversion mechanics in an s.r.o. and the tax consequences for both sides."
      - "My client wants an ESOP for 15 employees in an s.r.o. What are the options (share options, phantom shares, a new share class), how does the 2024/2025 tax deferral work and what must the employer notify?"
  sk:
    displayName: "Startupy, investície a ESOP ČR"
    summary: "Založenie a cap table, zakladateľské dohody a vesting, konvertibilné pôžičky a SAFE, seed a VC kolá s akcionárskou dohodou, likvidačná preferencia, anti-dilution a drag/tag, zamestnanecké akcie a opčné plány vrátane českého daňového odkladu, prevod IP a zamestnanecké diela, zákaz konkurencie a mlčanlivosť, dotácie a odpočet na výskum, crowdfunding a limity verejnej ponuky, exit a zdanenie zakladateľov."
    examplePrompts:
      - "Traja zakladatelia s.r.o. chcú nastaviť vesting 4 roky s 1 rokom cliff, ochranu pri odchode „bad leaver“ a prípravu na seed kolo. Ako to štruktúrovať v českej s.r.o. a čo dať do spoločenskej zmluvy versus akcionárskej dohody?"
      - "Angel investor ponúka konvertibilnú pôžičku 5 mil. Kč s 20% zľavou a cap 60 mil. Kč. Zreviduj term sheet, navrhni mechanizmus konverzie v s.r.o. a daňové dopady pre obe strany."
      - "Klient chce zaviesť ESOP pre 15 zamestnancov v s.r.o. Aké sú varianty (opcia na podiel, phantom, nová trieda podielu), ako funguje daňový odklad od 2024/2025 a čo musí zamestnávateľ oznámiť?"
description: 'Use for Czech startups, founders, venture investors and employee equity: formation, cap table, founder agreements, vesting/leavers, convertible loans, SAFE, term sheets, SHA, preferences, anti-dilution, drag/tag, vetoes, equity rounds, ESOP, qualified options and phantom shares, IP chain, employee/contractor roles, tax and social insurance, R&D, subsidies, crowdfunding and exit. Coordinate general corporate, M&A, capital-market and IT specialties. Research legal sources only through native CODEXIS in the application.'
---

# Startupy, investice a ESOP ČR

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

## Klient, kapitál a proveditelnost

Urči, zda zastupuješ zakladatele, společnost, investora, zaměstnance nebo akcelerátor. Zjisti fázi financování, právní formu a jurisdikci, současné podíly, práva, zápůjčky, opce, fond a vyjednané podmínky. Čti společenskou smlouvu, dohodu společníků, investiční listiny, IP smlouvy, pracovní vztahy a dotační závazky jako propojený celek.

Anglický název nástroje není právní mechanismus. V CODEXIS ověř, která práva lze založit společenskou smlouvou, smluvním závazkem, převodem, zvýšením kapitálu nebo jiným institutem; odděl účinky vůči společnosti, smluvním stranám a nabyvatelům. Zahraniční vzor nepoužívej jako důkaz české vymahatelnosti.

### Zakladatelé a investiční kolo

- Jaké výhody, formální požadavky, náklady a omezení má zvolená forma? Ověř druhy podílů a akcií, hlasovací a majetková práva, převoditelnost, listinnou reprezentaci, přednostní práva, příplatky, vlastní podíly a dědění. Jmenování a odvolání orgánů, informační práva, hlasování mimo zasedání, souhlasy dotčených osob a střet zájmů promítni do skutečných listin.
- Jak funguje závazek zakladatele pracovat, vesting, cliff, akcelerace a good/bad leaver? Definuj spouštěč, oprávněného, předmět, cenu a určení ceny, čas, postup převodu a prostředek vynucení. Prověř souhlasy, plnou moc, smlouvu budoucí, sankce, dobré mravy a kogentní ochranu; „propadnutí podílu“ bez mechanismu neprezentuj jako hotové řešení.
- U konvertibilní zápůjčky odděl poskytnutí, jistinu, úrok, splatnost a vznik práva či povinnosti konverze. Jak funguje kvalifikované kolo, diskont, cap, MFN, splatnost bez kola a exit? Ověř převzetí vkladové povinnosti, schválení, započtení, přednostní právo, ocenění a rejstříkový účinek; jednostranné započtení, smluvní započtení a nepeněžitý vklad jsou různé varianty k právnímu posouzení.
- SAFE posuď podle obsahu: jde o závazek, zálohu, budoucí smlouvu či jinou konstrukci? Vyřeš okamžik a způsob nabytí, určitost ceny, selhání kola, vrácení a insolvenční postavení. Nepředpokládej automatické vydání podílu pouze na základě podpisu.
- U term sheetu odděl závazná ustanovení od vyjednávacích záměrů, exkluzivitu, důvěrnost a předsmluvní odpovědnost. Pro investiční kolo řeš předinvestiční a poinvestiční valuaci, option pool, likvidační preference, přednost, anti-dilution, drag/tag, předkupní práva, vetovací záležitosti, pozorovatele, deadlock a exit. Anti-dilution potřebuje konkrétní korporátní či převodní kroky; smluvní waterfall při exitu není automaticky totožný s likvidačním zůstatkem.
- Zobraz cap table před poolem, plně zředěnou tabulku po poolu před investicí a po investici. Uveď jmenovatel, zdroj každé položky a kontrolní součet; neznámé opce nevkládej jako nulové. Waterfall odděl od skutečných proceeds konkrétního zakladatele.

### ESOP, daně a lidé

Porovnej skutečný podíl, opci, novou třídu, akcie společnosti a phantom či virtuální plnění. Jak se plán schvaluje, kdo poskytuje podíl nebo peníze, jak vzniká grant, vesting, exercise, expirace a vypořádání při odchodu či exitu? Otestuj celou časovou osu; good-leaver okno nesmí bez vysvětlení skončit před nejčasnějším přípustným exercise.

V CODEXIS ověř standardní zaměstnanecký benefit, jeho případný odklad a samostatný režim kvalifikované opce. U kvalifikované větve odděl diskont oproti grantové hodnotě od případného kvalifikovaného růstu. Pro každou větev zjisti podmínky, ocenění, okamžik příjmu, oznámení, ukončení odkladu, výjimky, maximální dobu a pojistné. Nepřebírej žádnou historickou délku odkladu či limit osvobození. Srážky z peněžní mzdy, nepeněžní plnění, náklad zaměstnavatele a pozdější prodej posuzuj odděleně.

Prověř zaměstnance, jednatele, zakladatele a kontraktora podle skutečného vztahu, nikoli jediné nálepky. U práce na dálku a cizinců řeš pobyt, oprávnění, pojistnou koordinaci a daňové smlouvy. Konkurenční doložku, mlčenlivost a odměnu funkcionáře posuď v příslušném režimu.

### IP, podpora a transakční kontrola

Vytvoř řetězec autor, čas vytvoření, smluvní vztah, právo vykonávané společností a chybějící souhlas. V CODEXIS ověř zaměstnanecká a objednaná díla včetně zvláštního režimu software a databází, činnost orgánu společnosti, licence, průmyslová práva a odměnu původce. Nepředpokládej, že každý zakladatel je zaměstnanec, ani opačný univerzální výsledek. Rozliš převoditelná práva a licenci. Prověř open source, sublicence, agentury, cizí práva, AI výstupy, data, obchodní tajemství, známky a domény; nápravu neantedatuj.

U financování zkontroluj veřejnou nabídku, crowdfunding, fond či syndikát, tokeny, sankce, prověřování investic a AML. Regulaci produktu, ochranu spotřebitele a údajů vyhodnoť podle skutečné činnosti. U dotací a VaV ověř způsobilé náklady, okamžiky dokumentace a oznámení, podnikové vazby a status malého podniku, kumulaci podpory, udržitelnost a změnu vlastníka. Daňovou ztrátu, úroky, spojené osoby, holding a prodej podílu posuď zvlášť podle rozhodného roku.

Dodej požadované úplné klauzule, plán nebo transakční dokumenty s tabulkou souhlasů, plateb, podpisů a zápisů. Osobní warranties přiřaď konkrétnímu povinnému a jeho skutečným příjmům, odůvodni ekonomickou zátěž a ověř kogentní výjimky. Závěr obsahuje klientské varianty, protiargumenty, mezery, realizační lhůty a náklady; právní rešerše ani tento profil nejsou investičním doporučením.
