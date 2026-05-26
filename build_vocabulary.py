"""
Build a comprehensive Nasa Yuwe vocabulary list from the parallel dataset.

For each unique Nasa Yuwe word/term, collect:
  - All Spanish translations (from direct dictionary/vocab sources)
  - All sources where the word appears (including sentence-level sources)

Output: nasa_yuwe_vocabulary.jsonl  (one entry per unique term)
        nasa_yuwe_vocabulary_summary.json
"""
import json, re, unicodedata
from collections import defaultdict

DATASET = "nasa_yuwe_parallel_dataset.jsonl"
OUT_VOCAB = "nasa_yuwe_vocabulary.jsonl"
OUT_SUMMARY = "nasa_yuwe_vocabulary_summary.json"

# Sources where nasa_yuwe field is a word/phrase (direct translation)
DIRECT_SOURCES = {
    "living_dict", "broomva_translation", "kwesxyuwe_thematic", "swarthmore"
}
# Sources where nasa_yuwe field is a sentence (need tokenisation)
SENTENCE_SOURCES = {
    "bible_nt", "broomva_instruct", "americasnlp_2024",
    "territorios_narrados", "adres_health", "procuraduria_institutional"
}

# Some nominally direct sources contain full sentence/article translations.
# Keep those as token evidence only; otherwise entire constitutional articles
# become vocabulary headwords.
MAX_DIRECT_NASA_CHARS = 120
MAX_DIRECT_SPANISH_CHARS = 250

def normalise(word):
    """Lowercase + NFC normalise a single word."""
    return unicodedata.normalize("NFC", word.strip().lower())

def tokenise(text):
    """Split text into word tokens, stripping punctuation."""
    tokens = re.findall(r"[\w''\u2019çñüëïäöẽĩãũ]+", text.lower(), re.UNICODE)
    return [t for t in tokens if len(t) >= 2]

def is_direct_vocab_entry(nasa_yuwe, spanish):
    """Return True when a direct-source pair is word/phrase-like."""
    if len(nasa_yuwe) > MAX_DIRECT_NASA_CHARS:
        return False
    if len(spanish) > MAX_DIRECT_SPANISH_CHARS:
        return False
    if re.match(r"(?i)^f['’]i['’]n['’]i\s+pe['’]la\s+\d+", nasa_yuwe.strip()):
        return False
    return True

# ── Pass 1: load all pairs ────────────────────────────────────────────
print("Loading dataset …")
pairs = []
with open(DATASET, "r", encoding="utf-8") as f:
    for line in f:
        pairs.append(json.loads(line))
print(f"  {len(pairs):,} pairs loaded")

# ── Pass 2: build vocab index ─────────────────────────────────────────
# vocab[norm_key] = {
#   "forms": set of surface forms,
#   "translations": list of (spanish, source),
#   "sources": set of source ids,
#   "is_direct": bool (has at least one direct dictionary translation)
# }
vocab = defaultdict(lambda: {
    "forms": set(),
    "translations": [],   # (spanish, source) tuples
    "sources": set(),
    "is_direct": False,
    "freq": 0,            # total occurrences across all pairs
})

print("Building vocabulary index …")

for pair in pairs:
    ny = pair["nasa_yuwe"].strip()
    spa = pair["spanish"].strip()
    src = pair["source"]

    if src in DIRECT_SOURCES and is_direct_vocab_entry(ny, spa):
        # Treat whole field as one vocab entry
        key = normalise(ny)
        if not key or len(key) < 2:
            continue
        entry = vocab[key]
        entry["forms"].add(ny)
        entry["translations"].append((spa, src))
        entry["sources"].add(src)
        entry["is_direct"] = True
        entry["freq"] += 1

        # Also index individual tokens if multi-word
        tokens = tokenise(ny)
        if len(tokens) > 1:
            for tok in tokens:
                tk = normalise(tok)
                if len(tk) >= 2:
                    vocab[tk]["forms"].add(tok)
                    vocab[tk]["sources"].add(src)
                    vocab[tk]["freq"] += 1
    else:
        # Sentence source: tokenise and index each word
        tokens = tokenise(ny)
        for tok in tokens:
            tk = normalise(tok)
            if len(tk) >= 2:
                vocab[tk]["forms"].add(tok)
                vocab[tk]["sources"].add(src)
                vocab[tk]["freq"] += 1

print(f"  {len(vocab):,} unique vocabulary entries")

# ── Pass 3: deduplicate translations per entry ────────────────────────
print("Deduplicating translations …")
for key, entry in vocab.items():
    seen = set()
    deduped = []
    for spa, src in entry["translations"]:
        norm_spa = normalise(spa)
        if norm_spa not in seen:
            seen.add(norm_spa)
            deduped.append({"spanish": spa, "source": src})
    entry["translations"] = deduped

# ── Pass 4: write output ──────────────────────────────────────────────
print(f"Writing {OUT_VOCAB} …")

# Sort: direct entries first (alphabetical), then token-only entries
entries_out = []
for key in sorted(vocab.keys()):
    e = vocab[key]
    obj = {
        "nasa_yuwe": key,
        "surface_forms": sorted(e["forms"]),
        "translations": e["translations"],  # already list of dicts
        "sources": sorted(e["sources"]),
        "frequency": e["freq"],
        "has_direct_translation": e["is_direct"],
    }
    entries_out.append(obj)

with open(OUT_VOCAB, "w", encoding="utf-8") as f:
    for obj in entries_out:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

# Stats
direct_count = sum(1 for e in entries_out if e["has_direct_translation"])
token_only = len(entries_out) - direct_count
trans_counts = [len(e["translations"]) for e in entries_out if e["has_direct_translation"]]

summary = {
    "total_vocabulary_entries": len(entries_out),
    "entries_with_direct_translation": direct_count,
    "entries_token_only": token_only,
    "avg_translations_per_entry": round(sum(trans_counts) / max(len(trans_counts), 1), 2),
    "source_coverage": {},
    "top_50_most_frequent": [],
}

# Source coverage
src_counts = defaultdict(int)
for e in entries_out:
    for s in e["sources"]:
        src_counts[s] += 1
summary["source_coverage"] = dict(sorted(src_counts.items(), key=lambda x: -x[1]))

# Top 50 most frequent
by_freq = sorted(entries_out, key=lambda x: -x["frequency"])
for e in by_freq[:50]:
    summary["top_50_most_frequent"].append({
        "nasa_yuwe": e["nasa_yuwe"],
        "frequency": e["frequency"],
        "translations": [t["spanish"] for t in e["translations"][:3]],
        "sources": e["sources"],
    })

with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\nDone!")
print(f"  {len(entries_out):,} vocabulary entries written to {OUT_VOCAB}")
print(f"  {direct_count:,} have direct Spanish translations")
print(f"  {token_only:,} are token-only (appear in sentences, no direct translation)")
print(f"\nTop 20 most frequent words:")
for e in by_freq[:20]:
    trans = ", ".join(t["spanish"] for t in e["translations"][:2]) if e["translations"] else "(no direct translation)"
    print(f"  {e['nasa_yuwe']:20s}  freq={e['frequency']:>5}  sources={len(e['sources'])}  → {trans}")
