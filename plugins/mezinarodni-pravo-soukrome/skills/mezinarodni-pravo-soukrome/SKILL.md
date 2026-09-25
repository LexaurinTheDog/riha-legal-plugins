---
uuid: 1a3eb1c5-cdd8-4dbf-8eaf-f75e9f969525
name: mezinarodni-pravo-soukrome
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Mezinárodní právo soukromé ČR"
    summary: "Přeshraniční spory a smlouvy - pravomoc soudů a rozhodné právo podle nařízení EU a ZMPS, doručování a dokazování do ciziny, uznání a výkon cizích rozhodnutí a rozhodčích nálezů, ověřování listin, doložky o volbě práva a soudu."
    examplePrompts:
      - "Německý odběratel nezaplatil faktury české firmě; ve smlouvě není nic o soudu ani právu. Kde žalovat a podle jakého práva?"
      - "Máme pravomocný rozsudek českého soudu proti dlužníkovi s majetkem v Rakousku a ve Velké Británii. Jak ho vykonat?"
      - "Klient se rozvedl na Ukrajině a chce se v ČR znovu oženit. Co je třeba k uznání rozvodu?"
  en:
    displayName: "Czech Cross-border Private Law"
    summary: "Cross-border disputes and contracts - jurisdiction and applicable law under EU regulations and the PIL Act, service and evidence abroad, recognition and enforcement of foreign judgments and awards, legalisation of documents, choice-of-law and forum clauses."
    examplePrompts:
      - "A German buyer has not paid invoices to a Czech company; the contract says nothing about courts or law. Where to sue and under which law?"
      - "We hold a final Czech judgment against a debtor with assets in Austria and the UK. How to enforce it?"
      - "My client divorced in Ukraine and wants to remarry in Czechia. What is needed to have the divorce recognised?"
  sk:
    displayName: "Medzinárodné právo súkromné ČR"
    summary: "Cezhraničné spory a zmluvy z pohľadu ČR - právomoc súdov a rozhodné právo podľa nariadení EÚ a ZMPS, doručovanie a dokazovanie do cudziny, uznanie a výkon cudzích rozhodnutí a rozhodcovských nálezov, overovanie listín, doložky o voľbe práva a súdu."
    examplePrompts:
      - "Nemecký odberateľ nezaplatil faktúry českej firme; v zmluve nie je nič o súde ani práve. Kde žalovať a podľa akého práva?"
      - "Máme právoplatný rozsudok českého súdu proti dlžníkovi s majetkom v Rakúsku a vo Veľkej Británii. Ako ho vykonať?"
      - "Klient sa rozviedol na Ukrajine a chce sa v ČR znovu oženiť. Čo treba na uznanie rozvodu?"
description: 'Použij pro cizí prvek: pravomoc a příslušnost, rozhodné právo, volbu soudu a práva, souběžná řízení, CISG, doručování a dokazování v cizině, uznání a výkon rozsudků i nálezů, evropské procesní nástroje, apostilu, překlady, sankce a přeshraniční rodinné, dědické či obchodní věci. Právní prameny výhradně nativním CODEXIS; oborové meritum spoj s odpovídajícím skillem.'
---

# Mezinárodní právo soukromé

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

## Cizí prvek a oddělené otázky

Z dodaných podkladů sestav země a vazby: sídla či bydliště stran, obvyklý pobyt, státní příslušnost, místo plnění, vzniku škody a majetku, právní forma stran a jejich spotřebitelské, pracovní či pojistné postavení. Zapiš uzavření smlouvy, škodní událost, zahájení každého řízení, vydání a doručení rozhodnutí. Pojmy bydliště a obvyklého pobytu nepovažuj automaticky za totožné. Zjisti klientův cíl a místo prakticky dosažitelného výkonu. České fórum ani český advokát samy neurčují české hmotné právo.

Odděl pravomoc a příslušnost, rozhodné právo, hmotněprávní režim, věcné účinky, proces doručování a dokazování, uznání a výkon a formu listin. Každá otázka může mít jiný pramen a rozhodný okamžik. Nejprve vyhledej pravidla věcné, osobní, územní a časové působnosti i vzájemné přednosti pramenů; nepoužívej mechanické pořadí bez prověření vztahových klauzulí.

## Prameny a dostupnost

Nativním CODEXIS rešeršuj podle otázky Brusel I bis, Luganskou úmluvu, Řím I a Řím II, zákon o mezinárodním právu soukromém, CISG, evropské procesní nástroje, rodinná a dědická nařízení, insolvenční a majetkové režimy manželů, Haagské úmluvy, Newyorskou úmluvu, přepravní úmluvy a bilaterální právní pomoc. Zjisti konkrétní smluvní státy, výhrady, prohlášení a přechodná ustanovení pro rozhodné období v dostupném nativním obsahu. Pro Spojené království neodvozuj výsledek pouze z označení Brexit. Chybí-li potřebná informace nebo text cizího práva, přesně označ mezeru; nepřejdi k externím atlasům, databázím či webům.

## Pravomoc a rozhodné právo

U fóra prověř obecnou, zvláštní a výlučnou příslušnost, ochranu slabší strany, sjednanou prorogaci, souhlas s doložkou ve všeobecných podmínkách a účinky procesní účasti bez námitky. Který soud je skutečně určen, pro jaké nároky a s jakou výlučností? U souběžných řízení zmapuj jejich předmět, účastníky, okamžiky zahájení a případná přednostní pravidla doložky. Nezaměňuj související řízení za totožnou věc.

U smlouvy prověř platnost a rozsah volby práva, náhradní určení bez volby, charakteristické plnění, užší vazbu, imperativní normy, ochranu zaměstnance či spotřebitele a výhradu veřejného pořádku. U mimosmluvních nároků zkoumej zvlášť místo škody a zvláštní pravidla výrobku, soutěže, životního prostředí a duševního vlastnictví. Zjisti, které právo řídí formu, výklad, promlčení, způsobilost, zastoupení a věcné účinky. Zpětný odkaz použij pouze po ověření jeho přípustnosti.

U smíšené smlouvy identifikuj skutečná plnění a rozsah CISG, její výjimky a případné vyloučení podle textu i doložených okolností. Nepředpokládej ani to, že volba práva smluvního státu CISG vylučuje, ani že je vždy možný pouze výslovný opt-out. Právní kvalifikace nesmí vzniknout pouze z názvu doložky.

## Vedení řízení, listiny a výkon

Pro doručování zjisti použitelný nástroj, přípustný způsob, přijímající orgán, formulář, jazyk a právo odmítnout. Odděl předání písemnosti, doložené doručení a právní účinky. U dokazování ověř dožádání, přímý důkaz, videokonferenci, překlady a procesní práva. Vnitrostátní fikci ani e-mailovou adresu nepřenášej automaticky do cizího režimu.

U uznání rozliš běžné civilní rozhodnutí, osobní stav, rodinnou věc a rozhodčí nález. Vyhledej potřebu samostatného výroku či prohlášení vykonatelnosti, osvědčení, originálů, překladu a doručení. Zhodnoť důvody odepření, veřejný pořádek, možnost účasti, neslučitelná rozhodnutí a vzájemnost, pokud ji daný režim vyžaduje. Porovnej evropský platební rozkaz, drobné nároky, exekuční titul a obstavení účtů podle ověřených podmínek, limitů, odporu a jistoty. U rozvodu ze třetího státu neoznamuj automaticky trvání manželství bez prověření uznání a výjimek.

U listin ověř apostilu, superlegalizaci či osvobození, oprávněný orgán, překlad, ekvivalenci veřejné listiny, plnou moc a zahraniční výpis. Úřední ověření podpisu není automatickým potvrzením všech hmotněprávních podmínek. Údaje cizí společnosti ponech podle dodaných listin s vyznačením aktuálnosti.

## Smlouvy a výstup

Připrav oddělené a navazující doložky práva, fóra či arbitráže, rozhodného jazyka, měny a kurzu, dodacích podmínek, doručování, zajištění a vypořádání. Prověř sankční a exportní překážky, ochranu údajů při přeshraničním předávání a vymahatelnost zajištění v cílovém státě; neslibuj úplný screening bez dat. Omezení odpovědnosti a ekonomicko-daňovou výhodnost posuzuj podle použitelného práva a doložených vstupů.

U rodiny, únosu dítěte, výživného, dědictví, insolvence, vysílání zaměstnanců, přeměn, přepravy a cizineckých souvislostí připoj oborové otázky, ale zachovej tuto kolizní mapu. Dodej tabulku otázka–pramen–rozhodný okamžik–fórum–právo–důkaz, harmonogram úkonů a požadovaný návrh či smlouvu. Při souběžném zahraničním řízení uveď bezodkladné ochranné kroky a potřebu místní pomoci jako doporučení, nikoli externí rešeršní cestu; neověřenou zahraniční lhůtu nepodávej jako jistou.
