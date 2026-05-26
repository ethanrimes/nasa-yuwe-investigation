"""Reproduce paper's Nasa Yuwe results (Table 2).

Loads each of the four fine-tuned models, translates the held-out test split
in both directions, and reports BLEU + chrF2++ via sacrebleu (same metric
configuration as the original notebook).
"""
import argparse, json, os, sys, time
import pandas as pd
import torch
import sacrebleu
from tqdm import tqdm
from transformers import NllbTokenizer, AutoModelForSeq2SeqLM

SRC_LANG = "spa_Latn"
TGT_LANG = "nas_Latn"

CONFIGS = [
    # (label, model_path, test_csv)
    ("Nasa All 600M",            "models/nllb_nasa_esp_completo_600M",   "data/nasa_full_dataset_test.csv"),
    ("Nasa All 1.3B",            "models/nllb_nasa_esp_completo_1_3B",   "data/nasa_full_dataset_test.csv"),
    ("Nasa Without Letters 600M","models/nllb_nasa_esp_sin_cartas_600m", "data/nasa_sin_cartas_test.csv"),
    ("Nasa Without Letters 1.3B","models/nllb_nasa_esp_sin_cartas_1_3B", "data/nasa_sin_cartas_test.csv"),
]

def translate_batch(model, tokenizer, texts, src_lang, tgt_lang, num_beams=4, max_input=1024):
    tokenizer.src_lang = src_lang
    tokenizer.tgt_lang = tgt_lang
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True,
                       max_length=max_input).to(model.device)
    # a=32, b=3 from notebook section 7 -> max_new_tokens scales with input length
    in_len = inputs.input_ids.shape[1]
    max_new = int(32 + 3 * in_len)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
            max_new_tokens=max_new,
            num_beams=num_beams,
            no_repeat_ngram_size=3,
        )
    return tokenizer.batch_decode(out, skip_special_tokens=True)

def run(label, model_path, test_csv, batch_size, limit):
    print(f"\n=== {label} ===")
    print(f"  model: {model_path}")
    print(f"  test : {test_csv}")
    df = pd.read_csv(test_csv).dropna().reset_index(drop=True)
    if limit:
        df = df.head(limit)
    print(f"  rows : {len(df)}")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = NllbTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device).eval()

    def do(src_texts, src_lang, tgt_lang):
        # length-sorted batching (mirrors paper's batched_translate)
        idx = sorted(range(len(src_texts)), key=lambda i: len(str(src_texts[i])))
        sorted_texts = [str(src_texts[i]) for i in idx]
        outs_sorted = []
        for i in tqdm(range(0, len(sorted_texts), batch_size), desc=f"{src_lang}->{tgt_lang}"):
            chunk = sorted_texts[i:i+batch_size]
            outs_sorted.extend(translate_batch(model, tokenizer, chunk, src_lang, tgt_lang))
        outs = [None] * len(src_texts)
        for pos, orig in enumerate(idx):
            outs[orig] = outs_sorted[pos]
        return outs

    t0 = time.time()
    es_to_nas = do(df["esp"].tolist(), SRC_LANG, TGT_LANG)
    nas_to_es = do(df["nas"].tolist(), TGT_LANG, SRC_LANG)
    elapsed = time.time() - t0

    bleu = sacrebleu.BLEU()
    chrf = sacrebleu.CHRF(word_order=2)  # chrF2++

    res = {
        "label": label, "n": len(df), "elapsed_s": round(elapsed, 1),
        "es_to_nas_bleu": bleu.corpus_score(es_to_nas, [df["nas"].tolist()]).score,
        "es_to_nas_chrf": chrf.corpus_score(es_to_nas, [df["nas"].tolist()]).score,
        "nas_to_es_bleu": bleu.corpus_score(nas_to_es, [df["esp"].tolist()]).score,
        "nas_to_es_chrf": chrf.corpus_score(nas_to_es, [df["esp"].tolist()]).score,
    }
    print(json.dumps(res, indent=2))

    # save predictions
    out_dir = "preds"
    os.makedirs(out_dir, exist_ok=True)
    df_out = df.copy()
    df_out["nas_pred"] = es_to_nas
    df_out["esp_pred"] = nas_to_es
    df_out.to_csv(os.path.join(out_dir, label.replace(" ", "_") + ".csv"), index=False)
    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="run only configs whose label contains this substring")
    ap.add_argument("--batch-size", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0, help="limit test rows (debug)")
    args = ap.parse_args()
    configs = [c for c in CONFIGS if (args.only or "").lower() in c[0].lower()]
    print(f"Device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    print(f"Running {len(configs)} config(s)")
    results = []
    for label, mp, tc in configs:
        results.append(run(label, mp, tc, args.batch_size, args.limit))
    print("\n\n=== SUMMARY ===")
    print(f"{'Config':<30}{'es->nas BLEU':>14}{'chrF':>10}{'nas->es BLEU':>14}{'chrF':>10}")
    for r in results:
        print(f"{r['label']:<30}{r['es_to_nas_bleu']:>14.2f}{r['es_to_nas_chrf']:>10.2f}{r['nas_to_es_bleu']:>14.2f}{r['nas_to_es_chrf']:>10.2f}")
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
