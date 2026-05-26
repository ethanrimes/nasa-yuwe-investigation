# 06_academic_papers — Grammars, theses, methodology, sociolinguistics

Reference material for understanding Nasa Yuwe morphology, phonology, and the research methods that produced the dictionaries and translations in the rest of the corpus. Most contain glossed example sentences that could be extracted as auxiliary parallel data.

## Files

```
06_academic_papers/
├── grammars/
│   ├── Preview_Gramatica_descriptiva_basica_Nasa_Yuwe.pdf
│   ├── Preview_Cultura_escrita_lengua_Nasa_Yuwe.pdf
│   ├── Rojas_Ramos_Localizacion_NasaYuwe.pdf
│   └── Rojas_Desde_arriba_y_por_abajo_alfabeto_nasa.pdf  ← CILLA 2002
├── theses/
│   ├── DiazMontenegro_2019_Munchique_thesis.pdf          ← ~6 MB, the major modern reference grammar
│   ├── CRUZ_EDILMA_DIAZ_Estado_NasaYuwe_Sxisxukwe.pdf
│   ├── MARIA_LUCIA_MUSSE_debilitamiento_nasa.pdf
│   └── LUIS_CAMAYO_Paksxaw_orientacion_pedagogica.pdf
├── methodology/
│   ├── Interprete_contextual_expresiones_Nasa_Yuwe_Dialnet.pdf
│   └── Firefox_Nasa_localization_UNIMINUTO.pdf
├── corpus_building/
│   └── Martinez_Sierra_Corpus_NasaYuwe_metaheuristic.pdf
├── sociolinguistics/
│   ├── Pitto_Transmision_idioma_nasa.pdf
│   ├── Colantropos_pueblo_nasa_escritura.pdf
│   ├── Nasa_Yat_redalyc.pdf
│   └── Abanate_Kwesx_Knaynxi_Nasa_Yuwe_Armada.pdf
└── americasNLP/
    ├── AmericasNLP_2024_TranslationColombianIndigenous_paper.pdf  ← the paper this work extends
    └── AmericasNLP_2025_findings.pdf
```

## Provenance highlights

| File | Author / Year | Why it matters |
| --- | --- | --- |
| `theses/DiazMontenegro_2019_Munchique_thesis.pdf` | Esteban Díaz Montenegro, Univ. Lyon 2 PhD, 2019 | The most comprehensive modern description of Nasa Yuwe (Munchique variety) — sociolinguistics, phonology, syntax. Contains 6 hours of transcribed, Spanish-translated audio that lives in the ELAR deposit. Many glossed sentences with parallel Spanish. |
| `grammars/Rojas_Desde_arriba_y_por_abajo_alfabeto_nasa.pdf` | Tulio Rojas Curieux, CILLA 2002, UT Austin | History of the unification of the Nasa Yuwe alphabet (basis of the "new orthography" used in `02_bible_raw/pbb_new_orth/`). |
| `grammars/Rojas_Ramos_Localizacion_NasaYuwe.pdf` | Rojas & Ramos, Amerindia 29/30, 2004–2005 | Locative morphology — important for understanding the postpositional suffixes that complicate tokenization. |
| `americasNLP/AmericasNLP_2024_TranslationColombianIndigenous_paper.pdf` | Robles et al., AmericasNLP 2024 | The paper that produced the foundational ~3,862-pair dataset in `_archive/paper_2024_repo/`. |
| `corpus_building/Martinez_Sierra_Corpus_NasaYuwe_metaheuristic.pdf` | Sierra Martínez et al., Computación y Sistemas 2018 | The 1,955-word manually-tagged POS corpus + 8 traditional narrative texts (175 sentences). The narratives themselves are not freely downloadable — must contact the Universidad del Cauca authors. |

## Source URLs (mostly already in MANIFEST history)

- Most CRIC/UAIIN theses came from https://sia.uaiinpebi-cric.edu.co/static/img/11_LIBROS/
- Díaz Montenegro thesis was downloaded by the user directly from HAL (https://theses.hal.science/tel-02469166) — automated curl/wget hits HAL's anti-bot wall.
- Procuraduría and ADRES PDFs are linked from their respective ministry portals.
- Caro y Cuervo PDFs are from https://lenguasyliteraturasnativas.caroycuervo.gov.co/

## Glossed example sentences — auxiliary parallel data

Several PDFs here contain hundreds of glossed example sentences with Spanish translations. Extracting them would augment `01_parallel_corpora/`:

- **DiazMontenegro 2019 thesis** — easily the largest source; estimated ~1,500–3,000 glossed examples
- **Rojas/Ramos Localización** — ~50–100 examples
- **Preview_Gramatica_descriptiva_basica** — ~100 examples (just a preview though)

Extraction is non-trivial: example sentences are usually interlinear-glossed (3-line format with morpheme breakdown), and the Spanish translation is on the third line. A custom parser per work is needed.

## Not yet harvested

- **Rojas Curieux 1998 *Gramática del Páez o Nasa Yuwe*** (LINCOM book, ISBN 9783895860188) — the foundational reference grammar; ~500+ glossed sentences. Physical book only.
- Other Tulio Rojas Curieux papers behind academia.edu / Scribd auth walls.
- **Landaburu "Expresión gramatical de lo epistémico"** chapter (Peeters 2007 volume) — physical book.
