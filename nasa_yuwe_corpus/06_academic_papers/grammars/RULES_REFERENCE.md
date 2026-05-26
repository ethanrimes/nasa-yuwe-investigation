# Nasa Yuwe Morphological & Grammatical Rules — Reference

A structured rule-set extraction guide for the hybrid rule-based + statistical MT model. This file points to **which grammar to consult** for each component you need to encode as rules, and summarizes the well-known patterns from the published literature.

> **Start here for any rule lookup**: `UNIFIED_GRAMMAR_RULES.md` (consolidated rule catalogue) +
> `complete_grammars/gramatica_descriptiva_basica/_extracted_text/textbook_full.md`
> (the full reusable extracted text of the primary grammar, Nieves 2019).

## Primary grammars in this corpus (in order of usefulness)

| File | Author / Year | Pages | What it covers best |
| --- | --- | ---: | --- |
| `complete_grammars/gramatica_descriptiva_basica/_extracted_text/textbook_full.md` + the 9 chapter PDFs | **Nieves Oviedo, 2019** (Univ. del Valle) | 172 | **PRIMARY REFERENCE — fully extracted.** Phonology (Cap 2), morphology (Cap 3), morfosintaxis + predicación + modopersonal (Cap 4), sintaxis (Cap 5), deíxis (Cap 6). All paradigm tables vision-verified. Use this as the canonical rule source. |
| `complete_grammars/Slocum_1986_Gramatica_Paez_SIL.pdf` | Slocum (SIL), 1986 | 187 | Earlier complete reference grammar (image-only PDF — OCR pending). Use to cross-check Nieves and to fill in the full verbal conjugation paradigms. |
| `complete_grammars/Paez_discourse_paragraph_sentence_structure_SIL.pdf` | SIL, ca. 1980s | 193 | Discourse-level structure beyond the single sentence — useful for above-clause information flow. |
| `../theses/DiazMontenegro_2019_Munchique_thesis.pdf` | Díaz Montenegro, 2019 | ~600 | Modern dialect-specific (Munchique) phonology + syntax. Use for dialect conditioning. |
| `complete_grammars/Estudios_en_Paez_SIL.pdf` | Slocum & Gerdel, 1981 | 174 | Syntax & discourse case studies. |
| `complete_grammars/Gerdel_1973_Fonemas_del_Paez_SIL.pdf` | Gerdel, 1973 | 37 | Foundational phonemic inventory paper; superseded but still useful for dialectal phoneme details. |
| `Rojas_Ramos_Localizacion_NasaYuwe.pdf` | Rojas & Ramos, 2004 | ~10 | Locative morphology — postpositional suffixes / clitics. |
| `Rojas_Desde_arriba_y_por_abajo_alfabeto_nasa.pdf` | Rojas, 2002 | ~10 | The 2001 orthographic unification — essential for the traditional ↔ new orthography normaliser. |
| `complete_grammars/CastilloOrozco_1877_Vocabulario_Paez_Uricoechea_ed.pdf` | Castillo y Orozco, 1755 (Uricoechea 1877 ed.) | — | Historical baseline vocabulary. Reference only — 18th-century orthography differs substantially. |
| `Preview_Gramatica_descriptiva_basica_Nasa_Yuwe.pdf` | (sample) | — | JSTOR preview of Nieves 2019. **Superseded** by the full extracted text. |

## Companion machine-readable rule files (this directory)

| File | Rows | Contents |
| --- | ---: | --- |
| `UNIFIED_GRAMMAR_RULES.md` | (consolidated) | Rule catalogue with IDs, examples, glosses, page citations |
| `morpheme_inventory.csv` | ~115 | Every morpheme (lex + gram), code, form, function, examples |
| `phoneme_inventory.csv` | 69 | 37 consonants + 32 vowels with full feature columns |
| `orthography_map.csv` | ~70 | IPA ↔ unified ↔ SIL-traditional graphemes |
| `predication_templates.csv` | ~57 | Predication patterns + Cap 5 sentence templates |
| `syntactic_rules.csv` | 50 | Numbered syntax rules from Cap 5 |

## Rule categories — where to look

### 1. Phonology / orthography

Two orthographies coexist (see `bible_raw/_SOURCES.md` for the bible-level split):

- **Traditional orthography (SIL, pre-2000)** — used in Slocum, Gerdel, Castillo y Orozco. Glottals as `'`. Heavy use of Spanish-derived letters.
- **Unified orthography (2000 community standard)** — used in modern CRIC/PEBI, eBible new-orth NT. Glottals as `ʼ` or `'`, more systematic. Documented in Rojas (2002).

**Rule sources (in priority order):**
- **Nieves 2019 Cap 2** → `complete_grammars/gramatica_descriptiva_basica/_extracted_text/textbook_full.md` (now fully extracted)
- Phoneme inventory machine-readable: `phoneme_inventory.csv`
- Orthography mapping: `orthography_map.csv` (synthesised from Nieves 2019 Tablas 4-6 + Rojas 2002)
- Cross-check / dialect variation: Díaz Montenegro 2019, LIAMES sound-change paper

**Known phonological features encoded as rules:**
- **4 vowel qualities** (i e a u) × 8 oppositions (oral/nasal × short/long × plain/glottalised/aspirated) = **32 vowels**
- **37 consonants** in maximal inventory: 24 stops/affricates (4 series × 4 places × 2 palatalisation values) + 6 fricatives + 3 nasals + 2 laterals + 2 approximants
- Palatalisation is a productive correlation through 7 of the 8 consonant series
- Glottal stops as phonemic; written `ʼ` in unified orthography (`'` in ASCII)
- Aspirated consonants written `h` after the base letter
- Prenasalised stops written as a single voiced letter in unified orthography (`b d z g` for `ᵐb ⁿd ⁿdz ⁿg`)

### 2. Nominal morphology

Nasa Yuwe is **suffixing and agglutinative**. The "case" system is via postpositional clitics that attach to nouns:

| Suffix | Function | Spanish equivalent | Source verified |
| --- | --- | --- | --- |
| `-su` | locative / instrumental | "por" / "en" | confirmed in master_vocab |
| `-ju` | comitative / instrumental | "con" | confirmed |
| `-pcach` | extent / terminus | "hasta" | confirmed |
| `-pcachja` | duration | "mientras, durante" | confirmed |
| `-va` | additive | "también" / "y" | confirmed |
| `-cjẽ` | spatial | "abajo" | confirmed |
| `-na` | dative / allative | "a, hacia, para" | check Rojas 2004 |
| `-ta` | locative | "en" | check Slocum |
| `-tx` | plural marker (nouns) | "-s" | Slocum 1986 |
| `-we'sx` | collective plural | "los, las (gente)" | Slocum 1986 |

**Action item**: Pull these from `Slocum_1986` chapters on nominal morphology and add to a `rules/suffixes_nominal.csv`.

### 3. Verbal morphology

The most morphologically complex part. Verbs inflect for:

- **Person** (1st, 2nd, 3rd)
- **Number** (singular, plural)
- **Aspect** (perfective, imperfective, progressive, …)
- **Mood** (indicative, imperative, interrogative, …)
- **Gender of speaker AND addressee in 2nd person singular** ← a famously unusual feature, **must be modeled separately**

#### Pronominal paradigm (from published literature)

| Person | Gender | Singular | Plural |
| --- | --- | --- | --- |
| 1 | M | `andy / andya'` | `cue'sh / cue'sha'` |
| 1 | F | `ũ'cue / ũ'cue'` | `cue'sh / cue'sha'` |
| 2 | M | `indy / indya'` | `i'cue'sh / i'cue'cha'` |
| 2 | F | `i'cue / i'cue'` | `i'cue'sh / i'cue'cha'` |
| 3 | N | `tyãa / tyãa'` | `tyãawe'sh / tyãawe'sha'` |

#### Sample verbal paradigm — `we'we-` "to speak", present indicative

| Person/Gender | Form |
| --- | --- |
| 1sg | `we'we-'tj` |
| 2sg.M | `we'we-'ng` |
| 2sg.F | `we'we-'i'cue` |
| 2sg.F.familiar | `we'we-'i'cha` |
| 3sg | `we'we-'c` |
| 1pl | `we'we-'tja'w` |
| 2pl | `we'we-'i'cue` |
| 3pl | `we'we-'ty` |

**Action item**: Use `Slocum_1986` chapter on verbs (probably ch. 3–5) to build full conjugation tables for ~20 most common verbs as rule-templates. Then derive a general inflectional schema.

### 4. Syntax

- Basic word order: **SOV** (some analyses propose OSV for emphatic constructions)
- Postpositions, not prepositions
- Possessor precedes possessed
- Demonstratives precede nouns

**Rule sources:**
- Slocum 1986, syntax chapter
- `Paez_discourse_paragraph_sentence_structure_SIL.pdf` for sentence-level patterns
- Díaz Montenegro 2019 syntax chapter
- Rojas Curieux 1998 PhD (physical only — gold standard)

### 5. Lexicon

The **master vocabulary** at `01_parallel_corpora/master_vocabulary_pbb.csv` contains 8,345 unique normalized lexemes, of which:

- **8,341** have Spanish glosses
- **4,043** appear in 2+ sources (high-confidence)
- **1,299** appear in 3+ sources (very high confidence — your rule-based component should trust these)
- **5,150** have POS tags

For semantic-domain classification, the Living Dictionaries data carries SIL semantic-domain codes (e.g., `2.1` = body, `5.1` = household objects). Use these to organize the lexicon by domain.

### 6. POS tag inventory

POS tags present in the master vocabulary (from Living Dictionaries):

```
n          (noun)
adj        (adjective)
adv        (adverb)
v          (verb generic)
verb transitive
verb intransitive
verb existential
particle
pronoun
postposition
interjection
```

Plus the Sierra et al. 2018 corpus-tagging paper documents a **finer tagset adapted from the Universal Tagset** with Nasa-specific extensions (separating Noun/Numeral, Qualifying adjectives vs. adverbs, etc.). See `06_academic_papers/corpus_building/Martinez_Sierra_Corpus_NasaYuwe_metaheuristic.pdf`.

## Recommended workflow for the hybrid model

1. **Use the master vocabulary** (`master_vocabulary_pbb.csv`) as your lexicon, filtering to `n_sources >= 2` for the rule-based fallback dictionary (~4,000 entries — trustworthy).
2. **Manually transcribe the suffix table** from Slocum 1986 ch. on morphology into a `rules/suffixes.csv`.
3. **Build the verb-stem extractor** that strips known inflectional suffixes (1sg `-'tj`, 3sg `-'c`, etc.) before dictionary lookup.
4. **Encode the 2nd-person speaker/addressee gender rule** — this is critical because conventional MT models will hallucinate gendered output.
5. **For OOV words**, fall back to subword statistical translation (NLLB or m2m100 finetuned).
6. **Orthography normalizer**: build a traditional → new orthography mapping table from `Rojas_Desde_arriba_y_por_abajo`. Run before lookup.

## Open items

- **Slocum 1986 *Gramática Páez*** (187 pp image-only PDF) — OCR-pending. Would unlock the complete verbal conjugation paradigms for ~20 high-frequency verbs (Nieves 2019 gives the *system*; Slocum gives more fully-filled cells per verb).
- **Sierra et al. 2018 POS-tagged corpus** (1,955 words / 175 sentences) — referenced but not posted. Email the Universidad del Cauca authors.
- **Rojas Curieux 1998 *Gramática del Páez*** (528-page LINCOM book) — physical only. A second gold-standard reference; if you can borrow a library copy and OCR it, it would provide a third independent paradigm cross-check.
- **Sound change rules across dialects** — Pitayo, Paniquita, Tierradentro, Munchique, Caldono each have distinct phonological profiles. Díaz Montenegro 2019 covers Munchique exhaustively. Other dialects need cross-referencing.
- **Finer modes** (DES, VOL, CONF, CORR, ENF, REST, INCER) — surface MPN forms per cell are referenced in Nieves 2019 but not always enumerated in printed tables; needs targeted re-scan of pp. 105-115.
