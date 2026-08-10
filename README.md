# riha-legal-plugins

Marketplace pluginů pro Claude Code zaměřených na českou advokátní praxi.

## Instalace

```
/plugin marketplace add LexaurinTheDog/riha-legal-plugins
/plugin install lhutnik@riha-legal-plugins
```

## Pluginy

### `lhutnik` — lhůty a termíny z jednání

Řeší konkrétní selhání advokátní praxe: poznámka z jednací síně vznikne, ale nikdy se z ní nestane termín s budíkem. Skill `/jednani` proto **záchyt a převod na termín spojuje do jednoho úkonu** — každý postup, kde je „zapsat" a „zanést do lhůtníku" odděleně, selhává na tom druhém kroku.

Z volných poznámek po jednání vytáhne lhůty a termín dalšího jednání, spočítá konce lhůt, předloží souhrn ke schválení a založí události v kalendáři s upomínkami.

**Dvě věci, kterými se liší od běžného lhůtníku:**

- Hlídá lhůty **všech stran a soudu**, ne jen vlastní. Zmeškaná lhůta protistrany je procesní příležitost — u lhůty protistrany zakládá i kontrolu den po jejím uplynutí.
- **Nehádá.** Nevyplývá-li z poznámek jednoznačně rozhodná skutečnost nebo délka lhůty, zeptá se a raději nezaloží nic. Chybný termín v kalendáři je horší než žádný, protože vypadá jako ohlídaný.

#### Kalkulátor lhůt

Součástí je `lhuta.py`, použitelný i samostatně:

```bash
python3 skills/jednani/lhuta.py 2026-02-02 30d
python3 skills/jednani/lhuta.py 2026-10-18 30d --json
```

Implementuje **§ 57 o. s. ř.**: běh od následujícího dne po rozhodné skutečnosti; u lhůt podle týdnů, měsíců a let shoda označení dne (není-li takový den v měsíci, poslední den měsíce); připadne-li konec na sobotu, neděli nebo svátek, posun na nejblíže následující pracovní den. Svátky dle z. č. 245/2000 Sb. včetně pohyblivých Velikonoc (Meeusův algoritmus), takže výpočet nezastará.

```
$ python3 lhuta.py 2026-10-18 30d
Rozhodná skutečnost:  2026-10-18  (neděle)
Lhůta běží od:        2026-10-19  (pondělí)
POSLEDNÍ DEN LHŮTY:   2026-11-18  (středa)
  (posunuto z 2026-11-17 — svátek)
```

Podporuje `Nd` / `Nt` / `Nm` / `Nr` — dny, týdny, měsíce, roky.

#### Konfigurace

Prostředí-specifická nastavení jsou v tabulce „Konfigurace" na začátku `SKILL.md` — kalendář, časové pásmo, JID chatu se sebou pro záchyt z mobilu, kam ukládat záznam, intervaly upomínek. Tělo skillu je na nich nezávislé, takže nasazení jinam znamená upravit jen tuhle tabulku.

Výchozí zápis termínů používá [`gog`](https://github.com/steipete/gogcli) (Google Kalendář). Není-li k dispozici, skill se zeptá, kam termíny zapsat.

## Upozornění

Nástroj nenahrazuje kontrolu advokáta. Kalkulátor je stavěný na **procesní** lhůty dle § 57 o. s. ř.; hmotněprávní lhůty (promlčecí, prekluzivní dle o. z.) se počítají jinak a podání u nich musí dojít včas, ne jen být odesláno.

## Licence

Apache-2.0
