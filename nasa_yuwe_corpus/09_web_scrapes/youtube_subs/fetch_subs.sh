#!/usr/bin/env bash
# Fetch subtitles for known Nasa Yuwe YouTube content.
#
# YouTube now requires authenticated cookies even for subtitle listings, so this
# must be run on a machine where you are logged in to YouTube in a browser.
#
# Prereqs:
#   pip install yt-dlp
#   (your browser logged into youtube.com)
#
# Usage:
#   ./fetch_subs.sh chrome      # or edge, firefox, brave, opera
#
# What it does:
#   * Probes each target with --list-subs (no video download, no audio)
#   * Then downloads any manual or auto-generated Spanish/English subtitles
#   * Stores .vtt + .info.json files in this directory
#
# Subtitle reality check: most of these channels rely on YouTube's auto-Spanish
# transcription of mixed Spanish/Nasa-Yuwe audio. Expect:
#   - the Spanish side to be mostly accurate
#   - the Nasa Yuwe side to be auto-transcribed AS IF it were Spanish (garbled)
# So treat this as supplementary data; the Bible/Constitution/dictionary corpora
# are far higher quality.

BROWSER="${1:-chrome}"
OUT_DIR="$(dirname "$0")"
cd "$OUT_DIR" || exit 1

YTDLP="python -m yt_dlp"
COMMON_OPTS=(
  --cookies-from-browser "$BROWSER"
  --skip-download
  --write-subs
  --write-auto-subs
  --sub-langs "es.*,en.*,pbb.*"
  --convert-subs vtt
  --write-info-json
  --sleep-requests 1
  --no-warnings
  -o "%(uploader)s/%(title)s [%(id)s].%(ext)s"
)

# Specific videos called out by the resource guides
VIDEOS=(
  # Joser channel highlights (specific videos)
  "https://www.youtube.com/watch?v=5quYl8ptDZ8"  # Repaso de los números en Nasa Yuwe
  "https://www.youtube.com/watch?v=SVar-rcVmk8"  # Pronunciación del saludo
  "https://www.youtube.com/watch?v=JtXnIL6CT0c"  # Repaso final consonantes
  "https://www.youtube.com/watch?v=hkYmaK6iKUs"  # y cómo es ella
  "https://www.youtube.com/watch?v=uv9uNDiClbk"  # Responde qué te gusta hacer
  # Documentary / cultural
  "https://www.youtube.com/watch?v=K2eMDeJSbaw"  # Lenguas indígenas: Nasa Yuwe (Norte del Cauca)
  "https://www.youtube.com/watch?v=W0mYoH80wMc"  # Kwe´sx Yuwe Fxiwa´s Kçxhãçxhan
  "https://www.youtube.com/watch?v=NVuEaovtE_0"  # Dos idiomas — docente indígena
  "https://www.youtube.com/watch?v=4YyAHlUGmig"  # Derechos en el Territorio
  # Films from UNESCO OIFF / cortometrajes (worth a look)
  # The original Reddit-posted Nasa Yuwe lesson:
  # (added as you discover more)
)

# Whole channels / playlists — broad sweeps
CHANNELS=(
  "https://www.youtube.com/@Joserteense%C3%B1a.25/videos"
  "https://www.youtube.com/playlist?list=PL_iSFODPZG0DunxV_h3DZKf9iW8XDUzS_"  # NasaYuwe playlist
  # Other channels mentioned in the resource guides; uncomment as desired:
  # "https://www.youtube.com/@FamiliaChilo"
  # "https://www.youtube.com/results?search_query=tejido+nasa+yuwe+4+payumat"
  # "https://www.youtube.com/@NasaCxhaCxha"
  # "https://www.youtube.com/@VocesComunes"
)

echo "==> Probing subtitle availability"
for url in "${VIDEOS[@]}"; do
  echo ""
  echo "## $url"
  $YTDLP --cookies-from-browser "$BROWSER" --list-subs --skip-download --no-warnings "$url" 2>&1 | head -20
done

echo ""
echo "==> Downloading subtitles (videos)"
for url in "${VIDEOS[@]}"; do
  $YTDLP "${COMMON_OPTS[@]}" "$url"
done

echo ""
echo "==> Downloading subtitles (channels/playlists)"
for url in "${CHANNELS[@]}"; do
  $YTDLP "${COMMON_OPTS[@]}" --playlist-end 200 "$url"
done

echo ""
echo "==> Done. Inventory:"
find . -name "*.vtt" | wc -l
