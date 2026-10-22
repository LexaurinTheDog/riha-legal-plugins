---
uuid: 2615c2b4-1f93-4647-a845-157740ee62ba
name: dedicke-pravo
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dědické právo ČR"
    summary: "Závěť a dědická smlouva, nepominutelní dědici, vydědění, odmítnutí a výhrada soupisu, dluhy zůstavitele, pozůstalostní řízení u notáře, spory, plánování majetku."
    examplePrompts:
      - "Zemřel otec, zanechal závěť jen ve prospěch družky a dluhy z podnikání. Co mají děti udělat a do kdy?"
      - "Připrav alografní závěť s vyděděním syna pro trvalé neprojevování zájmu - jaké jsou náležitosti a rizika?"
      - "Notář odkázal klienta k žalobě o dědické právo. Jak formulovat petit a jaká běží lhůta?"
  en:
    displayName: "Czech Inheritance Law"
    summary: "Wills and inheritance contracts, forced heirs, disinheritance, renunciation and inventory reservation, estate debts, probate before the notary, disputes, estate planning."
    examplePrompts:
      - "A father died leaving a will only in favour of his partner and business debts. What should the children do and by when?"
      - "Draft a witnessed will disinheriting a son for persistent lack of interest - requirements and risks?"
      - "The notary referred my client to file an action on the right of inheritance. How to phrase the claim and what deadline runs?"
  sk:
    displayName: "Dedičské právo ČR"
    summary: "Závet a dedičská zmluva, neopomenuteľní dedičia, vydedenie, odmietnutie a výhrada súpisu, dlhy poručiteľa, dedičské konanie u notára v ČR, spory, plánovanie majetku."
    examplePrompts:
      - "Zomrel otec, zanechal závet len v prospech družky a dlhy z podnikania. Čo majú deti urobiť a dokedy?"
      - "Priprav alografný závet s vydedením syna pre trvalé neprejavovanie záujmu - aké sú náležitosti a riziká?"
      - "Notár odkázal klienta na žalobu o dedičské právo. Ako formulovať petit a aká lehota beží?"
description: 'Použij pro české dědictví a pozůstalost: závěti, dědické smlouvy, odkazy, zákonná posloupnost, nepominutelní dědici, povinný díl, vydědění, nezpůsobilost, odmítnutí a soupis, dluhy, SJM, notářské řízení, dědické spory, likvidace, správa, přeshraniční dědictví a plánování pro případ smrti.'
---

# Dědické právo ČR

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

## Oborový postup: dědictví a pozůstalost

### Právo, osoba a rozhodný okamžik
Z podkladů určuj zůstavitele, klientovu roli, datum úmrtí, obvyklý pobyt, občanství, rodinné vztahy, majetek a dluhy v jednotlivých státech. Odděl plánování za života od probíhajícího pozůstalostního řízení nebo následného sporu. Rozhodné právo a pravomoc ověř podle nařízení (EU) č. 650/2012 (EUR-Lex, judikatura SDEU v CURIA), mezinárodní smlouvy (e-Sbírka, Sb. m. s.) a vnitrostátního kolizního práva (ZMPS v e-Sbírce); českou judikaturu k nim hledej v SLV. Zkoumej případnou volbu práva, územní a časovou působnost a evropské dědické osvědčení. Nezaměňuj bydliště v dokladu za prokázaný obvyklý pobyt.

U každé otázky odliš datum pořízení listiny, její změny a smrti. Načti přechodná ustanovení pro pořizovací způsobilost, formu i dědění; nepoužívej jediný nový režim automaticky na staré závěti. Identitu listiny, notáře, soudu a spisu přebírej pouze z doložených údajů.

### Tituly a osoby
Sestav soupis všech pořízení a zjisti jejich vztah: dědická smlouva, závěť, dovětek, odkaz, náhradnictví a svěřenské nástupnictví. Ověř rozsah případného odvolání nebo rozporu mezi pořízeními a zbytek zákonné posloupnosti. U listiny prověř formu, vlastní rukopis či podpis, současnou přítomnost a způsobilost svědků, notářskou formu, úlevy, určitost, podmínky a příkazy. Závěr o neplatnosti přiřaď konkrétní vadě a rozsahu; nevyslovuj jej automaticky pro celou závěť.

Pro zákonné dědění načti úplné podmínky příslušné třídy, reprezentace a soužití. U nepominutelného dědice prověř osobní status, věk, povinný díl a způsob jeho uplatnění. Zvlášť zkoumej vydědění, neuvedený důvod, opomenutí, dědickou nezpůsobilost a případné prominutí. U tvrzení o nezájmu či nevhodném chování zachovej vzájemné příčiny a důkazy, nikoli jen jednostranný příběh.

### Rozhodnutí dědice a ochrana před dluhy
Rozliš zřeknutí za života zůstavitele, odmítnutí dědictví a vzdání se ve prospěch jiného dědice. Ověř přípustnost, formu, poučení, lhůtu, počátek a možné prodloužení i význam pobytu v zahraničí. Prověř, zda předchozí nakládání s majetkem ovlivňuje možnost volby. Neodvozuj přijetí nebo zánik oprávnění pouze z neurčitého popisu návštěvy bytu.

U výhrady soupisu načti podmínky, prohlášení, lhůtu, zákonnou ochranu a následky porušení. Odděl hodnotu nabytého majetku, rozsah odpovědnosti a způsob uspokojení věřitelů. Zjisti dluhy zůstavitele, náklady pohřbu, zajištění, solidaritu a případné svolání věřitelů; insolvenční řízení zůstavitele a přihlášené pohledávky ověř `insolvence_vyhledat` → `insolvence_detail` → `insolvence_dokument_text`. Neznámá pasiva nejsou nulová; srovnej postup u předlužené pozůstalosti, likvidace a insolvenčních souvislostí.

### SJM, zvláštní majetek a započtení
Prověř vypořádání SJM a vlastnictví jednotlivých aktiv před sestavením pozůstalosti. U podílu ve společnosti či družstvu načti zakladatelské dokumenty z podkladů nebo ze sbírky listin (`sbirka_listin` → `listina_text`), zápis podílu `obchodni_rejstrik`, a ověř zákonnou možnost omezení přechodu, vypořádací podíl a kontinuitu správy. Zahrň autorská práva, bankovní účty, pojištění s obmyšleným a zahraniční majetek.

Započtení daru, určení povinného dílu a samostatné peněžité plnění posuzuj zvlášť. Účetní korekce podílů sama neprokazuje existenci vykonatelné platební povinnosti. Výpočty založ na ověřených hodnotách, rozhodném okamžiku ocenění a právních pravidlech; ukaž mezivýsledky a sporné vstupy.

### Řízení, spory a nezletilí
Přečti skutečná procesní rozhodnutí: zahájení, předběžné šetření, poučení, soupis, odkaz k žalobě a konečné usnesení. Zjisti pověření soudního komisaře, účastenství, sporná aktiva či pasiva a rozsah pravomocného výroku. Než doporučíš další žalobu, určuj, zda výrok ukládá vydání majetku, potvrzuje dědictví nebo ponechává spor mimo řízení.

U odkazu k žalobě ověř žalobce, žalované, přesný předmět, důkazní břemeno a určenou lhůtu; návrh nesmí minout soudem vymezený spor. Zahrň dohodu dědiců, její schválení, odvolání, dodatečné projednání a likvidaci. U nezletilého zjisti skutečného zástupce, střet zájmů, potřebu opatrovníka a schválení konkrétního jednání; příbuzenství ani pravomoc zástupce nedovozuj z role v příběhu. Náklady řízení, odměnu komisaře, poplatky a náhradu zastoupení vypočti odděleně podle rozhodné úpravy.

### Plánování a výstup
Porovnej závěť, dědickou smlouvu, darování pro případ smrti, svěřenský fond a pojištění podle klientova cíle, odvolatelnosti, povinného dílu, správy, daní a odpovědnosti. Ověř přípustný rozsah dispozice a potřebnou formu. Navrhni vykonavatele a správce, náhradní řešení a návaznost podnikání. Draft nenazývej platným notářským pořízením, dokud nebyla splněna forma.

Dodej prioritu a nejbližší lhůtu, mapu titulů a dědiců, varianty ochrany před dluhy, procesní nebo smluvní text a seznam chybějících podkladů. Zahrň následné zápisy, oznámení a daňové otázky jako kroky k provedení, nikoli jako již dokončené. Právní oporu čerpej z e-Sbírky (znění předpisů) a ze SLV (judikatura), unijní předpisy a judikaturu SDEU z EUR-Lex a CURIA.
