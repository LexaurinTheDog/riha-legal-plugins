---
uuid: fae0824e-fc7a-47b3-a8db-fda0bbe4aff2
name: spotrebitelske-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Spotřebitelské právo ČR"
    summary: "Spotřebitelské smlouvy a e-shopy, odstoupení, vady a reklamace, zakázaná ujednání a nekalé praktiky, spotřebitelský úvěr, mimosoudní řešení a hromadné řízení, compliance obchodníka."
    examplePrompts:
      - "E-shop odmítá vrátit peníze za zboží vrácené 13. den s tím, že bylo rozbalené. Má spotřebitel nárok?"
      - "Klient podepsal na prezentační akci smlouvu o úvěru na 150 000 Kč bez posouzení příjmů. Jak z toho ven?"
      - "Zreviduj obchodní podmínky e-shopu z pohledu spotřebitelského práva a ČOI."
  en:
    displayName: "Czech Consumer Law"
    summary: "Consumer contracts and e-commerce, withdrawal, defects and complaints, unfair terms and practices, consumer credit, ADR and collective redress, trader compliance."
    examplePrompts:
      - "An e-shop refuses to refund goods returned on day 13 because the package was opened. Is the consumer entitled to a refund?"
      - "My client signed a CZK 150,000 credit agreement at a sales event without any income assessment. How to get out of it?"
      - "Review an e-shop's terms and conditions from the consumer-law and ČOI perspective."
  sk:
    displayName: "Spotrebiteľské právo ČR"
    summary: "Spotrebiteľské zmluvy a e-shopy v ČR, odstúpenie, vady a reklamácie, zakázané dojednania a nekalé praktiky, spotrebiteľský úver, mimosúdne riešenie a hromadné konanie, compliance obchodníka."
    examplePrompts:
      - "E-shop odmieta vrátiť peniaze za tovar vrátený 13. deň s tým, že bol rozbalený. Má spotrebiteľ nárok?"
      - "Klient podpísal na prezentačnej akcii zmluvu o úvere na 150 000 Kč bez posúdenia príjmov. Ako z toho von?"
      - "Zreviduj obchodné podmienky e-shopu z pohľadu spotrebiteľského práva a ČOI."
description: 'Use for Czech consumer rights or trader compliance: consumer status and mixed purpose, distance/off-premises contracts, pre-contract information, withdrawal, returns, defects and guarantees, abusive terms, unfair practices, prices and reviews, consumer credit, ADR and financial arbitrator, collective litigation, travel, transport, energy, telecoms, digital content and cross-border jurisdiction. Research legal sources only through native CODEXIS in the application.'
---

# Spotřebitelské právo ČR

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

## Klient, smlouva a obchodní kanál

Urči, zda chráníš spotřebitele, obchodníka nebo jiného účastníka. Ověř skutečný účel nákupu; uvedení identifikačního čísla ani smíšený účel samy neřeší kvalifikaci. Zjisti kanál uzavření, nabídku, objednávku, potvrzení, převzetí, poučení, vady, reklamace, odstoupení a platby. Datum smlouvy není automaticky rozhodným datem každé procesní či sankční otázky.

V CODEXIS načti rozhodné znění občanských, spotřebitelských a sektorových pravidel, jejich přechody a relevantní unijní úpravu. Nikdy nevycházej z historických délek lhůt, předpokladů „záruky“ či připravených sankčních zkratek.

### Mapa rešerše

- Jaké postavení mají strany a jaký je režim smlouvy v provozovně, na dálku, mimo obchodní prostory nebo u finančních služeb? Ověř informační povinnosti, povinné potvrzení, trvalý nosič, telefonickou kontraktaci a závaznost objednávky. U online tržiště odliš provozovatele od skutečného prodejce.
- Pro každou chybějící informaci zkoumej vlastní následek. Vytvoř oddělené řádky pro poučení o odstoupení, náklady vrácení, odpovědnost za snížení hodnoty, dodatečné poplatky a vrácení ceny. Porušení jedné povinnosti automaticky nepřenášej na ostatní; ověř vliv pozdějšího poučení.
- Odstoupení bez důvodu: jaká je délka a počátek lhůty pro zboží, dílčí zásilky, služby nebo digitální plnění? Co musí být odesláno či doručeno a jak se to prokazuje? Ověř povinnost vrácení, možnost zadržet refundaci, způsob platby, náklady přepravy a zacházení se zbožím. Výjimky u zakázkové výroby, hygienického obalu, digitálního plnění, ubytování či termínové služby posuď podle všech podmínek, ne názvu produktu.
- Vady: jaké subjektivní a objektivní vlastnosti, aktualizace a soulad byly sjednány či vyžadovány? Odděl dobu uplatnění, domněnku existence vady, včasné oznámení, dobrovolnou záruku a promlčení. Ověř pořadí opravy, výměny, slevy a odstoupení, význam opakování a podstatnosti, použitou věc i náklady reklamace. Prověř, co je skutečným vyřízením reklamace, doklady, komunikaci a následek marného uplynutí rozhodné lhůty.
- Zneužívající ujednání: ověř transparentnost, nerovnováhu, kogentní ochranu, režim nepřihlížení a kontrolu soudem z úřední povinnosti. Prorogaci a arbitráž posuzuj samostatně podle druhu a data smlouvy; nepředpokládej univerzální domácí soud jen z označení spotřebitel.
- Nekalé praktiky: rozliš klamání, opomenutí, agresivní jednání a konkrétní zakázanou praktiku. Prověř slevy, referenční cenu, recenze, personalizaci a manipulační návrh rozhraní. Soukromoprávní nárok, podnět dozoru, sankce a nekalá soutěž nejsou totožné prostředky.
- Úvěr: ověř rozsah zákona, poskytovatele, zprostředkovatele, úvěruschopnost a skutečně zjištěné údaje. Načti zvlášť podmínky a následky vad informací, nákladových údajů, posouzení úvěruschopnosti, zajištění a sankcí; nepropojuj je do jedné předem určené neplatnosti či úrokové sazby. Posuď odstoupení, předčasné splacení, prodlení a pravomoc finančního arbitra.
- Proces: který subjekt ADR, regulátor, arbitr či soud může poskytnout požadované plnění? Ověř podmínky, legitimaci, náklady, lhůty a účinky řízení, kolektivní ochranu a vztah k individuálnímu nároku. Dostupnost či ukončení staré platformy dolož, nenabízej ji z historické šablony. U přeshraniční věci ověř rozhodné právo a fórum odděleně.
- Zvláštní sektory: zájezd odliš od jednotlivých služeb, prověř změny ceny, pomoc a insolvenční ochranu; u letecké dopravy kompenzaci, mimořádné okolnosti a rozhodné promlčení. U energií a telekomunikací řeš změnu dodavatele, dobu závazku, prolongaci, výpověď a regulátora. U timeshare, finančních služeb na dálku a digitálního obsahu zkoumej vlastní informační a ukončovací režim.
- Compliance obchodníka: projdi obchodní podmínky, produktové informace, cenu, objednávkovou cestu, poučení, formulář, reklamace, ADR, cookies, obchodní sdělení a ochranu údajů. Právně přípustné omezení odpovědnosti nesmí popřít kogentní spotřebitelskou ochranu.

### Judikatura a dokončení

V CODEXIS vytěž přiléhavé rozhodnutí SDEU, domácích soudů a případně ústavní ochranu slabší strany. Ověř celý nosný text, zda soud přebírá nebo odmítá argument účastníka, časovou úpravu a skutkové odlišnosti. Přesná spisová značka bez správného právního závěru nestačí.

Lhůty spočítej od doložené události s ověřenými pravidly posledního dne; odstoupení bez důvodu a práva z vady vedou samostatné časové osy. Dodej požadovanou výzvu, podání nebo konkrétní náhradní smluvní články za klienta. U peněžních nároků odděl jistinu, vrácení ceny, náklady, snížení hodnoty a příslušenství, pro petit zvol správný vztah mezi nároky. Závěr obsahuje nejsilnější protiargument, důkazní mezeru, ekonomickou variantu řešení a rozpočet správného řízení.
