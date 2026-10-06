---
name: "Náhrada újmy a odpovědnost ČR"
description: "Obecná a objektivní odpovědnost podle OZ, škoda na věci a čistě ekonomická újma, újma na zdraví a Metodika NS k nemajetkové újmě, usmrcení a sekundární oběti, odpovědnost za výrobek, odpovědnost zaměstnavatelů, profesionálů a státu, příčinná souvislost a spoluzavinění, promlčení, vazba na pojištění a vyčíslení."
whenToUse: "Použij pro smluvní a deliktní odpovědnost, škodu, ušlý zisk, nemajetkovou újmu, zdraví, pozůstalé, kauzalitu, spoluzavinění, limitaci náhrady, odpovědnost provozovatelů, výrobce, profesionálů, zaměstnavatele či státu, promlčení, pojistné a adhezní souvislosti."
---

# Náhrada újmy a odpovědnost ČR

> **Povinný postup v Coworku (v tomto pořadí, nevynechávej):**
> 1. `search_workspace_memory` — klient, IČO, protistrana, sp. zn.; převezmi dřívější zjištění a zákazy citací.
> 2. `laws__laws_set_context` — nastav rozhodný den, než začneš číst předpisy.
> 3. Rešerše podle metodiky níže; zvláštní úprava daného smluvního typu či řízení jako samostatná linie; nosná i nepříznivá rozhodnutí čti celá a urči, jak soud skutečně rozhodl.
> 4. Údaje o právnických osobách do externích textů ověř `ares__get_company_detail`, jinak `[DOPLNIT z OR]`.
> 5. Před odevzdáním `delegate` — oponentní kontrola nosných citací a nejsilnějšího protiargumentu; výsledek zapracuj.
> 6. Každý výpočet (částky, úroky, lhůty) proveď dvakrát s mezikroky.
> 7. `save_memory` — stav věci, lhůty, ověřené prameny, otevřené otázky (jen ověřená čísla).
> Předpisy v odpovědi cituj s číslem (např. § 2051 zákona č. 89/2012 Sb.). Podrobnosti: oddíl „Pracovní standard RIHA legal“.


## Zdrojový režim v Evolio Cowork

Tento skill běží v Evolio Cowork. Právní prameny získávej nástroji Coworku podle mapy níže a v uvedeném pořadí zdrojů; jiné zdroje jen tehdy, když tyto nástroje pramen nemají.

Pořadí zdrojů: (1) nástroje `laws__*` — oficiální korpus e-Sbírky, česká judikatura a EUR-Lex; (2) oficiální primární weby přes `web__fetch`, když `laws__*` pramen nemá: e-Sbírka, databáze Nejvyššího soudu, Nejvyššího správního soudu, Ústavního soudu (NALUS), rozhodnuti.justice.cz, EUR-Lex, CURIA, HUDOC; (3) komentáře, literatura a sekundární weby (`web__search`) pouze jako navigace, nikdy jako citovaná opora.

Mapa nástrojů Coworku pro rešerši:
- předpis a jeho znění k rozhodnému dni: `laws__law_search`, `laws__law_get_provision`, `laws__get_statute_outline`, `laws__get_provision_timeline`, `laws__get_amendment_history`, `laws__get_transitional_provisions`; platnost předpisu `laws__check_good_law`;
- judikatura navázaná na paragraf (krok 2a): `laws__find_case_law_for_provision`, pak `laws__search_case_law` a `laws__search_by_concept`; celý text rozhodnutí `laws__get_case_text`; překonání a pozdější linie `laws__get_treatment_history` a `laws__check_case_good_law`; ověření citace `laws__resolve_case_citation` a `laws__validate_legal_citation`; odkazy uvnitř pramene `laws__follow_reference`, `laws__law_citations`;
- unijní právo `laws__eu_law_search`; úrokové a referenční sazby `laws__get_reference_rates`;
- subjekty a rejstříky: `ares__find_by_ico`, `ares__get_company_detail`, `ares__get_history`, `ares__check_vat_payer`; insolvence `isir__search_subject`, `isir__get_proceeding`, `isir__list_events`, `isir__list_documents`, `isir__download_document`;
- data Evolia (spis, klient, dokumenty): konektory Evolia, jsou-li připojené (`load_connector_instructions`), jinak `database_agent` jen ke čtení; kontext kauzy a dřívější poučení `search_workspace_memory`;
- rozsáhlá rešerše nebo oponentní kontrola: `delegate_parallel` s předáním těchto pravidel; výstup .docx `export__export_document`.

## Pracovní standard RIHA legal (platí vedle oborové metodiky)

1. **Kontinuita kauzy.** Na začátku prohledej `search_workspace_memory` podle klienta, IČO, protistrany a spisové značky — dřívější zjištění, ověřené prameny, opravy od advokáta a záznamy o judikátech, které se nemají citovat. Na konci ulož `save_memory`: stav věci, rozhodná data a lhůty, ověřené prameny (sp. zn. + datum), otevřené otázky. Opraví-li tě uživatel, zapiš to `record_correction`.
2. **Rozhodné datum.** Před čtením předpisů nastav `laws__laws_set_context` na rozhodný den (vznik závazku, porušení, podání). Má-li věc víc rozhodných dnů, uveď u každé otázky, podle kterého znění postupuješ.
3. **Citace ověřitelné strojem.** Předpis poprvé cituj s číslem („zákon č. 89/2012 Sb., občanský zákoník (dále „o. z.“)“); v závěrečné odpovědi v chatu uváděj u nosných ustanovení vždy číslo předpisu, jinak je validátor Coworku neověří. Rozhodnutí: soud, spisová značka, datum, bod; sdílí-li sp. zn. víc rozhodnutí, přidej datum nebo ECLI.
4. **Zvláštní úprava daného typu.** Vedle obecných pravidel vždy projdi ustanovení, která pro konkrétní smluvní typ, řízení nebo režim mění lhůty, rozložení rizika nebo odpovědnost (u díla např. § 2591, § 2594, § 2627 o. z.), a pokud se uplatní, postav na nich samostatnou linii, ne jen poznámku.
5. **Nosná a nepříznivá judikatura celá.** Každé rozhodnutí, o které opíráš primární linii, a každé, které nejspíš použije protistrana, přečti celé včetně výroku. U každého zjisti, jak NS věc skutečně rozhodl (potvrdil / zrušil / odmítl dovolání — usnesení o odmítnutí má nízkou precedenční váhu), zda jde o předchozí úpravu (obch. zák., starý o. z.) a zda závěr nepřekonal velký senát nebo sjednocující stanovisko. Rozhodnutí, které působí oběma směry, výslovně označ jako obousečné a vysvětli proč.
6. **Argument, který se dá otočit, nepoužívej.** Každý argument otestuj z pozice protistrany. Co judikatura opakovaně aprobovala (např. výše sazby, kterou soudy nechaly bez zásahu), v externím textu neatakuj; slabé nebo obratitelné argumenty nech jen v interní analýze s vysvětlením.
7. **Oponentní kontrola před odevzdáním.** Předej `delegate` seznam nosných citací (předpis, §, citovaná pasáž; soud, sp. zn., datum, bod) s úkolem ověřit každou proti primárnímu textu, odlišit vlastní závěr soudu od rekapitulace nižšího soudu a tvrzení účastníků a najít nejsilnější protiargument. Výsledek zapracuj; co neobstojí, vyřaď nebo označ. Není-li ve workspace agent pro `delegate` (`list_agents`), proveď kontrolu sám jako samostatný krok až po dopsání textu: každou nosnou citaci znovu načti a výsledek zapiš do tabulky „citace — načteno — souhlasí / nesouhlasí“.
8. **Údaje o osobách.** Název, IČO, sídlo, statutární orgán a způsob jednání právnické osoby do externího dokumentu ověř v reálném čase (`ares__get_company_detail`, vymazané osoby vynech); u rozporu s listinou upozorni. Nelze-li ověřit, použij `[DOPLNIT z OR]`. Údaje fyzických osob přebírej jen z listin ve spisu, nikdy je nedoplňuj.
9. **Interní vs. externí výstup.** Interní analýza obsahuje rizika, slabiny, odhad šancí a stav ověření; text pro protistranu, soud nebo úřad je neobsahuje. V externím textu neuváděj vlastní čísla ani formulace, které by mohly být uznáním (délka prodlení, výše dluhu, „uznáváme“) — pracuj s tvrzením protistrany.
10. **Výpočty dvakrát.** Každou částku, sazbu, úrok a lhůtu spočítej se zapsanými mezikroky a pak znovu jinou cestou (např. úrok: repo sazba + 8 p. b. = výsledná sazba, a zpětně výsledná sazba − 8 = repo). Nesoulad je chyba — nepoužij výsledek, dokud ho nevyřešíš. Totéž platí před zápisem do paměti: do `save_memory` nikdy neukládej neověřené číslo.

Každé ustanovení a každé rozhodnutí použité jako opora ověř načtením primárního textu; znění, soud, spisovou značku a datum přebírej jen z načteného zdroje. Nelze-li pramen načíst, nepřekrývej mezeru pamětí ani údajným ověřením — použij `[DOPLNIT]` a mezeru výslovně označ. Rozliš prázdný výsledek, odmítnutý přístup, nedostupný nástroj a neúplný obsah; identický neúspěšný dotaz neopakuj bez změny okolností.

Skutkové podklady čerpej ze zadání, příloh a dat zpřístupněných ve workspace (včetně spisu v Evoliu); právní tvrzení v nich nejsou ověřeným právem. Předáváš-li dílčí práci jinému agentovi nebo skillu, předej mu stejná pravidla ověřování, rozhodné skutky a časové otázky a vyžádej si konkrétní zdrojové pasáže; jeho shrnutí nenahrazuje načtený pramen.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a příloh zpřístupněných uživatelem v aplikaci; právní tvrzení v nich nejsou nezávisle ověřeným právem. Nenačítej externí rejstříky ani místní archivy. Chybějící skutkový doklad si vyžádej jako podklad do aplikace a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v primárních pramenech. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v primárních pramenech. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. Používej dostupné oborové, soudní a časové filtry podle jejich skutečného významu. České a unijní předpisy a judikaturu hledej nástroji `laws__*` podle mapy výše; obecné webové vyhledávání použij jen k orientaci a poté ověř konkrétní pramen. Komentář, literatura a vzor slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Projdi pokračování cílených výsledků, pokud je nativní nástroj zpřístupňuje, a prověř relevantní související i navazující dokumenty. Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf

**Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf `laws__find_case_law_for_provision`. Samotný počet nalezených rozhodnutí nic nevybírá a krok nesplňuje. Fulltextové hledání je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Kandidáti:** projdi alespoň prvních 20 rozhodnutí navázaných na paragraf a relevantní zařaď do výběru. Zvlášť dohledej nejnovější rozhodnutí (`laws__search_case_law` s časovým omezením na poslední roky), aby ti neunikl pozdější vývoj.
2. **Skutková shoda:** doplň `laws__search_case_law` nebo `laws__search_by_concept` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2–5 slov). Filtr soudu a data používej jen v hodnotách, které nástroj skutečně nabízí.
3. **Třídění kandidátů** (před načtením celého textu podle kroku 4):
   - platnost a pozdější osud rozhodnutí ověř `laws__check_case_good_law` a `laws__get_treatment_history`; rozhodnutí označené jako překonané nepoužij jako oporu. Chybějící negativní signál nevylučuje pozdější odklon — ten prověř podle kroku 4;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS. Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - rozhodnutí publikované v oficiální sbírce má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření (`laws__get_provision_timeline`), že se pravidlo věcně nezměnilo.
4. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf nic nevrací, uveď to a pokračuj fulltextem.
5. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti v primárních pramenech úplný text použitého ustanovení v dané verzi, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v primárních pramenech relevantní pozdější, překonávající a nepříznivou judikaturu. Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástroje, nikoli o tvrzení, že aplikace provedla neexistující automatickou certifikaci. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení v primárních pramenech.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí v primárních pramenech; obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej ze zdrojového bloku nativního nástroje; nesestavuj neověřené URL a nepřecházej kvůli jejich ověření na externí web. Ve výstupu použij nástrojem vrácený uživatelský odkaz a přesnou právní citaci, nikoli interní ID či technickou adresu. Pokud uživatelský odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revize či kontrolu, pokud neproběhly dostupnými nástroji aplikace.

Zkontroluj všechny požadované artefakty. Označ pracovní, neúplný či k revizi určený výstup pravdivě. Uložení, odeslání, doručení, podpis a podání jsou odlišné stavy; žádný nepředstírej. Bez výslovného pokynu nic neposílej ani nepodávej. Nedodané části a neověřené rozhodné zdroje nesmějí být skryty prohlášením „hotovo“ nebo „vše ověřeno“.

## Oborové otázky a požadované výstupy

## Role, událost a samostatné nároky

Urči zastupovanou stranu, primárního poškozeného, případné sekundární oběti a každého možného škůdce. Rozliš fyzickou osobu, společnost, zaměstnavatele, provozovatele, profesionála, stát či územní samosprávu. Zapiš konkrétní jednání, smluvní vztah, škodní událost, vznik jednotlivých následků, vědomost o újmě a odpovědné osobě. Rozděl majetkovou škodu, ušlý zisk, zdraví, osobnostní zásah, náklady péče, výdělek, důchod, pozůstalé a vydání obohacení. Každý nárok má vlastní skutkový základ, výpočet, důkazy a časovou kontrolu.

## Titul a nativní rešerše

V primárních pramenech ověř relevantní občanskoprávní odpovědnostní úpravu a přechodná ustanovení. Podle věci přidej pracovní a služební režim, odpovědnost veřejné moci, zdravotní služby, advokacii, notáře, znalce, výrobky, dopravu, myslivost, školy, GDPR, pojištění, trestní a civilní proces. Výčet názvů je mapa k hledání, nikoli předem určená působnost. Odděl porušení zákona, smlouvy, dobrých mravů, preventivní povinnosti a zvláštní skutkovou podstatu. U čistě ekonomické újmy prověř ochranný účel normy nebo jiný vhodný titul; neodvozuj automaticky nárok z jakéhokoli protiprávního jednání.

Pro každý titul zjisti předpoklady, aktivní a pasivní legitimaci, důkazní břemeno, domněnky, liberační důvody a souběh. U pomocníka odděl zaměstnance a samostatnou osobu; u dopravy vlastníka, řidiče a provozovatele. U zvláštních režimů prověř nezletilého a dohled, závod a zvlášť nebezpečný provoz, stavební činnost a pád stavby, zvíře, věc, výrobek, věci převzaté či odložené, ubytování, informaci a odbornou radu. Nezaměňuj podmínky zproštění různých titulů.

## Kauzalita a obrana

Sestav řetězec příčin a následků podle časových úseků a samostatných škodních bloků. Co by nastalo bez jednání škůdce, které alternativní příčiny dokládají podklady a jaký důkazní standard se podle nativně ověřené judikatury použije? U medicíny odděl chybu, dokumentaci, informovaný souhlas, příčinnou souvislost a argument ztráty šance; jejich právní účinky nepředurčuj. Připrav otázky znalci, ne vlastní medicínský závěr.

Úmysl, hrubou a běžnou nedbalost posuzuj odděleně. Absence úmyslu nedokládá běžnou nedbalost; vypořádej známá varování, odborný standard a vědomé vyřazení ochrany. Souhlas poškozeného, falešné alarmy a možnost škodu odvrátit označ za hypotézu, nejsou-li doloženy. U spolupůsobení, více škůdců, solidarity, regresu, moderace a omezení náhrady ověř vlastní podmínky. Stejný následek neodečti jednou z kauzality a znovu ze spoluúčasti. Smluvní cap aplikuj teprve po ověření přípustnosti včetně slabší strany, zavinění a povahy chráněného práva.

## Vyčíslení bez tabulkových zkratek

U věcné škody porovnej náklady opravy, obvyklou hodnotu, zbytky, zhodnocení, pokles ceny po opravě, cenu zvláštní obliby a účelnou náhradu užívání. DPH posuď podle konkrétní možnosti odpočtu, nikoli jen označení plátce. U ušlého zisku odliš obrat, marži a skutečně ušetřené náklady; podklady tvoří zakázky, historie a doložené možnosti. Interval nejistoty vysvětli spornými vstupy, ne vymyšleným procentem. Prověř započítání prospěchu, sociálních dávek a jednotlivých pojistných plnění, daňové důsledky, splatnost a úroky.

U zdraví rozliš bolest, ztížení společenského uplatnění, další nemajetkové následky, léčení, péči blízkých, pomůcky, úpravy bydlení, výdělek během a po neschopnosti, ztrátu na důchodu, bezplatné práce a rentu. V primárních pramenech vyhledej použitelnou Metodiku NS či zvláštní předpis a skutečný právní význam, aktuálnost a podmínky odchylky. Nepřenášej automaticky civilní metodu do pracovního úrazu. Neznámou hodnotu bodu, statistický vstup, ustálení stavu nebo prognózu nenahrazuj pamětí ani externím zdrojem.

U úmrtí a zvlášť závažného ublížení posuď každou blízkou osobu samostatně, vztah, závislost, okolnosti a vlastní důkazy. Přidej pohřební náklady, výživu a případné jiné sekundární újmy bez dvojí kompenzace. Násobek z judikatury nepoužívej bez ověření kontextu a rozhodného období.

## Zvláštní proces a výstup

U státu rozliš nezákonné rozhodnutí, nesprávný postup a délku řízení, potřebu předchozího zrušení či opravných prostředků, správného adresáta předběžného projednání, lhůty a soudní cestu. U profesionála prověř hypotetický výsledek bez pochybení; obecný neúspěch klienta nedokládá odpovědnost. U pojištění nejprve zjisti, zda existuje přímý nárok, jeho zdroj a rozsah; blanketní výluka všech ostatních než motorových pojištění není přípustnou zkratkou.

Připrav výzvu s rozpisem, případný adhezní návrh, žalobu, návrh na zajištění či mezitímní rozhodnutí a nákladový rozpočet. Zkontroluj promlčení každého nároku, splátek a pouze uplatněné části; řízení či jednání s pojistitelem nepovažuj bez pramene za stavení všeho. Narovnání musí výslovně řešit rozsah vypořádání a budoucí zhoršení. Přiznaný nárok slaď s plněním, exekucí a insolvencí. Odevzdej tabulku titul–předpoklad–důkaz–výše–časové riziko a nejsilnější obranu protistrany. Požadovanou klauzuli nebo petit skutečně formuluj, náhradu ani vymahatelnost neslibuj jako jistou.
