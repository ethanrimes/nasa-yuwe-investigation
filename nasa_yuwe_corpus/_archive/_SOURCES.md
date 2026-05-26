# _archive — Original session inputs and pre-existing data

Material kept for reference but not part of the active corpus. The user can safely ignore this folder when training.

## Contents

```
_archive/
├── paper_2024_repo/                  ← The full GitHub repo for the AmericasNLP 2024 paper
│   (juanks235/MT-Colombian-Indigenous-Languages)
│   ├── Americas NLP.xlsx
│   ├── NLP Americas NLLB Methodology.docx
│   ├── README.md
│   ├── data_processing/
│   ├── datasets/                     ← 40 CSVs: arh_*, ing_*, wayuu_*, nasa_full_dataset_*
│   └── models/                       ← trained NLLB checkpoints (empty placeholders / pointers)
├── paper_2024_data_local/            ← Copy of the same `datasets/` CSVs at the repo root
├── paper_2024_data_local.zip          ← Same as above, zipped (~58 MB)
├── paper_2024_notebooks/              ← The training notebooks (convert.ipynb, eval scripts, NLLB *.ipynb)
├── paper_2024_nasa-spanish.tgz        ← 14 GB tarball of the same notebooks + cached model weights
├── paper_2024.americasnlp-1.2.pdf     ← The paper PDF
├── paper_2024_extracted_text.txt      ← Text-only version of the paper (used for citation lookups)
├── search_dumps/                      ← JSON dumps from archive.org and other discovery queries
│   ├── ia.json, ia2.json, ia_*.json
├── broomva_jsons/
│   └── broomva_github_repos.json     ← GitHub API dump of broomva's 100 repos
└── _initial_MANIFEST.md               ← The first manifest written during initial gathering — now superseded by per-folder _SOURCES.md
```

## Headline files

- `paper_2024_repo/datasets/` and `paper_2024_data_local/` both contain the **same 40 CSV files** — the published Robles et al. AmericasNLP 2024 train/dev/test splits for Wayuunaiki, Arhuaco, Inga, and Nasa Yuwe. The Nasa Yuwe-specific files are:
  - `nasa_full_dataset.csv` + `_train.csv` + `_dev.csv` + `_test.csv`
  - `nasa_sin_cartas*.csv` (variant without constitutional letters)
- `paper_2024_extracted_text.txt` is the page-by-page text of the paper itself, useful for citation traces.

## Why archived rather than promoted

The paper's Nasa Yuwe dataset (~3,862 pairs total: 3,729 dictionary + 57 letters + 53 common words + 23 articles) is **almost entirely subsumed** by the data in `01_parallel_corpora/`:

- The 3,729 dictionary entries come from Pueblos Originarios / Gerdel-Slocum, redundant with Living Dictionaries and Swarthmore.
- The 57 letters + 53 common words + 23 articles are subsumed by the cleaner `broomva_instruct_spa_pbb_train.parquet`.

So promoting these would just add redundancy. They're kept here for reproducibility comparison against the original paper benchmarks.
