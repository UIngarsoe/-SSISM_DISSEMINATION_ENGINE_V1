#!/usr/bin/env bash
# ssism_engine.sh
# SSISM Distributed Vigilance Engine — Grand Bargain Logic (V1.0.0)

# Exit immediately if a command exits with a non-zero status or if a variable is unset.
set -euo pipefail

# --- Configuration & Metadata ---
ENGINE_NAME="SSISM Distributed Vigilance Engine"
VERSION="V1.0.0"
DEFAULT_INPUT="indicators.txt"
# Alerts are written to the 'alerts' directory, creating it if it doesn't exist.
OUTDIR="${OUTDIR:-alerts}"

CHANNELS=("Telegram" "X" "IPFS" "Tor" "Local-Print")
TAGS="#IrrawaddyFiles #UnityWarning #FederalPush #ThreeHours"

# --- Utility Functions ---

# Generate an ISO 8601 UTC timestamp.
timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

# Hash the generated alert file. Supports sha256sum (Linux) or shasum -a 256 (macOS).
hash_file() {
  local f="$1"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$f" > "$f.sha256"
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$f" > "$f.sha256"
  else
    echo "[WARN] No sha256 tool found; skipping hash for $f" >&2
  fi
}

# Generic function to format and write an alert to a file.
emit_alert() {
  local title="$1"; shift
  local actions=("$@")

  mkdir -p "$OUTDIR"

  local ts; ts="$(timestamp)"
  # Sanitize title for filename
  local fname_base
  fname_base="$(echo "$title" | tr '[:space:]/' '_' | tr -cd '[:alnum:]_-')"
  local outfile="$OUTDIR/${ts}_${fname_base}.txt"

  {
    echo "--- ${title} ---"
    echo "Timestamp: $ts"
    echo "Engine: $ENGINE_NAME $VERSION"
    echo ""
    echo "Action Points:"
    for a in "${actions[@]}"; do
      echo "- $a"
    done
    echo ""
    echo "Dissemination Channels: ${CHANNELS[*]}"
    echo "Dissemination Tags: $TAGS"
  } | tee "$outfile"

  hash_file "$outfile"
  echo "[OK] Alert artifact created: $outfile"
  echo "[OK] Hash created: $outfile.sha256"
}

# Check if a pattern is found in the evidence blob (case-insensitive grep).
hit() {
  local pattern="$1"; local blob="$2"
  # -i: case-insensitive; -q: quiet (suppress output)
  echo "$blob" | grep -iqE "$pattern"
}

# --- Scenario Branches ---

branch_partition_accepted() {
  emit_alert "UNITY WARNING — Partition Acceptance Detected" \
    "Publish Federal Counter-Proposal across ethnic blocs" \
    "Freeze unilateral local deals; route talks through unity council" \
    "Amplify joint ops cadence; maintain shared logistics" \
    "Push scout encryption guide; compress comm windows"
}

branch_partition_rejected() {
  emit_alert "FEDERAL PUSH — Leverage Maintained" \
    "Publish Federal Union Roadmap with timeline and safeguards" \
    "Expose CMEC risk pathways; diversify economic lifelines" \
    "Coordinate narrative against partition; reinforce shared objectives" \
    "Maintain disciplined info ops; avoid premature victory claims"
}

branch_khin_nyunt_revival() {
  emit_alert "LEGITIMACY DENIAL PACK — Paranoia Theater" \
    "Deny sham election; document coercion and conscription" \
    "Amplify defections and collapse indicators (e.g., logistics failure)" \
    "Publish factional leak analyses; track censorship spikes" \
    "Protect civilians; de-escalate local flashpoints"
}

branch_china_ultimatum() {
  emit_alert "ECON COERCION WINDOW — Ultimatum Detected" \
    "Publish sanctions routing and resilience brief for economic actors" \
    "Expand mirror nodes (IPFS/Tor); print local summaries for offline access" \
    "Map blockade dependencies; pre-position alternatives (e.g., medical supplies)" \
    "Engage diaspora channels; maintain accurate translation parity"
}

branch_mi_collapse() {
  emit_alert "SAFETY RITUAL — MI Blind Spots Widening" \
    "Rotate routes and routines; shorten exposure windows" \
    "Enforce redaction discipline; remove PII in field notes" \
    "Train scouts on OPSEC; refresh encryption keys for 'Delta Ghost Map'" \
    "Archive hashes; mirror essential files (doctrine, maps)"
}

# --- Main Engine Logic ---

run_engine() {
  local infile="${1:-$DEFAULT_INPUT}"
  echo "--- $ENGINE_NAME $VERSION ---"
  echo "Reading indicators from: $infile"

  if [[ ! -f "$infile" ]]; then
    echo "[FATAL] Indicators file not found: $infile" >&2
    echo "Please create a file named 'indicators.txt' with evidence lines." >&2
    exit 1
  fi

  local evidence; evidence="$(cat "$infile")"
  local fired=0

  # Order matters: check highest-risk, most specific scenarios first.
  # Using || true to prevent 'set -e' from exiting on failed grep (no match)
  hit "partition ultimatum|cmec guarantee|deadline|blockade" "$evidence" && { branch_china_ultimatum; fired=1; } || true
  hit "ceasefire boundaries|accept partition|regional autonomy deal" "$evidence" && { branch_partition_accepted; fired=1; } || true
  hit "regime[- ]change rhetoric|advance beyond borders|delta offensive|magway proximity" "$evidence" && { branch_partition_rejected; fired=1; } || true
  hit "sham election|conscription surge|paranoid orders|khin nyunt revival" "$evidence" && { branch_khin_nyunt_revival; fired=1; } || true
  hit "warrants high.*leaders uncaught|defector note|mi blind|intelligence collapse" "$evidence" && { branch_mi_collapse; fired=1; } || true

  if [[ "$fired" -eq 0 ]]; then
    emit_alert "STATUS — No Triggers Fired (Vigilance Maintained)" \
      "Review indicators; raise confidence or refine patterns" \
      "Collect additional signals; widen time window" \
      "Maintain mirrors and hashes; hold vectors ('Doing Nothing as Value' protocol)"
  fi

  echo ""
  echo "[DONE] Engine run complete. Check the '$OUTDIR' directory for artifacts."
}

# Run the engine with the first argument as the input file, or use the default.
run_engine "${1:-}"
