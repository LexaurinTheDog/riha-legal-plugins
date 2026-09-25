---
uuid: 1b215851-806f-46bb-8852-55dd0ca229c4
name: verejne-zakazky-dotace
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Veřejné zakázky a dotace ČR"
    summary: "Režimy a druhy zadávacích řízení, námitky a návrh k ÚOHS, změny závazku, dotační podmínky, nesrovnalosti, porušení rozpočtové kázně a odvody, audity veřejného sektoru."
    examplePrompts:
      - "Obec chce rozdělit rekonstrukci školy na tři zakázky malého rozsahu. Je to přípustné a co hrozí?"
      - "Byli jsme vyloučeni ze zadávacího řízení pro nesplnění kvalifikace. Jaké lhůty běží pro námitky a návrh k ÚOHS a kolik je kauce?"
      - "Poskytovatel dotace vyměřil odvod 100 % za chybu ve výběrovém řízení dodavatele. Jak se bránit?"
  en:
    displayName: "Czech Public Procurement and Subsidies"
    summary: "Procurement regimes and procedures, objections and ÚOHS review, contract modifications, subsidy conditions, irregularities, budget discipline breaches and levies, public-sector audits."
    examplePrompts:
      - "A municipality wants to split a school reconstruction into three small-scale contracts. Is it permissible and what are the risks?"
      - "We were excluded from a tender for failing qualification. Which deadlines run for objections and the ÚOHS petition, and how much is the deposit?"
      - "The subsidy provider levied a 100 % repayment for an error in the supplier selection. How to defend?"
  sk:
    displayName: "Verejné zákazky a dotácie ČR"
    summary: "Režimy a druhy zadávacích konaní v ČR, námietky a návrh na ÚOHS, zmeny záväzku, dotačné podmienky, nezrovnalosti, porušenie rozpočtovej disciplíny a odvody, audity verejného sektora."
    examplePrompts:
      - "Obec chce rozdeliť rekonštrukciu školy na tri zákazky malého rozsahu. Je to prípustné a čo hrozí?"
      - "Boli sme vylúčení zo zadávacieho konania pre nesplnenie kvalifikácie. Aké lehoty bežia pre námietky a návrh na ÚOHS a aká je kaucia?"
      - "Poskytovateľ dotácie vyrubil odvod 100 % za chybu vo výberovom konaní dodávateľa. Ako sa brániť?"
description: 'Use for Czech public procurement and subsidies: contracting authority and supplier advice, tender preparation, evaluation, exclusions, objections and review, contract changes, grant eligibility, controls, financial corrections and recovery. Separate procurement, budget, tax, criminal and contractual consequences. Research legal sources only through native CODEXIS in the application.'
---

# Veřejné zakázky a dotace

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

## Oborový postup: veřejné zakázky a dotace

### Postavení klienta a mapa režimů

Urči klienta jako zadavatele, dodavatele, poddodavatele, poskytovatele či příjemce podpory. Vymez konkrétní zakázku nebo program, rozhodné období, fázi a požadovaný výsledek. Z dodaných podkladů sestav seznam zadávací dokumentace, vysvětlení a změn, nabídek, oznámení, rozhodnutí, smluv a doručení. U dotace odděl výzvu, žádost, rozhodnutí či smlouvu, podmínky, změny a kontrolní výstupy.

V CODEXIS prověř rozhodné právní režimy a vzájemný vztah zákona, unijní úpravy, programu a konkrétních podmínek. Přísnější formulace poskytovatele nemusí být automaticky platná nebo nadřazená zákonu. Podklad klienta zachovej jako důkaz obsahu jeho věci, ne jako nezávisle ověřený pramen aktuálního práva.

### Příprava a průběh zakázky

Jaké postavení má zadavatel a jaký druh zakázky skutečně pořizuje? Ověř předpokládanou hodnotu, funkční a časové souvislosti plnění, agregaci, dělení, sektorový či dotovaný režim, relevantní limity a výjimky. U vnitřního zadání, spolupráce veřejných zadavatelů nebo jednacího řízení bez uveřejnění dolož všechny podmínky; nepovažuj provozní pohodlí za právní důvod výjimky.

Posuď přípravnou tržní konzultaci, technické podmínky, kvalifikaci, hodnoticí kritéria, elektronickou komunikaci a přístup k dokumentaci. Zkoumej rovné zacházení, přiměřenost, transparentnost, střety zájmů a účast osob zapojených do přípravy. U vysvětlení nebo změny dokumentace ověř dopad na lhůtu a potřebné zveřejnění.

Při hodnocení odliš splnění podmínek, objasnění nabídky, zakázanou změnu a samotné hodnocení. U mimořádně nízké nabídkové ceny zachovej celý sled: identifikace pochybnosti, konkrétní žádost o vysvětlení, obsah odpovědi a posouzení důvodů. V CODEXIS rozliš povinné a možné vyloučení a ověř, na které účastníky se konkrétní pravidlo vztahuje; nezúžuj automaticky ochranu pouze na vybraného dodavatele.

U výběru, zrušení řízení a uzavření smlouvy prověř odůvodnění, oznámení, zákaz uzavření, zveřejnění a návaznost na registr smluv či jiné povinnosti. Uzavření, účinnost, zveřejnění a zaplacení nejsou stejnými událostmi.

### Změny smlouvy a přezkum

U dodatku určuj původní závazek, vyhrazenou změnu, další plnění, nepředvídatelnost, změnu dodavatele a přípustnost změny hodnoty či povahy. Jednotlivé tituly neslučuj; ověř pravidla součtu změn, jejich zdůvodnění a zveřejnění podle rozhodného znění. Přípustnost dodatku podle zadávacího práva neřeší automaticky jeho soukromoprávní účinnost.

U námitek a návrhu k přezkumnému orgánu určuj napadený úkon, okamžik vědomosti, skutečné doručení a přesný adresát. Ověř zákonné náležitosti, legitimaci, včasnost, předchozí námitky, kauci a požadované přílohy. Kauci nezaměňuj s poplatkem; samostatně řeš její výpočet, složení, případné vrácení a propadnutí.

Blokační dobu posuď podle konkrétního zahajovacího a ukončovacího důvodu. Pravomocné odmítnutí či zastavení může mít význam i uvnitř jinak uváděného časového intervalu. Následná soudní žaloba nemusí sama zákaz uzavřít smlouvu prodlužovat. Zvlášť ověř možnost a podmínky prozatímní ochrany.

Petit musí směřovat k opatření, které orgán smí přijmout: odstranění vady, zrušení příslušného úkonu či jiná zákonná náprava, nikoli automatické přikázání vybrat klienta. U soudního přezkumu samostatně ověř přípustnost, lhůtu a rozsah kontroly.

### Dotace, kontroly a vratky

Pro dotaci sestav životní cyklus od způsobilosti a žádosti přes financování, plnění ukazatelů a změny projektu až po udržitelnost. Rozliš veřejnoprávní rozhodnutí a smlouvu, státní, územní a unijní prostředky, zálohu a proplacení výdaje. Ověř způsobilost konkrétního nákladu, zákaz dvojího financování, veřejnou podporu, zakázkové povinnosti a doklady skutečného plnění.

U kontroly rozliš oprávnění jednotlivých orgánů, protokol, námitky, rozhodnutí o odvodu a navazující vymáhání. Neslučuj kontrolní zjištění s pravomocným platebním titulem. Prověř možnost opravy, dobrovolného vrácení, prominutí a jejich účinky; výzva k vrácení nemusí mít stejnou povahu jako rozhodnutí.

U porušení rozpočtové kázně, finanční opravy, odvodu, penále a trestního rizika identifikuj samostatné předpoklady. Výši neodvozuj automaticky od celé dotace; ověř proporcionalitu, rozhodné podmínky a relevantní praxi. Správní řád a daňový proces nejsou zaměnitelné, proto každému prostředku přiřaď správný režim. Samotné porušení podmínek nepovažuj bez dalších znaků za dotační podvod.

### Výstup

Dodej požadované námitky, návrh, žalobu, smluvní dodatek, vyjádření ke kontrole nebo dotační memorandum s konkrétními formulacemi. U každé vady uveď fakt, dokument, pravidlo, následek a nejsilnější protiargument. Připoj úplný časový a nákladový přehled včetně kauce, poplatků, odměny, případného odvodu a ekonomické varianty nápravy. U zadavatele či poskytovatele zachovej zákonnost a transparentnost; zájem klienta neodůvodňuje účelové obcházení soutěže.
