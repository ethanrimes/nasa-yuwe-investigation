# 01_parallel_corpora — MT-ready Spanish↔Nasa Yuwe pairs

Every file here is structured (CSV or parquet) with explicit Spanish ↔ Nasa Yuwe columns. Drop straight into a tokenizer / dataloader.

## Files

| File | Rows | Columns | Domain | Provenance |
| --- | ---: | --- | --- | --- |
| `bible_nt_es_pbb.csv` | 7,906 | book, chapter, verse, spanish, nasa_yuwe | NT scripture | Built locally from `02_bible_raw/pbb_traditional_orth/ebible_html/` (Wycliffe 1984 NT, pbb) and `02_bible_raw/spanish_aligned/spavbl_html/` (*Versión Biblia Libre*, 2018). See `scripts/build_parallel_nt.py`. Alignment by shared (book, chapter, verse) IDs. **Spanish is a separate Bible translation, not the translators' source text.** |
| `living_dictionaries_paez.csv` | 3,954 (3,950 with Spanish gloss) | entry_id, nasa_yuwe, pos, gloss_es, gloss_en, gloss_other, semantic_domain, notes | Lexical | Built locally from Living Dictionaries (livingdictionaries.app) Supabase paginated dump in `03_dictionaries/living_dictionaries/raw/supabase_paez/`. Most entries cite **Gerdel & Slocum 1983** as the underlying source. See `scripts/consolidate_living_dict.py`. |
| `swarthmore_talking_dictionary.csv` | 2,324 | id, initial, page, headword, part_of_speech, gloss, authority, audio_url, source_url | Lexical | Browse-mode scrape of `talkingdictionary.swarthmore.edu/paez/`. Same Gerdel/Slocum 1983 lineage. |
| `swarthmore_talking_dictionary_full.csv` | 3,912 | id, page, headword, part_of_speech, gloss, authority, audio_url, source_url | Lexical | All-entries scrape (search-mode). Slightly larger than the browse variant. Audio files are in `03_dictionaries/swarthmore_talking/audio/`. |
| `broomva_translation_pbb_spa_train.{csv,parquet}` | 2,428 | id, translation.pbb, translation.spa | Lexical+constitutional | HuggingFace `Broomva/translation_pbb_spa`, train split. CC-by-default, no attribution restrictions stated. |
| `broomva_translation_pbb_spa_validation.{csv,parquet}` | 607 | (same) | (same) | (same) |
| `broomva_translation_pbb_spa_test.{csv,parquet}` | 759 | (same) | (same) | (same) |
| `broomva_instruct_spa_pbb_train.parquet` | 7,483 | text (Llama-2 `[INST]…[/INST]` format) | Constitutional articles + dictionary | HuggingFace `Broomva/instruct-spa-pbb`. **Includes Constitution articles 1–40 in clean plain text — easier than OCRing the PDF.** |

Plus README and metadata side-files (`_broomva_*` prefixed).

## Headline counts

- **Total raw pairs across files: ~26,500**
- **Estimated unique pairs after dedup: ~17,000** (dictionary lineages overlap heavily)
- **Largest source of unique non-lexical pairs: Bible NT (7,906 verses)**

## Overlap matrix (rough)

| | Bible | Living | Swarth | Broomva-trans | Broomva-instruct |
| --- | --- | --- | --- | --- | --- |
| **Bible** | — | none | none | none | partial (Const. only) |
| **Living** | — | — | high (~80% — same Gerdel/Slocum source) | high | partial |
| **Swarth** | — | — | — | high | partial |
| **Broomva-trans** | — | — | — | — | partial |

## Rebuild scripts

- `scripts/build_parallel_nt.py` — walks `02_bible_raw/` HTML, emits `bible_nt_es_pbb.csv`.
- `scripts/consolidate_living_dict.py` — reads `03_dictionaries/living_dictionaries/raw/supabase_paez/*.json`, emits `living_dictionaries_paez.csv`.

## Licences

- Bible: Wycliffe Bible Translators © 1984 (pbb), CC-BY-NC-ND for distribution by eBible.org. *Versión Biblia Libre* © 2018, CC-BY-SA.
- Living Dictionaries: CC-BY for entries (Living Tongues Institute).
- Swarthmore Talking Dictionary: CC-BY-NC.
- Broomva HuggingFace datasets: no explicit licence on the dataset cards; ask the author for distribution rights.

## Recommended training pipeline

1. Concatenate all files via the snippet in the top-level `README.md`.
2. De-duplicate on `(es, pbb)` strings — drops ~30%.
3. Filter Bible NT verses with verse length > 5 tokens (drops short fragments like " 23 ").
4. Hold out the broomva test split (`broomva_translation_pbb_spa_test.parquet`) for benchmarking — it was the eval set for the published broomva models.
