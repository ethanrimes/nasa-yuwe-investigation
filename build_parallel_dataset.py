#!/usr/bin/env python3
"""
Consolidate all Nasa Yuwe ↔ Spanish parallel data into a single
deduplicated JSONL file for ML training.

Output schema per line:
{
  "nasa_yuwe": "...",
  "spanish": "...",
  "source": "bible_nt | living_dict | swarthmore | broomva_translation | broomva_instruct | americasnlp_2024",
  "domain": "religious | lexical | constitutional | mixed",
  "meta": { ... }   # optional source-specific metadata
}
"""

import json
import re
import unicodedata
from pathlib import Path

import pandas as pd

CORPUS = Path(r"Q:\nasa-yuwe-investigation\nasa_yuwe_corpus")
PARALLEL = CORPUS / "01_parallel_corpora"
ARCHIVE = CORPUS / "_archive" / "paper_2024_data_local"
OUT_DIR = Path(r"Q:\nasa-yuwe-investigation")

records: list[dict] = []


def clean(text: str | None) -> str:
    """Strip, collapse whitespace, NFC-normalize."""
    if not isinstance(text, str) or not text.strip():
        return ""
    text = unicodedata.normalize("NFC", text.strip())
    text = re.sub(r"\s+", " ", text)
    return text


def dedup_key(nasa: str, spa: str) -> str:
    """Lowercase + strip punctuation key for dedup."""
    def norm(s):
        s = s.lower().strip()
        s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
        s = re.sub(r"\s+", " ", s).strip()
        return s
    return norm(nasa) + "|||" + norm(spa)


# ── 1. Bible NT (verse-aligned) ─────────────────────────────────────────────
print("Loading Bible NT...")
df = pd.read_csv(PARALLEL / "bible_nt_es_pbb.csv")
for _, row in df.iterrows():
    nasa = clean(row.get("nasa_yuwe"))
    spa = clean(row.get("spanish"))
    if nasa and spa:
        records.append({
            "nasa_yuwe": nasa,
            "spanish": spa,
            "source": "bible_nt",
            "domain": "religious",
            "meta": {
                "book": row.get("book", ""),
                "chapter": int(row["chapter"]) if pd.notna(row.get("chapter")) else None,
                "verse": int(row["verse"]) if pd.notna(row.get("verse")) else None,
            }
        })
print(f"  → {len(records)} pairs")

# ── 2. Living Dictionaries ──────────────────────────────────────────────────
print("Loading Living Dictionaries...")
n_before = len(records)
df = pd.read_csv(PARALLEL / "living_dictionaries_paez.csv")
for _, row in df.iterrows():
    nasa = clean(row.get("nasa_yuwe"))
    spa = clean(row.get("gloss_es"))
    if nasa and spa:
        records.append({
            "nasa_yuwe": nasa,
            "spanish": spa,
            "source": "living_dict",
            "domain": "lexical",
            "meta": {
                "pos": clean(row.get("pos", "")),
                "gloss_en": clean(row.get("gloss_en", "")),
            }
        })
print(f"  → {len(records) - n_before} pairs")

# ── 3. Swarthmore Talking Dictionary (full version) ─────────────────────────
print("Loading Swarthmore Talking Dictionary...")
n_before = len(records)
df = pd.read_csv(PARALLEL / "swarthmore_talking_dictionary_full.csv")
for _, row in df.iterrows():
    nasa = clean(row.get("headword"))
    spa = clean(row.get("gloss"))
    if nasa and spa:
        records.append({
            "nasa_yuwe": nasa,
            "spanish": spa,
            "source": "swarthmore",
            "domain": "lexical",
            "meta": {
                "pos": clean(row.get("part_of_speech", "")),
                "audio_url": clean(row.get("audio_url", "")),
            }
        })
print(f"  → {len(records) - n_before} pairs")

# ── 4. Broomva translation (train + validation + test CSV) ──────────────────
print("Loading Broomva translation splits...")
n_before = len(records)
for split in ["train", "validation", "test"]:
    fpath = PARALLEL / f"broomva_translation_pbb_spa_{split}.csv"
    df = pd.read_csv(fpath)
    for _, row in df.iterrows():
        nasa = clean(row.get("translation.pbb"))
        spa = clean(row.get("translation.spa"))
        if nasa and spa:
            records.append({
                "nasa_yuwe": nasa,
                "spanish": spa,
                "source": "broomva_translation",
                "domain": "lexical",
                "meta": {"split": split}
            })
print(f"  → {len(records) - n_before} pairs")

# ── 5. Broomva instruct parquet (parse [INST]...[/INST] format) ─────────────
print("Loading Broomva instruct parquet...")
n_before = len(records)
df = pd.read_parquet(PARALLEL / "broomva_instruct_spa_pbb_train.parquet")
# Format: <s>[INST] Traduce de Español a Paez: {SPANISH} [/INST] {NASA_YUWE} </s>
pat = re.compile(
    r"\[INST\]\s*Traduce de Español a Paez:\s*(.+?)\s*\[/INST\]\s*(.+?)\s*</s>",
    re.DOTALL,
)
for _, row in df.iterrows():
    text = row.get("text", "")
    m = pat.search(text)
    if m:
        spa = clean(m.group(1))
        nasa = clean(m.group(2))
        if nasa and spa:
            records.append({
                "nasa_yuwe": nasa,
                "spanish": spa,
                "source": "broomva_instruct",
                "domain": "constitutional",
                "meta": {}
            })
print(f"  → {len(records) - n_before} pairs")

# ── 6. AmericasNLP 2024 full dataset (archive) ──────────────────────────────
print("Loading AmericasNLP 2024 archive (nasa_full_dataset.csv)...")
n_before = len(records)
fpath = ARCHIVE / "nasa_full_dataset.csv"
if fpath.exists():
    df = pd.read_csv(fpath)
    for _, row in df.iterrows():
        spa = clean(row.get("esp"))
        nasa = clean(row.get("nas"))
        if nasa and spa:
            records.append({
                "nasa_yuwe": nasa,
                "spanish": spa,
                "source": "americasnlp_2024",
                "domain": "mixed",
                "meta": {}
            })
    print(f"  → {len(records) - n_before} pairs")
else:
    print("  → file not found, skipping")


# ── Deduplication ────────────────────────────────────────────────────────────
print(f"\nTotal raw records: {len(records)}")

# Priority order: prefer richer / higher-quality sources
SOURCE_PRIORITY = {
    "bible_nt": 0,
    "americasnlp_2024": 1,
    "broomva_instruct": 2,
    "broomva_translation": 3,
    "living_dict": 4,
    "swarthmore": 5,
}

seen: dict[str, int] = {}
deduped: list[dict] = []
duplicates_dropped = 0

for i, rec in enumerate(records):
    key = dedup_key(rec["nasa_yuwe"], rec["spanish"])
    if key in seen:
        duplicates_dropped += 1
        # Keep the one with higher priority (lower number)
        existing_idx = seen[key]
        existing_priority = SOURCE_PRIORITY.get(deduped[existing_idx]["source"], 99)
        new_priority = SOURCE_PRIORITY.get(rec["source"], 99)
        if new_priority < existing_priority:
            deduped[existing_idx] = rec
            # seen[key] stays the same index
    else:
        seen[key] = len(deduped)
        deduped.append(rec)

print(f"Duplicates dropped: {duplicates_dropped}")
print(f"Unique pairs after dedup: {len(deduped)}")

# ── Domain statistics ────────────────────────────────────────────────────────
from collections import Counter

source_counts = Counter(r["source"] for r in deduped)
domain_counts = Counter(r["domain"] for r in deduped)

print("\n── By source ──")
for src, cnt in source_counts.most_common():
    print(f"  {src:25s} {cnt:>6,}")

print("\n── By domain ──")
for dom, cnt in domain_counts.most_common():
    print(f"  {dom:25s} {cnt:>6,}")

# ── Write JSONL ──────────────────────────────────────────────────────────────
out_jsonl = OUT_DIR / "nasa_yuwe_parallel_dataset.jsonl"
with open(out_jsonl, "w", encoding="utf-8") as f:
    for rec in deduped:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(f"\n✅ Wrote {len(deduped)} pairs → {out_jsonl}")

# ── Also write a summary JSON ───────────────────────────────────────────────
summary = {
    "total_pairs": len(deduped),
    "raw_before_dedup": len(records),
    "duplicates_dropped": duplicates_dropped,
    "by_source": dict(source_counts.most_common()),
    "by_domain": dict(domain_counts.most_common()),
    "schema": {
        "nasa_yuwe": "Nasa Yuwe (Páez) text — ISO 639-3: pbb",
        "spanish": "Spanish translation/gloss",
        "source": "Dataset origin identifier",
        "domain": "Content domain (religious, lexical, constitutional, mixed)",
        "meta": "Source-specific metadata (book/chapter/verse, POS, split, etc.)"
    },
    "notes": [
        "Bible NT pairs use traditional (1984) orthography aligned by verse with Versión Biblia Libre (Spanish 2018)",
        "Dictionary sources (living_dict, swarthmore, broomva_translation) derive from Gerdel & Slocum 1983",
        "Broomva instruct contains Colombian Constitution articles in Nasa Yuwe",
        "AmericasNLP 2024 is the Robles et al. paper bundle (constitution + dictionary mix)",
        "Deduplication uses lowercased, punctuation-stripped comparison; highest-priority source kept",
    ]
}

out_summary = OUT_DIR / "nasa_yuwe_parallel_dataset_summary.json"
with open(out_summary, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"✅ Wrote summary → {out_summary}")
