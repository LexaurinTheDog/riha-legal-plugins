---
uuid: 484a894a-a6ca-429c-aa59-e8041b4f33af
name: socialni-zabezpeceni
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Sociální zabezpečení ČR"
    summary: "Starobní, invalidní a pozůstalostní důchody, nemocenské a mateřská, státní sociální podpora a hmotná nouze, příspěvek na péči a dávky pro OZP, pojistné a penále, námitky a žaloby proti ČSSZ a úřadu práce, přezkum posudků, koordinace sociálního zabezpečení v EU."
    examplePrompts:
      - "ČSSZ zamítla klientovi invalidní důchod, posudkový lékař stanovil pokles pracovní schopnosti 30 %. Jak podat námitky a čím posudek zpochybnit?"
      - "Klientka pracovala 8 let v Německu a 25 let v ČR. Kde a jak žádat o starobní důchod a jak se doby sčítají?"
      - "Úřad práce odňal příspěvek na péči ve III. stupni po kontrole. Jaké jsou lhůty pro odvolání a jak prokázat závislost?"
  en:
    displayName: "Czech Social Security Law"
    summary: "Old-age, invalidity and survivors' pensions, sickness and maternity benefits, state social support and material need, care allowance and disability benefits, contributions and penalties, appeals against ČSSZ and labour office decisions, medical assessment review, EU coordination."
    examplePrompts:
      - "The social security administration denied my client's invalidity pension; the assessing doctor set a 30% loss of working capacity. How to object and how to challenge the assessment?"
      - "A client worked 8 years in Germany and 25 in the Czech Republic. Where and how to claim an old-age pension and how are periods aggregated?"
      - "The labour office withdrew a level III care allowance after a review. What are the appeal deadlines and how to prove dependency?"
  sk:
    displayName: "Sociálne zabezpečenie ČR"
    summary: "Starobné, invalidné a pozostalostné dôchodky, nemocenské a materská, štátna sociálna podpora a hmotná núdza, príspevok na starostlivosť a dávky pre ZŤP, poistné a penále, námietky a žaloby proti ČSSZ a úradu práce, preskúmanie posudkov, koordinácia v EÚ."
    examplePrompts:
      - "ČSSZ zamietla klientovi invalidný dôchodok, posudkový lekár stanovil pokles pracovnej schopnosti 30 %. Ako podať námietky a čím posudok spochybniť?"
      - "Klientka pracovala 8 rokov v Nemecku a 25 rokov v ČR. Kde a ako žiadať o starobný dôchodok a ako sa doby sčítavajú?"
      - "Úrad práce odňal príspevok na starostlivosť v III. stupni po kontrole. Aké sú lehoty na odvolanie a ako preukázať odkázanosť?"
description: 'Use for Czech pension, sickness and health insurance, social contributions and non-insurance benefits: starobní, invalidní a pozůstalostní důchody, ČSSZ a posudky, námitky, nemocenské, mateřství a ošetřování, OSVČ a pojistné, státní sociální pomoc, rodičovský příspěvek, bydlení a hmotná nouze, OZP a péče, Úřad práce, nezaměstnanost, sociální služby, přeshraniční koordinace a pracovní úrazy. Research legal sources only through native CODEXIS in the application.'
---

# Sociální zabezpečení ČR

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

### 2a. Judikatura navázaná na rozhodný paragraf (R5)

Tato cesta je dokumentována ve schématu nativního konektoru (`cdx-cli schema related`, parametr `part`) a byla ověřena v aplikaci 25. 9. 2026. **Povinný krok:** jakmile máš z kroku 1 a 3 určen rozhodný předpis a paragraf, spusť pro každý nosný paragraf **oba** příkazy z bodů 1 a 2. Samotný počet z `/related/counts` nic nevybírá a krok nesplňuje. Fulltextové hledání v `JD` je až druhý krok a slouží k doplnění skutkové shody; nenahrazuje seznam navázaných rozhodnutí.

1. **Počet navázané judikatury:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related/counts?part=paragraf<N>'` (např. `paragraf198`, `paragraf19c`; `elementId` ověř přes `/toc`).
2. **Kandidáti:** `cdx-cli get 'cdx://cz_law/<číslo>/<rok>/related?part=paragraf<N>&type=SOUVISEJICI_JUDIKATURA&limit=20'` - řazeno podle relevance; pro vývoj judikatury přidej `&sort=date`, další stránky `&offset=20`, `&offset=40` … Projdi alespoň prvních 20 kandidátů (titulek, `/meta`) a relevantní zařaď do výběru. Vrácená `docId` lze přímo použít v `cdx://doc/<docId>/meta` a `/text`.
3. **Skutková shoda:** doplň fulltextem `search JD` s krátkým dotazem (právní pojem + klíčový skutkový znak, 2-5 slov). Filtr soudu používej jen s přesnými hodnotami facety: `Nejvyšší soud`, `Nejvyšší správní soud`, `Ústavní soud`, `Vrchní soud` (Praha × Olomouc přes `--city "Praha"` / `--city "Olomouc"`); jiné hodnoty ověř přes `--with-facets`. Pro novou úpravu omez stáří přes `--issued-from`.
4. **Třídění kandidátů podle `/meta`** (před načtením celého textu podle kroku 4):
   - `derogated: true` → rozhodnutí je v CODEXIS označeno jako překonané; jako oporu je nepoužij. `false` nevylučuje pozdější odklon - ten prověř podle kroku 4;
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

## Rozhodný nárok, období a proces

Zapiš, zda klient žádá dávku, změnu její výše, obnovu výplaty, obranu proti odnětí, přeplatku nebo pojistnému. Rozliš důchodové a nemocenské pojištění, nepojistnou podporu, péči, zdravotní pojištění, nezaměstnanost a pracovněprávní náhradu. Urči vydávající orgán, posuzující instituci, fázi, doručení, osobu oprávněnou jednat a zahraniční prvek. Název dávky nestačí k určení opravného prostředku.

V CODEXIS zjisti právní režim rozhodného období včetně reformních přechodů, ročních parametrů a příloh prováděcích předpisů. Odděl vznik nároku, podání, posouzení zdravotního stavu, rozhodnutí a výplatu. Nová žádost a přezkum starého rozhodnutí nemusí mít stejný rozhodný skutkový okamžik.

### Oborové otázky

- Starobní důchod: jaký věk, doby pojištění a náhradní doby jsou rozhodné? Jak se prokazují práce, péče, studium, nezaměstnanost a zahraniční doby? Porovnej evidenční listy, informativní účet a další listiny; neexistence zápisu sama neprokazuje neexistenci doby. Ověř předčasnost, trvalé krácení, možnost výdělku, odklad, přepočet, valorizaci, péči o děti, základní a procentní výměru, redukce i rozhodné příjmy. Předdůchod z úspor neposuzuj automaticky jako předčasný státní důchod.
- Invalidita: jaká je rozhodující příčina dlouhodobě nepříznivého stavu, relevantní položka přílohy a její rozpětí? Diagnózy nesčítej. Ověř pravidla zvýšení a snížení hranice, společný limit důvodů změny, pracovní rekomandaci, potřebnou dobu pojištění, invaliditu z mládí a datum vzniku. Rozliš výdělečnou činnost, kontrolní prohlídku, změnu stupně, odnětí a přechod do jiného důchodu.
- Posudková mapa musí oddělit první stupeň, námitky či odvolání a soud. Zjisti skutečného autora, složení, dřívější účast a pravidla institucionální i osobní oddělenosti. Nový podpis není sám odstraněním konfliktu. Ke každému nálezu přiřaď lékařský podklad, chybějící vyšetření a konkrétní rozpor; navrhni doplnění nebo jiný odborný důkaz. Novou zprávu vztáhni k rozhodnému období, nevydávej pozdější nemoc za automatický důkaz nezákonnosti dřívějšího rozhodnutí.
- Pozůstalostní důchody: ověř okruh oprávněných vztahů, nezaopatřenost, trvání a obnovu nároku, péči, souběh a výši. Pojmy manželství, partnerství a soužití nepřenášej mezi verzemi bez kontroly; nezaopatřenost není jen věkový údaj.
- Nemocenské pojištění: ověř účast zaměstnance, dohodáře a OSVČ, ochrannou a podpůrčí dobu, denní základ a redukce. Odděl náhradu mzdy od nemocenského, peněžitou pomoc v mateřství, otcovskou, ošetřovné, dlouhodobou péči a vyrovnávací příspěvek. U dočasné neschopnosti řeš rozhodnutí lékaře, přezkum, režim, kontroly, krácení, povinnosti zaměstnavatele a přeplatky samostatně.
- Pojistné: jaký plátce, vyměřovací základ, hlavní či vedlejší činnost, záloha, přehled a splatnost se použijí? Ověř vliv souběhů a dohod, slev, paušálního režimu, minim a maxim. Rozliš kontrolní protokol, platební výměr a výkaz nedoplatků, námitky, splátky, prominutí, penále, promlčení a exekuci. Dluh společnosti automaticky neztotožňuj s dluhem jednatele; případnou odpovědnost a trestní rovinu založ na vlastních znacích.
- Nepojistné dávky: prověř přechod mezi systémy podpory, osobní a územní působnost, domácnost, rozhodné příjmy a majetek, náklady bydlení a součinnost. Odděl rodičovský příspěvek, podporu dětí a bydlení, porodné, pohřebné, živobytí, mimořádnou pomoc a pracovní motivační složky. Uveď oznamování změn, podmínky přeplatku a možnosti obrany; nedoporučuj zamlčení osoby, příjmu či majetku.
- OZP a péče: rozliš průkaz, mobilitu, pomůcku, spoluúčast a stupeň závislosti. Pro každou základní životní potřebu porovnej sociální šetření, typický den a zdravotní důkazy. Ověř právo vyjádřit se k podkladům, využití dávky, pečující osobu, smlouvu o sociální službě, úhrady, registraci a kontrolu poskytovatele.
- Zdravotní pojištění: ověř osobní účast, státního plátce, samoplátce, nárok na hrazenou péči, přeshraniční úhradu, změnu pojišťovny a obranu proti dluhu. U nezaměstnanosti odděl evidenci, podporu, rekvalifikaci a sankční vyřazení.
- Mezinárodní koordinace: ověř příslušnost při práci, vyslání, souběhu a práci na dálku, význam potvrzení, sčítání dob, dílčí důchody, export a přednost rodinných dávek. Posuď unijní, smluvní a případný zvláštní režim samostatně; daňová rezidence sama neurčuje pojištění.
- Pracovní úraz a nemoc z povolání: ověř uznání, odpovědný subjekt, liberaci, náhradu výdělku, rentu a valorizaci, bolest, náklady léčení, věcnou škodu a pozůstalé. Rozliš zákonné a smluvní pojištění, pracovní status a souběh s důchodem.

### Rozhodnutí a výstup

Přiléhavou judikaturu k posudkům, dokazování dob, dávkovým podmínkám a koordinaci načti v CODEXIS. Dodej matici podmínka, norma, důkaz, stav a riziko; konkrétní opravný prostředek, petit, příslušný orgán a vypočtenou lhůtu. Odděl právní moc, vykonatelnost a odkladný účinek. Poplatkové osvobození ověř pro danou věc; neodvozuj je od obecného sociálního charakteru. Výpočty opři o doložené příjmy a ověřené parametry s mezikroky, nikoli o historické sazby.
