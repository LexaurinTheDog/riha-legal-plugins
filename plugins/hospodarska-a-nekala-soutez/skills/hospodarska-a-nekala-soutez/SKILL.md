---
uuid: 2914684d-f296-46fe-b4a9-452343588299
name: hospodarska-a-nekala-soutez
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Hospodářská a nekalá soutěž ČR"
    summary: "Kartely, zneužití dominance, spojování soutěžitelů a řízení před ÚOHS, náhrada škody, nekalá soutěž a její nároky, regulace reklamy a nekalé obchodní praktiky."
    examplePrompts:
      - "Distributor nám v e-mailu píše, ať nedáváme cenu pod jeho doporučenou. Je to problém a co s tím?"
      - "Konkurent v reklamě tvrdí, že náš výrobek je nebezpečný. Jaké nároky máme a jak rychle?"
      - "ÚOHS provedl u klienta místní šetření. Jaká má klient práva a co dělat v prvních dnech?"
  en:
    displayName: "Czech Competition and Unfair Competition"
    summary: "Cartels, abuse of dominance, merger control and ÚOHS proceedings, damages, unfair competition claims, advertising regulation and unfair commercial practices."
    examplePrompts:
      - "A distributor e-mails us not to price below its recommended price. Is that a problem and what to do?"
      - "A competitor's advertising claims our product is dangerous. Which claims do we have and how fast?"
      - "The ÚOHS carried out a dawn raid at the client's premises. What are the client's rights and what to do in the first days?"
  sk:
    displayName: "Hospodárska a nekalá súťaž ČR"
    summary: "Kartely, zneužitie dominancie, koncentrácie a konanie pred ÚOHS, náhrada škody, nekalá súťaž a jej nároky, regulácia reklamy a nekalé obchodné praktiky v ČR."
    examplePrompts:
      - "Distribútor nám v e-maile píše, aby sme nedávali cenu pod jeho odporúčanú. Je to problém a čo s tým?"
      - "Konkurent v reklame tvrdí, že náš výrobok je nebezpečný. Aké nároky máme a ako rýchlo?"
      - "ÚOHS vykonal u klienta miestne šetrenie. Aké má klient práva a čo robiť v prvých dňoch?"
description: Veřejnoprávní ochrana hospodářské soutěže, soukromoprávní nekalá soutěž a navazující reklamní regulace. Kartely, vertikální omezení, dominance, spojování soutěžitelů, místní šetření, compliance, náhrada soutěžní škody, významná tržní síla a smluvní náprava ve prospěch klienta.
---

# Hospodářská a nekalá soutěž

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

## Vymezení větví a rozhodných skutečností

Rozliš veřejnoprávní soutěžní dohled, soukromoprávní ochranu před nekalou soutěží a ochranu spotřebitele či regulaci reklamy. Stejné jednání může vyžadovat více samostatných testů, příslušných orgánů a procesních prostředků. Zjisti postavení klienta: vyšetřovaný soutěžitel, dodavatel, distributor, dominantní podnik, poškozený konkurent, zákazník, asociace nebo účastník spojení. Definuj požadovaný výsledek, naléhavost a obchodní zájem, který má být zachován.

Zmapuj produkty, geografii, zákazníky, distribuční model, skupinu, tok informací, dohodnuté a skutečné chování, relevantní období a důkazy. Obraty, podíly, dominanci, cenový dopad ani účast na kartelu nedoplňuj odhadem bez označení. Rozhodné české normy a prováděcí úpravu pro příslušné období ověř v e-Sbírce, unijní normy a soft law v EUR-Lex, judikaturu v SLV (`nss` pro přezkum rozhodnutí ÚOHS) a CURIA; u soft law odděl právní sílu od závazných předpisů.

## Dohody, výjimky a obchodní omezení

U horizontální dohody, bid riggingu, výměny informací, rozhodnutí asociace, hub-and-spoke a vertikálního vztahu zjisti, zda existuje dohoda či koordinace, mezi jakými subjekty a o čem. Jde o omezení podle cíle, nebo je třeba dokazovat účinky? Je dotčen obchod mezi členskými státy? Jak jsou vymezeny relevantní trh, hospodářská jednotka a případná agentura nesoucí skutečné riziko?

U blokové výjimky vyhledej její aktuální věcnou, osobní a časovou působnost, podmínky, zakázaná omezení a relevantní přechodná pravidla. Ztráta výjimky není sama závěrem o protiprávnosti ani neplatnosti celé smlouvy. Samostatně zvaž individuální výjimku, prokázané efektivity, prospěch zákazníků, nezbytnost a zachování soutěže; pravidlo zanedbatelnosti nepoužívej plošně na zakázané cíle.

U cen dalšího prodeje prověř nejen znění, ale i pobídky, sankce, monitoring, e-maily a vynucování. U doporučené nebo maximální ceny nestačí název. Rozliš aktivní a pasivní prodej, výhradní a selektivní systém, zákazníky, území, tržiště a účinné využívání internetu. Prověř dvojí ceny, parity a sdílení informací při duální distribuci. U zákazu konkurence odděl trvání a období po skončení, automatické obnovování, skutečnou možnost výpovědi, náklady změny dodavatele a ochranu know-how. Navrhni proveditelnou náhradu každé problematické klauzule.

## Dominance, spojování a zvláštní trhy

Relevantní trh vymez podle zastupitelnosti, poptávky, nabídky a dostupných dat; případný cenový test označ za metodický nástroj, nikoli fiktivně provedené měření. Jaké skutečnosti podporují dominanci vedle podílu a jaký význam mají bariéry vstupu či vyjednávací síla odběratelů? Prověř diskriminaci, nepřiměřené ceny a podmínky, predaci, věrnostní slevy, vázání, odmítnutí dodávek a stlačení marží podle jejich samostatných znaků a objektivních ospravedlnění.

U digitálních trhů odděl soutěžní právo od zvláštního režimu určených poskytovatelů. U významné tržní síly a potravinových obchodních praktik ověř osoby, produkty, vztah stran, zakázané praktiky a smluvní požadavky; nepřenášej závěry automaticky na jiné sektory.

U spojení prověř vznik či změnu kontroly, společný podnik, správný rozsah skupinových obratů a rozhodné období; skupinu zmapuj přes `verejny_rejstrik_angazma_po` a `obchodni_rejstrik`, obraty dolož z účetních závěrek (`sbirka_listin` → `listina_text`). Zjisti českou a unijní příslušnost, postoupení, případné další přezkumné mechanismy, zákaz uskutečňování před povolením, výjimky a závazky. Nezaměňuj právní podpis smlouvy s převzetím faktické kontroly.

## Šetření, obhajoba a sankce

Při místním šetření navrhni okamžitý protokol: ověření pověření a rozsahu, přítomnost právní pomoci, odpovědné osoby, záznam úkonů, ochrana důvěrných materiálů a kontrola kopií. Jaké pravomoci má orgán ke vstupu, vysvětlením, elektronickým datům a vzdáleným úložištím? Jak se v konkrétním režimu chrání komunikace s advokátem? Nenavrhuj mazání, ukrývání ani maření důkazů. Sporný postup řeš doloženou námitkou a příslušným přezkumem.

Odděl sektorové šetření od řízení proti konkrétnímu subjektu. U leniency vyhledej pořadí, rozsah spolupráce, překážky a podmínky výsledku; bez rozhodnutí neslibuj imunitu. Narovnání a závazky porovnej podle uznání skutku, procesních práv, sankce, soukromých žalob a publicity. Sankční výpočet vyžaduje ověřený základ, období, přičitatelnost, přitěžující a polehčující okolnosti; odděl odpovědnost právnických a fyzických osob a dopady do veřejných zakázek. Připrav řádné a soudní opravné prostředky včetně lhůt a případné dočasné ochrany.

## Nekalá soutěž, reklama a náhrada škody

U nekalé soutěže nejdříve ověř obecné předpoklady, potom konkrétní skutkovou podstatu. Prověř klamavou a srovnávací reklamu, vyvolání záměny, parazitování, podplácení, zlehčování, obchodní tajemství, dotěrné či agresivní praktiky. Pravdivost jednotlivého údaje neprokazuje přípustnost celé reklamy. Zvlášť řeš influencery, environmentální tvrzení a výrobkové sektory s vlastními reklamními omezeními; budoucí unijní změnu neprezentuj jako již použitelnou.

Kdo má aktivní legitimaci a proti komu nárok směřuje? Kdy se mění důkazní břemeno? Odděl zdržení, odstranění závadného stavu, přiměřené zadostiučinění, škodu a bezdůvodné obohacení. Navrhni určitý petit, předběžné opatření a zajištění důkazu s ověřenými podmínkami jistoty, příslušnosti a nákladů.

U soutěžní škody vyhledej účinky rozhodnutí orgánu, případnou domněnku újmy, zpřístupnění důkazů, přenesení navýšení ceny, solidaritu a regres. Výši újmy založ na vysvětleném kontrafaktuálním scénáři a skutečných datech. Ověř počátek a stavění promlčení i vztah kolektivního, veřejnoprávního a individuálního řízení.

## Požadovaný výstup

Dodej oddělené závěry pro každou právní větev, důkazní mapu, nejsilnější protiargumenty, realistické nápravné varianty a přesné podání nebo smluvní redline podle zadání. Každá klauzule musí mít použitelnou náhradu, která chrání legitimní obchodní účel klienta; pouhé označení rizika nestačí. Compliance plán pokryje cenovou komunikaci, asociace, školení, šetření, hlášení incidentů a soutěžní DD. U praxe příslušného senátu uváděj jen skutečně prověřené rozhodování, jeho relevantní odlišnosti a nevyplněná místa.
