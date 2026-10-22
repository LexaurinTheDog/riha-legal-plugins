---
uuid: 5d95ddc3-4a55-4470-93cb-fdd7b4bc29df
name: obeti-trestnych-cinu
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Oběti trestných činů a poškození ČR"
    summary: "Práva obětí dle zákona 45/2013, zvlášť zranitelná oběť, poškozený v trestním řízení, adhezní nárok na náhradu škody a nemajetkové újmy, peněžitá pomoc státu, předběžná a ochranná opatření, ochrana při výslechu, důvěrník a zmocněnec, stížnost proti odložení, narovnání a mediace, domácí a sexuální násilí."
    examplePrompts:
      - "Klientka byla napadena partnerem, policie věc odložila jako přestupek. Jak podat stížnost proti odložení a jaká má klientka práva jako oběť domácího násilí?"
      - "Klient utrpěl při loupeži těžké zranění, pachatel je stíhán. Jak uplatnit nárok na bolestné, ztížení společenského uplatnění a ušlý výdělek v adhezním řízení a jak požádat o peněžitou pomoc státu?"
      - "Rodiče znásilněné nezletilé chtějí, aby dcera nemusela vypovídat před obžalovaným a aby byl zástupce bezplatný. Co lze v trestním řízení zajistit?"
  en:
    displayName: "Czech Crime Victims & Injured Parties"
    summary: "Victims' rights under Act 45/2013, especially vulnerable victims, injured party in criminal proceedings, adhesion claims for damages and non-pecuniary harm, state financial assistance, preliminary and protective measures, interview protection, confidant and counsel, complaints against dismissal, settlement and mediation, domestic and sexual violence cases."
    examplePrompts:
      - "My client was assaulted by her partner and the police dismissed the case as a misdemeanour. How to file a complaint against the dismissal and what rights does she have as a domestic-violence victim?"
      - "My client suffered serious injury in a robbery and the offender is prosecuted. How to claim pain, loss of amenity and lost earnings in the adhesion procedure and how to apply for state financial assistance?"
      - "Parents of a raped minor want her not to testify in front of the accused and want free counsel. What can be secured in the criminal proceedings?"
  sk:
    displayName: "Obete trestných činov a poškodení ČR"
    summary: "Práva obetí podľa zákona 45/2013, obzvlášť zraniteľná obeť, poškodený v trestnom konaní, adhézny nárok na náhradu škody a nemajetkovej ujmy, peňažná pomoc štátu, predbežné a ochranné opatrenia, ochrana pri výsluchu, dôverník a splnomocnenec, sťažnosť proti odloženiu, narovnanie a mediácia, domáce a sexuálne násilie."
    examplePrompts:
      - "Klientka bola napadnutá partnerom, polícia vec odložila ako priestupok. Ako podať sťažnosť proti odloženiu a aké má klientka práva ako obeť domáceho násilia?"
      - "Klient utrpel pri lúpeži ťažké zranenie, páchateľ je stíhaný. Ako uplatniť nárok na bolestné, sťaženie spoločenského uplatnenia a ušlý zárobok v adhéznom konaní a ako požiadať o peňažnú pomoc štátu?"
      - "Rodičia znásilnenej maloletej chcú, aby dcéra nemusela vypovedať pred obžalovaným a aby bol zástupca bezplatný. Čo možno v trestnom konaní zabezpečiť?"
description: 'Použij pro zastupování obětí a poškozených: zvláštní zranitelnost, ochranu a informace, důvěrníka a zmocněnce, šetrný výslech, bezpečnostní opatření, adhezní nárok, peněžitou pomoc, souhlas s trestním stíháním, stížnosti, náklady, restorativní řešení a výkon náhrady. Obhajobu obviněného řeší samostatný skill.'
---

# Oběti trestných činů a poškození

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

## Bezpečí, status a cíl klienta

Urči, zda klientem je oběť, zvlášť zranitelná oběť, poškozený člověk či společnost, pozůstalý, zákonný zástupce dítěte nebo pouze oznamovatel. Tyto statusy a jejich podmínky ověř zvlášť; procesní nárok není podmínkou všech forem ochrany a pomoci. Zjisti bezprostřední ohrožení, potřebu bezpečného kontaktu, jazykové či zdravotní bariéry, fázi řízení a již učiněné úkony. Bezpečnost, procesní práva, adhezní nárok a státní peněžitou pomoc veď jako oddělené větve.

Z podkladů zaznamenej čas činu, oznámení, doručení rozhodnutí, poučení, zahájení dokazování a přesný obsah již uplatněných nároků. Nedomýšlej diagnózu, trvalé následky, souhlas ani uskutečněný kontakt. Citlivé údaje v pracovních výstupech minimalizuj, v podání však zachovej právně potřebnou identifikaci. Přání rodiny nezaměňuj za vůli oběti a prověř kolizi jejího zástupce.

## Právní mapa

V SLV a e-Sbírce vyhledej zákon o obětech, trestní řád, občanský a trestní zákoník, policii, zvláštní soudní řízení, ochranu svědků, sociálně-právní ochranu dětí, sociální služby, probační a mediační službu a pojištění provozu vozidel. Podle věci připoj unijní pravidla práv obětí, přeshraničního odškodnění a ochranného příkazu a relevantní úmluvy. U právní kvalifikace, procesního úkonu a náhrad odliš časová znění; výčet zvlášť zranitelných, částky a lhůty načti včetně výjimek. Metodiku nebo formulář, které SLV ani e-Sbírka nemají, převezmi jen z oficiálního zdroje vydavatele s odkazem a datem; jako právní oporu je necituj.

## Oznámení, informace a účast

Prověř formu oznámení, žádost o vyrozumění, nahlížení, navrhování důkazů a účast při úkonech. U odložení, postoupení, zastavení či nečinnosti nejprve urč oprávněnou osobu, skutečný prostředek, adresáta a lhůtu. Podnět dohledu nepředstavuj jako náhradu včasné stížnosti. Argument účinného vyšetřování spoj s konkrétně opomenutým úkonem a odpovídající judikaturou ověřenou v SLV (`us`, `ns`) a HUDOC.

Odděl důvěrníka, smluvního zmocněnce, ustanoveného zmocněnce, bezplatnou odbornou pomoc a sníženou odměnu. U každého zjisti podmínky, fázi, rozsah, žádost a doklady. U dítěte a kolize rodiče ověř zvláštní zastoupení. U souhlasu s trestním stíháním prověř vymezené činy, vztah osob, účinky odmítnutí a zpětvzetí i výjimky závislosti nebo nátlaku; nevytvářej tlak na oběť.

U výslechu zkoumej individuální potřeby, školení vyslýchajícího, žádost o jeho pohlaví, záznam, opakování, účast odborníka, konfrontaci, rekognici a následnou použitelnost výpovědi. Šetrnost není automatické oprávnění slíbit, že další výslech nikdy nenastane. Připrav prohlášení o dopadu činu z klientových údajů, nikoli literárně doplněných traumat.

## Ochranná opatření

Rozliš policejní vykázání, civilní ochranu před domácím násilím, trestní předběžná opatření, podnět k vazbě, utajení totožnosti a zvláštní ochranu svědka. Pro každý nástroj zjisti podmínky, fázi, oprávněného navrhovatele, orgán, lhůtu, trvání, prodloužení a důsledek porušení. Vypočti návaznost ochrany, aby nevznikla neoznačená mezera. Žádost o informaci o propuštění či útěku a ochranu před kontaktem v budově soudu řeš samostatně.

U domácího a sexuálního násilí, stalkingu, nenávistného činu, obchodování s lidmi a nezletilé oběti prověř zvláštní pravidla a případné rodinné či pobytové souvislosti. U přeshraniční ochrany ověř působnost instrumentu. Doporučení odborné a bezpečnostní pomoci neoznačuj za skutečně sjednanou službu.

## Nároky a státní pomoc

Rozepiš adhezní nárok po osobách a složkách: věcná škoda, ušlý výdělek, léčení a péče, bolest, ztížení společenského uplatnění, další nemajetková újma, samostatné osobnostní zásahy, pozůstalí a obohacení. Stejný následek neodškodňuj dvakrát a z terapie nevyvozuj trvalý stav. Ověř metodu ocenění a potřebný odborný podklad; pracovní úraz a civilní zdraví nezaměňuj. Uveď důvod, částku či přesně neznámý vstup, důkaz, úroky, případnou solidaritu a stav uplatnění.

Zkontroluj rozhodný okamžik uplatnění v přípravném řízení, hlavním líčení a při dohodě o vině a trestu. Promlčení posuzuj zvlášť pro každou složku a pouze skutečně uplatněný rozsah; neznámou budoucí újmu nevymýšlej kvůli úplnosti. Prověř zajištění majetku, přiznání, odkaz na civilní řízení, odvolací oprávnění a samostatnou náhradu nákladů zmocněnce.

U státní pomoci ověř oprávněnou osobu, následek, podmínky oznámení, výši a limity, subjektivní a objektivní běh včetně zvláštní ochrany nezletilých. Peněžitá pomoc není plnou civilní náhradou. Při odmítnutí nejprve načti zvláštní vyloučení opravných prostředků; automaticky nenavrhuj rozklad, prověř soudní přezkum a osvobození. Zákonný přechod nároku na stát odliš od smluvního postoupení a od vrácení pomoci.

## Dohoda, výkon a výstup

U narovnání, mediace a podmíněného zastavení posuď dobrovolnost, bezpečí, skutečné uspokojení, zajištění a kontrolu budoucího plnění. Návrh dohody nesmí neurčitě rušit další nároky. Koordinuj pojistitele, adhezi a civilní spor bez dvojího plnění; přímý pojistný nárok ověř podle použitelného zákona. U výkonu a insolvence zjisti titul, zbytek nároku, přihlášení a rozsah případného osvobození dlužníka (`insolvence_vyhledat` → `insolvence_detail`); úroky z nároku spočti `urok_z_prodleni`. Dodej požadované podání, ochranný plán, tabulku práv a nároků, přesný rozpočet a nejbližší doloženou lhůtu; připravené a podané vždy odliš.
