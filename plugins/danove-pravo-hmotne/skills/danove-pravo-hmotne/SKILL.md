---
uuid: b4ee9117-7b62-418b-a588-9595859e419b
name: danove-pravo-hmotne
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Daňové právo hmotné ČR"
    summary: "Daň z příjmů FO a PO, DPH včetně odpočtu, reverse charge a řetězových podvodů, daň z nemovitých věcí, daňová rezidence a smlouvy o zamezení dvojího zdanění, převodní ceny, zneužití práva, daňové aspekty transakcí a přeměn, zaměstnanec × OSVČ, kryptoaktiva."
    examplePrompts:
      - "Finanční úřad odepřel klientovi odpočet DPH, protože dodavatel v řetězci neodvedl daň. Jaké jsou podmínky vědomostního testu a co musíme prokázat?"
      - "Klient prodává byt, který vlastnil 4 roky a rok v něm bydlel. Je příjem osvobozen a jak funguje časový test po novele?"
      - "Jednatel žije půl roku v Rakousku. Kde je daňovým rezidentem a jak se zdaní odměna jednatele podle smlouvy o zamezení dvojího zdanění?"
  en:
    displayName: "Czech Substantive Tax Law"
    summary: "Personal and corporate income tax, VAT including deduction, reverse charge and chain fraud, property tax, tax residence and double-tax treaties, transfer pricing, abuse of law, tax aspects of transactions and restructurings, employee vs. contractor, cryptoassets."
    examplePrompts:
      - "The tax office denied my client's VAT deduction because a supplier in the chain failed to pay. What are the knowledge-test conditions and what must we prove?"
      - "A client sells a flat owned for 4 years and lived in for one year. Is the income exempt and how does the holding-period test work after the amendment?"
      - "A managing director lives half the year in Austria. Where is he tax resident and how is his remuneration taxed under the double-tax treaty?"
  sk:
    displayName: "Daňové právo hmotné ČR"
    summary: "Daň z príjmov FO a PO, DPH vrátane odpočtu, reverse charge a reťazových podvodov, daň z nehnuteľností, daňová rezidencia a zmluvy o zamedzení dvojitého zdanenia, transferové oceňovanie, zneužitie práva, daňové aspekty transakcií a premien, zamestnanec × SZČO, kryptoaktíva."
    examplePrompts:
      - "Finančný úrad odoprel klientovi odpočet DPH, lebo dodávateľ v reťazci neodviedol daň. Aké sú podmienky vedomostného testu a čo musíme preukázať?"
      - "Klient predáva byt, ktorý vlastnil 4 roky a rok v ňom býval. Je príjem oslobodený a ako funguje časový test po novele?"
      - "Konateľ žije pol roka v Rakúsku. Kde je daňovým rezidentom a ako sa zdaní odmena konateľa podľa zmluvy o zamedzení dvojitého zdanenia?"
description: 'Použij pro hmotné české zdanění: příjmy FO a PO, DPH, osvobození a časové testy, nemovitosti, podíly, kryptoaktiva, náklady, odpisy, rezidence, dvojí zdanění, převodní ceny, zneužití práva, podvody a ručení u DPH, zaměstnanec versus OSVČ, odměňování, přeměny a holdingy, insolvenční a trestní daňové souvislosti. Samostatnou procesní obranu směruj do skillu správního a daňového řízení. Právní zdroje pouze nativním CODEXIS.'
---

# Daňové právo hmotné ČR

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

## Oborový postup: hmotné daňové právo

### Poplatník, období a otázky
Urči konkrétního klienta, jeho roli a skutečný hospodářský cíl. Rozliš fyzickou a právnickou osobu, rezidenta a nerezidenta, zaměstnance a podnikatele, holding, fond, svěřenský fond, SVJ, spolek a obec. Přiřaď daň, zdaňovací období, druh příjmu či plnění, účetní režim a cizí prvek. Rozliš plánování, tvrzení daně, kontrolu a spor. Procesní obranu koordinuj s příslušným oborovým postupem, ale neztrácej hmotněprávní otázku.

V nativním CODEXIS ověř rozhodné znění pro každou daňovou událost a přechodná pravidla podle nabytí, převodu, uskutečnění plnění, přijetí příjmu či vzniku nákladu. Stejná transakce nemusí mít totožný okamžik v různých daních. Vyhledej související prováděcí předpisy, mezinárodní smlouvu, protokoly a unijní pravidla. Metodiky, koordinační závěry a účetní standardy dostupné v CODEXIS odliš od zákona.

### Kontrola skutečného důvodu a realizace
U časování transakce eviduj odděleně, kdo navrhl termín, kdo požaduje změnu ceny a jaký motiv je doložen. Požadavek na slevu za odklad není požadavkem kupujícího na odklad. Skutečný daňový motiv nenahrazuj vymyšleným obchodním důvodem a doložený hospodářský důvod nezamlčuj. U každého faktu zachovej původ, stranu a stav doložení.

Závěrečný checklist znovu porovnej s původními podklady. Každý krok „zachovat“, „doložit“ nebo „potvrdit“ nesmí předpokládat neexistující událost či listinu. Není-li známo, kdo odklad navrhl, požaduj ověření původní komunikace, nikoli dodatečné vytvoření historického důvodu. Stejná podmíněnost musí zůstat v klientském shrnutí, smlouvě i přílohách. Podpis, účinnost převodu, zápis, platbu a oznámení drž jako samostatné budoucí nebo doložené stavy.

### Příjmy fyzických osob
Ověř rezidenci a smluvní řešení souběhu rezidencí podle celých podmínek, nikoli samotného občanství či evidenční adresy. Klasifikuj zaměstnání a orgánovou odměnu, podnikání, kapitálové příjmy, nájem a ostatní příjmy. Zahrň benefity, vozidla, stravování, dohody mimo pracovní poměr, autorské honoráře, spolupracující osoby, paušální výdaje a paušální režim. Každé osvobození posuzuj samostatně: nemovitost, bydlení a bytová potřeba, podíl, cenný papír, movitá věc, kryptoaktivum, dar, dědictví, důchod a náhrada újmy.

Zjisti rozhodné časové a hodnotové testy i oznamovací povinnost bez přenášení starých limitů do jiného roku. Odděl příjem od zisku a osvobození od povinnosti oznámit. Prověř nabývací cenu, oceňovací pravidla, použití výdajů, sazbu, slevy, odpočty, ztrátu a zálohy. U kryptoaktiv rozliš prodej, směnu, těžbu a poskytovanou službu podle skutečného modelu.

### Právnické osoby a strukturování
Navazuj účetní výsledek na daňový základ. Pro každý výdaj ověř reálnost, souvislost s příjmy, prokázání a zákonnou výjimku. Zahrň odpisy, technické zhodnocení versus opravu, rezervy, opravné položky, výzkum a vývoj, investiční pobídky, dary a sponzoring. U skupin prověř osvobození účastí, skutečného vlastníka příjmu, srážku a zajištění daně, převodní ceny, propojení, dokumentaci, kapitalizaci, výpůjční výdaje, CFC, exit tax, hybridní nesoulady a dorovnávací daň.

U přeměn, vkladu či prodeje závodu, likvidace, holdingů a fondů prověř kontinuitu odpisů, ztrát a nabývacích cen, hospodářskou podstatu a možnost závazného posouzení. Neutralitu ani zneužití práva neodvozuj pouze z daňové úspory. Odděl zastření, převodní ceny a zneužití práva včetně vlastních podmínek a důkazního břemene. Porovnej smluvní varianty podle čistého výnosu, slevy, financování, daní a doložených nákladů; vypočti hranici výhodnosti.

### DPH
Rozliš osobu, registraci a její okamžik, identifikovanou osobu, skupinu, předmět, místo a uskutečnění plnění. U odpočtu zkoumej hmotné a formální podmínky, ekonomické použití, doklady, lhůtu, poměr, krácení, vyrovnání a úpravu. Odděl neprokázané plnění, účast na podvodu, vědomostní test a ručení; každé větvi přiřaď důkazní břemeno. Zjisti konkrétní rozumná opatření klienta bez fingování kontroly dodavatele.

Prověř přenesení daňové povinnosti, stavby, pozemky, dokončení a podstatnou změnu, první dodání, nájem, volbu zdanění, sazby a přílohy. Historický test osvobození nepřenášej na nové plnění. Zahrň finanční, zdravotní, sociální a vzdělávací služby, opravy základu, nedobytné pohledávky, kontrolní a souhrnné hlášení, OSS/IOSS, dovoz, vývoz, přepravu v řetězci, poukazy, zálohy, závod a zrušení registrace.

### Další daně, práce, mezinárodní a trestní souvislosti
Podle zadání ověř daň z nemovitých věcí včetně místních koeficientů, silniční, spotřební, energetické a hazardní daně. U odměňování porovnej skutečnou závislou práci, orgánovou funkci, podnikání, ESOP, práci z domova, cestovní náhrady a vysílání; smluvní název není důkaz režimu. Mezinárodně prověř stálou provozovnu, přičítání zisku, jednotlivé druhy příjmů, metodu zápočtu či vynětí, rezidenční doklady, MLI, MAP, DAC a výměnu údajů.

U sankcí a trestních rizik samostatně zkoumej penále, úroky, opožděné tvrzení, opravné tvrzení, zkrácení a neodvedení daně, účinnou lítost, odpovědnost právnické osoby, zajištění a souběh sankcí. Nenavrhuj fiktivní doklady ani umělé řetězce.

### Výstup
Dodej závěr pro každou daň, tabulku podmínka–fakt–důkaz–pramen–riziko, ověřené výpočty s mezikroky a realizační plán. Zákonnou lhůtu přiznání či oznámení odvoď z použitelného procesního pravidla včetně způsobu podání, počátku, kalendáře a svátků; elektronická forma sama neprokazuje prodloužení. Interní rezervu označ zvlášť. Datum rešerše nezaměňuj s historickým nebo simulovaným rozhodným dnem.
