"""Extract aligned verse pairs from eBible.org HTML dumps.

Produces a parallel CSV (Spanish ↔ Nasa Yuwe / Páez NT) by walking each book's
chapter files and pairing verses by chapter + verse id.

Source data:
  pbb_html/    — Páez NT (Wycliffe 1984), language="pbb"
  spavbl_html/ — Versión Biblia Libre (Spanish), language="es"

Output:
  parallel_nt_es_pbb.csv  — columns: book, chapter, verse, spanish, nasa_yuwe
"""
from __future__ import annotations

import csv
import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).parent
NY_DIR = ROOT / "pbb_html"
ES_DIR = ROOT / "spavbl_html"
OUT_CSV = ROOT / "parallel_nt_es_pbb.csv"

NT_BOOKS = [
    "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH",
    "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS",
    "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV",
]


class VerseExtractor(HTMLParser):
    """Walks an eBible chapter HTML file and emits {verse_no: text} dicts.

    Verses are delimited by <span class="verse" id="VN">N </span>. Footnotes
    (<a class="notemark"> with nested <span class="popup">) are stripped.
    """

    def __init__(self) -> None:
        super().__init__()
        self.verses: dict[int, list[str]] = {}
        self.current_verse: int | None = None
        self.in_body = False
        self.skip_depth = 0   # for stripping footnotes / popups / nav
        self.in_chapter = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        cls = (a.get("class") or "")
        if tag == "div" and "main" in cls.split():
            self.in_body = True
            return
        if not self.in_body:
            return
        if tag == "ul" and "tnav" in cls.split():
            self.skip_depth = max(self.skip_depth, 1)
            self._nav = True
            return
        if tag == "div" and any(c in cls.split() for c in ("footnote", "copyright")):
            self.skip_depth += 100
            return
        if tag in ("a", "span") and any(c in cls.split() for c in ("notemark", "popup", "fr", "fk", "ft")):
            self.skip_depth += 1
            return
        if tag == "span" and "verse" in cls.split():
            vid = a.get("id", "")
            m = re.match(r"V(\d+)", vid)
            if m:
                self.current_verse = int(m.group(1))
                self.verses.setdefault(self.current_verse, [])
                self.skip_depth += 1   # the inner "N " text is the verse number
                self._verse_num_open = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "ul" and getattr(self, "_nav", False):
            self.skip_depth = max(0, self.skip_depth - 1)
            self._nav = False
            return
        if tag == "div":
            # footnotes/copyright open with +100 sentinel
            if self.skip_depth >= 100:
                self.skip_depth -= 100
                return
        if tag in ("a", "span"):
            if getattr(self, "_verse_num_open", False) and tag == "span":
                # closes the inner verse-number span
                self._verse_num_open = False
                self.skip_depth = max(0, self.skip_depth - 1)
                return
            if self.skip_depth > 0:
                self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.in_body or self.skip_depth > 0 or self.current_verse is None:
            return
        self.verses[self.current_verse].append(data)


def extract_chapter(path: Path) -> dict[int, str]:
    parser = VerseExtractor()
    parser.feed(path.read_text(encoding="utf-8"))
    out: dict[int, str] = {}
    for v, parts in parser.verses.items():
        text = "".join(parts)
        # collapse whitespace, strip NBSP and stray verse-number residue
        text = text.replace(" ", " ")
        text = re.sub(r"\s+", " ", text).strip()
        # In some chapters the verse number leaks (e.g. "12  Aça'..."); strip
        # a leading bare integer that matches the verse id.
        text = re.sub(rf"^{v}\s+", "", text)
        if text:
            out[v] = text
    return out


def collect(lang_dir: Path) -> dict[tuple[str, int, int], str]:
    rows: dict[tuple[str, int, int], str] = {}
    for book in NT_BOOKS:
        for chap_file in sorted(lang_dir.glob(f"{book}[0-9][0-9].htm")):
            m = re.match(rf"{book}(\d+)\.htm", chap_file.name)
            if not m:
                continue
            chap = int(m.group(1))
            for verse, text in extract_chapter(chap_file).items():
                rows[(book, chap, verse)] = text
    return rows


def main() -> None:
    print(f"Reading Nasa Yuwe NT from {NY_DIR}…")
    ny = collect(NY_DIR)
    print(f"  {len(ny)} verses")
    print(f"Reading Spanish NT from {ES_DIR}…")
    es = collect(ES_DIR)
    print(f"  {len(es)} verses")

    pairs = sorted(set(ny) & set(es))
    print(f"Aligned verses: {len(pairs)}")

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["book", "chapter", "verse", "spanish", "nasa_yuwe"])
        for key in pairs:
            book, chap, verse = key
            w.writerow([book, chap, verse, es[key], ny[key]])
    print(f"Wrote {OUT_CSV}")

    # Coverage report
    by_book: dict[str, int] = {}
    for (book, _, _) in pairs:
        by_book[book] = by_book.get(book, 0) + 1
    print("\nPer-book verse counts:")
    for book in NT_BOOKS:
        print(f"  {book}: {by_book.get(book, 0)}")


if __name__ == "__main__":
    main()
