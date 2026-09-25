---
uuid: 14ac3e62-b159-48c8-8ae6-4919f615132d
name: spravni-a-danove-rizeni
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Správní a daňové řízení ČR"
    summary: "Obrana proti rozhodnutím a postupům úřadů a správce daně - odvolání, přezkum, správní žaloba, kasační stížnost, daňová kontrola, sankce, prekluze, lhůty."
    examplePrompts:
      - "Finanční úřad doměřil DPH po kontrole a vyměřil penále. Jaké procesní námitky máme a do kdy podat odvolání?"
      - "Odvolací orgán potvrdil rozhodnutí stavebního úřadu. Připrav osnovu správní žaloby a posuď odkladný účinek."
      - "Úřad je rok nečinný v řízení o žádosti. Jaké prostředky obrany máme a v jakém pořadí?"
  en:
    displayName: "Czech Administrative and Tax Procedure"
    summary: "Challenging decisions and conduct of authorities and tax administrators - appeals, review, judicial review, cassation, tax audits, penalties, time bars, deadlines."
    examplePrompts:
      - "The tax office assessed additional VAT after an audit and imposed a penalty. Which procedural objections do we have and by when to appeal?"
      - "The appellate body upheld the building authority's decision. Draft an outline of the judicial review action and assess suspensive effect."
      - "An authority has been inactive for a year on our application. Which remedies do we have and in what order?"
  sk:
    displayName: "Správne a daňové konanie ČR"
    summary: "Obrana proti rozhodnutiam a postupom úradov a správcu dane v ČR - odvolanie, preskúmanie, správna žaloba, kasačná sťažnosť, daňová kontrola, sankcie, preklúzia, lehoty."
    examplePrompts:
      - "Finančný úrad dorubil DPH po kontrole a vyrubil penále. Aké procesné námietky máme a dokedy podať odvolanie?"
      - "Odvolací orgán potvrdil rozhodnutie stavebného úradu. Priprav osnovu správnej žaloby a posúď odkladný účinok."
      - "Úrad je rok nečinný v konaní o žiadosti. Aké prostriedky obrany máme a v akom poradí?"
description: 'Use to respond to or challenge Czech public authorities and tax administrators: administrative or tax procedure, decision, order, request, general measure, inaction or intervention, appeal, remonstrance, review, reopening, administrative court action, cassation, suspensive effect, tax audit, doubts, assessment, penalties, interest, securing orders, enforcement, time bars, remission, service and fees. Combine substantive taxation with the tax-law profile. Research legal sources only through native CODEXIS in the application.'
---

# Správní a daňové řízení ČR

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

## Povaha aktu před volbou prostředku

Zapiš klienta, správní či daňový orgán, procesní postavení, požadovaný výsledek a přesný napadaný úkon. Z podkladů sestav časovou osu zahájení, výzev, dokazování, rozhodnutí, doručení a výkonu. Rozliš tvrzení klienta a úřadu od doložených událostí; neoznačuj plánovaný opravný prostředek za podaný.

V CODEXIS ověř zvláštní oborovou úpravu a její vztah ke správnímu řádu, daňovému řádu a soudnímu řádu správnímu. Režim neurčuje hlavička úřadu ani jeho poučení. Samostatně zjisti rozhodné znění pro hmotnou povinnost, procesní úkon, sankci a přechod řízení.

### Procesní mapa

- Je napadeno rozhodnutí, usnesení, výzva, osvědčení, sdělení, kontrolní protokol, opatření obecné povahy, faktický zásah nebo nečinnost? Ověř právní účinky aktu, ne pouze název. Pro každou variantu určuj dostupné odvolání, rozklad, námitky, stížnost, přezkum, obnovu a soudní ochranu samostatně.
- Jak se stanoví věcná, místní a funkční příslušnost? Kdo je účastníkem, kdo zastupuje a kdy vzniká podjatost? Zjisti přístup ke spisu, možnost vyjádřit se a navrhovat důkazy. Ověř pravidla dokazování, odůvodnění, určitost výroku, poučení a doručení. Každou vadu spoj s jejím dopadem: nikoli každá nepravidelnost zakládá nicotnost nebo zrušení.
- Která událost spustila lhůtu? Vyhodnoť doručení zástupci, účinnost plné moci, fikci, datovou schránku, veřejnou vyhlášku a opomenutého účastníka podle konkrétního režimu. Délku, počátek, stavění, přerušení, prodloužení či prominutí načti z nativního právního zdroje. Právní moc a vykonatelnost nejsou totožné s doručením.
- Pro správní žalobu rozliš rozhodnutí, zásah, nečinnost a zrušení opatření obecné povahy. Ověř legitimaci, subsidiaritu, vyčerpání prostředků, žalovaného, soud, koncentraci a rozsah petitu. Námitku proti podkladovému aktu připoj správnou cestou; nepředpokládej automaticky jeho samostatnou napadnutelnost.
- U kasace zjisti přípustnost, případnou přijatelnost, zastoupení, zákonné důvody, čas a vztah k předchozím námitkám. Ústavní rovinu opři o konkrétní zásah, nikoli o obecný nesouhlas s hodnocením.

### Daňová a sankční větev

Odliš daňovou kontrolu, postup k odstranění pochybností, stanovení daně, placení, zajištění a exekuci. Pro každý úkon ověř zahájení, rozsah, opakování, součinnost, projednání výsledku a opravnou cestu. Promlčení placení a prekluze stanovení nejsou stejnou otázkou; sestav úplnou časovou osu relevantních událostí a jejich zákonných účinků.

U DPH odděl skutečnost plnění, postavení dodavatele, formální doklady a účast na podvodu. Vyvrácení jednoho důvodu samo neodstraňuje druhý nezávislý důvod doměření. Ke každému závěru přiřaď důkazní břemeno a konkrétní skutkovou oporu. Právní domněnku nezaměňuj s prokázanou znalostí nebo úmyslem.

Prověř, zda odvolací orgán přidal skutkové podklady či nové právní posouzení, k nimž měl klient dostat možnost reakce. Podnět přezkumu neslibuj jako řádný opravný prostředek. U obnovy odděl nový důkaz o staré skutečnosti od pozdější změny poměrů.

Penále, úrok z prodlení, úrok související s posečkáním, pokuta za opožděné tvrzení a jiné sankce mají vlastní podmínky, základ, sazbu, časový režim a cestu prominutí. Načti je jednotlivě; správní metodiku nebo pokyn správce neoznač za zákon. U souběhu se správním trestáním nebo trestním řízením ověř zákaz dvojího postihu a procesní použití podkladů, nikoli automatickou blokaci jednoho řízení druhým.

### Dočasná ochrana, náklady a výstup

Zjisti, zda opravný prostředek skutečně má odkladný účinek, zda byl vyloučen a jak o ochranu žádat. Posečkání daně není totéž co odkladný účinek žaloby; porovnej rozsah, trvání, úroky a vliv na exekuci. K návrhu připoj konkrétní scénář újmy klienta, dopad na jiné osoby a veřejný zájem, doložené finanční údaje a přesně označený výkon.

V CODEXIS zpracuj rozhodnutí přiléhavá povaze aktu, důkazním vadám a časovým otázkám; ověř navazující a případně překonávající judikaturu i rozšířený senát. Je-li požadována praxe konkrétního senátu, eviduj skutečně identifikované srovnávací věci.

Dodej použitelné podání: režim, včasnost, přípustnost, procesní vady, věcné argumenty, důkazy, nejsilnější protiargument a přesný petit. Náklady rozepiš pro každý prostředek, zejména odděleně žalobu a návrh na odkladný účinek, zastoupení a případné další úkony; u každého ověř osvobození. Neoznačuj posečkání za bezúročné ani návrh za bezplatný bez zdroje. Navazující náhradu škody a nesprávný úřední postup posuď samostatně včetně předběžného uplatnění a podmínek nároku.
