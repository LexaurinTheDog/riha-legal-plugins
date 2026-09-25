---
uuid: 86ca962b-ddad-4712-a9ed-fb012f3fe23a
name: pracovni-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Pracovní právo ČR"
    summary: "Pracovní poměr od vzniku po skončení - výpověď a její neplatnost, odstupné, mzda a pracovní doba, odpovědnost, konkurenční doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zaměstnavatel chce dát výpověď pro nadbytečnost zaměstnanci, který je 3 měsíce v pracovní neschopnosti. Lze to a jak?"
      - "Klient dostal okamžité zrušení pracovního poměru za pozdní příchody. Je to platné a do kdy se bránit?"
      - "Připrav konkurenční doložku pro obchodního ředitele tak, aby byla vymahatelná."
  en:
    displayName: "Czech Labour Law"
    summary: "Employment from formation to termination - notice and its invalidity, severance, pay and working time, liability, non-compete, agreements outside employment, disguised employment, disputes."
    examplePrompts:
      - "An employer wants to give redundancy notice to an employee who has been on sick leave for 3 months. Is it possible and how?"
      - "My client received an immediate termination for late arrivals. Is it valid and by when must they challenge it?"
      - "Draft a non-compete clause for a sales director so that it is enforceable."
  sk:
    displayName: "Pracovné právo ČR"
    summary: "Český pracovný pomer od vzniku po skončenie - výpoveď a jej neplatnosť, odstupné, mzda a pracovný čas, zodpovednosť, konkurenčná doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zamestnávateľ chce dať výpoveď pre nadbytočnosť zamestnancovi, ktorý je 3 mesiace práceneschopný. Dá sa to a ako?"
      - "Klient dostal okamžité zrušenie pracovného pomeru za neskoré príchody. Je platné a dokedy sa brániť?"
      - "Priprav konkurenčnú doložku pre obchodného riaditeľa tak, aby bola vymáhateľná."
description: 'Použij pro zaměstnavatele, zaměstnance, HR a odbory: pracovní smlouvy, DPP a DPČ, dobu určitou a zkušební dobu, skončení a neplatnost, mzdu a pracovní dobu, dovolenou a home office, odpovědnost a úrazy, konkurenční doložky, přechod práv, propouštění, agenturní a nelegální práci, diskriminaci, whistleblowing a inspekci. Právní zdroje jen nativní CODEXIS v aplikaci.'
---

# Pracovní právo ČR

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

## Strana, vztah a časová osa

Urči klientovu stranu a cíl: vznik nebo změnu vztahu, jeho bezpečné skončení, obranu proti rozvázání, vymáhání plnění, nastavení HR nebo kontrolu inspekce. Zájmy zaměstnavatele, zaměstnance a odborů nejsou totožné. Z podkladů zjisti skutečný výkon, smlouvu, dodatky, kolektivní úpravu, vnitřní předpisy, výplatní a docházkové záznamy, organizační rozhodnutí, výtky, zdravotní podklady a doručenky. Datum listiny nezaměňuj s doručením ani tvrzený důvod s prokázaným skutkem.

Rozliš pracovní poměr, dohody mimo něj, agenturní zaměstnání, služební vztah a samostatné podnikání. Závislou práci posuzuj podle skutečných znaků a rozsahu, nikoli podle faktury nebo názvu smlouvy. U cizinců a přeshraničního výkonu přidej pobytové, zaměstnanostní a kolizní otázky; český formulář automaticky neurčuje celý právní režim.

## Nativní právní a časová kontrola

V CODEXIS vyhledej zákoník práce, subsidiární občanské právo, zaměstnanost, inspekci, antidiskriminační úpravu, ochranu oznamovatelů, nemocenské a další potřebné pojistné předpisy, pracovní úrazy, prováděcí mzdová pravidla a civilní proces. U mzdy, délky vztahu, právního jednání, doručení, žaloby i tarifu urč samostatně rozhodné znění a přechod. Novela nečiní všechny starší smlouvy automaticky podřízenými jednomu novému pravidlu.

Každou odchylku od zákona posuď podle konkrétní normy, minim, maxim, kogentních požadavků a zákazu vzdání se chráněných práv. Nepoužívej ani univerzální zákaz odchylky v neprospěch zaměstnance, ani obecnou smluvní volnost. Pevné hodinové limity, sazby a násobky ze starého vzoru nahraď ověřeným zněním v nativním nástroji.

## Vznik, změny a skončení

Při tvorbě smlouvy zkontroluj druh práce, místo, nástup, formu, informování, odměnu, dobu určitou, její opakování a případné výjimky. U zkušební doby ověř sjednání, délku, prodloužení a vztah k době určité. U dohod vyhledej rozsah práce, rozvrh, evidenci, dovolenou a pojistné či informační souvislosti. Podle zadání doplň přechod práv a povinností, změnu místa nebo druhu práce, hromadné propouštění a součinnost s odbory a veřejnými orgány.

U skončení odděl dohodu, výpověď, okamžité zrušení, zrušení ve zkušební době, uplynutí doby a jiné zákonné události. Který důvod lze použít pro skutečné skutky, jaká intenzita porušení je požadována, je nutná předchozí výtka, organizační změna, lékařský posudek či souhlas odborů? Nezaměňuj závažné a zvlášť hrubé porušení a nedoplňuj chybějící opakování. Prověř ochrannou dobu a konkrétní výjimky, oprávnění podepsat, formu a dovolený způsob doručení včetně elektronického.

Výpovědní důvod, subjektivní a objektivní lhůtu zaměstnavatele, běh výpovědní doby a žalobní lhůtu zaměstnance počítej odděleně. Samotná oprava jedné lhůty neřeší ostatní. U doručení dolož počátek, právní pravidlo a konec; souhlas s elektronickou komunikací a technické odeslání nemusí samy splnit zákonný režim. Vyhledej odstupné či jiné zvláštní plnění, potvrzení o zaměstnání a návaznost na podporu.

## Neplatné skončení a peněžní následky

Odděl žalobu na neplatnost od písemného oznámení, že zaměstnanec trvá na dalším zaměstnávání. Zaznamenej druh rozvázání, zamýšlený den skončení, oznámení, skutečný výkon práce, nepřidělování a možnost či připravenost pracovat. Náhradu nesčítej se mzdou za stejnou skutečně vykonanou práci. Pro jednotlivá období urč titul, vstupní průměrný výdělek, výjimky a případné moderování včetně potřeby návrhu.

U netrvání na pokračování rozliš následky neplatné výpovědi a jiných způsobů zrušení; zvláštní náhradu z jedné větve automaticky nepřenášej do druhé. U rozvázání zaměstnancem zkoumej vlastní režim nároků zaměstnavatele. Prekluzi a promlčení neztotožňuj. Návrh dohody nesmí bez kontroly potlačit již vzniklá nebo kogentně chráněná práva.

## Práce, odměna a odpovědnost

U mzdy a platu prověř použitelné minimum, zaručený standard, rovné odměňování, příplatky, přesčas, práci ve svátek a noci, pohotovost, evidenci a splatnost. U pracovní doby zkoumej rozvrh, přestávky a odpočinek. U dovolené a překážek urč skutečné období a nárok včetně práce na dohodu; nezaměňuj kalendářní dny, směny a hodiny. U home office připrav konkrétní dohodu, náklady, bezpečnost a ukončení režimu.

Odpovědnost zaměstnance rozděl na obecnou škodu, schodek, ztrátu svěřených věcí a další tituly; u každého ověř zavinění, dohody, důkazní břemeno a limity. U zaměstnavatele odděl obecnou odpovědnost, pracovní úraz a nemoc z povolání, zproštění, jednotlivé náhrady a pojistnou souvislost. U škody a výdělku používej doložené výpočty, nikoli pevný násobek.

U konkurenční doložky zkoumej oprávněný zájem, přípustný rozsah, vyrovnání, sankci a ukončení. Mlčenlivost, souběžnou činnost, monitoring, osobní údaje a ochranu oznamovatele posuzuj samostatně; smluvní pokutu nebo zajištění nepřebírej z obchodní smlouvy. Přípustnou ochranu klienta promítni do konkrétní klauzule.

## Spor a dokončení

Připrav argumenty a nejsilnější protiargument, důkazní mapu, předžalobní výzvu, vykonatelný petit a příslušný soud. Diskriminaci a přesun důkazního břemene opři o konkrétní podmínky. Podnět inspekci není rozhodnutím o soukromém nároku ani automatickým stavením lhůty. Rozpočet zahrnuje každé podání, osvobození a tarifní úkony. Při smluvním zadání dodej hotovou listinu s řádným skutkovým vymezením a podpisovým/doručovacím plánem; návrh ani jeho předání klientovi neoznačuj za doručené skončení pracovního poměru.
