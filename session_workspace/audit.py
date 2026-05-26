import json, re, collections

def looks_like_nasa_yuwe(s):
    sl = s.lower()
    markers = ["txa","kwe","çxa","jĩ","jxk","yuwe","nasa","ã","ẽ","ĩ","ũ","ç","kh","fx",
               "vx","wẽ","’sx","u’j","yu’","'sx","u'j","yu'"]
    score = sum(1 for m in markers if m in sl)
    apos = s.count("'") + s.count("’") + s.count("ʼ")
    if apos / max(len(s),1) > 0.03: score += 3
    if re.search(r"[ãẽĩõũ]", s): score += 2
    if "ç" in s: score += 2
    return score >= 3

by_src = collections.Counter()
bad = collections.Counter()
examples = collections.defaultdict(list)
for line in open(r"Q:\nasa-yuwe-investigation\nasa_yuwe_parallel_dataset.jsonl", encoding="utf-8"):
    r = json.loads(line)
    by_src[r["source"]] += 1
    if looks_like_nasa_yuwe(r["spanish"]):
        bad[r["source"]] += 1
        if len(examples[r["source"]]) < 2:
            examples[r["source"]].append(r["spanish"][:100])

print(f"{'source':<30}{'total':>8}{'bad':>8}{'pct':>8}")
for s in sorted(by_src, key=lambda x: -bad[x]):
    t = by_src[s]; b = bad[s]
    print(f"{s:<30}{t:>8}{b:>8}{100*b/t:>7.1f}%")
print(f"{'TOTAL':<30}{sum(by_src.values()):>8}{sum(bad.values()):>8}{100*sum(bad.values())/sum(by_src.values()):>7.1f}%")
print()
for s, exs in examples.items():
    print(f"-- {s} examples --")
    for e in exs: print("  ", e)
