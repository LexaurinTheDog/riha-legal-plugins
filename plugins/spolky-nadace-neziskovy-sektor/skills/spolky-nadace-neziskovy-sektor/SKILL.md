---
uuid: 787c59aa-e879-4541-9781-67649e743f04
name: spolky-nadace-neziskovy-sektor
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Spolky, nadace a neziskový sektor ČR"
    summary: "Spolky, nadace, nadační fondy a ústavy - založení a rejstříky, vnitřní správa a spory členů, přezkum rozhodnutí orgánů, dary, veřejné sbírky, dotace, daňový režim, účetní povinnosti, zánik a odpovědnost."
    examplePrompts:
      - "Členská schůze spolku vyloučila klienta bez předchozí výzvy a bez možnosti se vyjádřit. Jak se bránit a do kdy?"
      - "Chceme založit nadační fond na podporu regionálních talentů. Co potřebujeme, kolik to stojí a jaké budou průběžné povinnosti?"
      - "Spolek přijal dar 800 000 Kč od firmy a chce jí za to dát reklamu na webu. Jaké jsou daňové dopady pro obě strany?"
  en:
    displayName: "Czech Non-profit Law"
    summary: "Associations, foundations, endowment funds and institutes - formation and registers, governance and member disputes, review of body decisions, donations, public collections, grants, tax status, accounting duties, dissolution and liability."
    examplePrompts:
      - "The general meeting of an association expelled my client without prior warning or a chance to respond. How to defend and by when?"
      - "We want to set up an endowment fund for regional talent. What is needed, what does it cost and what are the ongoing duties?"
      - "An association accepted a CZK 800,000 donation from a company and wants to give it advertising on its website. What are the tax consequences for both sides?"
  sk:
    displayName: "Spolky, nadácie a neziskový sektor ČR"
    summary: "Spolky, nadácie, nadačné fondy a ústavy v ČR - založenie a registre, vnútorná správa a spory členov, preskúmanie rozhodnutí orgánov, dary, verejné zbierky, dotácie, daňový režim, účtovné povinnosti, zánik a zodpovednosť."
    examplePrompts:
      - "Členská schôdza spolku vylúčila klienta bez predchádzajúcej výzvy a bez možnosti sa vyjadriť. Ako sa brániť a dokedy?"
      - "Chceme založiť nadačný fond na podporu regionálnych talentov. Čo potrebujeme, koľko to stojí a aké budú priebežné povinnosti?"
      - "Spolok prijal dar 800 000 Kč od firmy a chce jej za to dať reklamu na webe. Aké sú daňové dopady pre obe strany?"
description: 'Use for Czech non-profit entities and civic activity: spolek a pobočný spolek, nadace, nadační fond, ústav, o.p.s., sociální družstvo, založení, stanovy, orgány, členství a vyloučení, soudní přezkum, rejstříky, dary a veřejné sbírky, dotace, veřejně prospěšný poplatník, daně, účetnictví, dobrovolníci, odpovědnost, přeměny a likvidace. Research legal sources only through native CODEXIS in the application.'
---

# Spolky, nadace a neziskový sektor ČR

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

## Forma, klient a zdroj pravidel

Urči, zda jednáš za organizaci, zakladatele, člena, člena orgánu, dárce, příjemce podpory nebo věřitele. Zjisti právní formu, čas založení, rejstříkový stav a rozhodné stanovy, statut či nadační listinu. Odděl zákon, vnitřní předpis a individuální rozhodnutí; autonomie organizace není předpoklad neexistence soudní ochrany.

V CODEXIS ověř rozdíly mezi spolkem, pobočným spolkem, nadací, nadačním fondem, ústavem, existující obecně prospěšnou společností, sociálním družstvem, církevní osobou a obchodní společností se sociálním cílem. Název nezisková organizace neprokazuje daňové osvobození ani konkrétní právo. Starší právní formu a pokračování organizace podrob přechodným pravidlům.

### Otázky životního cyklu organizace

- Založení a vznik: jaké osoby, právní jednání, účel, název, sídlo, orgány, vklady a forma jsou vyžadovány? Prověř ustavující schůzi, schválení stanov, nadační listinu, jistinu a oddělení založení od zápisu a vzniku. Vyžádej souhlasy a podklady k sídlu, podpisům a funkci; nevytvářej neexistující schůzi nebo potvrzení.
- Vnitřní správa spolku: kdo svolává a rozhoduje, jak se určuje členství, program, doručení pozvánky, usnášeníschopnost a většina? Ověř stanovy i dispozitivnost zákona, delegáty, dílčí schůze, distanční hlasování, zápis a právo na informace. Prověř statutární, kontrolní a rozhodčí orgány, funkční období, způsob zastupování, střet zájmů a péči řádného hospodáře.
- Členství: jak vzniká, mění se a zaniká, co zakládá příspěvkovou povinnost a jak je veden seznam členů? U vyloučení načti zvláštní pravidla výzvy, vyjádření, vnitřního opravného postupu a soudní ochrany; nevydávej jej za běžné rozhodnutí orgánu bez odlišení. U pobočného spolku ověř rozsah osobnosti, stanovami určenou vazbu a konkrétní pravidla ručení.
- Soudní přezkum: kdo je legitimován, jaké rozhodnutí je napadáno, kdy se o něm dozvěděl a jaká ochrana už byla využita? Pro neplatnost, zdánlivost a jiné vady ověř vlastní důsledky a lhůty. Korektiv nevyslovení neplatnosti posuzuj podle všech kumulativních podmínek; ochranu třetích osob v dobré víře odděl. Neomezuj předběžnou ochranu majetku na doslovně uvedený prodej, může jít o jinou dispozici či výkon hlasovacích práv.
- Nadace a fondy: jaký účel, majetkový režim a orgány se použijí? Ověř nakládání s jistinou, nadační příspěvky, příjemce spojené s orgány, schvalování, vyúčtování a vrácení, přidružený fond a změnu účelu. U ústavu ověř vztah zakladatele, ředitele a rady, poskytované služby a kontrolu hospodaření; nepřenášej mechanicky spolková pravidla.
- Financování: jde o členský příspěvek, dar, reklamu, nadační příspěvek, dotaci, veřejnou sbírku či ekonomickou činnost? Rozhoduje obsah a protiplnění, ne pouze název smlouvy. U smíšených plnění odděl části a podmínky použití; vyčísli dopad pro obě strany. Ověř crowdfunding, bezhotovostní sbírku, dárcovské zprávy, oznámení, evidenci, vyúčtování a sankce podle rozhodného režimu.
- Dotace a dobrovolnictví: ověř poskytovatele, titul, program a podmínky, nárokovost, veřejnoprávní smlouvu, změny účelu a rozpočtovou kázeň. Prověř akreditaci, dobrovolnickou smlouvu, náklady, pojištění, bezpečnost a postavení osob. U sociálních služeb doplň registraci, smluvní režim a financování.
- Daně a účetnictví: splňuje osoba znaky veřejně prospěšného poplatníka a není ve výluce? Odděl hlavní a vedlejší činnost, příjmy mimo předmět, osvobozené a zdanitelné příjmy. Ověř účelové dary, odpočet dárce, reklamu, DPH, ekonomickou činnost, registraci a přiznání. Zjisti podmínky účetního režimu, auditu, výroční zprávy a ukládání listin. Nepředpokládej existenci zapisovatelného statusu pouze podle názvu institutu.
- Odpovědnost: jaká povinnost byla porušena a komu vznikla újma? Posuď orgány, zaměstnance i právnickou osobu, odměnu za funkci, pojištění a možnou trestní přičitatelnost. Zpronevěru, dotační podvod nebo porušení správy cizího majetku neposuzuj jen z hospodářského neúspěchu.
- Změny a zánik: ověř změnu stanov, právní formy, fúzi, rozdělení, ochranu členů a věřitelů, zrušení dobrovolné či soudní, likvidaci, použití zůstatku a výmaz. Přetrvávající závazky a dotační podmínky mohou změnit vhodnost zvolené varianty.

### Povinný výstup

V CODEXIS vyhledej přiléhavou judikaturu k autonomii, ochraně člena, výkladu stanov, příspěvkům, hospodaření a daním. Výstup spoj s konkrétními listinami organizace a odliš údaj účastníka od doloženého faktu. Dodej požadované stanovy, usnesení, smluvní články či návrh soudu, nejen návod k jejich sepsání.

Závěr obsahuje postup, správný orgán, právní základ ze zákona a stanov, doložený počátek a konec lhůty, petit a důkazy. Náklady rejstříkového úkonu a sporného přezkumu počítej odděleně: osvobození v jednom typu řízení neprokazuje osvobození ve druhém. Uveď ekonomický a daňový dopad, souhlasy a otevřené dokumentační mezery.
