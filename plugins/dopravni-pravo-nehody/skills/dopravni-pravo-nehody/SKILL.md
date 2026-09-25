---
uuid: 95b3ce6d-ee08-44bc-82fc-e43edd6308b9
name: dopravni-pravo-nehody
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dopravní právo a nehody ČR"
    summary: "Odpovědnost a náhrada újmy z dopravní nehody, pojistné plnění z povinného ručení, dopravní přestupky a bodový systém, zadržení řidičského průkazu, trestné činy v dopravě, dopravci a cestující."
    examplePrompts:
      - "Klientovi do auta narazil řidič, který od nehody ujel. Kdo zaplatí škodu a jaké nároky uplatnit?"
      - "Řidiči byl zadržen řidičský průkaz po naměření 1,2 promile. Co mu hrozí a jak postupovat v prvních dnech?"
      - "Pojišťovna viníka krátí náhradu za opravu o amortizaci a odmítá náhradní vozidlo. Je to v souladu s judikaturou?"
  en:
    displayName: "Czech Traffic Law and Accidents"
    summary: "Accident liability and compensation, motor insurance claims, traffic offences and the points system, licence suspension, traffic crimes, carriers and passengers."
    examplePrompts:
      - "A hit-and-run driver crashed into my client's car. Who pays the damage and which claims to raise?"
      - "A driver's licence was seized after a reading of 1.2 per mille. What does he face and how to proceed in the first days?"
      - "The at-fault party's insurer deducts depreciation from repair costs and refuses a replacement car. Is that consistent with case law?"
  sk:
    displayName: "Dopravné právo a nehody ČR"
    summary: "Zodpovednosť a náhrada ujmy z dopravnej nehody v ČR, poistné plnenie z povinného zmluvného poistenia, dopravné priestupky a bodový systém, zadržanie vodičského preukazu, trestné činy v doprave, dopravcovia a cestujúci."
    examplePrompts:
      - "Klientovi do auta narazil vodič, ktorý od nehody ušiel. Kto zaplatí škodu a aké nároky uplatniť?"
      - "Vodičovi bol zadržaný vodičský preukaz po nameraní 1,2 promile. Čo mu hrozí a ako postupovať v prvých dňoch?"
      - "Poisťovňa vinníka kráti náhradu za opravu o amortizáciu a odmieta náhradné vozidlo. Je to v súlade s judikatúrou?"
description: Použij pro dopravní nehody, náhradu újmy, povinné ručení a regres, dopravní přestupky a trestné činy, řidičská oprávnění a body, provoz vozidel, komunikace, taxislužbu a nákladní dopravu, CMR a práva cestujících. Právní zdroje pouze nativním CODEXIS.
---

# Dopravní právo a nehody ČR

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

## Oborový postup: dopravní události a přeprava

### Role a paralelní větve
Nejprve odděl řidiče, provozovatele, vlastníka, poškozeného, chodce, cyklistu, cestujícího, dopravce a pojistitele. Zjisti klientův cíl a skutečný stav přestupkového, trestního, pojistného a civilního řízení. Jedna událost není jeden nárok s jedinou lhůtou. V CODEXIS ověř rozhodné znění silničních, přestupkových, občanských, trestních a pojistných pravidel včetně nástupnické úpravy povinného ručení. U trestání prověř časové použití a případnou příznivější úpravu; sazby, body a limity nedoplňuj z paměti.

### Událost a důkazy
Z podkladů sestav přesný průběh nehody, datum a místo, vozidla, pojištění, zranění, okolnosti komunikace a stav zahájených řízení. Odděl měřenou rychlost či hladinu látky, odborný závěr a pouhé tvrzení. Vyžádej záznam o nehodě, policejní listiny, fotografie, svědky, dostupné záznamy, lékařské podklady a oznámení pojistiteli. U technických měření prověř potřebné ověření přístroje, obsluhu, odchylky a návaznost znaleckého posouzení.

V nativních pramenech zjisti povinnosti účastníka na místě, přivolání policie, poskytnutí pomoci, výměnu údajů, zachování důkazů a podrobení se zákonnému vyšetření. Nevyvozuj automaticky trestný čin z každého porušení. Nenavrhuj únik před kontrolou, nepravdivou identifikaci řidiče ani dodatečné zkreslení děje. Uznání viny v listině a právní odpovědnost zkoumej samostatně.

### Odpovědnost a peněžní nároky
Pro každého potenciálně odpovědného ověř vlastní titul: zvláštní povahu provozu, zaviněné jednání, užití bez souhlasu, střet provozů, závadu ve sjízdnosti nebo přepravní vztah. Zjisti liberační důvody, míru účasti, příčinnou souvislost a spoluúčast poškozeného; porušení povinnosti nepřepočítej bez odůvodnění na mechanické procento krácení.

Ke každé újmě přiřaď vlastní právní základ, období a důkaz. Rozliš opravu, obvyklou cenu, totální škodu, hodnotu zbytku, znehodnocení, odtah, náhradní vozidlo, znalecké náklady a ušlý zisk. Amortizaci a délku náhradního vozidla zkoumej podle konkrétního případu a ověřené judikatury. U zdraví odděl bolest, ztížení uplatnění, péči a léčbu, pracovní neschopnost, následnou ztrátu výdělku a důchodu, duševní útrapy, pohřeb a výživu pozůstalých. Metodiku soudu dostupnou v CODEXIS nepředstavuj jako závazný sazebník.

Při dílčím plnění ukaž základ nároku, právně odůvodněné krácení a až potom odečet skutečně přijatých peněz. Platbu jednoho subjektu nezapočítej duplicitně. Úroky, promlčení a oznámení vůči škůdci, pojistiteli a případnému garančnímu subjektu posuzuj odděleně.

### Pojištění a regres
Prověř přímý nárok, pojistnou událost, rozsah a limit krytí, výluky, šetření, splatnost, úrok a potřebnou součinnost. U nezjištěného či nepojištěného vozidla ověř podmínky garančního plnění a spoluúčasti. Odděl povinné ručení a havarijní pojištění. Regres zkoumej podle konkrétního důvodu, příčinné souvislosti, osoby a případných mezí; alkohol, nehlášení či technickou vadu nepovažuj bez načtení pravidla za univerzální regres. Zahrň nepojištěný provoz a příspěvky do garančního systému.

### Přestupky, trestní řízení a oprávnění
U přestupku určuj skutkovou podstatu, sankci, bodový následek, důkazní břemeno a promlčení. Rozliš příkaz na místě, písemný příkaz, odpor, řádné řízení, odvolání a soudní přezkum; jejich následky a rizika změny sankce ověř samostatně. U odpovědnosti provozovatele zjisti podmínky subsidiárního postupu, výzvu a skutečný pokus zjistit řidiče.

U řidičského oprávnění odliš zadržení dokladu, zákaz činnosti, záznam bodů, pozbytí a vrácení oprávnění. Prověř započtení doby, námitky proti bodům, odečty, školení, přezkoušení a zdravotní či psychologické požadavky. Profesní dopad na zaměstnání nebo živnost vycházej z klientových podkladů.

Trestně zkoumej nedbalostní újmu a usmrcení, důležitou povinnost, stav vylučující způsobilost, neposkytnutí pomoci, maření a obecné ohrožení. Odděl obhajobu od procesních práv poškozeného, adhezního nároku a zajištění. Prověř odklony a dohodu, náhradu újmy, souběh a zákaz dvojího postihu bez automatické analogie mezi větvemi.

### Doprava, vozidla a výstup
U dopravce prověř oprávnění, taxislužbu, mezinárodní dopravu, doby řízení a odpočinku, tachografy a odpovědnost řidiče i dopravce. U nákladní přepravy zjisti působnost CMR, limity, reklamace, promlčení, výluky a rozhodné právo. U letecké dopravy odliš zpoždění, zrušení, odepření nástupu, péči a mimořádné okolnosti. U vozidla zahrň převod, registraci, technickou způsobilost, leasing a ukončení provozu.

Dodej mapu řízení a nároků s adresátem, ověřenou lhůtou a důkazy. Požadovanou výzvu, obranu či petit skutečně sepiš; připoj výpočet náhrady a zvlášť náklady řízení, alternativu dohody a seznam chybějících podkladů.
