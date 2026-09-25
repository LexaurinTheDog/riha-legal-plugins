---
uuid: af51a746-5b9e-4574-936d-a76ba5055106
name: zemedelske-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Zemědělské právo ČR"
    summary: "Zemědělský pacht a jeho výpověď, pozemkové úpravy, ochrana zemědělského půdního fondu a vynětí, přímé platby SZP a podmíněnost, sankce a odvolání u dotací, LPIS a evidence zemědělského podnikatele, škody zvěří a myslivost, vodní právo a hnojiva, welfare zvířat a veterinární právo, prvovýroba potravin a prodej ze dvora, ekologické zemědělství, agrovoltaika, předání farmy a zdanění zemědělců."
    examplePrompts:
      - "Klient zdědil 12 ha orné půdy propachtované družstvu smlouvou z roku 2008 na dobu neurčitou. Chce půdu převzít a hospodařit sám. Kdy a jak vypovědět pacht a co s dotacemi na LPIS?"
      - "SZIF zkrátil klientovi přímé platby o 30 % za porušení podmíněnosti (eroze, hnojení) a vyměřil vrácení dotace za 2 roky. Jak se odvolat a jaké jsou šance u soudu?"
      - "Farmář chce na 5 ha postavit agrovoltaickou elektrárnu a vedle toho prodávat vlastní sýry a maso ze dvora. Jaká povolení, vynětí ze ZPF, veterinární a hygienické podmínky a daňové dopady?"
  en:
    displayName: "Czech Agricultural Law"
    summary: "Agricultural lease and its termination, land consolidation, protection of the agricultural land fund and land withdrawal, CAP direct payments and conditionality, subsidy sanctions and appeals, LPIS and the farm register, game damage and hunting, water and fertiliser rules, animal welfare and veterinary law, food primary production and direct sales, organic farming, agri-photovoltaics, farm succession and taxation of farmers."
    examplePrompts:
      - "My client inherited 12 ha of arable land leased to a cooperative under a 2008 open-ended contract and wants to farm it himself. When and how to terminate the lease and what about the LPIS subsidies?"
      - "The paying agency cut my client's direct payments by 30% for conditionality breaches (erosion, fertilisation) and ordered repayment for two years. How to appeal and what are the chances in court?"
      - "A farmer wants to build an agri-photovoltaic plant on 5 ha and sell his own cheese and meat from the farm. Which permits, land-fund withdrawal, veterinary and hygiene conditions and tax consequences apply?"
  sk:
    displayName: "Poľnohospodárske právo ČR"
    summary: "Poľnohospodársky nájom (pacht) a jeho výpoveď, pozemkové úpravy, ochrana poľnohospodárskeho pôdneho fondu a vyňatie, priame platby SPP a podmienenosť, sankcie a odvolania pri dotáciách, LPIS a evidencia poľnohospodárskeho podnikateľa, škody zverou a poľovníctvo, vodné právo a hnojivá, welfare zvierat a veterinárne právo, prvovýroba potravín a predaj z dvora, ekologické poľnohospodárstvo, agrovoltaika, odovzdanie farmy a zdanenie poľnohospodárov."
    examplePrompts:
      - "Klient zdedil 12 ha ornej pôdy prepachtovanej družstvu zmluvou z roku 2008 na dobu neurčitú. Chce pôdu prevziať a hospodáriť sám. Kedy a ako vypovedať pacht a čo s dotáciami na LPIS?"
      - "SZIF skrátil klientovi priame platby o 30 % za porušenie podmienenosti (erózia, hnojenie) a vymeral vrátenie dotácie za 2 roky. Ako sa odvolať a aké sú šance na súde?"
      - "Farmár chce na 5 ha postaviť agrovoltaickú elektráreň a popri tom predávať vlastné syry a mäso z dvora. Aké povolenia, vyňatie zo ZPF, veterinárne a hygienické podmienky a daňové dopady?"
description: 'Use for Czech agriculture and rural business: agricultural land and leases, farming records and subsidies, land protection and consolidation, livestock and veterinary duties, food and inputs, water, hunting damage, farm transfers and related taxes. Distinguish private title, public records, programme eligibility and operational duties. Research legal sources only through native CODEXIS in the application.'
---

# Zemědělské právo

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

### 2a. Judikatura navázaná na rozhodný paragraf (R5.1)

Tato cesta je dokumentována ve schématu nativního konektoru (`cdx-cli schema related`, parametr `part`) a byla ověřena v aplikaci 25. 9. 2026. **Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf **oba** příkazy z bodů 1 a 2. Samotný počet z `/related/counts` nic nevybírá a krok nesplňuje. Fulltextové hledání v `JD` je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Počet navázané judikatury:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related/counts?part=paragraf<N>'` (např. `paragraf198`, `paragraf19c`; `elementId` ověř přes `/toc`).
2. **Kandidáti:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related?part=paragraf<N>&type=SOUVISEJICI_JUDIKATURA&limit=20'` - řazeno podle relevance. **Spusť ho vždy dvakrát:** podle relevance a s `&sort=date` (nejnovějších 20), aby ti neunikla rozhodnutí z posledních let; další stránky `&offset=20`, `&offset=40` … Projdi alespoň prvních 20 kandidátů (titulek, `/meta`) a relevantní zařaď do výběru. Vrácená `docId` lze přímo použít v `cdx://doc/<docId>/meta` a `/text`.
3. **Skutková shoda:** doplň fulltextem `search JD` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2-5 slov). Filtr soudu používej jen s přesnými hodnotami facety: `Nejvyšší soud`, `Nejvyšší správní soud`, `Ústavní soud`, `Vrchní soud` (Praha × Olomouc přes `--city "Praha"` / `--city "Olomouc"`); jiné hodnoty ověř přes `--with-facets`. Pro novou úpravu omez stáří přes `--issued-from`.
4. **Třídění kandidátů podle `/meta`** (před načtením celého textu podle kroku 4):
   - `derogated: true` → rozhodnutí je v CODEXIS označeno jako překonané; jako oporu je nepoužij. `false` nevylučuje pozdější odklon - ten prověř podle kroku 4;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (výsledek `&sort=date` z bodu 2 a fulltext `"velký senát" <právní pojem>`). Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
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

## Oborový postup: zemědělské právo

### Klient, hospodaření a rozhodné období

Urči, zda klient je vlastník, pachtýř, dědic, zemědělský podnikatel, družstvo, obec, myslivecký subjekt nebo výrobce potravin. Z dodaných podkladů propojuj parcely, vlastnické podíly, fakticky užívané plochy, evidenci půdy, půdní bloky, kulturu, kvalitu půdy, zvířata a provozovny. Evidenční údaj nesmí nahradit soukromoprávní titul ani důkaz skutečného hospodaření.

Zaznamenej uzavření a změny smluv, výpovědi, předání půdy, sklizeň, dotační rok, víceleté závazky a kontrolní události. V CODEXIS ověř každý příslušný časový režim včetně přechodných ustanovení. Pravidlo z jiného dotačního roku ani podobně nazvaný program nepřebírej jako aktuální rozhodné právo.

### Půda, pacht a soukromá práva

Odliš pacht, nájem, výpůjčku, tolerované užívání a užívání bez titulu podle obsahu a doby vzniku. Ověř oprávnění pronajímatele či propachtovatele, souhlas spoluvlastníků, dobu, formu, předmět, úplnost příloh a předání. Pachtovní rok, splatnost pachtovného, výpovědní doba a účinky porušení jsou samostatné otázky pro rešerši, nikoli zapamatované univerzální termíny.

Při tvorbě smlouvy určuj plochy a kultury, povolené využití, cenu a naturální plnění, daňový režim, vody, přístup, podmínky péče a investic. Uprav víceleté porosty, sklizeň při skončení, vypořádání zhodnocení, rekultivaci, předání a doklady. Rozděl odpovědnost ve prospěch klienta v mezích kogentního práva; veřejnoprávní odpovědnost nelze vůči úřadu odstranit pouhým smluvním přenesením. Změnu vlastníka, úmrtí, předkupní právo či restituci neposuzuj automaticky jako zánik vztahu.

U obecních, státních nebo církevních pozemků ověř zvláštní dispoziční, schvalovací a zveřejňovací režim. U historických nebo restitučních nároků pracuj s konkrétními listinami a rozhodným právem. U hranic, přístupu, veřejné komunikace a sousedských imisí odděl soukromou a veřejnou ochranu; provoz zemědělství nemá automatickou imunitu vůči sousedům.

### Evidence půdy a podpory

Samostatně kontroluj právní titul, evidenci užívání půdy, postavení aktivního zemědělce a podmínky konkrétní podpory. Splnění jednoho neprokazuje zbývající. U dvojího deklarování, změny uživatele nebo ukončení titulu vymez důkazy, postup změny a možné dopady pro konkrétní rok; nevyvozuj bez ověření ztrátu všech podpor.

U přímých plateb, redistributivní podpory, mladého zemědělce, ekoplatby, vázané podpory, znevýhodněných oblastí, agroenvironmentálních závazků, ekologického hospodaření, welfare a investičních projektů určuj přesnou identitu programu a rozhodnou verzi. Nepřiřazuj číslo prováděcího předpisu odhadem podle podobného názvu. Ověř žádost, způsobilé plochy a zvířata, termíny, změny, odnětí žádosti, souběhy a omezení.

Podmíněnost a standardy hospodaření ověř podle příslušného období: eroze, pokryv, střídání plodin, trvalé travní porosty, voda, hnojiva, přípravky, krajinné prvky, ochrana přírody, zdraví a pohoda zvířat. Urči důkazy skutečného splnění, nikoli jen deklaraci v žádosti. U sankce prověř rozsah, závažnost, opakování, úmysl a proporcionalitu.

Rozliš administrativní kontrolu, kontrolu na místě, dálkové zjištění, protokol, námitky a rozhodnutí. U vyšší moci nebo mimořádných okolností dolož událost, příčinný vztah, oznámení a důkazy. Krácení, sankce, vrácení, úrok a trestní odpovědnost mají odlišné podmínky. Změnu hospodáře, převod podniku či úmrtí posuď i pro pokračující víceleté závazky; nepředpokládej automatické vrácení celého plnění.

### Ochrana a uspořádání krajiny

U zemědělského půdního fondu zkoumej skutečný záměr, třídu a kvalitu půdy, dočasné či trvalé odnětí, kompetenci, výjimky, odvod a rekultivaci. Výpočet založ na ověřených přílohách a údajích konkrétní parcely. U agrovoltaiky či energetického projektu samostatně řeš přípustnost stavby, zemědělské využití, energetický režim, připojení, evidenci půdy a dotace.

U pozemkových úprav rozliš obvod, účastenství, soupis nároků, ocenění, plán společných zařízení, návrh nového uspořádání a jednotlivá rozhodnutí. Ověř požadavky na souhlas, přiměřenost a námitky podle rozhodného režimu. Schválení návrhu a rozhodnutí o výměně práv nemusí mít stejné účinky ani opravné prostředky. Vztah k břemenům, zástavám, pachtu a zápisu posuď konkrétně.

U závlah, studní, odběrů, odvodnění a ochranných pásem prověř titul, povolení, poplatky, vlastnictví zařízení a omezení za sucha. U kejdy, hnoje, hnojiv a přípravků zkoumej skladování, havarijní ochranu, aplikační omezení, evidenci, odbornou způsobilost a ochranu včel. Časová okna a množstevní limity načti pro konkrétní území a období, nepřebírej je zpaměti.

### Zvířata, zvěř a potraviny

U chovu ověř registraci, označování, přesuny, záznamy, veterinární péči, léčiva, ochranné lhůty, nákazy, welfare, přepravu, porážku a nakládání s kadávery. Mimořádná opatření a náhrady nákladů nebo škody posuzuj podle konkrétní události a uplatnění. Chov pro vlastní potřebu nemusí být vyňat ze všech povinností.

U myslivosti odliš vlastníka pozemku, člena společenstva a uživatele honitby. U škody zjisti původce, porost či jiný předmět, dobu, prevenci, oznámení, vyčíslení a důkazy výnosu a ceny. Škoda zvěří a škoda vybraným chráněným živočichem mohou vyžadovat jiného adresáta a postup. Lhůtu oznámení, vyčíslení po sklizni a žaloby neztotožňuj.

U potravin odliš prvovýrobu, zpracování, přímý prodej a distribuci. Podle komodity prověř registraci či schválení, hygienu, vlastní kontrolu, označení, sledovatelnost a omezení malého množství. Zvlášť řeš krmiva, osiva, ekologickou certifikaci, chráněná označení, víno, pěstitelské pálení a dodavatelské vztahy včetně nekalých praktik. Ekologická certifikace a dotační způsobilost nejsou totožné.

### Podnik, daně a výstup

U převodu farmy porovnej převod podílů a jednotlivých aktiv, zaměstnance, dluhy, pacht, oprávnění, dotace, evidenci půdy, zvířata a dokumentaci. Zohledni dědění, rodinné vztahy, spojené osoby a družstevní či transformační souvislosti.

Daňově ověř režim půdy, pachtu, podnikání, skutečných či paušálních výdajů, provozní a investiční podpory, daně z přidané hodnoty, biologických aktiv, odpisů a relevantního vracení spotřební daně. Porovnávej čisté ekonomické varianty včetně pojištění, financování, veřejné podpory a nákladů sezónní práce a bezpečnosti. Neoznačuj automaticky každou dotaci za plnění mimo daňový režim.

Dodej požadovanou smlouvu, námitky, odvolání, žádost, vyčíslení škody nebo transakční plán. Uveď konkrétní petit či náhradní znění, podklady, lhůty, náklady, protiargumenty a oddělené soukromé, správní a dotační následky.
