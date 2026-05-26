import json
items = [json.loads(l) for l in open(r"Q:\nasa-yuwe-investigation\parallel-data-sample\benchmark\benchmark.jsonl", encoding="utf-8")]

def esc(s): return s.replace("|", "\\|").replace("\n", " ").strip()

with open(r"Q:\nasa-yuwe-investigation\parallel-data-sample\benchmark\benchmark_translate_to_spanish.md", "w", encoding="utf-8") as f:
    f.write("# Benchmark Nasa Yuwe → Español (rellenar)\n\n")
    f.write("Traduzca cada entrada Nasa Yuwe al español en la columna vacía.\n\n")
    f.write("| # | Nasa Yuwe | Español |\n|---|-----------|---------|\n")
    for r in items:
        f.write(f"| {r['id']} | {esc(r['nasa_yuwe'])} |  |\n")

with open(r"Q:\nasa-yuwe-investigation\parallel-data-sample\benchmark\benchmark_translate_to_nasa_yuwe.md", "w", encoding="utf-8") as f:
    f.write("# Benchmark Español → Nasa Yuwe (rellenar)\n\n")
    f.write("Traduzca cada entrada española al Nasa Yuwe en la columna vacía.\n\n")
    f.write("| # | Español | Nasa Yuwe |\n|---|---------|-----------|\n")
    for r in items:
        f.write(f"| {r['id']} | {esc(r['spanish_reference'])} |  |\n")

print("wrote", len(items), "items to both files")
