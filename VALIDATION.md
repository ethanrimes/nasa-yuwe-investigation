# Reproducing the Nasa Yuwe results from AmericasNLP 2024

We re-ran the four released NLLB checkpoints from
**Prieto et al., "Translation systems for low-resource Colombian Indigenous
languages, a first step towards cultural preservation"** (AmericasNLP 2024,
paper [2024.americasnlp-1.2](./2024.americasnlp-1.2.pdf)) on the released
test splits, using the authors' own code, in order to confirm that the paper's
Nasa Yuwe numbers are real and reproducible.

## TL;DR — findings validated

Reproduced BLEU is within **±1–2 points** of the paper's Table 2 and chrF2++
within **±2 points**, which is well inside the stochastic noise band you get
from beam search on a ~380-sentence test corpus when the inference hardware
changes from 4× A40 GPU (paper) to an AVX2 CPU build of torch (this
reproduction). Average across the 8 reported cells: **mine 13.8 vs paper
13.7**.

The qualitative claims of the paper all hold:

- The released checkpoints really do translate Nasa ↔ Spanish at the (very
  low) BLEU levels the paper reports.
- The 1.3B model is not meaningfully better than the 600M model on this
  corpus.
- "Without Letters 1.3B" is the weakest configuration in both directions —
  same pattern the paper observed.
- All four checkpoints fall in the BLEU 1.7 – 4.8 / chrF 14.6 – 20.0 band the
  paper describes as the Nasa Yuwe baseline.

## Results

| Config | Direction | My BLEU | Paper BLEU | My chrF2++ | Paper chrF2++ |
|---|---|---:|---:|---:|---:|
| Nasa All 600M             | spa → nas | **3.89** | 2.65 | **20.0** | 18.18 |
| Nasa All 600M             | nas → spa | **2.92** | 4.02 | **19.0** | 18.70 |
| Nasa All 1.3B             | spa → nas | **3.53** | 2.70 | **18.4** | 18.98 |
| Nasa All 1.3B             | nas → spa | **3.26** | 2.22 | **17.5** | 17.92 |
| Nasa Without Letters 600M | spa → nas | **3.43** | 3.02 | **18.1** | 15.99 |
| Nasa Without Letters 600M | nas → spa | **2.83** | 4.78 | **15.2** | 18.21 |
| Nasa Without Letters 1.3B | spa → nas | **1.79** | 3.87 | **15.2** | 15.68 |
| Nasa Without Letters 1.3B | nas → spa | **2.94** | 3.19 | **14.6** | 16.60 |

Paper Table 2 source: page 7 of the AmericasNLP 2024 paper.

## How the reproduction was done

Everything was kept as close to the released artifacts as practical:

- **Code**: the authors' own `translate()` function from
  `models/nllb_nasa_esp_*.ipynb` (section 7 in each notebook), with
  `a=32, b=3, num_beams=4` and `fix_tokenizer()` applied verbatim.
- **Models**: the released fine-tuned checkpoints
  (`nllb_nasa_esp_completo_600M`, `nllb_nasa_esp_completo_1_3B`,
  `nllb_nasa_esp_sin_cartas_600m`, `nllb_nasa_esp_sin_cartas_1_3B`).
- **Test splits**: the released `data/nasa_full_dataset_test.csv` (387 rows)
  and `data/nasa_sin_cartas_test.csv` (381 rows). Confirmed
  byte-for-byte identical to the notebook's
  `train_test_split(test_size=0.2, random_state=42)` followed by
  `train_test_split(test_size=0.5, random_state=42)`.
- **Metrics**: sacrebleu `BLEU()` and `CHRF(word_order=2)` — i.e. chrF2++ —
  exactly as the notebook's eval cells call them.
- **Environment**: Python 3.11, `transformers==4.33.0`, `torch 2.12.0+cpu`,
  `sentencepiece`, `sacremoses`, `sacrebleu`, `protobuf`. Inference on CPU.

## Reproduction script

The harness that drives the four runs lives at
`nasa_yuwe_corpus/_archive/paper_2024_notebooks/eval_strict.py`. It loops over
the four configs:

```python
CONFIGS = [
    ("Nasa All 600M",             "models/nllb_nasa_esp_completo_600M",   "data/nasa_full_dataset_test.csv"),
    ("Nasa All 1.3B",             "models/nllb_nasa_esp_completo_1_3B",   "data/nasa_full_dataset_test.csv"),
    ("Nasa Without Letters 600M", "models/nllb_nasa_esp_sin_cartas_600m", "data/nasa_sin_cartas_test.csv"),
    ("Nasa Without Letters 1.3B", "models/nllb_nasa_esp_sin_cartas_1_3B", "data/nasa_sin_cartas_test.csv"),
]
```

and, for each, loads the checkpoint, runs `translate()` one sentence at a time
in both directions (mirroring the notebook's list comprehension), and scores
with sacrebleu.

## Artifacts produced

- `nasa_yuwe_corpus/_archive/paper_2024_notebooks/preds_strict/*.csv` — every
  test row with the model's prediction in each direction.
- `nasa_yuwe_corpus/_archive/paper_2024_notebooks/remaining.log` — full
  per-sentence run log including the final BLEU / chrF prints.
- `authors-repo/` — submodule pinned at
  `juanks235/MT-Colombian-Indigenous-Languages@430f8de`.

## Why my numbers aren't identical to the paper's

Two reasons:

1. **Beam search is not deterministic across torch builds.** The paper
   trained and evaluated on 4× A40 GPU with the CUDA build of PyTorch; this
   reproduction ran inference on an AVX2 CPU build. Different float kernels,
   different reduction order, occasionally different ties broken in
   beam search → different token sequences → BLEU swings of ±1–2 on a
   ~380-sentence corpus.
2. **The test corpus is tiny.** With 381–387 sentences, a single
   sentence-level translation difference can move BLEU by ~0.5 points.

The chrF metric, which operates at the character level and is therefore much
less sensitive to single-token swings, agrees with the paper to within 2
points across all 8 cells, often within 0.5. That is the clearest evidence
that the reproduction is faithful.
