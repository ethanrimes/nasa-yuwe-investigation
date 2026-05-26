"""Fetch senses for our nasa-yuwe-páez entries by passing entry IDs to PostgREST."""
import json, glob, urllib.request, urllib.parse, time, os

BASE_DIR = "Q:/nasa-yuwe-investigation/nasa_yuwe_materials/dictionaries/raw/supabase_paez"
SUPABASE_URL = "https://actkqboqpzniojhgtqzw.supabase.co"
ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFjdGtxYm9xcHpuaW9qaGd0cXp3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDEzOTQ0MzEsImV4cCI6MjAxNjk3MDQzMX0.KxeGK8Dnyg_BU9_eqtlNqbTyuPpmW6Dwasld1-HOiyE"

ids = []
for f in sorted(glob.glob(os.path.join(BASE_DIR, "entries_*.json"))):
    with open(f, encoding="utf-8") as fh:
        data = json.load(fh)
    for e in data:
        ids.append(e["id"])
print(f"Total entry IDs: {len(ids)}")

with open(os.path.join(BASE_DIR, "entry_ids.txt"), "w", encoding="utf-8") as fh:
    for i in ids: fh.write(i+"\n")

# Fetch senses for these entries, batching 100 IDs per request
BATCH = 100
all_senses = []
for i in range(0, len(ids), BATCH):
    chunk = ids[i:i+BATCH]
    id_list = ",".join(chunk)
    url = (
        f"{SUPABASE_URL}/rest/v1/senses?"
        f"select=id,entry_id,glosses,parts_of_speech,definition,semantic_domains,plural_form,variant&"
        f"entry_id=in.({id_list})"
    )
    req = urllib.request.Request(url, headers={
        "apikey": ANON_KEY,
        "Authorization": f"Bearer {ANON_KEY}",
        "User-Agent": "Mozilla/5.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        all_senses.extend(data)
        if i % 500 == 0:
            print(f"  batch {i}: total senses so far = {len(all_senses)}")
    except Exception as e:
        print(f"  batch {i} error: {e}")
    time.sleep(0.3)

with open(os.path.join(BASE_DIR, "senses_for_paez.json"), "w", encoding="utf-8") as fh:
    json.dump(all_senses, fh, ensure_ascii=False)
print(f"Wrote {len(all_senses)} senses to senses_for_paez.json")
