#!/usr/bin/env bash
# build_article.sh
# Usage:
# ./build_article.sh "IR-2025-12-08-YeBilu-Assault" "Escalating Resistance: The Ye Bilu Assault..." "SSISM Threat Intelligence Unit" "2025-12-08" "IR-2025-12-08-YeBilu-Assault" "Myanmar Conflict / Field Intelligence" "['SSISM','Myanmar']" "UIngarsoe/-SSISM_DISSEMINATION_ENGINE_V1" "CC BY-NC-SA 4.0" "content.md"

set -e

OUT_BASENAME="$1"    # e.g. IR-2025-12-08-YeBilu-Assault
TITLE="$2"
AUTHOR="$3"
DATE="$4"            # 2025-12-08 (ISO)
VERSION="$5"
CATEGORY="$6"
TAGS="$7"            # e.g. "['SSISM','Myanmar']"
REPO="$8"
LICENSE="$9"
CONTENT_FILE="${10}"

TEMPLATE="article_template.html"
TMPFILE="$(mktemp --suffix=.html)"
OUTFILE="${OUT_BASENAME}.html"

if [ ! -f "$TEMPLATE" ]; then
  echo "Template $TEMPLATE not found!"
  exit 1
fi

if [ ! -f "$CONTENT_FILE" ]; then
  echo "Content file $CONTENT_FILE not found!"
  exit 1
fi

# Read content (preserve newlines)
CONTENT_RAW="$(sed 's/$/\
/' "$CONTENT_FILE" | sed ':a;N;$!ba;s/\n/\
/g')"

# Build human date (same as date here)
DATE_HUMAN="$DATE"

# Perform replacements into a temp file
awk -v title="$TITLE" -v author="$AUTHOR" -v date="$DATE" -v date_human="$DATE_HUMAN" -v version="$VERSION" \
    -v category="$CATEGORY" -v tags="$TAGS" -v repo="$REPO" -v license="$LICENSE" \
    -v content="$(awk '{printf "%s\\n", $0}' "$CONTENT_FILE")" \
'{
  gsub("{{TITLE}}", title);
  gsub("{{AUTHOR}}", author);
  gsub("{{DATE}}", date);
  gsub("{{DATE_HUMAN}}", date_human);
  gsub("{{VERSION}}", version);
  gsub("{{CATEGORY}}", category);
  gsub("{{TAGS}}", tags);
  gsub("{{REPOSITORY}}", repo);
  gsub("{{LICENSE}}", license);
  # Content placeholder (this uses a marker line to insert later)
  print $0
}' "$TEMPLATE" > "$TMPFILE"

# Replace the content marker by a safer method:
# we will replace the literal line that has {{CONTENT}} with the content file
awk -v contentfile="$CONTENT_FILE" '
  BEGIN{ inserted=0 }
  {
    if (index($0,"{{CONTENT}}")>0 && inserted==0) {
      while((getline line < contentfile) > 0) {
        print line
      }
      inserted=1
    } else {
      print $0
    }
  }
' "$TMPFILE" > "${TMPFILE}.2"

# Compute SHA-256 of the final file (but first create a provisional output)
mv "${TMPFILE}.2" "$OUTFILE"

# Compute SHA-256 (portable)
if command -v sha256sum >/dev/null 2>&1; then
  SHA256="$(sha256sum "$OUTFILE" | awk '{print $1}')"
elif command -v shasum >/dev/null 2>&1; then
  SHA256="$(shasum -a 256 "$OUTFILE" | awk '{print $1}')"
else
  echo "No SHA-256 utility found. Install coreutils or use shasum."
  exit 1
fi

# Replace placeholder in-file (safely)
# Use python (safer for inplace replacement)
python3 - <<PY
from pathlib import Path
p=Path("$OUTFILE")
s=p.read_text(encoding="utf-8")
s=s.replace("<PLACEHOLDER_SHA256>", "$SHA256")
s=s.replace('PENDING', 'Integrity Verified')
p.write_text(s, encoding="utf-8")
print("Inserted SHA-256:", "$SHA256")
PY

echo "Built file: $OUTFILE"
