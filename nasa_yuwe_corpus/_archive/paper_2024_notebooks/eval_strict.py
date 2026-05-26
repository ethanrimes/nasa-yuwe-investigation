"""Strict reproduction of the AmericasNLP 2024 Nasa Yuwe results (Table 2).

Mirrors the released notebook (nllb_nasa_esp_*.ipynb, section 7) line-for-line:
  - transformers==4.33, NllbTokenizer
  - translate() with a=32, b=3, num_beams=4 (no other generate kwargs)
  - one-sentence-at-a-time inference: `[translate(t)[0] for t in df_test[col]]`
  - sacrebleu BLEU() and CHRF(word_order=2)  -- chrF2++
  - test split = released *_test.csv files
"""
import argparse, json, os, time
import pandas as pd
import torch
import sacrebleu
from tqdm import tqdm
from transformers import NllbTokenizer, AutoModelForSeq2SeqLM

LANG_ORIGIN = "spa_Latn"
LANG_TARGET = "nas_Latn"

CONFIGS = [
    ("Nasa All 600M",             "models/nllb_nasa_esp_completo_600M",   "data/nasa_full_dataset_test.csv"),
    ("Nasa All 1.3B",             "models/nllb_nasa_esp_completo_1_3B",   "data/nasa_full_dataset_test.csv"),
    ("Nasa Without Letters 600M", "models/nllb_nasa_esp_sin_cartas_600m", "data/nasa_sin_cartas_test.csv"),
    ("Nasa Without Letters 1.3B", "models/nllb_nasa_esp_sin_cartas_1_3B", "data/nasa_sin_cartas_test.csv"),
]

def fix_tokenizer(tokenizer, new_lang=LANG_TARGET):
    """Verbatim from the released notebook: register the new language token."""
    old_len = len(tokenizer) - int(new_lang in tokenizer.added_tokens_encoder)
    tokenizer.lang_code_to_id[new_lang] = old_len - 1
    tokenizer.id_to_lang_code[old_len - 1] = new_lang
    tokenizer.fairseq_tokens_to_ids["<mask>"] = (
        len(tokenizer.sp_model) + len(tokenizer.lang_code_to_id) + tokenizer.fairseq_offset
    )
    tokenizer.fairseq_tokens_to_ids.update(tokenizer.lang_code_to_id)
    tokenizer.fairseq_ids_to_tokens = {v: k for k, v in tokenizer.fairseq_tokens_to_ids.items()}
    if new_lang not in tokenizer._additional_special_tokens:
        tokenizer._additional_special_tokens.append(new_lang)
    tokenizer.added_tokens_encoder = {}
    tokenizer.added_tokens_decoder = {}

def make_translate(model, tokenizer):
    def translate(text, src_lang=LANG_ORIGIN, tgt_lang=LANG_TARGET,
                  a=32, b=3, max_input_length=1024, num_beams=4, **kwargs):
        tokenizer.src_lang = src_lang
        tokenizer.tgt_lang = tgt_lang
        inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True,
                           max_length=max_input_length)
        result = model.generate(
            **inputs.to(model.device),
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
            max_new_tokens=int(a + b * inputs.input_ids.shape[1]),
            num_beams=num_beams,
            **kwargs,
        )
        return tokenizer.batch_decode(result, skip_special_tokens=True)
    return translate

def run(label, model_path, test_csv, limit=0):
    print(f"\n=== {label} ===  model={model_path}  test={test_csv}", flush=True)
    df = pd.read_csv(test_csv).dropna().reset_index(drop=True)
    if limit:
        df = df.head(limit)
    print(f"  rows: {len(df)}", flush=True)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = NllbTokenizer.from_pretrained(model_path)
    fix_tokenizer(tokenizer)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device).eval()
    translate = make_translate(model, tokenizer)

    t0 = time.time()
    esp_translated = [translate(t, LANG_TARGET, LANG_ORIGIN)[0]
                      for t in tqdm(df["nas"].tolist(), desc="nas->esp")]
    nas_translated = [translate(t, LANG_ORIGIN, LANG_TARGET)[0]
                      for t in tqdm(df["esp"].tolist(), desc="esp->nas")]
    elapsed = time.time() - t0

    bleu = sacrebleu.BLEU()
    chrf = sacrebleu.CHRF(word_order=2)

    refs_esp = [df["esp"].tolist()]
    refs_nas = [df["nas"].tolist()]
    res = {
        "label": label, "n": len(df), "elapsed_s": round(elapsed, 1),
        # Paper columns: Spanish->Target and Target->Spanish
        "spa_to_tgt_bleu": bleu.corpus_score(nas_translated, refs_nas).score,
        "spa_to_tgt_chrf": chrf.corpus_score(nas_translated, refs_nas).score,
        "tgt_to_spa_bleu": bleu.corpus_score(esp_translated, refs_esp).score,
        "tgt_to_spa_chrf": chrf.corpus_score(esp_translated, refs_esp).score,
    }
    print(json.dumps(res, indent=2), flush=True)

    os.makedirs("preds_strict", exist_ok=True)
    df_out = df.copy()
    df_out["nas_pred"] = nas_translated
    df_out["esp_pred"] = esp_translated
    df_out.to_csv(os.path.join("preds_strict", label.replace(" ", "_") + ".csv"), index=False)
    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    configs = [c for c in CONFIGS if args.only.lower() in c[0].lower()]
    print(f"Device: {'cuda' if torch.cuda.is_available() else 'cpu'}", flush=True)
    results = []
    # Save previously completed 600M result if its prediction file exists
    prev = "preds_strict/Nasa_All_600M.csv"
    if os.path.exists(prev) and not any("All 600M" in c[0] for c in configs):
        pass
    for label, mp, tc in configs:
        results.append(run(label, mp, tc, args.limit))
        # incremental save
        try:
            existing = []
            if os.path.exists("results_strict.json"):
                existing = [r for r in json.load(open("results_strict.json")) if r.get("label") != label and r.get("n", 0) >= 100]
            existing.append(results[-1])
            with open("results_strict.json", "w") as f:
                json.dump(existing, f, indent=2)
        except Exception as e:
            print("save warn:", e)
    print("\n\n=== SUMMARY (paper Table 2 columns) ===", flush=True)
    print(f"{'Config':<32}{'spa->tgt BLEU':>15}{'chrF':>9}{'tgt->spa BLEU':>16}{'chrF':>9}")
    for r in results:
        print(f"{r['label']:<32}{r['spa_to_tgt_bleu']:>15.2f}{r['spa_to_tgt_chrf']:>9.2f}"
              f"{r['tgt_to_spa_bleu']:>16.2f}{r['tgt_to_spa_chrf']:>9.2f}")
    with open("results_strict.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
