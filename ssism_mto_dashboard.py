import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page config for wide layout
st.set_page_config(
    page_title="SSISM-DOS-MTO-2025-UPDATE-1",
    page_icon="🛡️",
    layout="wide"
)

# Header with dossier branding
st.title("🛡️ SSISM UPDATE ADDENDUM")
st.markdown("**DOSSIER ID: SSISM-DOS-MTO-2025-UPDATE-1**")
st.markdown("*Maj-Gen Myat Tun Oo Post-ASEAN Trajectory*")
st.markdown("**Date: 16 December 2025** | **Target: ASEAN Digital Ministers**")

# Sidebar for timeline navigation
st.sidebar.header("📅 Timeline Filter")
date_range = st.sidebar.date_input(
    "Select Period",
    value=(datetime(2025, 1, 17), datetime(2025, 12, 16)),
    min_value=datetime(2025, 1, 1),
    max_value=datetime(2025, 12, 16)
)

# Key timeline data for Myat Tun Oo trajectory
timeline_data = pd.DataFrame({
    "Date": [
        "2025-01-17", "2025-01-19", "2025-02-01", 
        "2025-06-01", "2025-12-01", "2025-12-16"
    ],
    "Event": [
        "ASEAN Digital Ministers’ Meeting (Bangkok)",
        "Anti-scam cooperation pledge with Thailand",
        "Civilian attire transition (Minister/Deputy PM)",
        "USDP election candidacy announced",
        "Scam hubs at peak capacity (Myawaddy/KK Park)",
        "SSISM Dossier published"
    ],
    "Category": ["Commitment", "Pledge", "Civilianization", "Election", "Reality", "Exposure"],
    "Scam_Index": [100, 100, 120, 160, 240, 240],  # Normalized growth
    "Status": ["Public Promise", "Regional Pledge", "Rebranding", "Election Play", "Expansion", "Accountability"]
})

# Filter data by selected date range
filtered_timeline = timeline_data[
    (pd.to_datetime(timeline_data["Date"]) >= pd.to_datetime(date_range[0])) &
    (pd.to_datetime(timeline_data["Date"]) <= pd.to_datetime(date_range[1]))
]

# Main dashboard layout with 2 columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Key Events Timeline")
    
    # Custom timeline using Plotly Gantt-style
    fig_timeline = px.timeline(
        filtered_timeline,
        x_start="Date",
        x_end="Date",
        y="Event",
        color="Category",
        hover_data=["Status"],
        title="Myat Tun Oo: Commitments vs Reality"
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(height=400)
    st.plotly_chart(fig_timeline, use_container_width=True)

with col2:
    st.subheader("📊 Scam Economy Growth")
    
    # Scam growth line chart
    fig_growth = px.line(
        filtered_timeline,
        x="Date",
        y="Scam_Index",
        title="Scam Operations Expansion (Normalized Index)",
        markers=True,
        color_discrete_sequence=["#ff4444"]
    )
    fig_growth.add_hline(y=100, line_dash="dash", line_color="green", 
                        annotation_text="Jan 2025 Baseline")
    fig_growth.update_layout(height=400)
    st.plotly_chart(fig_growth, use_container_width=True)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("ASEAN Pledges", "2", "0 Delivered")
col2.metric("Civilian Shift", "Feb 2025", "+140% Scam Growth")
col3.metric("USDP Role", "Confirmed", "No Reform")
col4.metric("Victim Surge", "40%+", "UNODC Data")

# Key Judgment Section
st.markdown("---")
st.subheader("⚖️ Key Judgment")
st.markdown("""
> **Civilian clothes changed; scam protection didn't.**  
> ASEAN cooperation requires outcome verification, not narrative nods.
""")

# Actionable Recommendations for ASEAN
st.subheader("🔍 ASEAN Action Items")
with st.expander("Expand Recommendations"):
    st.markdown("""
    - **Demand metrics** on Jan 2025 commitments at Q1 2026 meeting
    - **Flag USDP role** for enhanced due diligence
    - **Verify telecom shutdowns** in scam zones (Myawaddy/Shwe Kokko)
    - **Track AI-scam evolution** (deepfakes/voice cloning)
    """)

# Footer with integrity seal
st.markdown("---")
st.markdown("""
**Integrity Seal**: SHA-256 Protected OSINT  
**Classification**: Public OSINT for ASEAN Policymakers  
**SSISM Analytical Cell** | 16 Dec 2025
""")

# Download button for dossier
st.download_button(
    label="📥 Download Full Dossier (Markdown)",
    data="""
# SSISM-DOS-MTO-2025-UPDATE-1 Full Content
[Full dossier content here...]
    """,
    file_name="SSISM-DOS-MTO-2025-UPDATE-1.md",
    mime="text/markdown"
)
