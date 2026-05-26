import json, re, random, collections, os

random.seed(20260525)

SRC = r"Q:\nasa-yuwe-investigation\nasa_yuwe_parallel_dataset.jsonl"
OUT_DIR = r"Q:\nasa-yuwe-investigation\parallel-data-sample\benchmark"
os.makedirs(OUT_DIR, exist_ok=True)

def looks_like_nasa_yuwe(s):
    sl = s.lower()
    markers = ["txa","kwe","çxa","jĩ","jxk","yuwe","nasa","ã","ẽ","ĩ","ũ","ç","kh","fx",
               "vx","wẽ","’sx","u’j","yu’","'sx","u'j","yu'"]
    score = sum(1 for m in markers if m in sl)
    apos = s.count("'") + s.count("’") + s.count("ʼ")
    if apos / max(len(s),1) > 0.04: score += 3
    if re.search(r"[ãẽĩõũ]", s): score += 2
    if "ç" in s: score += 2
    return score >= 3

# Drop entries where Spanish field has Nasa Yuwe characters that indicate misalignment.
# But keep entries whose Spanish field is plausibly Spanish (no special-char triggers).
def looks_spanish(s):
    if not s.strip(): return False
    # require at least some ASCII letters and majority Latin word chars
    letters = sum(c.isalpha() for c in s)
    if letters < 1: return False
    return not looks_like_nasa_yuwe(s)

records = []
for line in open(SRC, encoding="utf-8"):
    r = json.loads(line)
    if not r["nasa_yuwe"].strip() or not r["spanish"].strip(): continue
    if not looks_spanish(r["spanish"]): continue
    # filter the noisiest sources entirely
    if r["source"] in ("territorios_narrados",): continue
    records.append(r)

by_src = collections.defaultdict(list)
for r in records:
    by_src[r["source"]].append(r)

def words(s): return len(s.split())

def pick(pool, n, key=None, exclude_substr=None, seen=None):
    seen = seen if seen is not None else set()
    cand = []
    for r in pool:
        ny = r["nasa_yuwe"].strip()
        if ny in seen: continue
        if exclude_substr and any(x in r["spanish"].lower() for x in exclude_substr): continue
        if key and not key(r): continue
        cand.append(r)
    random.shuffle(cand)
    picks = cand[:n]
    for r in picks: seen.add(r["nasa_yuwe"].strip())
    return picks

seen = set()
benchmark = []

# Tier 1: Single content words / very short lexical (1-2 tokens NY)
t1_pool = by_src["living_dict"] + by_src["broomva_translation"] + by_src["kwesxyuwe_thematic"]
t1 = pick(t1_pool, 8,
          key=lambda r: 1 <= words(r["nasa_yuwe"]) <= 2 and 1 <= words(r["spanish"]) <= 4
                       and len(r["nasa_yuwe"]) >= 3,
          seen=seen)
for r in t1: r["_tier"] = "T1: single word / lexical"

# Tier 2: Short phrases (3-6 NY tokens)
t2_pool = by_src["living_dict"] + by_src["broomva_translation"] + by_src["kwesxyuwe_thematic"] + by_src["americasnlp_2024"]
t2 = pick(t2_pool, 6,
          key=lambda r: 3 <= words(r["nasa_yuwe"]) <= 6 and 3 <= words(r["spanish"]) <= 10,
          seen=seen)
for r in t2: r["_tier"] = "T2: short phrase"

# Tier 3: Short sentences (5-12 NY tokens), mix religious and constitutional/everyday
t3a = pick(by_src["bible_nt"], 4,
           key=lambda r: 5 <= words(r["nasa_yuwe"]) <= 12 and 5 <= words(r["spanish"]) <= 20,
           seen=seen)
t3b = pick(by_src["broomva_instruct"], 3,
           key=lambda r: 5 <= words(r["nasa_yuwe"]) <= 12 and 5 <= words(r["spanish"]) <= 20,
           seen=seen)
t3c = pick(by_src["americasnlp_2024"], 2,
           key=lambda r: 5 <= words(r["nasa_yuwe"]) <= 12 and 5 <= words(r["spanish"]) <= 20,
           seen=seen)
for r in t3a + t3b + t3c: r["_tier"] = "T3: short sentence"

# Tier 4: Medium sentences (13-30 NY tokens)
t4a = pick(by_src["bible_nt"], 4,
           key=lambda r: 13 <= words(r["nasa_yuwe"]) <= 30,
           seen=seen)
t4b = pick(by_src["broomva_instruct"], 3,
           key=lambda r: 13 <= words(r["nasa_yuwe"]) <= 30,
           seen=seen)
t4c = pick(by_src["americasnlp_2024"], 2,
           key=lambda r: 13 <= words(r["nasa_yuwe"]) <= 30,
           seen=seen)
for r in t4a + t4b + t4c: r["_tier"] = "T4: medium sentence"

# Tier 5: Long / complex sentences (30-80 NY tokens)
t5a = pick(by_src["bible_nt"], 2,
           key=lambda r: 30 <= words(r["nasa_yuwe"]) <= 80,
           seen=seen)
t5b = pick(by_src["broomva_instruct"], 2,
           key=lambda r: 30 <= words(r["nasa_yuwe"]) <= 80,
           seen=seen)
t5c = pick(by_src["americasnlp_2024"], 1,
           key=lambda r: 30 <= words(r["nasa_yuwe"]) <= 80,
           seen=seen)
for r in t5a + t5b + t5c: r["_tier"] = "T5: long / complex"

benchmark = t1 + t2 + t3a + t3b + t3c + t4a + t4b + t4c + t5a + t5b + t5c

def esc(s):
    return s.replace("|", "\\|").replace("\n", " ").strip()

# Markdown - paired (gold)
with open(os.path.join(OUT_DIR, "benchmark_full.md"), "w", encoding="utf-8") as f:
    f.write("# Benchmark de Traducción Nasa Yuwe → Español\n\n")
    f.write(f"Total: {len(benchmark)} elementos, seleccionados en 5 niveles de dificultad.\n")
    f.write("Filtrado para excluir filas con texto Nasa Yuwe contaminando la columna Español "
            "(territorios_narrados excluido por completo).\n\n")
    f.write("| # | Nivel | Nasa Yuwe | Español (referencia) | Fuente |\n")
    f.write("|---|-------|-----------|----------------------|--------|\n")
    for i, r in enumerate(benchmark, 1):
        f.write(f"| {i} | {r['_tier']} | {esc(r['nasa_yuwe'])} | {esc(r['spanish'])} | {r['source']} |\n")

# Markdown - prompt-only (Nasa Yuwe to translate)
with open(os.path.join(OUT_DIR, "benchmark_prompt.md"), "w", encoding="utf-8") as f:
    f.write("# Benchmark Nasa Yuwe — prompts a traducir al Español\n\n")
    f.write("Traduzca cada entrada al español. No consulte fuentes externas.\n\n")
    f.write("| # | Nivel | Nasa Yuwe |\n|---|-------|-----------|\n")
    for i, r in enumerate(benchmark, 1):
        f.write(f"| {i} | {r['_tier']} | {esc(r['nasa_yuwe'])} |\n")

# JSONL for automated evaluation
with open(os.path.join(OUT_DIR, "benchmark.jsonl"), "w", encoding="utf-8") as f:
    for i, r in enumerate(benchmark, 1):
        f.write(json.dumps({
            "id": i,
            "tier": r["_tier"],
            "nasa_yuwe": r["nasa_yuwe"],
            "spanish_reference": r["spanish"],
            "source": r["source"],
            "domain": r.get("domain"),
        }, ensure_ascii=False) + "\n")

dist = collections.Counter((r["_tier"], r["source"]) for r in benchmark)
print(f"Total: {len(benchmark)}")
print("Distribution (tier, source):")
for k, v in sorted(dist.items()):
    print(f"  {k[0]:<25} {k[1]:<25} {v}")
