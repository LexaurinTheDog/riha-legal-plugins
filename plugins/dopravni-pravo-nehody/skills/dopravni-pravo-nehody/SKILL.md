---
uuid: 95b3ce6d-ee08-44bc-82fc-e43edd6308b9
name: dopravni-pravo-nehody
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Dopravní právo a nehody ČR"
    summary: "Odpovědnost a náhrada újmy z dopravní nehody, pojistné plnění z povinného ručení, dopravní přestupky a bodový systém, zadržení řidičského průkazu, trestné činy v dopravě, dopravci a cestující."
    examplePrompts:
      - "Klientovi do auta narazil řidič, který od nehody ujel. Kdo zaplatí škodu a jaké nároky uplatnit?"
      - "Řidiči byl zadržen řidičský průkaz po naměření 1,2 promile. Co mu hrozí a jak postupovat v prvních dnech?"
      - "Pojišťovna viníka krátí náhradu za opravu o amortizaci a odmítá náhradní vozidlo. Je to v souladu s judikaturou?"
  en:
    displayName: "Czech Traffic Law and Accidents"
    summary: "Accident liability and compensation, motor insurance claims, traffic offences and the points system, licence suspension, traffic crimes, carriers and passengers."
    examplePrompts:
      - "A hit-and-run driver crashed into my client's car. Who pays the damage and which claims to raise?"
      - "A driver's licence was seized after a reading of 1.2 per mille. What does he face and how to proceed in the first days?"
      - "The at-fault party's insurer deducts depreciation from repair costs and refuses a replacement car. Is that consistent with case law?"
  sk:
    displayName: "Dopravné právo a nehody ČR"
    summary: "Zodpovednosť a náhrada ujmy z dopravnej nehody v ČR, poistné plnenie z povinného zmluvného poistenia, dopravné priestupky a bodový systém, zadržanie vodičského preukazu, trestné činy v doprave, dopravcovia a cestujúci."
    examplePrompts:
      - "Klientovi do auta narazil vodič, ktorý od nehody ušiel. Kto zaplatí škodu a aké nároky uplatniť?"
      - "Vodičovi bol zadržaný vodičský preukaz po nameraní 1,2 promile. Čo mu hrozí a ako postupovať v prvých dňoch?"
      - "Poisťovňa vinníka kráti náhradu za opravu o amortizáciu a odmieta náhradné vozidlo. Je to v súlade s judikatúrou?"
description: Use when the user's matter involves Czech road traffic, vehicles or transport - dopravní nehoda, hlášení policii, viník, poškozený, provozovatel vozidla, odpovědnost z provozu dopravního prostředku (§ 2927+ OZ), střet vozidel, spoluzavinění, náhrada škody na vozidle, amortizace, náhradní vozidlo, újma na zdraví, povinné ručení (168/1999 Sb.), pojistitel, Česká kancelář pojistitelů, garanční fond, nepojištěné vozidlo, regres pojistitele, havarijní pojištění, zákon o silničním provozu (361/2000 Sb.), dopravní přestupek, rychlost, alkohol, drogy, bodový systém, vybodování, zadržení řidičského průkazu, zákaz řízení, příkaz na místě, odpor, přestupkové řízení, objektivní odpovědnost provozovatele, trestné činy v dopravě (§ 143, § 147, § 148, § 274, § 337 TZ), registr vozidel, STK, taxi, nákladní doprava, CMR, doby řízení, práva cestujících v letecké dopravě. Standalone skill - bundles CODEXIS methodology with traffic-practice method; no need to load the general codexis skill.
---

# Dopravní právo a nehody ČR

Samostatný oborový skill pro nehody, přestupky a trestné činy v dopravě a nároky z nich. Jedna událost obvykle běží ve **třech řízeních najednou** - přestupkové/trestní, pojistné (povinné ručení) a civilní (náhrada újmy) - s různými lhůtami a různým důkazním břemenem. Odpovědnost provozovatele je objektivní; vina řidiče se řeší zvlášť.

## Operating Assumptions

- Pro CODEXIS výhradně `cdx-cli`; nainstalováno a přihlášeno, bez preflightu.
- Kanonické tvary: `cdx-cli get cdx://cz_law/361/2000/versions`, `cdx-cli get 'cdx://doc/<versionId>/toc'`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf125c'`, `cdx-cli get cdx://cz_law/168/1999/versions`, `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf2927'`, `cdx-cli search JD --query "amortizace náhrada škody oprava vozidla obvyklá cena" --court "Nejvyšší soud" --limit 5`.
- Zákon o silničním provozu byl zásadně novelizován k 1. 1. 2024 (nový bodový systém, sazby pokut, zákazy řízení) a průběžně dál; zákon o povinném ručení byl nahrazen novou úpravou (ověř číslo a účinnost). **Sazby pokut, počty bodů, délky zákazů, hranice hlášení nehody, limity plnění a lhůty ověř v aktuálním znění k datu skutku**; paragrafy s písmeny dohledávej přes `/toc`. Nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| Zákon o silničním provozu | 361/2000 Sb. | `cz_law/361/2000` | Povinnosti řidiče (§ 4-§ 5), alkohol a návykové látky, nehoda (§ 47), řidičské oprávnění a průkaz, zadržení ŘP (§ 118a+), bodový systém (§ 123a+), kauce (§ 124a+), přestupky (§ 125c+), objektivní odpovědnost provozovatele (§ 125f+) |
| Zákon o odpovědnosti za přestupky | 250/2016 Sb. | `cz_law/250/2016` | Promlčení (§ 29-§ 32), příkaz a příkaz na místě (§ 90-§ 92), řízení, odvolání, upuštění od zbytku zákazu činnosti (§ 47) |
| Zákon o pojištění odpovědnosti z provozu vozidla | 168/1999 Sb. (a nástupnická úprava - ověř) | `cz_law/168/1999` | Rozsah pojištění, přímý nárok proti pojistiteli, lhůty pro šetření, regres pojistitele, ČKP a garanční fond, nepojištěná vozidla |
| OZ | 89/2012 Sb. | `cz_law/89/2012` | Provoz dopravních prostředků (§ 2927-§ 2932), obecná odpovědnost (§ 2910), spoluzavinění (§ 2918), škoda na věci (§ 2969), újma na zdraví (§ 2958+), promlčení (§ 620+, § 635 u pojistného plnění - ověř), pojistná smlouva (§ 2758+) |
| Trestní zákoník | 40/2009 Sb. | `cz_law/40/2009` | Usmrcení z nedbalosti (§ 143), ublížení na zdraví z nedbalosti (§ 147-§ 148), neposkytnutí pomoci řidičem (§ 151), ohrožení pod vlivem návykové látky (§ 274), maření výkonu (§ 337), zákaz činnosti (§ 73) |
| Zákon o podmínkách provozu vozidel | 56/2001 Sb. | `cz_law/56/2001` | Registr vozidel a lhůty přepisu, technická způsobilost, STK, sankce |
| Zákon o pozemních komunikacích | 13/1997 Sb. | `cz_law/13/1997` | Závady ve sjízdnosti a odpovědnost vlastníka komunikace (§ 27) |
| Zákon o silniční dopravě | 111/1994 Sb. | `cz_law/111/1994` | Dopravci, taxislužba, doby řízení, tachografy, sankce |
| Zákon o získávání odborné způsobilosti / vyhláška o zdravotní způsobilosti | 247/2000 Sb. / 277/2004 Sb. | `cz_law/247/2000`, `cz_law/277/2004` | Autoškoly, zdravotní způsobilost řidičů, lékařské prohlídky |
| Úmluva CMR / nařízení o dobách řízení | 11/1975 Sb. / (ES) 561/2006 | zdroj `CR`, `EU` | Mezinárodní nákladní přeprava, odpovědnost dopravce a limity, doby řízení a odpočinku |
| Nařízení o právech cestujících v letecké dopravě | (ES) 261/2004 | zdroj `EU` | Náhrada při zpoždění, zrušení a odepření nástupu |
| Metodika NS k náhradě nemajetkové újmy | - | zdroj `JD`/`LT` | Bolestné a ztížení společenského uplatnění (pomůcka, ne předpis) |

## Rešeršní strategie

1. `/versions` **k datu nehody / skutku** → `/toc` (paragrafy 118a, 123a, 125c, 125f) → `/text?part=`.
2. Judikatura: **NS** senát 25 Cdo (odpovědnost z provozu, střet, amortizace, náhradní vozidlo, ztížení uplatnění), senáty Tdo (§ 274, § 143, § 147 TZ), **NSS** (přestupky, měření rychlosti, objektivní odpovědnost provozovatele, zadržení ŘP, body), **ÚS** (amortizace, ne bis in idem), **SDEU** (`ES` - směrnice o pojištění motorových vozidel, nařízení 261/2004). Ověř datum a novelu.
3. Komentář (`COMMENT`) k pojmům (provozovatel, zvláštní povaha provozu, stav vylučující způsobilost, závada ve sjízdnosti); metodiky ČKP a pojišťoven jsou orientace, ne pramen.

## Workflow

1. **Role a řízení.** Řidič-viník / poškozený / provozovatel / chodec, cyklista / dopravce / pojistitel. Zjisti, která řízení běží nebo hrozí: přestupkové (obecní úřad ORP, policie), trestní (PČR, SZ), pojistné (pojistitel viníka, ČKP, vlastní havarijní), civilní (náhrada újmy). Pro každé zaznamenej lhůty.
2. **Na místě a hned po nehodě.** Povinnosti účastníka (§ 47 - zastavit, označit, pomoc, totožnost; **hlášení policii** při zranění, škodě nad zákonnou hranici, škodě na majetku třetí osoby nebo komunikaci, při nemožnosti obnovit provoz - ověř hranici), společný záznam o nehodě (formulář) s náčrtem a podpisy, foto, svědci, kamera, dechová zkouška (odmítnutí = přestupek s nejvyšší sazbou), lékařské vyšetření i při zdánlivě lehkém zranění, oznámení pojistiteli (lhůty v pojistných podmínkách), neuznávat vinu bez právního posouzení; **neopouštět místo** (přestupek / § 151 TZ, regres pojistitele).
3. **Odpovědnost za újmu.** **Objektivní odpovědnost provozovatele** (§ 2927 - liberace jen nemohl-li škodě zabránit ani při vynaložení veškerého úsilí, ne u vad provozu), provozovatel × řidič × ten, kdo užil vozidlo bez vědomí (§ 2930), **střet provozů** (§ 2932 - podle míry účasti, ne jen viny), obecná odpovědnost řidiče (§ 2910), spoluzavinění poškozeného (§ 2918 - pás, přilba, jízda s opilým řidičem), odpovědnost vlastníka komunikace za závadu ve sjízdnosti (§ 27 zák. 13/1997 Sb. - ověř podmínky), odpovědnost dopravce vůči cestujícím.
4. **Nároky poškozeného.** Vozidlo: náklady opravy (obvyklá cena, **amortizace jen výjimečně** - judikatura ÚS a NS o zhodnocení), totální škoda (obvyklá cena před nehodou minus vrak), znehodnocení, odtah, **náhradní vozidlo po dobu nezbytnou** (i po totální škodě do vyplacení), znalecký posudek, ušlý zisk; zdraví: bolestné a ztížení společenského uplatnění (§ 2958 - Metodika NS), duševní útrapy blízkých (§ 2959), náklady léčení a péče, ztráta na výdělku a důchodu, renta, náklady pohřbu a výživa pozůstalým (§ 2966); věci ve vozidle; úroky z prodlení od výzvy. Uplatnit **přímo u pojistitele viníka** (přímý nárok; pojistitel má lhůtu k šetření a sdělení - ověř), u ČKP (nepojištěné nebo nezjištěné vozidlo - rozsah a spoluúčast ověř), z vlastního havarijního (regres pojistitele proti viníkovi). Promlčení: vůči škůdci 3 roky subjektivní (§ 620), vůči pojistiteli zvláštní úprava (ověř § 635 OZ / pojistný zákon); trestní řízení - adhezní nárok nejpozději před dokazováním v hlavním líčení.
5. **Regres a sankce pojistitele.** Regres pojistitele proti pojištěnému (alkohol/drogy, bez řidičského oprávnění, opuštění místa nehody, nezpůsobilé vozidlo, úmysl - ověř výčet a limity), pojistné podmínky havarijního pojištění (výluky), příspěvek nepojištěných do garančního fondu, sankce za provoz bez pojištění.
6. **Přestupky.** Skutková podstata (§ 125c - rychlost podle překročení, alkohol/drogy, mobil, pás, semafor, nehoda s neohlášením), sankce (pokuta, zákaz činnosti, body - **tabulka po 1. 1. 2024**, ověř), **příkaz na místě** (blok - souhlas = konečné, nelze odvolat), příkaz ve správním řízení (**odpor do 8 dnů** - řízení pokračuje, hrozí i přísnější sankce), ústní jednání, dokazování (kalibrace a ověření měřidla, výcvik obsluhy, foto, kamera, znalec), **promlčení** (§ 30 zák. 250/2016 Sb. - 1 rok, u závažnějších 3 roky; přerušení - ověř), odvolání 15 dnů (odkladný účinek), správní žaloba 2 měsíce; **objektivní odpovědnost provozovatele** (§ 125f-§ 125h - výzva k úhradě určené částky, možnost sdělit řidiče, nelze-li řidiče zjistit); souběh s trestním (ne bis in idem).
7. **Řidičské oprávnění a body.** Zadržení řidičského průkazu policií (§ 118a-§ 118c - důvody, rozhodnutí obecního úřadu, započtení do zákazu), zákaz činnosti (upuštění po výkonu poloviny - § 47 zák. 250/2016 Sb. / § 90 TZ), bodový systém (§ 123a+ - záznam, oznámení při 12 bodech, pozbytí oprávnění na 1 rok, odečet bodů a školení, námitky proti záznamu - lhůta ověř), vrácení oprávnění (přezkoušení, zdravotní a psychologické vyšetření), zdravotní způsobilost (lékařské prohlídky podle věku - ověř).
8. **Trestné činy v dopravě.** Ohrožení pod vlivem návykové látky (§ 274 - stav vylučující způsobilost, hranice podle judikatury a znaleckých posudků - ověř), usmrcení a ublížení z nedbalosti (§ 143, § 147-§ 148 - porušení důležité povinnosti, souběh), neposkytnutí pomoci (§ 151), maření výkonu (§ 337 - řízení v zákazu), obecné ohrožení; postup obhajoby (fáze, lhůty, dohoda o vině a trestu, podmíněné zastavení, náhrada škody jako polehčující), trest zákazu činnosti a jeho vliv na živnost/zaměstnání; poškozený v trestním řízení (zmocněnec, adhezní nárok, zajištění).
9. **Dopravci, cestující, vozidla.** Silniční doprava (koncese, taxislužba, eurolicence, doby řízení a odpočinku - nařízení 561/2006, tachografy, sankce dopravci i řidiči), nákladní přeprava (odpovědnost dopravce, CMR - limity a lhůty pro reklamaci a promlčení - ověř), cestující (přepravní podmínky, letecká kompenzace - nařízení 261/2004: zpoždění, zrušení, mimořádné okolnosti, lhůty), registr vozidel (přepis vozidla v zákonné lhůtě, odpovědnost převodce/nabyvatele, STK, ekologická likvidace), leasing a odpovědnost provozovatele.

## Časté pasti

- Opuštění místa nehody nebo nepřivolání policie tam, kde to zákon vyžaduje - přestupek/trestný čin a regres pojistitele.
- Odmítnutí dechové zkoušky nebo lékařského vyšetření - sankce jako při nejvyšší hladině.
- Souhlas s příkazem na místě „ať je klid" - blok je konečný, body se zapíší; odpor proti příkazu po 8 dnech je pozdě.
- Provozovatel ignoruje výzvu k úhradě určené částky - následuje řízení o objektivní odpovědnosti bez možnosti přenést na řidiče.
- Sazby, body a zákazy citované podle znění před 1. 1. 2024.
- Nárok uplatněný jen u viníka, ne u jeho pojistitele (a naopak); promlčení vůči pojistiteli počítané jako vůči škůdci.
- Přijetí krácení o amortizaci nebo odmítnutí náhradního vozidla bez odkazu na judikaturu ÚS/NS.
- Adhezní nárok uplatněný až po zahájení dokazování - soud o něm nerozhodne.
- Spoluzavinění poškozeného (pás, přilba) nezohledněné v odhadu nároku.
- Střet vozidel posuzovaný jen podle viny řidičů místo podle míry účasti provozů (§ 2932).
- Zákaz činnosti počítaný bez započtení doby zadržení ŘP; žádost o upuštění od zbytku zákazu před uplynutím poloviny.
- Doplňování hladiny alkoholu, rychlosti, dat a spisových značek z paměti - vždy z listin nebo `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** (co udělat / nepodepsat, do kdy; které řízení běží).
2. **Role a odpovědnost** (objektivní × zaviněná, spoluzavinění, regres).
3. **Právní rámec** - 361/2000, 250/2016, pojistný zákon, OZ, TZ v aktuálním znění k datu skutku, s odkazy.
4. **Nároky / obrana** - tabulka: nárok/úkon | právní základ | adresát | lhůta | důkaz.
5. **Rizika a alternativy** (body, zákaz, regres, dohoda s pojistitelem, znalec).
6. **Judikatura** - jen ověřená v CODEXIS, kompaktní citace; Metodika NS jako orientace.
7. **Podklady a otevřené otázky**, placeholdery `[DOPLNIT]`.

## Pravidla výstupu

- Odkazy jen přes resolvovanou `https://` URL ze source bloku; `cdx://` nikdy do výstupu; žádná raw ID.
- Paragraf jako klikací reference; rozhodnutí `SOUD - SP. ZN. - DD.MM.RRRR` (např. `NS - 25 Cdo 1234/2024 - …`, `NSS - 7 As 123/2025 - …`) z metadat, nikdy vymyšlené.
- Zachovej kvalifikátory („nemohl zabránit ani při vynaložení veškerého úsilí“, „podle míry účasti“, „do 8 dnů ode dne doručení“, „stav vylučující způsobilost“).
- Jeden časový řez; znění účinné v den nehody / skutku.
- Zdravotní údaje uváděj jen v nezbytném rozsahu.

## Hard Rules

- Paragraf známý → žádný broad search; paragrafy s písmeny přes `/toc`; změny → `/versions`.
- `docId` jen z API.
- Sazby, body, hladiny, limity plnění a lhůty nikdy z paměti - vždy z aktuálního znění s odkazem a datem účinnosti.
- Mimo CODEXIS jen oficiální zdroje (policie.gov.cz, mdcr.cz, ckp.cz, cnb.cz, nssoud.cz) když CODEXIS neodpovídá; nikdy neradit, jak se vyhnout kontrole nebo zkreslit průběh nehody.
