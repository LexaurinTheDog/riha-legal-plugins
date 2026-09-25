---
uuid: 7e6a23ab-70c6-4c2b-a3fd-96bceb2335df
name: e-commerce-digitalni-sluzby
version: 1.1.1
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "E-commerce a digitální služby ČR"
    summary: "E-shopy a distanční smlouvy, informační povinnosti a 14denní odstoupení, obchodní podmínky, shoda a záruka u zboží a digitálního obsahu, reklamace a ADR, nekalé praktiky a pravidla slev, online tržiště a povinnosti platforem dle DSA a P2B, cookies a přímý marketing, platební služby a chargeback, bezpečnost výrobků, přístupnost, přeshraniční prodej, příslušnost a DPH OSS."
    examplePrompts:
      - "Klient spouští e-shop s elektronikou pro ČR a Slovensko. Zreviduj obchodní podmínky a nákupní proces: informační povinnosti, tlačítko objednávky, odstoupení, reklamace, slevy, cookies a DPH."
      - "Zákazník vrátil po 13 dnech rozbalený a použitý robotický vysavač a chce celou kupní cenu. Musí e-shop vracet vše, nebo lze krátit za snížení hodnoty, a jak to prokázat?"
      - "Klient provozuje online tržiště, kde prodávají třetí strany. Jaké povinnosti má vůči DSA, P2B a spotřebitelům a kdy odpovídá za vadné zboží prodejců?"
  en:
    displayName: "Czech E-commerce & Digital Services"
    summary: "Online shops and distance contracts, consumer information duties and the 14-day withdrawal, terms and conditions, conformity and warranty for goods and digital content, complaints and ADR, unfair commercial practices and price-reduction rules, online marketplaces and platform obligations under the DSA and P2B, cookies and direct marketing, payment services and chargebacks, product safety, accessibility, cross-border sales, jurisdiction and VAT OSS."
    examplePrompts:
      - "My client is launching an electronics e-shop for the Czech Republic and Slovakia. Review the terms and the checkout: information duties, order button, withdrawal, complaints, discounts, cookies and VAT."
      - "A customer returned an unboxed, used robot vacuum after 13 days and wants the full price back. Must the e-shop refund everything, or can it deduct for diminished value, and how to prove it?"
      - "My client runs an online marketplace with third-party sellers. What are its obligations under the DSA, P2B and consumer law, and when is it liable for sellers' defective goods?"
  sk:
    displayName: "E-commerce a digitálne služby ČR"
    summary: "E-shopy a dištančné zmluvy, informačné povinnosti a 14-dňové odstúpenie, obchodné podmienky, zhoda a záruka pri tovare a digitálnom obsahu, reklamácie a ADR, nekalé praktiky a pravidlá zliav, online trhoviská a povinnosti platforiem podľa DSA a P2B, cookies a priamy marketing, platobné služby a chargeback, bezpečnosť výrobkov, prístupnosť, cezhraničný predaj, príslušnosť a DPH OSS."
    examplePrompts:
      - "Klient spúšťa e-shop s elektronikou pre ČR a Slovensko. Zreviduj obchodné podmienky a nákupný proces: informačné povinnosti, tlačidlo objednávky, odstúpenie, reklamácie, zľavy, cookies a DPH."
      - "Zákazník vrátil po 13 dňoch rozbalený a použitý robotický vysávač a chce celú kúpnu cenu. Musí e-shop vracať všetko, alebo možno krátiť za zníženie hodnoty, a ako to preukázať?"
      - "Klient prevádzkuje online trhovisko, kde predávajú tretie strany. Aké povinnosti má voči DSA, P2B a spotrebiteľom a kedy zodpovedá za chybný tovar predajcov?"
description: Použij pro online prodej, distanční a mimo provozovnu uzavřené smlouvy, e-shopy, digitální obsah a služby, tržiště, platformy, dropshipping, předplatné, obchodní podmínky, objednávky, odstoupení, vady, reklamace, reklamu, cookies, platby, DSA, P2B, GPSR, přístupnost a přeshraniční daňové souvislosti. Specializované otázky dat a IT smluv koordinuj s GDPR a IT skilly. Právní zdroje pouze nativním CODEXIS.
---

# E-commerce a digitální služby ČR

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

## Oborový postup: e-shop a digitální služby

### Model, zákazník a působnost
Z podkladů zjisti, zda klient prodává vlastní zboží, poskytuje digitální obsah nebo službu, předplatné, zprostředkovává, provozuje tržiště či srovnávač, používá dropshipping nebo působí jako prodejce na platformě. Rozliš B2C, B2B, C2C a smíšený účel; uvedení identifikačního čísla samo neřeší každý status zákazníka. Urči kanál, cílové státy, jazyk, měnu, způsob dodání, platby, regulované produkty a rozhodné datum. V CODEXIS ověř soukromoprávní, veřejnoprávní a platformní vrstvy včetně přechodných pravidel; nový předpis nebo návrh nesmí být bez ověření zaměněn za použitelné právo.

### Nákupní cesta a obchodní podmínky
Pro každý krok od nabídky po potvrzení smlouvy porovnej skutečný klientský text nebo snímek s konkrétním zákonným požadavkem. Ověř identitu a kontakt, vlastnosti, celkovou cenu, daně, dopravu, platbu, dodání, trvání, ukončení, digitální funkčnost, kompatibilitu, aktualizace, reklamace, záruku a ADR. Prověř personalizovanou cenu, dodatečné platby, trvalý nosič a zachování použité verze podmínek.

Zkoumej význam tlačítka, okamžik vzniku smlouvy, rozdíl potvrzení objednávky a smlouvy, cenovou chybu a důkaz seznámení s podmínkami. Každé informační vadě přiřaď vlastní soukromoprávní a správní následek. Chybějící poučení o odstoupení neposuzuj stejně jako libovolný jiný nedostatek a prodloužení lhůty nevyvozuj univerzálně. U dlouhodobých smluv prověř změny podmínek, cen a automatickou obnovu.

### Odstoupení a vypořádání
Rozliš odstoupení bez důvodu, reklamaci, ukončení digitální služby a odstoupení pro porušení. U každé větve ověř vznik práva, počátek a běh lhůty, formu, výjimky a důkazní břemeno. U postupného dodání, předplatného, služeb a digitálního obsahu neaplikuj jednotný spouštěč.

U výjimek načti úplné podmínky individualizovaného, kazícího se či zapečetěného zboží, médií, termínovaných služeb, naléhavých oprav a digitálního plnění. Prověř skutečnou žádost či souhlas, poučení a potvrzení; předzaškrtnuté pole nevydávej za důkaz aktivního jednání. Zjisti rozsah vrácení ceny a dopravy, náklady zpětného odeslání, zadržení refundace, způsob platby, poměrnou úhradu služby a prokázané snížení hodnoty. Paušální odmítnutí rozbaleného zboží ani automatické započtení újmy nenahrazuje konkrétní test.

Po již účinném ukončení dodej postup vypořádání, nikoli znovu pouze návrh budoucího odstoupení. U digitálního plnění rozliš uživatelské soubory, osobní údaje a interní analytická data a ověř nárok na dostupnost či vrácení obsahu.

### Vady a reklamační proces
Rozliš zboží, zboží s digitálními prvky, digitální obsah a digitální službu. Ověř subjektivní a objektivní shodu, vliv reklamy, aktualizace, možné zvlášť odsouhlasené odchylky a domněnky. Zkoumej nové, použité a pro konkrétní vadu zlevněné zboží, dobu vytknutí, odstranění vady a informační povinnosti při vyřízení. Rozděl opravu, výměnu, slevu, odstoupení a náklady včetně přepravy či demontáže podle jejich podmínek. Záruku za jakost nezaměňuj se zákonnou odpovědností.

Z podkladů zjisti reklamaci, potvrzení, předání do opravy, vyřízení a informování zákazníka jako odlišné události. Ověř odpovědnou osobu: prodejce, výrobce, dovozce nebo poskytovatele záruky. B2B režim a jeho notifikaci řeš zvlášť; omezení práv a odpovědnosti posuzuj podle skutečné ochrany strany.

### Marketing, bezpečnost a platformy
Prověř ceny a slevy včetně referenčního období a výjimek, recenze a jejich ověřování, placené řazení, falešnou naléhavost, diskriminaci a nekalé praktiky. U cookies, newsletteru, volání, personalizace a zákaznických účtů odděl právní základ, souhlas, zákaznickou výjimku, informování, odhlášení, retenci a zpracovatele. Nepovažuj celou analytiku za technickou nezbytnost.

U DSA a P2B zjisti konkrétní kategorii služby a výjimky podle její velikosti či funkce. Prověř kontaktní místa, identifikaci obchodníků, odpovědnost za obsah, oznámení, odůvodnění, stížnosti, mediaci, transparentnost, reklamu, doporučování a ochranu nezletilých. Zprostředkovatele neoznačuj automaticky za prodávajícího; analyzuj jeho skutečné vystupování. U dropshippingu prověř zvlášť smluvní, dovozní a bezpečnostní roli.

Zahrň GPSR, odpovědnou osobu, informace v nabídce, stažení a informování zákazníků; podle produktu sektorová pravidla pro potraviny, léčiva, kosmetiku, hračky, elektro, ochranné prostředky, alkohol, tabák a další regulované zboží. Ověř přístupnost, její výjimky, obaly, odpady, baterie a rozšířenou odpovědnost výrobce. Právní stav ADR či dřívější ODR infrastruktury ověř v CODEXIS, nepřebírej starý vzor.

### Platby, hranice a výstupy
Rozliš bránu a poskytování platebních služeb, silné ověření, zákonné vrácení platby a pravidla chargebacku, BNPL, poukazy, věrnostní programy a kryptoaktiva. U přepravy zjisti přechod nebezpečí, nedodání, zásilku poškozenou cestou a postavení výdejního místa. Přeshraničně odděl rozhodné právo, fórum, zaměření činnosti, kogentní ochranu a geoblocking. Daňově prověř DPH, místo plnění, OSS/IOSS, domnělého dodavatele, cla, příjmy a oznamování platforem.

Dodej tabulku prvek–požadavek–stav–následek–oprava a úplné texty zadaných podmínek, tlačítek, poučení či odpovědí. Ověř soudní nebo ADR cestu, dohled a náklady zvlášť. Zohledni hromadné a přeshraniční spory. Nepředkládej audit souladu nepředloženého rozhraní jako hotový a nenavrhuj obcházení spotřebitelských práv.
