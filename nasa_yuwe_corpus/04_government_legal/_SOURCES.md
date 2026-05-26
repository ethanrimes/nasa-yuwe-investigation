# 04_government_legal — Government, constitutional, and administrative texts

Authoritative formal-register Nasa Yuwe text — primarily the 1991 Colombian Constitution and various government communications.

## Files

```
04_government_legal/
├── constitution_1991/
│   ├── Constitucion_de_1991_Nasa_Yuwe_Uniandes.pdf     ← 13.6 MB
│   ├── La_traduccion_contextual_constitucion_Nasa_Yuwe_Ramos_Pacho.pdf
│   └── Landaburu_traduccion_constitucion_7lenguas.pdf
├── procuraduria/
│   ├── Caracterizacion_NASA_YUWE_Procuraduria.pdf
│   └── Texto_Institucional_Nasa_Castellano_Nasa_Yuwe_Procuraduria.pdf
├── adres/
│   └── TEXTO_LENGUA_NASAYUWE_Adres.pdf
├── caroycuervo/
│   └── Paez_CaroyCuervo.pdf
├── consejo_de_estado/
│   ├── nasa_yuwe_institutional_overview.html
│   ├── landing_es.html
│   └── about_es.html
└── ministry_of_justice/                ← (empty placeholder; see SUIN-Juriscol notes)
```

## Provenance

| File | Source | URL | Year |
| --- | --- | --- | --- |
| `Constitucion_de_1991_Nasa_Yuwe_Uniandes.pdf` | Uniandes Patrimonio Documental | https://patrimoniodocumental.uniandes.edu.co/digital/collection/constitution | 1994 (translation), 2022 (digital re-release with MinJusticia) |
| `La_traduccion_contextual_constitucion_Nasa_Yuwe_Ramos_Pacho.pdf` | Ramos Pacho article on contextual translation | DialNet | n/a |
| `Landaburu_traduccion_constitucion_7lenguas.pdf` | Amerindia / CNRS | https://amerindia.cnrs.fr/wp-content/uploads/2021/02/Historia-de-la-traduccio%CC%81n-... | (Landaburu retrospective) |
| `Caracterizacion_NASA_YUWE_Procuraduria.pdf` | Procuraduría General | https://apps.procuraduria.gov.co/portal/media/file/Caracterizacion%20%20NASA%20YUWE.pdf | n/a |
| `Texto_Institucional_Nasa_Castellano_Nasa_Yuwe_Procuraduria.pdf` | Procuraduría General | apps.procuraduria.gov.co | n/a |
| `TEXTO_LENGUA_NASAYUWE_Adres.pdf` | ADRES (Administradora de los Recursos del Sistema General de Seguridad Social en Salud) | https://www.adres.gov.co/portal-del-ciudadano/Lenguas_nativas/TEXTO_LENGUA_NASAYUWE.pdf | 2025 |
| `Paez_CaroyCuervo.pdf` | Instituto Caro y Cuervo | https://lenguasyliteraturasnativas.caroycuervo.gov.co/publicaciones/2023/11/paez.pdf | 2023 (Ingrid Jung overview) |
| `nasa_yuwe_institutional_overview.html` | Consejo de Estado | https://www.consejodeestado.gov.co/2021/11/04/nasa-yuwe/index.htm | 2021 (text & audio by Yaid Bolaños of Tumbichucue reservation) |

## Parallel content already extracted into `01_parallel_corpora/`

The cleanest Constitution parallel data is **not** in the Uniandes PDF (which needs OCR), but in `01_parallel_corpora/broomva_instruct_spa_pbb_train.parquet` — articles 1–40 as clean `[INST] Spanish [/INST] Nasa-Yuwe` strings. Filter rows where `text` contains "Artículo".

## Not yet harvested

- **SUIN-Juriscol portal** (https://www.suin-juriscol.gov.co/legislacion/constituciones_lenguasindigenas.html) — same constitution content as the Uniandes PDF, but with cleaner per-article navigation. Could be scraped article-by-article instead of OCR'ing the PDF.
- **Consejo de Estado audio** — page references audio narration by Yaid Bolaños; needs browser dev tools to extract the embedded MP3 URL.
- **Derechos en el Territorio (Constitutional Court rulings)** — turns out **Nasa Yuwe is NOT included** in the 30 indigenous languages they published. Verified via site language menu.
