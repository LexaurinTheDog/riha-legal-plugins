---
name: jednani
description: Záznam z jednání soudu → hlídané lhůty v kalendáři. Z volných poznámek po jednání vytáhne lhůty všech stran a termín dalšího jednání, spočítá konce lhůt dle § 57 o. s. ř. a založí události s upomínkami. Triggers: /jednani, záznam z jednání, byl jsem u soudu, po jednání, zapiš lhůtu, odročeno, lhůtník, procesní lhůta.
---

# Záznam z jednání → hlídané lhůty

Účel: aby se poznámka z jednací síně **ve stejném úkonu** změnila na termín s budíkem. Dva oddělené kroky („zapsat" a „zanést do lhůtníku") selhávají na tom druhém — proto se tady dělají naráz.

Skill je soběstačný: kalkulátor lhůt leží vedle tohoto souboru (`lhuta.py`).

## Konfigurace

Výchozí hodnoty pro toto prostředí. Při nasazení jinde uprav jen tuhle sekci — zbytek skillu je na ní nezávislý.

| Klíč | Hodnota |
|---|---|
| Kalendář (zdroj pravdy pro lhůty) | `gog calendar create primary` |
| Časové pásmo | `Europe/Prague` |
| Záchyt z mobilu | chat se sebou (WhatsApp/Signal), JID `<tvoje-cislo>@s.whatsapp.net` — vyplň |
| Kam ukládat záznam | do složky kauzy; neznáš-li ji, zeptej se |
| Upomínky u lhůty | `popup:7d`, `popup:3d`, `popup:1d` |
| Upomínky u jednání | `popup:7d`, `popup:1d` |

Není-li k dispozici `gog`, zeptej se, kam termíny zapsat — **nikdy je nezakládej „naslepo" jinam**, než co uživatel potvrdí.

## ŽELEZNÁ PRAVIDLA

1. **Nikdy nehádat lhůtu.** Nevíš-li jistě rozhodnou skutečnost (od čeho lhůta běží) nebo její délku, ZEPTEJ SE. Chybný termín v kalendáři je horší než žádný — vypadá jako ohlídaný.
2. **Zachytit lhůty VŠECH stran**, ne jen klientovy: moje / protistrany / soudu. Zmeškaná lhůta protistrany je procesní příležitost, ne cizí starost.
3. **Konce lhůt počítat výhradně skriptem**, nikdy zpaměti ani odhadem.
4. **Rozhodná skutečnost není vždy den jednání.** Bývá i doručení, zveřejnění v rejstříku, právní moc. Rozliš to a v pochybnosti se ptej.
5. Před založením událostí předlož **souhrn ke schválení**. Teprve po potvrzení zakládej.

## Postup

### 1. Získej vstup

- **Z terminálu:** poznámky jsou v argumentu skillu, jinak o ně požádej.
- **Z mobilu** (řekne-li uživatel „poslal jsem si to", „z whatsappu"): načti poslední zprávy z chatu se sebou dle konfigurace, vyber ty od posledního jednání a nech uživatele potvrdit, které patří k věci.

### 2. Vytěž fakta

Sestav tabulku z toho, co v poznámkách je. Co chybí, **vypiš jako otázky** — nedomýšlej:

| Pole | Pozn. |
|---|---|
| Klient / spis | |
| Sp. zn. / č. j. | přesně dle záhlaví |
| Soud, senát/samosoudce | |
| Datum jednání | |
| Co se stalo | přednesy, dokazování, uznané/sporné skutečnosti |
| **Lhůty** | pro každou: *kdo*, *co má udělat*, *délka*, *od jaké skutečnosti* |
| **Další jednání** | datum, čas, síň, adresa |
| Poučení | zejm. § 118a, § 118b odst. 1 (koncentrace) |
| Úkoly pro mě | co sepsat, co doložit, koho oslovit |

### 3. Spočítej lhůty

Pro každou lhůtu zavolej kalkulátor a použij `posledni_den`:

```bash
python3 "$SKILL_DIR/lhuta.py" 2026-02-02 30d --json
```

Podporuje `Nd` / `Nt` / `Nm` / `Nr` (dny, týdny, měsíce, roky). Implementuje § 57 o. s. ř.: běh od následujícího dne po rozhodné skutečnosti; u týdnů/měsíců/let shoda označení dne (není-li takový den, poslední den měsíce); posun z víkendu a svátku na nejblíže následující pracovní den. Svátky včetně pohyblivých Velikonoc.

### 4. Předlož souhrn ke schválení

Vypiš, co se založí — každou lhůtu s posledním dnem a upomínkami, jednání s časem a síní. Vyžádej potvrzení.

### 5. Založ události

Vždy s časovým pásmem z konfigurace a vždy s private properties (podle nich lze později stavět kontrolní přejezd):
`lhutnik=1`, `typ=lhuta|jednani|kontrola`, `kdo=my|protistrana|soud`, `spis="<sp. zn.>"`.

**Lhůta** — celodenní událost na poslední den:

```bash
gog calendar create primary \
  --summary "LHŮTA (protistrana): <co> — <sp. zn.>" \
  --from 2026-03-04 --to 2026-03-05 --all-day --timezone Europe/Prague \
  --description "<od čeho běží, co se stane při nesplnění, kde ověřit>" \
  --reminder popup:7d --reminder popup:3d --reminder popup:1d \
  --private-prop lhutnik=1 --private-prop typ=lhuta --private-prop kdo=protistrana \
  --private-prop spis="<sp. zn.>"
```

**Jednání** — časovaná událost:

```bash
gog calendar create primary \
  --summary "Jednání: <klient> — <sp. zn.>" \
  --from "2026-06-15T15:00:00+02:00" --to "2026-06-15T16:30:00+02:00" \
  --timezone Europe/Prague \
  --location "<soud, adresa, jednací síň>" \
  --reminder popup:7d --reminder popup:1d \
  --private-prop lhutnik=1 --private-prop typ=jednani --private-prop spis="<sp. zn.>"
```

U lhůty protistrany založ **navíc kontrolní událost** den po jejím uplynutí: „ověřit ve spisu/rejstříku, zda protistrana doplnila" (`--private-prop typ=kontrola`).

Neznáš-li délku jednání, počítej 90 minut a řekni to uživateli.

### 6. Ulož strukturovaný záznam

`Zaznam_z_jednani_YYYY-MM-DD.md` do složky kauzy, s frontmatter `spis`, `sp_zn`, `soud`, `datum`, `lhuty`, `dalsi_jednani`, `zalozeno_v_kalendari: true`.

### 7. Uzavři

Shrň, co bylo založeno, a **výslovně vyjmenuj, co jsi nezaložil a proč** (chybějící údaj, nejasná rozhodná skutečnost). Nedopověděné údaje musí zůstat viditelné, ne zmizet.

## Časté pasti

- **§ 118b odst. 1 poslední věta**: byla-li dána výzva dle § 118a, smí soud přihlédnout i k později uvedeným skutečnostem. Zmeškání takové lhůty protistranou tedy *není* prekluze — argumentovat neunesením břemene tvrzení, ne prekluzí.
- Lhůta „ode dne zveřejnění v rejstříku" běží od zveřejnění, ne od jednání ani od doručení.
- Odročeno „na neurčito" = žádná událost jednání, ale **založ kontrolu za 3 měsíce**, ať věc nezapadne.
- Vyhlásí-li soud rozhodnutí při jednání, běží lhůta k opravnému prostředku typicky od **doručení písemného vyhotovení** — v den jednání ji tedy ještě nelze uzavřít; založ kontrolu na očekávané doručení.
- Lhůty hmotněprávní (promlčecí, prekluzivní dle o. z.) se počítají jinak než procesní a **musí dojít včas**, ne jen být odeslány. Kalkulátor je stavěný na procesní lhůty dle § 57 o. s. ř. — u hmotněprávních jeho výsledek nepoužívej bez kontroly.
