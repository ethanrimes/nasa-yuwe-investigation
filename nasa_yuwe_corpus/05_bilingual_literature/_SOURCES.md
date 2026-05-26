# 05_bilingual_literature — Bilingual children's books and cultural literature

Professionally edited bilingual Nasa Yuwe ↔ Spanish published books. PDFs are scanned/typeset — extracting clean parallel sentences requires OCR or layout-aware parsing.

## Files

```
05_bilingual_literature/
├── territorios_narrados/
│   ├── 04-Ipx_kwet_pekuj-AlrededorTulpa.pdf            ← 9.1 MB
│   ├── 06-Nasa_Ujunxin_Thegnxi-LeyendoVidaNasa.pdf     ← 5.4 MB
│   ├── 09-Luucx_Pekuhn_Ujusaa-Chivito.pdf              ← 2.9 MB
│   └── 10-Lxan_Nasa_Pal-AlvaroMojana.pdf               ← 3.2 MB
└── Putunkaa_Serruma_5etnias_ICBF.pdf                   ← 7.7 MB
```

## Provenance

| Book | Original title | Source | Publisher |
| --- | --- | --- | --- |
| #04 Ipx Kwet Peku'j | Alrededor de la tulpa | https://archive.org/details/04-ipx-kwet-pekuj-alrededor-de-la-tulpa-edicion-bilingue-nasayuwe-espanol | MinEducación de Colombia / *Plan Nacional de Lectura, Escritura y Oralidad* (Territorios Narrados series) |
| #06 Nasa U'junxin Thegnxi | Leyendo la vida Nasa | https://archive.org/details/06-nasa-ujunxin-thegnxi-... | Same series |
| #09 Luucx Pekuhn U'jusaa | Chivito, el niño viajero | https://archive.org/details/09-luucx-pekuhn-ujusaa-chivito-... | Same series |
| #10 Lxan Nasa Pal Kũbxyac | Álvaro Nasa Pal y la Mojana | https://archive.org/details/10-lxan-nasa-pal-kubxyac-... | Same series |
| Putunkaa Serruma | (Arrullos y relatos de 5 etnias) | https://maguare.gov.co/wp-content/uploads/2017/12/493_putunka-serruma.pdf | ICBF / Maguaré |

**Licence:** Territorios Narrados PDFs are CC-BY-NC-ND 4.0 per the Internet Archive metadata.

## ⚠ Important note on Putunkaa Serruma

This book covers **Piapoco, Arhuaco, Kamëntsá, Uitoto, and Wayúu — NOT Nasa Yuwe.** It was included on a recommendation from one of the resource guides, which was incorrect. The PDF is kept for reference (it's referenced in adjacent literature on bilingual children's books in Colombia) but is **not usable as Nasa Yuwe training data.**

## Territorios Narrados — recommended next step

Each PDF contains a clearly-structured "Texto en Nasa Yuwe / Texto en español" page-by-page parallel layout. Extracting the parallel text requires:

1. PDF → text via `pdftotext -layout` (preserves columns) OR `pdfplumber` for finer-grained extraction
2. Detect left/right column boundaries
3. Match paragraphs by index

Estimated yield: 200–500 sentences per book × 4 books = **~1,500 sentence pairs**, all in a literary/narrative register the Bible and dictionary don't cover.

This is on the to-do list — the PDFs are saved but the extracted text is not in `01_parallel_corpora/` yet.

## Not yet harvested

- Other PEBI/CRIC bilingual books (Sa't Luuçx series, Comunicación Comunitaria, etc.) — see `07_pedagogical/cric_uaiin_pebi/CRIC_UAIIN_PEBI_Catalogo_2024.pdf` for the full catalog. Physical copies only from CDI-UAIIN-CRIC in Popayán.
- **MinEducación "Kutx yuwe = palabra y tul nasa" (2015)** — referenced in catalogs but no direct download located.
