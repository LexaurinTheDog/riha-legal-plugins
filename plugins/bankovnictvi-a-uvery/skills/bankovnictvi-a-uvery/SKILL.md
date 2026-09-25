---
uuid: f3bbcce5-dc2e-4a38-b673-952147fcb5d1
name: bankovnictvi-a-uvery
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Bankovnictví a úvěry ČR"
    summary: "Smlouvy o úvěru a zápůjčce, zákon o spotřebitelském úvěru a posouzení úvěruschopnosti, předčasné splacení a prodlení, hypotéky a zajištění, ručení a akcesorická zajištění, platební služby a neautorizované transakce, bankovní tajemství a blokace účtů, finanční arbitr, dohled a licence ČNB, nebankovní poskytovatelé."
    examplePrompts:
      - "Nebankovní společnost půjčila klientovi 300 000 Kč bez ověření příjmů. Lze namítat neplatnost smlouvy pro neposouzení úvěruschopnosti a co se pak vrací?"
      - "Klient chce předčasně splatit hypotéku s fixací a banka požaduje náhradu nákladů 150 000 Kč. Jaký je zákonný limit po novele?"
      - "Z účtu klienta odešla platba, kterou nezadal, po phishingu. Musí banka vrátit peníze a v jaké lhůtě, a kdy se uplatní hrubá nedbalost klienta?"
  en:
    displayName: "Czech Banking & Credit Law"
    summary: "Loan and credit agreements, consumer credit act and creditworthiness assessment, early repayment and default, mortgages and security packages, guarantees, payment services and unauthorised transactions, bank secrecy and account freezes, financial arbiter, ČNB supervision and licensing, non-bank lenders."
    examplePrompts:
      - "A non-bank lender lent my client CZK 300,000 without verifying income. Can we claim the contract is void for failure to assess creditworthiness and what is then returned?"
      - "My client wants to repay a fixed-rate mortgage early and the bank demands CZK 150,000 in costs. What is the statutory cap after the amendment?"
      - "A payment left my client's account after phishing without her authorising it. Must the bank refund, by when, and when does the client's gross negligence apply?"
  sk:
    displayName: "Bankovníctvo a úvery ČR"
    summary: "Zmluvy o úvere a pôžičke, zákon o spotrebiteľskom úvere a posúdenie úverovej schopnosti, predčasné splatenie a omeškanie, hypotéky a zabezpečenie, ručenie, platobné služby a neautorizované transakcie, bankové tajomstvo a blokácie účtov, finančný arbiter, dohľad a licencie ČNB, nebankoví poskytovatelia."
    examplePrompts:
      - "Nebanková spoločnosť požičala klientovi 300 000 Kč bez overenia príjmov. Možno namietať neplatnosť zmluvy pre neposúdenie úverovej schopnosti a čo sa potom vracia?"
      - "Klient chce predčasne splatiť hypotéku s fixáciou a banka požaduje náhradu nákladov 150 000 Kč. Aký je zákonný limit po novele?"
      - "Z účtu klienta odišla platba, ktorú nezadal, po phishingu. Musí banka vrátiť peniaze a v akej lehote, a kedy sa uplatní hrubá nedbanlivosť klienta?"
description: 'Použij pro banky, úvěry, zápůjčky a platební služby v ČR: spotřebitelský a podnikatelský úvěr, hypotéky, úvěruschopnost, RPSN, předčasné splacení, prodlení, zajištění, ručení, notářské zápisy, neautorizované platby, phishing, účty, bankovní tajemství, ČNB, finanční arbitr, BNPL, leasing, fintech, kryptoaktiva a insolvenční souvislosti. Právní zdroje jen nativním CODEXIS.'
---

# Bankovnictví a úvěry ČR

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

## Oborový postup: bankovnictví, úvěry a platby

### Kvalifikace a podklady
Urči, zda klient vystupuje jako dlužník, věřitel, ručitel, manžel, poskytovatel či zprostředkovatel. Rozliš spotřebitele, podnikatele a obec podle skutečného účelu jednání. Eviduj banku, nebankovní subjekt, platformu nebo soukromého půjčitele a povahu produktu: úvěr, zápůjčka, hypotéka, kontokorent, karta, leasing, stavební spoření, odložená platba, P2P, syndikovaný či akviziční úvěr. Z podkladů sestav osu smlouvy, čerpání, fixace, oznámení nové sazby, žádosti o splacení, skutečného splacení, prodlení a vymáhání. Ke každé právní otázce vyhledej v CODEXIS vlastní časový režim včetně předchozí úpravy a přechodu.

### Vznik spotřebitelského závazku
Ověř působnost zákona o spotřebitelském úvěru, výjimky, oprávnění poskytovatele a zprostředkovatele, předsmluvní informace, poradenství a odměnu. Vyžádej smlouvu, informační formulář, podklady o příjmech, výdajích a ověření úvěruschopnosti, sazebník i splátkový kalendář. Samostatně zkoumej kvalitu posouzení úvěruschopnosti, písemnou formu a obsah smlouvy, správnost RPSN a celkových nákladů. U každého porušení načti konkrétní následek, možnost přezkumu z úřední povinnosti, vypořádání jistiny a důkazní břemeno. Nezaměňuj neplatnost pro úvěruschopnost se sankcemi informačních vad a nevkládej univerzální prekluzi námitky. Prověř odstoupení, vázaný úvěr, dobu na rozmyšlenou, směnky, rozhodčí doložky a přiměřenost zajištění.

### Předčasné splacení a ekonomické porovnání
Nejprve zjisti druh úvěru a rozhodný přechodný režim; poté všechny bezplatné případy, účelné náklady a stropy. Ověř skutečný spouštěč informačního okna, nikoli jen datum konce fixace. U zákonného výpočtu odděl administrativní náklady, smluvní úrok, referenční úrok a jejich rozdíl. Z úplného ustanovení ověř pořadí operací a místo použití nezáporného omezení: záporný rozdíl neodstraňuj před sečtením, pokud zákon stanoví omezení až výsledného základu. Prověř částečné splacení, rozhodnou skupinu referenční sazby a období. Datum odhadu nemusí být rozhodným datem skutečného splacení. Nedostupnou sazbu nedoplňuj externě.

Porovnej varianty splacení, čekání a refinancování včetně úroků, slev, poplatků, výnosu volných prostředků a doložených nákladů. Ukaž hranici výhodnosti a citlivost na neznámé vstupy. Unijní judikaturu o snížení nákladů nepřenášej bez testu na odlišný úvěrový produkt.

### Prodlení, smluvní volnost a zajištění
Ověř podmínky změn sazeb, zesplatnění, předchozí výzvy, dodatečné doby, sankčních limitů a postoupení. Odděl jednotlivé splátky, jistinu, smluvní úrok, úrok z prodlení, pokutu a náklady. Zkoumej lichvu, dobré mravy, adhezní podmínky a moderaci podle role stran; nepředpokládej, že podnikatelský vztah vylučuje každou ochranu.

U zástav nemovitostí, podílů, pohledávek, movitých věcí a závodu ověř vznik, pořadí, zápis, výkon a vypořádání. Zahrň ručení, finanční záruku, zajišťovací převod, srážky ze mzdy, směnku a notářský zápis. Samostatně posuď ochranu ručitele, manžela a SJM. Prověř cross-default, kovenanty, mezivěřitelské dohody, podřízenost, refinancování a zachování zajištění; v insolvenci přihlášku, neúčinnost zajištění a započtení.

### Platby a účty
Rozliš autorizaci od technické autentizace, podvod plátce, hrubou nedbalost, neautorizovanou a nesprávně provedenou platbu i podvodně vyvolaný autorizovaný převod. Vyžádej původní komunikaci, logy, varování, okamžik oznámení a údaje o silném ověření. Ověř rozdělení důkazního břemene, vrácení částky, výjimky, spoluúčast, časové limity a povinnost dohledání. Samotné použití kódu nevydávej za úplný právní závěr. Zahrň inkaso, otevřené bankovnictví, platební brány, elektronické peníze, ochranu svěřených prostředků, ověření příjemce a přeshraniční platby.

U blokace určuj zvlášť exekuci, AML, sankce, trestní zajištění a insolvenci. Ověř chráněný a základní účet, disponenty, nezletilé, účet zemřelého, právo na informace, bankovní tajemství a jeho výjimky. Změnu či výpověď účtu posuzuj podle smlouvy i konkrétního zákonného režimu.

### Regulace, spory a výstup
Prověř licenční a odborné podmínky, hypoteční makroobezřetnostní omezení, dohled ČNB, pojištění vkladů a řešení krize bank. U fintech, MiCA, DORA a nových úvěrových či platebních pravidel zjisti skutečnou použitelnost, nikoli stav legislativního návrhu. Stav povolení z nedodaných registrů nepředpokládej.

Dodej mapu nároků s důkazním břemenem, lhůtou a finančním dopadem. Samostatně ověř působnost finančního arbitra, soudní přezkum jeho rozhodnutí, reklamaci a podnět dohledu; podnět není přiznání peněz. Porovnej restrukturalizaci, refinancování a oddlužení. Požadovanou smlouvu, výzvu či petit skutečně sepiš, náklady řízení počítej odděleně od nákladů úvěru. Nenavrhuj zastření věřitele ani nepravdivé údaje pro úvěruschopnost.
