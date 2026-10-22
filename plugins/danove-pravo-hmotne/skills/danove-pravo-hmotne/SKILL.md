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
description: 'Použij pro hmotné české zdanění: příjmy FO a PO, DPH, osvobození a časové testy, nemovitosti, podíly, kryptoaktiva, náklady, odpisy, rezidence, dvojí zdanění, převodní ceny, zneužití práva, podvody a ručení u DPH, zaměstnanec versus OSVČ, odměňování, přeměny a holdingy, insolvenční a trestní daňové souvislosti. Samostatnou procesní obranu směruj do skillu správního a daňového řízení.'
---

# Daňové právo hmotné ČR

## Zdrojový režim: SLV, e-Sbírka a Sagasu

Právní prameny získávej těmito nástroji v uvedeném pořadí; jiné zdroje jen tehdy, když tyto pramen nemají:

1. **MCP SLV (Salvia)** — česká judikatura a vyhledání předpisu. Indexy `ns` (Nejvyšší soud), `nss` (Nejvyšší správní soud), `us` (Ústavní soud), `justice` (okresní, krajské a vrchní soudy), `isir` (insolvenční rejstřík). Nástroje: `search_decisions`, `search_by_case_number`, `fetch_decision`; předpisy `search_regulations`, `fetch_regulation_info`, `fetch_regulation_text`.
2. **Skill e-Sbírka** (`/esbirka` z pluginu `zdroje-slv`, skript `scripts/esbirka.py` v adresáři skillu `esbirka`) — úřední znění předpisu účinné k rozhodnému dni (`info --k`, `par --k`, `text`), historie znění (`zneni`), rozdíly mezi zněními (`diff`), novely, přechodná ustanovení a nálezy ÚS (`souvislosti`). Znění citované v odpovědi ber odsud, ne z paměti ani z textu rozhodnutí.
3. **MCP Sagasu** — subjekty, rejstříky a výpočty: ekonomický subjekt podle IČO nebo názvu `firma_vyhledat` → `firma_detail` (ARES, jen aktivní; slovenské `firma_sk_vyhledat` → `firma_sk_detail`); výpis z obchodního rejstříku se statutárními orgány, společníky a kapitálem `obchodni_rejstrik`; zaniklé a vymazané osoby `verejny_rejstrik`, angažmá fyzické osoby `verejny_rejstrik_osoba`, angažmá právnické osoby `verejny_rejstrik_angazma_po`; listiny ze sbírky listin a jejich text `sbirka_listin` → `listina_text`; živnosti `zivnostensky_rejstrik`, `zivnostnik_vyhledat`; nespolehlivý plátce DPH a zveřejněné účty `dph_status`; adresa podle RÚIAN `standardizace_adresy`; ID datové schránky `datova_schranka_vyhledat` (nejjistěji podle IČO); advokáti `advokat_cz_vyhledat` → `advokat_cz_detail`; insolvence `insolvence_vyhledat` → `insolvence_detail` (události) → `insolvence_dokument_text`; výpočty `urok_z_prodleni`, `odmena_advokata`, `soudni_poplatek`. Postup je vždy vyhledání → detail → text. Když ARES nic nevrátí, subjekt může být zaniklý — ověř ve `verejny_rejstrik` dřív, než uzavřeš, že neexistuje.
4. Komentáře, literatura a webové zdroje slouží jen jako navigace, nikdy jako citovaná opora; jejich odkazy na normy a rozhodnutí ověř načtením v SLV nebo e-Sbírce.

Výpočty Sagasu (úrok z prodlení, odměna advokáta, soudní poplatek) přeber i s rozpisem a citací předpisu a přepočítej je druhou cestou (např. repo sazba + 8 p. b. = sazba a zpět); nesoulad je chyba. Údaje o právnické osobě do externího dokumentu (název, IČO, sídlo, statutární orgán, způsob jednání) ověř v Sagasu v reálném čase, vymazané osoby vynech; nelze-li ověřit, použij `[DOPLNIT z OR]`. Údaje fyzických osob jednajících za právnickou osobu (statutární orgán, prokurista, likvidátor) ověř týmž způsobem v `obchodni_rejstrik` nebo `verejny_rejstrik`; ostatní údaje fyzických osob přebírej jen z listin ve spisu.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán. Rozliš prázdný výsledek, odmítnutý přístup (SLV i Sagasu vyžadují přihlášení), nedostupný nástroj a neúplný obsah. Identický neúspěšný dotaz neopakuj bez změny; zkus věcně odůvodněnou alternativu (jiný index, jiný režim hledání, kratší dotaz), pak mezeru přesně označ `[DOPLNIT]`. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením. Znění, soud, spisovou značku a datum přebírej jen z načteného zdroje.

Je-li pro dílčí práci použit další agent nebo skill, předej mu výslovně tento zdrojový režim, rozhodné skutky a časové otázky. Vyžádej konkrétní zdrojové pasáže; jeho shrnutí nenahrazuje načtený pramen.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a z listin, které uživatel předložil; právní tvrzení v nich nejsou nezávisle ověřeným právem. Rejstříkové údaje (subjekt, statutární orgán, sbírka listin, insolvence, datová schránka) ověřuj v Sagasu podle oddílu Zdrojový režim; jiné externí databáze a místní archivy bez pokynu nenačítej. Chybějící skutkový doklad si vyžádej od uživatele a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v SLV a e-Sbírce. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v SLV a e-Sbírce. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. V SLV používej filtry podle jejich skutečného významu: index soudu (`idx`), vazbu na předpis (`reg_num`, `reg_year`, `reg_par`, případně `reg_num2`…), časový filtr `date_from` a režim hledání (`bm25`, `knn`, `hybrid`). Judikaturu hledej v SLV přes indexy `ns`, `nss`, `us`, `justice` a `isir`, předpisy přes `search_regulations` a jejich znění v e-Sbírce; unijní předpisy a judikaturu SDEU a ESLP ověř v oficiálních databázích (EUR-Lex, CURIA, HUDOC). Komentář, literatura a vzor slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v SLV nebo e-Sbírce.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Neomezuj se na první várku výsledků: rozšiř dotazy na další indexy, režimy a `date_from` a prověř související i navazující dokumenty (u rozhodnutí `citedBy` a `citedCaseLaw` z `fetch_decision`, u předpisu `souvislosti` v e-Sbírce). Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, vyhledej pro každý nosný paragraf rozhodnutí, která ho citují: `search_decisions` s `reg_num`, `reg_year` a `reg_par` (bez dotazu vrátí všechna rozhodnutí citující ustanovení, nejnovější první; s krátkým dotazem je seřadí podle relevance uvnitř této množiny). Fulltext je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje vazbu na paragraf.

1. **Kandidáti:** hledej přes indexy `ns`, `nss` a `us` (podle oboru i `justice`, v insolvenci `isir`) — jedno volání = jeden index. Projdi alespoň prvních 20 kandidátů a relevantní zařaď do výběru. Zvlášť dohledej nejnovější rozhodnutí (`date_from` na poslední roky), aby ti neunikl pozdější vývoj. Druhé ustanovení lze přidat přes `reg_num2`/`reg_year2`/`reg_par2`.
2. **Skutková shoda:** doplň fulltextem. Režim `bm25`: 2–5 výrazných právních pojmů, všechna slova musí v textu být (nula výsledků znamená vypustit slovo, ne absenci judikatury). Režim `knn`: jedna právní otázka formulovaná jako právní věta; víc otázek rozděl do více dotazů. Známou spisovou značku dohledej `search_by_case_number`.
3. **Třídění kandidátů** (před načtením celého textu podle kroku 4):
   - **citační graf:** `fetch_decision` vrací `citedBy` (pozdější rozhodnutí, která ho citují) a `citedCaseLaw`; sleduj `citedBy` 1–2 skoky k nejnovějšímu vyjádření téže právní věty a k případnému odklonu. Absence odklonu v `citedBy` pozdější odklon nevylučuje (citační graf nemusí být úplný), proto doplň i `search_decisions` s `date_from`;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (výsledky s `date_from` z bodu 1 a fulltext `velký senát <právní pojem>`). Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované v oficiální sbírce má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření v e-Sbírce (`diff`, `par --k`), že se pravidlo věcně nezměnilo; ustanovení, která rozhodnutí skutečně aplikovalo, jsou v `regulations[]` z `fetch_decision`.
4. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf nic nevrací, uveď to a pokračuj fulltextem.
5. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti v e-Sbírce (`par --k <datum>`, případně `text`) úplný text použitého ustanovení ve znění účinném k rozhodnému dni, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky; SLV použij jen k identifikaci předpisu. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v SLV relevantní pozdější, překonávající a nepříznivou judikaturu (`citedBy` z `fetch_decision`, `search_decisions` s `date_from`); nálezy ÚS rušící použité ustanovení ověř v e-Sbírce (`souvislosti`). Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástrojů, nikoli o tvrzení o automatickém ověření, které neproběhlo. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení v SLV a e-Sbírce.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí v SLV (`search_decisions` v příslušném indexu, `search_by_case_number`); obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej jen z odpovědí SLV, e-Sbírky a Sagasu, u unijních pramenů a judikatury SDEU a ESLP z EUR-Lex, CURIA a HUDOC; URL nesestavuj ani nedomýšlej. Ve výstupu uveď přesnou právní citaci (soud, spisová značka, datum, případně ECLI; předpis číslem ve Sbírce, §, odstavec, písmeno), nikoli interní ID nástroje. Pokud odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revizi či kontrolu, pokud skutečně neproběhly a nedokládá je výsledek nástroje.

Zkontroluj všechny požadované artefakty. Označ pracovní, neúplný či k revizi určený výstup pravdivě. Uložení, odeslání, doručení, podpis a podání jsou odlišné stavy; žádný nepředstírej. Bez výslovného pokynu nic neposílej ani nepodávej. Nedodané části a neověřené rozhodné zdroje nesmějí být skryty prohlášením „hotovo“ nebo „vše ověřeno“.

## Oborové otázky a požadované výstupy

## Oborový postup: hmotné daňové právo

### Poplatník, období a otázky
Urči konkrétního klienta, jeho roli a skutečný hospodářský cíl. Rozliš fyzickou a právnickou osobu, rezidenta a nerezidenta, zaměstnance a podnikatele, holding, fond, svěřenský fond, SVJ, spolek a obec. Přiřaď daň, zdaňovací období, druh příjmu či plnění, účetní režim a cizí prvek. Rozliš plánování, tvrzení daně, kontrolu a spor. Procesní obranu koordinuj s příslušným oborovým postupem, ale neztrácej hmotněprávní otázku.

V SLV a e-Sbírce ověř rozhodné znění pro každou daňovou událost a přechodná pravidla podle nabytí, převodu, uskutečnění plnění, přijetí příjmu či vzniku nákladu. Stejná transakce nemusí mít totožný okamžik v různých daních. Vyhledej související prováděcí předpisy, mezinárodní smlouvu, protokoly a unijní pravidla. Metodiky GFŘ, závěry Koordinačního výboru a účetní standardy (financnisprava.cz, mfcr.cz) používej jen k navigaci a odliš je od zákona načteného v e-Sbírce.

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
Rozliš osobu, registraci a její okamžik, identifikovanou osobu, skupinu, předmět, místo a uskutečnění plnění. U odpočtu zkoumej hmotné a formální podmínky, ekonomické použití, doklady, lhůtu, poměr, krácení, vyrovnání a úpravu. Odděl neprokázané plnění, účast na podvodu, vědomostní test a ručení; každé větvi přiřaď důkazní břemeno. Zjisti konkrétní rozumná opatření klienta bez fingování kontroly dodavatele; status nespolehlivého plátce a zveřejněné účty dodavatele ověř `dph_status`, jeho identitu a historii `firma_detail`, `verejny_rejstrik` a `insolvence_vyhledat`.

Prověř přenesení daňové povinnosti, stavby, pozemky, dokončení a podstatnou změnu, první dodání, nájem, volbu zdanění, sazby a přílohy. Historický test osvobození nepřenášej na nové plnění. Zahrň finanční, zdravotní, sociální a vzdělávací služby, opravy základu, nedobytné pohledávky, kontrolní a souhrnné hlášení, OSS/IOSS, dovoz, vývoz, přepravu v řetězci, poukazy, zálohy, závod a zrušení registrace.

### Další daně, práce, mezinárodní a trestní souvislosti
Podle zadání ověř daň z nemovitých věcí včetně místních koeficientů, silniční, spotřební, energetické a hazardní daně. U odměňování porovnej skutečnou závislou práci, orgánovou funkci, podnikání, ESOP, práci z domova, cestovní náhrady a vysílání; smluvní název není důkaz režimu. Mezinárodně prověř stálou provozovnu, přičítání zisku, jednotlivé druhy příjmů, metodu zápočtu či vynětí, rezidenční doklady, MLI, MAP, DAC a výměnu údajů.

U sankcí a trestních rizik samostatně zkoumej penále, úroky, opožděné tvrzení, opravné tvrzení, zkrácení a neodvedení daně, účinnou lítost, odpovědnost právnické osoby, zajištění a souběh sankcí. Nenavrhuj fiktivní doklady ani umělé řetězce.

### Výstup
Dodej závěr pro každou daň, tabulku podmínka–fakt–důkaz–pramen–riziko, ověřené výpočty s mezikroky a realizační plán. Zákonnou lhůtu přiznání či oznámení odvoď z použitelného procesního pravidla včetně způsobu podání, počátku, kalendáře a svátků; elektronická forma sama neprokazuje prodloužení. Interní rezervu označ zvlášť. Datum rešerše nezaměňuj s historickým nebo simulovaným rozhodným dnem.
