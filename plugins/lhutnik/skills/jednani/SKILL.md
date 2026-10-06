---
name: "Lhůtník – záznam z jednání"
description: "Z poznámek po jednání soudu vytáhne lhůty všech stran a termín dalšího jednání, spočítá konce lhůt a po schválení je založí v Evoliu jako události a úkoly ke spisu."
whenToUse: "Uživatel se vrátil z jednání nebo poslal poznámky, usnesení či protokol a potřebuje ohlídat lhůty: záznam z jednání, byl jsem u soudu, po jednání, odročeno, zapiš lhůtu, lhůtník, procesní lhůta, kdy končí lhůta, spočítej lhůtu, výzva soudu s lhůtou."
---

# Lhůtník – záznam z jednání → hlídané lhůty v Evoliu

Účel: poznámka z jednací síně se **ve stejném úkonu** změní na termín s upomínkou ve spisu v Evoliu. Zapsat a zanést do lhůtníku jako dva oddělené kroky selhává na tom druhém — proto se to tady dělá naráz.

## Železná pravidla

1. **Nikdy nehádej lhůtu.** Nevíš-li jistě rozhodnou skutečnost (od čeho lhůta běží) nebo její délku, polož otázku nástrojem `ask_user`. Chybný termín v lhůtníku je horší než žádný — vypadá jako ohlídaný.
2. **Zachyť lhůty VŠECH stran** — naše, protistrany, soudu. Zmeškaná lhůta protistrany je procesní příležitost.
3. **Rozhodná skutečnost není vždy den jednání.** Bývá jí doručení, zveřejnění v rejstříku, právní moc. V pochybnosti se ptej.
4. **Každý výpočet ukaž s mezikroky** (rozhodná skutečnost → první den běhu → nominální konec → posun) a proveď ho **dvakrát nezávisle** (jednou po dnech/měsících dopředu, jednou kontrolou zpětně od výsledku). Při neshodě výsledek nepoužij a řekni to.
5. **Nic nezakládej bez schválení.** Před zápisem do Evolia předlož souhrn a vyžádej souhlas nástrojem `request_approval`.
6. Nic neodesílej soudu, klientovi ani protistraně.

## 1. Vstup

- Poznámky ze zadání, přiložený protokol, usnesení nebo výzva soudu (čti je `file_read`).
- Je-li připojen konektor Evolia, dohledej spis (`load_connector_instructions` pro `evolio_pripady`; jinak `database_agent` nad `evolioprod` jen ke čtení) — spisovou značku, soud a klienta přebírej ze spisu, ne z odhadu.
- Pro kontext případu projdi `search_workspace_memory` podle klienta nebo sp. zn.

## 2. Vytěž fakta

Sestav tabulku z toho, co v podkladech je. Co chybí, vypiš jako otázky — nedomýšlej:

| Pole | Pozn. |
|---|---|
| Klient / spis v Evoliu | |
| Sp. zn. / č. j. | přesně dle záhlaví |
| Soud, senát / samosoudce | |
| Datum jednání | |
| Co se stalo | přednesy, dokazování, uznané / sporné skutečnosti |
| **Lhůty** | pro každou: *kdo*, *co má udělat*, *délka*, *od jaké skutečnosti*, *procesní režim* |
| **Další jednání** | datum, čas, síň, adresa |
| Poučení | zejm. § 118a, § 118b odst. 1 o. s. ř. (koncentrace) |
| Úkoly pro nás | co sepsat, co doložit, koho oslovit |

## 3. Spočítej lhůty

**Nejdřív ověř pravidlo** v platném znění k rozhodnému dni nástrojem `laws__law_get_provision` (případně `laws__get_provision_timeline`): u civilního řízení § 57 o. s. ř., u jiného režimu jeho vlastní ustanovení (správní řád § 40, trestní řád § 60, daňový řád § 33, insolvenční zákon odkazuje na o. s. ř. přes § 7). U hmotněprávních lhůt (promlčení, prekluze dle o. z. §§ 605–608) platí jiná pravidla a **musí dojít včas** — ověř je zvlášť a výsledek označ jako hmotněprávní.

Postup podle § 57 o. s. ř. (po ověření znění):
- Do běhu se nezapočítává den, kdy došlo ke skutečnosti určující počátek; lhůta začíná běžet následujícím dnem.
- Lhůta v týdnech, měsících či letech končí dnem, který se pojmenováním nebo číslem shoduje se dnem, kdy nastala rozhodná skutečnost; takový den v měsíci není-li, končí posledním dnem měsíce.
- Připadne-li konec na sobotu, neděli nebo svátek, je posledním dnem nejblíže následující pracovní den.
- Lhůta je zachována, je-li posledního dne podání učiněno u soudu nebo odevzdáno orgánu, který má povinnost je doručit (pošta, datová schránka).

**Svátky a dny pracovního klidu ČR** (zákon č. 245/2000 Sb. — při pochybnosti ověř `laws__law_get_provision`):
pevné: 1. 1., 1. 5., 8. 5., 5. 7., 6. 7., 28. 9., 28. 10., 17. 11., 24. 12., 25. 12., 26. 12.;
pohyblivé:

| Rok | Velký pátek | Velikonoční pondělí |
|---|---|---|
| 2026 | 3. 4. | 6. 4. |
| 2027 | 26. 3. | 29. 3. |
| 2028 | 14. 4. | 17. 4. |
| 2029 | 30. 3. | 2. 4. |
| 2030 | 19. 4. | 22. 4. |
| 2031 | 11. 4. | 14. 4. |

Den v týdnu u výsledku vždy uveď slovem (např. „pondělí 2. 11. 2026“) — nesoulad data a dne v týdnu je signál chyby výpočtu.

## 4. Předlož souhrn ke schválení

Tabulka: kdo · co · rozhodná skutečnost · délka · výpočet · **poslední den (den v týdnu)** · upomínky · co se stane při nesplnění. U jednání datum, čas, síň, adresa. Pak `request_approval`.

## 5. Založ v Evoliu

Po schválení načti `load_connector_instructions` pro `evolio_udalosti` a `evolio_ukoly` a postupuj podle nich. Není-li konektor připojen (uživatel není přihlášen), **nic nezakládej jinam** — řekni, že je potřeba připojit konektor „evolio.cz“ v nastavení Coworku, a předej hotovou tabulku k ručnímu zápisu.

- **Lhůta** — celodenní událost na poslední den ke spisu; název `LHŮTA (my|protistrana|soud): <co> — <sp. zn.>`; popis: od čeho běží, výpočet, následek nesplnění, kde ověřit. Upomínky 7, 3 a 1 den předem (pokud konektor upomínky umí; jinak úkol s termínem o 3 pracovní dny dřív).
- **Jednání** — časovaná událost s místem (soud, adresa, síň), upomínky 7 a 1 den předem. Neznáš-li délku, počítej 90 minut a řekni to.
- **U lhůty protistrany** navíc úkol den po uplynutí: „ověřit ve spisu / ISIR, zda protistrana splnila“.
- **Úkoly pro nás** jako úkoly ke spisu s termínem nejpozději 2 pracovní dny před koncem lhůty.

## 6. Ulož záznam

Záznam z jednání ulož jako soubor (`file_write`, případně `export__export_document` do .docx) a klíčová fakta do paměti workspace (`save_memory`: sp. zn., další jednání, lhůty a jejich konce).

## 7. Uzavři

Shrň, co bylo založeno, a **výslovně vyjmenuj, co založeno nebylo a proč** (chybějící údaj, nejasná rozhodná skutečnost, nepřipojený konektor). Nedořešené údaje musí zůstat viditelné.

## Časté pasti

- **§ 118b odst. 1 poslední věta o. s. ř.**: byla-li dána výzva dle § 118a, smí soud přihlédnout i k později uvedeným skutečnostem. Zmeškání takové lhůty protistranou tedy není prekluze — argumentuj neunesením břemene tvrzení.
- Lhůta „ode dne zveřejnění v rejstříku“ (ISIR) běží od zveřejnění, ne od jednání ani doručení — datum zveřejnění ověř `isir__list_events`.
- Odročeno „na neurčito“ = žádná událost jednání, ale úkol kontroly za 3 měsíce.
- Vyhlásí-li soud rozhodnutí při jednání, lhůta k odvolání běží od **doručení písemného vyhotovení** — založ jen kontrolu očekávaného doručení.
- Soudcovská lhůta (určená soudem) může být prodloužena; zákonnou lhůtu soud prodloužit nemůže — v popisu rozliš.
- Doručení fikcí do datové schránky: 10. den po dodání, nepřihlásí-li se adresát dříve — rozhodnou skutečnost ověř z doručenky, ne z data odeslání.
