---
uuid: 5a185893-07b1-47f4-afdd-4a65fb787ab0
name: aml-compliance
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "AML compliance ČR"
    summary: "Povinné osoby, identifikace a kontrola klienta, skutečný majitel a PEP, sankční screening, oznámení podezřelého obchodu FAÚ, systém vnitřních zásad a školení, zvláštní povinnosti advokáta a mlčenlivost, spouštěče u nemovitostí a úschov, evidence skutečných majitelů, kontroly a sankce, AML balíček EU."
    examplePrompts:
      - "Advokát přebírá do úschovy kupní cenu 12 mil. Kč od zahraniční společnosti s nejasnou strukturou. Jaké AML povinnosti má a kdy může/musí obchod odmítnout?"
      - "Realitní kancelář dostala od FAÚ výzvu k předložení dokumentů. Co musí mít v pořádku a jaké hrozí pokuty?"
      - "Připrav checklist kontroly klienta pro s.r.o. se skutečným majitelem v evidenci a jednatelem PEP."
  en:
    displayName: "Czech AML Compliance"
    summary: "Obliged persons, customer identification and due diligence, beneficial owner and PEP checks, sanctions screening, suspicious transaction reports to FAÚ, internal policies and training, attorney-specific duties and privilege, real-estate and escrow triggers, beneficial owner register, inspections and penalties, EU AML package."
    examplePrompts:
      - "A lawyer is taking CZK 12 million purchase price into escrow from a foreign company with an unclear structure. What AML duties apply and when may or must the transaction be refused?"
      - "A real-estate agency received a request for documents from the FAÚ. What must be in order and what fines apply?"
      - "Prepare a customer due-diligence checklist for an s.r.o. with a registered beneficial owner and a PEP managing director."
  sk:
    displayName: "AML compliance ČR"
    summary: "Povinné osoby, identifikácia a kontrola klienta, konečný užívateľ výhod a PEP, sankčný screening, hlásenie podozrivého obchodu FAÚ, systém vnútorných zásad a školenia, osobitné povinnosti advokáta a mlčanlivosť, spúšťače pri nehnuteľnostiach a úschovách, evidencia skutočných majiteľov, kontroly a sankcie, AML balík EÚ."
    examplePrompts:
      - "Advokát preberá do úschovy kúpnu cenu 12 mil. Kč od zahraničnej spoločnosti s nejasnou štruktúrou. Aké AML povinnosti má a kedy môže/musí obchod odmietnuť?"
      - "Realitná kancelária dostala od FAÚ výzvu na predloženie dokumentov. Čo musí mať v poriadku a aké hrozia pokuty?"
      - "Priprav checklist kontroly klienta pre s.r.o. s konečným užívateľom výhod v evidencii a konateľom PEP."
description: 'Použij pro české AML a sankční povinnosti: povinné osoby včetně advokátů, notářů, realitních zprostředkovatelů, účetních a finančních institucí; identifikace a kontrola klienta, skutečný majitel, PEP, rizika, úschovy, hotovost, virtuální aktiva, podezřelé obchody, FAÚ a ČAK, mlčenlivost, vnitřní zásady, školení, uchovávání, kontroly a sankce, evropský AML rámec a AMLA. Právní rešerše výhradně nativním CODEXIS ve vm.codexis.ai.'
---

# AML compliance ČR

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

## Oborový postup: AML a sankce

### Role, obchod a rozsah povinností
Z podkladů určuj klienta, zastupovanou stranu, skutečný obchod, čas plánovaného nebo uskutečněného úkonu a původ informací. Odděl právní poradu, zjišťování právního postavení a zastupování v řízení od úschovy, nemovitostní transakce, správy majetku nebo založení společnosti či svěřenského fondu. V nativním CODEXIS ověř, zda konkrétní činnost činí danou osobu povinnou, jaké jsou výjimky a časová pravidla. Neodvozuj povinnost ani výjimku pouze z profesního označení. Zohledni banky, platební instituce, směnárny, poskytovatele služeb s kryptoaktivy, realitní kanceláře, auditory, poradce, účetní, obchodníky s uměním, dražebníky, hazard a další skutečně relevantní činnosti.

### Identifikace a kontrola klienta
Samostatně ověř spouštěče identifikace a kontroly: vztah, příležitostný obchod, související platby, podezření, hotovost a druh služby. U každého spouštěče zjisti rozhodný práh, výjimku, okamžik a potřebné doklady; částky nedoplňuj z instrukcí. Prověř přípustné osobní, zprostředkované, převzaté a dálkové postupy, oprávnění jednající osoby, platnost identifikačního prostředku, kopírování dokladů a auditní záznam. Fotografie dokladu sama neprokazuje splnění konkrétního zákonného postupu.

Pro kontrolu vytvoř mapu účelu obchodu, vlastnické a řídicí struktury, skutečného majitele, zdroje prostředků a případně majetku. Zjisti, jak se ověřuje struktura u trustu, nepřímého vlastnictví a zastupujících osob, jak se řeší nesrovnalost evidence a jaké jsou následky chybějícího zápisu pro korporátní práva. Podklady k faktické struktuře vyžádej od uživatele; existenci či správnost zápisu nevymýšlej. Právní pravidla a dostupnou metodiku hledej pouze v CODEXIS a rozliš jejich právní sílu.

### Rizika, PEP a třetí osoby
Vytvoř individuální profil zeměpisného, klientského, produktového a distribučního rizika. Ověř předpoklady zjednodušené a zesílené kontroly, schvalování vedením a průběžné aktualizace. U politicky exponovaných osob posuď také rodinné a blízké spolupracující osoby; u bývalé PEP zvlášť zákonnou dobu i pokračující specifické riziko. Samotné uplynutí času nenahrazuje zjištění rizik. Platbu třetí osobou prověř podle jejího vztahu k obchodu, zdroje a účelu; sama není důkazem trestné činnosti.

### Rozhodnutí o obchodu a mlčenlivost
Veď oddělené větve: uskutečnění či neuskutečnění obchodu, oznámení podezřelého obchodu, odklad příkazu a sankční zákaz plnění. Ke každé načti vlastní podmínky a výjimky. Ověř adresáta, cestu oznámení, naléhavost a běh lhůty; u advokáta prověř chráněné informace a případnou roli ČAK. Lhůtu orgánu nezaměňuj s dobou, po kterou může čekat oznamovatel. U odkladu zjisti spouštěč, přijetí oznámení, prodloužení a výjimky. Odmítnutí obchodu samo neuzavírá oznamovací větev. Odděl zákonné odrazování klienta od nepřípustného prozrazení oznámení nebo šetření.

### Sankční a organizační vrstva
Ověř osobní a územní působnost sankčních pravidel, přímé i nepřímé vlastnictví a kontrolu, sektorové zákazy, obcházení, zmrazení, oznámení, licence a výjimky pro konkrétní právní služby. Případné zahraniční vazby posuzuj jen z nativně dostupných pramenů. Není-li k rozhodnému dni dostupný úplný sankční podklad, nenahrazuj jej externím screeningem a nevydávej potvrzení bezrizikovosti.

Podle typu klienta prověř systém vnitřních zásad, hodnocení rizik, kontaktní osobu, školení, nezávislou kontrolu, skupinové politiky, whistleblowing, dobu uchovávání a GDPR. Zahrň úschovní evidenci, platební režim, nemovitosti, správu účtů a kryptoaktiva včetně pravidel předávání údajů. Evropský AML rámec a národní přechod posuzuj po jednotlivých povinnostech. Prověř i daňovou součinnost a přeshraniční oznamování, pokud souvisí se zadáním.

### Kontroly, obrana a výstup
U kontroly FAÚ, ČAK nebo ČNB ověř pravomoc, rozsah součinnosti, sankční skutkovou podstatu, zavinění či liberační podmínky, přiměřenost, nápravu, opravný prostředek a soudní přezkum. Odděl správní, kárnou a trestní odpovědnost. Vyhledej související rozhodnutí o profesní mlčenlivosti, skutečném majiteli a kontrole klienta; nepřebírej hotová ratio z názvu případu.

Dodej závěr pro konkrétní obchod, rizikový profil a tabulku krok–právní základ–doklad–odpovědná osoba–ověřená lhůta. Je-li zadána směrnice, oznámení nebo smluvní klauzule, napiš její použitelné znění s otevřenými údaji označenými k doplnění. Nikdy nenavrhuj obcházení identifikace, dělení hotovosti za účelem obcházení nebo fingování důkazů. Připravené oznámení neoznačuj jako podané.
