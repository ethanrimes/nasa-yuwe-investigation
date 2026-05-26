# 03_dictionaries — Lexical resources

Word/phrase-level resources. The structured CSVs already live in `01_parallel_corpora/`; this folder has the raw scraped JSON, the print dictionaries (PDFs), and the audio files behind the Swarthmore Talking Dictionary.

## Directory layout

```
03_dictionaries/
├── living_dictionaries/
│   ├── raw/
│   │   ├── supabase_paez/         ← paginated Supabase API dump
│   │   │   ├── entries_*.json     ← 3,934 entries across 8 pages
│   │   │   ├── senses_*.json      ← 9,934 senses across 6 pages
│   │   │   ├── audio.json
│   │   │   └── sentences.json
│   │   ├── living_nasa-yuwe-paez_entries.html
│   │   ├── living_nasa-yuwe_entries.html
│   │   ├── pueblos_paez.html      ← Pueblos Originarios Páez dictionary page
│   │   ├── swarthmore_*.html      ← Swarthmore Talking Dictionary scrapes
│   │   └── blogspot_index.html    ← diccnasayuwe.blogspot.com index
│   ├── scrape_supabase_paez.sh    ← scraper script (audit trail)
│   └── fetch_senses_by_entry.py   ← helper script
├── swarthmore_talking/
│   ├── audio/                     ← 1,002+ MP3 audio files of speaker pronunciations
│   └── pages/                     ← HTML scrapes of the dictionary's search interface
└── pdfs/
    ├── CDI_144_Diccionario_Nasa_Yuwe_UAIIN_CRIC.pdf
    ├── Dic_Nasa_ling_fi.pdf
    └── Nasa_Yuwete_Wewna_Fxijya_Piyaca_UAIIN_CRIC.pdf
```

## Sources

| Resource | URL | Entries | Notes |
| --- | --- | ---: | --- |
| Living Dictionaries (Páez) | https://livingdictionaries.app/nasa-yuwe-paez | 3,934 | Maintained by Living Tongues Institute. Most entries cite Gerdel & Slocum 1983 as source. |
| Swarthmore Talking Dictionary | http://talkingdictionary.swarthmore.edu/paez/ | 3,934 entries / 1,002 audio | Maintained by K. David Harrison's group; data also from Gerdel & Slocum 1983 plus 2012 fieldwork by Ananías Piñacué and Francy Yanet (Stanford workshop at Instituto Caro y Cuervo). |
| Diccionario Nasa Yuwe UAIIN/CRIC (CDI-144) | https://sia.uaiinpebi-cric.edu.co/static/img/11_LIBROS/CDI_-_144_DICCIONARIO_NASA_YUWE.pdf | n/a (PDF) | Community-published unified-orthography dictionary. |
| Dic. Nasa (ling.fi) | http://www.ling.fi/Entradas%20diccionario/Dic=Nasa.pdf | n/a (PDF) | Alain Fabre's etnolinguistic compilation entry. |
| Nasa Yuwete Wewna Fxijya Piyaca | https://sia.uaiinpebi-cric.edu.co/static/img/IMAGENES_CDI/... | n/a (PDF) | CRIC vocabulary primer. |

## What's in `01_parallel_corpora/` derived from this folder

- `living_dictionaries_paez.csv` — 3,950 with Spanish glosses (built from `living_dictionaries/raw/supabase_paez/`)
- `swarthmore_talking_dictionary.csv` / `_full.csv` — 2,324 / 3,912 entries (pre-built from a previous session's scraping)

## Not yet harvested

- **Pueblos Originarios** dictionary text — `pueblos_paez.html` is auth-protected; only the index page scraped.
- **diccnasayuwe.blogspot.com** entries — index scraped, individual entries not parsed.
- **Glosbe** Nasa Yuwe pairs — sparse community-driven dictionary at https://glosbe.com. Per-query scrape required; lower yield than Living Dictionaries.
- **Scribd "Diccionario Nasa Yuwe-Castellano"** — auth-walled, likely redundant with Living Dictionaries (same Gerdel/Slocum source).
