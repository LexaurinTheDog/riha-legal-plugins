---
uuid: 68b2a19b-42d1-4372-9078-585514ff420f
name: skolske-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Školské právo ČR"
    summary: "Přijímání do škol a odvolání, spádovost, speciální vzdělávací potřeby a podpůrná opatření, kázeňská opatření a vyloučení, šikana a bezpečnost, pracovní vztahy pedagogů, škola jako právnická osoba a zřizovatel, ČŠI, úplata a školné, vysoké školy a studenti."
    examplePrompts:
      - "Dítě nebylo přijato do spádové základní školy pro naplněnou kapacitu. Jak podat odvolání a jaké jsou šance?"
      - "Ředitel střední školy chce vyloučit žáka za opakované porušení školního řádu. Jaký je postup, lhůty a jak se žák může bránit?"
      - "Učitelka bez plné kvalifikace má smlouvu na dobu určitou potřetí za sebou. Je to v souladu se zákonem o pedagogických pracovnících a zákoníkem práce?"
  en:
    displayName: "Czech Education Law"
    summary: "School admissions and appeals, catchment areas, special educational needs and support measures, discipline and expulsion, bullying and safety, teachers' employment, school as a legal entity and its founder, school inspection, tuition and fees, universities and students."
    examplePrompts:
      - "A child was not admitted to the catchment primary school due to full capacity. How to appeal and what are the chances?"
      - "A secondary school principal wants to expel a pupil for repeated breaches of school rules. What is the procedure, the deadlines, and how can the pupil defend?"
      - "A teacher without full qualification has a third consecutive fixed-term contract. Is this compliant with the pedagogical staff act and the Labour Code?"
  sk:
    displayName: "Školské právo ČR"
    summary: "Prijímanie do škôl a odvolania, spádovosť, špeciálne výchovno-vzdelávacie potreby a podporné opatrenia, disciplinárne opatrenia a vylúčenie, šikana a bezpečnosť, pracovné vzťahy pedagógov, škola ako právnická osoba a zriaďovateľ, ČŠI, úplata a školné, vysoké školy a študenti."
    examplePrompts:
      - "Dieťa nebolo prijaté do spádovej základnej školy pre naplnenú kapacitu. Ako podať odvolanie a aké sú šance?"
      - "Riaditeľ strednej školy chce vylúčiť žiaka za opakované porušenie školského poriadku. Aký je postup, lehoty a ako sa žiak môže brániť?"
      - "Učiteľka bez plnej kvalifikácie má zmluvu na dobu určitú tretíkrát za sebou. Je to v súlade so zákonom o pedagogických zamestnancoch a zákonníkom práce?"
description: 'Use for Czech schools, pupils, parents, teachers, school founders and universities: přijímací řízení, spádovost, odklad a povinná docházka, inkluze a podpůrná opatření, školní řád, kázeň a vyloučení, hodnocení a maturita, šikana a úraz, ředitel a pedagogové, ČŠI, školné, financování, VŠ, disciplinární řízení a poplatky za studium. Distinguish administrative, factual, employment and contractual routes. Research legal sources only through native CODEXIS in the application.'
---

# Školské právo ČR

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

## Oborový plán rešerše a výstupů

Nejprve označ klienta: dítě, zákonný zástupce, zletilý žák, student, pedagog, ředitel, škola nebo zřizovatel. Zjisti druh a právní formu školy, školní rok, datum podání, rozhodnutí, doručení a faktického zásahu. Ptej se, zda klient požaduje přijetí, návrat do výuky, podporu, změnu hodnocení, náhradu újmy nebo pracovněprávní ochranu. Tyto cíle mají rozdílné důkazní i procesní předpoklady.

### Mapa právních otázek

- Kdy škola rozhoduje ve veřejnoprávním řízení a kdy jedná fakticky, smluvně či jako zaměstnavatel? V CODEXIS ověř zvláštní školskou úpravu, obecný správní proces, soudní ochranu a vztah k pracovnímu a občanskému právu. Poučení školy není samo důkaz správné procesní cesty. Rozliš příjemce podání od orgánu, který o něm rozhoduje.
- Jaká pravidla přijímání platila pro daný ročník a kolo? Prověř zveřejnění kritérií, kapacitu, spádovost, pořadí, losování, talentové a jednotné zkoušky, elektronické přihlášky, jazykové úlevy, přestupy a uvolněná místa. U MŠ a ZŠ ověř věkové podmínky, povinné vzdělávání, zdravotní podmínky a výjimky. U odkladu, vzdělávání doma či v zahraničí načti podmínky a potřebná doporučení. Staré termíny ani již nepoužívané úkony nepřenášej.
- Jaká podpůrná opatření vyžaduje konkrétní potřeba? Odliš pedagogické hodnocení, doporučení poradenského zařízení, jeho revizi a povinnosti školy. Ověř souhlas, individuální plán, asistenci, pomůcky, tlumočení, nadání, odlišný mateřský jazyk, zdravotní výuku a zařazení do zvláštní třídy. Nedostatek prostředků není bez dalšího ověřená omluva; porovnej dostupné stížnostní, zásahové a antidiskriminační prostředky.
- Splnil žák skutečně povinnou docházku? Samotný název školy to neprokazuje. Pro kázeň rozliš intenzitu, zavinění, opakování a kumulativní zákonné znaky; jednotlivý konflikt neoznač automaticky za kvalifikovaný útok. Zvlášť ověř čas pro zahájení řízení, čas rozhodnutí, případnou trestní výjimku, slyšení žáka, dokazování a interní projednání. Vyloučení, právní moc a zákaz vstupu jsou samostatné události.
- Jaké prostředky směřují proti hodnocení, opravné zkoušce, maturitě nebo jejímu dílčímu výsledku? Ověř rozhodující orgán, formu, přezkoušení a počátek lhůty; nemíchej právní přezkum s novým odborným hodnocením. U školního řádu prověř přijetí a seznámení, meze omezení mobilů, oblečení a náboženských projevů, omlouvání absence a informace rodičům.
- Jak vznikl úraz nebo šikana a kdo měl dohled? Rozliš školu, pedagoga, agresora, jeho zástupce, pořadatele a pojistitele; ověř každý titul odpovědnosti a případný regres samostatně. Vyžádej časovou osu, záznamy, svědky, lékařské zprávy a přijatá opatření. Prověř oznamování, bezpečnost akcí, zdravotní péči, léky, alergie a stravování. U kamer, fotografií a matriky ověř právní titul, účel a ochranu údajů.
- Jaké jsou předpoklady pedagoga, uznání kvalifikace a výjimky? Ověř dobu určitou, její řetězení, přímou pedagogickou práci, odměňování, dovolenou, vzdělávání a skončení. U ředitele odděl jmenování, konkurz, funkci, odvolání a pracovní poměr; nepředpokládej automaticky správní soudnictví.
- U školy a zřizovatele prověř rejstříkový stav, kapacitu, zřizovací listinu, školskou radu, financování, dotace, úplatu a osvobození. Rozliš kontrolu ČŠI, opravu inspekčního závěru a právní prostředek klienta. U soukromé školy reviduj školné, změny ceny, ukončení a vracení plateb jako smluvní otázky.
- U VŠ samostatně řeš přijetí, studijní a zkušební pravidla, uznávání předmětů, přerušení, ukončení, stipendia, poplatky a jejich prominutí, disciplinární řízení, plagiátorství, nostrifikaci, tituly, habilitace, akreditaci a akademickou samosprávu. Pravidla nižších škol nepřenášej.

### Kontrola strategie

V CODEXIS vyhledej přiléhavé správní, civilní a ústavní rozhodnutí podle povahy otázky, včetně práva na vzdělání, rovného přístupu a spolupůsobení rodičovské odpovědnosti. Požadovanou praxi konkrétního senátu nevyvozuj z obecných rozhodnutí soudu. U konfliktu rodičů ověř rozsah zastupování a skutečná soudní omezení, nikoli tvrzení jednoho rodiče.

Výstup musí obsahovat tabulku krok, orgán, ověřený právní základ, rozhodný okamžik, důkaz, lhůta a riziko; při cíli okamžitého návratu do výuky zvlášť posuď předběžnou ochranu a subsidiaritu. Stížnost sama není návratem do výuky. Dodej požadované podání či změněné smluvní články, odpovídající petit a položkový rozpočet. Kapacity, vnitřní předpisy a skutkové listiny čerpej z podkladů; jejich nedostupnost nepřeklenutá nativním zdrojem zůstává otevřenou otázkou.
