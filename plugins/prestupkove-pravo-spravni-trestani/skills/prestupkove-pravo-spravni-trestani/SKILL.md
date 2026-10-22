---
uuid: b7fee0bb-4d40-4fdf-888b-b023fa988c43
name: prestupkove-pravo-spravni-trestani
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Přestupkové právo a správní trestání ČR"
    summary: "Odpovědnost za přestupek dle zákona 250/2016, přestupky fyzických osob, podnikatelů a právnických osob s liberací, promlčení, správní tresty a jejich výměra, příkaz a odpor, příkazový blok, ústní jednání a dokazování, dopravní přestupky a bodový systém, odvolání se zákazem reformationis in peius, přezkumné řízení, správní žaloba a moderace trestu, ne bis in idem s trestním právem."
    examplePrompts:
      - "Klientovi přišel příkaz za překročení rychlosti o 45 km/h v obci s pokutou a zákazem řízení na 6 měsíců, měření proběhlo před 14 měsíci. Je přestupek promlčen a má smysl podat odpor?"
      - "Firmě klienta uložil živnostenský úřad pokutu 400 000 Kč za přestupek, o kterém rozhodl bez ústního jednání a bez výslechu navržených svědků. Jaké vady namítat v odvolání a lze žádat moderaci u soudu?"
      - "Klient dostal za tentýž skutek pokutu v přestupkovém řízení a nyní je trestně stíhán. Brání zásada ne bis in idem trestnímu stíhání?"
  en:
    displayName: "Czech Misdemeanours & Administrative Penalties"
    summary: "Liability for administrative offences under Act 250/2016, offences of individuals, entrepreneurs and legal entities with exculpation, limitation periods, penalties and their assessment, penalty orders and objections, on-the-spot fines, oral hearings and evidence, traffic offences and the points system, appeals with the ban on reformatio in peius, review proceedings, judicial review and moderation of penalties, ne bis in idem with criminal law."
    examplePrompts:
      - "My client received a penalty order for speeding by 45 km/h in a built-up area with a fine and a 6-month driving ban; the measurement took place 14 months ago. Is the offence time-barred and is an objection worthwhile?"
      - "The trade licensing office fined my client's company CZK 400,000 without an oral hearing and without examining the proposed witnesses. Which defects to raise on appeal and can the court moderate the fine?"
      - "My client was fined in misdemeanour proceedings for the same act and is now criminally prosecuted. Does ne bis in idem bar the prosecution?"
  sk:
    displayName: "Priestupkové právo a správne trestanie ČR"
    summary: "Zodpovednosť za priestupok podľa zákona 250/2016, priestupky fyzických osôb, podnikateľov a právnických osôb s liberáciou, premlčanie, správne tresty a ich výmera, príkaz a odpor, príkazový blok, ústne pojednávanie a dokazovanie, dopravné priestupky a bodový systém, odvolanie so zákazom reformationis in peius, preskúmavacie konanie, správna žaloba a moderácia trestu, ne bis in idem s trestným právom."
    examplePrompts:
      - "Klientovi prišiel príkaz za prekročenie rýchlosti o 45 km/h v obci s pokutou a zákazom vedenia na 6 mesiacov, meranie prebehlo pred 14 mesiacmi. Je priestupok premlčaný a má zmysel podať odpor?"
      - "Firme klienta uložil živnostenský úrad pokutu 400 000 Kč za priestupok, o ktorom rozhodol bez ústneho pojednávania a bez výsluchu navrhnutých svedkov. Aké vady namietať v odvolaní a možno žiadať moderáciu na súde?"
      - "Klient dostal za ten istý skutok pokutu v priestupkovom konaní a teraz je trestne stíhaný. Bráni zásada ne bis in idem trestnému stíhaniu?"
description: 'Použij pro přestupky a správní sankce: obviněného, poškozeného, odpovědnost fyzických a právnických osob, liberaci, promlčení, příkaz a odpor, tresty, náklady, odvolání, soudní moderaci, dopravní přestupky, body a zákaz řízení, ne bis in idem a hranici trestného činu. Obecný správní proces a trestní obhajobu propojuj s oborovými skilly.'
---

# Přestupkové právo a správní trestání

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

## Skutek, role a ochranné lhůty

Urči, zda klientem je obviněný člověk, mladistvý, podnikající fyzická osoba, právnická osoba, provozovatel vozidla, poškozený, vlastník věci nebo osoba přímo postižená. Vymez tvrzený skutek, místo, čas, způsob, následek, právní kvalifikaci a skutečnou fázi. Rozliš výzvu před zahájením, oznámení řízení, příkaz, příkaz na místě, rozhodnutí, odvolání, soudní přezkum, vymáhání a evidenci bodů. Z podkladů zjisti doručení každého úkonu; datum vyhotovení není automaticky okamžik právních účinků.

Nejprve ze znění předpisu ověřeného v e-Sbírce (`par --k`) stanov lhůty odporu, odvolání, žaloby, kasačního prostředku a zvláštních námitek. Odděl je od promlčení odpovědnosti, lhůt orgánu a vymáhání. Ani možný zánik odpovědnosti neodůvodňuje opomenutí včasného procesního prostředku. U neúplného rozhodnutí odliš doloženou vadu od otázky, kterou lze potvrdit teprve úplným spisem; žalobní námitku formuluj podmíněně a konkrétně.

## Právní rámec

V SLV a e-Sbírce vyhledej zákon o odpovědnosti za přestupky, některých přestupcích, správní řád, správní soudnictví, kontrolní řád a skutečně relevantní sektorový zákon. U dopravy přidej silniční provoz, vozidla, metrologii a vyšetření návykových látek; u jiných věcí stavební, živnostenskou, spotřebitelskou, pracovněprávní, reklamní, finanční nebo environmentální regulaci. V lidskoprávních pramenech a judikatuře ověř dopad trestních záruk, nikoli pouze tematický odkaz.

Porovnej znění v době skutku a relevantní pozdější režimy včetně přechodných ustanovení a příznivější úpravy. Zákaz retroaktivity, porovnání zákona a soudní přezkum časové změny mají vlastní podmínky. Nevytvářej kombinaci nejvýhodnějších jednotlivých ustanovení bez právní opory. Sazby, body, hranice a lhůty načti včetně příloh a zvláštních odchylek.

## Znaky a důkazy

U každého znaku skutkové podstaty uveď, co tvrdí orgán, jaký má důkaz, kdo nese břemeno a jaká je konkrétní obrana. U fyzické osoby prověř zavinění, omyl, věk, příčetnost, krajní nouzi a obranu. U společnosti a podnikatele odděl přičitatelnost od liberačního úsilí; formální směrnice sama neprokazuje reálnou kontrolu. Prověř přechod odpovědnosti a zánik osoby; zánik, přeměnu a právního nástupce ověř ve `verejny_rejstrik` (zahrnuje vymazané osoby) a `obchodni_rejstrik`. Skutečné školení, dohled a nápravu musí dokládat podklady, ne model.

Zkoumej totožnost a dostatečné vymezení skutku, pokračování, trvání, hromadnost, souběh a poměr k trestnímu či kázeňskému řízení. Pro ne bis in idem porovnej konkrétní skutkové okolnosti, právní moc, povahu sankcí a případné podmínky přípustného souběhu; neodvozuj výsledek z pouhého dvojího spisu.

U důkazů rozliš záznam o podání vysvětlení, jiné policejní listiny, protokol, výpověď, fotografii, měření a soukromou nahrávku. Nevylučuj všechny policejní záznamy paušálně ani je nepovažuj samotné za rozhodující. U měřidla ověř podklady ke konkrétní metodě, ověření, nejistotě, obsluze, místu a identitě vozidla. U alkoholu a jiných látek nepracuj s pevnou tolerancí nebo univerzální trestní hranicí bez pramene a odborného podkladu.

Prověř právo mlčet, zákaz sebeobviňování, tlumočení, zastoupení, nahlížení, ústní jednání, výslech svědků, kladení otázek a vyjádření k podkladům. Vadu spoj s jejím skutečným dopadem; ne každá procesní nedokonalost automaticky znamená nicotnost či zrušení.

## Promlčení, trest a proces

Sestav úplnou osu promlčení: okamžik dokonání či ukončení, správná délka podle sazby a zvláštního zákona, zákonné stavení a přerušení, nové běhy a konečná hranice. U prvního procesního aktu zjisti, zda a kdy právně působil; nezaměňuj oznámení a vydání různých druhů rozhodnutí.

U trestu prověř zákonný druh, rozpětí, povinnost uložit, závažnost, zavinění, polehčující a přitěžující okolnosti, recidivu, poměry a odůvodnění. Zvaž upuštění, podmíněné upuštění, mimořádné snížení, společný trest, započtení zadržení, propadnutí, zabrání, zveřejnění a ochranné opatření podle konkrétních podmínek. Náklady řízení ani náhrada škody nejsou druhem trestu; vypočti je samostatně podle rozhodného předpisu.

Po odporu porovnej druh a výměru s příkazem a načti ochranné pravidlo i výjimku změněné kvalifikace. Nepředpokládej automatické obecné zvýšení trestu. Příkaz na místě vyžaduje samostatnou analýzu souhlasu, právní moci a možností přezkumu. U odvolání ověř zákaz změny v neprospěch, nové důkazy, blanketní podání a doplnění. U přezkumu a obnovy rozliš návrh, podnět a subjektivní nárok na zahájení.

V žalobě vymez včas konkrétní body, petit a podle cíle samostatný odkladný účinek či moderaci. U kasace ověř zastoupení, lhůtu, přípustnost a přijatelnost podle aktuálního rozsahu, nikoli historické výjimky. Podnět k přezkumu nenahrazuje řádný opravný prostředek.

## Typové dopady a výstup

U dopravy odděl řidiče a provozovatele, určenou částku, pokutu, zákaz činnosti, zadržení průkazu a body. Námitky proti záznamu bodů mají vlastní rozsah a účinky; zvláštní časové pravidlo nepředstavuj bez ověření jako univerzální prekluzi. U vrácení oprávnění a upuštění od zbytku ověř potřebná vyšetření a přezkoušení. U občanského soužití prověř souhlas dotčené osoby, u majetku hranici trestného činu a recidivu, u veřejného pořádku zákonnost výzvy a místní normu.

Dodej doporučenou obranu, nejsilnější protiargument, konkrétní podání, výpočet promlčení, sankční a nákladovou tabulku a potřebné důkazy. U podniku připoj skutečný nápravný plán bez přiznání nedoloženého skutku. Nikdy nedoplňuj řidiče, dokument školení nebo kalibraci. Rešerši judikatury prováděj v SLV (`nss`, `us`, u hranice trestného činu i `ns`), judikaturu ESLP v HUDOC; přiznaná mezera nezbavuje povinnosti dodat použitelný výstup v doložitelném rozsahu.
