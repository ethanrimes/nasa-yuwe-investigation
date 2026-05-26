# 09_web_scrapes — Raw web captures and scraping scripts

Discovery and partial-scrape artifacts. These are not training-ready but are kept so we don't have to re-discover URLs / re-crawl pages later.

## Directory layout

```
09_web_scrapes/
├── jw_org/                            ← Jehovah's Witnesses Nasa Yuwe library scrape
│   ├── extract_pubs.sh                ← scraper script
│   ├── raw/
│   │   ├── root.html, cat_*.html      ← top-level category pages
│   │   ├── sub__pbb_wol_*.html        ← per-year subpages
│   │   ├── all_pubs.tsv               ← ★ 100 publication codes discovered
│   │   ├── sample_pub.html
│   │   └── finder_es_lff.html         ← sample Spanish equivalent
│   ├── html/                          ← (empty; placeholder for future PDF extraction)
│   └── pdfs/                          ← (empty; placeholder)
├── wikimedia_incubator/               ← Nasa Yuwe Wikipedia incubator (only 3 articles)
│   ├── Wp_pbb_*.html                  ← rendered articles
│   └── Wp_pbb_*.wiki.txt              ← raw wikitext
├── legacy_pages_swarthmore/           ← older Swarthmore scrapes (mostly redundant)
│   ├── kwesxyuwe.com_material.html.html
│   ├── livingdictionaries.app_nasa-yuwe.html
│   ├── repositorio.uniandes.edu.co_*.html
│   ├── sites.google.com_view_polifonias-unicauca_*.html
│   ├── www.omniglot.com_writing_paez.htm.html
│   ├── talking_dictionary_browse/     ← initial browse-mode HTML
│   └── talking_dictionary_all_search/ ← all-search HTML
├── consejo_de_estado_html/            ← (empty; Consejo HTML lives in 04_government_legal)
├── youtube_subs/
│   └── fetch_subs.sh                  ← yt-dlp script you run locally with --cookies-from-browser
└── initial_metadata/                  ← initial discovery dumps
    ├── candidate_download_links.txt
    ├── harvested_links.txt
    ├── download_manifest.csv
    └── various .txt / .json captures from first scrape pass
```

## High-value file: `jw_org/raw/all_pubs.tsv`

100 Nasa Yuwe publications on `wol.jw.org/pbb/wol/library/r345/lp-paz/`, indexed by category and publication code. Format:

```
category    pub-code    title-in-nasa-yuwe    url-path
```

Every code maps to a Spanish equivalent at the same URL with `/pbb/` → `/es/`. Downloading the PDFs requires browser cookies (the JW.org download dropdown calls a `data-jsonurl` endpoint that needs rendered DOM state). The JW Library Android app is the most reliable batch path — install, set language to Nasa Yuwe, download all, then language-switch to Spanish.

## YouTube subtitles

The `youtube_subs/fetch_subs.sh` script targets known Nasa Yuwe channels (Joser, Familia Chilo, NasaYuwe playlist, etc.). YouTube now requires authenticated cookies for all subtitle access, so this must be run locally with `--cookies-from-browser chrome` (or your browser of choice).

**Expectation-setting:** most of these channels rely on YouTube's auto-Spanish ASR transcription of mixed Spanish+Nasa-Yuwe audio. The Spanish side is okay; the Nasa Yuwe side is garbled (transcribed as if it were Spanish). Treat as low-priority supplementary data.

## Initial metadata files

`initial_metadata/` holds the first-pass discovery dumps from a prior session — `harvested_links.txt`, `candidate_download_links.txt`, etc. These are kept for audit but most useful URLs from them have already been followed up.
