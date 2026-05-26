#!/usr/bin/env bash
# Pulls all entries from the Supabase-backed nasa-yuwe-páez Living Dictionary
set -e
SUPABASE_URL="https://actkqboqpzniojhgtqzw.supabase.co"
ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFjdGtxYm9xcHpuaW9qaGd0cXp3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDEzOTQ0MzEsImV4cCI6MjAxNjk3MDQzMX0.KxeGK8Dnyg_BU9_eqtlNqbTyuPpmW6Dwasld1-HOiyE"
DICT="nasa-yuwe-p%C3%A1ez"
OUT_DIR="/q/nasa-yuwe-investigation/nasa_yuwe_materials/dictionaries/raw/supabase_paez"
mkdir -p "$OUT_DIR"

# Pull entries in pages of 500 using offset/limit (no embedded join)
SELECT_ENTRIES="id,dictionary_id,lexeme,phonetic,interlinearization,morphology,notes,sources,scientific_names,deleted"
PAGE=0
LIMIT=500
TOTAL=4500

while [ $((PAGE*LIMIT)) -lt $TOTAL ]; do
  OFFSET=$((PAGE*LIMIT))
  OUT="$OUT_DIR/entries_${OFFSET}.json"
  echo "Entries offset=$OFFSET..."
  /mingw64/bin/curl -sSL --max-time 60 \
    -H "apikey: $ANON_KEY" \
    -H "Authorization: Bearer $ANON_KEY" \
    "$SUPABASE_URL/rest/v1/entries?dictionary_id=eq.$DICT&select=$SELECT_ENTRIES&order=id&limit=$LIMIT&offset=$OFFSET" \
    -o "$OUT"
  COUNT=$(grep -o '"id":"[^"]*"' "$OUT" | wc -l)
  SIZE=$(wc -c < "$OUT")
  echo "  bytes=$SIZE entries=$COUNT"
  if [ "$COUNT" -lt 10 ] && [ "$OFFSET" -gt 0 ]; then break; fi
  PAGE=$((PAGE+1))
  sleep 0.3
done

# Get senses paged
echo "Fetching senses (paged)..."
SP=0
SLIMIT=2000
while [ $SP -lt 6 ]; do
  SOFF=$((SP*SLIMIT))
  OUT="$OUT_DIR/senses_${SOFF}.json"
  /mingw64/bin/curl -sSL --max-time 60 \
    -H "apikey: $ANON_KEY" \
    -H "Authorization: Bearer $ANON_KEY" \
    "$SUPABASE_URL/rest/v1/senses?select=id,entry_id,glosses,parts_of_speech,definition,semantic_domains&order=entry_id&limit=$SLIMIT&offset=$SOFF" \
    -o "$OUT"
  COUNT=$(grep -o '"id":"[^"]*"' "$OUT" | wc -l)
  echo "  senses offset=$SOFF count=$COUNT"
  if [ "$COUNT" -lt 10 ]; then break; fi
  SP=$((SP+1))
  sleep 0.3
done

echo "Done."
ls -la "$OUT_DIR/"
