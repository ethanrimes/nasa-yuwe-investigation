"""Generate INVENTORY.csv — machine-readable per-file inventory of the corpus.

Walks the entire nasa_yuwe_corpus/ tree (excluding self) and tags each file with:
  - category (top-level folder)
  - subcategory (immediate subfolder)
  - relative_path
  - filename
  - extension
  - size_bytes
  - content_kind  (parallel_csv, raw_html, audio_mp3, pdf_grammar, ...)
  - language(s)
  - origin_url    (best-effort; filled from per-file mapping where known)
  - notes
  - sentence_pairs (if applicable)

Run from repo root:  python _build_inventory.py
"""
from __future__ import annotations
import csv
import sys
import json
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "INVENTORY.csv"

# Best-effort origin/notes/lang map. Keyed by suffix-of-path so we can match
# across the moved layout cleanly.
META = {
    # 01_parallel_corpora
    "01_parallel_corpora/bible_nt_es_pbb.csv":
        ("parallel_corpus", "es+pbb", 7906,
         "Built locally from 02_bible_raw/ HTML. Wycliffe 1984 NT × Versión Biblia Libre (2018).",
         "https://eBible.org/Scriptures/pbb_html.zip + https://eBible.org/Scriptures/spavbl_html.zip"),
    "01_parallel_corpora/living_dictionaries_paez.csv":
        ("parallel_dict", "es+pbb+en", 3954,
         "Living Dictionaries Páez via Supabase paginated dump. Most entries cite Gerdel & Slocum 1983.",
         "https://livingdictionaries.app/nasa-yuwe-paez/entries"),
    "01_parallel_corpora/swarthmore_talking_dictionary.csv":
        ("parallel_dict", "es+pbb", 2324, "Swarthmore Talking Dictionary, browse-mode scrape.",
         "http://talkingdictionary.swarthmore.edu/paez/"),
    "01_parallel_corpora/swarthmore_talking_dictionary_full.csv":
        ("parallel_dict", "es+pbb", 3912, "Swarthmore Talking Dictionary, all-entries scrape.",
         "http://talkingdictionary.swarthmore.edu/paez/"),
    "01_parallel_corpora/broomva_translation_pbb_spa_train.parquet":
        ("parallel_corpus", "es+pbb", 2428, "broomva HF dataset train split.",
         "https://huggingface.co/datasets/Broomva/translation_pbb_spa"),
    "01_parallel_corpora/broomva_translation_pbb_spa_validation.parquet":
        ("parallel_corpus", "es+pbb", 607, "broomva HF dataset validation split.",
         "https://huggingface.co/datasets/Broomva/translation_pbb_spa"),
    "01_parallel_corpora/broomva_translation_pbb_spa_test.parquet":
        ("parallel_corpus", "es+pbb", 759, "broomva HF dataset test split.",
         "https://huggingface.co/datasets/Broomva/translation_pbb_spa"),
    "01_parallel_corpora/broomva_instruct_spa_pbb_train.parquet":
        ("parallel_corpus", "es+pbb", 7483,
         "broomva instruct dataset (Llama-2 INST format); incl. Constitution articles 1–40.",
         "https://huggingface.co/datasets/Broomva/instruct-spa-pbb"),
    # 02_bible_raw — single PDFs
    "02_bible_raw/pbb_traditional_orth/scriptureearth_complete_NT.pdf":
        ("bible_text", "pbb", None, "Wycliffe NT 1984, traditional orthography, combined PDF.",
         "https://www.scriptureearth.org/data/pbb/PDF/00-WNTpbb-web.pdf"),
    "02_bible_raw/pbb_new_orth/scriptureearth_complete_NT.pdf":
        ("bible_text", "pbb", None, "Wycliffe NT 2014, NEW orthography, combined PDF.",
         "https://www.scriptureearth.org/data/pbb/PDF/00-WNTpbbN-web.pdf"),
    "02_bible_raw/ot_stories/pbb_Dyusna-selpisaawesh_1993.pdf":
        ("bible_text", "pbb", None,
         "OT narrative summary (Gen–Kings stories). Second edition 1993.",
         "https://www.scriptureearth.org/data/pbb/PDF/pbb_Nasa_Dyusna-selpisaawesh_2ndEd_1993.pdf"),
    "02_bible_raw/creation/pbb_CREATION.pdf":
        ("bible_text", "pbb", None, "Standalone Creation account.",
         "https://www.scriptureearth.org/data/pbb/PDF/pbbCREATION.pdf"),
    # 04_government_legal
    "04_government_legal/constitution_1991/Constitucion_de_1991_Nasa_Yuwe_Uniandes.pdf":
        ("government_bilingual", "es+pbb", None,
         "1991 Colombian Constitution in Nasa Yuwe, CCELA translation 1994, digital re-release 2022.",
         "https://patrimoniodocumental.uniandes.edu.co/digital/collection/constitution"),
    "04_government_legal/consejo_de_estado/nasa_yuwe_institutional_overview.html":
        ("government_bilingual", "pbb", None,
         "Consejo de Estado institutional overview in Nasa Yuwe; text by Yaid Bolaños (Tumbichucue).",
         "https://www.consejodeestado.gov.co/2021/11/04/nasa-yuwe/index.htm"),
    "04_government_legal/procuraduria/Caracterizacion_NASA_YUWE_Procuraduria.pdf":
        ("government_bilingual", "es+pbb", None, "Procuraduría characterization of Nasa Yuwe.",
         "https://apps.procuraduria.gov.co/portal/media/file/Caracterizacion%20%20NASA%20YUWE.pdf"),
    "04_government_legal/adres/TEXTO_LENGUA_NASAYUWE_Adres.pdf":
        ("government_bilingual", "es+pbb", None, "ADRES (health admin) bilingual brochure.",
         "https://www.adres.gov.co/portal-del-ciudadano/Lenguas_nativas/TEXTO_LENGUA_NASAYUWE.pdf"),
    "04_government_legal/caroycuervo/Paez_CaroyCuervo.pdf":
        ("government_bilingual", "es", None,
         "Caro y Cuervo Páez overview (Ingrid Jung, 2023). About Nasa Yuwe, in Spanish.",
         "https://lenguasyliteraturasnativas.caroycuervo.gov.co/publicaciones/2023/11/paez.pdf"),
    # 05_bilingual_literature — Territorios Narrados
    "05_bilingual_literature/territorios_narrados/04-Ipx_kwet_pekuj-AlrededorTulpa.pdf":
        ("bilingual_book", "es+pbb", None, "Territorios Narrados #04 — Ipx Kwet Peku'j.",
         "https://archive.org/details/04-ipx-kwet-pekuj-alrededor-de-la-tulpa-edicion-bilingue-nasayuwe-espanol"),
    "05_bilingual_literature/territorios_narrados/06-Nasa_Ujunxin_Thegnxi-LeyendoVidaNasa.pdf":
        ("bilingual_book", "es+pbb", None, "Territorios Narrados #06.",
         "https://archive.org/details/06-nasa-ujunxin-thegnxi-leyendo-la-vida-nasa-edicion-bilingue-nasayuwe-espanol"),
    "05_bilingual_literature/territorios_narrados/09-Luucx_Pekuhn_Ujusaa-Chivito.pdf":
        ("bilingual_book", "es+pbb", None, "Territorios Narrados #09 — Chivito.",
         "https://archive.org/details/09-luucx-pekuhn-ujusaa-chivito-el-nino-viajero-edicion-bilingue-nasayuwe-espanol"),
    "05_bilingual_literature/territorios_narrados/10-Lxan_Nasa_Pal-AlvaroMojana.pdf":
        ("bilingual_book", "es+pbb", None, "Territorios Narrados #10 — Álvaro y la Mojana.",
         "https://archive.org/details/10-lxan-nasa-pal-kubxyac-alvaro-nasa-pal-y-la-mojana-edicion-bilingue-nasayuwe-espanol"),
    "05_bilingual_literature/Putunkaa_Serruma_5etnias_ICBF.pdf":
        ("bilingual_book", "es+piap+arh+kbh+huu+guc", None,
         "WARNING: covers Piapoco/Arhuaco/Kamëntsá/Uitoto/Wayúu — NOT Nasa Yuwe.",
         "https://maguare.gov.co/wp-content/uploads/2017/12/493_putunka-serruma.pdf"),
    # 06_academic_papers — key theses
    "06_academic_papers/theses/DiazMontenegro_2019_Munchique_thesis.pdf":
        ("thesis", "es+pbb", None,
         "Díaz Montenegro 2019 PhD Lyon 2 — comprehensive Munchique variety description.",
         "https://theses.hal.science/tel-02469166"),
    "06_academic_papers/americasNLP/AmericasNLP_2024_TranslationColombianIndigenous_paper.pdf":
        ("paper", "en", None, "Robles et al. AmericasNLP 2024 — the paper this work extends.",
         "https://aclanthology.org/2024.americasnlp-1.2/"),
    "06_academic_papers/americasNLP/AmericasNLP_2025_findings.pdf":
        ("paper", "en", None, "AmericasNLP 2025 shared task findings.",
         "https://aclanthology.org/2025.americasnlp-1.16/"),
    "06_academic_papers/grammars/Rojas_Desde_arriba_y_por_abajo_alfabeto_nasa.pdf":
        ("paper", "es", None, "Rojas Curieux 2002 CILLA paper on the Nasa Yuwe alphabet unification.",
         "https://hdl.handle.net/2152/120791"),
    # 07_pedagogical
    "07_pedagogical/cric_uaiin_pebi/CRIC_UAIIN_PEBI_Catalogo_2024.pdf":
        ("catalog", "es", None, "PEBI-CRIC 2024 educational materials catalog.",
         "https://sia.uaiinpebi-cric.edu.co/static/img/IMAGENES_CDI/CATALOGO_CDI_UAIIN_CRIC_2024.pdf"),
}


def detect_kind(path: Path) -> tuple[str, str]:
    """Return (content_kind, languages)."""
    ext = path.suffix.lower()
    name = path.name.lower()
    rel_str = str(path.relative_to(ROOT)).replace("\\", "/")

    # Authoritative override from META
    if rel_str in META:
        kind = META[rel_str][0]
        lang = META[rel_str][1]
        return kind, lang

    # Heuristics
    if ext == ".csv":
        return "csv_data", "?"
    if ext == ".parquet":
        return "parquet_data", "?"
    if ext == ".pdf":
        if "/03_dictionaries/" in rel_str:
            return "pdf_dictionary", "es+pbb"
        if "/04_government_legal/" in rel_str:
            return "pdf_government", "es+pbb"
        if "/05_bilingual_literature/" in rel_str:
            return "pdf_bilingual_book", "es+pbb"
        if "/06_academic_papers/" in rel_str:
            return "pdf_academic", "es"
        if "/07_pedagogical/" in rel_str:
            return "pdf_pedagogical", "es+pbb"
        if "/02_bible_raw/" in rel_str:
            return "pdf_bible", "pbb"
        return "pdf_other", "?"
    if ext in (".htm", ".html"):
        return "html_scrape", "?"
    if ext == ".epub":
        return "epub_bible", "pbb" if "pbb" in name else "es"
    if ext == ".zip":
        return "zip_bundle", "?"
    if ext in (".mp3", ".ogg", ".wav", ".flac"):
        return "audio", "pbb"
    if ext == ".json":
        return "json_data", "?"
    if ext == ".txt":
        return "text", "?"
    if ext == ".py":
        return "script_python", "n/a"
    if ext == ".sh":
        return "script_shell", "n/a"
    if ext == ".tgz" or ext == ".gz":
        return "archive_tarball", "?"
    if ext == ".xlsx" or ext == ".docx":
        return "office_doc", "?"
    if ext == ".ipynb":
        return "notebook", "n/a"
    if ext == ".md":
        return "doc_markdown", "?"
    return "other", "?"


def main() -> None:
    rows = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir():
            continue
        if path.name == "INVENTORY.csv" or path.name == "_build_inventory.py":
            continue
        try:
            size = path.stat().st_size
        except OSError:
            continue
        rel = path.relative_to(ROOT)
        rel_str = str(rel).replace("\\", "/")
        parts = rel_str.split("/")
        category = parts[0] if len(parts) > 0 else ""
        # subcategory only applies when the file lives in a real subfolder
        subcategory = parts[1] if len(parts) > 2 else ""
        kind, lang = detect_kind(path)
        meta = META.get(rel_str)
        pairs = meta[2] if meta else ""
        notes = meta[3] if meta else ""
        origin = meta[4] if meta else ""
        rows.append({
            "category": category,
            "subcategory": subcategory,
            "relative_path": rel_str,
            "filename": path.name,
            "extension": path.suffix.lstrip(".").lower(),
            "size_bytes": size,
            "content_kind": kind,
            "languages": lang,
            "sentence_pairs": pairs,
            "origin_url": origin,
            "notes": notes,
        })
    fields = ["category","subcategory","relative_path","filename","extension",
              "size_bytes","content_kind","languages","sentence_pairs","origin_url","notes"]
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {OUT} ({len(rows)} files)")

    # Print category summary
    from collections import Counter
    cat_size: dict[str, int] = {}
    cat_count: Counter[str] = Counter()
    for r in rows:
        cat_count[r["category"]] += 1
        cat_size[r["category"]] = cat_size.get(r["category"], 0) + r["size_bytes"]
    print("\nPer-category summary:")
    for cat in sorted(cat_count):
        sz_mb = cat_size[cat] / 1_048_576
        print(f"  {cat:<30} {cat_count[cat]:>5} files  {sz_mb:>10.1f} MB")


if __name__ == "__main__":
    main()
