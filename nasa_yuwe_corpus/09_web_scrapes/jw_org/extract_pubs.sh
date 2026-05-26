#!/bin/bash
# Extract publication URLs and titles from category pages
set -e

BASE_DIR="/q/nasa-yuwe-investigation/nasa_yuwe_materials/jw_org"
cd "$BASE_DIR"

# Output: category|pub_code|title|url
> raw/all_pubs.tsv

for f in raw/cat_bible.html raw/cat_magazines.html raw/cat_brochures.html raw/cat_programs.html raw/cat_books.html raw/cat_tracts.html raw/cat_other.html; do
    cat="${f#raw/cat_}"
    cat="${cat%.html}"
    # Use awk to extract href + title pairs
    python3 -c "
import re, sys, html
content = open('$f', encoding='utf-8').read()
# Find <a href=\"/pbb/wol/publication/r345/lp-paz/CODE\" ... title in cardLine1
pattern = re.compile(r'<a href=\"(/pbb/wol/publication/r345/lp-paz/[^\"]+)\"[^>]*>.*?cardLine1.*?>\s*<span[^>]*></span>\s*(.*?)\s*</div>', re.DOTALL)
for m in pattern.finditer(content):
    url = m.group(1)
    title = re.sub(r'\s+', ' ', html.unescape(m.group(2))).strip()
    code = url.rsplit('/', 1)[-1]
    print(f'$cat\t{code}\t{title}\t{url}')
" >> raw/all_pubs.tsv
done

echo "Total publications found:"
wc -l raw/all_pubs.tsv
echo "By category:"
cut -f1 raw/all_pubs.tsv | sort | uniq -c
