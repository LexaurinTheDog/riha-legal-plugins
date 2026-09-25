---
uuid: 5d95ddc3-4a55-4470-93cb-fdd7b4bc29df
name: obeti-trestnych-cinu
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Oběti trestných činů a poškození ČR"
    summary: "Práva obětí dle zákona 45/2013, zvlášť zranitelná oběť, poškozený v trestním řízení, adhezní nárok na náhradu škody a nemajetkové újmy, peněžitá pomoc státu, předběžná a ochranná opatření, ochrana při výslechu, důvěrník a zmocněnec, stížnost proti odložení, narovnání a mediace, domácí a sexuální násilí."
    examplePrompts:
      - "Klientka byla napadena partnerem, policie věc odložila jako přestupek. Jak podat stížnost proti odložení a jaká má klientka práva jako oběť domácího násilí?"
      - "Klient utrpěl při loupeži těžké zranění, pachatel je stíhán. Jak uplatnit nárok na bolestné, ztížení společenského uplatnění a ušlý výdělek v adhezním řízení a jak požádat o peněžitou pomoc státu?"
      - "Rodiče znásilněné nezletilé chtějí, aby dcera nemusela vypovídat před obžalovaným a aby byl zástupce bezplatný. Co lze v trestním řízení zajistit?"
  en:
    displayName: "Czech Crime Victims & Injured Parties"
    summary: "Victims' rights under Act 45/2013, especially vulnerable victims, injured party in criminal proceedings, adhesion claims for damages and non-pecuniary harm, state financial assistance, preliminary and protective measures, interview protection, confidant and counsel, complaints against dismissal, settlement and mediation, domestic and sexual violence cases."
    examplePrompts:
      - "My client was assaulted by her partner and the police dismissed the case as a misdemeanour. How to file a complaint against the dismissal and what rights does she have as a domestic-violence victim?"
      - "My client suffered serious injury in a robbery and the offender is prosecuted. How to claim pain, loss of amenity and lost earnings in the adhesion procedure and how to apply for state financial assistance?"
      - "Parents of a raped minor want her not to testify in front of the accused and want free counsel. What can be secured in the criminal proceedings?"
  sk:
    displayName: "Obete trestných činov a poškodení ČR"
    summary: "Práva obetí podľa zákona 45/2013, obzvlášť zraniteľná obeť, poškodený v trestnom konaní, adhézny nárok na náhradu škody a nemajetkovej ujmy, peňažná pomoc štátu, predbežné a ochranné opatrenia, ochrana pri výsluchu, dôverník a splnomocnenec, sťažnosť proti odloženiu, narovnanie a mediácia, domáce a sexuálne násilie."
    examplePrompts:
      - "Klientka bola napadnutá partnerom, polícia vec odložila ako priestupok. Ako podať sťažnosť proti odloženiu a aké má klientka práva ako obeť domáceho násilia?"
      - "Klient utrpel pri lúpeži ťažké zranenie, páchateľ je stíhaný. Ako uplatniť nárok na bolestné, sťaženie spoločenského uplatnenia a ušlý zárobok v adhéznom konaní a ako požiadať o peňažnú pomoc štátu?"
      - "Rodičia znásilnenej maloletej chcú, aby dcéra nemusela vypovedať pred obžalovaným a aby bol zástupca bezplatný. Čo možno v trestnom konaní zabezpečiť?"
description: 'Použij pro zastupování obětí a poškozených: zvláštní zranitelnost, ochranu a informace, důvěrníka a zmocněnce, šetrný výslech, bezpečnostní opatření, adhezní nárok, peněžitou pomoc, souhlas s trestním stíháním, stížnosti, náklady, restorativní řešení a výkon náhrady. Obhajobu obviněného řeší samostatný skill. Právní zdroje jen nativní CODEXIS v aplikaci.'
---

# Oběti trestných činů a poškození

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

## Bezpečí, status a cíl klienta

Urči, zda klientem je oběť, zvlášť zranitelná oběť, poškozený člověk či společnost, pozůstalý, zákonný zástupce dítěte nebo pouze oznamovatel. Tyto statusy a jejich podmínky ověř zvlášť; procesní nárok není podmínkou všech forem ochrany a pomoci. Zjisti bezprostřední ohrožení, potřebu bezpečného kontaktu, jazykové či zdravotní bariéry, fázi řízení a již učiněné úkony. Bezpečnost, procesní práva, adhezní nárok a státní peněžitou pomoc veď jako oddělené větve.

Z podkladů zaznamenej čas činu, oznámení, doručení rozhodnutí, poučení, zahájení dokazování a přesný obsah již uplatněných nároků. Nedomýšlej diagnózu, trvalé následky, souhlas ani uskutečněný kontakt. Citlivé údaje v pracovních výstupech minimalizuj, v podání však zachovej právně potřebnou identifikaci. Přání rodiny nezaměňuj za vůli oběti a prověř kolizi jejího zástupce.

## Nativní právní mapa

V CODEXIS vyhledej zákon o obětech, trestní řád, občanský a trestní zákoník, policii, zvláštní soudní řízení, ochranu svědků, sociálně-právní ochranu dětí, sociální služby, probační a mediační službu a pojištění provozu vozidel. Podle věci připoj unijní pravidla práv obětí, přeshraničního odškodnění a ochranného příkazu a relevantní úmluvy. U právní kvalifikace, procesního úkonu a náhrad odliš časová znění; výčet zvlášť zranitelných, částky a lhůty načti včetně výjimek. Nedostupnou metodiku, formulář nebo podklad nepřebírej z externího webu.

## Oznámení, informace a účast

Prověř formu oznámení, žádost o vyrozumění, nahlížení, navrhování důkazů a účast při úkonech. U odložení, postoupení, zastavení či nečinnosti nejprve urč oprávněnou osobu, skutečný prostředek, adresáta a lhůtu. Podnět dohledu nepředstavuj jako náhradu včasné stížnosti. Argument účinného vyšetřování spoj s konkrétně opomenutým úkonem a odpovídající nativně ověřenou judikaturou.

Odděl důvěrníka, smluvního zmocněnce, ustanoveného zmocněnce, bezplatnou odbornou pomoc a sníženou odměnu. U každého zjisti podmínky, fázi, rozsah, žádost a doklady. U dítěte a kolize rodiče ověř zvláštní zastoupení. U souhlasu s trestním stíháním prověř vymezené činy, vztah osob, účinky odmítnutí a zpětvzetí i výjimky závislosti nebo nátlaku; nevytvářej tlak na oběť.

U výslechu zkoumej individuální potřeby, školení vyslýchajícího, žádost o jeho pohlaví, záznam, opakování, účast odborníka, konfrontaci, rekognici a následnou použitelnost výpovědi. Šetrnost není automatické oprávnění slíbit, že další výslech nikdy nenastane. Připrav prohlášení o dopadu činu z klientových údajů, nikoli literárně doplněných traumat.

## Ochranná opatření

Rozliš policejní vykázání, civilní ochranu před domácím násilím, trestní předběžná opatření, podnět k vazbě, utajení totožnosti a zvláštní ochranu svědka. Pro každý nástroj zjisti podmínky, fázi, oprávněného navrhovatele, orgán, lhůtu, trvání, prodloužení a důsledek porušení. Vypočti návaznost ochrany, aby nevznikla neoznačená mezera. Žádost o informaci o propuštění či útěku a ochranu před kontaktem v budově soudu řeš samostatně.

U domácího a sexuálního násilí, stalkingu, nenávistného činu, obchodování s lidmi a nezletilé oběti prověř zvláštní pravidla a případné rodinné či pobytové souvislosti. U přeshraniční ochrany ověř působnost instrumentu. Doporučení odborné a bezpečnostní pomoci neoznačuj za skutečně sjednanou službu.

## Nároky a státní pomoc

Rozepiš adhezní nárok po osobách a složkách: věcná škoda, ušlý výdělek, léčení a péče, bolest, ztížení společenského uplatnění, další nemajetková újma, samostatné osobnostní zásahy, pozůstalí a obohacení. Stejný následek neodškodňuj dvakrát a z terapie nevyvozuj trvalý stav. Ověř metodu ocenění a potřebný odborný podklad; pracovní úraz a civilní zdraví nezaměňuj. Uveď důvod, částku či přesně neznámý vstup, důkaz, úroky, případnou solidaritu a stav uplatnění.

Zkontroluj rozhodný okamžik uplatnění v přípravném řízení, hlavním líčení a při dohodě o vině a trestu. Promlčení posuzuj zvlášť pro každou složku a pouze skutečně uplatněný rozsah; neznámou budoucí újmu nevymýšlej kvůli úplnosti. Prověř zajištění majetku, přiznání, odkaz na civilní řízení, odvolací oprávnění a samostatnou náhradu nákladů zmocněnce.

U státní pomoci ověř oprávněnou osobu, následek, podmínky oznámení, výši a limity, subjektivní a objektivní běh včetně zvláštní ochrany nezletilých. Peněžitá pomoc není plnou civilní náhradou. Při odmítnutí nejprve načti zvláštní vyloučení opravných prostředků; automaticky nenavrhuj rozklad, prověř soudní přezkum a osvobození. Zákonný přechod nároku na stát odliš od smluvního postoupení a od vrácení pomoci.

## Dohoda, výkon a výstup

U narovnání, mediace a podmíněného zastavení posuď dobrovolnost, bezpečí, skutečné uspokojení, zajištění a kontrolu budoucího plnění. Návrh dohody nesmí neurčitě rušit další nároky. Koordinuj pojistitele, adhezi a civilní spor bez dvojího plnění; přímý pojistný nárok ověř podle použitelného zákona. U výkonu a insolvence zjisti titul, zbytek nároku, přihlášení a rozsah případného osvobození dlužníka. Dodej požadované podání, ochranný plán, tabulku práv a nároků, přesný rozpočet a nejbližší doloženou lhůtu; připravené a podané vždy odliš.
