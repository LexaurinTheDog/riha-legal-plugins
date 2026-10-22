---
uuid: 780180e9-2aca-4484-b30a-6e8c2bd28510
name: startupy-investice-esop
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Startupy, investice a ESOP ČR"
    summary: "Založení a cap table, zakladatelské dohody a vesting, konvertibilní zápůjčky a SAFE, seed a VC kola s akcionářskou dohodou, likvidační preference, anti-dilution a drag/tag, zaměstnanecké akcie a opční plány včetně českého daňového odkladu, převod IP a zaměstnanecká díla, zákaz konkurence a mlčenlivost, dotace a odpočet na výzkum, crowdfunding a limity veřejné nabídky, exit a zdanění zakladatelů."
    examplePrompts:
      - "Tři zakladatelé s.r.o. chtějí nastavit vesting 4 roky s 1 rokem cliff, ochranu při odchodu „bad leaver“ a přípravu na seed kolo. Jak to strukturovat v české s.r.o. a co dát do společenské smlouvy versus akcionářské dohody?"
      - "Angel investor nabízí konvertibilní zápůjčku 5 mil. Kč s 20% slevou a cap 60 mil. Kč. Zreviduj term sheet, navrhni mechanismus konverze v s.r.o. a daňové dopady pro obě strany."
      - "Klient chce zavést ESOP pro 15 zaměstnanců v s.r.o. Jaké jsou varianty (opce na podíl, phantom, nová třída podílu), jak funguje daňový odklad od 2024/2025 a co musí zaměstnavatel oznámit?"
  en:
    displayName: "Czech Startups, Investments & ESOP"
    summary: "Founding and cap table, founders' agreements and vesting, convertible loans and SAFE-type instruments, seed and VC rounds with shareholders' agreements, liquidation preference, anti-dilution and drag/tag, employee share and option plans including Czech tax deferral, IP assignment and employee works, non-compete and confidentiality, grants and R&D deductions, crowdfunding and public-offer limits, exits and founder taxation."
    examplePrompts:
      - "Three founders of an s.r.o. want 4-year vesting with a 1-year cliff, bad-leaver protection and preparation for a seed round. How to structure it in a Czech s.r.o. and what belongs in the articles versus the shareholders' agreement?"
      - "An angel offers a CZK 5m convertible loan with a 20% discount and a CZK 60m cap. Review the term sheet, propose the conversion mechanics in an s.r.o. and the tax consequences for both sides."
      - "My client wants an ESOP for 15 employees in an s.r.o. What are the options (share options, phantom shares, a new share class), how does the 2024/2025 tax deferral work and what must the employer notify?"
  sk:
    displayName: "Startupy, investície a ESOP ČR"
    summary: "Založenie a cap table, zakladateľské dohody a vesting, konvertibilné pôžičky a SAFE, seed a VC kolá s akcionárskou dohodou, likvidačná preferencia, anti-dilution a drag/tag, zamestnanecké akcie a opčné plány vrátane českého daňového odkladu, prevod IP a zamestnanecké diela, zákaz konkurencie a mlčanlivosť, dotácie a odpočet na výskum, crowdfunding a limity verejnej ponuky, exit a zdanenie zakladateľov."
    examplePrompts:
      - "Traja zakladatelia s.r.o. chcú nastaviť vesting 4 roky s 1 rokom cliff, ochranu pri odchode „bad leaver“ a prípravu na seed kolo. Ako to štruktúrovať v českej s.r.o. a čo dať do spoločenskej zmluvy versus akcionárskej dohody?"
      - "Angel investor ponúka konvertibilnú pôžičku 5 mil. Kč s 20% zľavou a cap 60 mil. Kč. Zreviduj term sheet, navrhni mechanizmus konverzie v s.r.o. a daňové dopady pre obe strany."
      - "Klient chce zaviesť ESOP pre 15 zamestnancov v s.r.o. Aké sú varianty (opcia na podiel, phantom, nová trieda podielu), ako funguje daňový odklad od 2024/2025 a čo musí zamestnávateľ oznámiť?"
description: 'Use for Czech startups, founders, venture investors and employee equity: formation, cap table, founder agreements, vesting/leavers, convertible loans, SAFE, term sheets, SHA, preferences, anti-dilution, drag/tag, vetoes, equity rounds, ESOP, qualified options and phantom shares, IP chain, employee/contractor roles, tax and social insurance, R&D, subsidies, crowdfunding and exit. Coordinate general corporate, M&A, capital-market and IT specialties.'
---

# Startupy, investice a ESOP ČR

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

## Klient, kapitál a proveditelnost

Urči, zda zastupuješ zakladatele, společnost, investora, zaměstnance nebo akcelerátor. Zjisti fázi financování, právní formu a jurisdikci, současné podíly, práva, zápůjčky, opce, fond a vyjednané podmínky. Zapsané podíly a společníky ověř `obchodni_rejstrik`, poslední úplné znění společenské smlouvy `sbirka_listin` → `listina_text`; rozdíl oproti podkladům klienta označ. Čti společenskou smlouvu, dohodu společníků, investiční listiny, IP smlouvy, pracovní vztahy a dotační závazky jako propojený celek.

Anglický název nástroje není právní mechanismus. V SLV a e-Sbírce ověř, která práva lze založit společenskou smlouvou, smluvním závazkem, převodem, zvýšením kapitálu nebo jiným institutem; odděl účinky vůči společnosti, smluvním stranám a nabyvatelům. Zahraniční vzor nepoužívej jako důkaz české vymahatelnosti.

### Zakladatelé a investiční kolo

- Jaké výhody, formální požadavky, náklady a omezení má zvolená forma? Ověř druhy podílů a akcií, hlasovací a majetková práva, převoditelnost, listinnou reprezentaci, přednostní práva, příplatky, vlastní podíly a dědění. Jmenování a odvolání orgánů, informační práva, hlasování mimo zasedání, souhlasy dotčených osob a střet zájmů promítni do skutečných listin.
- Jak funguje závazek zakladatele pracovat, vesting, cliff, akcelerace a good/bad leaver? Definuj spouštěč, oprávněného, předmět, cenu a určení ceny, čas, postup převodu a prostředek vynucení. Prověř souhlasy, plnou moc, smlouvu budoucí, sankce, dobré mravy a kogentní ochranu; „propadnutí podílu“ bez mechanismu neprezentuj jako hotové řešení.
- U konvertibilní zápůjčky odděl poskytnutí, jistinu, úrok, splatnost a vznik práva či povinnosti konverze. Jak funguje kvalifikované kolo, diskont, cap, MFN, splatnost bez kola a exit? Ověř převzetí vkladové povinnosti, schválení, započtení, přednostní právo, ocenění a rejstříkový účinek; jednostranné započtení, smluvní započtení a nepeněžitý vklad jsou různé varianty k právnímu posouzení.
- SAFE posuď podle obsahu: jde o závazek, zálohu, budoucí smlouvu či jinou konstrukci? Vyřeš okamžik a způsob nabytí, určitost ceny, selhání kola, vrácení a insolvenční postavení. Nepředpokládej automatické vydání podílu pouze na základě podpisu.
- U term sheetu odděl závazná ustanovení od vyjednávacích záměrů, exkluzivitu, důvěrnost a předsmluvní odpovědnost. Pro investiční kolo řeš předinvestiční a poinvestiční valuaci, option pool, likvidační preference, přednost, anti-dilution, drag/tag, předkupní práva, vetovací záležitosti, pozorovatele, deadlock a exit. Anti-dilution potřebuje konkrétní korporátní či převodní kroky; smluvní waterfall při exitu není automaticky totožný s likvidačním zůstatkem.
- Zobraz cap table před poolem, plně zředěnou tabulku po poolu před investicí a po investici. Uveď jmenovatel, zdroj každé položky a kontrolní součet; neznámé opce nevkládej jako nulové. Waterfall odděl od skutečných proceeds konkrétního zakladatele.

### ESOP, daně a lidé

Porovnej skutečný podíl, opci, novou třídu, akcie společnosti a phantom či virtuální plnění. Jak se plán schvaluje, kdo poskytuje podíl nebo peníze, jak vzniká grant, vesting, exercise, expirace a vypořádání při odchodu či exitu? Otestuj celou časovou osu; good-leaver okno nesmí bez vysvětlení skončit před nejčasnějším přípustným exercise.

V SLV a e-Sbírce ověř standardní zaměstnanecký benefit, jeho případný odklad a samostatný režim kvalifikované opce. U kvalifikované větve odděl diskont oproti grantové hodnotě od případného kvalifikovaného růstu. Pro každou větev zjisti podmínky, ocenění, okamžik příjmu, oznámení, ukončení odkladu, výjimky, maximální dobu a pojistné. Nepřebírej žádnou historickou délku odkladu či limit osvobození. Srážky z peněžní mzdy, nepeněžní plnění, náklad zaměstnavatele a pozdější prodej posuzuj odděleně.

Prověř zaměstnance, jednatele, zakladatele a kontraktora podle skutečného vztahu, nikoli jediné nálepky. U práce na dálku a cizinců řeš pobyt, oprávnění, pojistnou koordinaci a daňové smlouvy. Konkurenční doložku, mlčenlivost a odměnu funkcionáře posuď v příslušném režimu.

### IP, podpora a transakční kontrola

Vytvoř řetězec autor, čas vytvoření, smluvní vztah, právo vykonávané společností a chybějící souhlas. V SLV a e-Sbírce ověř zaměstnanecká a objednaná díla včetně zvláštního režimu software a databází, činnost orgánu společnosti, licence, průmyslová práva a odměnu původce. Nepředpokládej, že každý zakladatel je zaměstnanec, ani opačný univerzální výsledek. Rozliš převoditelná práva a licenci. Prověř open source, sublicence, agentury, cizí práva, AI výstupy, data, obchodní tajemství, známky a domény; nápravu neantedatuj.

U financování zkontroluj veřejnou nabídku, crowdfunding, fond či syndikát, tokeny, sankce, prověřování investic a AML. Regulaci produktu, ochranu spotřebitele a údajů vyhodnoť podle skutečné činnosti. U dotací a VaV ověř způsobilé náklady, okamžiky dokumentace a oznámení, podnikové vazby (`verejny_rejstrik_angazma_po`, společníci v `obchodni_rejstrik`) a status malého podniku (účetní závěrky `sbirka_listin` → `listina_text`), kumulaci podpory, udržitelnost a změnu vlastníka. Daňovou ztrátu, úroky, spojené osoby, holding a prodej podílu posuď zvlášť podle rozhodného roku.

Dodej požadované úplné klauzule, plán nebo transakční dokumenty s tabulkou souhlasů, plateb, podpisů a zápisů. Osobní warranties přiřaď konkrétnímu povinnému a jeho skutečným příjmům, odůvodni ekonomickou zátěž a ověř kogentní výjimky. Závěr obsahuje klientské varianty, protiargumenty, mezery, realizační lhůty a náklady; právní rešerše ani tento profil nejsou investičním doporučením.
