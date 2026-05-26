"""Distill every lexical source into a single deduplicated master vocabulary.

Output:  01_parallel_corpora/master_vocabulary_pbb.csv
Columns:
    nasa_yuwe       — canonical lexeme (normalized: lowercased, whitespace-collapsed)
    nasa_yuwe_raw   — original surface form from the first source
    spanish         — Spanish gloss (best-pick across sources)
    english         — English gloss if present
    pos             — part of speech tag if present
    semantic_domain — SIL semantic-domain code if present
    notes           — source-specific notes
    sources         — comma-separated list of sources contributing this entry
    n_sources       — count of sources

Sources merged (in priority order — earlier sources win on tie):
    1. Living Dictionaries (3,950 Spanish-glossed entries; Gerdel/Slocum 1983 lineage + community fieldwork)
    2. Swarthmore Talking Dictionary full (3,912 entries; same Gerdel/Slocum lineage)
    3. broomva translation_pbb_spa (train + val + test = 3,794 entries)
    4. Paper 2024 dataset (nasa_full_dataset.csv — Pueblos Originarios + CCELA 1994 constitution glossary)

Run:
    cd nasa_yuwe_corpus/01_parallel_corpora
    python scripts/consolidate_vocabulary.py
"""
from __future__ import annotations
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # nasa_yuwe_corpus root
PC = ROOT / "01_parallel_corpora"
OUT = PC / "master_vocabulary_pbb.csv"
ARCHIVE = ROOT / "_archive" / "paper_2024_data_local"


def normalize(text: str) -> str:
    """Lowercase + collapse whitespace + strip surrounding punctuation."""
    if not text:
        return ""
    text = unicodedata.normalize("NFC", text).strip().lower()
    text = re.sub(r"\s+", " ", text)
    # Strip leading/trailing common punctuation but keep diacritics & glottals
    text = text.strip(' "“”\'()[]{}.,;:!?')
    return text


def add_entry(store: dict, nasa_yuwe: str, spanish: str = "", english: str = "",
              pos: str = "", semantic_domain: str = "", notes: str = "",
              source: str = "", nasa_yuwe_raw: str | None = None) -> None:
    key = normalize(nasa_yuwe)
    if not key or len(key) > 200:
        return
    raw = nasa_yuwe_raw if nasa_yuwe_raw is not None else nasa_yuwe
    if key not in store:
        store[key] = {
            "nasa_yuwe": key,
            "nasa_yuwe_raw": raw.strip(),
            "spanish": spanish.strip() if spanish else "",
            "english": english.strip() if english else "",
            "pos": pos.strip() if pos else "",
            "semantic_domain": semantic_domain.strip() if semantic_domain else "",
            "notes": notes.strip() if notes else "",
            "sources": set(),
        }
    e = store[key]
    if source:
        e["sources"].add(source)
    # Fill in missing fields if this source has them
    for fld, val in (("spanish", spanish), ("english", english),
                     ("pos", pos), ("semantic_domain", semantic_domain),
                     ("notes", notes)):
        if not e[fld] and val:
            e[fld] = val.strip()


def load_living(store: dict) -> int:
    p = PC / "living_dictionaries_paez.csv"
    if not p.exists():
        return 0
    n = 0
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            add_entry(
                store,
                nasa_yuwe=r.get("nasa_yuwe", ""),
                spanish=r.get("gloss_es", ""),
                english=r.get("gloss_en", ""),
                pos=r.get("pos", ""),
                semantic_domain=r.get("semantic_domain", ""),
                notes=r.get("notes", "")[:200] if r.get("notes") else "",
                source="living_dictionaries",
            )
            n += 1
    return n


def load_swarthmore(store: dict) -> int:
    p = PC / "swarthmore_talking_dictionary_full.csv"
    if not p.exists():
        return 0
    n = 0
    with p.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            add_entry(
                store,
                nasa_yuwe=r.get("headword", ""),
                spanish=r.get("gloss", ""),
                pos=r.get("part_of_speech", ""),
                notes=r.get("authority", "")[:200] if r.get("authority") else "",
                source="swarthmore_talking",
            )
            n += 1
    return n


def load_broomva(store: dict) -> int:
    n = 0
    for split in ("train", "validation", "test"):
        p = PC / f"broomva_translation_pbb_spa_{split}.csv"
        if not p.exists():
            continue
        with p.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                add_entry(
                    store,
                    nasa_yuwe=r.get("translation.pbb", ""),
                    spanish=r.get("translation.spa", ""),
                    source=f"broomva_{split}",
                )
                n += 1
    return n


def load_paper_dataset(store: dict) -> int:
    p = ARCHIVE / "nasa_full_dataset.csv"
    if not p.exists():
        return 0
    n = 0
    with p.open(encoding="utf-8") as f:
        # Detect columns
        sample = f.read(2000)
        f.seek(0)
        reader = csv.DictReader(f)
        # Robles paper schema is usually: spa, pbb or similar
        for r in reader:
            spa_col = next((c for c in r if c.lower() in ("spa", "spanish", "es", "esp", "español")), None)
            pbb_col = next((c for c in r if c.lower() in ("pbb", "nasa", "nasa_yuwe", "nas")), None)
            if not (spa_col and pbb_col):
                continue
            add_entry(
                store,
                nasa_yuwe=r[pbb_col],
                spanish=r[spa_col],
                source="paper_2024",
            )
            n += 1
    return n


def main() -> None:
    store: dict[str, dict] = {}

    counts = {
        "living_dictionaries":  load_living(store),
        "swarthmore_talking":   load_swarthmore(store),
        "broomva_translation":  load_broomva(store),
        "paper_2024":           load_paper_dataset(store),
    }

    rows = []
    for k, e in store.items():
        e["sources"] = ",".join(sorted(e["sources"]))
        e["n_sources"] = e["sources"].count(",") + 1 if e["sources"] else 0
        rows.append(e)

    rows.sort(key=lambda r: r["nasa_yuwe"])

    fields = ["nasa_yuwe", "nasa_yuwe_raw", "spanish", "english", "pos",
              "semantic_domain", "notes", "sources", "n_sources"]
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # Stats
    print(f"Wrote {OUT}")
    print()
    print("Per-source input row counts (before dedup):")
    total = 0
    for k, v in counts.items():
        print(f"  {k:<24} {v:>6}")
        total += v
    print(f"  {'TOTAL_INPUT':<24} {total:>6}")
    print()
    print(f"Unique normalized entries:           {len(rows):>6}")
    spanish_glossed = sum(1 for r in rows if r["spanish"])
    print(f"With Spanish gloss:                  {spanish_glossed:>6}")
    multi_source = sum(1 for r in rows if r["n_sources"] >= 2)
    print(f"Appearing in >=2 sources (high conf): {multi_source:>6}")
    triple_source = sum(1 for r in rows if r["n_sources"] >= 3)
    print(f"Appearing in >=3 sources:             {triple_source:>6}")
    with_pos = sum(1 for r in rows if r["pos"])
    print(f"With POS tag:                        {with_pos:>6}")


if __name__ == "__main__":
    main()
