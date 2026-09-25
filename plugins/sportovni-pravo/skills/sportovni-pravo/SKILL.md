---
uuid: 51c7259c-9474-4e02-9fe2-60f87af0d188
name: sportovni-pravo
version: 1.1.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Sportovní právo ČR"
    summary: "Smlouvy sportovců a klubů, svazové řády a přezkum disciplinárních rozhodnutí, přestupy a arbitráž, odpovědnost za sportovní úrazy, pořádání akcí, sponzoring, dary a veřejná podpora, antidoping, mládež."
    examplePrompts:
      - "Klub chce s hráčem uzavřít profesionální smlouvu jako s OSVČ. Jaká jsou rizika a co musí smlouva obsahovat?"
      - "Disciplinární komise svazu zastavila klientovi činnost na rok. Lze rozhodnutí napadnout u soudu a do kdy?"
      - "Nadace nabízí klubu příspěvek na vybavení výměnou za logo na dresech. Je to dar, nebo reklama, a jak se zdaní?"
  en:
    displayName: "Czech Sports Law"
    summary: "Athlete and club contracts, federation rules and disciplinary review, transfers and arbitration, liability for sports injuries, event organisation, sponsorship, donations and public funding, anti-doping, minors."
    examplePrompts:
      - "A club wants to sign a player as a self-employed professional. What are the risks and what must the contract contain?"
      - "A federation disciplinary committee suspended my client for a year. Can the decision be challenged in court and by when?"
      - "A foundation offers a club a contribution for equipment in exchange for a logo on jerseys. Is it a donation or advertising, and how is it taxed?"
  sk:
    displayName: "Športové právo ČR"
    summary: "Zmluvy športovcov a klubov v ČR, zväzové poriadky a preskúmanie disciplinárnych rozhodnutí, prestupy a arbitráž, zodpovednosť za športové úrazy, organizácia podujatí, sponzoring, dary a verejná podpora, antidoping, mládež."
    examplePrompts:
      - "Klub chce s hráčom uzavrieť profesionálnu zmluvu ako so SZČO. Aké sú riziká a čo musí zmluva obsahovať?"
      - "Disciplinárna komisia zväzu zastavila klientovi činnosť na rok. Možno rozhodnutie napadnúť na súde a dokedy?"
      - "Nadácia ponúka klubu príspevok na vybavenie výmenou za logo na dresoch. Je to dar alebo reklama a ako sa zdaní?"
description: 'Use for Czech sport: athletes, clubs, associations, agents, professional-player agreements, employment versus self-employment, transfers and loans, training compensation, federation discipline and review, arbitration and CAS, injuries, event safety, broadcasting and marketing, sponsorship, donations, public sports funding, antidoping, minors, coaches and e-sport. Coordinate employment, tax, association and contract analysis. Research legal sources only through native CODEXIS in the application.'
---

# Sportovní právo ČR

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

## Role a souběh sportovních režimů

Urči klienta: sportovec, klub, svaz, agent, trenér, pořadatel, divák, sponzor, dárce nebo veřejný podporovatel. Zjisti právní formu, členství, registraci, soutěž, přeshraniční vazby a smluvní řetězec. Odděl profesionalitu či amatérství od právního režimu činnosti; sportovní označení samo neřeší práci, daň ani pojištění.

Právní prameny a judikaturu ověřuj pouze nativně v CODEXIS. U stanov, soutěžních, přestupních, licenčních a disciplinárních řádů, antidopingových pravidel a arbitráže zjisti, zda jejich úplná rozhodná verze je tímto způsobem dostupná. Nedostupnost nezakrývej obecnou znalostí FIFA, UEFA, WADA nebo CAS. Listina dodaná klientem je podklad s vlastní proveniencí, nikoli důkaz nativního ověření její aktuálnosti. Kritický závěr bez potřebného pravidla ponech podmíněný a přesně označ mezeru.

### Povinné oborové otázky

- Vztah sportovec–klub: odpovídá skutečné provádění činnosti pracovnímu, civilnímu nebo jinému režimu? Zjisti pokyny, čas, místo, samostatnost, riziko, odměnu a výhradnost. V CODEXIS vyhledej skutkově přiléhavé soudní závěry a jejich meze. Nejistotu promítni do skutečných alternativ smluvních článků, nikoli do civilní etikety zakrývající závislou práci.
- Hráčská a trenérská smlouva: jak vymezit výkon, dobu, prodloužení, odměnu, bonus, náklady, zdravotní péči, pojištění a zranění? Ověř disciplinární oprávnění klubu, ukončení, konkurenční omezení, mlčenlivost, marketing a práva k podobě. U cizince řeš pobyt, pracovní oprávnění, zdanění a pojištění podle místa činnosti; u nezletilého zastoupení, vyspělost a zvláštní ochranu.
- Neplacení: odděl splatnost, podstatnost porušení, dodatečnou lhůtu a účinky odstoupení u pokračujícího plnění. Pracovněprávní skončení neposuzuj jako civilní odstoupení. Zadané platby, dluhy a oznámení přenes beze změny také do konečného checklistu.
- Svazová správa: který akt, orgán a verze řádu jsou rozhodné? Ověř právo být slyšen, dokazování, podjatost, vnitřní opravné prostředky, legitimaci a rozsah soudního přezkumu. Vyloučení člena, běžné rozhodnutí orgánu, rozhodčí komise a arbitráž nemusí mít stejnou cestu ochrany. Odděl sportovní uvážení od zákonnosti a proporcionality. Zjisti samostatné lhůty svazové, arbitrážní a soudní.
- Přestup, hostování a zastoupení: kdo převádí jaká práva a co je podmínkou registrace či způsobilosti ke startu? Prověř výchovné, solidaritu, platby mezi kluby, agentovu roli, střet zájmů, oprávnění, exkluzivitu a ukončení. Smluvní účinnost není totožná se sportovní registrací. U mládeže a přeshraničního pohybu ověř zvláštní omezení a případné unijní soutěžní souvislosti.
- Odpovědnost při sportu: odděl újmu sportovce, škodu klubu, odpovědnost jiného účastníka, trenéra, provozovatele a pořadatele. Zjisti porušení pravidel, povahu sportu, přijaté riziko, kauzalitu, zdravotní způsobilost, dohled a bezpečnost vybavení. V pracovním režimu ověř vlastní limity a výjimky náhrady i pracovní úraz; nepodmiňuj jej mechanicky civilním zaviněním klubu.
- Každý cap nebo waiver posuď směrově za klienta a podle konkrétního režimu, včetně kogentních výjimek. Nesnižuj současně klientovy vlastní nároky bez pokynu. Vyčísli známý ekonomický rozdíl; neznámé daňové a pojistné vstupy ponech otevřené.
- Pořádání akcí: prověř pořadatelskou službu, divácké násilí, bezpečnost, obecní povolení, zábor a dopravu, hluk, hudební práva, pojištění, vstupenky a storno. U přenosových práv ověř rozsah licence, významné události, kolektivní prodej a soutěžní omezení. U kamer, akreditace a marketingu posuď osobní údaje.
- Financování: jde obsahově o reklamu, dar, nadační příspěvek, členský příspěvek nebo dotaci? Ověř protiplnění, schvalování, účel, vyúčtování, vrácení, veřejně prospěšný režim, hlavní a vedlejší činnost, DPH a odpočty. U podpory sportovní infrastruktury a NSA rozliš rozhodnutí, program, evidenci a veřejnou podporu; zápis do rejstříku sportu sám nepotvrzuje nárok. Reklamu hazardu a alkoholu posuď se zvláštní ochranou mládeže.
- Antidoping a ochrana dětí: ověř dostupnou rozhodnou úpravu kontroly, zakázaného jednání, výjimek, sankcí a přezkumu, smluvní a pracovní dopady i trestní rovinu. U mládeže řeš bezpečí, dohled, oznámení a ochranu před zneužíváním. Nenavrhuj obcházení kontrol, registrace nebo bezpečnostních pravidel.

### Výstup pro klienta

Dodej matici nárok či krok, právní základ a jeho povaha, orgán, lhůta, důkaz, riziko a další potřebný zdroj. Ke sporu připoj vykonatelný petit a položkové náklady; ke smlouvě úplné použitelné články a vědomý rozhodovací bod mezi režimy. Zohledni smír, sportovní dopad přerušení činnosti, finance a reputaci. Nevyřešená dostupnost svazového či arbitrážního pravidla nesmí být označena za úplnou rešerši.
