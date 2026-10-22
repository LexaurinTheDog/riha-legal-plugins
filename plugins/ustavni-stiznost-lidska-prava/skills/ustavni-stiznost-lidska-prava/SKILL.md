---
uuid: d43ced1e-7f34-4e5c-a810-17bcda834398
name: ustavni-stiznost-lidska-prava
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Ústavní stížnost a lidská práva"
    summary: "Přípustnost a vyčerpání opravných prostředků, dvouměsíční lhůta, sepis ústavní stížnosti, argumentace základními právy, test proporcionality, stížnost k ESLP, Listina EU a předběžná otázka."
    examplePrompts:
      - "Nejvyšší soud odmítl dovolání klienta pro nepřípustnost. Běží lhůta pro ústavní stížnost a proti čemu ji podat?"
      - "Připrav strukturu ústavní stížnosti proti rozsudku, který nereagoval na klíčovou námitku - jaké právo namítat a jakou judikaturu ÚS?"
      - "Ústavní soud stížnost odmítl jako zjevně neopodstatněnou. Do kdy a jak podat stížnost k ESLP a co musí obsahovat formulář?"
  en:
    displayName: "Czech Constitutional Complaint & Human Rights"
    summary: "Admissibility and exhaustion of remedies, the two-month deadline, drafting the petition, fundamental-rights argumentation, proportionality test, ECHR application, EU Charter and preliminary references."
    examplePrompts:
      - "The Supreme Court rejected my client's appeal on points of law as inadmissible. Is the constitutional complaint deadline running and what should it target?"
      - "Draft the structure of a constitutional complaint against a judgment that ignored a key objection - which right to invoke and which Constitutional Court case law?"
      - "The Constitutional Court dismissed the complaint as manifestly unfounded. By when and how do we apply to the ECHR and what must the form contain?"
  sk:
    displayName: "Ústavná sťažnosť a ľudské práva ČR"
    summary: "Prípustnosť a vyčerpanie opravných prostriedkov, dvojmesačná lehota, spísanie ústavnej sťažnosti, argumentácia základnými právami, test proporcionality, sťažnosť na ESĽP, Charta EÚ a prejudiciálna otázka."
    examplePrompts:
      - "Najvyšší súd odmietol dovolanie klienta pre neprípustnosť. Plynie lehota na ústavnú sťažnosť a proti čomu ju podať?"
      - "Priprav štruktúru ústavnej sťažnosti proti rozsudku, ktorý nereagoval na kľúčovú námietku - aké právo namietať a akú judikatúru ÚS?"
      - "Ústavný súd sťažnosť odmietol ako zjavne neopodstatnenú. Dokedy a ako podať sťažnosť na ESĽP a čo musí obsahovať formulár?"
description: Use for Czech constitutional complaints, fundamental rights, admissibility, remedies, interim protection, constitutional review, Strasbourg proceedings and related EU Charter issues. Distinguish constitutional review from ordinary appeal.
---

# Ústavní stížnost a lidská práva

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

## Oborový postup: ústavní stížnost a lidská práva

### Cíl, legitimace a napadený zásah

Identifikuj klienta, povahu zásahu a přesný požadovaný výsledek. Je stěžovatelem fyzická osoba, právnická osoba nebo územní samospráva a jaké konkrétní právo jí v daném postavení náleží? Ověř procesní legitimaci, povinné zastoupení, plnou moc a případný střet zájmů; u právnické osoby ověř statutární orgán a způsob jednání `obchodni_rejstrik` nebo `verejny_rejstrik`. Odliš rozhodnutí, jiný zásah, nečinnost a otázku ústavnosti předpisu; každému odpovídají jiné podmínky a petit.

Ústavní argument nesmí pouze opakovat, že obecný soud nesprávně hodnotil důkazy nebo vyložil zákon. Vymez tvrzený ústavní deficit, jeho závažnost, vazbu na konkrétní pasáž rozhodnutí a dopad na klienta. Současně nepodceňuj zákonnou otázku, pokud právě její extrémní řešení nebo chybějící odůvodnění zakládá zásah do práva.

### Vyčerpání prostředků a čas

Z dodaného spisu sestav úplný řetězec rozhodnutí, opravných prostředků, způsobu jejich vyřízení a doloženého doručení. Rozliš prostředek přípustný, skutečně podaný, projednaný, odmítnutý pro vady a odmítnutý z důvodů ponechaných na uvážení. Tato rozlišení mohou měnit vyčerpání i počátek lhůty; nepovažuj poslední časově vydanou listinu automaticky za rozhodnutí o posledním relevantním prostředku.

V SLV a e-Sbírce ověř, které prostředky musí být v dané situaci vyčerpány, jaké jsou výjimky a jaký význam má návrh obnovy nebo dozorový podnět. U jiného zásahu odděl jeho počátek, zjištění a trvání. U průtahů řeš dostupnou ochranu proti pokračující nečinnosti a samostatně nápravu již skončeného řízení. Před podáním propočti lhůtu z doložené události včetně pravidel doručení a konce; interní bezpečný termín odliš od zákonného.

### Věcná analýza práv

Podle skutků posuď spravedlivý proces, rovnost zbraní, kontradiktornost, právo být slyšen, překvapivé rozhodnutí, opomenuté důkazy, zákonného soudce, přiměřenou délku, odůvodnění a nepřiměřený formalismus. U každé námitky ukaž, kde byla uplatněna, jak na ni orgán reagoval a jak by její řádné posouzení mohlo ovlivnit výsledek.

Dále prověř relevantní ochranu vlastnictví a legitimního očekávání, soukromí a osobní autonomie, rodinného života, projevu, rovnosti, náboženství, sociálních práv nebo územní samosprávy. Zvol test odpovídající konkrétnímu právu a intenzitě zásahu. Proporcionalitu, zákaz diskriminace a test racionality nepoužívej jako zaměnitelné formuláře. Vypořádej legitimní cíl, skutkovou oporu zásahu a nejsilnější argument veřejné moci nebo protistrany.

Judikaturu vyhodnoť z celých textů, včetně odlišných stanovisek, návaznosti a pozdějšího vývoje. Rozliš nález, usnesení, rozhodnutí pléna, senátu a stanovisko; jejich význam neurčuj mechanicky jen názvem formy. Je-li zadána předchozí praxe konkrétního senátu, identifikuj právě tento senát a skutečně srovnatelné věci. Obecný přehled Ústavního soudu nenahrazuje požadovanou senátní analýzu.

### Petit a prozatímní ochrana

Urči, která rozhodnutí je nutné napadnout pro dosažení cíle a která do petitu nepatří. Rozsah odůvodni podle procesní návaznosti a tvrzeného zásahu, nikoli mechanickým výčtem všech listin. Identifikuj orgán, spis, datum a části výroku. Návrh na vyslovení porušení, zrušení rozhodnutí, zákaz pokračování nebo obnovení stavu musí odpovídat pravomoci soudu a povaze zásahu.

U akcesorického návrhu na zrušení předpisu dolož konkrétní aplikované ustanovení, vazbu na věc a tvrzený rozpor. U odkladu vykonatelnosti odděleně ověř obě relevantní podmínky: vztah k důležitému veřejnému zájmu a porovnání újmy při výkonu s újmou při odkladu. Dodrž směr srovnání a vysvětli konkrétní důkazy pro každou podmínku. Již dokončený výkon nesmí být popsán jako budoucí nebezpečí, které odklad ještě odvrátí.

### Evropská ochrana

U Evropského soudu pro lidská práva samostatně ověř postavení oběti, vyčerpání účinných prostředků, rozhodné konečné rozhodnutí, lhůtu, význam stejné věci projednávané jinde a ostatní podmínky přijatelnosti. Zjisti skutečné požadavky na formulář, podpisy, přílohy, jazyk a podání z oficiálních pramenů ESLP (Jednací řád soudu, praktický pokyn a formulář na echr.coe.int; judikatura v HUDOC); text Úmluvy ověř v e-Sbírce (č. 209/1992 Sb.). Není-li potřebná verze nebo formulář dostupný, přesně označ mezeru a nepoužívej paměťové ujištění.

Rozliš konstatování porušení, spravedlivé zadostiučinění, případnou obnovu a výkon rozsudku. Nárok na zadostiučinění formuluj ve správné fázi a s doloženým výpočtem. U unijních práv nejprve ověř působnost Listiny základních práv Evropské unie v dané věci. Nepoložení předběžné otázky neoznačuj automaticky za porušení práva; prověř povinnost, výjimky a odůvodnění soudu.

### Výstup a rozhodnutí klienta

Dodej skutečnou stížnost nebo jiný požadovaný text, nikoli jen úvahu o ústavnosti. Připoj tabulku přípustnosti, chronologii, seznam příloh, petity a konkrétní ústavní argumenty s oporou ve faktech. Náklady ověř pro daný postup: poplatek či osvobození, smluvní zastoupení, případná pomoc a podmínky výjimečné náhrady nejsou totožné otázky. Vysvětli realistický dosažitelný výsledek, procesní riziko a klientova nevratná rozhodnutí.
