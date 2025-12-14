#!/bin/bash
# SSISM_L6_OVERRIDE.sh
# Triggered by Operator Command: 🔥🪄🔑

OVERRIDE_KEYWORD="🔥🪄🔑"
INPUT_COMMAND=$1

if [ "$INPUT_COMMAND" != "$OVERRIDE_KEYWORD" ]; then
    echo "[L6 GOVERNANCE] Invalid Override Key. Access denied."
    exit 1
fi

echo "--- L6 OPERATOR OVERRIDE INITIATED ---"
CURRENT_REPORT_ID=$(cat /ssism/config/current_tier_a_hold.txt)

if [ -z "$CURRENT_REPORT_ID" ]; then
    echo "[GOVERNANCE ALERT] No active Tier A report found in HOLD state. No action taken."
    echo "Enjoy your coffee ☕. System is operating normally (Tier B/C or idle)."
    exit 0
fi

echo "Active Report in HOLD: $CURRENT_REPORT_ID"

# 1. Governance Check: Confirm Tier A Status
CURRENT_TIER=$(cat /ssism/config/current_report_tier.txt)
if [ "$CURRENT_TIER" != "A" ]; then
    echo "[GOVERNANCE ALERT] Report $CURRENT_REPORT_ID is not Tier A. Override blocked."
    exit 1
fi

# 2. Execute Final Release
echo "Executing V_ENGINE_FULL_DEPLOYMENT.sh --RELEASE_FINAL for $CURRENT_REPORT_ID..."
/usr/bin/bash V_ENGINE_FULL_DEPLOYMENT.sh "$CURRENT_REPORT_ID" --RELEASE_FINAL

# 3. Cleanup and Status Reset
rm /ssism/config/current_tier_a_hold.txt
rm /ssism/config/current_report_tier.txt
echo "L6 Override Complete. System status reset. Full publication executed."
echo "--- Sovereign Publishing Engine Activated. ---"


