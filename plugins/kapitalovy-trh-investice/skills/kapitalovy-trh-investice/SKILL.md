---
uuid: 35193222-32dc-4e1f-8177-f5a1d933624a
name: kapitalovy-trh-investice
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Kapitálový trh a investice ČR"
    summary: "Obchodníci s cennými papíry a zprostředkovatelé dle MiFID II, vhodnost a přiměřenost, nároky investorů vůči obchodníkům, veřejná nabídka a výjimky z prospektu, dluhopisy a schůze vlastníků, investiční fondy a režimy ZISIF, crowdfunding, kryptoaktiva dle MiCA, zneužití trhu a insider dealing, informační povinnosti emitentů a oznámení podílů, nabídky převzetí a squeeze-out, dohled a sankce ČNB, finanční arbitr, zdanění investičních příjmů."
    examplePrompts:
      - "Klient (důchodce) investoval přes zprostředkovatele 2 mil. Kč do korporátních dluhopisů developera, který zkrachoval. Zprostředkovatel nezjišťoval jeho znalosti a tvrdil, že jde o „bezpečnou investici“. Jaké nároky má a proti komu?"
      - "Startup klienta chce vydat dluhopisy za 25 mil. Kč a nabízet je veřejnosti přes web. Potřebuje prospekt, nebo lze využít výjimku, a jaké má povinnosti vůči ČNB?"
      - "Klient je členem představenstva kótované společnosti a před zveřejněním výsledků prodal akcie. ČNB zahájila řízení pro insider dealing. Jak se bránit a jaké hrozí sankce?"
  en:
    displayName: "Czech Capital Markets & Investments"
    summary: "Investment firms and intermediaries under MiFID II, suitability and appropriateness, investor claims against brokers, public offers and prospectus exemptions, bonds and bondholder meetings, investment funds and AIFMD regimes, crowdfunding, crypto-assets under MiCA, market abuse and insider dealing, issuer disclosure and major holdings, takeover bids and squeeze-outs, CNB supervision and sanctions, financial arbitrator, taxation of investment income."
    examplePrompts:
      - "My client (a pensioner) invested CZK 2m through an intermediary into corporate bonds of a developer that went bankrupt. The intermediary did not assess his knowledge and called it a 'safe investment'. What claims does he have and against whom?"
      - "My client's startup wants to issue CZK 25m of bonds and offer them to the public via its website. Does it need a prospectus or can it use an exemption, and what are its duties towards the CNB?"
      - "My client sits on the board of a listed company and sold shares before results were published. The CNB opened insider-dealing proceedings. How to defend and what sanctions are at stake?"
  sk:
    displayName: "Kapitálový trh a investície ČR"
    summary: "Obchodníci s cennými papiermi a sprostredkovatelia podľa MiFID II, vhodnosť a primeranosť, nároky investorov voči obchodníkom, verejná ponuka a výnimky z prospektu, dlhopisy a schôdze vlastníkov, investičné fondy a režimy ZISIF, crowdfunding, kryptoaktíva podľa MiCA, zneužitie trhu a insider dealing, informačné povinnosti emitentov a oznámenie podielov, ponuky na prevzatie a squeeze-out, dohľad a sankcie ČNB, finančný arbiter, zdanenie investičných príjmov."
    examplePrompts:
      - "Klient (dôchodca) investoval cez sprostredkovateľa 2 mil. Kč do korporátnych dlhopisov developera, ktorý skrachoval. Sprostredkovateľ nezisťoval jeho znalosti a tvrdil, že ide o „bezpečnú investíciu“. Aké nároky má a proti komu?"
      - "Startup klienta chce vydať dlhopisy za 25 mil. Kč a ponúkať ich verejnosti cez web. Potrebuje prospekt, alebo možno využiť výnimku, a aké má povinnosti voči ČNB?"
      - "Klient je členom predstavenstva kótovanej spoločnosti a pred zverejnením výsledkov predal akcie. ČNB začala konanie pre insider dealing. Ako sa brániť a aké hrozia sankcie?"
description: Regulace investičních služeb, ochrana investorů a jejich nároky, emise a distribuce nástrojů, fondy, crowdfunding, kryptoaktiva, zneužívání trhu a povinnosti poskytovatelů. Zahrnuje licencování, prospekty, informační dokumenty a daně. Bankovní úvěry a zajištění směruje bankovnímu skillu, obecné korporátní otázky a převody účastí korporátnímu/M&A skillu a pojištění pojistnému skillu. Právní posouzení nenahrazuje osobní investiční doporučení.
---

# Kapitálový trh a investice

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

## Role, produkt a rozhodný režim

Urči, zda zastupuješ investora, obchodníka, zprostředkovatele, vázaného zástupce, emitenta, fond, správce, platformu, poskytovatele krypto služeb nebo člena orgánu. Rozliš zákaznickou kategorii a skutečně vykonávanou činnost: obecný marketing, osobní doporučení, přijímání a předávání pokynů, provádění, správu, upisování či úschovu. Název poradce ani disclaimer nepřebíjejí reálné jednání.

Klasifikuj akcie, dluhopisy, podíly, ETF, deriváty, strukturované produkty a tokeny podle skutečných práv a fungování. Token může vyžadovat režim finančního nástroje; označení NFT nebo klubová investice samo nevylučuje regulaci. Zjisti země, rezidence, skupinu, data nabízení, uzavření a plnění. V nativním CODEXIS vyhledej české i unijní vrstvy, prováděcí akty a přechodná pravidla; metodiky a obecné pokyny odliš od závazné normy. Změny pravidel fondů, obchodování, prospektů, digitálních aktiv či zveřejňování nespojuj s neověřeným pevným datem.

## Ochrana zákazníka a vznik nároku

Odděl kategorizaci, vhodnost doporučení, přiměřenost produktu, produktové informace, pobídky a nejlepší provedení. Jaké údaje o zkušenostech, znalostech, cílech, toleranci rizika a schopnosti nést ztrátu byly skutečně získány? Dotazník předvyplněný poskytovatelem není automaticky důkazem kvalifikovaného posouzení. Koncentraci počítej vůči správně doloženému portfoliu a relevantním aktivům, nikoli vůči svévolnému jmenovateli.

Ověř obsah a načasování prohlášení o vhodnosti a případné výjimky při dálkovém jednání. Nabídka možnosti odložit obchod není sama splněním všech kumulativních podmínek výjimky. U nezávislého a jiného poradenství vyhledej rozdílný režim pobídek; informování o poplatku nezhojí pobídku, kterou právo nepřipouští.

Prověř cílový trh a produktové řízení, střety zájmů, odměny, nadměrné obchodování, náklady před obchodem i následně, evidenci komunikace, úschovu a oddělení klientského majetku. U garanční ochrany vyhledej přesný rozsah a limity podle události; neprezentuj ji jako obecnou náhradu investiční ztráty.

Pro civilní nárok přiřaď každé osobě její vlastní povinnost: emitent, poradce, vázaný zástupce, zastoupený poskytovatel, platforma či autor informačního dokumentu. Odděl porušení, zavinění, příčinnou souvislost a újmu. Špatná výkonnost produktu sama nedokazuje odpovědnost. Popiš doložený alternativní scénář rozhodnutí klienta, skutečnou hodnotu, výnosy, poplatky a případné snížení škody bez dvojí náhrady.

Prověř neplatnost, omyl, klamání, odstoupení a zvláštní dálkové výjimky, promlčení a souběh s insolvencí emitenta. Dohledový podnět není automaticky žalobou na peníze. Příslušnost finančního arbitra ověř pro konkrétní protistranu, produkt a nárok; alternativně posuď civilní či kolektivní řízení, trestní adhezi a přihlášku. Nečekej bez právního důvodu na výsledek dohledu.

## Emitent, nabídka a fondové struktury

U emise dluhopisů prověř korporátní oprávnění, emisní podmínky, podobu, identifikaci, výnos, splatnost, zajištění, společného zástupce, schůzi vlastníků a změny práv. U veřejné nabídky analyzuj skutečnou komunikaci, agregaci nabídek, území, období a přesné podmínky výjimek z prospektu. Nezaměňuj prospekt, reklamu, klíčové informace a bílou knihu. Schválení dokumentu není potvrzením bezpečnosti investice.

Rozliš vydávání vlastních nástrojů od jejich regulované distribuce. Zajisti soulad tvrzení, rizik, použití výtěžku a finančních dat a vyhodnoť odpovědnost za nesprávné informace. U finančních potíží odděl práva vlastníků, zajištění, insolvenční postup a případnou restrukturalizaci.

U fondů rozliš kolektivní a kvalifikované investování, soukromou správu a pouhou registraci. Registrace nemusí být licencí a jeden veřejný webový údaj sám neřeší celý test veřejného nabízení. Ověř okruh oslovených osob, marketing, kvalifikaci investora, objem, výjimky, právní formu, podfondy, statut, oceňování, páku, administrátora, depozitáře a přeshraniční nabízení.

U crowdfundingu rozliš podnikatelské financování od spotřebitelského úvěru, nástroje, agregaci, informační dokument, testy nezkušeného investora a případnou dobu na rozmyšlenou. U kryptoaktiv prověř tokenové kategorie, licenci služby, bílou knihu, přechodný režim, pravidla převodních informací, úschovu a zneužívání trhu. U tokenizovaných finančních nástrojů zvaž zvláštní režim infrastruktury distribuovaného registru.

## Tržní integrita a organizace poskytovatele

U vnitřní informace rozlož přesnost, neveřejnost, cenovou významnost a časový vývoj včetně dílčích kroků delšího procesu. Kdy má být zveřejněna a za jakých podmínek může být zveřejnění odloženo? Prověř dokumentaci a oznámení, seznamy osob, zákaz obchodování či změny pokynu, doporučení a neoprávněné předání. Zvlášť řeš průzkum trhu, manipulaci, benchmarky, hlášení podezřelých pokynů a obchodů, zpětné odkupy a legitimní výjimky.

U vedoucích osob a propojených osob zjisti oznamování a obchodní omezení. U významných účastí zahrň hlasovací práva, jednání ve shodě a nástroje; u nabídek převzetí, vytěsnění a delistingu ověř postup, cenu, ochranu menšiny a soudní přezkum. Zohledni periodické informace a formát výkaznictví, pokud se uplatní.

U poskytovatele prověř licenci a její rozsah, kapitálový režim, řízení, kvalifikované účasti, odbornost, AML, střety, whistleblowing, osobní údaje, outsourcing a digitální odolnost. U přeshraniční činnosti vyhledej podmínky oprávnění, oznámení a skutečné zpětné iniciativy zákazníka. Nezaměňuj investiční službu s přijímáním vkladů. Sankční obrana vyžaduje konkrétní skutek, přičitatelnost, práva při kontrole, lhůty, odůvodnění a přezkum; zvlášť řeš zveřejnění rozhodnutí a ochranu údajů.

## Daně a povinný výstup

Daně posuzuj podle osoby, roku, rezidence, nástroje, nabytí a realizace. Rozliš prodejní příjem od zisku, časové a hodnotové podmínky osvobození a jejich případné souběhy či změny, dividendy, srážku a zahraniční zápočet. Podle zadání zahrň dlouhodobé investiční produkty, zaměstnanecké plány, krypto, fondové výnosy, holding a oznamovací přeshraniční režimy. Historický limit nebo sazbu nepřenášej bez nového ověření.

Dodej právní mapu produktu a služby, přehled povinností a důkazů, úplné požadované podmínky či podání a varianty ve prospěch klienta. Odděl civilní, dohledové a trestní závěry. U peněžního nároku připoj přesný petit, výpočet újmy a nákladů, nejsilnější námitky a připravenost k podání; u investiční varianty nepředstírej individuální ekonomické doporučení bez podkladů.
