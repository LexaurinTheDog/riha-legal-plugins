---
uuid: 52b7f277-741b-453a-8643-8781e5c870ee
name: exekuce-obrana-dluznika
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Exekuce - obrana povinného ČR"
    summary: "Audit exekučního titulu, návrhy na odklad a zastavení, nezabavitelné minimum a chráněný účet, mobiliární exekuce, nemovitost a SJM, vylučovací žaloby třetích osob, náklady, stížnosti, oddlužení jako východisko."
    examplePrompts:
      - "Klientovi přišlo vyrozumění o zahájení exekuce pro dluh z roku 2012 podle rozhodčího nálezu. Co zkontrolovat a jaké návrhy podat?"
      - "Exekutor zablokoval účet, na který chodí mzda a přídavky na děti. Jak rychle uvolnit prostředky?"
      - "Exekutor sepsal v bytě věci, které patří přítelkyni povinného. Jak je dostat ze soupisu?"
  en:
    displayName: "Czech Enforcement Defence"
    summary: "Auditing the enforcement title, motions to stay and stop, protected minimum and protected account, seizure of movables, real estate and marital property, third-party claims, costs, complaints, debt relief as an exit."
    examplePrompts:
      - "My client received a notice of enforcement for a 2012 debt based on an arbitration award. What to check and which motions to file?"
      - "The bailiff froze an account receiving wages and child benefits. How to release funds quickly?"
      - "The bailiff inventoried items in the flat that belong to the debtor's girlfriend. How to get them off the inventory?"
  sk:
    displayName: "Exekúcia - obrana povinného ČR"
    summary: "Audit exekučného titulu v ČR, návrhy na odklad a zastavenie, nezabaviteľné minimum a chránený účet, mobiliárna exekúcia, nehnuteľnosť a BSM, vylučovacie žaloby tretích osôb, trovy, sťažnosti, oddlženie ako východisko."
    examplePrompts:
      - "Klientovi prišlo upovedomenie o začatí exekúcie pre dlh z roku 2012 podľa rozhodcovského nálezu. Čo skontrolovať a aké návrhy podať?"
      - "Exekútor zablokoval účet, na ktorý chodí mzda a prídavky na deti. Ako rýchlo uvoľniť prostriedky?"
      - "Exekútor spísal v byte veci, ktoré patria priateľke povinného. Ako ich dostať zo súpisu?"
description: 'Obrana povinného, manžela a třetích osob v soudní exekuci a v souvisejícím výkonu rozhodnutí: titul, doručení, zastavení, odklad, vyloučení majetku, chráněné příjmy a náklady. Rozlišuje daňovou a správní exekuci, insolvenční souběh a odpovědnost za nesprávný postup. Primární vymáhání z pozice věřitele řeší příslušný věřitelský skill.'
---

# Exekuce a obrana dlužníka

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

## Zadání, fáze a podklady

Zjisti, zda chráníš povinného, jeho manžela, vlastníka postižené věci nebo jinou osobu, jaký výsledek klient potřebuje a co bezprostředně ohrožuje jeho bydlení, příjem či provoz. Rozliš soudní exekuci, soudní výkon rozhodnutí a daňové či správní vymáhání. U nepeněžitého plnění, zejména vyklizení, samostatně ověř způsob výkonu, ochranu dotčených osob a podmínky odkladu. Z dokumentů vytvoř mapu všech souběžných řízení, titulů, exekučních příkazů, postiženého majetku, skutečných úhrad a plánovaných úkonů. Údaje o jiných řízeních ani stav evidence nedoplňuj domněnkou.

Sestav časovou osu vzniku a splatnosti dluhu, nalézacího řízení, doručování, právní moci, vykonatelnosti, zahájení vymáhání a každé platby. Odděl doručení povinnému, zástupci a případnou fikci. Která právní úprava a přechodná ustanovení dopadají na každý krok? Jaké rozdílné lhůty jsou spojeny s dobrovolným splněním, návrhem na zastavení, námitkami proti nákladům a dražbou? Obecné poučení neber jako důkaz správného doručení.

## Titul a rozsah vymáhaného práva

Ověř v nativním CODEXIS podmínky formální a materiální vykonatelnosti právě tohoto titulu. Co vyžaduje určitost účastníků, plnění, času a podmínky plnění? Existuje podklad pro přechod práva či povinnosti? Jaký význam mají vadné doručení platebního rozkazu, rozsudek pro zmeškání, rozhodčí doložka ve spotřebitelském vztahu, notářský zápis nebo veřejnoprávní titul? Je nutný samostatný opravný prostředek v původním řízení a jak se vztahuje k exekuční obraně?

Prověř promlčení podle rozhodných časových pravidel, zaplacení, započtení, prominutí, dohodu, zánik zajištění, nepřípustné příslušenství a zvláštní ochranu zranitelného či nezletilého dlužníka. Úhradu před podáním exekučního návrhu, po zahájení řízení a výtěžek vymožený exekutorem posuzuj odděleně. Blokace účtu není bez dokladu úhradou věřiteli. Každou částku přiřaď ke dni, příjemci a právně ověřenému pořadí započtení; nepřeváděj sporné tvrzení věřitele na prokázaný zůstatek.

## Procesní obrana a naléhavé kroky

Pro každý důvod zastavení zjisti oprávněnou osobu, adresáta, obsah, důkazní břemeno, lhůtu, účinky a opravný prostředek. Odliš úplné a částečné zastavení i zvláštní obranu manžela. Lhůta, kterou exekutor poskytuje ostatním k vyjádření, není automaticky lhůtou pro jeho rozhodnutí nebo předložení věci soudu: vyhledej každou z těchto povinností samostatně.

Kdy lze žádat odklad pro dočasnou nepříznivou situaci, očekávané zastavení nebo jiný konkrétní důvod? Co musí klient tvrdit a doložit o nezavinění, přechodnosti, újmě a poměru k zájmům oprávněného? Prověř důvody bezvýslednosti řízení, podmínky ochrany před prodejem obydlí a souběh s insolvencí. Splátková dohoda sama o sobě nedokládá skončení exekuce ani jistý odklad dražby.

U majetku třetí osoby porovnej návrh na vyškrtnutí ze soupisu, vylučovací žalobu a další dostupné prostředky. Zjisti návazné lhůty, správného žalovaného, ochranu před zpeněžením a důkaz vlastnictví. U společného jmění odděl dobu vzniku závazku, jeho účel, souhlas či nesouhlas manžela, změny majetkového režimu a jejich účinky vůči věřiteli.

## Ochrana příjmů, majetku a základního provozu

Podle rozhodného období vyhledej pravidla srážek ze mzdy, přednostních pohledávek, vyživovaných osob, souběhu plátců, dalších příjmů a nezabavitelných plnění. Vypočti jednotlivé kroky z doložených příjmů, nikoli z historické tabulky. Zvlášť ověř ochranu sociálních dávek a příjmů po připsání na účet, podmínky chráněného účtu a případného jednorázového uvolnění prostředků; tyto instituty nezaměňuj.

Které věci jsou pro konkrétní osobu vyloučeny z postihu pro zdravotní, rodinný, osobní nebo pracovní účel? Co vyžaduje ochrana běžného vybavení domácnosti, zdravotních pomůcek, osobních předmětů, zvířat a podnikatelských nástrojů? Jak se uplatní přiměřenost zvoleného způsobu exekuce, hodnota majetku, alternativní uspokojení a práva spoluvlastníků?

## Náklady, veřejnoprávní vymáhání a odpovědnost

Odděl náklady oprávněného, náklady exekutora, soudní poplatky a vlastní smluvní odměnu klienta. Ověř rozhodnou tarifní úpravu, základ odměny, skutečně vymožené plnění, případné snížení při dobrovolném splnění, hotové výdaje, DPH a rozhodování o nákladech při zastavení. Kdo zavinil zahájení či pokračování a má to pro tento typ nákladů význam? Zastavení automaticky neznamená jednu předem danou nákladovou variantu.

U daňové a správní exekuce vyhledej jejich vlastní námitkové, odkladné, zastavovací a přezkumné prostředky včetně posečkání; nepřenášej mechanicky soudní exekuční postup ani předpoklad přípustného odvolání. Stížnost či dohled nenahrazují procesní obranu. Prověř podmínky odpovědnosti exekutora nebo státu, vznik škody, příčinnou souvislost a předběžné uplatnění.

## Výstup pro rozhodnutí

Dodej nejbližší bezpečný krok, varianty zastavení a odkladu, konkrétní podání s důkazy a vykonatelným petitem. U částečného zastavení přesně označ titul, jistinu, jednotlivé příslušenství a odlišné nákladové položky, včetně toho, které části návrh nezasahuje. Zachovej protistraně nejsilnější argumenty a doložené odpovědi.

Při práci s judikaturou rozliš závěr jednotlivých instancí, přezkumný výsledek a případné zrušení; nepřičítej nižšímu soudu názor přezkumného soudu ani nevymýšlej čísla odstavců. Posuď také dohodu, prominutí příslušenství, konsolidaci a oddlužení včetně oprávnění sepisovatele. Historické dluhové amnestie nabídni jen po ověření jejich aktuální použitelnosti. Uzavři plánem důkazů, lhůt, plateb, nákladů a neověřených bodů; připravený návrh není podáním ani rozhodnutím o zastavení.
