---
uuid: a0694e49-04e3-430c-89d7-4202875d068f
name: obce-a-verejna-sprava
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Obce a veřejná správa ČR"
    summary: "Působnost orgánů obce, nakládání s obecním majetkem a záměr, vyhlášky a jejich přezkum, svobodný přístup k informacím, dotace a obecní společnosti, referendum, dozor a přezkoumání hospodaření, odpovědnost zastupitelů."
    examplePrompts:
      - "Obec prodala pozemek bez zveřejnění záměru a za cenu pod znaleckým posudkem. Je smlouva platná a kdo za to odpovídá?"
      - "Občan žádá podle infozákona o smlouvy a platy vedoucích úředníků. Co musíme vydat, co odmítnout a v jakých lhůtách?"
      - "Zastupitelstvo chce vyhláškou zakázat konzumaci alkoholu na celém území obce. Obstojí to před ministerstvem a Ústavním soudem?"
  en:
    displayName: "Czech Municipal Law"
    summary: "Competences of municipal bodies, disposal of municipal property and publication of intent, by-laws and their review, freedom of information, municipal grants and companies, referendum, supervision and audit, liability of councillors."
    examplePrompts:
      - "A municipality sold a plot without publishing its intent and below the appraised price. Is the contract valid and who is liable?"
      - "A citizen requests contracts and salaries of senior officials under the freedom-of-information act. What must we disclose, what may we refuse, and by when?"
      - "The council wants a by-law banning alcohol consumption across the whole municipality. Will it survive ministry review and the Constitutional Court?"
  sk:
    displayName: "Obce a verejná správa ČR"
    summary: "Pôsobnosť orgánov obce v ČR, nakladanie s obecným majetkom a zámer, vyhlášky a ich preskúmanie, slobodný prístup k informáciám, dotácie a obecné spoločnosti, referendum, dozor a preskúmanie hospodárenia, zodpovednosť poslancov."
    examplePrompts:
      - "Obec predala pozemok bez zverejnenia zámeru a za cenu pod znaleckým posudkom. Je zmluva platná a kto za to zodpovedá?"
      - "Občan žiada podľa infozákona o zmluvy a platy vedúcich úradníkov. Čo musíme vydať, čo odmietnuť a v akých lehotách?"
      - "Zastupiteľstvo chce vyhláškou zakázať konzumáciu alkoholu na celom území obce. Obstojí to pred ministerstvom a Ústavným súdom?"
description: 'Použij pro obce, kraje a veřejné subjekty: samostatnou a přenesenou působnost, zastupitelstvo, radu a starostu, obecní majetek, záměry a smlouvy, normotvorbu a dozor, informace, dotace a rozpočet, obecní organizace, referendum, poplatky, střet zájmů a odpovědnost. Právní zdroje výhradně nativní CODEXIS v aplikaci.'
---

# Obce a veřejná správa ČR

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

## Postavení klienta a povaha jednání

Urči, zda zastupuješ obec, kraj, městskou část, orgán, zastupitele, úředníka, obecní společnost či organizaci, občana nebo smluvního partnera. Rozliš samostatnou a přenesenou působnost a soukromoprávní dispozici. Z této kvalifikace odvoď až po ověření odpovědný subjekt, orgán, dozor a soudní cestu. U Prahy a statutárního města prověř zvláštní úpravu a dodaný statut. Záměr obce, usnesení, smlouva, zveřejnění a podpis jsou samostatné skutkové události.

Vyžádej v aplikaci úplné dobové zápisy, podklady orgánu, text záměru a důkaz jeho zveřejnění, smlouvu, cenové ocenění, rozpočtové a dotační dokumenty. Neznámá čísla usnesení, parcely, hlasování a data nenahrazuj pamětí ani externím procházením registrů. U dodaného výpisu či potvrzení výslovně uváděj, jaké období dokládá.

## Mapa právní rešerše

Nativním CODEXIS ověř zákony o obcích, krajích a hlavním městě Praze, rozpočtová pravidla územních rozpočtů, přezkoumání hospodaření a finanční kontrolu, svobodný přístup k informacím, střet zájmů, referendum, místní poplatky a daňový řád. Podle věci přidej správní řád, úředníky, obecní policii, registr smluv, veřejné zakázky, petice, shromáždění a odpovědnost veřejné moci. Pro soukromé dispozice a obecní korporace připoj občanský zákoník a korporátní právo; pro zásah do samosprávy ústavní prameny. U každého úkonu načti rozhodné časové znění a přechod.

## Majetek a smluvní postup

Je konkrétní dispozice podmíněna zveřejněním záměru, jaká je výjimka, obsah, délka a okamžik splnění? Který orgán má vyhrazenou pravomoc, co lze delegovat a kdo může podepsat? Porovnej skutečný text smlouvy se schválením; doložka o splnění podmínek sama nenahrazuje jejich důkaz. U ceny obvyklé zjisti relevantní ocenění a případné důvody odchylky v celých dobových podkladech, ne pouze v jedné větě usnesení.

Vyhodnoť každou vadu zvlášť: záměr, kompetenci, předchozí schválení, cenu, střet zájmů, podpis, uveřejnění a účinnost. Neoznačuj všechny vady automaticky za totožnou neplatnost. Prověř registr smluv, výjimky, nápravu a časové následky, případné zadávání a veřejnou podporu. Újmu a individuální zavinění zastupitele neodvozuj jen z rozdílu cen nebo z neplatnosti.

U vadného převodu nejprve vyřeš, komu hmotněprávně náleží právo. Odděl odstranění nesouladu zápisu od nového nabytí; dohoda o opravě není automaticky nový nákup. Bezodkladně prověř ochranu před nesprávným zápisem a její lhůty i při probíhajícím jednání. Rozliš vzájemnou restituci a samostatný nárok na náhradu újmy. Požadovaná dohoda musí upravit skutečné vypořádání, nikoli zakrýt chybějící schválení.

## Orgány, normotvorba a transparentnost

U zastupitelstva a rady ověř svolání, program, veřejnost, kvórum, rozhodnou množinu hlasů, práva občana vyjádřit se, zápis a námitky. U mandátu, neslučitelnosti, odměn, tajemníka, výborů a komisí zjisti konkrétní kompetence. Oznámení osobního zájmu a případnou překážku hlasování posuzuj odděleně.

U obecně závazné vyhlášky, nařízení a opatření obecné povahy rozliš právní formu, zmocnění, působnost, postup vydání, publikaci, účinnost a přezkum. Vyhledej aktuálně použitelné judikatorní testy zákonnosti a proporcionality; nepovažuj každé překrytí se zákonem automaticky za zakázanou duplicitu. U tržního řádu, veřejného pořádku, odpadu, hřbitovů, poplatků a územního plánu urč zvláštní pramen i kontrolní orgán.

U informací prověř povinný subjekt, existenci a povahu informace, žádost, doplnění, lhůtu, úhradu, částečné poskytnutí, anonymizaci a odmítnutí. Platy, obchodní tajemství, osobní údaje a vnitřní dokumenty nepodřazuj paušálně výluce; uveď konkrétní test veřejného zájmu. Odděl odvolání, stížnost na postup a žalobu podle skutečného úkonu.

## Rozpočet, organizace a veřejnost

U rozpočtu a závěrečného účtu zkontroluj návrh, zveřejnění, projednání, schválení, změny a nápravná opatření z přezkumu. U dotace či návratné výpomoci prověř program, žádost, oprávněný orgán, veřejnoprávní smlouvu, zveřejnění, účel a vyúčtování, porušení kázně, odvody a řešení sporu. Veřejnou podporu, de minimis, blokové výjimky a služby obecného hospodářského zájmu ověř podle konkrétního příjemce a činnosti.

U příspěvkové organizace, obecní společnosti a svazku obcí posuď zakládací dokumenty, svěřený majetek, kontrolu a vztah k zadávání včetně in-house podmínek. U referenda zkoumej otázku, přípravný výbor, podpisy, přípustnost, vyhlášení, platnost a závaznost; lhůty soudní ochrany nezaměňuj s politickým jednáním. U petic, shromáždění, poplatků, obecní policie, bytů, škol a veřejných služeb urč konkrétní proces, nikoli univerzální stížnost.

## Výstup pro rozhodnutí

Dodej tabulku krok–orgán–právní opora–podklad–lhůta–zveřejnění, konkrétní usnesení, smlouvu či podání podle zadání a oddělené riziko neplatnosti, dozoru, odvodu a odpovědnosti. U zastupitelů, úředníků a obce odliš civilní, pracovněprávní, veřejnomocenskou a trestní odpovědnost i případný regres. Rešeršuj v CODEXIS i nejsilnější protiargument a srovnatelnou praxi konkrétního senátu, je-li zadána. Rozpočet obsahuje skutečné samostatné návrhy a použitelné sazby, smluvní varianta přípustnou ochranu klienta a doložené ekonomické či daňové předpoklady.
