# --- 3. SECURITY VULNERABILITY ASSESSMENT (SEC-VULN) REFINED ---

SEC_DATA_SOURCES="Infra_Integrity_Checks, IDP_Location_Streams, Conflict_Event_Logs, Earthquake_Damage_Reports"
MATRIX_OUTPUT="${OUTPUT_DIR}/disaster_resilience_matrix_${DATE_STAMP}.geojson"

Echo "[TASK] Starting DISASTER_RESILIENCE_MATRIX_GENERATOR." | tee -a "$LOG_FILE"

# --- Sub-Engine 3.1: Critical Infrastructure Fragility Index (CIFI) ---
Run_cifi_assessment() {
    $V_ENGINE_ML_CLASSIFIER \
        --input-data "$SEC_DATA_SOURCES" \
        --model "CIFI_Damage_Resilience_v4.0" \
        --metrics "PowerGrid_Failure_Prob, HealthFacility_Integrity, RoadNetwork_Redundancy" \
        --output-layer "CIFI_SCORE_LAYER"
}

# --- Sub-Engine 3.2: Humanitarian Access Mapper (HAM) ---
Run_ham_assessment() {
    $V_ENGINE_GEOSPATIAL \
        --layer "IDP_Location_Streams" \
        --density-threshold "10000_per_sq_km" \
        --output-layer "IDP_DENSITY_LAYER"

    $V_ENGINE_GEOSPATIAL \
        --layer "Conflict_Event_Logs" \
        --buffer-zone "5km_Blockade" \
        --output-layer "CONFLICT_BLOCKADE_LAYER"
}

# --- Sub-Engine 3.3: Matrix Fusion and Metta-Audit Routing ---
Run_matrix_fusion() {
    Echo "[TASK] Fusing CIFI, IDP Density, and Conflict Blockade Layers." | tee -a "$LOG_FILE"

    $V_ENGINE_GEOSPATIAL_FUSION \
        --layers "CIFI_SCORE_LAYER, IDP_DENSITY_LAYER, CONFLICT_BLOCKADE_LAYER" \
        --algorithm "Weighted_Priority_Metric" \
        --metric-name "AID_PRIORITY_SCORE" \
        --output-format "GEOJSON" \
        > "$MATRIX_OUTPUT"

    $V_ENGINE_ROUTER \
        --input-matrix "$MATRIX_OUTPUT" \
        --start-nodes "Thailand_Border_Crossing, Laos_Logistics_Hub" \
        --optimization "Shortest_Safe_Route_(Low_Conflict_Inhibitor)" \
        --output-routes "${OUTPUT_DIR}/metta_audit_routes_${DATE_STAMP}.kml"
}

Run_cifi_assessment
Run_ham_assessment
Run_matrix_fusion

Echo "[SUCCESS] Disaster Resilience Matrix Generated: ${MATRIX_OUTPUT}" | tee -a "$LOG_FILE"
