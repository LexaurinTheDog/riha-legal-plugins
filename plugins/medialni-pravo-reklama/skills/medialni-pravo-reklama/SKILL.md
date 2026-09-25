---
uuid: 2ecb06ce-cf76-468a-84cf-e00f8713841e
name: medialni-pravo-reklama
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Mediální právo a reklama ČR"
    summary: "Tiskový zákon a právo na odpověď, regulace vysílání a audiovizuálních služeb na vyžádání, regulace reklamy včetně léčiv, alkoholu, tabáku, hazardu a potravin, klamavá a srovnávací reklama, nekalé obchodní praktiky a ochrana spotřebitele, influencer marketing, difamace a ochrana osobnosti versus svoboda projevu, ochrana zdroje novináře, DSA a EMFA, přímý marketing a spam."
    examplePrompts:
      - "Deník zveřejnil o klientovi (starostovi) článek s nepravdivým tvrzením o zpronevěře dotace. Jak uplatnit právo na odpověď, jaké jsou lhůty a kdy má smysl žaloba na ochranu osobnosti?"
      - "Klient prodává doplněk stravy a chce kampaň s influencery, která tvrdí, že produkt „posiluje imunitu a pomáhá při hubnutí“. Co je přípustné a jak označit spolupráci?"
      - "Konkurent klienta spustil srovnávací reklamu, kde uvádí ceny klienta z minulého roku a označuje jeho produkt za „předražený šmejd“. Jaké nároky lze uplatnit a lze žádat předběžné opatření?"
  en:
    displayName: "Czech Media & Advertising Law"
    summary: "Press law and right of reply, broadcasting and on-demand audiovisual services regulation, advertising regulation including pharmaceuticals, alcohol, tobacco, gambling and food, misleading and comparative advertising, unfair commercial practices and consumer protection, influencer marketing, defamation and personality rights versus freedom of expression, journalists' source protection, Digital Services Act and European Media Freedom Act, direct marketing and spam."
    examplePrompts:
      - "A daily published an article about my client (a mayor) with a false claim of subsidy embezzlement. How to exercise the right of reply, what are the deadlines and when is a personality-rights action worthwhile?"
      - "My client sells a food supplement and wants an influencer campaign claiming the product 'boosts immunity and helps weight loss'. What is permissible and how must the cooperation be labelled?"
      - "A competitor launched comparative advertising quoting my client's last-year prices and calling his product 'overpriced junk'. Which claims can be brought and is an interim injunction available?"
  sk:
    displayName: "Mediálne právo a reklama ČR"
    summary: "Tlačový zákon a právo na odpoveď, regulácia vysielania a audiovizuálnych služieb na požiadanie, regulácia reklamy vrátane liečiv, alkoholu, tabaku, hazardu a potravín, klamlivá a porovnávacia reklama, nekalé obchodné praktiky a ochrana spotrebiteľa, influencer marketing, difamácia a ochrana osobnosti verzus sloboda prejavu, ochrana zdroja novinára, DSA a EMFA, priamy marketing a spam."
    examplePrompts:
      - "Denník zverejnil o klientovi (starostovi) článok s nepravdivým tvrdením o sprenevere dotácie. Ako uplatniť právo na odpoveď, aké sú lehoty a kedy má zmysel žaloba na ochranu osobnosti?"
      - "Klient predáva výživový doplnok a chce kampaň s influencermi, ktorá tvrdí, že produkt „posilňuje imunitu a pomáha pri chudnutí“. Čo je prípustné a ako označiť spoluprácu?"
      - "Konkurent klienta spustil porovnávaciu reklamu, kde uvádza ceny klienta z minulého roka a označuje jeho produkt za „predražený šmejd“. Aké nároky možno uplatniť a možno žiadať predbežné opatrenie?"
description: Použij pro tisk, vysílání, audiovizuální služby, reklamní kampaně, influencery, právo na odpověď, novinářské zdroje, mediální osobnostní zásahy, komoditní a politickou reklamu, přímý marketing, dohled a reklamní smlouvy. Obecnou náhradu újmy, platformovou infrastrukturu a hospodářskou soutěž propojuj s příslušným oborovým skillem. Právní zdroje jen nativní CODEXIS v aplikaci.
---

# Mediální právo a reklama ČR

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

## Role, obsah a zachování faktů

Zjisti, zda zastupuješ dotčeného člověka či právnickou osobu, vydavatele, redakci, vysílatele, poskytovatele audiovizuální služby, platformu, zadavatele, zpracovatele nebo šiřitele reklamy, influencera, agenturu, soutěžitele nebo spotřebitelskou organizaci. Každé roli odpovídá jiný nárok a odpovědnost. Z dodaného obsahu zaznamenej přesná slova, obraz, zvuk, formát, datum, dosah a následné změny. Screenshot nemusí dokazovat dobu celé publikace; návrh opravy nedokazuje zveřejnění. Chybějící podobu kampaně nebo vyjádření osoby vyžádej v aplikaci.

## Kvalifikace a nativní prameny

Rozliš tisk, rozhlas, televizi, službu na vyžádání, samostatný web, sociální síť a sdílení videa. Je konkrétní obsah skutkovým tvrzením, hodnotícím soudem, smíšeným výrokem, reklamou, sponzoringem, umístěním produktu nebo obchodním či politickým sdělením? Pouhý počet sledujících či příspěvků neurčuje službu ani dozor. V CODEXIS vyhledej rozhodná znění tiskového zákona, regulace vysílání a audiovizuálních služeb, regulace reklamy, ochrany spotřebitele, občanského zákoníku, autorského a známkového práva, elektronických komunikací, informačních služeb a zpracování údajů. Podle věci přidej DSA, EMFA, politickou reklamu, AI Act a komoditní unijní předpisy. Jejich působnost a data použitelnosti teprve ověř.

## Ochrana před zveřejněním a obrana média

U každého výroku ověř právní význam pravdivosti, věcného základu, veřejného zájmu, postavení osoby, okolností získání informace, formy a intenzity. Nezaměňuj právnickou osobu za nositele všech práv člověka. Vyhledej kritéria proporcionality mezi soukromím, důstojností, pověstí a svobodou projevu; porovnej i rozhodnutí odmítající obdobné nároky. Převzetí od agentury nebo úředního zdroje nepředstavuj bez prověření jako úplnou imunitu.

Prověř podmínky práva na odpověď a dodatečné sdělení pro skutečné médium, oprávněnou osobu, obsah žádosti, adresáta, lhůtu a výjimky. Sestav samostatný kalendář publikace, žádosti, vyřízení a žaloby. Nepřenášej tiskový režim automaticky na web. U obecné ochrany porovnej opravu, anonymizaci, stažení, zákaz dalšího šíření, omluvu a peněžité zadostiučinění. Omluvu formuluj přesně včetně místa, formy a času; zákaz nesmí být neurčitý či nepřiměřeně široký. Zvaž rozdíl mezi archivem, původním článkem a výsledkem vyhledávání.

Pro redakci ověř ochranu zdroje, meze povinné součinnosti, presumpci neviny, ochranu dětí a obětí, obrazové licence a autorskou citaci. U radničního periodika zkoumej zvláštní povinnosti. U platformy prověř oznámení nezákonného obsahu, odůvodnění rozhodnutí, stížnost a odpovědnost za komentáře podle její skutečné role. Nepoužívej nález o konkrétním diskusním fóru jako univerzální pravidlo moderace.

## Reklama před spuštěním

Projdi souběžně obecnou, komoditní a mediální regulaci. U klamání a srovnávání urč cílovou skupinu, ověřitelné tvrzení, úplnost ceny, časovou platnost srovnání, metodiku průzkumu, slevy, recenze, nadsázku, agresivní praktiky a obsah příloh zákona. Nedoplňuj srovnání konkurenta, pokud v kampani není. U léčiv, zdravotnických prostředků, potravin a doplňků nejdříve kvalifikuj výrobek; následně ověř povolená tvrzení a povinné informace pouze v dostupném nativním obsahu. Nedostupný registr nepřeklen prostřednictvím externího webu.

Samostatně prověř alkohol, tabák a elektronické cigarety, hazard, finanční služby, energie, cestovní služby, kosmetiku, zbraně, ochranné přípravky, pohřebnictví, výživu dětí a údaje o vozidlech. U každé relevantní komodity zjisti zákazy, výjimky, publikum a příslušný dozor. U influencera zkoumej úplatu, barter, vlastní produkt, rozpoznatelnost spolupráce, umístění označení, nezletilost a případnou audiovizuální regulaci. U syntetického obrazu či hlasu ověř zvlášť označování a osobnostní oprávnění.

U e-mailů, zpráv, telefonátů, cookies a profilování rozliš zákonný titul zpracování a přípustnost komunikačního kanálu, souhlas, zákaznickou výjimku, námitku a odhlášení. Prověř reklamu dětem, citlivé údaje, soutěže a možné hazardní či daňové důsledky. Autorskou hudbu, fotografie, známky konkurenta a podobu osoby posuzuj podle doložené licence, ne podle zadavatelova ujištění.

## Odpovědnost a hotové výstupy

Rozliš příslušnost každého dozorového orgánu, odpovědnost jednotlivých rolí, promlčení, liberační obranu, souběh a proporcionalitu sankce. U vysílání zjisti, zda je pro daný postih nutné předchozí upozornění a jaké podmínky typové souvislosti splňuje. Pro civilní větev připrav výzvu, petit, důkazy, předběžnou ochranu a samostatný rozpočet poplatků, jistoty a nákladů; podnět dozoru nenahrazuje žalobu.

Při smluvním zadání dodej klauzule briefu, schvalování, licencí, označení, oprav, odpovědnosti, regresu a ukončení ve prospěch klienta v přípustném rozsahu. Interní regres neoznačuj za zánik veřejnoprávní odpovědnosti. Nápravný plán obsahuje přesné znění opravy, odpovědnou osobu, termín a důkaz provedení. Výstup uzavři tabulkou prvek–režim–ověřená opora–riziko–konkrétní změna a úplným požadovaným dokumentem.
