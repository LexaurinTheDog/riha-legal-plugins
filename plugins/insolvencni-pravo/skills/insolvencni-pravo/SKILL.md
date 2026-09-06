---
uuid: e0293478-596a-4d8c-aae7-0d2289aca509
name: insolvencni-pravo
version: 1.0.0
jurisdictions: [CZ]
i18n:
  cs:
    displayName: "Insolvenční právo ČR"
    summary: "Insolvenční řízení z pohledu věřitele, dlužníka i správce - přihlášky, přezkum a popření, incidenční spory, oddlužení, konkurs, moratorium, ISIR."
    examplePrompts:
      - "Klient má pohledávku za firmou, na kterou byl dnes prohlášen úpadek. Co musí udělat a do kdy?"
      - "Správce popřel naši pohledávku co do pravosti. Připrav postup a osnovu incidenční žaloby."
      - "Dlužník v oddlužení přestal platit splátky. Hrozí zrušení oddlužení a jak se bránit?"
  en:
    displayName: "Czech Insolvency Law"
    summary: "Czech insolvency proceedings from the creditor, debtor and trustee perspective - claims, review and denial, incidental disputes, debt relief, bankruptcy, moratorium, ISIR."
    examplePrompts:
      - "My client has a receivable against a company declared insolvent today. What must they do and by when?"
      - "The trustee denied our claim as to its existence. Prepare the procedure and outline of the incidental action."
      - "A debtor in debt relief stopped paying. Is cancellation of debt relief imminent and how to defend?"
  sk:
    displayName: "Insolvenčné právo ČR"
    summary: "České insolvenčné konanie z pohľadu veriteľa, dlžníka aj správcu - prihlášky, prieskum a popretie, incidenčné spory, oddlženie, konkurz, moratórium, ISIR."
    examplePrompts:
      - "Klient má pohľadávku voči firme, na ktorú bol dnes vyhlásený úpadok. Čo musí urobiť a dokedy?"
      - "Správca poprel našu pohľadávku čo do pravosti. Priprav postup a osnovu incidenčnej žaloby."
      - "Dlžník v oddlžení prestal platiť splátky. Hrozí zrušenie oddlženia a ako sa brániť?"
description: Use when the user's matter involves Czech insolvency proceedings in any role - creditor, debtor, insolvency trustee (insolvenční správce), secured creditor - or touches insolvenční zákon (182/2006 Sb.), zákon o insolvenčních správcích (312/2006 Sb.), ISIR, úpadek, insolvenční návrh, přihláška pohledávky, přezkumné jednání, popření pohledávky, incidenční spor, žaloba na určení pohledávky, vylučovací žaloba, odpůrčí žaloba, neúčinnost právního jednání, oddlužení, splátkový kalendář, zrušení oddlužení, nepoctivý záměr, konkurs, reorganizace, moratorium, preventivní restrukturalizace (284/2023 Sb.), majetková podstata, zajištěný věřitel, výtěžek zpeněžení, pohledávky za podstatou, schůze věřitelů, odměna správce (313/2007 Sb.), or when a debtor "is in insolvency", "went bankrupt", "filed for debt relief". Standalone skill - bundles CODEXIS methodology with insolvency-law reasoning; no need to load the general codexis skill.
---

# Insolvenční právo ČR

Samostatný oborový skill pro české insolvenční řízení. Metodika, ne katalog odpovědí: nejprve role a fáze řízení, pak lhůta, teprve potom hmotné právo.

## Operating Assumptions

- Pro všechny dotazy do CODEXIS používej `cdx-cli`. Předpokládej, že je nainstalovaný a přihlášený; nedělej preflight (`which`, bare `cdx-cli`).
- Kanonické tvary:
  - `cdx-cli search JD --query "..." --court "Nejvyšší soud" --limit 5`
  - `cdx-cli get cdx://cz_law/182/2006/versions`
  - `cdx-cli get 'cdx://doc/<versionId>/text?part=paragraf198'`
- Používej jen dokumentované subpříkazy `search`, `get`, `schema`. Preferuj flagy před JSON payloadem.
- Insolvenční zákon se novelizuje často a lhůty i číslování odstavců se měnily (zejména novely 2017, 2019, 2024). **Každé konkrétní číslo (lhůta, procento, odstavec) ověř v aktuálním znění přes `/versions` → `/toc` → `/text?part=`.** Nikdy z paměti.

## Klíčové předpisy

| Předpis | Číslo | CODEXIS base | K čemu |
|---|---|---|---|
| IZ - insolvenční zákon | 182/2006 Sb. | `cz_law/182/2006` | Celé řízení, přihlášky, přezkum, incidenční spory, způsoby řešení úpadku |
| ZIS - zákon o insolvenčních správcích | 312/2006 Sb. | `cz_law/312/2006` | Postavení, oprávnění a odpovědnost správce, ohlášený společník |
| o. s. ř. | 99/1963 Sb. | `cz_law/99/1963` | Subsidiárně (§ 7 IZ) - doručování, lhůty, dokazování, odvolání |
| Vyhláška o odměně IS | 313/2007 Sb. | `cz_law/313/2007` | Odměna a hotové výdaje správce, odměna ze zpeněžení zajištění |
| Jednací řád pro insolvenční řízení | 191/2017 Sb. | `cz_law/191/2017` | Formuláře, náležitosti podání, seznamy |
| Zákon o preventivní restrukturalizaci | 284/2023 Sb. | `cz_law/284/2023` | Alternativa k moratoriu a insolvenci pro podnikatele |
| OZ / ZOK | 89/2012 Sb. / 90/2012 Sb. | `cz_law/89/2012`, `cz_law/90/2012` | Titul pohledávky, zajištění, korporátní vazby, odpovědnost statutárů |
| Nařízení o insolvenčním řízení | (EU) 2015/848 | zdroj `EU` | Přeshraniční prvek, COMI, uznávání |

## Rešeršní strategie pro insolvenci

1. **Zákon první.** Znáš-li paragraf, jdi rovnou `cdx://cz_law/182/2006` → `/versions` → `/toc` → `/text?part=paragrafNNN`. Broad search až když nevíš, kde hledat.
2. **Judikatura:** `cdx-cli search JD --query "..." --court "Nejvyšší soud" --limit 5`. Insolvenční senát NS má spisové značky `NSČR` (např. `29 NSČR 45/2025`) - do query přidej „NSČR“ nebo „insolvenční“. Pro odvolací praxi filtruj `--court "Vrchní soud v Praze"` / `"Vrchní soud v Olomouci"` (značky `VSPH`, `VSOL`).
3. **Komentář** (`COMMENT`) použij pro výklad sporných pojmů (nepoctivý záměr, pohledávka za podstatou, zajištění), ne jako primární oporu.
4. **Vzory** (`VS`) pro přihlášku, incidenční žalobu, návrh na povolení oddlužení - vždy sladit s aktuálním formulářem.
5. Pro stav konkrétního řízení odkazuj na ISIR (`isir.justice.cz`) - CODEXIS neobsahuje spisy. Údaje o dlužníku (IČO, sídlo) ověř v ARES / obchodním rejstříku, nikdy je nedoplňuj z paměti.

## Workflow insolvenčního praktika

1. **Role.** Zjisti, za koho uživatel jedná: nezajištěný věřitel / zajištěný věřitel / dlužník / insolvenční správce / statutární orgán dlužníka / nabyvatel majetku. Stejná otázka má pro každou roli jinou odpověď a jinou lhůtu.
2. **Fáze řízení.** Před rozhodnutím o úpadku (§ 97-§ 133 IZ) × po rozhodnutí o úpadku (§ 136 IZ) × po rozhodnutí o způsobu řešení (konkurs § 244+, reorganizace § 316+, oddlužení § 389+) × po skončení. Fáze určuje, co lze ještě udělat.
3. **Lhůta dřív než merit.** Insolvenční lhůty jsou zpravidla propadné a **zmeškání nelze prominout (§ 83 IZ)**. Nejprve urči, která lhůta běží, od kterého okamžiku (zveřejnění v ISIR × zvláštní doručení) a kdy končí. Teprve pak řeš obsah.
4. **Účinky zahájení a úpadku.** Zkontroluj, co už nastalo: § 109 IZ (účinky zahájení - zákaz exekuce, omezení uplatňování pohledávek), § 111 IZ (omezení dlužníka v nakládání), § 140-§ 140e IZ (přerušení a zákaz zahájení jiných řízení), § 246 IZ (přechod dispozičních oprávnění na správce v konkursu).
5. **Klasifikace pohledávky.** Přihlašovaná (§ 173 IZ) × za majetkovou podstatou (§ 168 IZ) × postavená na roveň (§ 169 IZ) × nepřihlašovaná / vyloučená (§ 170 IZ). Zajištěná × nezajištěná; vykonatelná × nevykonatelná; podmíněná; v cizí měně. Klasifikace určuje, zda se přihlašuje, jak se uplatňuje (§ 203 IZ) a jak se uspokojuje.
6. **Titul a důkazy.** Ověř skutečný právní důvod pohledávky a listiny. Přihláška má účinky žaloby (§ 173 odst. 4 IZ) - vada v důvodu nebo výši se v incidenčním sporu obtížně zhojuje.
7. **Návrh řešení + rizika.** Vždy uveď alternativy (např. moratorium × preventivní restrukturalizace × insolvenční návrh; popření × uznání s výhradou; odvolání × žaloba) a co každá z nich znamená pro lhůty a náklady.

## Typické úkoly a recepty

**Přihláška pohledávky (§ 173-§ 177 IZ):** pouze na předepsaném formuláři (§ 176 IZ); lhůta stanovená v rozhodnutí o úpadku (§ 136 IZ - ověř aktuální délku), počítaná od zveřejnění v ISIR, nikoli od doručení věřiteli; k opožděné přihlášce se nepřihlíží (§ 173 odst. 1 IZ). Výše ke dni rozhodnutí o úpadku, příslušenství zvlášť, zajištění uplatnit výslovně (§ 174 IZ) - neuplatněné zajištění se ztrácí. Sankce za přihlášení nadsazené pohledávky § 178-§ 179 IZ - ověř aktuální podobu. Výzva k opravě vad § 188 IZ.

**Přezkum a popření (§ 190-§ 202, § 410 IZ):** správce popírá pravost, výši nebo pořadí (§ 193-§ 195 IZ); popření věřitelem § 200 IZ (písemně na formuláři, lhůta a jistota - ověř). V oddlužení probíhá přezkum bez jednání u správce (§ 410 IZ). Dlužníkovo popření má v konkursu jen omezené účinky (§ 192 odst. 3 IZ).

**Incidenční spor o pravost/výši/pořadí (§ 159, § 198-§ 199 IZ):** nevykonatelná popřená pohledávka - žalobu podává **věřitel** ve lhůtě dle § 198 odst. 1 IZ (běží od přezkumného jednání, s minimální dobou od doručení vyrozumění § 197 odst. 2 IZ); nepodá-li, k pohledávce se nepřihlíží. Vykonatelná pohledávka - žalobu podává **popírající** (§ 199 IZ) a důvodem popření nemohou být skutečnosti, které dlužník neuplatnil v nalézacím řízení, ani pouhé jiné právní posouzení (§ 199 odst. 2 a 3 IZ). Petit směřuje na určení, žalovaným je ten, kdo popřel.

**Vylučovací žaloba (§ 225 IZ):** vlastník věci sepsané do podstaty podává žalobu proti správci ve lhůtě od doručení vyrozumění o soupisu (§ 224 IZ); po marném uplynutí platí, že věc je do soupisu pojata oprávněně. Do rozhodnutí nelze věc zpeněžit (§ 225 odst. 4 IZ - výjimky ověř).

**Odporovatelnost (§ 235-§ 243 IZ):** aktivně legitimován je jen správce (§ 239 IZ), lhůta od účinnosti rozhodnutí o úpadku, tři skutkové podstaty: bez přiměřeného protiplnění (§ 240), zvýhodňující (§ 241), úmyslně zkracující (§ 242) - každá má vlastní časový test.

**Oddlužení (§ 389-§ 418 IZ):** návrh jen na formuláři a přes advokáta / oprávněnou osobu (§ 390a IZ); nepoctivý záměr § 395 IZ; povinnosti dlužníka § 412 IZ; zrušení § 418 IZ - odstavce byly přečíslovány novelou, cituj podle aktuálního znění. Při dotazu na zrušení pro nepoctivý záměr rozliš nová zjištění od pouhého výkonu práva dlužníkem.

**Zajištěný věřitel v konkursu:** pokyny ke správě a zpeněžení (§ 230, § 293 IZ), vydání výtěžku (§ 298 IZ) po odečtení nákladů v zákonných limitech a odměny správce dle vyhl. 313/2007 Sb. V oddlužení se zajištěný majetek zpeněžuje jen na žádost zajištěného věřitele (§ 409 IZ) - bez žádosti nelze, ani při vysoké hodnotě.

**Moratorium (§ 115-§ 127 IZ):** návrh vyžaduje souhlas věřitelské většiny a seznamy dle § 104 IZ; přílohy jsou posuzovány striktně a výzva k odstranění vad se nepoužije (§ 117 IZ) - jediný pokus. Moratorium neposouvá splatnost ani nebrání zesplatnění úvěru. Pro podnikatele porovnej s preventivní restrukturalizací (284/2023 Sb.).

**Opravné prostředky:** odvolání 15 dnů (§ 204 o. s. ř. přes § 7 IZ); proti rozhodnutím při výkonu dohlédací činnosti odvolání není (§ 91 IZ); dovolání k NS řeší insolvenční senát 29 NSČR. Doručení „zvlášť“ (§ 75 IZ) × doručení vyhláškou (§ 71 IZ) - od kterého se počítá lhůta, ověř u každého rozhodnutí.

## Lhůty - kontrolní seznam

Ke každé lhůtě uveď: **předpis + odstavec, od kdy běží, zda je propadná, zda ji lze prominout (v insolvenci zpravidla NE - § 83 IZ)**. Konkrétní délku vždy ověř v aktuálním znění:

- přihláška pohledávky - od zveřejnění rozhodnutí o úpadku (§ 136 IZ)
- oprava vad přihlášky - od doručení výzvy (§ 188 IZ)
- žaloba věřitele na určení popřené pohledávky (§ 198 IZ)
- žaloba popírajícího u vykonatelné pohledávky (§ 199 IZ)
- vylučovací žaloba - od doručení vyrozumění o soupisu (§ 225 IZ)
- odpůrčí žaloba správce (§ 239 IZ)
- odvolání proti usnesení (§ 204 o. s. ř.)
- námitky / stížnosti na správce a schůze věřitelů (§ 29, § 47-§ 53 IZ)

## Časté pasti

- Počítání lhůty pro přihlášku od doručení věřiteli místo od zveřejnění v ISIR.
- Přihlášení nezajištěné pohledávky, ač existuje zajištění - zajištění se pak neuplatní.
- Spolehnutí na prominutí zmeškání lhůty (§ 83 IZ ho vylučuje).
- Popření vykonatelné pohledávky z důvodů, které dlužník mohl uplatnit dříve (§ 199 odst. 2 IZ).
- Záměna pohledávky za podstatou (§ 168) s přihlašovanou pohledávkou - uplatňuje se u správce (§ 203), ne přihláškou.
- Citování zrušeného rozhodnutí: odvolací soud často zruší usnesení o úpadku a následuje nové s vyšším číslem (A-NN) - vždy ověř, které je v platnosti.
- Použití číslování odstavců § 418 nebo § 136 IZ ze starého znění.
- Zastupování dlužníka i jeho věřitele (nebo manžela) v téže insolvenci - střet zájmů, substituce ho nezhojí.
- Tvrzení o délce lhůt, procentech uspokojení, výši odměny správce z paměti - vždy ověř.
- Hádání názvu, IČO nebo spisové značky dlužníka; neověřené údaje označ `[DOPLNIT]`.

## Struktura odpovědi

1. **Závěr a nejbližší lhůta** v první větě (co udělat a do kdy).
2. **Role a fáze řízení**, ze kterých závěr vychází.
3. **Právní rámec** - paragrafy IZ v aktuálním znění, subsidiárně o. s. ř.
4. **Postup krok za krokem** včetně formulářů, adresáta (soud × správce) a způsobu podání.
5. **Rizika a alternativy** (co se stane při zmeškání, jiné cesty).
6. **Judikatura** - jen ověřená v CODEXIS, s kompaktní citací.
7. **Otevřené otázky a předpoklady** (datum znění zákona, chybějící skutkové údaje).

## Pravidla výstupu

- Odkazy pro uživatele MUSÍ používat resolvovanou `https://` URL ze source bloku tool outputu (`【src_xxx】 url: https://…`). Schéma `cdx://` je jen adresace pro `cdx-cli get` - nikdy do výstupu. Nevystavuj raw ID ani API suffixy (`/text`, `/meta`, `/toc`).
- Paragraf je sám klikací referencí: `[§ 198 odst. 1 IZ](https://…#paragraf198)`.
- Citace rozhodnutí ve tvaru `SOUD - Č. J. / SP. ZN. - DD.MM.RRRR` (např. `NS - 29 NSČR 45/2025 - 12.03.2026`, `VS Praha - 4 VSPH 1683/2025 - …`) sestavená z metadat; obecný titulek jen jako doplňkový text.
- Spisovou značku ani číslo jednací nikdy nevymýšlej ani nedoplňuj podle vzoru - pokud CODEXIS rozhodnutí nenajde, řekni to.
- Při parafrázi zákona zachovej operativní kvalifikátory („nejpozději“, „do“, „ode dne zveřejnění“, „k okamžiku“) - jejich vypuštění mění význam.
- Všechny citované paragrafy resolvuj v jednom časovém řezu (stejná verze IZ k datu dotazu).

## Hard Rules

- Znáš-li paragraf, nezačínej broad searchem.
- Pro změny zákona začni `/versions`, ne `/text`.
- Pro konkrétní paragraf: `/toc` → `elementId` (např. `paragraf198`) → `/text?part=<elementId>`; při selhání `/toc` fallback na `/text` celého zákona.
- Nehádej `docId` - vždy z API response.
- Nepoužívej web, když CODEXIS odpovídá; mimo CODEXIS jen oficiální zdroje (ISIR, justice.cz, ARES).
