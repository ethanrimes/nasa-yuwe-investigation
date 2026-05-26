import json, random, os, collections

import time
random.seed(int(time.time()))

SRC = r"Q:\nasa-yuwe-investigation\nasa_yuwe_parallel_dataset.jsonl"
OUT = r"Q:\nasa-yuwe-investigation\parallel-data-sample\source"
os.makedirs(OUT, exist_ok=True)

# Stratified allocation (overweighting full-sentence sources)
QUOTAS = {
    "bible_nt": 6,
    "broomva_instruct": 6,
    "americasnlp_2024": 6,
    "territorios_narrados": 4,
    "adres_health": 2,
    "procuraduria_institutional": 1,
    "living_dict": 2,
    "broomva_translation": 2,
    "kwesxyuwe_thematic": 1,
}
assert sum(QUOTAS.values()) == 30

def looks_like_nasa_yuwe(s):
    import re
    sl = s.lower()
    markers = ["txa", "kwe", "çxa", "jĩ", "jxk", "yuwe", "nasa", "ã", "ẽ", "ĩ", "ũ",
               "ç", "kh", "fx", "vx", "wẽ", "sxh", "jxk", "'sx", "’sx", "u’j", "yu’",
               "u'j", "yu'", "xa’", "xa'"]
    score = sum(1 for m in markers if m in sl)
    apos = s.count("'") + s.count("’") + s.count("ʼ")
    if apos / max(len(s), 1) > 0.03:
        score += 3
    if re.search(r"[ãẽĩõũ]", s):
        score += 2
    if "ç" in s and "ção" not in sl and "çã" not in sl:
        score += 2
    return score >= 3

buckets = collections.defaultdict(list)
with open(SRC, encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        buckets[rec["source"]].append(rec)

sampled = []
for src, n in QUOTAS.items():
    pool = buckets[src]
    if src in ("bible_nt", "broomva_instruct", "americasnlp_2024", "territorios_narrados",
               "adres_health", "procuraduria_institutional"):
        filtered = [r for r in pool if len(r["nasa_yuwe"].split()) >= 4 and len(r["spanish"].split()) >= 4]
        if len(filtered) >= n:
            pool = filtered
    pool = [r for r in pool if not looks_like_nasa_yuwe(r["spanish"])]
    picks = random.sample(pool, n)
    sampled.extend(picks)

random.shuffle(sampled)

def esc(s):
    return s.replace("|", "\\|").replace("\n", " ").strip()

# 1) Full markdown
with open(os.path.join(OUT, "sample_full.md"), "w", encoding="utf-8") as f:
    f.write("# Muestra del Conjunto de Datos Paralelo (30 elementos estratificados)\n\n")
    f.write("Muestreo estratificado por fuente, con sobreponderación de fuentes de oraciones completas.\n\n")
    f.write("| # | Nasa Yuwe | Español | Fuente |\n")
    f.write("|---|-----------|---------|--------|\n")
    for i, r in enumerate(sampled, 1):
        f.write(f"| {i} | {esc(r['nasa_yuwe'])} | {esc(r['spanish'])} | {r['source']} |\n")

# 2) Nasa Yuwe only
with open(os.path.join(OUT, "sample_nasa_yuwe.md"), "w", encoding="utf-8") as f:
    f.write("# Muestra - solo Nasa Yuwe\n\n")
    f.write("| # | Nasa Yuwe |\n|---|-----------|\n")
    for i, r in enumerate(sampled, 1):
        f.write(f"| {i} | {esc(r['nasa_yuwe'])} |\n")

# 3) Spanish only
with open(os.path.join(OUT, "sample_spanish.md"), "w", encoding="utf-8") as f:
    f.write("# Muestra - solo Español\n\n")
    f.write("| # | Español |\n|---|---------|\n")
    for i, r in enumerate(sampled, 1):
        f.write(f"| {i} | {esc(r['spanish'])} |\n")

# Summary
counts = collections.Counter(r["source"] for r in sampled)
print("Source distribution:", dict(counts))
print("Total:", len(sampled))
print("Wrote files to", OUT)
