---
uuid: 7dcc8498-c468-472f-b815-09073e97daa9
name: bytove-pravo-najem-svj
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Bytové právo - nájem a SVJ ČR"
    summary: "Nájem bytu a prostor sloužících podnikání, výpověď a vyklizení, nájemné a vyúčtování služeb, společenství vlastníků, bytová družstva, krátkodobé pronájmy."
    examplePrompts:
      - "Nájemce neplatí tři měsíce a v bytě bydlí i osoby, které nenahlásil. Jak dát platnou výpověď a jak rychle ho vystěhovat?"
      - "Shromáždění SVJ schválilo úvěr na zateplení a klient byl přehlasován. Může se bránit a do kdy?"
      - "Pronajímatel vrátil jistotu sníženou o 'opotřebení' bez dokladů. Jaké má nájemce nároky?"
  en:
    displayName: "Czech Housing Law - Leases and HOAs"
    summary: "Residential and commercial leases, termination and eviction, rent and service charges, owners' associations (SVJ), housing cooperatives, short-term rentals."
    examplePrompts:
      - "A tenant has not paid for three months and unregistered persons live in the flat. How to give a valid notice and evict quickly?"
      - "The owners' meeting approved a loan for insulation and my client was outvoted. Can he challenge it and by when?"
      - "The landlord returned the deposit reduced for 'wear and tear' without receipts. What claims does the tenant have?"
  sk:
    displayName: "Bytové právo - nájom a SVJ ČR"
    summary: "Nájom bytu a priestorov slúžiacich podnikaniu v ČR, výpoveď a vypratanie, nájomné a vyúčtovanie služieb, spoločenstvá vlastníkov, bytové družstvá, krátkodobé prenájmy."
    examplePrompts:
      - "Nájomca neplatí tri mesiace a v byte bývajú aj osoby, ktoré nenahlásil. Ako dať platnú výpoveď a ako rýchlo ho vysťahovať?"
      - "Zhromaždenie SVJ schválilo úver na zateplenie a klient bol prehlasovaný. Môže sa brániť a dokedy?"
      - "Prenajímateľ vrátil zábezpeku zníženú o 'opotrebenie' bez dokladov. Aké má nájomca nároky?"
description: Použij pro nájem bytu či domu, podnikatelských prostor, podnájem, pacht, ubytování a krátkodobé pronájmy; nájemné, jistotu, služby, opravy, výpovědi, přezkum a vyklizení; SVJ, prohlášení vlastníka, shromáždění, příspěvky, převody jednotek a bytová družstva. Právní rešerše pouze nativním CODEXIS.
---

# Bytové právo – nájem a SVJ ČR

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

## Oborový postup: nájemní vztahy a správa domu

### Kvalifikace, identita a čas
Nejprve určuj roli klienta a skutečný účel užívání. Rozliš nájem bytu nebo domu k bydlení, podnikatelský prostor, obecný nájem, družstevní nájem, podnájem, pacht, ubytování, výpůjčku a výprosu. Název smlouvy nestačí. Identitu bytu, jednotky, domu, podílů a stran přebírej z dodaných listin; nedoplňuj ji údaji jiné nemovitosti. Zjisti vznik vztahu, dodatky a rozhodné události. V CODEXIS ověř přechod starých nájmů a režim jednotek vymezených podle předchozí úpravy; nespojuj je automaticky do jednoho časového řezu.

### Smlouva za klientovu stranu
Ověř formu a následky její vady, předmět, stav a předání, sjednaný nebo náhradní způsob určení nájemného, služby a zálohy. Samostatně prověř dohodnuté a zákonné zvyšování nájemného, limity a postup soudu. Zkoumej přípustnost a vzájemnou vazbu jistoty, smluvní pokuty, úročení, započtení a vrácení. Rozděl běžnou údržbu, drobné opravy a větší vady podle rozhodných prováděcích předpisů, nikoli podle zapamatovaných částek.

Prověř zvířata, stavební úpravy, součinnost, domácnost, oznamování změn, podnájem a energetické doklady. Při redlinu chraň konkrétní stranu v mezích ověřené kogentní ochrany; napiš celé články, nikoli jen rizikové poznámky. U podnikatelských prostor zohledni investice a odpisy, převod nájmu se závodem, změnu účelu, provoz a zákaznickou základnu. U pachtu odděl užívání od požívání výnosů.

### Výpověď a jiné skončení
U každého způsobu skončení ověř právní titul, podmínky, náležitosti, oprávněnou osobu a následky. Rozliš dohodu, dobu určitou a její možné obnovení, výpověď jednotlivých stran, změnu okolností, zánik předmětu a přechod nájmu při smrti. U výpovědi eviduj zvlášť vyhotovení, podpis, odeslání, dojití, běh výpovědní doby a zjištění vady. Známé odeslání nenahrazuje neznámé dojití.

Ověř skutečný obsah poučení, vymezení skutku a zákonného důvodu. U okamžitého ukončení zvlášť načti podmínky předchozí výzvy, možnost nápravy a důkaz doručení; na jiný režim je nepřenášej mechanicky. Každé vadě přiřaď její konkrétní právní následek a rozsah soudního přezkumu. Uplynutí lhůty k přezkumu nepovažuj bez výzkumu za zhojení všech vad; rozliš neplatnost a jednání, ke kterému se nepřihlíží. U podnikatelského nájmu samostatně prověř námitky proti výpovědi a jejich vazbu na soudní ochranu.

### Vyklizení, dluhy a služby
Zkontroluj odevzdání, stav podle protokolu, běžné opotřebení, náhradu za užívání po skončení, nájemné, služby a škodu jako odlišné položky. Prověř přípustnost započtení jistoty a zákaz nepřípustné svépomoci. Návrh na vyklizení musí přesně identifikovat objekt a osoby; petit přezkumu musí určit konkrétní výpověď. Ověř pravomoc, příslušnost, předběžnou ochranu, náklady a následný výkon včetně nakládání s věcmi.

U služeb ověř rozsah, zálohy, rozúčtovací metodu, měřidla, vyúčtování, zpřístupnění podkladů, námitky, splatnost a sankce. Ke každému úkonu zjisti vlastní lhůtu a spouštěč. Nedostatek vyúčtování nepřeváděj automaticky na univerzální výsledek; dolož, jak ovlivňuje právě uplatněný nárok.

### SVJ a družstvo
Prověř prohlášení vlastníka, společné části, změny podílů, vznik a zápis SVJ, stanovy a působnost orgánů. U shromáždění a per rollam zkoumej svolání, obsah pozvánky, podklady, formu, usnášeníschopnost a potřebnou většinu podle zákona i stanov. Neuváděj jednu pevnou svolávací dobu pro každý dům. U přehlasovaného vlastníka ověř legitimaci, důvod, čas počátku lhůty a možný návrh soudu. Zahrň příspěvky na správu, vymáhání dluhů, nucený prodej, potvrzení o dluzích při převodu, stavební úpravy, pojištění a ochranu údajů či kamery.

U bytového družstva odliš členské právo, nájem, převod podílu, účinky vůči družstvu, anuitu a financování. Prověř vyloučení, výstrahu, námitky, soudní přezkum, vypořádací podíl, delegáty a podmínky převodu jednotky do vlastnictví. Daňový a poplatkový režim podílu nezaměňuj s jednotkou.

### Krátkodobé užívání a dokončení
U krátkodobého pronájmu a Airbnb ověř smluvní kvalifikaci, souhlas, oprávnění SVJ, živnostenskou a obecní regulaci, hostovskou evidenci, daně a poplatky. Z toho, že jde o krátký pobyt, nevyvozuj bez analýzy všechny právní následky.

Dodej nejbližší úkon a ověřenou lhůtu, kvalifikaci, mapu nároků a důkazů, použitelné smluvní nebo procesní znění a alternativy dohody či splátek. Pokud je požadována praxe konkrétního senátu, vyhledej v CODEXIS jeho srovnatelná rozhodnutí a odděl od obecné judikatury soudu. Každou neověřenou identitu či datum označ k doplnění.
