# 02_bible_raw — New Testament scriptures and aligned Spanish

Both Nasa Yuwe NT orthographies plus the Old Testament narrative summary, in every format I could find.

## Directory layout

```
02_bible_raw/
├── pbb_traditional_orth/      ← Wycliffe 1984 NT (the orthography used in `bible_nt_es_pbb.csv`)
│   ├── ebible_html/           ← 323 chapter HTML files (one per book chapter)
│   ├── ebible_pbb_html.zip    ← same HTML packaged
│   ├── ebible_pbb.epub
│   ├── ebible_pbb_readaloud.zip
│   ├── ebible_pbb_sword.zip   ← CrossWire Sword module
│   └── scriptureearth_complete_NT.pdf   ← single combined PDF (6.8 MB)
├── pbb_new_orth/               ← New unified orthography (post-2000 standard)
│   └── scriptureearth_complete_NT.pdf   ← single combined PDF (3.7 MB)
├── ot_stories/
│   └── pbb_Dyusna-selpisaawesh_1993.pdf ← OT narrative summary (Gen–Kings stories)
├── creation/
│   └── pbb_CREATION.pdf       ← standalone creation account
└── spanish_aligned/            ← used to build the parallel NT
    ├── spavbl_html/           ← Versión Biblia Libre chapter HTML
    ├── spavbl_html.zip
    ├── spavbl.epub
    └── spavbl_sword.zip
```

## Provenance

| Resource | Source | URL | Year | Licence |
| --- | --- | --- | --- | --- |
| pbb traditional NT (HTML/ePub/Sword) | eBible.org `pbb` | https://eBible.org/Scriptures/pbb_html.zip etc | 1984 (Wycliffe), 2011 republish | CC-BY-NC-ND © WBT |
| pbb traditional NT (single PDF) | Scripture Earth (SIL) | https://www.scriptureearth.org/data/pbb/PDF/00-WNTpbb-web.pdf | 1984/2011 | Same |
| pbb **new** orthography NT (PDF) | Scripture Earth (SIL) | https://www.scriptureearth.org/data/pbb/PDF/00-WNTpbbN-web.pdf | 2014 | Same |
| OT narrative summary | Scripture Earth (SIL) | https://www.scriptureearth.org/data/pbb/PDF/pbb_Nasa_Dyusna-selpisaawesh_2ndEd_1993.pdf | 1993 (2nd ed) | Same |
| Creation account | Scripture Earth (SIL) | https://www.scriptureearth.org/data/pbb/PDF/pbbCREATION.pdf | n/a | Same |
| *Versión Biblia Libre* (Spanish) | eBible.org `spavbl` | https://eBible.org/Scriptures/spavbl_html.zip | 2018+ | CC-BY-SA |

Per-book PDFs (e.g., `41-MATpbb-web.pdf`, `41-MATpbbN-web.pdf`) are also available at the Scripture Earth `/data/pbb/PDF/` directory if you want book-level splits — not downloaded here because the complete combined PDF supersedes them.

## How the parallel CSV was built

`01_parallel_corpora/scripts/build_parallel_nt.py`:
1. For each of 27 NT books × N chapters, parse the `<span class="verse" id="VN">` markers in both the pbb and spavbl HTML.
2. Strip footnote and cross-reference text.
3. Emit one row per `(book, chapter, verse)` where both languages have non-empty text.

Result: **7,906 aligned verses** (out of 7,923 pbb / 7,941 spa raw verse extractions).

## Important caveats

- The Spanish text is a 2018 translation; the Nasa Yuwe text is a 1984 translation. Both translate the Greek/Hebrew NT canon, so per-verse meaning is consistent but word choice diverges. The Spanish is **not** the Spanish source the SIL translators worked from.
- The **new-orthography** NT has a different surface form for almost every word. If your downstream consumers read CRIC/PEBI-style modern Nasa Yuwe, you may want to re-align using the new-orth PDF instead. The PDF is not pre-segmented; expect to OCR + sentence-split it.
- The OT narrative summary is **not** the canonical OT — it's a Gen–Kings story digest. The Sociedad Bíblica Colombiana 2024 complete Bible has the canonical OT, but is not yet publicly downloadable.

## Not yet fetched

- Per-book individual PDFs (available at `https://www.scriptureearth.org/data/pbb/PDF/NN-BOOKpbb[N]-web.pdf` for NN=41..67, BOOK in NT book codes)
- USFM source (not published by SIL for `pbb`)
- Faith Comes By Hearing audio NT (free API key at https://4.dbt.io/api_key/request)
- Sociedad Bíblica Colombiana 2024 complete Bible (OT+NT, single integrated edition)
