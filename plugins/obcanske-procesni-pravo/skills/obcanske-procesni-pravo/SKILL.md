---
uuid: 66f31eeb-2f0d-4023-bde4-6c9f8d3eb0f6
name: obcanske-procesni-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Občanské procesní právo ČR"
    summary: "Pravomoc a příslušnost, sepis žaloby a petitu, soudní poplatky, doručování a lhůty, dokazování a důkazní břemeno, rozsudek pro zmeškání a platební rozkaz, předběžná opatření, odvolání a mimořádné opravné prostředky včetně přípustnosti dovolání, náklady řízení a advokátní tarif, nesporná řízení."
    examplePrompts:
      - "Rozsudek odvolacího soudu byl doručen do datové schránky 3. 6. a klient ho otevřel 15. 6. Do kdy běží lhůta pro dovolání a jak správně vymezit přípustnost podle § 237?"
      - "Žalovaný se nedostavil k prvnímu jednání a soud vydal rozsudek pro zmeškání. Jaké jsou možnosti obrany a lhůty?"
      - "Připrav petit a strukturu žaloby na zaplacení 480 000 Kč s příslušenstvím z nezaplacené faktury, včetně výpočtu soudního poplatku a nákladů."
  en:
    displayName: "Czech Civil Procedure"
    summary: "Jurisdiction and venue, drafting claims and petitions, court fees, service and deadlines, evidence and burden of proof, default judgments and payment orders, interim measures, appeals and extraordinary remedies including admissibility of dovolání, costs and attorney tariff, non-contentious proceedings."
    examplePrompts:
      - "The appellate judgment was delivered to the data box on 3 June and opened on 15 June. When does the deadline for an appeal on points of law expire and how to frame admissibility under § 237?"
      - "The defendant did not attend the first hearing and the court issued a default judgment. What are the remedies and deadlines?"
      - "Draft the relief sought and structure of a claim for CZK 480,000 with accessories from an unpaid invoice, including the court fee and costs calculation."
  sk:
    displayName: "Občianske procesné právo ČR"
    summary: "Právomoc a príslušnosť, spísanie žaloby a petitu, súdne poplatky, doručovanie a lehoty, dokazovanie a dôkazné bremeno, rozsudok pre zmeškanie a platobný rozkaz, predbežné opatrenia, odvolanie a mimoriadne opravné prostriedky vrátane prípustnosti dovolania, trovy konania a advokátska tarifa, nesporové konania."
    examplePrompts:
      - "Rozsudok odvolacieho súdu bol doručený do dátovej schránky 3. 6. a klient ho otvoril 15. 6. Dokedy plynie lehota na dovolanie a ako správne vymedziť prípustnosť podľa § 237?"
      - "Žalovaný sa nedostavil na prvé pojednávanie a súd vydal rozsudok pre zmeškanie. Aké sú možnosti obrany a lehoty?"
      - "Priprav petit a štruktúru žaloby na zaplatenie 480 000 Kč s príslušenstvom z nezaplatenej faktúry, vrátane výpočtu súdneho poplatku a trov."
description: 'Použij pro civilní sporné, zvláštní a hromadné řízení: pravomoc, příslušnost, žalobu a petit, doručování, lhůty, dokazování a koncentraci, platební rozkazy, uznání a zmeškání, předběžná opatření, odvolání a dovolání, obnovu a zmatečnost, soudní poplatky, tarifní náklady, průtahy a spravedlivý proces.'
---

# Občanské procesní právo ČR

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

## Fáze, rozhodnutí a nejbližší úkon

Nejprve zjisti klienta, účastníky, zastoupení, soud, typ a fázi řízení, požadovanou ochranu a všechny napadené výroky. Účastníka-PO ověř `obchodni_rejstrik` (zaniklého `verejny_rejstrik`), probíhající insolvenci účastníka `insolvence_vyhledat` a ID datové schránky soudu či účastníka `datova_schranka_vyhledat`. Z podkladů odděl datum vyhotovení, vyhlášení, dodání do schránky, právně účinného doručení, právní moci a vykonatelnosti. Komu a jak bylo doručováno, byl ustanoven zástupce, je k dispozici úplná doručenka a poučení? Lhůtu nepočítej automaticky od data dokumentu ani vždy od doručení: nejprve vyhledej skutečný zákonný spouštěč.

V SLV a e-Sbírce vyhledej občanský soudní řád, zvláštní soudní řízení, soudní poplatky včetně sazebníku, advokátní tarif, elektronické úkony, hromadné řízení, soudy a soudce, mediaci, výkon a odpovědnost veřejné moci. Podle povahy sporu přidej hmotný zákon a přeshraniční instrument. Prověř přechodná pravidla podle zahájení řízení i konkrétního úkonu, nikoli jen dnešní verzi.

## Podmínky řízení a volba prostředku

Odděl pravomoc, věcnou a místní příslušnost, procesní způsobilost, zastoupení, legitimaci a důvodnost. U místní příslušnosti projdi výlučný režim před obecným, případnou volbu a prorogaci. U rozhodčí smlouvy ověř rozsah a okamžik námitky. U cizího prvku nepřejdi přímo k tuzemskému obecnému soudu. Prověř litispendenci, rozhodnutou věc, podjatost a zákonné obsazení soudu.

Porovnej žalobu na plnění, určení nebo jiný druh ochrany, platební rozkaz, elektronický platební rozkaz a hromadné řízení. Výši nároku nepovažuj bez načteného pravidla za limit formulářového řízení. U určovací žaloby konkrétně vysvětli právní zájem a vztah k žalobě na plnění. U předžalobní výzvy ověř obsah, adresu, odeslání, interval a možné výjimky nákladového následku. Samostatně posuď promlčení, zajištění důkazu, předběžné opatření, jeho jistotu a odpovědnost za újmu.

## Podání, doručování a dokazování

Žaloba musí spojit rozhodující skutky, jednotlivé nároky a důkazy s určitým vykonatelným petitem. Rozliš hlavní, eventuální a alternativní návrh. U platební povinnosti uveď konkrétní příslušenství a počátek i délku plnění odpovídající požadovanému rozhodnutí; neurčité jak stanoví soud není hotový petit. U nepeněžité povinnosti přesně urč adresáta, předmět, rozsah a čas. Kontroluj změnu, zpětvzetí, vzájemný návrh, započtení a procesní nástupnictví podle jejich vlastních pravidel.

Pro každý způsob podání vyhledej formu, podpis, doplnění, příslušného příjemce a okamžik zachování lhůty. Pro fikci doručení a konec lhůty samostatně prověř pracovní dny, svátky, vyloučení fikce, neúčinnost a případnou nápravu. Předlož řetězec právní událost–počátek–běh–konec–způsob včasného úkonu. Neznámé doručení nevyřeš vymyšleným datem.

Zmapuj povinnost tvrzení a důkazní břemeno podle konkrétního titulu, domněnek a ochranných pravidel, nikoli sloganem kdo tvrdí, prokazuje. Prověř koncentraci, poučení, přípravné a první jednání, výjimky novot a návrhy na doplnění. Rozliš soukromou a veřejnou listinu, výslech svědka a účastníka, odborné vyjádření a znalecký posudek, soukromý posudek s potřebnou doložkou, ohledání a nahrávku s testem přípustnosti. Opomenutý důkaz nebo překvapivý závěr konkrétně spoj s dopadem na obranu.

## Rozhodnutí a opravné prostředky

Platební rozkaz, rozsudek pro uznání a pro zmeškání kontroluj odděleně. U kvalifikované výzvy prověř doručení, poučení, obsah reakce a překážky. U zmeškání odděl odvolání proti vadným předpokladům od návrhu na zrušení pro omluvitelný důvod; jejich lhůty a účinky neslučuj. Prověř smír, přerušení, zastavení, opravu a doplnění rozhodnutí.

U odvolání zjisti subjektivní i objektivní přípustnost, rozsah, důvody, novoty, vázanost, odkladný účinek a návrh na změnu či zrušení. Bagatelní výluku, poučení a zvláštní režim vždy načti. U dovolání odděl právní otázku, závislost napadeného rozhodnutí na jejím řešení, konkrétní variantu přípustnosti a dovolací důvod. Připoj skutečně ověřené srovnání s rozhodovací praxí; skutkový nesouhlas nevydávej za právní otázku. Prověř výluky, povinné zastoupení, lhůtu, doplnění a odklad.

U obnovy, zmatečnosti, ústavní ochrany a průtahů ověř samostatné důvody, legitimaci, lhůty a vyčerpání prostředků. Zvaž návrh na určení lhůty a odpovědnost státu odděleně. U nesporného, rodinného, pracovního, spotřebitelského a insolvenčního sporu nepřenášej obecná pravidla bez zvláštní kontroly.

## Náklady a hotový dokument

Nejprve rozhodni nákladový základ: úspěch, procesní zavinění, výzva, úvaha soudu, moderace, náklady státu a nezastoupeného účastníka. Pak spočti každý úkon podle jeho data, tarifní hodnoty a sazby v Sagasu `odmena_advokata` a doplň rozsah, paušál, cestovné, čas a podmínky DPH. Pro každý samostatný návrh spočti poplatek `soudni_poplatek` a ověř osvobození, splatnost, následky neplacení a vrácení; zákonný úrok z prodlení v příslušenství spočti `urok_z_prodleni`; jistotu veď zvlášť. Historické příklady částek nejsou aktuální sazebník.

Dodej požadované podání, přílohový seznam, výpočet a strategii s protiargumenty, nikoli pouze osnovu. U přípravy jednání připoj pořadí důkazů, reakce na námitky a praxi skutečně identifikovaného senátu, je-li zadána. Při převodu dokumentu ověř skutečnou funkčnost odkazů v souboru; vzhled citace nenahrazuje hyperlink. Připravený dokument, odeslání a podání soudu označ jako rozdílné stavy.
