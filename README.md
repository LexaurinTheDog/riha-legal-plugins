<img src="icon.svg" width="56" alt="">

# riha-legal-plugins

Marketplace pluginů pro Claude Code zaměřených na českou advokátní praxi. Obsahuje **50 oborových právních skillů** a nástroj na hlídání lhůt.

## Instalace

```
/plugin marketplace add LexaurinTheDog/riha-legal-plugins
/plugin install lhutnik@riha-legal-plugins
/plugin install smluvni-pravo@riha-legal-plugins
```

Ikona pluginu je v jeho kořeni jako `icon.svg` a barva odpovídá oborové skupině; Claude Code pole `icon` ignoruje, používá ho katalog marketplace.

## Pluginy

### Oborové právní skilly (50)

Každý skill je samostatný pracovní postup pro jeden obor: ví, které předpisy otevřít, jakou judikaturu hledat, čím začít odpověď a kde se v oboru nejčastěji chybuje. Metodika práce s právní databází je zabudovaná uvnitř, obecný rešeršní skill se nenačítá.

Všech padesát má stejných sedm částí ve stejném pořadí — základní reflexy, operating assumptions, klíčové předpisy, rešeršní strategie, workflow, časté pasti, struktura odpovědi a hard rules. Napříč skilly platí pravidlo, že lhůty, sazby a prahové hodnoty se neuvádějí z paměti, ale ověřují v aktuálním znění; jinak zůstává placeholder `[DOPLNIT]`.

#### Civilní právo (11)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `dedicke-pravo` | Dědické právo | 89/2012 Sb., 292/2013 Sb., 91/2012 Sb. |
| `mezinarodni-pravo-soukrome` | Mezinárodní právo soukromé | 91/2012 Sb., 74/1959 Sb., 216/1994 Sb. |
| `nahrada-ujmy-odpovednost` | Náhrada újmy a odpovědnost | 89/2012 Sb., 262/2006 Sb., 276/2015 Sb. |
| `obcanske-procesni-pravo` | Občanské procesní právo | 99/1963 Sb., 292/2013 Sb., 549/1991 Sb. |
| `ochrana-osobnosti-gdpr` | Ochrana osobnosti a GDPR | 89/2012 Sb., 46/2000 Sb., 231/2001 Sb. |
| `opatrovnictvi-svepravnost` | Opatrovnictví a svéprávnost | 89/2012 Sb., 292/2013 Sb., 372/2011 Sb. |
| `rodinne-pravo` | Rodinné právo | 89/2012 Sb., 292/2013 Sb., 99/1963 Sb. |
| `rozhodci-rizeni-mediace` | Rozhodčí řízení a mediace | 216/1994 Sb., 74/1959 Sb., 176/1964 Sb. |
| `smluvni-pravo` | Smluvní právo | 89/2012 Sb., 90/2012 Sb., 634/1992 Sb. |
| `spotrebitelske-pravo` | Spotřebitelské právo | 89/2012 Sb., 634/1992 Sb., 257/2016 Sb. |
| `vecna-prava-sousedske-spory` | Věcná práva a sousedské spory | 89/2012 Sb., 256/2013 Sb., 357/2013 Sb. |

#### Nemovitosti a stavebnictví (4)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `bytove-pravo-najem-svj` | Bytové právo - nájem a SVJ | 89/2012 Sb., 366/2013 Sb., 67/2013 Sb. |
| `nemovitosti-transakce` | Nemovitosti a realitní transakce | 89/2012 Sb., 256/2013 Sb., 357/2013 Sb. |
| `stavebni-pravo` | Stavební právo | 283/2021 Sb., 183/2006 Sb., 500/2004 Sb. |
| `zemedelske-pravo` | Zemědělské právo | 89/2012 Sb., 252/1997 Sb., 334/1992 Sb. |

#### Obchod a korporace (10)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `dusevni-vlastnictvi` | Duševní vlastnictví | 121/2000 Sb., 89/2012 Sb., 441/2003 Sb. |
| `e-commerce-digitalni-sluzby` | E-commerce a digitální služby | 89/2012 Sb., 634/1992 Sb., 179/2024 Sb. |
| `franchising-distribuce-obchodni-zastoupeni` | Franchising, distribuce a obchodní zastoupení | 89/2012 Sb., 143/2001 Sb., 262/2017 Sb. |
| `fuze-akvizice` | Fúze a akvizice | 90/2012 Sb., 89/2012 Sb., 408/2010 Sb. |
| `hospodarska-a-nekala-soutez` | Hospodářská a nekalá soutěž | 143/2001 Sb., 262/2017 Sb., 395/2009 Sb. |
| `it-pravo-kyberbezpecnost` | IT právo a kyberbezpečnost | 264/2025 Sb., 181/2014 Sb., 121/2000 Sb. |
| `korporatni-pravo` | Korporátní právo | 90/2012 Sb., 89/2012 Sb., 304/2013 Sb. |
| `medialni-pravo-reklama` | Mediální právo a reklama | 46/2000 Sb., 231/2001 Sb., 132/2010 Sb. |
| `sportovni-pravo` | Sportovní právo | 115/2001 Sb., 89/2012 Sb., 435/2004 Sb. |
| `startupy-investice-esop` | Startupy, investice a ESOP | 90/2012 Sb., 33/2020 Sb., 89/2012 Sb. |

#### Finance a pohledávky (8)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `aml-compliance` | AML compliance | 253/2008 Sb., 37/2021 Sb., 69/2006 Sb. |
| `bankovnictvi-a-uvery` | Bankovnictví a úvěry | 257/2016 Sb., 89/2012 Sb., 370/2017 Sb. |
| `danove-pravo-hmotne` | Daňové právo hmotné | 586/1992 Sb., 235/2004 Sb., 280/2009 Sb. |
| `exekuce-obrana-dluznika` | Exekuce - obrana povinného | 120/2001 Sb., 99/1963 Sb., 595/2006 Sb. |
| `insolvencni-pravo` | Insolvenční právo | 182/2006 Sb., 312/2006 Sb., 99/1963 Sb. |
| `kapitalovy-trh-investice` | Kapitálový trh a investice | 256/2004 Sb., 240/2013 Sb., 190/2004 Sb. |
| `pojistne-pravo` | Pojistné právo | 89/2012 Sb., 37/2004 Sb., 30/2024 Sb. |
| `vymahani-pohledavek` | Vymáhání pohledávek | 89/2012 Sb., 351/2013 Sb., 99/1963 Sb. |

#### Trestní a správní trestání (4)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `trestni-pravo-hospodarske` | Hospodářské trestní právo | 40/2009 Sb., 418/2011 Sb., 141/1961 Sb. |
| `obeti-trestnych-cinu` | Oběti trestných činů a poškození | 45/2013 Sb., 141/1961 Sb., 89/2012 Sb. |
| `prestupkove-pravo-spravni-trestani` | Přestupkové právo a správní trestání | 250/2016 Sb., 520/2005 Sb., 251/2016 Sb. |
| `trestni-obhajoba` | Trestní právo a obhajoba | 141/1961 Sb., 40/2009 Sb., 418/2011 Sb. |

#### Veřejná správa a regulace (11)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `cizinecke-a-azylove-pravo` | Cizinecké a azylové právo | 326/1999 Sb., 325/1999 Sb., 221/2003 Sb. |
| `dopravni-pravo-nehody` | Dopravní právo a nehody | 361/2000 Sb., 250/2016 Sb., 168/1999 Sb. |
| `energeticke-pravo` | Energetické právo | 458/2000 Sb., 165/2012 Sb., 406/2000 Sb. |
| `obce-a-verejna-sprava` | Obce a veřejná správa | 128/2000 Sb., 131/2000 Sb., 250/2000 Sb. |
| `pravo-zivotniho-prostredi` | Právo životního prostředí | 100/2001 Sb., 76/2002 Sb., 148/2023 Sb. |
| `spolky-nadace-neziskovy-sektor` | Spolky, nadace a neziskový sektor | 89/2012 Sb., 304/2013 Sb., 90/2012 Sb. |
| `spravni-a-danove-rizeni` | Správní a daňové řízení | 500/2004 Sb., 280/2009 Sb., 150/2002 Sb. |
| `verejne-zakazky-dotace` | Veřejné zakázky a dotace | 134/2016 Sb., 340/2015 Sb., 218/2000 Sb. |
| `zdravotnicke-pravo` | Zdravotnické právo | 372/2011 Sb., 373/2011 Sb., 48/1997 Sb. |
| `ustavni-stiznost-lidska-prava` | Ústavní stížnost a lidská práva | 1/1993 Sb., 2/1993 Sb., 182/1993 Sb. |
| `skolske-pravo` | Školské právo | 561/2004 Sb., 563/2004 Sb., 75/2005 Sb. |

#### Práce a sociální zabezpečení (2)

| Plugin | Obor | Klíčové předpisy |
|---|---|---|
| `pracovni-pravo` | Pracovní právo | 262/2006 Sb., 89/2012 Sb., 435/2004 Sb. |
| `socialni-zabezpeceni` | Sociální zabezpečení | 155/1995 Sb., 582/1991 Sb., 187/2006 Sb. |

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
