#!/usr/bin/env python3
"""
Extract parallel Nasa Yuwe ↔ Spanish data from PDFs, HTML, and other
resources that weren't in the first consolidation pass.

Sources processed:
1. Procuraduría institutional text (PDF) - paragraph-level parallel
2. ADRES health text (PDF) - interleaved Spanish/Nasa Yuwe
3. Territorios Narrados bilingual children's books (4 PDFs)
4. KwesxYuwe thematic vocabulary PDFs (17 PDFs)
5. AmericasNLP 2024 "nasa_sin_cartas" dataset (archive CSV - constitution subset)
6. Consejo de Estado institutional overview (HTML)
7. UNAD teaching pamphlet (PDF)

Output: appends new pairs to nasa_yuwe_parallel_dataset.jsonl
"""

import json
import re
import unicodedata
from pathlib import Path
from collections import Counter

import pdfplumber
import pandas as pd

CORPUS = Path(r"Q:\nasa-yuwe-investigation\nasa_yuwe_corpus")
OUT_DIR = Path(r"Q:\nasa-yuwe-investigation")

new_records: list[dict] = []


def clean(text: str | None) -> str:
    if not isinstance(text, str) or not text.strip():
        return ""
    text = unicodedata.normalize("NFC", text.strip())
    text = re.sub(r"\s+", " ", text)
    return text


def dedup_key(nasa: str, spa: str) -> str:
    def norm(s):
        s = s.lower().strip()
        s = re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)
        s = re.sub(r"\s+", " ", s).strip()
        return s
    return norm(nasa) + "|||" + norm(spa)


# ─────────────────────────────────────────────────────────────────────────────
# 1. PROCURADURÍA — bilingual institutional text
# Pages alternate Spanish paragraph → Nasa Yuwe paragraph
# ─────────────────────────────────────────────────────────────────────────────
print("=== Procuraduría Institutional Text ===")
pdf_path = CORPUS / "04_government_legal" / "procuraduria" / "Texto_Institucional_Nasa_Castellano_Nasa_Yuwe_Procuraduria.pdf"

with pdfplumber.open(pdf_path) as pdf:
    # Pages 4-45 have parallel content (Spanish then Nasa Yuwe on alternating pages or sections)
    all_text = []
    for page in pdf.pages[3:]:  # Skip title/credits pages
        text = page.extract_text()
        if text:
            # Remove page header/footer
            text = re.sub(r"^Texto\s*\nInstitucional\s*\n?", "", text.strip())
            text = re.sub(r"^\d+\s*$", "", text.strip(), flags=re.MULTILINE)
            text = re.sub(r"\nNasa\s*\nCastellano - Nasa Yuwe\s*$", "", text.strip())
            if text.strip():
                all_text.append(text.strip())

    full_text = "\n\n".join(all_text)

    # The document has Spanish paragraphs followed by Nasa Yuwe translations
    # Spanish sections have standard Spanish text
    # Nasa Yuwe sections have characteristic markers: çxa, txaw, we'sx, ji'ph, etc.
    
    # Split into paragraphs
    paragraphs = [p.strip() for p in re.split(r"\n\n+", full_text) if p.strip() and len(p.strip()) > 30]
    
    # Heuristic: detect language per paragraph
    def is_nasa_yuwe(text):
        """Heuristic to detect Nasa Yuwe text."""
        nasa_markers = ["çxa", "txaw", "we'sx", "ji'ph", "kwe'sx", "fxi'z", "jiiçx", 
                       "theg", "nxu", "üus", "txaa", "pu'çx", "pkhakh", "nasa",
                       "mjwii", "ewuu", "jxuka", "nasawe"]
        text_lower = text.lower()
        score = sum(1 for m in nasa_markers if m in text_lower)
        return score >= 3
    
    # Pair consecutive Spanish → Nasa Yuwe paragraphs
    i = 0
    paired = 0
    while i < len(paragraphs) - 1:
        spa = paragraphs[i]
        nasa = paragraphs[i + 1]
        
        if not is_nasa_yuwe(spa) and is_nasa_yuwe(nasa):
            spa_clean = clean(spa)
            nasa_clean = clean(nasa)
            if spa_clean and nasa_clean and len(nasa_clean) > 20:
                new_records.append({
                    "nasa_yuwe": nasa_clean,
                    "spanish": spa_clean,
                    "source": "procuraduria_institutional",
                    "domain": "government",
                    "meta": {}
                })
                paired += 1
            i += 2
        else:
            i += 1
    
    print(f"  → {paired} paragraph pairs extracted")


# ─────────────────────────────────────────────────────────────────────────────
# 2. ADRES — health system bilingual text
# Interleaved: Spanish line, then Nasa Yuwe line
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== ADRES Health Text ===")
pdf_path = CORPUS / "04_government_legal" / "adres" / "TEXTO_LENGUA_NASAYUWE_Adres.pdf"

with pdfplumber.open(pdf_path) as pdf:
    all_text = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            # Remove headers
            text = re.sub(r"^ADRES - LENGUA NASA YUWE\s*", "", text.strip())
            text = re.sub(r"^L E N G U A\s*\nN A S A\s*Y U W E\s*", "", text.strip())
            text = re.sub(r"^L E N G U A N AS A Y U W E\s*\n?", "", text.strip())
            text = re.sub(r"^Traducción\s*\n?", "", text.strip())
            if text.strip():
                all_text.append(text.strip())

    full_text = "\n".join(all_text)
    lines = [l.strip() for l in full_text.split("\n") if l.strip() and len(l.strip()) > 15]
    
    # The ADRES document interleaves Spanish and Nasa Yuwe lines
    def is_nasa_yuwe_line(text):
        nasa_markers = ["çxa", "txaw", "we'sx", "ji'ph", "kwe'sx", "fxi'z", "jxuka",
                       "theg", "nxu", "üus", "pu'çx", "pkhak", "nasawe", "txâ",
                       "ji´ph", "we´sx", "jxuka"]
        text_lower = text.lower()
        score = sum(1 for m in nasa_markers if m in text_lower)
        return score >= 2
    
    paired = 0
    i = 0
    while i < len(lines) - 1:
        if not is_nasa_yuwe_line(lines[i]) and is_nasa_yuwe_line(lines[i + 1]):
            spa = clean(lines[i])
            nasa = clean(lines[i + 1])
            if spa and nasa:
                new_records.append({
                    "nasa_yuwe": nasa,
                    "spanish": spa,
                    "source": "adres_health",
                    "domain": "government",
                    "meta": {}
                })
                paired += 1
            i += 2
        else:
            i += 1
    
    print(f"  → {paired} pairs extracted")


# ─────────────────────────────────────────────────────────────────────────────
# 3. TERRITORIOS NARRADOS — bilingual children's books (4 PDFs)
# Pattern: Nasa Yuwe paragraph followed by Spanish paragraph on same/adjacent pages
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Territorios Narrados (Bilingual Children's Books) ===")
books_dir = CORPUS / "05_bilingual_literature" / "territorios_narrados"

book_files = [
    "04-Ipx_kwet_pekuj-AlrededorTulpa.pdf",
    "06-Nasa_Ujunxin_Thegnxi-LeyendoVidaNasa.pdf",
    "09-Luucx_Pekuhn_Ujusaa-Chivito.pdf",
    "10-Lxan_Nasa_Pal-AlvaroMojana.pdf",
]

def is_nasa_yuwe_para(text):
    """More sensitive check for children's books."""
    markers = ["çxa", "txã", "we'sx", "luuçx", "fxi", "kwe'sx", "nasa",
              "wa'j", "ũ", "çxh", "txaw", "ẽ", "nxu", "jxk", "u'j",
              "thẽ", "yakh", "pkhakh", "ku'l", "ĩ'kh", "khiç", "dxi'j"]
    text_lower = text.lower()
    score = sum(1 for m in markers if m in text_lower)
    # Also check for high density of special chars
    special = sum(1 for c in text if c in "çẽũĩãñ'")
    ratio = special / max(len(text), 1)
    return score >= 3 or (score >= 2 and ratio > 0.02)

total_book_pairs = 0
for book_file in book_files:
    pdf_path = books_dir / book_file
    book_name = book_file.split("-")[0].strip("0")
    
    with pdfplumber.open(pdf_path) as pdf:
        paragraphs = []
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            # Clean up
            text = text.strip()
            # Remove page numbers
            text = re.sub(r"^\d+\s*$", "", text, flags=re.MULTILINE)
            # Split into paragraphs (by bullet points or double newlines)
            # The books use  bullet markers for parallel pairs
            parts = re.split(r"(?:\n\s*\n|\n\s*)", text)
            for p in parts:
                p = p.strip()
                if len(p) > 25:
                    paragraphs.append(p)
        
        # Pair Nasa Yuwe → Spanish paragraphs
        paired = 0
        i = 0
        while i < len(paragraphs) - 1:
            p1 = paragraphs[i]
            p2 = paragraphs[i + 1]
            
            # Pattern 1: Nasa Yuwe first, then Spanish
            if is_nasa_yuwe_para(p1) and not is_nasa_yuwe_para(p2):
                nasa = clean(p1)
                spa = clean(p2)
                if nasa and spa and len(nasa) > 15 and len(spa) > 15:
                    new_records.append({
                        "nasa_yuwe": nasa,
                        "spanish": spa,
                        "source": "territorios_narrados",
                        "domain": "literary",
                        "meta": {"book": book_file.rsplit(".", 1)[0]}
                    })
                    paired += 1
                i += 2
            # Pattern 2: Spanish first, then Nasa Yuwe
            elif not is_nasa_yuwe_para(p1) and is_nasa_yuwe_para(p2):
                spa = clean(p1)
                nasa = clean(p2)
                if nasa and spa and len(nasa) > 15 and len(spa) > 15:
                    new_records.append({
                        "nasa_yuwe": nasa,
                        "spanish": spa,
                        "source": "territorios_narrados",
                        "domain": "literary",
                        "meta": {"book": book_file.rsplit(".", 1)[0]}
                    })
                    paired += 1
                i += 2
            else:
                i += 1
        
        print(f"  {book_file}: {paired} pairs")
        total_book_pairs += paired

print(f"  → Total book pairs: {total_book_pairs}")


# ─────────────────────────────────────────────────────────────────────────────
# 4. KWESXYUWE THEMATIC VOCABULARY PDFs
# Format: Nasa Yuwe word | Spanish meaning tables
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== KwesxYuwe Thematic Vocabulary ===")
kwesxyuwe_dir = CORPUS / "07_pedagogical" / "kwesxyuwe_thematic"

total_vocab = 0
for pdf_file in sorted(kwesxyuwe_dir.glob("*.pdf")):
    theme = pdf_file.stem.replace("KwesxYuwe_", "").replace("_NY", "")
    
    with pdfplumber.open(pdf_file) as pdf:
        pairs_in_file = 0
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            
            lines = text.strip().split("\n")
            for line in lines:
                line = line.strip()
                # Skip headers, word search grids, etc.
                if not line or len(line) < 3:
                    continue
                if re.match(r"^[A-ZÇÑÜ\s]{10,}$", line):  # Skip word search grid lines
                    continue
                if "NASA YUWE" in line.upper() and "SIGNIFICADO" in line.upper():
                    continue
                if "Sopa de Letras" in line or "Kwe'sx Yuweth" in line:
                    continue
                if line.startswith("Luuçx Yase"):
                    continue
                    
                # Try to split on tab or multiple spaces
                parts = re.split(r"\t+|\s{2,}", line, maxsplit=1)
                if len(parts) == 2:
                    nasa = clean(parts[0])
                    spa = clean(parts[1])
                    if nasa and spa and len(nasa) >= 2 and len(spa) >= 2:
                        # Verify it looks like a word pair (not grid noise)
                        if not re.match(r"^[A-ZÇÑÜ\s]+$", nasa):
                            new_records.append({
                                "nasa_yuwe": nasa,
                                "spanish": spa,
                                "source": "kwesxyuwe_vocab",
                                "domain": "pedagogical",
                                "meta": {"theme": theme}
                            })
                            pairs_in_file += 1
        
        if pairs_in_file > 0:
            print(f"  {pdf_file.name}: {pairs_in_file} pairs")
            total_vocab += pairs_in_file

print(f"  → Total vocabulary pairs: {total_vocab}")


# ─────────────────────────────────────────────────────────────────────────────
# 5. UNAD Teaching Pamphlet
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== UNAD Teaching Pamphlet ===")
pdf_path = CORPUS / "07_pedagogical" / "La_Alegria_de_Aprender_Nasa_Yuwe_y_Castellano_UNAD.pdf"
try:
    with pdfplumber.open(pdf_path) as pdf:
        unad_pairs = 0
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            lines = text.strip().split("\n")
            for line in lines:
                line = line.strip()
                parts = re.split(r"\t+|\s{2,}", line, maxsplit=1)
                if len(parts) == 2:
                    p1, p2 = clean(parts[0]), clean(parts[1])
                    if p1 and p2 and len(p1) >= 2 and len(p2) >= 2:
                        # Determine which is Nasa Yuwe vs Spanish
                        if is_nasa_yuwe_para(p1) and not is_nasa_yuwe_para(p2):
                            new_records.append({
                                "nasa_yuwe": p1, "spanish": p2,
                                "source": "unad_pamphlet", "domain": "pedagogical", "meta": {}
                            })
                            unad_pairs += 1
                        elif not is_nasa_yuwe_para(p1) and is_nasa_yuwe_para(p2):
                            new_records.append({
                                "nasa_yuwe": p2, "spanish": p1,
                                "source": "unad_pamphlet", "domain": "pedagogical", "meta": {}
                            })
                            unad_pairs += 1
        print(f"  → {unad_pairs} pairs extracted")
except Exception as e:
    print(f"  → Error: {e}")


# ─────────────────────────────────────────────────────────────────────────────
# 6. Consejo de Estado HTML — monolingual Nasa Yuwe with Spanish credits
# The page has Nasa Yuwe text but the Spanish equivalent is only "CREDITOS TEXTO"
# This is mostly monolingual Nasa Yuwe — skip for parallel data
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Consejo de Estado HTML ===")
print("  → Monolingual Nasa Yuwe only (no Spanish parallel), skipping")


# ─────────────────────────────────────────────────────────────────────────────
# 7. Caracterización NASA YUWE (Procuraduría) - mostly Spanish about Nasa culture
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Caracterización Procuraduría ===")
print("  → Spanish-only ethnographic description, no parallel content, skipping")


# ─────────────────────────────────────────────────────────────────────────────
# 8. Caro y Cuervo + CRIC Dictionary PDFs - image-only, no extractable text
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Dictionary PDFs ===")
print("  → Caro y Cuervo: scanned images only (no OCR text)")
print("  → CRIC Dictionary: scanned images only (no OCR text)")
print("  → Vocab primer: single page, no text layer")


# ─────────────────────────────────────────────────────────────────────────────
# 9. Wikimedia Incubator articles — too short, mostly metadata/navigation
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Wikimedia Incubator ===")
print("  → Only 3 stub articles with minimal content, skipping")


# ─────────────────────────────────────────────────────────────────────────────
# 10. JW.org pages — Nasa Yuwe text but Spanish equivalents not yet downloaded
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== JW.org ===")
print("  → 100 pub codes catalogued but PDFs/HTML not yet downloaded")
print("  → Need browser-authenticated scraping for Spanish equivalents")


# ─────────────────────────────────────────────────────────────────────────────
# DEDUPLICATION against existing dataset + internal dedup
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"New raw records from this pass: {len(new_records)}")

# Load existing dataset keys
existing_keys = set()
existing_jsonl = OUT_DIR / "nasa_yuwe_parallel_dataset.jsonl"
existing_count = 0
with open(existing_jsonl, "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        existing_keys.add(dedup_key(rec["nasa_yuwe"], rec["spanish"]))
        existing_count += 1

print(f"Existing dataset has {existing_count} pairs")

# Dedup new records against existing and against themselves
seen = set(existing_keys)
truly_new = []
dups = 0
for rec in new_records:
    key = dedup_key(rec["nasa_yuwe"], rec["spanish"])
    if key in seen:
        dups += 1
    else:
        seen.add(key)
        truly_new.append(rec)

print(f"Duplicates with existing dataset: {dups}")
print(f"Truly new pairs: {len(truly_new)}")

# Stats
source_counts = Counter(r["source"] for r in truly_new)
domain_counts = Counter(r["domain"] for r in truly_new)

print("\n── New pairs by source ──")
for src, cnt in source_counts.most_common():
    print(f"  {src:30s} {cnt:>5,}")

print("\n── New pairs by domain ──")
for dom, cnt in domain_counts.most_common():
    print(f"  {dom:30s} {cnt:>5,}")

# Append to existing JSONL
with open(existing_jsonl, "a", encoding="utf-8") as f:
    for rec in truly_new:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

new_total = existing_count + len(truly_new)
print(f"\n✅ Appended {len(truly_new)} new pairs → {existing_jsonl}")
print(f"✅ New total: {new_total} pairs")

# Update summary
summary_path = OUT_DIR / "nasa_yuwe_parallel_dataset_summary.json"
with open(summary_path, "r", encoding="utf-8") as f:
    summary = json.load(f)

# Recount from file
all_source_counts = Counter()
all_domain_counts = Counter()
total = 0
with open(existing_jsonl, "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        all_source_counts[rec["source"]] += 1
        all_domain_counts[rec["domain"]] += 1
        total += 1

summary["total_pairs"] = total
summary["raw_before_dedup"] = summary.get("raw_before_dedup", 0) + len(new_records)
summary["by_source"] = dict(all_source_counts.most_common())
summary["by_domain"] = dict(all_domain_counts.most_common())
summary["notes"].append("Pass 2: Extracted from Procuraduría, ADRES, Territorios Narrados books, KwesxYuwe vocabulary PDFs")

with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"✅ Updated summary → {summary_path}")
