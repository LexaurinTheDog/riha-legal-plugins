---
uuid: ef96515c-43b1-4370-b1ee-9820b322a61c
name: trestni-pravo-hospodarske
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Hospodářské trestní právo ČR"
    summary: "Podvod, úvěrový a dotační podvod, zpronevěra, porušení povinnosti při správě cizího majetku, úpadkové a věřitelské delikty, zkrácení daně a účinná lítost, korupce a zakázkové delikty, legalizace, trestní odpovědnost právnických osob a compliance obhajoba, zajištění majetku, strategie obhajoby a spolupráce s orgány."
    examplePrompts:
      - "Jednatel klienta je obviněn ze zkrácení daně za DPH z řetězce dodavatelů. Jaká je obhajoba na subjektivní stránce a je ještě možná účinná lítost?"
      - "Policie zajistila firmě účty a nemovitost jako výnos z trestné činnosti. Jaké jsou lhůty a možnosti zrušení nebo omezení zajištění?"
      - "Společnost dostala výzvu jako obviněná právnická osoba za dotační podvod zaměstnance. Jak uplatnit vyvinění podle § 8 odst. 5 TOPO a co doložit?"
  en:
    displayName: "Czech Economic Crime & White-Collar Defence"
    summary: "Fraud, credit and subsidy fraud, embezzlement, breach of fiduciary duty, insolvency and creditor offences, tax evasion and effective repentance, corruption and procurement crimes, money laundering, corporate criminal liability and compliance defence, asset seizure, defence strategy and cooperation with authorities."
    examplePrompts:
      - "My client's managing director is charged with VAT evasion arising from a supplier chain. What is the defence on mens rea and is effective repentance still available?"
      - "The police froze the company's accounts and a property as proceeds of crime. What are the deadlines and options to lift or narrow the freeze?"
      - "The company was summoned as an accused legal person for an employee's subsidy fraud. How to invoke the exculpation under § 8(5) of the corporate liability act and what to document?"
  sk:
    displayName: "Hospodárske trestné právo ČR"
    summary: "Podvod, úverový a dotačný podvod, sprenevera, porušenie povinnosti pri správe cudzieho majetku, úpadkové a veriteľské delikty, skrátenie dane a účinná ľútosť, korupcia a zákazkové delikty, legalizácia, trestná zodpovednosť právnických osôb a compliance obhajoba, zaistenie majetku, stratégia obhajoby a spolupráca s orgánmi."
    examplePrompts:
      - "Konateľ klienta je obvinený zo skrátenia dane za DPH z reťazca dodávateľov. Aká je obhajoba na subjektívnej stránke a je ešte možná účinná ľútosť?"
      - "Polícia zaistila firme účty a nehnuteľnosť ako výnos z trestnej činnosti. Aké sú lehoty a možnosti zrušenia alebo obmedzenia zaistenia?"
      - "Spoločnosť dostala výzvu ako obvinená právnická osoba za dotačný podvod zamestnanca. Ako uplatniť vyvinenie podľa § 8 ods. 5 TOPO a čo doložiť?"
description: Use for Czech business and economic crime, directors and corporate defendants, fraud, tax and subsidy offences, creditor and insolvency offences, bribery, procurement, money laundering, accounting, compliance, asset seizure and negotiated outcomes. Distinguish criminal issues from connected civil, tax and administrative exposure. Research legal sources only through native CODEXIS in the application.
---

# Hospodářské trestní právo

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

## Oborový postup: hospodářská kriminalita

### Osoby, transakce a čas

Urči klientovu skutečnou roli: jednatel, člen orgánu, vlastník, zaměstnanec, účetní, poradce, právnická osoba, poškozený nebo svědek. Odděl osobní a korporátní zájem a případný konflikt zastoupení. Z dodaných podkladů sestav chronologii rozhodnutí, smluv, účetních operací, plateb, daňových podání a procesních úkonů. U každé osoby rozliš tehdejší znalosti od toho, co se ukázalo později.

Propoj trestní řízení s daňovou kontrolou, insolvencí, civilními nároky, licencemi a profesními povinnostmi, ale nepřenášej automaticky závěry ani důkazní břemena mezi režimy. V CODEXIS ověř rozhodná znění, pozdější příznivější právní úpravu, promlčení a pravidla pokračování. Nepřepisuj kvalifikaci podle zapamatované změny hranic škody.

### Mapa možných skutkových podstat

U podvodu zjišťuj konkrétní klam, omyl, majetkovou dispozici, kauzalitu a úmysl v rozhodném okamžiku. Pozdější platební neschopnost sama nedokládá původní podvodný úmysl. U úvěru a dotace odděl nepravdivé údaje při žádosti, použití prostředků v rozporu s účelem a kvalifikovaný následek; absence konečné škody nemusí odpovídat absenci všech znaků základní skutkové podstaty. Porušení dotačních podmínek není samo trestní kvalifikací. U unijních prostředků samostatně prověř působnost příslušných orgánů včetně evropského žalobce.

U zpronevěry ověř svěření, vlastnictví a smluvní titul nakládání. U správy cizího majetku určuj konkrétní povinnost, její adresáta, porušení, zavinění a škodu. Podnikatelský neúspěch neposuzuj zpětně bez informací a možností dostupných při rozhodování. Zkoumej delegaci, kontrolu, střet zájmů a hranice podnikatelského úsudku.

U poškození nebo zvýhodnění věřitele a insolvenčních deliktů dolož finanční stav, splatné závazky, dispozice s majetkem, postavení jednotlivých věřitelů a znalost jednajících osob. Nezaměňuj účetní ztrátu, nedostatek hotovosti, úpadek a jeho trestněprávní následek. Ověř povinnosti součinnosti, správnost seznamů a potřebné znalecké otázky.

U daní odděl zkrácení daně od neodvedení skutečně sražených či vybraných částek. Prověř reálnost plnění, fakturaci, tok peněz, možnost dispozice a důkazy zavinění. Standard daňového posouzení účasti na podvodu nepřenášej bez dalšího na trestní úmysl. U účetnictví, evidence a výkazů rozliš formální vadu od zákonem vyžadovaného ohrožení nebo následku.

Podle skutků prověř legalizaci výnosů, zdroj majetku, vlastní či cizí předchozí činnost a případnou nedbalostní formu; úplatkářství ve veřejné i soukromé sféře; manipulaci zakázky nebo soutěže; zneužití informací a postavení, neoprávněné podnikání, soutěžní, duševněvlastnické, počítačové nebo měnové delikty. Sponzoring, provize ani formálně označená poradenská smlouva samy nerozhodují o povaze protiplnění.

### Škoda, prospěch a odpovědnost

Zpracuj samostatné výpočty škody, získaného prospěchu a rozsahu jednání. Ověř ocenění, rozhodný okamžik, zahrnutí daně, dílčí plnění, skutečně dotčenou část dotace a přípustnou agregaci skutků. Pozdější úhradu vyhodnoť odděleně pro dokonání, škodu, náhradu a sankci. U neznámých parametrů dodej vzorec a chybějící důkazy, nikoli vymyšlený součet.

U právnické osoby zkoumej každý předpoklad přičitatelnosti, souvislost s činností a význam konkrétních preventivních opatření. Papírový compliance program není důkazem skutečného fungování. Odděl opatření existující před skutkem od pozdější nápravy. Posuď procesní zastoupení, právní nástupnictví a dopad možných trestů na zaměstnance, věřitele a pokračování podniku.

Samostatně vyhodnoť smluvní zesplatnění bankovního financování, zákonnou způsobilost dodavatele veřejné zakázky, trestní zákaz činnosti a možnosti nápravných opatření dodavatele. Není to jediný automatický následek „trestního problému“. Každý skutečně doložený smluvní spouštěč zachovej a ověř vedle veřejnoprávního režimu.

### Obhajoba, zajištění a náprava

Sestav matici znaků, důkazů obžaloby, slabin, protiargumentů a návrhů dokazování. U odborných otázek určuj zadání znalci a potřebná vstupní data; znalecký závěr nenahrazuje právní subsumpci. Zvaž ochranu před sebeobviněním a použití výpovědí či dokumentů v souběžných řízeních.

U prohlídek a digitálních dat odděl oprávnění získat zařízení od možnosti zkoumat obsah, ověř výjimky a ochranu důvěrných sdělení. Nevyžaduj bez rešerše pokaždé nové povolení. U majetkového zajištění rozliš výnos, náhradní hodnotu, nárok poškozeného a budoucí trest; zkoumej přiměřenost, trvání, provozní peníze a práva třetích osob. Daňový zajišťovací příkaz nepovažuj za stejný institut.

U účinné lítosti ověř přesný okruh činů, dobrovolnost, dobu a rozsah nápravy i odlišnosti fyzických a právnických osob. U upuštění od potrestání, odklonů, dohody nebo spolupráce prověř všechny podmínky včetně postoje k poškozenému, náhrady či jiného zadostiučinění a proporcionality. Samotná úhrada negarantuje zastavení. Klient musí rozhodnout informovaně o přiznání a jeho dalších důsledcích.

### Prevence a výstup

Pokud je zadána compliance, navrhni opatření odpovídající doloženým rizikům: rozhodovací a kontrolní pravomoci, prověřování partnerů, schvalování plateb, dary, střety zájmů, oznamování, školení a uchování záznamů. Nedoporučuj skrývání, zpětné falšování ani ničení dokumentů.

Dodej požadované konkrétní podání nebo interní opatření, právní kvalifikaci ve variantách, skutkovou a důkazní mapu, výpočet relevantních hodnot, procesní petit a náklady. Ukaž největší právní i ekonomické riziko, realistickou alternativu a chybějící podklady. Neověřený znak nebo zdroj nesmí zmizet v kategorickém shrnutí.
