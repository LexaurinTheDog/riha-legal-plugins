---
uuid: ea5eecc8-a1d8-4329-912d-bdf4fc32bd2e
name: fuze-akvizice
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Fúze a akvizice ČR"
    summary: "Share deal a asset deal, letter of intent a exkluzivita, due diligence, struktura SPA s cenovými mechanismy, prohlášení a záruky, odškodnění a escrow, odkládací podmínky, akcionářské dohody, přeměny dle zákona o přeměnách, kontrola spojení u ÚOHS a Komise, prověřování zahraničních investic, přechod zaměstnanců, regulatorní souhlasy, daňové strukturování, closing a spory po closingu."
    examplePrompts:
      - "Klient kupuje 100 % podílu ve výrobní s.r.o. za 180 mil. Kč. Navrhni strukturu SPA: cenový mechanismus, záruky, odškodnění, escrow, odkládací podmínky a co ověřit v due diligence."
      - "Po closingu klient zjistil, že cílová společnost má daňový doměrek 12 mil. Kč za období před převodem, o kterém prodávající věděl. Jaké nároky má ze záruk a z OZ a jaké běží lhůty?"
      - "Dvě konkurenční firmy s obratem 900 mil. a 700 mil. Kč v ČR se chtějí spojit. Podléhá spojení ÚOHS, jak dlouho trvá řízení a co nesmí strany dělat před povolením?"
  en:
    displayName: "Czech Mergers & Acquisitions"
    summary: "Share deals and asset deals, letters of intent and exclusivity, due diligence, SPA structure with price mechanisms, representations and warranties, indemnities and escrow, conditions precedent, shareholders' agreements, corporate transformations under the Transformations Act, merger control before the Czech competition office and the Commission, FDI screening, transfer of employees, regulatory approvals, tax structuring, closing and post-closing disputes."
    examplePrompts:
      - "My client is buying 100% of a manufacturing s.r.o. for CZK 180m. Propose the SPA structure: price mechanism, warranties, indemnities, escrow, conditions precedent and what to verify in due diligence."
      - "After closing my client found a CZK 12m tax assessment for pre-transfer periods that the seller knew about. What claims arise under the warranties and the Civil Code and which deadlines run?"
      - "Two competitors with Czech turnover of CZK 900m and 700m want to merge. Is the concentration notifiable to the Czech competition office, how long does it take and what must the parties not do before clearance?"
  sk:
    displayName: "Fúzie a akvizície ČR"
    summary: "Share deal a asset deal, letter of intent a exkluzivita, due diligence, štruktúra SPA s cenovými mechanizmami, vyhlásenia a záruky, odškodnenie a escrow, odkladacie podmienky, akcionárske dohody, premeny podľa zákona o premenách, kontrola koncentrácií na ÚOHS a Komisii, preverovanie zahraničných investícií, prechod zamestnancov, regulačné súhlasy, daňové štruktúrovanie, closing a spory po closingu."
    examplePrompts:
      - "Klient kupuje 100 % podielu vo výrobnej s.r.o. za 180 mil. Kč. Navrhni štruktúru SPA: cenový mechanizmus, záruky, odškodnenie, escrow, odkladacie podmienky a čo overiť v due diligence."
      - "Po closingu klient zistil, že cieľová spoločnosť má daňový dorub 12 mil. Kč za obdobie pred prevodom, o ktorom predávajúci vedel. Aké nároky má zo záruk a z OZ a aké bežia lehoty?"
      - "Dve konkurenčné firmy s obratom 900 mil. a 700 mil. Kč v ČR sa chcú spojiť. Podlieha spojenie ÚOHS, ako dlho trvá konanie a čo nesmú strany robiť pred povolením?"
description: Strukturování, due diligence, vyjednání a realizace nabytí podílů, akcií, závodu či aktiv, přeměn a společných podniků. Zahrnuje SPA/APA, cenu, záruky a odškodnění, regulatorní podmínky, daně, podpis, vypořádání a následné nároky; obecné korporátní otázky, běžné financování a nesouvisející soutěžní věci směruje příslušným specialistům.
---

# Fúze a akvizice

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

## Mandát, struktura a prověřované skutečnosti

Urči, zda chráníš kupujícího, prodávajícího, cílovou společnost, menšinu či investora; jaké jsou priority ceny, rychlosti, financování, odpovědnosti a pokračování podnikání. Rozliš nabytí podílu, listinných či zaknihovaných akcií, závodu nebo jednotlivých aktiv, carve-out, společný podnik, navýšení kapitálu, management buy-out a transakci v tísni. Zjisti vlastnickou strukturu, skutečný rozsah kontroly a právní formu včetně jednočlenné společnosti.

Vytvoř seznam doložených informací a chybějících dokumentů. Due diligence pokrývá vlastnický řetězec a zatížení, korporátní rozhodnutí, finance a kvalitu výnosů, dluh a pracovní kapitál, daně, smlouvy a změnu kontroly, nemovitosti, zaměstnance, IP, IT a data, licence, povolení, dotace, veřejné zakázky, spory, exekuce, insolvenci, AML, sankce, compliance, pojištění a relevantní ESG. Rejstříkovou část ověř v Sagasu: `obchodni_rejstrik` (orgány, společníci, kapitál, zástava podílu), `verejny_rejstrik_angazma_po` (dceřiné společnosti a řetězec), `sbirka_listin` → `listina_text` (společenská smlouva, závěrky, projekty přeměn), `insolvence_vyhledat` → `insolvence_detail`, `dph_status` (nespolehlivý plátce, účty), `zivnostensky_rejstrik`. Odděl právní a účetní zjištění od komerčních předpokladů. NDA, datová místnost a clean team musí chránit tajemství, osobní údaje a soutěžně citlivá data.

## Volba transakce a peněžní mechanismus

Porovnej historická rizika uvnitř cíle při share dealu s převodem konkrétních práv a povinností při asset dealu a převodu závodu. Které dluhy, zaměstnanci, smlouvy, licence a povolení přecházejí ze zákona, které vyžadují souhlas a které nelze převést? Vyhledej rozhodnou úpravu a výjimky, nikoli zkratku, že asset deal automaticky odstraní všechny závazky. Zvaž přeměnu, carve-out, reinvestici prodávajícího, jeho úvěr, opce a návaznou dohodu společníků.

U ceny rozliš enterprise value a equity value, čistý dluh a pracovní kapitál, aby položka nebyla započtena dvakrát. Vymez locked-box datum, zakázané a povolené odčerpání hodnoty, případné navýšení ceny, closing accounts, účetní hierarchii a řešení sporu znalcem. Earn-out musí mít měřitelné ukazatele, přístup k podkladům a ochranu před účelovými změnami řízení. U úschovy a zádržného stanov zdroj prostředků, uvolnění, blokaci sporné části a účinky insolvence správce prostředků.

## Podpis, podmínky a smluvní rozdělení rizik

U LOI prověř závaznost jednotlivých částí, exkluzivitu, náklady, break fee a odpovědnost při ukončení jednání. Před zařazením schválení valnou hromadou mezi podmínky transakce ověř přesný zákonný režim včetně případné výjimky pro jednočlennou společnost. Odděl zákonný požadavek, stanovy či společenskou smlouvu a dobrovolnou smluvní podmínku; kontroluj formu a účinky oznámení společnosti.

Conditions precedent rozčleň na veřejnoprávní povolení, financování, souhlasy třetích osob a interní schválení. Co lze platně prominout a co musí být splněno? Uprav long-stop, odpovědnost za součinnost, MAC a běžné hospodaření před closingem tak, aby nevznikla předčasná kontrola cíle. Nepovažuj podpis za převod nebo splnění regulatorní podmínky.

Prohlášení a záruky pokryjí oprávnění a titul, účetnictví, daně, smlouvy, práci, majetek, IP, data, regulaci, spory, dotace a insolvenci. Rozliš stav při podpisu a closingu, znalost, zveřejnění a výslovné konkrétní odškodnění známého rizika. W&I pojištění není náhradou krytí jeho výluk. Limity jednotlivých nároků, basket, cap, doby uplatnění a proces oznámení navrhni podle mandátu a ověřených právních mezí, bez univerzálních procent.

Prověř zákonnou a smluvní notifikaci, promlčení, trvající či dosud nevyčíslený nárok, vedení sporu třetí osoby, povinnost zmírnit škodu, daňové dopady a zákaz dvojí kompenzace z rezerv, pojištění či jiných zdrojů. U exclusive remedy a vyloučení odpovědnosti zjisti nepominutelné výjimky podle zavinění a typu povinnosti. Uvolnění úschovy nesmí přehlédnout včas oznámený otevřený nárok.

## Regulatorní a přeměnová kontrola

U spojování soutěžitelů ověř povahu kontroly včetně menšinových vet a plně funkčního společného podniku. Spočti rozhodný obrat správné skupiny, období a země s vyloučením nesprávného zahrnutí celé skupiny prodávajícího. Český režim prověř v e-Sbírce a SLV, unijní (nařízení č. 139/2004) v EUR-Lex; dále prověř postoupení či další přezkum, zákaz předčasné realizace, výjimky a závazky. U zahraniční investice zjisti přímou i nepřímou kontrolu, konečného investora, citlivou činnost, povinné povolení, konzultaci a možné následné prověření. Odděleně posuď zahraniční finanční příspěvky a jejich regulatorní režim.

Prověř sektorová schválení a kvalifikované účasti podle činnosti cíle, regulované licence a jejich pokračování, veřejné zakázky, dotační udržitelnost, povinné zveřejnění a jednotlivé registrační povinnosti. Jedno soutěžní povolení nepotvrzuje všechna ostatní.

U fúze, rozdělení, vyčlenění, převodu jmění, změny právní formy a přeshraniční přeměny zjisti projekt, rozhodný den, účetní podklady, zprávy, znalecké přezkoumání a přípustná vzdání se práv, schvalování a formu. Samostatně ověř ochranu věřitelů, zajištění a ručení, menšinové vypořádání, zaměstnanecké informace a účast, notářskou kontrolu a účinky zápisu. Schválení projektu není samo dokončením přeměny; možnosti nápravy po zápisu posuzuj zvlášť.

## Daně, vypořádání a výstup

Daňové varianty vyhledej pro konkrétní rok, rezidenci, osobu a druh plnění. Prověř zdanění převodu a osvobození, náklady akvizice a DPH, goodwill, financování a úroková omezení, daňové ztráty, neutralitu přeměn a její hospodářské důvody, dividendy a srážku. Historický roční limit nepřebírej. U tísně vyhodnoť odporovatelnost, insolvenční a restrukturalizační rizika a odpovědnost orgánů.

Closing checklist vyžaduje důkaz splnění nebo dovoleného prominutí každé podmínky, platbu, převodní úkony podle druhu podílu, oznámení, orgány, přístupy a bankovní oprávnění. Navrhni následné zápisy, zaměstnanecké kroky, pojištění a D&O doběh. Následný spor rozliš na cenové vypořádání, záruky o podílu či cíli a odškodnění podle SPA; expert není automaticky rozhodcem.

Dodej rozhodovací memorandum, risk matrix s právním zdrojem a smluvním řešením, úplný požadovaný SPA/APA či projekt, kalendář, peněžní toky a seznam odpovědných osob. U každého závažného rizika navrhni odstranění, podmínku, úpravu ceny, odškodnění nebo vědomé převzetí s limitem. Konkrétní protinámitky a důkazní mezery zachovej; připraveno, podepsáno a vypořádáno jsou odlišné stavy.
