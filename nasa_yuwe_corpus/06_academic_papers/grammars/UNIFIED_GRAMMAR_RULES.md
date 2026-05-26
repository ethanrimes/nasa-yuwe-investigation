# Unified Nasa Yuwe Grammar Rules

Consolidated rule catalogue for the hybrid rule-based + statistical MT model.

**Primary source — fully extracted** ✓
Nieves Oviedo, Rocío del Pilar. *Gramática Descriptiva Básica del Nasa Yuwe: Lengua Indígena Colombiana.*
Programa Editorial Universidad del Valle, 2019. ISBN 978-958-765-950-4. (Hereafter **GDB 2019**.)

The full extracted text now lives at
`complete_grammars/gramatica_descriptiva_basica/_extracted_text/textbook_full.md`
(reusable, ~232 KB, vision-verified for the critical paradigm tables). Previous
extractions in `_extracted_text/clean/` only contained the first few pages of
each chapter and were missing Cap 2 (Fonología) and Cap 5 (Sintaxis) entirely;
both gaps are now closed.

**Secondary sources** (cross-checks):
- Slocum, M. C. *Gramática Páez.* SIL Townsend, 1986 (187 pp; image-only PDF — OCR pending).
- Slocum & Gerdel. *Estudios en Páez.* SIL Serie Sintáctica, 1981 (174 pp).
- *Páez Discourse, Paragraph and Sentence Structure.* SIL, n.d. (193 pp).
- Gerdel, F. L. *Fonemas del páez.* MinGobierno, 1973 (37 pp).
- Rojas Curieux, T. *Desde arriba y por abajo.* CRIC, 2002 (orthography unification, 2001).
- Díaz Montenegro, E. *El habla nasa (páez) de Munchique.* Univ. Lyon 2 PhD, 2019.
- Castillo y Orozco / Uricoechea, *Vocabulario Páez-Castellano.* 1877 (1755 ms.) — historical only.

**Companion machine-readable files** (same directory):
- `phoneme_inventory.csv` — 69 phoneme rows (37 C + 32 V) with feature columns
- `orthography_map.csv` — IPA ↔ unified ↔ SIL-traditional mapping
- `morpheme_inventory.csv` — all morphemes (~115 rows after extension)
- `predication_templates.csv` — predication patterns + Cap 5 sentence templates
- `syntactic_rules.csv` — 50 syntactic rules from Cap 5

---

## Table of contents

1. [Conventions and notation](#1-conventions-and-notation)
2. [Phonology](#2-phonology)
3. [Orthography](#3-orthography)
4. [Morphology — types, procedures, lexeme classes](#4-morphology)
5. [Word classes](#5-word-classes)
6. [Predication and the modal-personal morpheme](#6-predication-and-the-modal-personal-morpheme)
7. [Argument structure and case](#7-argument-structure-and-case)
8. [Aspect](#8-aspect)
9. [Information structure: topicalisation and focalisation](#9-information-structure-topicalisation-and-focalisation)
10. [Voice](#10-voice)
11. [Deixis: person, space, time](#11-deixis-person-space-time)
12. [Pronouns and possessives](#12-pronouns-and-possessives)
13. [Negation, interrogation, modality](#13-negation-interrogation-modality)
14. [Sentence types and complex clauses (Sintaxis)](#14-sentence-types-and-complex-clauses)
15. [Dialectology](#15-dialectology)
16. [Full morpheme / abbreviation inventory](#16-full-morpheme--abbreviation-inventory)
17. [Open rule-set items](#17-open-rule-set-items)
18. [Implementation guidance for the hybrid MT model](#18-implementation-guidance-for-the-hybrid-mt-model)

---

## 1. Conventions and notation

Inherited from GDB 2019 (Symbols and Conventions section):

| Symbol | Meaning |
| --- | --- |
| `*` | ungrammatical / non-existent |
| `=` | equivalent to |
| `→` | is realised as |
| `~` | phonological alternation / allomorph condition |
| `-` (left) | morpheme suffixes to a base |
| `-` (right) | morpheme prefixes to a base |
| `-…-` | morpheme is surrounded by other morphemes (medial) |
| `.` | syllable boundary |
| `ø` | zero (null) morph |
| `+` | adds morphemes or categories |
| `{…}` | morpheme delimiter |
| `[…]` | phonetic transcription (IPA) |
| `/…/` | phonological transcription |
| `/…/ : /…/` | phonological opposition |
| `"…"` | Spanish gloss |
| `ʼ` | glottalised (apostrophe, unified orthography) |

In the *yuxtalineal* (interlinear) example notation used throughout the grammar:
- `{…}` morphological level
- `//…//` utterance gloss line
- `/` separates words
- `-` separates morphemes
- `.` joins amalgamated categories (e.g. `3psASER.PE`)

---

## 2. Phonology

Source: GDB 2019 Capítulo 2 (pp. 27-56), now fully extracted.

### 2.1 Consonant system (37 phonemes in the maximal inventory)

Four points of articulation × eight series:

- **Órdenes (place):** labial, apical, palatoalveolar, posterior (velar + glottal)
- **Series (manner/voicing/aspiration):** oclusivos básicos, oclusivos aspirados, oclusivos prenasalizados, fricativos sordos, fricativos sonoros, nasales, laterales, aproximantes
- **Correlación de palatalización** runs through every series except the approximants

24 oclusivos (4 básicos + 4 palatalizados + 4 aspirados + 4 aspirados-palatalizados + 4 prenasalizados + 4 prenasalizados-palatalizados), 6 fricativos, 3 nasales, 2 laterales, 2 aproximantes = **37**.

| | Labial | Apical | Palatoalveolar | Posterior |
|---|---|---|---|---|
| Oclusivo básico       | p          | t          | ts          | k          |
| Oclusivo palatalizado | pʲ         | tʲ         | tsʲ         | kʲ         |
| Oclusivo aspirado     | pʰ         | tʰ         | tsʰ         | kʰ         |
| Aspirado palatalizado | pʲʰ        | tʲʰ        | tsʲʰ        | kʲʰ        |
| Prenasalizado         | ᵐb         | ⁿd         | ⁿdz         | ⁿg         |
| Prenasal palatalizado | ᵐbʲ        | ⁿdʲ        | ⁿdzʲ        | ⁿgʲ        |
| Fricativo sordo       | —          | s          | —           | h          |
| Fricativo palat.      | ɸʲ         | sʲ         | —           | hʲ         |
| Fricativo sonoro      | βʲ         | —          | —           | —          |
| Nasal                 | m          | n / nʲ     | —           | —          |
| Lateral               | —          | l / lʲ     | —           | —          |
| Aproximante           | w          | —          | j           | —          |

The ts-series is phonetically affricate but groups paradigmatically with the stops.

**Regional reductions** (GDB Cap 2 pp. 27-28):
- Tierradentro, Paniquitá, Caldono-Pueblo Nuevo: full 37-consonant inventory
- Rojas (1991a, 1998) for Munchique-Tigres: 34 consonants
- Yule (1991b) for Toribío: 34 consonants
- Rojas, Perdomo & Corrales (2011) for Novirao: 35 consonants
- Jung (2000, 2008) for Tierradentro: reports 35

### 2.2 Vowel system (32 phonemes in the maximal inventory)

Four qualities **i e a u** (no /o/ phoneme — a notable feature) × eight oppositions per quality:

| Quality | Oral breve | Oral larga | Glotalizada | Aspirada | Nasal breve | Nasal larga | Nasal glotalizada | Nasal aspirada |
|---|---|---|---|---|---|---|---|---|
| /i/ | i  | ii  | iʼ  | ih  | ĩ  | ĩĩ  | ĩʼ  | ĩh  |
| /e/ | e  | ee  | eʼ  | eh  | ẽ  | ẽẽ  | ẽʼ  | ẽh  |
| /a/ | a  | aa  | aʼ  | ah  | ã  | ãã  | ãʼ  | ãh  |
| /u/ | u  | uu  | uʼ  | uh  | ũ  | ũũ  | ũʼ  | ũh  |

4 × 8 = **32 vowels**. Toribío and Munchique-Tigres lack the length contrast for vowels, yielding 24 vowel phonemes.

### 2.3 Syllable structure

Maximal: **(C)(C)V(C)** with the vowel always nuclear.
- Up to two consonants in the onset (mostly C₁ + glide)
- One consonant coda
- Toribío has a slightly different structure (Yule 1991b) — typically no long vowels and a constrained onset.

### 2.4 Morphophonological rules (GDB Cap 2 §morfofonología)

Implementation-relevant alternations:

| Rule ID | Context | Process | Example |
|---|---|---|---|
| **PHON-MPH-001** | Stem-final vowel + V-initial suffix | hiatus repair via deletion or epenthesis | `ji'ph-a'` `ji'ph-u-ku` |
| **PHON-MPH-002** | Stressed syllable before TOP `-aʼ` | long-form allomorph of topicaliser | `kusi-aʼ` (not `*kus-aʼ`) |
| **PHON-MPH-003** | Stem-final aspirated C + V-initial suffix | aspiration preserved | `mji-ø-yãwa-aʼ` → `mjiyãwaʼ` |
| **PHON-MPH-004** | IMPF allomorph selection | `{-u}` after most stems; `{-i}` and `{-e}` selected by stem-final phonology | `wuwu-u-ku`, `teçx-i-ku`, `peb-e-ku` |
| **PHON-MPH-005** | Consecutive glottalised segments | one glottal feature absorbed | (productive in fast speech) |
| **PHON-MPH-006** | Nasal vowel + nasal C | nasal feature spreads (autosegmental) | (regional, esp. Munchique) |

### 2.5 Stress

Lexical stress is contrastive but largely predictable as penultimate, with notable exceptions. The TOP long-form rule (PHON-MPH-002) is the only morphophonological process that directly references stress.

---

## 3. Orthography

GDB 2019 uses the **unified orthography** ratified by the CRIC community process in **2001** (Rojas Curieux 2002). The traditional SIL orthography (1984 NT, Slocum 1986, Gerdel 1973) coexists in older materials.

### 3.1 IPA ↔ Unified ↔ SIL-traditional mapping (Tablas 4-6, vision-verified)

The complete machine-readable table is in `orthography_map.csv`. High-leverage transformations:

| Unified | SIL-traditional | IPA |
|---|---|---|
| `çx`   | `c'h` / `'ch`           | tsʲ |
| `ç`    | `'c` / `ts`             | ts  |
| `çxh`  | `c'h` (ambiguous w/ ç)  | tsʲʰ |
| `çh`   | `tsh`                   | tsʰ |
| `tx`   | `ty`                    | tʲ |
| `kx`   | `ky` / `k'`             | kʲ |
| `nx`   | `ñ`                     | nʲ |
| `lx`   | `ll`                    | lʲ |
| `sx`   | `sh`                    | sʲ |
| `jx`   | `jh` / `sh`             | hʲ |
| `fx`   | `f'`                    | ɸʲ |
| `vx`   | `b'` / `v`              | βʲ |
| `j`    | `h` / `j`               | h |
| `ph th kh` | `ph th kh`          | pʰ tʰ kʰ |
| `b d z g`  | `mb nd ndz ng`      | ᵐb ⁿd ⁿdz ⁿg (single letter in unified) |
| `ã ẽ ĩ ũ`  | `~a in en…` (various) | nasal vowels |
| `ii ee aa uu` | (no length marker)    | long vowels |
| `iʼ eʼ aʼ uʼ` | `i' e' a' u'`         | glottalised vowels |
| `ih eh ah uh` | (often unwritten)       | aspirated vowels |
| `ʼ`           | `'`                     | ʔ |

⚠ **Build a bidirectional orthography normaliser as your first preprocessing step.**
Without it, lookups on the unified `çxhab` ("pueblo") miss SIL-form `c'hab`; lookups
on the unified `nx-` miss SIL `ñ-`. The normaliser is the single highest-leverage
preprocessing component for any rule-based lookup over heterogeneous corpora.

### 3.2 Prenasalisation convention

In the unified orthography, the prenasalised stops are written as **single letters**:
- ᵐb → `b`, ⁿd → `d`, ⁿdz → `z`, ⁿg → `g`

There is **no /b/, /d/, /g/ that is *not* prenasalised** — every orthographic `b` is
phonetically [ᵐb]. This is critical for IPA-aware downstream components.

### 3.3 Glottalisation

The unified orthography uses the modifier letter apostrophe `ʼ` (U+02BC) following
the segment it glottalises. Many electronic resources (this corpus included) substitute
the ASCII straight apostrophe `'` for ease of typing. **Treat both as the same
character** for lookup purposes.

---

## 4. Morphology

GDB Capítulo 3 (pp. 57-80).

### 4.1 Morpheme types and realisation

> *"En nasa yuwe los morfemas están formados por un fonema o una cadena de fonemas,
> articulados en secuencia lineal; no existen morfemas discontinuos ni por marcación
> suprasegmental. Tampoco se expresan significados mediante alternancia de elementos."*
> (Cap 3, opening)

**Implementation invariant:** every morpheme is a **contiguous segmental string**.
No infixes, no tonal morphology, no ablaut. The morphological analyser does not need
to model non-concatenative morphology.

### 4.2 Morphological procedures

- **Flexión (inflection)** — person, number, aspect, mode, case
- **Derivación (derivation)** — class-changing operations
- **Composición (compounding)** — lexical formation

### 4.3 Derivation morphemes (Cap 3)

| Code | Form | Process | Example |
|---|---|---|---|
| NOM | `-sa` | nominaliser: V → N "el que V" | `ka-piya-sa` "el que enseña" |
| FACT | `ka-` | factitive prefix: Q/N → V "hacer Q" | `ka-piya-` "enseñar" (lit. hacer-aprender) |
| CAUS | `-tx-` | causative (medial) | (productive on dynamic verbs) |
| DIN | `-yuu-` | dinamizador: N → change-of-state V | `knaʼsa-yuu-` "volverse jovencita" |
| REF | `yaʼ-` | reflexive / media voice (prefix) | `yaʼ-waʼkx-` "morderse" |
| DIM | `-ne` | diminutive | (productive on nominals) |
| COL | `-weʼsx` | collective plural (people) | `txãweʼsx` "ellos" |

### 4.4 Lexeme classes

GDB classifies lexemes by both formal traits (what morphemes they accept) and semantic content:

| Code | Class | Defining trait | Example |
|---|---|---|---|
| **N** | Nominal | accepts case suffixes; predicates with PE | `nasa` "persona", `yat` "casa", `çxhab` "pueblo" |
| **V (LV)** | Verbal | accepts aspect + MPN; predicates with PD | `weʼwe-` "hablar", `mji-` "trabajar", `umu-` "tejer" |
| **VN** | Verbonominal | can take both N and V morphology | `kwehne` "relámpago", `sek` "sol" |
| **Q** | Cualificativo | accepts MPN directly; sometimes derives a V with aspect | `talx` "flaco", `çxihme` "blanco", `zxiçxkwe` "bonito" |

Per the **predicativity criterion** (Cap 4, repeated in Cap 5), **every lexeme of any
of the four classes can take the modopersonal morpheme and predicate directly**.
Nouns predicate without a copula. This is uncommon cross-linguistically and is a
major design pivot for the MT system.

---

## 5. Word classes

GDB 2019 distinguishes:

- **Lexemas** (N, V, VN, Q — see §4.4)
- **Pronouns** — personal + reflexive (§12)
- **Demonstratives** — `na` (proximal), `txã` (distal), `kxã` (distal alt)
- **Spatial deictics** — `ay-`, `ki-`, `txã-`, `kxã-` (combine with INE)
- **Temporal deictics** — `ãçxha` (today), `kusi` (this morning), `uʼnah` (yesterday), `kuskay` (tomorrow), `naʼ` (now)
- **Interrogatives** — `kim` (who), `kĩh` (what), `maa` (how), `maatx` (where), `maaçxa` (when), `kimweʼsx` (who-pl)
- **Quantifiers** — indefinite (`jxuka` "all"), numerals (`teeçx` 1, `ẽene` 2, `tekh` 3, `phaaza` 4, `tahç` 5)
- **Connectors** — `maa` (adversative), `iʼpa` (disjunctive), `vxitku` (consecutive)
- **Negation** — `me` (free) / `-me-` (bound)

---

## 6. Predication and the modal-personal morpheme

The single most important syntactic concept. **All predication is marked by a
clause-final modal-personal suffix on the predicate word** (modopersonal, MPN).

### 6.1 Two types of predication

| Type | Code | What it relates | Example |
|---|---|---|---|
| **Estativa** | PE | entity ↔ property/state | `Mlxiaʼ zxiçxkweʼ` "María es bonita" |
| **Dinámica**  | PD | entity ↔ event | `txã jibaʼ sena wuwuk` "ese caballo corre mucho" |

### 6.2 The modal-personal morpheme inventory

The MPN slot fuses **mode + person + number + predication type** in one morph.

#### Modes (15 documented)

| Code | Mode |
|---|---|
| ASER | Asertivo (default declarative) |
| INTE | Interrogativo |
| SUS  | Suspensivo (uncertainty/inference) |
| IMP  | Imperativo |
| EXH  | Exhortativo (1pl inclusive command) |
| PROH | Prohibitivo |
| INCI | Incitativo |
| INCER | Incertidumbre |
| CONF | Confirmado |
| CORR | Corroborativo |
| HIP  | Hipotético |
| DES  | Desiderativo |
| VOL  | Volitivo |
| ENF  | Enfático |
| REST | Restrictivo |

Plus person/number labels `1ps 2ps 3ps 1pp 2pp 3pp` and predication tag `.PE` / `.PD`.

Example: `3psASER.PE` = 3rd singular assertive estative; `1psINTE` = 1st singular interrogative.

#### Core ASER / SUS / INTE paradigm (Tabla 9 + Tabla 13, vision-verified)

| Persona | Asertivo | Suspensivo | Interrogativo |
|---|---|---|---|
| 1sg | `-thu`         | `-tka`        | `-nja`        |
| 2sg | `-gu`          | `-ga`         | `-gaʼ`        |
| 3sg PE | `-aʼ`       | `-na`         | `-naʼ`        |
| 3sg PD | `-ku`       | `-ka`         | `-kaʼ`        |
| 1pl | `-thaʼw`       | `-tkhaʼw`     | `-njaʼw`      |
| 2pl | `-iʼkwe`       | `-kwe`        | `-kweʼ`       |
| 3pl PE | `-ta`       | `-txina`      | `-txinaʼ`     |
| 3pl PD | `-tx`       | `-txna`       | `-txnaʼ`      |

Tabla 9 fuses the 3rd-person rows; Tabla 13 (p. 107) disambiguates them by PE/PD.
**For the MT system, encode Tabla 13 as the canonical paradigm.** The Tabla 9
collapsed form is useful for parsing under-disambiguated input.

> **Discrepancy resolved**: Tabla 9 lists `-txna` for "3pl suspensive" while Tabla 13
> distinguishes `-txina` (PE) from `-txna` (PD). Both surface forms exist; the difference
> is the predication type cued by the rest of the predicate complex.

### 6.3 Aspect-driven PE/PD selection

> *"Cuando está ausente la categoría gramatical de aspecto, el predicado es siempre
> estativo. Cuando está presente la categoría de aspecto, puede ser estativo o
> dinámico, dependiendo de la combinatoria de morfemas que contenga la palabra
> predicativa."* (Cap 4b)

**Rule PRED-001**: if the predicate has no aspect suffix → force estative.
**Rule PRED-002**: if aspect is present, decide PE vs PD from the surface MPN form (use Tabla 13).

### 6.4 Estative predicates *with* aspect

Estative predication is compatible with aspect when the aspect is **NEG, D3, INT, PROS or INM**:

- `waʼkx-ø-me-aʼ` "no mordió" (V-AOR-NEG-3psASER.PE)
- `puuç-ø-ne-na` "como que le dio de comer allá lejos" (V-AOR-D3-3psSUS.PE)
- `lem-u-ç-aʼ` "se está amarilleando" (V-IMPF-INT-3psASER.PE)
- `wete-ø-yãwa-aʼ` "se va a caer" (V-AOR-PROS-3psASER.PE)
- `mji-ø-yãwayã-aʼ` "ya no va a trabajar" (V-AOR-INM-3psASER.PE)

### 6.5 Stative-verb / aspect interaction

> *"Los verbos estativos se combinan con la predicación estativa cuando van con el
> aoristo, lo que da un valor temporal de presente, y con la predicación dinámica
> cuando van con el imperfectivo, lo que da un valor temporal de pasado."* (Cap 4b)

| Stative verb + aspect | Surface MPN | Tense |
|---|---|---|
| `ji'ph-` + AOR + PE  | `ji'ph-ø-aʼ` "tiene"    | present |
| `ji'ph-` + IMPF + PD | `ji'ph-u-ku` "tuvo"     | past |

### 6.6 Periphrastic predicates

Some predicates are auxiliary + main verb. The auxiliaries are positional verbs
(`ũs-` "estar de pie / ubicado", `uʼp-` "estar sentado"):

- `fxiʼ-nxi ũs-ø-aʼ` "está escrito" (V-RES + AUX-AOR-3psASER.PE)
- `pud-na uʼp-ø-aʼ` "está hilando sentada" (V-DUR + AUX-AOR-3psASER.PE)

---

## 7. Argument structure and case

### 7.1 Syntactic functions

GDB Cap 4b: nuclear `predicado` + `sujeto` + `objeto directo (OD)` + `objeto
indirecto (OI)` + circunstanciales (locativo, temporal, sociativo, instrumental,
benefactivo, …).

### 7.2 Verbal valence

- **Valencia 1**: subject only
- **Valencia 2**: subject + OD
- **Valencia 3**: subject + OD + OI
- Locative verbs additionally select a location argument
- Anything not selected by the verb = **adjunto**

### 7.3 Direct-object morphology

| Suffix | Function | Number |
|---|---|---|
| `{-aʼs}`   | OBJ (acusativo-dativo) | sg |
| `{-txiʼs}` | OBJpl                  | pl |

**Rule ARG-001**: when both OD and OI co-occur in a clause, **only the indirect
object is marked**; the direct object goes unmarked.

`Tmiguʼ yaʼja uʼkwe-aʼs pesku` "Domingo me regaló una mochila"

**Rule ARG-002**: When the OD is contextually unambiguous, it can appear without
any case marking. `luuçxaʼ çxaju ũʼek` "el niño come piña" (`çxaju` = bare OD).

### 7.4 Locative case

| Suffix | Function | Axis |
|---|---|---|
| `{-te}`  | INE generic / vertical body-axis | — |
| `{-ka}`  | INE | — |
| `{-su}`  | INE / "por" | — |
| `{-khe}` | INE | — |
| `{-na}`  | ALA (motion to) | — |
| `{-ju}`  | ELA (motion from) | — |

GDB also notes finer-grained body-axis inessives:
**INE** (vertical/generic) / **INEh** (horizontal) / **INEi** (slightly inclined) /
**INEp** (steep slope). These are sub-codes in interlinear glosses; their precise
phonetic exponents are dialect-conditioned.

### 7.5 Circumstantial case

| Suffix | Function | Code |
|---|---|---|
| `{-ji}`   | benefactivo  | BEN  |
| `{-yakh}` | sociativo / comitativo | SOC  |
| `{-uh}`   | instrumental | INS  |
| `{-va}`   | aditivo "también / y" | ADI |
| `{-pcach}`   | extensión / terminus "hasta" | (extent) |
| `{-pcachja}` | duración "mientras, durante" | (duration) |
| `{-cjẽ}`     | abajo (spatial) | (spatial) |
| `{-thẽʼj}`   | similativo "como" | SIMI |

Example: `çxiçx-aʼs çxilx-uh waka-ø-thu` "corté la carne con el cuchillo"

---

## 8. Aspect

| Code | Aspect | Form |
|---|---|---|
| AOR  | Aoristo                   | `{-ø}` (null) |
| IMPF | Imperfectivo              | `{-u}` / `{-i}` / `{-e}` (allomorphs by stem) |
| INCO | Aspecto incoativo         | (form per stem) |
| RES  | Aspecto resultativo       | `{-nxi}` |
| DUR  | Aspecto durativo          | `{-na}` |
| ITE  | Aspecto iterativo         | (form) |
| INT  | Aspecto interno (interior)| `{-ç}` |
| EXT  | Aspecto externo           | `{-yã}` |
| PROS | Aspecto prospectivo       | `{-yãwa}` |
| INM  | Aspecto inminente         | `{-yãwayã}` |

The aspect + lexeme-class combination determines whether the predication is
estative or dynamic (see §6.3-6.5).

---

## 9. Information structure: topicalisation and focalisation

### 9.1 Topicalisation `{-aʼ}` (TOP)

Marker on the constituent presented as the topic. Almost always sentence-initial.

- `Peklu-aʼ kãse-ø-ki-ku` "Pedro descansó" (subject topicalised)
- `uʼnah-aʼ çxhab-te ũs-u-thu` "ayer estuve en el pueblo" (time topicalised)

Has an allophonic long form after stressed syllables (`kusi-aʼ`, not `*kus-aʼ`).
Frequently — but not always — coincides with the subject. Temporal circumstantials
are particularly often topicalised.

### 9.2 Focalisation

Formal procedure: **move the modopersonal + distance morphemes off the predicate
and onto the focused constituent**.

| Configuration | Glossed example |
|---|---|
| No focus       | `misx-aʼ Karlus-aʼs waʼkx-ø-ku-ku` "el gato mordió a Carlos" |
| Subject focus  | `misx-ku-ku Karlus-aʼs waʼkx-ø` "fue el gato quien mordió a Carlos" |
| Object focus   | `misx-aʼ Karlus-aʼs-ku-ku waʼkx-ø` "fue a Carlos a quien el gato mordió" |
| Locative focus | `yat-te-ku-ku misx-aʼ Karlus-aʼs waʼkx-ø` "fue en la casa donde el gato mordió a Carlos" |
| Temporal focus | `saptu-ku-ku misx-aʼ Karlus-aʼs waʼkx-ø` "fue el sábado cuando el gato mordió a Carlos" |

**Detection rule INFO-001**: a modal-personal suffix on a non-verbal constituent ⇒
that constituent is in focus.

---

## 10. Voice

| Voice | Subject = | Marker |
|---|---|---|
| **Activa** | agent | (default; no morpheme) |
| **Media**  | patient | reflexive prefix `yaʼ-` |

Voice-media construction: `yaʼ-` + verb. The patient is promoted to subject;
the agent is suppressed.

- `kla-aʼ yaʼ-yaçkipu-ø-tx` "las vacas se dejaron arrear" (REF-V-AOR-3pp)
- `misx-aʼ yaʼ-ukawakx-i-ku` "la gata se deja empujar"
- `agx-aʼ yaʼ-waʼkx-ø-ku-thu` "yo me mordí" (also true reflexive)

The prefix `yaʼ-` is also the morpheme used for true reflexives and reciprocals;
sense is resolved by context and number agreement.

---

## 11. Deixis: person, space, time

GDB Cap 6 covers this domain in detail. Three deictic categories: persona, espacio, tiempo.

### 11.1 Person

Three persons × two numbers, with gender contrast **in 1st and 2nd singular only**.
The 3rd person reuses the distal demonstrative `txã / kxã` — atypical
cross-linguistically. See §12 for the full table.

### 11.2 Spatial deixis

Built compositionally from **two or three morphemes** — a deictic base + a locative case:

- `ay-te-aʼ` "es aquí" (cerca + INE + 3psASER.PE)
- Bases attested: `ay-`, `ki-`, distal `txã-`, distal-distal `kxã-`, interrogative `kĩh-` ("¿dónde?")

Distance markers (D1, D2, D3) appear inside the verbal complex too:
- `-ki-` D1 proximal (speaker sphere)
- `-ku-` D2 medial
- `-ne-` D3 distal

Example: `Peklu-aʼ kãse-ø-ki-ku` (Pedro-TOP/descansar-AOR-D1-3psASER.PD) — the event
is presented as occurring in the speaker's deictic sphere.

### 11.3 Temporal deixis

Free morphemes:

| Form | Meaning |
|---|---|
| `ãçxha` | hoy |
| `kusi`  | esta mañana |
| `uʼnah` | ayer |
| `kuskay`| mañana |
| `naʼ`   | ahora |

Temporal expressions are normally topicalised (`-aʼ`) and sentence-initial.

---

## 12. Pronouns and possessives

### 12.1 Personal pronouns (Tabla 8, vision-verified)

| Persona | Género | Singular | Plural |
|---|---|---|---|
| 1 | M | `adx` / `agx`  | `kweʼsx`     |
| 1 | F | `uʼkwe`        | `kweʼsx`     |
| 2 | M | `idx` / `igx`  | `iʼkweʼsx`   |
| 2 | F | `iʼkwe`        | `iʼkweʼsx`   |
| 3 | neutro | `txã` / `kxã` | `txãweʼsx` / `kxãweʼsx` |

Slash forms = dialectal/register variants. Gender contrast only in singular 1 and 2.

### 12.2 Possessive determiners (Tabla 14, vision-verified)

Identical to personal pronouns **except** for 3rd person, which adds the benefactive
`{-ji}` to disambiguate from the homophonous demonstrative:

| Persona | Singular | Plural |
|---|---|---|
| 1 M | `adx` / `agx`        | `kweʼsx`     |
| 1 F | `uʼkwe`              | `kweʼsx`     |
| 2 M | `idx` / `igx`        | `iʼkweʼsx`   |
| 2 F | `iʼkwe`              | `iʼkweʼsx`   |
| 3   | `txã-ji` / `kxã-ji`  | `txãweʼsx` / `kxãweʼsx` |

### 12.3 Reflexive / reciprocal

Prefix `yaʼ-` on the verb (see §10). Plural agreement marks reciprocal:

- `agx-aʼ yaʼ-waʼkx-ø-ku-thu` "yo me mordí" (reflexive)
- `kweʼsx-aʼ yaʼ-waʼkx-thaʼw` "nos mordimos mutuamente" (reciprocal — plural)

---

## 13. Negation, interrogation, modality

### 13.1 Negation

Morpheme `{-me-}` (NEG) appears in the predicate between aspect and modopersonal:

- `waʼkx-ø-me-aʼ` "no mordió" (V-AOR-NEG-3psASER.PE)
- `igx-aʼ kuskay-aʼ mji-i-me-ne-gaʼ` "¿no trabajarás mañana?" (you-TOP/tomorrow-TOP/V-IMPF-NEG-D3-2psINTE)

Free standalone negative: `me` "no".

### 13.2 Interrogation

**Total/yes-no question**: INTE modopersonal on the predicate, no question word.
- `talx-naʼ` "¿es flaco?" (Q-3psINTE.PE)
- `mji-i-me-ne-gaʼ` "¿no trabajará?" (V-IMPF-NEG-D3-2psINTE)

**Partial/WH question**: WH word + INTE modopersonal. The WH word is a separate
constituent; the question marker is still on the predicate.
- `kim-naʼ` "¿quién es?" (who-3psINTE.PE)
- `kim nasa-naʼ` "¿quién es paez?"
- `kĩh-naʼ` "¿qué es?"
- `maa-naʼ` "¿cómo es?"

WH inventory:

| Form | Meaning |
|---|---|
| `kim`     | quién (sg) |
| `kimweʼsx`| quiénes (pl) |
| `kĩh`     | qué |
| `maa`     | cómo (also = adversative "pero" as a connector) |
| `maatx`   | dónde |
| `maaçxa`  | cuándo |

### 13.3 Imperatives and other moods

| Mood | Marker | Example |
|---|---|---|
| IMP 2sg     | `-k`                      | `ah-k` "¡cocina!" |
| IMP.pl 2pl  | `-weʼ`                    | `ah-weʼ` "¡cocinen!" |
| PROH        | `-me-` + IMP              | `ah-me-k` "¡no cocines!" |
| EXH (1pl)   | `-nxa`                    | `ah-nxa` "cocinemos" |
| HIP         | `-yaʼ-` + ku/ka set       | `mji-yaʼ-ku` "si trabajara" |
| Specific finer-grained modes (DES, VOL, CONF, CORR, …) | (form per Cap 5) | (under-documented in the printed paradigm tables) |

---

## 14. Sentence types and complex clauses

GDB Capítulo 5 (pp. 113-145).

### 14.1 Sentence typology

GDB classifies clauses on two axes:

**By speaker formulation (modalidad)**:
- Declarativas
  - Asertivas (ASER) — propiamente asertivas + suspensivas (SUS)
  - No asertivas — interrogativas totales + interrogativas parciales
- No declarativas — imperatives, exhortatives, etc.

All declaratives can additionally be **negativas**.

**By structural complexity**:
- Simples — one predicate nucleus
- Compuestas — multiple simple clauses joined
  - Yuxtapuestas (no morpheme)
  - Coordinadas (with a connector: adversativa, disyuntiva, consecutiva)
- Complejas — joined by subordinación

### 14.2 Word-sentence

A single predicative word can constitute a complete sentence — the lexeme is the
predicate and the MPN supplies the actantial index.

- `waʼkx-ku` "(él/ella) mordió" — complete sentence (V-AOR-3psASER.PD; subject implicit)

### 14.3 Predicates without aspect — all four lexeme types

| Lexeme class | Example | Gloss |
|---|---|---|
| Nominal       | `nasa-aʼ`          | "es paez" (N-3psASER.PE) |
| Verbonominal  | `kwehne-na`        | "como que es relámpago" (VN-3psSUS.PE) |
| Cualificativo | `talx-naʼ`         | "¿es flaco?" (Q-3psINTE.PE) |
| V nominalizado| `ka-piya-sa-aʼ`    | "es profesor" (FACT-aprender-NOM-3psASER.PE) |

Same construction with free grammemes (DEM, deictics, interrogatives, quantifiers):

| Type | Example | Gloss |
|---|---|---|
| Demonstrative  | `na-aʼ`        | "es este"     (DEM1-3psASER.PE) |
| Spatial deictic| `ay-te-aʼ`     | "es aquí"     (cerca-INE-3psASER.PE) |
| Temporal       | `ãçxh-aʼ`      | "es hoy"      (hoy-3psASER.PE) |
| Interrogative  | `kim-naʼ`      | "¿quién es?"  (quién-3psINTE.PE) |
| Quantifier     | `tekh-ta`      | "son tres"    (tres-3ppASER.PE) |
| Negation       | `me-aʼ`        | "(es) no"     (NEG-3psASER.PE) |

### 14.4 Predicates with aspect — dynamic and estative

Examples already given in §6.4-6.5.

### 14.5 Compound clauses

| Type | Structure | Example |
|---|---|---|
| Yuxtaposición | `Clause1 / Clause2` (each has its own MPN) | `adxaʼ uʼjuthu / igxaʼ kãsegu` "yo me fui; tú descansaste" |
| Adversativa | `Clause1 maa Clause2` | `adxaʼ uʼjuthu maa igxaʼ kãsegu` "yo me fui pero tú descansaste" |
| Disyuntiva  | `Clause1 iʼpa Clause2` | `adxaʼ uʼjuthu iʼpa igxaʼ kãsegu` "yo me fui o tú descansaste" |
| Consecutiva | `Clause1 vxitku Clause2` | `adxaʼ uʼjuthu vxitku igxaʼ kãsegu` "yo me fui entonces tú descansaste" |

### 14.6 Complex clauses (subordinación)

Two cross-cutting parameters:

- **Same-subject (IS) / different-subject (DS)** — switch reference marking on the subordinated verb
- **Semantic relation** — temporal, condicional, hipotética, concesiva, causal, final, relativa

| Code | Function | Form |
|---|---|---|
| ANT.IS | anterioridad mismo sujeto       | `-xpe`      |
| ANT.DS | anterioridad diferente sujeto   | `-xpena`    |
| CONC.IS | concesivo mismo sujeto         | `-yãkpe`    |
| CONC.DS | concesivo diferente sujeto     | `-yãna`     |
| FIN.G | finalidad general                | `-yãwa` (homophonous w/ prospective aspect) |
| FIN.E | finalidad específica             | `-jiyu`     |

Hypothetical conditional uses `-yaʼ-` followed by a ku/ka MPN cell:
- `mji-yaʼ-ku-ʼ uʼj-e-ç-tsxa` "si trabajara me iría"

### 14.7 Relative clauses

**Adnominal relatives** modify a head noun. The relativised verb is nominalised
with `-sa`:

- `uy zxiçxkwe-sa ah-ø-ku-ku` "la mujer que es bonita cocinó"

**Nominal relatives** can themselves function as subject, OD, OI or attribute:

- `mji-sa-weʼsx ũʼ-a ew-aʼ` "la comida de los que trabajan es buena"
  (V-NOM-COL = "los trabajadores"; functions as possessor of "comida")

---

## 15. Dialectology

From GDB Generalidades (Nieves 1995 proposal):

| Zone | Resguardos |
|---|---|
| **Norte**    | Munchique-Los Tigres, Huellas, Toribío, San Francisco, Tacueyó |
| **Centro A** | Jambaló, Pitayó |
| **Centro B** | Caldono, Pioyá, Pueblo Nuevo |
| **Sur**      | Novirao, Paniquitá |
| **Tierradentro** | (large area; further subdivision needed) |
| **Adiciones posteriores** | Quichaya (Centro), Jebalá (Sur) |

Speakers in Tolima, Huila, Valle del Cauca, Putumayo, Caquetá remain undocumented.

**Phonological consequences:**
- North (Munchique-Tigres, Toribío) → reduced 34-vowel system, no length contrast
- Tierradentro, Paniquitá, Caldono-Pueblo Nuevo → full 37-consonant inventory
- Toribío → different syllable structure (no clusters)

**Implementation:** if your training data has dialect tags, **keep them and condition
the model on them**. A model trained on mixed dialects without tagging will produce
inconsistent output.

---

## 16. Full morpheme / abbreviation inventory

The full machine-readable list is in `morpheme_inventory.csv` (≈ 115 entries after
extension). What follows is the **gloss code legend** plus the high-frequency
suffixes used across the literature.

### 16.1 Mode and predication

| Code | Meaning |
|---|---|
| ASER | Modo asertivo |
| INTE | Modo interrogativo |
| SUS  | Modo suspensivo |
| IMP  | Imperativo (sg) |
| IMP.pl | Imperativo plural |
| EXH  | Exhortativo |
| PROH | Prohibitivo |
| INCI | Incitativo |
| INCER | Incertidumbre |
| CONF | Confirmado |
| CORR | Corroborativo |
| HIP  | Hipotético |
| DES  | Desiderativo |
| VOL  | Volitivo |
| ENF  | Enfático |
| REST | Restrictivo |
| PD   | Predicación dinámica |
| PE   | Predicación estativa |

### 16.2 Aspect

| Code | Meaning |
|---|---|
| AOR  | Aspecto aoristo |
| IMPF | Imperfectivo |
| INCO | Aspecto incoativo |
| RES  | Aspecto resultativo |
| DUR  | Aspecto durativo |
| ITE  | Aspecto iterativo |
| INT  | Aspecto interno |
| EXT  | Aspecto externo |
| PROS | Aspecto prospectivo |
| INM  | Aspecto inminente |

### 16.3 Case / locative

| Code | Meaning |
|---|---|
| OBJ    | Objeto (acusativo/dativo) |
| OBJpl  | Objeto plural |
| TOP    | Topicalizador |
| INE    | Inesivo (generic / vertical body-axis) |
| INEh   | Inesivo (horizontal body-axis) |
| INEi   | Inesivo (slightly inclined) |
| INEp   | Inesivo (steep slope) |
| ALA    | Alativo |
| ELA    | Elativo |
| BEN    | Benefactivo |
| SOC    | Sociativo |
| INS    | Instrumental |
| ADI    | Aditivo |
| SIMI   | Similativo |

### 16.4 Derivation / valence

| Code | Meaning |
|---|---|
| NOM  | Nominalizador |
| CAUS | Causativo |
| FACT | Factitivo |
| DIN  | Dinamizador |
| REF  | Reflexivo / media |
| RECI | Recíproco |
| NEG  | Negación |
| COL  | Colectivo plural |
| DIM  | Diminutivo |

### 16.5 Subordination & connectors

| Code | Meaning |
|---|---|
| ANT.IS | Anterioridad mismo sujeto |
| ANT.DS | Anterioridad distinto sujeto |
| CONC.IS | Concesivo mismo sujeto |
| CONC.DS | Concesivo distinto sujeto |
| FIN.G  | Finalidad general |
| FIN.E  | Finalidad específica |
| C      | Conector libre |
| CM     | Caso morfológico |

### 16.6 Deictic / functional

| Code | Meaning |
|---|---|
| D       | Deíctico |
| D1 / D2 / D3 | Distancia proximal / medial / distal |
| DEM1 / DEM2 | Demostrativo proximal / distal |
| FUT     | Futuro |
| MPN     | Modo.persona.número (fused modal-personal slot) |

### 16.7 Lexeme class

| Code | Meaning |
|---|---|
| N    | Nominal |
| V    | Verbo |
| VN   | Verbonominal |
| LV   | Lexema verbal |
| Q    | Cualificativo |

### 16.8 Person / number

| Code | Meaning |
|---|---|
| 1ps  | 1ª persona singular |
| 2ps  | 2ª persona singular |
| 3ps  | 3ª persona singular |
| 1pp  | 1ª persona plural |
| 2pp  | 2ª persona plural |
| 3pp  | 3ª persona plural |
| DS   | Distinto sujeto |

### 16.9 Confirmed surface suffixes — quick reference

| Suffix | Function | Spanish |
|---|---|---|
| `{-aʼ}`     | TOP                       | (n/a — functional) |
| `{-aʼs}`    | OBJ singular              | (n/a) |
| `{-txiʼs}`  | OBJ plural                | (n/a) |
| `{-te}`     | INE generic               | "en" |
| `{-ka}`     | INE                       | "en" |
| `{-su}`     | INE / "por"               | "por", "en" |
| `{-khe}`    | INE                       | "en" |
| `{-na}`     | ALA / DUR                 | "a, hacia" / durativo |
| `{-ju}`     | ELA                       | "de, desde" |
| `{-ji}`     | BEN                       | "para" |
| `{-yakh}`   | SOC                       | "con" |
| `{-uh}`     | INS                       | "con (instrumento)" |
| `{-va}`     | ADI                       | "también, y" |
| `{-pcach}`  | extensión                 | "hasta" |
| `{-pcachja}`| duración                  | "mientras, durante" |
| `{-cjẽ}`    | spatial                   | "abajo" |
| `{-thẽʼj}`  | SIMI                      | "como" |
| `{-tx}`     | plural (nominal)          | (number) |
| `{-weʼsx}`  | colectivo plural          | "los, las (gente)" |
| `{-ø}`      | AOR                       | (zero morph) |
| `{-u}` `{-i}` `{-e}` | IMPF (allomorphs) | (aspect) |
| `{-nxi}`    | RES                       | (aspect) |
| `{-na}`     | DUR (same surface as ALA) | (aspect) |
| `{-ç}`      | INT                       | (aspect) |
| `{-yã}`     | EXT                       | (aspect) |
| `{-yãwa}`   | PROS / FIN.G              | (aspect / purpose) |
| `{-yãwayã}` | INM                       | (aspect) |
| `{-me-}`    | NEG                       | "no" |
| `{-ki-}`    | D1 proximal               | (deictic) |
| `{-ku-}`    | D2 medial                 | (deictic) |
| `{-ne-}`    | D3 distal                 | (deictic) |
| `{yaʼ-}`    | REF / RECI (prefix)       | reflexive / middle / reciprocal |
| `{ka-}`     | FACT (prefix)             | factitivo |
| `{-sa}`     | NOM                       | "el que V" |
| `{-yuu-}`   | DIN                       | "volverse N" |
| `{-k}`      | IMP 2sg                   | "¡V!" |
| `{-weʼ}`    | IMP.pl                    | "¡Vd!" |
| `{-nxa}`    | EXH 1pl                   | "Vmos" |
| `{-yaʼ-}`   | HIP base                  | "si V" |
| `{-xpe}` / `{-xpena}` | ANT.IS / ANT.DS | "después de V" |
| `{-yãkpe}` / `{-yãna}` | CONC.IS / CONC.DS | "aunque V" |
| `{-jiyu}`   | FIN.E                     | "para que V" |

---

## 17. Open rule-set items

Items still needing source-side work:

| Item | Where to find it | Status |
|---|---|---|
| Full conjugation paradigms for ~20 high-frequency verbs (every mode × person × number cell) | Slocum 1986 ch. 3-5 (image-only — OCR needed) | Pending |
| Finer modes (DES, VOL, CONF, CORR, ENF, REST, INCER) — surface MPN forms per cell | GDB Cap 5 + Cap 4 (some not enumerated in printed tables) | Partial — needs targeted re-scan of pp. 105-115 |
| Full IMPF allomorph trigger rules (`-u` / `-i` / `-e`) | GDB Cap 2 §morfofonología (extracted but needs human review) | Partial |
| Full inventory of switch-reference morphemes by aspect | GDB Cap 5 §subordinación + Slocum ch. on complex clauses | Partial — extracted forms in `morpheme_inventory.csv` need cross-check |
| Numeral system above 5 + classifiers if any | Slocum 1986 + `Kwesxyuwe_Los_numeros_NY.pdf` | Pending |
| INE sub-axis suffixes (INEh, INEi, INEp) — surface forms | GDB Cap 2 + Cap 4 (referenced but forms not enumerated in our scan) | Pending |
| Causative `{-tx-}` productivity & restrictions | GDB Cap 3 derivation section | Partial |
| Reciprocal disambiguation rule (vs. reflexive) | GDB Cap 5 + Slocum | Partial |
| Sound change rules across dialects (Pitayó, Caldono, Munchique, Tierradentro) | Díaz Montenegro 2019 (Munchique only); LIAMES sound-change paper for others | Partial |

---

## 18. Implementation guidance for the hybrid MT model

A practical roadmap drawing on §§ 1-17.

### 18.1 Preprocessing pipeline (do this first)

1. **Orthography normaliser** — bidirectional rule table from `orthography_map.csv`.
   Handles: `c'h ↔ çx`, `ñ ↔ nx`, `ll ↔ lx`, `sh ↔ sx`, `ts ↔ ç`, `mb ↔ b`, etc.
   Also normalise apostrophes (`'` ↔ `ʼ`) and combining tildes.
2. **Tokeniser** — Nasa Yuwe is space-separated at the word level; respect the
   apostrophe as part of glottalised vowels (don't split on it).
3. **Morphological segmenter** — initial pass with a deterministic suffix-stripping
   automaton driven by `morpheme_inventory.csv`. Order matters: MPN first (rightmost),
   then NEG/D1-D3, then aspect, then case, then plural.

### 18.2 Predication classifier

A small state machine over each predicate word:

```
predicate_word := (yaʼ-)? STEM (ASP)? (NEG)? (D1|D2|D3)? MPN
```

with these decisions:

- `MPN.PE` vs `MPN.PD` → use Tabla 13 (§6.2)
- no aspect → force PE
- aspect present and aspect ∈ {NEG, D3, INT, PROS, INM} → can still be PE
- aspect ∈ {AOR, IMPF, IMPFu, DUR, RES, …} + dynamic MPN → PD

### 18.3 Lexicon

- Use `master_vocabulary_pbb.csv` filtered to `n_sources >= 2` for the rule-based
  fallback dictionary (~4,000 trusted entries).
- For OOV: fall back to subword statistical translation (NLLB or m2m100 fine-tuned).

### 18.4 The 2nd-person gender rule

The 2sg pronoun differs by **addressee gender** (`idx/igx` for male addressee,
`iʼkwe` for female addressee), as does any 2sg agreement morphology. A vanilla MT
model will hallucinate. **Carry addressee gender as a tag** in your sentence
metadata; condition the output on it.

### 18.5 Encoding the MPN as a state machine

The MPN slot is a fused mode × person × number × predication-type cell. A trie of
`(surface form → {mode, person, number, predication})` lookups using Tabla 13 as
the canonical paradigm is the cleanest implementation.

### 18.6 Focalisation detection

When a non-verbal constituent carries a modopersonal morpheme, that constituent is
focused. The bare predicate that follows is a participle-like AOR form. Flag the
configuration and gloss as cleft.

### 18.7 Sentence-type pipeline

Classify the input clause as:
1. **Word-sentence** → single MPN-bearing word
2. **Simple** → one predicate nucleus
3. **Compound** → multiple clauses joined by `maa` / `iʼpa` / `vxitku` or by yuxtaposition
4. **Complex** → contains a subordinated verb with switch-reference morphology, NOM relative, or HIP/FIN/CONC morpheme

For each, route to a separate generator template (templates enumerated in `predication_templates.csv`).

### 18.8 Dialect conditioning

If a training example has a dialect tag, prepend it as a control token
(`<dialect:munchique>`, `<dialect:caldono>`, …). Otherwise default to the
**Tierradentro** maximal inventory and let the model fall back when generating.

---

*Last updated: full-textbook extraction + vision verification pass. Supersedes
`UNIFIED_GRAMMAR_RULES.md.old` (which still flagged Cap 2 and Cap 5 as missing).*
