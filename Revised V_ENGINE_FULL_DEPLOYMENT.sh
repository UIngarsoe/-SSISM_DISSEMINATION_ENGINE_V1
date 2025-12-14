# ... (inside the else block of V_ENGINE_FULL_DEPLOYMENT.sh) ...

    # 1. Execute Tier B functions
    ./V_ENGINE_LIMITED_DEPLOYMENT.sh $REPORT_ID
    
    # --- State Saving for L6 Override ---
    mkdir -p /ssism/config
    echo "$REPORT_ID" > /ssism/config/current_tier_a_hold.txt
    echo "A" > /ssism/config/current_report_tier.txt
    # -----------------------------------
    
    echo "ACTION REQUIRED: Report is in Tier A. Full Public Release is held."
    echo "Please perform Morning Ritual Coffee Review. Use the L6 Override command to proceed."
    
