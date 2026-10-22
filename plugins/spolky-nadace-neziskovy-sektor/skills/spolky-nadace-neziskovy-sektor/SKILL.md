---
uuid: 787c59aa-e879-4541-9781-67649e743f04
name: spolky-nadace-neziskovy-sektor
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Spolky, nadace a neziskový sektor ČR"
    summary: "Spolky, nadace, nadační fondy a ústavy - založení a rejstříky, vnitřní správa a spory členů, přezkum rozhodnutí orgánů, dary, veřejné sbírky, dotace, daňový režim, účetní povinnosti, zánik a odpovědnost."
    examplePrompts:
      - "Členská schůze spolku vyloučila klienta bez předchozí výzvy a bez možnosti se vyjádřit. Jak se bránit a do kdy?"
      - "Chceme založit nadační fond na podporu regionálních talentů. Co potřebujeme, kolik to stojí a jaké budou průběžné povinnosti?"
      - "Spolek přijal dar 800 000 Kč od firmy a chce jí za to dát reklamu na webu. Jaké jsou daňové dopady pro obě strany?"
  en:
    displayName: "Czech Non-profit Law"
    summary: "Associations, foundations, endowment funds and institutes - formation and registers, governance and member disputes, review of body decisions, donations, public collections, grants, tax status, accounting duties, dissolution and liability."
    examplePrompts:
      - "The general meeting of an association expelled my client without prior warning or a chance to respond. How to defend and by when?"
      - "We want to set up an endowment fund for regional talent. What is needed, what does it cost and what are the ongoing duties?"
      - "An association accepted a CZK 800,000 donation from a company and wants to give it advertising on its website. What are the tax consequences for both sides?"
  sk:
    displayName: "Spolky, nadácie a neziskový sektor ČR"
    summary: "Spolky, nadácie, nadačné fondy a ústavy v ČR - založenie a registre, vnútorná správa a spory členov, preskúmanie rozhodnutí orgánov, dary, verejné zbierky, dotácie, daňový režim, účtovné povinnosti, zánik a zodpovednosť."
    examplePrompts:
      - "Členská schôdza spolku vylúčila klienta bez predchádzajúcej výzvy a bez možnosti sa vyjadriť. Ako sa brániť a dokedy?"
      - "Chceme založiť nadačný fond na podporu regionálnych talentov. Čo potrebujeme, koľko to stojí a aké budú priebežné povinnosti?"
      - "Spolok prijal dar 800 000 Kč od firmy a chce jej za to dať reklamu na webe. Aké sú daňové dopady pre obe strany?"
description: 'Use for Czech non-profit entities and civic activity: spolek a pobočný spolek, nadace, nadační fond, ústav, o.p.s., sociální družstvo, založení, stanovy, orgány, členství a vyloučení, soudní přezkum, rejstříky, dary a veřejné sbírky, dotace, veřejně prospěšný poplatník, daně, účetnictví, dobrovolníci, odpovědnost, přeměny a likvidace.'
---

# Spolky, nadace a neziskový sektor ČR

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

## Forma, klient a zdroj pravidel

Urči, zda jednáš za organizaci, zakladatele, člena, člena orgánu, dárce, příjemce podpory nebo věřitele. Zjisti právní formu, čas založení, rejstříkový stav (`verejny_rejstrik`) a rozhodné stanovy, statut či nadační listinu (`sbirka_listin` → `listina_text`); u osob ve vedení `verejny_rejstrik_osoba`. Odděl zákon, vnitřní předpis a individuální rozhodnutí; autonomie organizace není předpoklad neexistence soudní ochrany.

V SLV a e-Sbírce ověř rozdíly mezi spolkem, pobočným spolkem, nadací, nadačním fondem, ústavem, existující obecně prospěšnou společností, sociálním družstvem, církevní osobou a obchodní společností se sociálním cílem. Název nezisková organizace neprokazuje daňové osvobození ani konkrétní právo. Starší právní formu a pokračování organizace podrob přechodným pravidlům.

### Otázky životního cyklu organizace

- Založení a vznik: jaké osoby, právní jednání, účel, název, sídlo, orgány, vklady a forma jsou vyžadovány? Prověř ustavující schůzi, schválení stanov, nadační listinu, jistinu a oddělení založení od zápisu a vzniku. Vyžádej souhlasy a podklady k sídlu, podpisům a funkci; nevytvářej neexistující schůzi nebo potvrzení.
- Vnitřní správa spolku: kdo svolává a rozhoduje, jak se určuje členství, program, doručení pozvánky, usnášeníschopnost a většina? Ověř stanovy i dispozitivnost zákona, delegáty, dílčí schůze, distanční hlasování, zápis a právo na informace. Prověř statutární, kontrolní a rozhodčí orgány, funkční období, způsob zastupování, střet zájmů a péči řádného hospodáře.
- Členství: jak vzniká, mění se a zaniká, co zakládá příspěvkovou povinnost a jak je veden seznam členů? U vyloučení načti zvláštní pravidla výzvy, vyjádření, vnitřního opravného postupu a soudní ochrany; nevydávej jej za běžné rozhodnutí orgánu bez odlišení. U pobočného spolku ověř rozsah osobnosti, stanovami určenou vazbu a konkrétní pravidla ručení.
- Soudní přezkum: kdo je legitimován, jaké rozhodnutí je napadáno, kdy se o něm dozvěděl a jaká ochrana už byla využita? Pro neplatnost, zdánlivost a jiné vady ověř vlastní důsledky a lhůty. Korektiv nevyslovení neplatnosti posuzuj podle všech kumulativních podmínek; ochranu třetích osob v dobré víře odděl. Neomezuj předběžnou ochranu majetku na doslovně uvedený prodej, může jít o jinou dispozici či výkon hlasovacích práv.
- Nadace a fondy: jaký účel, majetkový režim a orgány se použijí? Ověř nakládání s jistinou, nadační příspěvky, příjemce spojené s orgány, schvalování, vyúčtování a vrácení, přidružený fond a změnu účelu. U ústavu ověř vztah zakladatele, ředitele a rady, poskytované služby a kontrolu hospodaření; nepřenášej mechanicky spolková pravidla.
- Financování: jde o členský příspěvek, dar, reklamu, nadační příspěvek, dotaci, veřejnou sbírku či ekonomickou činnost? Rozhoduje obsah a protiplnění, ne pouze název smlouvy. U smíšených plnění odděl části a podmínky použití; vyčísli dopad pro obě strany. Ověř crowdfunding, bezhotovostní sbírku, dárcovské zprávy, oznámení, evidenci, vyúčtování a sankce podle rozhodného režimu.
- Dotace a dobrovolnictví: ověř poskytovatele, titul, program a podmínky, nárokovost, veřejnoprávní smlouvu, změny účelu a rozpočtovou kázeň. Prověř akreditaci, dobrovolnickou smlouvu, náklady, pojištění, bezpečnost a postavení osob. U sociálních služeb doplň registraci, smluvní režim a financování.
- Daně a účetnictví: splňuje osoba znaky veřejně prospěšného poplatníka a není ve výluce? Odděl hlavní a vedlejší činnost, příjmy mimo předmět, osvobozené a zdanitelné příjmy. Ověř účelové dary, odpočet dárce, reklamu, DPH, ekonomickou činnost, registraci a přiznání. Zjisti podmínky účetního režimu, auditu, výroční zprávy a ukládání listin. Nepředpokládej existenci zapisovatelného statusu pouze podle názvu institutu.
- Odpovědnost: jaká povinnost byla porušena a komu vznikla újma? Posuď orgány, zaměstnance i právnickou osobu, odměnu za funkci, pojištění a možnou trestní přičitatelnost. Zpronevěru, dotační podvod nebo porušení správy cizího majetku neposuzuj jen z hospodářského neúspěchu.
- Změny a zánik: ověř změnu stanov, právní formy, fúzi, rozdělení, ochranu členů a věřitelů, zrušení dobrovolné či soudní, likvidaci, použití zůstatku a výmaz. Přetrvávající závazky a dotační podmínky mohou změnit vhodnost zvolené varianty.

### Povinný výstup

V SLV (`ns`, `us`, u daní `nss`) vyhledej přiléhavou judikaturu k autonomii, ochraně člena, výkladu stanov, příspěvkům, hospodaření a daním. Výstup spoj s konkrétními listinami organizace a odliš údaj účastníka od doloženého faktu. Dodej požadované stanovy, usnesení, smluvní články či návrh soudu, nejen návod k jejich sepsání.

Závěr obsahuje postup, správný orgán, právní základ ze zákona a stanov, doložený počátek a konec lhůty, petit a důkazy. Náklady rejstříkového úkonu a sporného přezkumu počítej odděleně (`soudni_poplatek`, `odmena_advokata`, s přepočtem): osvobození v jednom typu řízení neprokazuje osvobození ve druhém. Uveď ekonomický a daňový dopad, souhlasy a otevřené dokumentační mezery.
