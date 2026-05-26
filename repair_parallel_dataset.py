#!/usr/bin/env python3
"""
Repair known source-layout contamination in nasa_yuwe_parallel_dataset.jsonl.

The original additional-data pass treated PDF text extraction as a flat line
stream. That broke two-column and alternating-page layouts, especially the
Territorios Narrados books and the ADRES pamphlet. This script removes those
rows, reparses the PDFs with page/block layout, and rewrites the JSONL plus
summary counts.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import json
import math
import re
import unicodedata
from pathlib import Path

import fitz


ROOT = Path(r"Q:\nasa-yuwe-investigation")
CORPUS = ROOT / "nasa_yuwe_corpus"
DATASET = ROOT / "nasa_yuwe_parallel_dataset.jsonl"
SUMMARY = ROOT / "nasa_yuwe_parallel_dataset_summary.json"
BOOK_DIR = CORPUS / "05_bilingual_literature" / "territorios_narrados"
ADRES_PDF = (
    CORPUS / "04_government_legal" / "adres" / "TEXTO_LENGUA_NASAYUWE_Adres.pdf"
)

SPANISH_WORDS = set(
    """
    a al como con cuando de del debe deben donde el en entre era eran es esta estas
    están este estos fue ha han hay la las le les lo los más muy no o para pero por
    porque que se si sino sobre son su sus también todo todos todas un una unos unas
    agua años casa comunidad cual día desde este hacia hasta hombre la mujer niño
    niña niños niñas para que recursos salud servicios sistema territorio
    """.split()
)

NASA_MARKERS = [
    "ç",
    "ã",
    "ẽ",
    "ĩ",
    "ũ",
    "û",
    "î",
    "ï",
    "â",
    "ê",
    "ô",
    "tx",
    "kx",
    "fx",
    "sx",
    "çx",
    "nx",
    "we’sx",
    "we'sx",
    "ji’",
    "ji'",
    "u’",
    "u'",
    "txã",
    "ksxa",
    "jx",
    "çxa",
    "yuwe",
]

HEADER_PATTERNS = [
    "Territorios Narrados",
    "Leyendo la vida nasa",
    "Nasa u´junxin thegnxi",
    "Nasa u’junxin thegnxi",
    "ADRES - LENGUA NASA YUWE",
    "LENGUA NASA YUWE",
    "Traducción",
]

BOOK_RANGES = {
    "04-Ipx_kwet_pekuj-AlrededorTulpa.pdf": (17, 61),
    "06-Nasa_Ujunxin_Thegnxi-LeyendoVidaNasa.pdf": (18, 47),
    "09-Luucx_Pekuhn_Ujusaa-Chivito.pdf": (14, 32),
    "10-Lxan_Nasa_Pal-AlvaroMojana.pdf": (14, 31),
}


def clean(text: str | None) -> str:
    """Normalize PDF extraction artifacts without changing orthography."""
    if not text:
        return ""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\ufb01", "fi").replace("\ufb02", "fl")
    text = text.replace("´", "’")
    text = re.sub(r"AD\s*R\s*ES\s*-\s*LENGUA\s*NASA\s*YUW\s*E", " ", text)
    text = re.sub(r"\bLENGUA\s+NASA\s+Y\s*UW\s*E\b", " ", text)
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^\W*\d{1,3}\s+(?=[A-Za-zÁÉÍÓÚÑáéíóúñÇç])", "", text).strip()
    text = re.sub(r"^[•\-–]+\s*", "", text).strip()
    text = (
        text.replace("fi nancieros", "financieros")
        .replace("fi nanciera", "financiera")
        .replace("Afi liados", "Afiliados")
        .replace("afi liados", "afiliados")
        .replace("confi anza", "confianza")
        .replace("efi ciente", "eficiente")
        .replace("sufi ciente", "suficiente")
    )
    return text


def dedup_key(nasa: str, spanish: str) -> str:
    def norm(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", "", text, flags=re.UNICODE)
        return re.sub(r"\s+", " ", text).strip()

    return norm(nasa) + "|||" + norm(spanish)


def language_scores(text: str) -> tuple[int, int]:
    lower = text.lower()
    spanish_tokens = re.findall(r"[a-záéíóúñü]+", lower)
    spanish_score = sum(token in SPANISH_WORDS for token in spanish_tokens)
    nasa_score = sum(lower.count(marker) for marker in NASA_MARKERS)
    nasa_score += len(re.findall(r"\w[’']\w", lower))
    return nasa_score, spanish_score


def classify(text: str) -> str:
    nasa_score, spanish_score = language_scores(text)
    if nasa_score >= max(2, spanish_score):
        return "nasa_yuwe"
    return "spanish"


def valid_block(text: str) -> bool:
    if not text or len(text) < 20 or text.isdigit():
        return False
    if any(header in text for header in HEADER_PATTERNS):
        return False
    return not re.match(
        r"^(Los nasa|Glosario|Textos|ISBN|Reservados|Serie Río|Primera edición|©|"
        r"L ibertad|Sobre Territorios|Introducción|Presentación)\b",
        text,
    )


def valid_adres_block(text: str) -> bool:
    if not text or len(text) < 8 or text.isdigit():
        return False
    return not any(header in text for header in HEADER_PATTERNS)


def split_sentences(text: str) -> list[str]:
    parts: list[str] = []
    start = 0
    for match in re.finditer(r"[.!?](?=\s+|$)", text):
        end = match.end()
        if re.search(r"\b[apm]\.$", text[max(0, start) : end].lower()):
            continue
        if end != len(text) and not re.match(r"\s+[A-ZÁÉÍÓÚÑÜ¿¡«“]", text[end : end + 3]):
            continue
        part = text[start:end].strip()
        if len(part) >= 20:
            parts.append(part)
            start = end
    rest = text[start:].strip()
    if rest:
        parts.append(rest)
    if len(parts) <= 1 and len(text) > 420:
        parts = [part.strip() for part in re.split(r"(?<=;)\s+", text) if part.strip()]
    return parts or [text]


def ends_sentence(text: str) -> bool:
    text = text.strip()
    if not re.search(r"[.!?]\s*$", text):
        return False
    return not re.search(r"\b[apm]\.\s*$", text.lower())


def split_long_clause(text: str, chunks: int) -> list[str]:
    """Split unpunctuated long Nasa Yuwe blocks at nearby clause boundaries."""
    if chunks <= 1 or len(text) < 320:
        return [text]

    boundaries = [match.end() for match in re.finditer(r"[,;:]\s+", text)]
    if len(boundaries) < chunks - 1:
        boundaries = [match.end() for match in re.finditer(r"\s+", text)]

    pieces: list[str] = []
    start = 0
    for i in range(1, chunks):
        target = round(len(text) * i / chunks)
        boundary = min((b for b in boundaries if b > start + 40), key=lambda b: abs(b - target), default=None)
        if boundary is None or boundary >= len(text) - 40:
            break
        pieces.append(text[start:boundary].strip())
        start = boundary
    pieces.append(text[start:].strip())
    return [piece for piece in pieces if piece]


def align_sentences(nasa_text: str, spanish_text: str) -> list[tuple[str, str]]:
    nasa_sentences = split_sentences(nasa_text)
    spanish_sentences = split_sentences(spanish_text)

    if len(nasa_sentences) == 1 and len(spanish_sentences) > 1:
        nasa_sentences = split_long_clause(nasa_sentences[0], len(spanish_sentences))
    if len(spanish_sentences) == 1 and len(nasa_sentences) > 1:
        spanish_sentences = split_long_clause(spanish_sentences[0], len(nasa_sentences))

    if len(nasa_sentences) == len(spanish_sentences):
        return list(zip(nasa_sentences, spanish_sentences))
    if len(nasa_sentences) == 1 and len(spanish_sentences) == 1:
        return [(nasa_text, spanish_text)]

    ratio = (sum(map(len, nasa_sentences)) or len(nasa_text)) / (
        sum(map(len, spanish_sentences)) or len(spanish_text)
    )
    nasa_count = len(nasa_sentences)
    spanish_count = len(spanish_sentences)

    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> tuple[float, tuple[tuple[str, str], ...]]:
        if i == nasa_count and j == spanish_count:
            return 0.0, ()

        best_cost = math.inf
        best_path: tuple[tuple[str, str], ...] = ()
        for nasa_take in range(1, 4):
            for spanish_take in range(1, 4):
                if i + nasa_take > nasa_count or j + spanish_take > spanish_count:
                    continue
                nasa_group = " ".join(nasa_sentences[i : i + nasa_take])
                spanish_group = " ".join(spanish_sentences[j : j + spanish_take])
                length_cost = abs(len(nasa_group) - ratio * len(spanish_group)) / max(
                    len(nasa_group), ratio * len(spanish_group), 1
                )
                merge_penalty = 0.10 * ((nasa_take - 1) + (spanish_take - 1))
                remaining_cost, remaining_path = dp(i + nasa_take, j + spanish_take)
                cost = length_cost + merge_penalty + remaining_cost
                if cost < best_cost:
                    best_cost = cost
                    best_path = ((nasa_group, spanish_group),) + remaining_path
        return best_cost, best_path

    return list(dp(0, 0)[1]) or [(nasa_text, spanish_text)]


def extract_book_blocks(pdf_path: Path, first_page: int, last_page: int) -> list[dict]:
    doc = fitz.open(pdf_path)
    blocks: list[dict] = []
    for page_number in range(first_page, last_page + 1):
        page = doc[page_number - 1]
        for block in page.get_text("blocks"):
            x0, y0, _x1, _y1, text, *_rest = block
            cleaned = clean(text)
            if valid_block(cleaned):
                blocks.append(
                    {
                        "page": page_number,
                        "x": x0,
                        "y": y0,
                        "text": cleaned,
                        "lang": classify(cleaned),
                    }
                )
    return blocks


def pair_block_lists(nasa_blocks: list[dict], spanish_blocks: list[dict]) -> list[tuple[str, str, int, int]]:
    if not nasa_blocks or not spanish_blocks:
        return []
    if len(nasa_blocks) == len(spanish_blocks):
        return [
            (nasa["text"], spanish["text"], nasa["page"], spanish["page"])
            for nasa, spanish in zip(nasa_blocks, spanish_blocks)
        ]

    def partition(blocks: list[dict], groups: int) -> list[list[dict]]:
        return [
            blocks[round(i * len(blocks) / groups) : round((i + 1) * len(blocks) / groups)]
            for i in range(groups)
        ]

    if len(nasa_blocks) < len(spanish_blocks):
        spanish_groups = partition(spanish_blocks, len(nasa_blocks))
        return [
            (
                nasa["text"],
                " ".join(block["text"] for block in spanish_group),
                nasa["page"],
                spanish_group[0]["page"],
            )
            for nasa, spanish_group in zip(nasa_blocks, spanish_groups)
            if spanish_group
        ]

    nasa_groups = partition(nasa_blocks, len(spanish_blocks))
    return [
        (
            " ".join(block["text"] for block in nasa_group),
            spanish["text"],
            nasa_group[0]["page"],
            spanish["page"],
        )
        for nasa_group, spanish in zip(nasa_groups, spanish_blocks)
        if nasa_group
    ]


def pair_book_blocks(blocks: list[dict]) -> list[tuple[str, str, int, int]]:
    pairs: list[tuple[str, str, int, int]] = []
    pending_lang: str | None = None
    pending_blocks: list[dict] = []

    def flush(lang: str, current_blocks: list[dict]) -> None:
        nonlocal pending_lang, pending_blocks
        if not pending_blocks or pending_lang == lang:
            return
        if pending_lang == "nasa_yuwe":
            pairs.extend(pair_block_lists(pending_blocks, current_blocks))
        else:
            pairs.extend(pair_block_lists(current_blocks, pending_blocks))
        pending_lang = None
        pending_blocks = []

    for page_number in sorted({block["page"] for block in blocks}):
        page_blocks = sorted(
            [block for block in blocks if block["page"] == page_number],
            key=lambda block: (block["y"], block["x"]),
        )
        languages = {block["lang"] for block in page_blocks}

        if languages == {"nasa_yuwe", "spanish"}:
            runs: list[tuple[str, list[dict]]] = []
            current_lang: str | None = None
            current_run: list[dict] = []
            for block in page_blocks:
                if current_lang is None or block["lang"] == current_lang:
                    current_run.append(block)
                    current_lang = block["lang"]
                else:
                    runs.append((current_lang, current_run))
                    current_lang = block["lang"]
                    current_run = [block]
            if current_run and current_lang:
                runs.append((current_lang, current_run))

            i = 0
            while i < len(runs) - 1:
                first_lang, first_blocks = runs[i]
                second_lang, second_blocks = runs[i + 1]
                if first_lang == second_lang:
                    i += 1
                    continue
                if first_lang == "nasa_yuwe":
                    pairs.extend(pair_block_lists(first_blocks, second_blocks))
                else:
                    pairs.extend(pair_block_lists(second_blocks, first_blocks))
                i += 2
        elif len(languages) == 1:
            lang = next(iter(languages))
            if pending_blocks and pending_lang != lang:
                flush(lang, page_blocks)
            elif pending_lang == lang:
                pending_blocks.extend(page_blocks)
            else:
                pending_lang = lang
                pending_blocks = list(page_blocks)

    return pairs


def extract_territorios() -> list[dict]:
    records: list[dict] = []
    for book_file, (first_page, last_page) in BOOK_RANGES.items():
        pdf_path = BOOK_DIR / book_file
        blocks = extract_book_blocks(pdf_path, first_page, last_page)
        block_pairs = pair_book_blocks(blocks)

        for nasa_text, spanish_text, nasa_page, spanish_page in block_pairs:
            for nasa_sentence, spanish_sentence in align_sentences(nasa_text, spanish_text):
                nasa_sentence = clean(nasa_sentence)
                spanish_sentence = clean(spanish_sentence)
                if len(nasa_sentence) < 16 or len(spanish_sentence) < 16:
                    continue
                records.append(
                    {
                        "nasa_yuwe": nasa_sentence,
                        "spanish": spanish_sentence,
                        "source": "territorios_narrados",
                        "domain": "literary",
                        "meta": {
                            "book": book_file.rsplit(".", 1)[0],
                            "nasa_page": nasa_page,
                            "spanish_page": spanish_page,
                            "repair": "layout_aware_2026_05",
                        },
                    }
                )
    return records


def extract_adres_segments() -> list[tuple[str, str]]:
    doc = fitz.open(ADRES_PDF)
    pending_spanish: list[str] = []
    segments: list[tuple[str, str]] = []

    for page_number in range(2, doc.page_count + 1):
        page = doc[page_number - 1]
        blocks = sorted(page.get_text("blocks"), key=lambda block: (block[1], block[0]))
        for block in blocks:
            _x0, _y0, _x1, _y1, text, *_rest = block
            cleaned = clean(text)
            if not valid_adres_block(cleaned):
                continue

            mixed_tail = "fortalecido e incluyente"
            if mixed_tail in cleaned:
                nasa_part, spanish_tail = cleaned.split(mixed_tail, 1)
                nasa_part = clean(nasa_part)
                spanish_tail = clean(mixed_tail + spanish_tail)
                if pending_spanish and nasa_part:
                    segments.append((" ".join(pending_spanish), nasa_part))
                    pending_spanish = []
                if spanish_tail:
                    pending_spanish.append(spanish_tail)
                continue

            lang = classify(cleaned)
            if lang == "spanish":
                pending_spanish.append(cleaned)
            elif pending_spanish:
                segments.append((" ".join(pending_spanish), cleaned))
                pending_spanish = []

    return segments


def extract_adres() -> list[dict]:
    records: list[dict] = []
    pending_spanish: list[str] = []
    pending_nasa: list[str] = []

    for spanish_segment, nasa_segment in extract_adres_segments():
        pending_spanish.append(spanish_segment)
        pending_nasa.append(nasa_segment)
        spanish_text = clean(" ".join(pending_spanish))
        nasa_text = clean(" ".join(pending_nasa))
        if ends_sentence(spanish_text):
            for nasa_sentence, spanish_sentence in align_sentences(nasa_text, spanish_text):
                nasa_sentence = clean(nasa_sentence)
                spanish_sentence = clean(spanish_sentence)
                if len(nasa_sentence) < 16 or len(spanish_sentence) < 16:
                    continue
                records.append(
                    {
                        "nasa_yuwe": nasa_sentence,
                        "spanish": spanish_sentence,
                        "source": "adres_health",
                        "domain": "government",
                        "meta": {"repair": "layout_aware_2026_05"},
                    }
                )
            pending_spanish = []
            pending_nasa = []

    return records


def is_americas_metadata_leak(record: dict) -> bool:
    if record.get("source") != "americasnlp_2024":
        return False
    nasa = clean(record.get("nasa_yuwe", ""))
    spanish = clean(record.get("spanish", ""))
    if nasa.lower() != spanish.lower() or len(spanish) <= 10:
        return False
    # Keep short lexical cognates; drop proper-name/title/footer rows from PDF front matter.
    return bool(
        re.search(r"\s", spanish)
        or re.search(r"[A-Z]{2,}", spanish)
        or spanish.endswith(".")
        or "Traducción" in spanish
    )


def load_existing_records() -> list[dict]:
    records = []
    with DATASET.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def write_dataset(records: list[dict]) -> None:
    with DATASET.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def update_summary(records: list[dict], repaired_counts: Counter) -> None:
    source_counts = Counter(record["source"] for record in records)
    domain_counts = Counter(record["domain"] for record in records)

    with SUMMARY.open(encoding="utf-8") as handle:
        summary = json.load(handle)

    summary["total_pairs"] = len(records)
    summary["by_source"] = dict(source_counts.most_common())
    summary["by_domain"] = dict(domain_counts.most_common())

    note = (
        "Repair 2026-05: replaced contaminated territorios_narrados and "
        "adres_health PDF extraction with layout-aware sentence/paragraph pairs; "
        f"current repaired counts are {repaired_counts['territorios_narrados']} "
        f"Territorios rows and {repaired_counts['adres_health']} ADRES rows, with "
        "AmericasNLP exact metadata/title leaks filtered."
    )
    notes = [existing for existing in summary.get("notes", []) if not existing.startswith("Repair 2026-05:")]
    notes.append(note)
    summary["notes"] = notes

    with SUMMARY.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> None:
    existing = load_existing_records()
    removed_counts: Counter = Counter()
    kept: list[dict] = []

    for record in existing:
        source = record.get("source")
        if source in {"territorios_narrados", "adres_health"} or is_americas_metadata_leak(record):
            removed_counts[source] += 1
        else:
            kept.append(record)

    repaired = extract_territorios() + extract_adres()
    repaired_counts = Counter(record["source"] for record in repaired)

    seen: set[str] = set()
    final_records: list[dict] = []
    for record in kept + repaired:
        key = dedup_key(record["nasa_yuwe"], record["spanish"])
        if key in seen:
            continue
        seen.add(key)
        final_records.append(record)

    write_dataset(final_records)
    update_summary(final_records, repaired_counts)

    print(f"Loaded records: {len(existing)}")
    print(f"Removed: {dict(removed_counts)}")
    print(f"Added repaired: {dict(repaired_counts)}")
    print(f"Wrote records: {len(final_records)}")


if __name__ == "__main__":
    main()
