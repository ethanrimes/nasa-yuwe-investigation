# Nasa Yuwe (Páez) Materials — Inventory

All resources gathered for training a Spanish ↔ Nasa Yuwe machine translation model.
ISO 639-3 code: `pbb`. Approx. 60,000–100,000 speakers in Cauca, Colombia.

## Parallel Spanish ↔ Nasa Yuwe data (ready for MT training)

| File | Pairs | Source | Notes |
| --- | ---: | --- | --- |
| `bible/parallel_nt_es_pbb.csv` | 7,906 | New Testament, aligned by (book, chapter, verse) | **Highest value.** Largest single parallel corpus in this collection. See "Caveats" below. |
| `dictionaries/living_dictionaries_paez.csv` | 3,950 | Living Dictionaries (Páez), sourced from Gerdel & Slocum 1983 | Lexeme → Spanish gloss, with POS tags |
| `metadata/talking_dictionary_entries_full.csv` | 3,912 | Swarthmore Talking Dictionary (Páez deposit, 2012) | Same Gerdel/Slocum lineage, slightly different rendering |
| `datasets/nasa_full_dataset*.csv` | (pre-existing) | Robles et al. 2024 paper data | The paper's consolidated train/dev/test |

After dedup the bible + dictionaries alone provide **~11,800 unique Spanish↔Nasa Yuwe pairs**, roughly 3× what the published paper had for Nasa Yuwe.

## Bible (`bible/`)

Two complete-NT downloads aligned by verse numbering:

- `pbb_html/` — Páez NT, Wycliffe Bible Translators 1984, HTML chapter-per-file (323 files)
- `pbb.epub`, `pbb_readaloud.zip`, `pbb2011eb_sword.zip` — same NT in ePub, plain-read, and CrossWire Sword formats
- `spavbl_html/` — *Versión Biblia Libre* (Spanish, 2018+), HTML chapter-per-file (1,268 files; whole Bible)
- `spavbl.epub`, `spavbl_sword.zip` — same in ePub / Sword
- `build_parallel_nt.py` — script that produced `parallel_nt_es_pbb.csv`

### Caveat about the Spanish source
The Spanish in `parallel_nt_es_pbb.csv` is **not** the source text the Nasa Yuwe translators used. It is a separate Spanish translation aligned by shared verse numbers — the standard approach for low-resource Bible MT (it is also what the paper does for Wayuunaiki via YouVersion). Both translations render the same Greek/Hebrew canon, so per-verse meaning matches even though the word choices are independent.

If you want a closer stylistic match to SIL's Wycliffe Nasa Yuwe, consider re-aligning against the Spanish NTV or NVI (those are SIL/Biblica-adjacent). Multiple Spanish parallels can also be combined as data augmentation.

## Bilingual MinEducación books — Territorios Narrados (`territorios_narrados/`)

Series #4, #6, #9, #10 from Colombia's *Plan Nacional de Lectura, Escritura y Oralidad*. Professionally edited bilingual Nasa Yuwe ↔ Spanish children's literature. PDFs only — text extraction will require OCR/parsing.

| File | Title |
| --- | --- |
| `04-Ipx_kwet_pekuj-AlrededorTulpa.pdf` | Ipx Kwet Peku'j — Alrededor de la tulpa |
| `06-Nasa_Ujunxin_Thegnxi-LeyendoVidaNasa.pdf` | Nasa U'junxin Thegnxi — Leyendo la vida Nasa |
| `09-Luucx_Pekuhn_Ujusaa-Chivito.pdf` | Luucx pekuhn u'jusaa — Chivito, el niño viajero |
| `10-Lxan_Nasa_Pal-AlvaroMojana.pdf` | Lxan Nasa Pal kũbxyac — Álvaro Nasa Pal y la Mojana |

## PDFs (`pdfs/`)

40 files / 53 MB. Mix of pre-existing pulls and freshly fetched government, academic, and pedagogical materials.

Government / constitutional:
- `Constitucion_de_1991_Nasa_Yuwe_Uniandes.pdf` — Constitution in Nasa Yuwe (13.6 MB)
- `Texto_Institucional_Nasa_Castellano_Nasa_Yuwe_Procuraduria.pdf`
- `Caracterizacion_NASA_YUWE_Procuraduria.pdf`
- `TEXTO_LENGUA_NASAYUWE_Adres.pdf`

CRIC / UAIIN academic theses (PEBI program):
- `MARIA_LUCIA_MUSSE_debilitamiento_nasa.pdf`
- `LUIS_CAMAYO_Paksxaw_orientacion_pedagogica.pdf`
- `CRUZ_EDILMA_DIAZ_Estado_NasaYuwe_Sxisxukwe.pdf`

Linguistic/grammar references:
- `CDI_144_Diccionario_Nasa_Yuwe_UAIIN_CRIC.pdf`
- `Dic_Nasa_ling_fi.pdf`
- `Paez_CaroyCuervo.pdf`
- `Rojas_Ramos_Localizacion_NasaYuwe.pdf`
- `Pitto_Transmision_idioma_nasa.pdf`
- `Colantropos_pueblo_nasa_escritura.pdf`
- `Nasa_Yat_redalyc.pdf`
- `Abanate_Kwesx_Knaynxi_Nasa_Yuwe_Armada.pdf`
- `Preview_Cultura_escrita_lengua_Nasa_Yuwe.pdf`
- `Preview_Gramatica_descriptiva_basica_Nasa_Yuwe.pdf`

Pedagogical (kwesxyuwe.com themed vocabulary PDFs, 17 files):
- `KwesxYuwe_*.pdf` — Animals, Body, Food, Numbers, Tools, Plants, etc.

Methodology papers:
- `AmericasNLP_2024_TranslationColombianIndigenous_paper.pdf` — the paper this work extends
- `Martinez_Sierra_Corpus_NasaYuwe_metaheuristic.pdf`
- `Interprete_contextual_expresiones_Nasa_Yuwe_Dialnet.pdf`
- `La_traduccion_contextual_constitucion_Nasa_Yuwe_Ramos_Pacho.pdf`

## Dictionaries (`dictionaries/`)

- `living_dictionaries_paez.csv` — 3,950 consolidated entries (Nasa Yuwe → Spanish, with POS)
- `raw/supabase_paez/entries_*.json` — raw Supabase paginated dump (3,934 entries)
- `raw/supabase_paez/senses_*.json` — sense/gloss tables (9,934 senses)
- `raw/supabase_paez/audio.json` — audio file URLs
- `raw/swarthmore_*.html` — Swarthmore Talking Dictionary scrapes
- `raw/pueblos_paez.html`, `raw/blogspot_index.html` — other lexicon attempts
- `raw/living_*.html` — Living Dictionaries entry pages

## Wikimedia Incubator (`wikimedia_incubator/`)

The Nasa Yuwe Wikipedia incubator project has only 3 articles. Both HTML and raw wikitext saved. Low value for MT but included for completeness.

## JW.org (`jw_org/`)

100 publications in Nasa Yuwe discovered at https://wol.jw.org/pbb/wol/library/r345/lp-paz. Manifest at `raw/all_pubs.tsv`. PDFs were **not** successfully downloaded — JW.org wraps publication downloads behind an authenticated dropdown. To finish this, the scraper needs to follow each `/pbb/wol/publication/r345/lp-paz/<pub-code>` page, find its `data-jsonurl` for the "Other formats" menu, and grab the PDF link from that JSON. JW.org is a high-value target because every publication exists in Spanish too — the pub code is shared across languages, so once a PDF is found, swapping `/pbb/` → `/es/` (or following the `Otros idiomas` switcher) yields the Spanish equivalent.

## Other directories (pre-existing, untouched)

- `audio/talking_dictionary_all/` — 1,002 mp3 files from Swarthmore (~77 MB)
- `pages/` — HTML scrapes of the Talking Dictionary search results
- `metadata/` — pre-existing download manifests and Talking Dictionary CSVs

## Addendum — sources from the cross-check against the user-supplied resource guide

After comparing against `Nasa Yuwe Language Resources for Machine Translation.md`, these additional resources were fetched in a second pass:

### Added to `bible/scripture_earth/`
Scripture Earth (SIL) publishes the Nasa NT in **both orthographies** as direct PDFs:
- `00-WNTpbb-traditional.pdf` — Complete NT in traditional orthography (6.8 MB; this is the same translation as the eBible.org `pbb` dump but in a single PDF)
- `00-WNTpbbN-new_orth.pdf` — **Complete NT in NEW orthography (3.7 MB)** — a *separate* orthographic variant, first published 2014. Aligning this against either the eBible Spanish or against the traditional-orth PDF would give a second 7,900-verse parallel set with different surface forms (useful as both data augmentation and as a Spanish-free orthography-mapping signal).
- `pbb_Dyusna-selpisaawesh_OT_stories_1993.pdf` — **OT narrative stories (4.5 MB)** — a separate publication, not the canonical OT but covers Genesis–Kings narratives. *New parallel data beyond the NT.*
- `pbb_CREATION.pdf` — Standalone Creation account (1 MB)
- Per-book PDFs in both orthographies are also available at `https://www.scriptureearth.org/data/pbb/PDF/<NN>-<BOOK>pbb[N]-web.pdf` if needed.

### Added to `pdfs/`
- `cric_catalog/CRIC_UAIIN_PEBI_Catalogo_2024.pdf` (6.2 MB) — Full 2024 PEBI-CRIC bilingual-materials catalog. Use this to identify which physical Sa't Luuçx / Lecto-Escritura / Comunicación Comunitaria titles are worth requesting from CDI-UAIIN-CRIC in Popayán.
- `AmericasNLP_2025_findings.pdf` — Findings of the AmericasNLP 2025 shared task (Colombian languages including Nasa Yuwe were included for the first time).
- `Landaburu_traduccion_constitucion_7lenguas.pdf` — Landaburu's history of the 1991 Constitution translation into 7 indigenous languages, including Nasa Yuwe.
- `Putunkaa_Serruma_5etnias_ICBF.pdf` (7.7 MB) — The ICBF bilingual lullabies book. **Note: contrary to the user's guide, this volume covers Piapoco, Arhuaco, Kamëntsá, Uitoto, and Wayúu — *not* Nasa Yuwe.** Kept because it's referenced in the AmericasNLP paper as a related precedent.

### Checked but not actionable

- **`derechosenelterritorio.com` (Amazon Conservation Team / Constitutional Court)** — the user's guide claims this includes Nasa Yuwe among 26+ indigenous languages. **Verified false:** the site's actual language menu lists 30 indigenous + Afro-Colombian languages but **Nasa Yuwe is not among them.** Available languages on the site are: aaja-kurri, aingae, awapit, bari-ara, creole, damana, ebera-bedea, epera-pedee, ette-taara, gunadule, hitnu, inga, jiw-jame, kamentsa, koreguaje, maguta, murui-muinauaido, namtrik, narp, piapoco, polindara, quillasinga, sikuani, siona, tukano, uwa, wayuunaiki, woun-meu, yukpa. Nasa Yuwe may have been planned but is not in the published set as of this check.
- **AILLA** (https://ailla.utexas.org) — modern interface is a JavaScript SPA; needs browser automation (e.g., Playwright) or AILLA's OAI-PMH API to enumerate Nasa Yuwe holdings.
- **`UNIMINUTO` Firefox-Nasa paper** — the article-PDF URL returned only 2 KB (publisher landing page, not the full PDF). Worth retrying after a manual page-view to grab the real article link.
- **Mozilla Pontoon / Transvision** — no `pbb` locale appears in Mozilla's localization platforms; the UNIMINUTO project's localization files (if any survived) are not on Mozilla's servers.

## Addendum 2 — sources from the second resource guide (Computational Linguistic Resources)

### Added to `huggingface_broomva/` — **biggest find of either cross-check**

Carlos D. Escobar-Valbuena (HuggingFace: `Broomva`) published two **ML-ready Spanish-Páez parallel datasets** and several pretrained translation models. All are CC-licensed and downloadable directly.

| Dataset | Rows | Format |
| --- | ---: | --- |
| `translation_pbb_spa` train | 2,428 | parquet + CSV (`id`, `translation.pbb`, `translation.spa`) |
| `translation_pbb_spa` validation | 607 | same |
| `translation_pbb_spa` test | 759 | same |
| `instruct-spa-pbb` train | 7,483 | parquet (Llama-2 `[INST]…[/INST]` format, **includes Constitution articles**) |

Total **3,794 word/phrase-level pairs** plus 7,483 instruction-tuning rows that include long-form Constitution article text — partially overlapping with our dictionary data (Gerdel/Slocum lineage) but separately curated and instruction-formatted. The `instruct` rows contain the *full text* of Constitution articles 1–40 in both languages, which is **the cleanest sentence-aligned constitutional pair I've seen in this collection** (the Uniandes Constitution PDF needs OCR to extract; this is already plain text).

Also worth noting (not downloaded — these are models, not data):

- `Broomva/llama-2-7b-chat-instruct-translate-spa-pbb` — Llama-2 7B finetuned for Spanish→Páez translation
- `Broomva/{t5,mt5,bart}-*-spa-pbb` — multiple smaller seq2seq baselines

These give you a working pretrained baseline you can finetune on your enlarged corpus, instead of starting from raw NLLB-200.

### Added to `government_bilingual/`

- `consejodeestado_nasayuwe_index.html` — full HTML of the Consejo de Estado's Nasa Yuwe institutional-overview page, authored by Yaid Bolaños of Tumbichucue reservation (Inzá, Cauca). Contains ~1.5 KB of formal administrative-domain Nasa Yuwe text. The matching Spanish text is the Council's standard "Quiénes Somos" institutional page (linked in the HTML chrome) — short but a clean register-aligned pair when extracted.

### Checked but redundant or not actionable

- **SUIN-Juriscol Constitution portal** — same content as the Uniandes Constitution PDF already in `pdfs/`. The cleanest plain-text version is now in `huggingface_broomva/instruct_spa_pbb_train.parquet`.
- **patrimoniodocumental.uniandes.edu.co/digital/collection/constitution** — alternative scan archive; covers the same Constitution text.
- **Glosbe (`glosbe.com`)** — community-driven dictionary; Nasa Yuwe content is sparse and scraping requires per-query requests. Lower yield than Living Dictionaries.
- **Scribd "Diccionario Nasa Yuwe-Castellano"** — auth-walled; same Gerdel/Slocum source as Living Dictionaries.
- **LIAMES "Tracing sound change" paper, Sierra et al. 8-story IR corpus** — these are linguistic / IR research artifacts, not directly available as downloadable parallel text. Sierra's eight texts ("Nasa vxanxi's pta'sxnxi", "Kutxh wala ũpxhnxi yuwe", etc., 175 sentences / 1,955 words) would have to be requested from the Universidad del Cauca authors.
- **Consejo de Estado YouTube/audio companion** — page references audio narration by Yaid Bolaños but the audio file URL is not in the HTML; would need to follow the embedded media player to extract.

## Original "Sources NOT yet fetched" list (still open)

- **Sociedad Bíblica Colombiana** — released the *complete* Nasa Yuwe Bible (OT+NT) in 2024 after a 19-year project. The Wycliffe NT in `bible/` is NT-only and from 1984. The new SBC complete Bible would roughly double the parallel corpus once obtainable. SBC does not publish a direct text download.
- **Diaz-Montenegro thesis** (https://theses.hal.science/tel-02469166) — HAL anti-bot blocked direct curl; needs a browser-driven fetch.
- **Faith Comes By Hearing / Bible Brain API** (https://4.dbt.io) — full Nasa Yuwe audio NT plus matched verse-level text; requires a free API key.
- **ELAR Diaz-Montenegro deposit** (https://www.elararchive.org/dk0381) — audio + transcripts from the Munchique variety; deposit access is gated.
- **MinEducación "Kutx yuwe = palabra y tul nasa"** (2015 bilingual book) — referenced but not located online as a direct PDF.
- **PEBI-CRIC physical bilingual cartillas** (Sa't Luuçx, Lecto-Escritura, Comunicación Comunitaria, etc.) — see `pdfs/cric_catalog/` for titles; physical request from CDI-UAIIN-CRIC, Popayán is the only confirmed route.
- **colombialanguages.virtual.uniandes.edu.co team** — actively expanding short-phrase datasets with a native translator (per their site); direct outreach is the best path.
- **YouTube channels** (Joser @Joserteenseña.25, NasaYuwe playlist) — bilingual lessons with captions; needs `yt-dlp --write-subs` extraction.
- **UNESCO OIFF 2019 films** — Nasa Yuwe films with Spanish/English `.srt` subtitles; needs to be located on the IYIL2019 site or UNESCO YouTube.
- **Rojas Curieux (1998) *Gramática del Páez o Nasa Yuwe*** — physical book (LINCOM Studies in Native American Linguistics 8, ISBN 9783895860188), contains hundreds of glossed example sentences; library access needed.

## Reproducing the parallel NT corpus

```sh
cd nasa_yuwe_materials_claude/bible
python build_parallel_nt.py
# → parallel_nt_es_pbb.csv (7,906 rows)
```

## Reproducing the dictionary CSV

```sh
cd nasa_yuwe_materials_claude/dictionaries
python consolidate_living_dict.py
# → living_dictionaries_paez.csv (3,950 entries with Spanish gloss)
```
