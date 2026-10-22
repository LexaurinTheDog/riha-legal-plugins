---
uuid: 86ca962b-ddad-4712-a9ed-fb012f3fe23a
name: pracovni-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Pracovní právo ČR"
    summary: "Pracovní poměr od vzniku po skončení - výpověď a její neplatnost, odstupné, mzda a pracovní doba, odpovědnost, konkurenční doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zaměstnavatel chce dát výpověď pro nadbytečnost zaměstnanci, který je 3 měsíce v pracovní neschopnosti. Lze to a jak?"
      - "Klient dostal okamžité zrušení pracovního poměru za pozdní příchody. Je to platné a do kdy se bránit?"
      - "Připrav konkurenční doložku pro obchodního ředitele tak, aby byla vymahatelná."
  en:
    displayName: "Czech Labour Law"
    summary: "Employment from formation to termination - notice and its invalidity, severance, pay and working time, liability, non-compete, agreements outside employment, disguised employment, disputes."
    examplePrompts:
      - "An employer wants to give redundancy notice to an employee who has been on sick leave for 3 months. Is it possible and how?"
      - "My client received an immediate termination for late arrivals. Is it valid and by when must they challenge it?"
      - "Draft a non-compete clause for a sales director so that it is enforceable."
  sk:
    displayName: "Pracovné právo ČR"
    summary: "Český pracovný pomer od vzniku po skončenie - výpoveď a jej neplatnosť, odstupné, mzda a pracovný čas, zodpovednosť, konkurenčná doložka, dohody, švarcsystém, spory."
    examplePrompts:
      - "Zamestnávateľ chce dať výpoveď pre nadbytočnosť zamestnancovi, ktorý je 3 mesiace práceneschopný. Dá sa to a ako?"
      - "Klient dostal okamžité zrušenie pracovného pomeru za neskoré príchody. Je platné a dokedy sa brániť?"
      - "Priprav konkurenčnú doložku pre obchodného riaditeľa tak, aby bola vymáhateľná."
description: 'Použij pro zaměstnavatele, zaměstnance, HR a odbory: pracovní smlouvy, DPP a DPČ, dobu určitou a zkušební dobu, skončení a neplatnost, mzdu a pracovní dobu, dovolenou a home office, odpovědnost a úrazy, konkurenční doložky, přechod práv, propouštění, agenturní a nelegální práci, diskriminaci, whistleblowing a inspekci.'
---

# Pracovní právo ČR

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

## Strana, vztah a časová osa

Urči klientovu stranu a cíl: vznik nebo změnu vztahu, jeho bezpečné skončení, obranu proti rozvázání, vymáhání plnění, nastavení HR nebo kontrolu inspekce. Zájmy zaměstnavatele, zaměstnance a odborů nejsou totožné. Z podkladů zjisti skutečný výkon, smlouvu, dodatky, kolektivní úpravu, vnitřní předpisy, výplatní a docházkové záznamy, organizační rozhodnutí, výtky, zdravotní podklady a doručenky. Datum listiny nezaměňuj s doručením ani tvrzený důvod s prokázaným skutkem.

Rozliš pracovní poměr, dohody mimo něj, agenturní zaměstnání, služební vztah a samostatné podnikání. Závislou práci posuzuj podle skutečných znaků a rozsahu, nikoli podle faktury nebo názvu smlouvy. U cizinců a přeshraničního výkonu přidej pobytové, zaměstnanostní a kolizní otázky; český formulář automaticky neurčuje celý právní režim.

## Právní a časová kontrola

V SLV a e-Sbírce vyhledej zákoník práce, subsidiární občanské právo, zaměstnanost, inspekci, antidiskriminační úpravu, ochranu oznamovatelů, nemocenské a další potřebné pojistné předpisy, pracovní úrazy, prováděcí mzdová pravidla a civilní proces. U mzdy, délky vztahu, právního jednání, doručení, žaloby i tarifu urč samostatně rozhodné znění a přechod. Novela nečiní všechny starší smlouvy automaticky podřízenými jednomu novému pravidlu.

Každou odchylku od zákona posuď podle konkrétní normy, minim, maxim, kogentních požadavků a zákazu vzdání se chráněných práv. Nepoužívej ani univerzální zákaz odchylky v neprospěch zaměstnance, ani obecnou smluvní volnost. Pevné hodinové limity, sazby a násobky ze starého vzoru nahraď zněním ověřeným v e-Sbírce k rozhodnému dni (`par --k`), u prováděcích nařízení vlády včetně aktuální novely (`souvislosti`).

## Vznik, změny a skončení

Při tvorbě smlouvy zkontroluj druh práce, místo, nástup, formu, informování, odměnu, dobu určitou, její opakování a případné výjimky. U zkušební doby ověř sjednání, délku, prodloužení a vztah k době určité. U dohod vyhledej rozsah práce, rozvrh, evidenci, dovolenou a pojistné či informační souvislosti. Podle zadání doplň přechod práv a povinností, změnu místa nebo druhu práce, hromadné propouštění a součinnost s odbory a veřejnými orgány.

U skončení odděl dohodu, výpověď, okamžité zrušení, zrušení ve zkušební době, uplynutí doby a jiné zákonné události. Který důvod lze použít pro skutečné skutky, jaká intenzita porušení je požadována, je nutná předchozí výtka, organizační změna, lékařský posudek či souhlas odborů? Nezaměňuj závažné a zvlášť hrubé porušení a nedoplňuj chybějící opakování. Prověř ochrannou dobu a konkrétní výjimky, oprávnění podepsat, formu a dovolený způsob doručení včetně elektronického.

Výpovědní důvod, subjektivní a objektivní lhůtu zaměstnavatele, běh výpovědní doby a žalobní lhůtu zaměstnance počítej odděleně. Samotná oprava jedné lhůty neřeší ostatní. U doručení dolož počátek, právní pravidlo a konec; souhlas s elektronickou komunikací a technické odeslání nemusí samy splnit zákonný režim. Vyhledej odstupné či jiné zvláštní plnění, potvrzení o zaměstnání a návaznost na podporu.

## Neplatné skončení a peněžní následky

Odděl žalobu na neplatnost od písemného oznámení, že zaměstnanec trvá na dalším zaměstnávání. Zaznamenej druh rozvázání, zamýšlený den skončení, oznámení, skutečný výkon práce, nepřidělování a možnost či připravenost pracovat. Náhradu nesčítej se mzdou za stejnou skutečně vykonanou práci. Pro jednotlivá období urč titul, vstupní průměrný výdělek, výjimky a případné moderování včetně potřeby návrhu.

U netrvání na pokračování rozliš následky neplatné výpovědi a jiných způsobů zrušení; zvláštní náhradu z jedné větve automaticky nepřenášej do druhé. U rozvázání zaměstnancem zkoumej vlastní režim nároků zaměstnavatele. Prekluzi a promlčení neztotožňuj. Návrh dohody nesmí bez kontroly potlačit již vzniklá nebo kogentně chráněná práva.

## Práce, odměna a odpovědnost

U mzdy a platu prověř použitelné minimum, zaručený standard, rovné odměňování, příplatky, přesčas, práci ve svátek a noci, pohotovost, evidenci a splatnost. U pracovní doby zkoumej rozvrh, přestávky a odpočinek. U dovolené a překážek urč skutečné období a nárok včetně práce na dohodu; nezaměňuj kalendářní dny, směny a hodiny. U home office připrav konkrétní dohodu, náklady, bezpečnost a ukončení režimu.

Odpovědnost zaměstnance rozděl na obecnou škodu, schodek, ztrátu svěřených věcí a další tituly; u každého ověř zavinění, dohody, důkazní břemeno a limity. U zaměstnavatele odděl obecnou odpovědnost, pracovní úraz a nemoc z povolání, zproštění, jednotlivé náhrady a pojistnou souvislost. U škody a výdělku používej doložené výpočty, nikoli pevný násobek.

U konkurenční doložky zkoumej oprávněný zájem, přípustný rozsah, vyrovnání, sankci a ukončení. Mlčenlivost, souběžnou činnost, monitoring, osobní údaje a ochranu oznamovatele posuzuj samostatně; smluvní pokutu nebo zajištění nepřebírej z obchodní smlouvy. Přípustnou ochranu klienta promítni do konkrétní klauzule.

## Spor a dokončení

Připrav argumenty a nejsilnější protiargument, důkazní mapu, předžalobní výzvu, vykonatelný petit a příslušný soud. Diskriminaci a přesun důkazního břemene opři o konkrétní podmínky. Podnět inspekci není rozhodnutím o soukromém nároku ani automatickým stavením lhůty. Rozpočet zahrnuje každé podání, osvobození a tarifní úkony: poplatek spočti `soudni_poplatek`, tarifní odměnu po úkonech `odmena_advokata`, úrok z prodlení z dlužné mzdy či náhrady mzdy `urok_z_prodleni`; insolvenci zaměstnavatele ověř `insolvence_vyhledat`. Při smluvním zadání dodej hotovou listinu s řádným skutkovým vymezením a podpisovým/doručovacím plánem; návrh ani jeho předání klientovi neoznačuj za doručené skončení pracovního poměru.
