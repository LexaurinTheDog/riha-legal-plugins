---
uuid: 2615c2b4-1f93-4647-a845-157740ee62ba
name: dedicke-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dědické právo ČR"
    summary: "Závěť a dědická smlouva, nepominutelní dědici, vydědění, odmítnutí a výhrada soupisu, dluhy zůstavitele, pozůstalostní řízení u notáře, spory, plánování majetku."
    examplePrompts:
      - "Zemřel otec, zanechal závěť jen ve prospěch družky a dluhy z podnikání. Co mají děti udělat a do kdy?"
      - "Připrav alografní závěť s vyděděním syna pro trvalé neprojevování zájmu - jaké jsou náležitosti a rizika?"
      - "Notář odkázal klienta k žalobě o dědické právo. Jak formulovat petit a jaká běží lhůta?"
  en:
    displayName: "Czech Inheritance Law"
    summary: "Wills and inheritance contracts, forced heirs, disinheritance, renunciation and inventory reservation, estate debts, probate before the notary, disputes, estate planning."
    examplePrompts:
      - "A father died leaving a will only in favour of his partner and business debts. What should the children do and by when?"
      - "Draft a witnessed will disinheriting a son for persistent lack of interest - requirements and risks?"
      - "The notary referred my client to file an action on the right of inheritance. How to phrase the claim and what deadline runs?"
  sk:
    displayName: "Dedičské právo ČR"
    summary: "Závet a dedičská zmluva, neopomenuteľní dedičia, vydedenie, odmietnutie a výhrada súpisu, dlhy poručiteľa, dedičské konanie u notára v ČR, spory, plánovanie majetku."
    examplePrompts:
      - "Zomrel otec, zanechal závet len v prospech družky a dlhy z podnikania. Čo majú deti urobiť a dokedy?"
      - "Priprav alografný závet s vydedením syna pre trvalé neprejavovanie záujmu - aké sú náležitosti a riziká?"
      - "Notár odkázal klienta na žalobu o dedičské právo. Ako formulovať petit a aká lehota beží?"
description: 'Použij pro české dědictví a pozůstalost: závěti, dědické smlouvy, odkazy, zákonná posloupnost, nepominutelní dědici, povinný díl, vydědění, nezpůsobilost, odmítnutí a soupis, dluhy, SJM, notářské řízení, dědické spory, likvidace, správa, přeshraniční dědictví a plánování pro případ smrti. Právní zdroje jen nativním CODEXIS.'
---

# Dědické právo ČR

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

## Oborový postup: dědictví a pozůstalost

### Právo, osoba a rozhodný okamžik
Z podkladů určuj zůstavitele, klientovu roli, datum úmrtí, obvyklý pobyt, občanství, rodinné vztahy, majetek a dluhy v jednotlivých státech. Odděl plánování za života od probíhajícího pozůstalostního řízení nebo následného sporu. V nativním CODEXIS ověř rozhodné právo a pravomoc podle použitelného unijního rámce, mezinárodní smlouvy a vnitrostátního kolizního práva. Zkoumej případnou volbu práva, územní a časovou působnost a evropské dědické osvědčení. Nezaměňuj bydliště v dokladu za prokázaný obvyklý pobyt.

U každé otázky odliš datum pořízení listiny, její změny a smrti. Načti přechodná ustanovení pro pořizovací způsobilost, formu i dědění; nepoužívej jediný nový režim automaticky na staré závěti. Identitu listiny, notáře, soudu a spisu přebírej pouze z doložených údajů.

### Tituly a osoby
Sestav soupis všech pořízení a zjisti jejich vztah: dědická smlouva, závěť, dovětek, odkaz, náhradnictví a svěřenské nástupnictví. Ověř rozsah případného odvolání nebo rozporu mezi pořízeními a zbytek zákonné posloupnosti. U listiny prověř formu, vlastní rukopis či podpis, současnou přítomnost a způsobilost svědků, notářskou formu, úlevy, určitost, podmínky a příkazy. Závěr o neplatnosti přiřaď konkrétní vadě a rozsahu; nevyslovuj jej automaticky pro celou závěť.

Pro zákonné dědění načti úplné podmínky příslušné třídy, reprezentace a soužití. U nepominutelného dědice prověř osobní status, věk, povinný díl a způsob jeho uplatnění. Zvlášť zkoumej vydědění, neuvedený důvod, opomenutí, dědickou nezpůsobilost a případné prominutí. U tvrzení o nezájmu či nevhodném chování zachovej vzájemné příčiny a důkazy, nikoli jen jednostranný příběh.

### Rozhodnutí dědice a ochrana před dluhy
Rozliš zřeknutí za života zůstavitele, odmítnutí dědictví a vzdání se ve prospěch jiného dědice. Ověř přípustnost, formu, poučení, lhůtu, počátek a možné prodloužení i význam pobytu v zahraničí. Prověř, zda předchozí nakládání s majetkem ovlivňuje možnost volby. Neodvozuj přijetí nebo zánik oprávnění pouze z neurčitého popisu návštěvy bytu.

U výhrady soupisu načti podmínky, prohlášení, lhůtu, zákonnou ochranu a následky porušení. Odděl hodnotu nabytého majetku, rozsah odpovědnosti a způsob uspokojení věřitelů. Zjisti dluhy zůstavitele, náklady pohřbu, zajištění, solidaritu a případné svolání věřitelů. Neznámá pasiva nejsou nulová; srovnej postup u předlužené pozůstalosti, likvidace a insolvenčních souvislostí.

### SJM, zvláštní majetek a započtení
Prověř vypořádání SJM a vlastnictví jednotlivých aktiv před sestavením pozůstalosti. U podílu ve společnosti či družstvu načti zakladatelské dokumenty z podkladů a ověř zákonnou možnost omezení přechodu, vypořádací podíl a kontinuitu správy. Zahrň autorská práva, bankovní účty, pojištění s obmyšleným a zahraniční majetek.

Započtení daru, určení povinného dílu a samostatné peněžité plnění posuzuj zvlášť. Účetní korekce podílů sama neprokazuje existenci vykonatelné platební povinnosti. Výpočty založ na ověřených hodnotách, rozhodném okamžiku ocenění a právních pravidlech; ukaž mezivýsledky a sporné vstupy.

### Řízení, spory a nezletilí
Přečti skutečná procesní rozhodnutí: zahájení, předběžné šetření, poučení, soupis, odkaz k žalobě a konečné usnesení. Zjisti pověření soudního komisaře, účastenství, sporná aktiva či pasiva a rozsah pravomocného výroku. Než doporučíš další žalobu, určuj, zda výrok ukládá vydání majetku, potvrzuje dědictví nebo ponechává spor mimo řízení.

U odkazu k žalobě ověř žalobce, žalované, přesný předmět, důkazní břemeno a určenou lhůtu; návrh nesmí minout soudem vymezený spor. Zahrň dohodu dědiců, její schválení, odvolání, dodatečné projednání a likvidaci. U nezletilého zjisti skutečného zástupce, střet zájmů, potřebu opatrovníka a schválení konkrétního jednání; příbuzenství ani pravomoc zástupce nedovozuj z role v příběhu. Náklady řízení, odměnu komisaře, poplatky a náhradu zastoupení vypočti odděleně podle rozhodné úpravy.

### Plánování a výstup
Porovnej závěť, dědickou smlouvu, darování pro případ smrti, svěřenský fond a pojištění podle klientova cíle, odvolatelnosti, povinného dílu, správy, daní a odpovědnosti. Ověř přípustný rozsah dispozice a potřebnou formu. Navrhni vykonavatele a správce, náhradní řešení a návaznost podnikání. Draft nenazývej platným notářským pořízením, dokud nebyla splněna forma.

Dodej prioritu a nejbližší lhůtu, mapu titulů a dědiců, varianty ochrany před dluhy, procesní nebo smluvní text a seznam chybějících podkladů. Zahrň následné zápisy, oznámení a daňové otázky jako kroky k provedení, nikoli jako již dokončené. Veškerou právní oporu a relevantní judikaturu čerpej pouze z CODEXIS.
