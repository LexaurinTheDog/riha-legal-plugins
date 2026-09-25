---
uuid: d81b733a-368e-414d-9a58-7a527d2f8245
name: it-pravo-kyberbezpecnost
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "IT právo a kyberbezpečnost ČR"
    summary: "Smlouvy o vývoji a licencování software, SaaS a cloud, IT outsourcing a SLA, open source, NIS2 a nový zákon o kybernetické bezpečnosti, regulované subjekty a hlášení incidentů, DORA, odpovědnost za bezpečnostní incident, platformy a DSA, elektronické podpisy a eIDAS."
    examplePrompts:
      - "Dodavatel software nedodal systém včas a klient chce odstoupit a získat zpět zálohy. Co říká smlouva o dílo v IT a jak řešit zdrojové kódy a licenci?"
      - "Klient je střední výrobní firma s 60 zaměstnanci. Spadá pod nový zákon o kybernetické bezpečnosti a co musí do kdy udělat?"
      - "Po ransomware útoku unikla data zákazníků. Jaké oznamovací povinnosti (NÚKIB, ÚOOÚ, zákazníci) a lhůty běží a jak omezit odpovědnost?"
  en:
    displayName: "Czech IT Law & Cybersecurity"
    summary: "Software development and licensing contracts, SaaS and cloud, IT outsourcing and SLA, open source, NIS2 and the new Cybersecurity Act, regulated entities and incident reporting, DORA, security breach liability, platforms and DSA, electronic signatures and eIDAS."
    examplePrompts:
      - "A software vendor missed the delivery deadline and my client wants to withdraw and recover advances. What do IT work contracts say and how to handle source code and licence?"
      - "My client is a mid-sized manufacturer with 60 employees. Does it fall under the new Cybersecurity Act and what must it do by when?"
      - "After a ransomware attack customer data leaked. Which notification duties (NÚKIB, data protection authority, customers) and deadlines apply and how to limit liability?"
  sk:
    displayName: "IT právo a kyberbezpečnosť ČR"
    summary: "Zmluvy o vývoji a licencovaní softvéru, SaaS a cloud, IT outsourcing a SLA, open source, NIS2 a nový zákon o kybernetickej bezpečnosti, regulované subjekty a hlásenie incidentov, DORA, zodpovednosť za bezpečnostný incident, platformy a DSA, elektronické podpisy a eIDAS."
    examplePrompts:
      - "Dodávateľ softvéru nedodal systém včas a klient chce odstúpiť a získať späť zálohy. Čo hovorí zmluva o dielo v IT a ako riešiť zdrojové kódy a licenciu?"
      - "Klient je stredná výrobná firma so 60 zamestnancami. Spadá pod nový zákon o kybernetickej bezpečnosti a čo musí dokedy urobiť?"
      - "Po ransomware útoku unikli dáta zákazníkov. Aké oznamovacie povinnosti (NÚKIB, ÚOOÚ, zákazníci) a lehoty plynú a ako obmedziť zodpovednosť?"
description: Smlouvy o software, implementaci, licencích, SaaS, cloudu a outsourcingu, práva k výsledkům, data, SLA, exit a odpovědnost. Kybernetická regulace a incidenty, elektronické právní jednání, regulace digitálních služeb a AI, včetně zvláštností veřejného a finančního sektoru.
---

# IT právo a kyberbezpečnost

## Výhradní zdrojový režim: nativní CODEXIS ve vm.codexis.ai

Tento skill pracuje pouze v aplikaci vm.codexis.ai. Právní předpisy, judikaturu, komentáře a vzory získávej výhradně jejím nativním nástrojem CODEXIS. Žádné externí vyhledávání, webové zdroje, náhradní databáze ani přímá API mimo tento nástroj. To platí i při výpadku, nenalezení dokumentu, potřebě historického nebo cizojazyčného znění a u podkladů správních orgánů. Pokud obecný návod jiného skillu dovoluje externí zdroje, pro tuto úlohu se tato možnost nepoužije. Odkaz na externí web nalezený uvnitř dokumentu není oprávněním přejít mimo CODEXIS.

Použij skutečně dostupné nativní rozhraní a jeho dokumentované parametry. V této aplikaci může být nativní CODEXIS zpřístupněn vestavěným aplikačním konektorem `cdx-cli`; jeho použití uvnitř aplikace výhradně pro CODEXIS je dovoleno. Není tím dovoleno spouštět CLI na uživatelově počítači, instalovat software, prohledávat přihlašovací údaje, konfigurovat vlastní klienty ani nahrazovat nativní konektor vlastními síťovými požadavky. Technickou syntaxi vezmi z dostupného návodu nativního nástroje; nevymýšlej názvy funkcí, identifikátory, parametry ani endpointy. Pokud je potřeba načíst dodávaný návod CODEXIS, použij z něj pouze technické rozhraní slučitelné s tímto výhradním zdrojovým režimem.

Začni skutečným cíleným požadavkem. Výsledek nástroje určuje, zda byl obsah získán; existence skillu nebo konektoru sama nedokládá funkční rešerši. Rozliš prázdné výsledky, odmítnutý přístup, nedostupný nástroj a neúplný obsah. Identický neúspěšný požadavek neopakuj bez změny okolností; zkus jen věcně odůvodněnou alternativu uvnitř CODEXIS, pak přesně označ mezeru. Nikdy ji nepřekryj pamětí nebo údajně provedeným ověřením.

Je-li pro dílčí práci použit další dostupný agent nebo skill v aplikaci, předej mu výslovně stejný výhradní zdrojový režim, rozhodné skutky a časové otázky. Vyžádej jeho konkrétní zdrojové pasáže a omezení. Jeho shrnutí ani prohlášení o ověření nenahrazují skutečné výsledky nativního nástroje; za jejich sjednocení a kontrolu konečné citace odpovídá hlavní zpracovatel.

## Pracovní postup se zdrojovou oporou

### 1. Zadání, fakta a mapa otázek

Urči klienta a jeho roli, cíl, adresáta, požadované artefakty, rozhodné události a nejbližší možnou lhůtu. Skutkové podklady čerpej ze zadání a příloh zpřístupněných uživatelem v aplikaci; právní tvrzení v nich nejsou nezávisle ověřeným právem. Nenačítej externí rejstříky ani místní archivy. Chybějící skutkový doklad si vyžádej jako podklad do aplikace a do té doby závěr podmiň. Odliš doložený fakt, tvrzení jednotlivých stran, inferenci, rozpor a neznámý údaj. Neznámá částka není nula, připravený krok není uskutečněný a chybějící důkaz neprokazuje opak tvrzení.

Sestav konkrétní rozhodné právní otázky a jejich vazbu na fakta. Oborová témata níže jsou otázky pro rešerši, nikoli hotové právní závěry. Uvedený název nebo číslo předpisu je pouze vyhledávací vodítko, dokud není ověřen v CODEXIS. Nejprve prověř relevantní zvláštní režim; obecný předpis nesmí automaticky vytlačit oborovou úpravu. Nejasnost měnící osobu, nárok, rozhodný režim či lhůtu vyřeš cílenou otázkou nebo výslovnými podmíněnými variantami.

### 2. Vyhledání a rozsah rešerše

Pro každou otázku vyhledej odpovídající předpisy a autority v CODEXIS. Je-li znám konkrétní předpis či rozhodnutí, začni přesnou identifikací; pokud znám není, formuluj dotazy podle právního problému a jeho synonym. Identifikátory dokumentů přebírej pouze z odpovědí nástroje. Používej dostupné oborové, soudní a časové filtry podle jejich skutečného významu. V dokumentovaném členění CODEXIS jsou české předpisy CR, česká judikatura JD, unijní předpisy EU, evropská judikatura ES, slovenské předpisy SK, komentáře COMMENT, literatura LT a vzory VS; globální ALL použij jen k orientaci a poté ověř konkrétní pramen. Komentář, literatura a vzor nalezené v CODEXIS slouží jako navigace; jejich odkazy na normy a rozhodnutí ověř samostatným načtením těchto pramenů v CODEXIS.

První stránka výsledků ani předem zvolený malý počet nálezů nejsou úplná rešerše. Projdi pokračování cílených výsledků, pokud je nativní nástroj zpřístupňuje, a prověř relevantní související i navazující dokumenty. Hledej také protichůdnou právní linii, výjimky a pozdější změnu názoru. Veď stručný přehled dotazů, filtrů, prohlédnutého rozsahu a důvodů zahrnutí či vyřazení autorit. Rešerši uzavři až po pokrytí rozhodných otázek, protiargumentů a relevantních odkazů; nedostupná pokračování nebo vyčerpaný rozpočet označ jako omezení, nikoli úplnost. Netvrď vyčerpání veškeré existující judikatury.

### 2a. Judikatura navázaná na rozhodný paragraf (R5.1)

Tato cesta je dokumentována ve schématu nativního konektoru (`cdx-cli schema related`, parametr `part`) a byla ověřena v aplikaci 25. 9. 2026. **Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf **oba** příkazy z bodů 1 a 2. Samotný počet z `/related/counts` nic nevybírá a krok nesplňuje. Fulltextové hledání v `JD` je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Počet navázané judikatury:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related/counts?part=paragraf<N>'` (např. `paragraf198`, `paragraf19c`; `elementId` ověř přes `/toc`).
2. **Kandidáti:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related?part=paragraf<N>&type=SOUVISEJICI_JUDIKATURA&limit=20'` - řazeno podle relevance. **Spusť ho vždy dvakrát:** podle relevance a s `&sort=date` (nejnovějších 20), aby ti neunikla rozhodnutí z posledních let; další stránky `&offset=20`, `&offset=40` … Projdi alespoň prvních 20 kandidátů (titulek, `/meta`) a relevantní zařaď do výběru. Vrácená `docId` lze přímo použít v `cdx://doc/<docId>/meta` a `/text`.
3. **Skutková shoda:** doplň fulltextem `search JD` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2-5 slov). Filtr soudu používej jen s přesnými hodnotami facety: `Nejvyšší soud`, `Nejvyšší správní soud`, `Ústavní soud`, `Vrchní soud` (Praha × Olomouc přes `--city "Praha"` / `--city "Olomouc"`); jiné hodnoty ověř přes `--with-facets`. Pro novou úpravu omez stáří přes `--issued-from`.
4. **Třídění kandidátů podle `/meta`** (před načtením celého textu podle kroku 4):
   - `derogated: true` → rozhodnutí je v CODEXIS označeno jako překonané; jako oporu je nepoužij. `false` nevylučuje pozdější odklon - ten prověř podle kroku 4;
   - **sjednocující rozhodnutí:** zjisti, zda k témuž paragrafu a téže otázce existuje pozdější rozhodnutí velkého senátu NS či NSS, stanovisko pléna nebo kolegia, nebo nález pléna ÚS (výsledek `&sort=date` z bodu 2 a fulltext `"velký senát" <právní pojem>`). Rozhodnutí vydané **před** ním použij jen tehdy, když ho sjednocující rozhodnutí výslovně přejímá; jinak ho označ jako překonané nebo neaplikovatelné a uveď proč. Ve zdrojovém přehledu uveď data obou rozhodnutí. Stejně prověř **každý judikát citovaný protistranou**: datum, předpis, k němuž byl vydán (např. obch. zák., ObčZ 1964), a zda nebyl překonán;
   - vyplněné `sbirkoveCislo` (např. `Rc 105/2013`) = publikováno v oficiální sbírce; má přednost před nepublikovaným rozhodnutím téhož soudu;
   - stanovisko a velký senát > běžný senát; nález ÚS > usnesení ÚS; NS / NSS / ÚS > vrchní > krajský soud;
   - rozhodnutí vydané k jinému znění paragrafu, než je rozhodné podle kroku 3, použij jen po ověření, že se pravidlo věcně nezměnilo.
5. Ve zdrojovém přehledu (krok 5) u každého judikátu uveď, zda pochází z vazby na paragraf, nebo z fulltextu. Když vazba na rozhodný paragraf vrací nulu, uveď to a pokračuj fulltextem.
6. **Nerozšiřuj závěr rozhodnutí na otázku, kterou soud neřešil.** Např. rozhodnutí o náležitostech výpovědi neřeší, *kdy* výpověď nabyla účinnosti, a rozhodnutí o povaze lhůty neřeší, na který den připadá její konec; takovou dílčí otázku odpověz samostatně podle zákona a případně další judikatury, jinak ji označ jako neověřenou.

### 3. Předpis: úplný relevantní text a správný časový režim

Pro každou nosnou normu vytvoř vazbu: právní otázka → rozhodná událost a datum → vybrané znění → přechodné pravidlo → důvod použitelnosti. Odděl hmotněprávní režim, procesní úkon, zdaňovací období a datum relevantní pro sazbu či náklady. Dnešní znění nesmí nahradit historicky nebo přechodně rozhodné znění. Seznam verzí nebo informace, že k určitému dni nebyla novela, neprokazují obsah ani použitelnost ustanovení.

Načti v CODEXIS úplný text použitého ustanovení v dané verzi, včetně všech odstavců, písmen a vět, které určují podmínky a výjimky. Připoj relevantní definice, odkazovaná ustanovení, zvláštní a prováděcí předpisy, přílohy a přechodná ustanovení novel. Odkazy sleduj, dokud je vysvětlen rozhodný právní následek; nepřeskakuj výjimku nebo negativní podmínku. U rozsáhlého předpisu nepostačuje izolovaný fragment bez systematického kontextu, ale není třeba vkládat celý zákon do odpovědi. Rozliš platnost, účinnost a případně odloženou použitelnost. Uchovej nástrojem vrácenou identitu verze a skutečně dostupná časová metadata; chybějící údaje nevytvářej.

Čísla, sazby, prahy, lhůty, koeficienty a jejich podmínky přebírej až z takto načteného znění. Samostatně dolož, proč se hodí na konkrétní skutkový stav. Cituj přesný paragraf či článek, odstavec a písmeno; neopírej závěr o obecný odkaz na celý zákon, pokud rozhoduje konkrétní pravidlo.

### 4. Judikatura: celý dokument, skutečný závěr a použitelnost

U každého rozhodnutí použitého jako právní opora načti celý text od výroku po závěr odůvodnění, včetně samostatných pokračování, příloh či odlišných stanovisek, jsou-li součástí dokumentu. Vyčerpej dostupné pokračování obsahu; shrnutí, vyhledávací úryvek, metadata ani právní věta nenahrazují rozhodnutí. Pokud nástroj dodá jen část, stav zůstává neúplný. Odděleně eviduj, zda byl dokument nalezen, celý načten a zda jeho závěr skutečně podporuje právní tezi; neodvozuj jeden stav z druhého.

Z úplného textu vytěž rozhodnou otázku, podstatné skutky, procesní situaci, výrok, vlastní nosné důvody soudu, omezení a případné odlišné stanovisko. Výslovně odliš tvrzení účastníka, rekapitulaci nižšího soudu, citaci jiné autority a vlastní právní závěr rozhodujícího soudu. Právní věta vydavatele ani odmítací výrok samy neurčují meritorní závěr.

Ke každé použité tezi připoj konkrétní bod; nejsou-li body, stránku nebo dohledatelný oddíl a krátkou identifikující pasáž. Ze zdroje přebírej soud, spisovou značku nebo číslo jednací a datum; ECLI uveď jen je-li dostupné. Doslovnou citaci porovnej s načteným textem, parafrázi označ a zachovej podmínky i výhrady. Uveď, proč je věc skutkově a právně srovnatelná a v čem se liší. Prověř v CODEXIS relevantní pozdější, překonávající a nepříznivou judikaturu. Odkaz uvnitř rozhodnutí není důkaz samostatného ověření citované věci.

### 5. Zdrojový přehled, argumentace a výstup

Interně udržuj pro každou nosnou právní tezi: otázku, zdroj a jeho identitu, časový režim, načtenou pasáž, stav úplnosti, důvod použitelnosti a omezení. Jde o evidenci skutečných výsledků nástroje, nikoli o tvrzení, že aplikace provedla neexistující automatickou certifikaci. Neověřenou tezi nepoužívej jako nepodmíněnou rozhodnou oporu. Při mezeře dodej užitečnou ověřenou část a přesně odděl, co vyžaduje další podklad nebo načtení v CODEXIS.

Každý nosný argument spoj s ověřeným pravidlem, konkrétním faktem a důkazem, subsumpcí, následkem a vazbou na požadované řešení. Zachovej primární, podpůrnou a eventuální linii; odchylku od pokynu odůvodni. Vypořádej nejsilnější protiargument bez zbytečného přiznání sporné skutečnosti. Je-li zadána praxe konkrétního senátu, identifikuj skutečný senát a jeho dostupná srovnávací rozhodnutí v CODEXIS; obecná judikatura soudu není náhradou. Nedostupnost popiš bez domyšleného trendu.

Odkazy přebírej ze zdrojového bloku nativního nástroje; nesestavuj neověřené URL a nepřecházej kvůli jejich ověření na externí web. Ve výstupu použij nástrojem vrácený uživatelský odkaz a přesnou právní citaci, nikoli interní ID či technickou adresu. Pokud uživatelský odkaz nebo metadata chybí, údaj nevymýšlej a stav označ. U citovaného ustanovení kontroluj přesnost textu, nikoli pouze funkční odkaz. V klientském textu neuváděj interní technický protokol, není-li vyžádán; omezení rozhodného závěru však musí zůstat viditelné.

### 6. Konečný artefakt, náklady a smlouvy

Před odevzdáním porovnej se zdrojovým přehledem i původními podklady celý konečný text včetně shrnutí, petitu, realizačního checklistu, rozpočtu a příloh. Nový závěr či nárok doplněný při psaní vyžaduje doplnění rešerše a opakování souvisejících kontrol. Vlastní předchozí shrnutí není náhradou původního pramene.

U procesního výstupu odděl pravomoc, věcnou a místní příslušnost, přípustnost, lhůtu a důvodnost. Každý výrok petitu musí odpovídat nároku, účastníkům, předmětu, rozsahu a času plnění a mít konkrétní skutkovou a právní oporu. Náklady prověř podle všech konečně navržených nároků a úkonů: osvobození, zpoplatněný předmět, položka, základ, sazba, počet úkonů, paušály a případná daň. Jistota není poplatek a smluvní odměna není automaticky náhradou přiznatelnou soudem. Výpočty uváděj s mezikroky a nezávislým přepočtem; neznámý parametr nenahrazuj nulou. U lhůty dolož událost, počátek, délku, pravidla běhu a konec. Interní bezpečnostní termín odliš od zákonného konce.

U smlouvy nebo revize dodej skutečně požadované úplné znění, ne jen seznam rizik. Odděl rozhodné právo od fóra, ověř kogentní ochranu, vazby definic, plnění, ukončení, vypořádání a alokace odpovědnosti. Varianty ekonomické a daňové výhodnosti porovnávej na doložených předpokladech včetně nákladů, nikoli jen nominální sazby. Omezení odpovědnosti formuluj ve prospěch klienta jen po ověření jeho přípustných mezí; nepředstírej platnost plošného zřeknutí. Redline musí zachovat originál a dohledatelné změny; u souboru netvrď jeho vytvoření, revize či kontrolu, pokud neproběhly dostupnými nástroji aplikace.

Zkontroluj všechny požadované artefakty. Označ pracovní, neúplný či k revizi určený výstup pravdivě. Uložení, odeslání, doručení, podpis a podání jsou odlišné stavy; žádný nepředstírej. Bez výslovného pokynu nic neposílej ani nepodávej. Nedodané části a neověřené rozhodné zdroje nesmějí být skryty prohlášením „hotovo“ nebo „vše ověřeno“.

## Oborové otázky a požadované výstupy

## Mandát a technické skutečnosti

Urči klienta, jeho roli dodavatele, objednatele, provozovatele či regulované osoby a obchodní cíl. Rozliš zakázkový software, implementaci, licenci, SaaS, cloud, outsourcing, hardware, IoT, platformu a AI. Zjisti spotřebitelský, podnikatelský, veřejný nebo finanční kontext. Zmapuj služby, dodavatele, země hostingu, data, kritické závislosti, smlouvy, skutečné technické možnosti a rozhodná data; právní klasifikaci neopírej o marketingový název produktu.

Každý závěr o právu vyhledej v nativním CODEXIS pro relevantní období, včetně přechodných pravidel, přímo použitelných unijních předpisů a prováděcích aktů. Technické tvrzení odděl od doloženého testu. Nefunkční záloha, neověřený export nebo chybějící klíče se nezhojí právní deklarací o předání.

## Dodávka, akceptace a obchodní podmínky

U smlouvy stanov funkční a technický rozsah, rozhraní, dokumentaci, metodiku vývoje, backlog a odpovědnost za změny. Rozliš pevný rozsah od průběžně řízeného vývoje. Uprav milníky, závislosti, součinnost, prostředí, testovací data a testy, kategorie vad, opakování testu a skutečné předpoklady akceptace. Prověř, kdy může mít mlčení či užívání akceptační význam; nezakládej převzetí neotestovaného díla na nepřiměřené automatické fikci bez právního a obchodního posouzení.

U ceny rozliš pevnou částku, odhad a časovou odměnu, rozpočtový strop, výdaje a platební milníky. Změnové řízení má před zahájením práce zachytit cenu, termín a dopad na rozsah. Uprav prodlení a příčinnou součinnost klienta, zadržení přiměřené platby, nápravu, částečné ukončení, vracení plateb a rozpracovaný výsledek. Odděl odpovědnost za vady, záruku, údržbu a následný rozvoj.

## Práva a použitelnost výsledku

Zmapuj autorský řetězec podle skutečného autora, pracovního vztahu, přímé objednávky a subdodávky. Vyhledej zvláštní režim objednaného počítačového programu či databáze a jeho podmínky; nepředpokládej, že každý samostatný dodavatel vyžaduje stejnou licenční konstrukci. Odděl oprávnění vykonávat majetková práva, licenci, vlastnictví nosiče a oprávnění třetích osob.

Licenci vymez podle užití, změn, spojení, území, doby, počtu uživatelů, převodu, sublicencí, výhradnosti a formy. Prověř zaměstnanecké odměny, dekompilaci, vyčerpání a limity smluvních zákazů. U open-source komponent zjisti konkrétní licenci, propojení, distribuci či vzdálené poskytování; nepřipisuj každé komponentě automatický dopad na celý zdrojový kód. Zahrň SDK, data, modely a práva k výstupům AI, obchodní tajemství a podmínky textového a datového vytěžování.

Praktickou nezávislost zajisti doloženým předáním zdrojů, sestavení, dokumentace, přístupů, klíčů, formátů dat a potřebných oprávnění. U úschovy zdrojů řeš kontrolu úplnosti a použitelnosti již před akceptací, aktualizace, podmínky vydání a oprávnění náhradního dodavatele. Step-in bez souhlasů a přístupů nemusí být proveditelný.

## Provoz, data a ukončení

SLA navrhni s měřitelnou dostupností, časovým základem, výlukami, údržbou, měřením, reakcí a obnovou. Rozliš cíl doby obnovy služby od cíle maximální ztráty dat vyjádřené časem; nezaměňuj tyto veličiny ani deklaraci s provedeným testem. Kredity neposuzuj automaticky jako jedinou nápravu. Limity odpovědnosti a její případné vyloučení vyvaž ve prospěch klienta v ověřených mezích, včetně výjimek, pojištění a vztahu k smluvní pokutě.

U osobních údajů vyhledej role, zpracovatelská ujednání, subdodavatele, audit, zabezpečení, předání do třetích zemí a právní použitelnost zvoleného mechanismu. U cloudu řeš koncentraci, umístění a dostupnost dat, změnu ceny, přenositelnost, export, přechodnou podporu, výmaz a doložení jeho rozsahu. Ve veřejném sektoru ověř zvláštní cloudové, evidenční či atestační požadavky, zadávání, změny závazku a riziko vendor lock-in. U finančního klienta samostatně vyhledej požadavky na ICT třetí strany, smlouvy, dohled a odolnost.

## Kybernetická regulace a incident

Klasifikuj službu podle skutečné činnosti, velikosti, skupinových vazeb, zvláštních kritérií a výjimek. Zjisti příslušný režim povinností a zda na digitální infrastrukturu dopadá zvláštní nebo přímá unijní úprava. Odděl účinnost předpisu, splnění podmínek regulované služby, registraci, doručení rozhodnutí a počátek jednotlivé povinnosti; nevztahuj datum jednoho úkonu mechanicky na vše.

Sestav přiměřený plán řízení rizik, odpovědných rolí, aktiv, přístupů, logování, kryptografie, záloh, kontinuity, školení a dodavatelského řetězce včetně případných omezení rizikových dodavatelů. U každé povinnosti uveď ověřený počátek, adaptační pravidlo, odpovědnou osobu a důkaz plnění.

Při incidentu zachovej logy, časovou osu, důkazní integritu, důvěrnost a bezpečné obnovení. Rozliš hlášení kybernetickému orgánu, ochranu osobních údajů, finanční dohled, policii, smluvní oznámení a pojištění. Každá větev má vlastní spouštěč, obsah a čas; vyhledej prvotní, návazné a závěrečné hlášení, případný průběžný stav při trvajícím incidentu a povinnosti po vyřešení. Prověř zvláštnosti poskytovatele důvěryhodných služeb. Oznamovací tabulku ani kontaktní návrh neoznačuj za uskutečněné hlášení. U vydírání zohledni sankce, trestní rizika a pojistné podmínky; nedoporučuj zatajení incidentu nebo protiprávní platbu.

## Elektronické jednání, digitální služby a AI

U elektronického úkonu ověř požadovanou formu a úroveň podpisu, zvláštní požadavky na ověření, podpis fyzické osoby versus pečeť, časové razítko, dlouhodobé uchování a prokazování identity. Samostatně posuď datové schránky, doručení, výjimky fikce, elektronickou identifikaci, bankovní identitu a digitální peněženky podle použitelné úpravy.

Podle produktu prověř hostování a obsah, digitální spotřebitelské plnění, platformové povinnosti, cookies a marketing, kybernetické požadavky na produkty a zranitelnosti i kritickou odolnost. U AI klasifikuj systém, poskytovatele, nasazujícího a další role podle účelu a použití; vyhledej zákazy, rizikovou kategorii, obecné modely, transparentnost, automatizované rozhodování a postupnou použitelnost. Zahrň výcviková data, zaměstnaneckou politiku a veřejné použití, pokud souvisejí se zadáním.

## Výstup

Dodej úplné požadované smluvní znění, akceptační či incidentní přílohu, zdrojově doloženou matici povinností a plán exitu. Zachovej otevřené incidentní úkoly až do splnění skutečných podmínek, nikoli do uplynutí univerzální doby. Připoj klientské varianty odpovědnosti, protinámitky, důkazní mezery a při sporu konkrétní nárok, petit a kontrolovatelný výpočet nákladů.
