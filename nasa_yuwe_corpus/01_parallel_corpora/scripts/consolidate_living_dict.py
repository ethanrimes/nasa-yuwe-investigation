"""Consolidate Living Dictionaries Páez entries into a Spanish↔Nasa Yuwe CSV.

Inputs (from background dictionary scrape):
  raw/supabase_paez/entries_*.json  — paginated `entries` table (3,934 total)
  raw/supabase_paez/senses_*.json   — paginated `senses` table (glosses per entry)
  raw/supabase_paez/audio.json      — audio metadata (skipped here)

Output:
  living_dictionaries_paez.csv  — columns:
    entry_id, nasa_yuwe (lexeme), pos, gloss_es, gloss_en, gloss_other,
    semantic_domain, notes
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
RAW = ROOT / "raw" / "supabase_paez"
OUT = ROOT / "living_dictionaries_paez.csv"


def load_paginated(prefix: str) -> list[dict]:
    rows: list[dict] = []
    paths = list(RAW.glob(f"{prefix}_*.json"))

    def _key(p: Path) -> int:
        tail = p.stem.split("_")[-1]
        return int(tail) if tail.isdigit() else 0

    for fp in sorted(paths, key=_key):
        try:
            rows.extend(json.loads(fp.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    return rows


def main() -> None:
    entries = load_paginated("entries")
    senses = load_paginated("senses")
    print(f"Loaded {len(entries)} entries, {len(senses)} senses")

    # Group senses by entry_id
    senses_by_entry: dict[str, list[dict]] = {}
    for s in senses:
        eid = s.get("entry_id")
        if eid:
            senses_by_entry.setdefault(eid, []).append(s)

    def lexeme_text(lx) -> str:
        if not lx:
            return ""
        if isinstance(lx, str):
            return lx
        if isinstance(lx, dict):
            return lx.get("default") or lx.get("lo1") or lx.get("ny") or ""
        return str(lx)

    def notes_text(notes) -> str:
        if isinstance(notes, dict):
            return notes.get("default", "")
        return notes or ""

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["entry_id", "nasa_yuwe", "pos", "gloss_es", "gloss_en", "gloss_other", "semantic_domain", "notes"])
        for e in entries:
            eid = e.get("id")
            lex = lexeme_text(e.get("lexeme"))
            notes = notes_text(e.get("notes"))
            ents = senses_by_entry.get(eid, [])
            if not ents:
                w.writerow([eid, lex, "", "", "", "", "", notes])
                continue
            for s in ents:
                gl = s.get("glosses") or {}
                pos_list = s.get("parts_of_speech") or []
                pos = ",".join(pos_list) if isinstance(pos_list, list) else str(pos_list)
                gl_es = gl.get("es", "") if isinstance(gl, dict) else ""
                gl_en = gl.get("en", "") if isinstance(gl, dict) else ""
                other = {k: v for k, v in (gl.items() if isinstance(gl, dict) else []) if k not in ("es", "en")}
                gl_other = "; ".join(f"{k}: {v}" for k, v in other.items())
                sem = ",".join(s.get("semantic_domains") or [])
                w.writerow([eid, lex, pos, gl_es, gl_en, gl_other, sem, notes])

    # Stats
    with_es = sum(1 for e in entries if any((s.get("glosses") or {}).get("es") for s in senses_by_entry.get(e.get("id"), [])))
    print(f"Entries with Spanish gloss: {with_es}")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
