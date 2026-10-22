# e-Sbírka – referenční popis REST rozhraní

Zdroje: funkční specifikace „Veřejné API systému e-Sbírka“ (MV ČR, v. 1.4, registr smluv), JS klient
portálu e-sbirka.gov.cz (build 8/2026) a ověřená volání (9/2026). Neoficiální, ale ověřené.

## Základní URL a autentizace

| Base | Autentizace | Poznámka |
|---|---|---|
| `https://api.e-sbirka.gov.cz` | hlavička **`esel-api-access-key: <klíč>`** (klíč přidělí MV ČR, odbor strategického rozvoje, na žádost datovou schránkou; podpora esel@spcss.cz) | bez hlavičky nebo s jiným názvem `401 {"chyby":[{"kod":"NEPLATNY_API_KLIC","popis":"Nezaslán API klíč."}]}`; CORS preflight název hlavičky jen opakuje, nelze z něj nic vyčíst |
| `https://e-sbirka.gov.cz/sbr-cache` | žádná | Varnish cache portálu, stejné cesty a data (používá ji sám portál) |
| `https://e-sbirka.gov.cz/sbr-externi` | žádná | necachovaná varianta téhož |

**Rozdíly mezi API s klíčem a cache (ověřeno 9/2026):** API s klíčem běží nad službou `esel-esbir-daver`, cache portálu nad
`esel-esbir-dasex`. Na API s klíčem **chybí** `…/obsah`, `…/obsah/{uzel}`, `…/rozdilove-fragmenty/{zneniCil}` a
`…/zneni-ke-srovnani` (generické Spring 404 `{"status":404,"error":"Not Found","path":"/esel-esbir-daver/…"}`)
a parametr `predmetneDatum` je ignorován (vrací aktuální znění) – datum patří do staleUrl. Funkční na obou:
detail, `historie`, `fragmenty`, `nabidka-ustanoveni`, `souvislosti`, `dalsi-informace`, `castky`, číselníky,
`POST /jednoducha-vyhledavani`.

Historické adresy `www.e-sbirka.cz/*` přesměrovávají (308) na `e-sbirka.gov.cz`.
Stránka `/api-dokumentace` na nové doméně vrací 404 (9/2026).

Chyby mají jednotný tvar `{"chyby":[{"kod":"…","popis":"…","datumCasChyby":"…"}]}`:
`NEPLATNY_API_KLIC`, `DOKUMENT_NENALEZEN`, `CHYBI_VSTUPNI_PARAMETR`, `CHYBNY_RETEZEC`, `OBECNA_CHYBA`.

## Identifikátory

- **staleUrl** `/{sbirka}/{rok}/{cislo}` = předpis (server přesměruje na aktuální znění);
  `/{sbirka}/{rok}/{cislo}/{RRRR-MM-DD}` = znění účinné k datu (server normalizuje na počátek znění);
  `/…/0000-00-00` = dokument bez účinnostních znění (nálezy ÚS, sdělení). Kotva na ustanovení: `#par_2079`, `#par_310-pism_c`.
- V cestě URL musí být staleUrl **celé URL-encodované** (`%2Fsb%2F2012%2F89%2F2026-01-01`).
- **ELI** `/eli/cz/sb/2012/89/2026-01-01/dokument/norma/cast_4/hlava_2/dil_1/oddil_2/pododdil_1/par_2079/odst_2`
  – hierarchie fragmentů; potomci ustanovení = fragmenty s ELI prefixem `…/par_2079/`.
- `sbirkaKod`: `sb` Sbírka zákonů, `sm` Sbírka mezinárodních smluv, `ul0/ul1/ul2` Úřední list, `vcs` Úř. věst. čsl.
- `dokumentBaseId` (číselné id předpisu) a `fragmentId` (číselné id fragmentu v konkrétním znění).

## Endpointy – dokument sbírky (`/dokumenty-sbirky/{staleUrl}…`, GET)

| Cesta | Parametry | Vrací |
|---|---|---|
| `/dokumenty-sbirky/{staleUrl}` | `predmetneDatum` (RRRR-MM-DD), `odkazId` | metadata znění: `staleUrl`, `eli`, `typZneni` (AKTUALNI/MINULE/BUDOUCI/VYHLASENE), `datumUcinnostiZneniOd/Do`, `novely[]`, `uplnaCitace`, `uplnaCitaceSNovelami`, `datumUcinnostiOd`, `datumZruseni`, `rusiciDokumentSbirky`, `cisloCastky`, `rokCastky`, `dokumentBaseId`, `kodDokumentuSbirky`, `nikdyNebylUcinny`, příznaky `zobrazit*` |
| `/dokumenty-sbirky/{staleUrl}/historie` | – | `historie[]` všech znění: `cisloZneni`, `typZneni`, `datumUcinnostiZneniOd/Do`, `staleUrl`, `novely[]`, `poznamky[]` |
| `/dokumenty-sbirky/{staleUrl}/zneni-ke-srovnani` | – | totéž jako historie, pro výběr srovnání (`vybraneZneni`) |
| `/dokumenty-sbirky/{staleUrl}/fragmenty` | `cisloStranky` (od 0, 1000 fragmentů/stránka), `fulltextJednoZeSlov`, `fulltextVsechnaSlova`, `fulltextUvedenaFraze`, `odkazId`, `predmetneDatum` | `seznam[]` fragmentů + `pocetStranek` (fulltext nefiltruje stránky, jen zvýrazňuje) |
| `/dokumenty-sbirky/{staleUrl}/obsah` | – | kořen systematiky: `polozkyObsahu[]` (`oznaceniUstanoveni`, `nazev`, `rozsah`, `fragmentId`, `id`, `maPotomky`) |
| `/dokumenty-sbirky/{staleUrl}/obsah/{nadrazenyUzelId}` | – | podřízené položky (hlavy, díly…) |
| `/dokumenty-sbirky/{staleUrl}/nabidka-ustanoveni` | `text` („§ 2079“, „§ 2079 odst. 2“, „čl. 5“), `maxPocet` | `fragmentyNabidky[]`: `identifikaceUstanoveni`, `nazev`, `fragmentId` |
| `/dokumenty-sbirky/{staleUrl}/rozdilove-fragmenty/{zneniCil}` | `fulltext*` | všechny fragmenty cílového znění; změněné mají `typRozdilu` (UPRAVA/VLOZENO/ZRUSENO) a v `xhtml` značky `<ins>`/`<del>` |
| `/dokumenty-sbirky/{staleUrl}/rozdilovy-obsah/{zneniCil}` | – | rozdílová systematika |
| `/dokumenty-sbirky/{staleUrl}/souvislosti` | – | `souvislosti[]` po typech (viz TypSouvislosti) s `dokumentySbirky[]` |
| `/dokumenty-sbirky/{staleUrl}/dalsi-informace` | – | `dalsiNazvy` (zkratky NOZ, OZ…), `datumSchvaleni`, `podtypAktuKod`, věcný rejstřík (CzechVoc) |
| `/dokumenty-sbirky/{staleUrl}/id` | – | číselné id dokumentu |
| `/dokumenty-sbirky/{staleUrl}/odkazy-ke-stazeni` | – | PDF/DOCX ke stažení (znění) |
| `/dokumenty-sbirky/{staleUrl}/odkazy-ke-stazeni-porovnani` | `srovnavaneStaleUrl` | PDF srovnání znění |
| `/dokumenty-sbirky/{staleUrl}/fragmenty/{fragmentId}/novelizace-a-derogace` | – | novelizační body a derogace k fragmentu |
| `/dokumenty-sbirky/{staleUrl}/fragmenty/{fragmentId}/konsolidacni-konflikty` | – | konflikty konsolidace |
| `/dokumenty-sbirky/{staleUrl}/fragmenty/{fragmentId}/ostatni-kontextove-informace` | – | asociační vazby, prováděcí předpisy k fragmentu |
| `/dokumenty-sbirky/{staleUrl}/fragmenty/{fragmentId}/rpp` | – | registr práv a povinností |
| `/dokumenty-sbirky/{staleUrl}/duvodove-zpravy`, `…/duvodova-zprava/fragmenty`, `…/duvodova-zprava/obsah` | – / `cisloStranky` | důvodové zprávy (jsou-li) |
| `/dokumenty-sbirky/{staleUrl}/citizen-summary`, `…/citizen-summary/fragmenty` | – | stručný popis pro veřejnost (je-li) |
| `/dokumenty-sbirky/{staleUrl}/souvisejici-dokumenty/{id}/fragmenty` | `cisloStranky` | text souvisejícího dokumentu |

### Fragment

`id`, `eli`, `staleUrl` (s kotvou), `kodTypuFragmentu`, `hloubka`, `xhtml` (text s `<var>` označením a `<czechvoc-termin>`),
`zkracenaCitace` („§ 2079 odst. 2 zákona č. 89/2012 Sb.“), `uplnaCitace`, `odkazyZFragmentu[]`, `jeUcinny`,
příznaky `maNovelizace`, `maDerogace`, `maNalezyUS`, `maVykladovaStanoviska`, `maKonsolidacniKonflikty`, `maUpozorneni`,
`maRegistrPravAPovinnosti`, `maAsociacniVazby`, `maDefiniceKonceptu`, `maVerejnopravniPovinnosti`.

Typy fragmentů (`kodTypuFragmentu`, úplný číselník `GET /typy-fragmentu`): `Virtual_Document`, `Virtual_Prefix`, `Prefix_Number`,
`Prefix_Type`, `Prefix_Date`, `Prefix_Title`, `Prefix`, `Virtual_Norma`, `Cast`, `Hlava`, `Dil`, `Oddil`, `Pododdil`,
`Nadpis_nad` (nadpis nad §), `Paragraf`, `Nadpis_pod` (nadpis pod §), `Odstavec_Dc`, `Pismeno_Lb`, `Bod_*`,
`Pokracovani_Text`, `Priloha*`, `Block_*`.

## Vyhledávání a rejstříky

| Metoda a cesta | Tělo / parametry | Vrací |
|---|---|---|
| `POST /jednoducha-vyhledavani` | `{"fulltext":"…","start":0,"pocet":10,"razeni":[…]}` (alternativně `czechVocPreferovanyTerminTextNazvu`) | `pocetCelkem`, `seznam[]` (`staleUrl`, `nazev`, `kodDokumentuSbirky`, `stavDokumentuSbirky`, `datum`) |
| `POST /jednoducha-vyhledavani/zneni` | `{"dokumentSbirkyStaleUrl":"/sb/2012/89","fullText":"…"}` | znění a související dokumenty předpisu odpovídající dotazu |
| `POST /rozsirena-vyhledavani/pravni-akt-esbirka` | `fulltextVsechnaSlova`, `fulltextUvedenaFraze`, `fulltextJednoZeSlov`, `fulltextNeobsahujeSlova`, `rozsahVyhledavani`, `kodyTypAktu[]`, `kodyPodtypAktu[]`, `predmetneDatumOd/Do`, `dalsiPodminky[]`, `podminkySouvislosti[]`, `kontextVyhledavani` (povinné), `start`, `pocet` | seznam předpisů |
| `POST /rozsirena-vyhledavani/zneni` | obdobně + `dokumentSbirkyStaleUrl` | znění |
| `GET /jednoducha-vyhledavani/pravni-akt-esbirka-naseptavac/{kontextVyhledavani}` | `text`, `maxPocet`, `podtypPravniAktNavrhuKod` | našeptávač |
| `GET /rejstriky/{typRejstriku}` | `razeni[]`, `start`, `pocet` | rejstříky: chronologický, `UCINNE_PRAVNI_AKTY`, aktuálně vyhlášené / zrušené |
| `GET /castky/{kodSbirky}/{rok}/{cislo}` | – | metadata částky + `pravneZavazneZneni` (PDF `dokumentId` → `https://e-sbirka.gov.cz/sbr-externi/stahni/overena-zneni/{dokumentId}`) |
| `GET /castky/{kodSbirky}/{rok}/{cislo}/opravy` | – | redakční opravy |
| `GET /sbirky`, `/sady-dokumentu`, `/typy-aktu`, `/podtypyaktu`, `/typy-dokumentu`, `/typy-fragmentu` | – | číselníky |
| `GET /koncepty/schema-konceptu/{kod}/seznam`, `POST …/vyhledavani`, `GET /koncepty/{id}/detail` | – | věcný rejstřík CzechVoc (`VECNYREJ`) |

Stránkování všude `start` (offset) + `pocet`; fragmenty výjimečně `cisloStranky` s pevnou velikostí 1000.

## Číselníky (enumy)

- `typZneni`: `AKTUALNI`, `MINULE`, `BUDOUCI`, `VYHLASENE`.
- `stavDokumentuSbirky`: `AKTUALNE_PLATNY`, `ZRUSENY`, `VYHLASENY_BEZ_UCINNOSTI`, `VYHLASENY_BUDOUCI`, `NEPLATNY`.
- `RozsahVyhledavani`: `AKTUALNI_ZNENI`, `VSECHNA_ZNENI`, `NOVELY`, `VYHLASENE_ZNENI`, `BEZ_NOVEL`, `PLATNE`, `POUZE_CR`, `POUZE_UCINNE`.
- `TypSouvislosti` (pořadí v odpovědi): `MENI`, `JE_MENEN`, `RUSI`, `JE_RUSEN`, `ODKAZUJE`, `JE_ODKAZOVAN`, `PROVADI`, `JE_PROVADEN`,
  `NALEZY_US` (`NALEZY_US_ROZHODOVAN` / `NALEZY_US_ROZHODUJE`), `VYHLASENA_UPLNA_ZNENI`, `USNESENI_PS`, `USNESENI_PS_OPATRENI_SENATU`,
  `REDAKCNI_OPRAVY`, `DEFINICE_DATUMOVE_UCINNOSTI`, `NOVELA_NIKDY_NEPLATILA`, `IMPLEMENTOVANE_EU`, `OSTATNI`.
- `typRozdilu` (srovnání znění): `UPRAVA`, `VLOZENO`, `ZRUSENO`.
- `typAktuKod`: `PRAVPRED` (právní předpis) …; `podtypAktuKod`: `ZAKON`, `NARVLADY`, `VYHLASKA`, `NALEZUS`, `SDELENI` … (`GET /podtypyaktu`).

## Další služby portálu (bez klíče)

- `https://e-sbirka.gov.cz/leg-externi/legislativni-procesy/dokument/{dokumentBaseId}/ma-legislativni-procesy` – běžící legislativní proces (e-Legislativa).
- `https://e-sbirka.gov.cz/souborove-sluzby/soubory/{dokumentId}` – stažení souboru; `…/verejne-pozadavky-dokumenty/pozadavky/{pozadavekId}` – stav asynchronního generování.
- Open data (ELI dumpy): `https://opendata.eselpoint.gov.cz/esel-esb/{eli}`.
