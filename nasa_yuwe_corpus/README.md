# Nasa Yuwe Corpus — consolidated resources for Spanish↔Nasa Yuwe MT

A clean, structured collection of every Nasa Yuwe (Páez) language resource gathered for training a Spanish↔Nasa Yuwe machine translation model. ISO 639-3: `pbb`. ~60,000–100,000 speakers in the Cauca department, Colombia.

## Folder hierarchy

```
nasa_yuwe_corpus/
├── 01_parallel_corpora/        ← MT-ready CSV/parquet aligned at sentence level
├── 02_bible_raw/                ← raw NT scriptures (both orthographies + OT stories)
├── 03_dictionaries/             ← lexical resources (CSV + raw + audio + PDFs)
├── 04_government_legal/         ← constitution, government bilingual texts
├── 05_bilingual_literature/     ← children's books, MinEducación series
├── 06_academic_papers/          ← grammars, theses, methodology, sociolinguistics
├── 07_pedagogical/              ← teaching materials, vocabulary cards, catalogs
├── 08_oral_audio/               ← spoken-language audio (placeholder; needs scraping)
├── 09_web_scrapes/              ← raw web captures (JW.org, Wikimedia, Swarthmore pages)
├── 10_models_references/        ← pretrained models on HuggingFace (no downloads)
├── _archive/                    ← original AmericasNLP-2024 paper + repo + raw dumps
├── MANIFEST.md                  ← detailed inventory (legacy; superseded by INVENTORY.csv)
├── INVENTORY.csv                ← machine-readable per-file inventory
└── README.md                    ← this file
```

Each top-level folder contains a `_SOURCES.md` documenting where every file came from, the licence, the alignment method, and the sentence count where applicable.

## Headline numbers — parallel Spanish↔Nasa Yuwe pairs

| Source | Pairs | Domain | Where |
| --- | ---: | --- | --- |
| Bible NT (verse-aligned) | **7,906** | Religious | `01_parallel_corpora/bible_nt_es_pbb.csv` |
| Living Dictionaries (with Spanish gloss) | **3,950** | Lexical | `01_parallel_corpora/living_dictionaries_paez.csv` |
| Swarthmore Talking Dictionary | **3,912** | Lexical | `01_parallel_corpora/swarthmore_talking_dictionary_full.csv` |
| broomva translation_pbb_spa (train+val+test) | **3,794** | Lexical+constitutional | `01_parallel_corpora/broomva_translation_pbb_spa_*.csv` |
| broomva instruct-spa-pbb (incl. Constitution full text) | **7,483** | Constitutional + dict | `01_parallel_corpora/broomva_instruct_spa_pbb_train.parquet` |
| AmericasNLP 2024 paper bundle (Robles et al.) | ~3,862 | Mixed | `_archive/paper_2024_data_local/nasa_full_dataset*.csv` |

⚠ Significant overlap exists between Living Dictionaries, Swarthmore, broomva-translation, and the AmericasNLP paper bundle — they all ultimately derive from the **Gerdel & Slocum 1983** print dictionary. De-duplicating across these is the recommended first preprocessing step.

The Bible NT pairs are the **largest source of unique non-lexical data**. The broomva instruct dataset has clean parallel Constitution articles (1–40) that complement the Bible domain.

## Bible alignment caveat (read before training)

`01_parallel_corpora/bible_nt_es_pbb.csv` aligns the Wycliffe 1984 Nasa Yuwe NT (`pbb` from eBible.org) with the *Versión Biblia Libre* (Spanish, 2018) by shared (book, chapter, verse) IDs. Both are independent translations of the Greek/Hebrew NT canon; the Spanish text is **not** the source from which translators produced the Nasa Yuwe text. Per-verse meaning aligns; word choice does not.

If you want a closer stylistic match to SIL's translation style, re-align against Spanish NTV or NVI. Multiple Spanish parallels can also be combined as data augmentation. See `02_bible_raw/_SOURCES.md` for the rebuild script.

## Two orthographies — important for tokenization

The Nasa NT exists in **two orthographies** that you need to decide between (or model together with a tag):

- **Traditional orthography (1984)** — eBible.org `pbb`, used for `bible_nt_es_pbb.csv`. Heavier diacritic use, ` ' ` glottals, mixed Spanish-derived spellings.
- **New orthography (2014)** — Scripture Earth `pbbN`, complete NT at `02_bible_raw/pbb_new_orth/scriptureearth_complete_NT.pdf`. The unified alphabet ratified by the Nasa community in 2000, used in modern CRIC/PEBI publications.

If your downstream community use will read CRIC/PEBI materials, prefer the new orthography. If your downstream evaluation set uses 1984 SIL spelling, prefer the traditional. Long-term, build a normalizer between them.

## Pretrained models (not downloaded — references only)

See `10_models_references/_SOURCES.md`. Carlos D. Escobar-Valbuena (`Broomva`) published several finetuned Spanish→Páez seq2seq models on HuggingFace including a Llama-2-7B variant. Worth fine-tuning on top of instead of starting from raw NLLB-200.

## Quick start — load every parallel pair into one DataFrame

```python
import pandas as pd

dfs = []
# Bible NT — high quality, verse-aligned
df = pd.read_csv("01_parallel_corpora/bible_nt_es_pbb.csv")
dfs.append(df.rename(columns={"spanish":"es","nasa_yuwe":"pbb"})[["es","pbb"]].assign(source="bible_nt"))

# Living Dictionaries
df = pd.read_csv("01_parallel_corpora/living_dictionaries_paez.csv")
dfs.append(df[df["gloss_es"].notna()].rename(columns={"gloss_es":"es","nasa_yuwe":"pbb"})[["es","pbb"]].assign(source="living_dict"))

# Swarthmore
df = pd.read_csv("01_parallel_corpora/swarthmore_talking_dictionary_full.csv")
dfs.append(df.rename(columns={"gloss":"es","headword":"pbb"})[["es","pbb"]].assign(source="swarthmore"))

# Broomva translation parquet (or CSV)
for split in ["train","validation","test"]:
    df = pd.read_parquet(f"01_parallel_corpora/broomva_translation_pbb_spa_{split}.parquet")
    df = pd.json_normalize(df["translation"]).rename(columns={"spa":"es"}).assign(source=f"broomva_{split}")
    dfs.append(df[["es","pbb","source"]])

all_pairs = pd.concat(dfs, ignore_index=True)
all_pairs = all_pairs.drop_duplicates(subset=["es","pbb"])
print(f"Total unique pairs: {len(all_pairs)}")
```

Expected count: ~17,000 unique pairs after dedup (~25,000 raw before, given ~30% dictionary overlap).

## Where to go next

Open items that need human work (browser auth, account creation, or direct outreach) are documented per-folder in their `_SOURCES.md`. The most important:

1. **Sociedad Bíblica Colombiana 2024 complete Bible (OT+NT)** — would roughly double parallel corpus. Email SBC.
2. **JW.org publication PDFs** (100 codes already catalogued in `09_web_scrapes/jw_org/raw/all_pubs.tsv`) — needs Playwright or the Android JW Library app.
3. **AILLA `ailla:124387` (Tulio Rojas Colombian Languages collection)** — register an AILLA account at ailla.utexas.org.
4. **Faith Comes By Hearing Bible Brain API** — free API key at https://4.dbt.io/api_key/request gives timestamped audio NT (useful for ASR).
5. **ELAR `dk0381` (Díaz-Montenegro Munchique deposit)** — only conversational/oral parallel data in scope.
