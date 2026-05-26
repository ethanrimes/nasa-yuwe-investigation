# 10_models_references — Pretrained models on HuggingFace

No models are downloaded to disk here (they're large and HuggingFace hosts them). This file documents the existing publicly available Spanish↔Páez models you can fine-tune on top of instead of training NLLB-200 from scratch.

## All by Carlos D. Escobar-Valbuena (`Broomva`)

These are released alongside the datasets that ended up in `01_parallel_corpora/broomva_*` — same author, same training data.

| Model | Size | Type | URL |
| --- | --- | --- | --- |
| `Broomva/llama-2-7b-chat-instruct-translate-spa-pbb` | 7B params | Llama-2 chat-instruct, finetuned for Spanish→Páez | https://huggingface.co/Broomva/llama-2-7b-chat-instruct-translate-spa-pbb |
| Multiple T5, mT5, BART variants for `spa-pbb` | small–base | seq2seq encoder-decoder | https://huggingface.co/Broomva (filter by `pbb`) |

Plus several models for `spa-guc` (Wayuunaiki, ISO `guc`) that are *not* useful for Nasa Yuwe — different language despite similar collection name.

## What you might use instead

For multilingual transfer:

- **NLLB-200** (`facebook/nllb-200-distilled-600M`, `-1.3B`, `-3.3B`) — the architecture used in the Robles et al. AmericasNLP 2024 paper. Does *not* have Nasa Yuwe in its supported language list; you finetune it with a custom `pbb_Latn` tag.
- **m2m100** (`facebook/m2m100_418M`, `_1.2B`) — recommended by the resource guide as outperforming m2m100-48 alternatives for low-resource indigenous languages.
- **MADLAD-400** (`google/madlad400-*`) — Google's "1000-language" multilingual MT model; covers some Colombian indigenous languages, may have implicit Páez exposure.

## Suggested workflow

1. Pick `Broomva/llama-2-7b-chat-instruct-translate-spa-pbb` as a strong already-finetuned baseline.
2. Re-finetune it (LoRA) on the deduplicated parallel corpus from `01_parallel_corpora/`.
3. Evaluate against the held-out `broomva_translation_pbb_spa_test.parquet` so your numbers are comparable to the published broomva models.
4. Compare against a parallel NLLB-200 1.3B finetune (the AmericasNLP 2024 paper baseline).
