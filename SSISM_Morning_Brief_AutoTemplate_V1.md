# SSISM Morning Brief — AutoTemplate V1
System Location: /distribution_system/
Version: 2025-12-12
Classification: INTERNAL-SSISM-ENGINE
Integrity: SHA256-WAITING

---

# 0. SYSTEM AUTO-FILL HEADER
%SSISM_ENGINE_AUTOFILL_START%

DATE_UTC: {{AUTO_DATE_UTC}}
DATE_LOCAL: {{AUTO_DATE_LOCAL}}
OPERATOR: {{AUTO_OPERATOR_NAME}}
ENGINE_VERSION: {{AUTO_ENGINE_VERSION}}
LLM_STACK: {{AUTO_LLM_STACK}}   # e.g., GROK-2 | GEMINI-2 | GPT-5.1

%SSISM_ENGINE_AUTOFILL_END%

---

# 1. STRATEGIC SITUATION SNAPSHOT
%SECTION_SNAPSHOT%

- THEATRE: {{THEATRE}}
- KEY FRONTLINES TODAY:
  1. {{FRONTLINE_1}}
  2. {{FRONTLINE_2}}
  3. {{FRONTLINE_3}}

Critical Drivers:
- {{DRIVER_1}}
- {{DRIVER_2}}
- {{DRIVER_3}}

---

# 2. OVERNIGHT EVENTS (H01–H12)
%SECTION_OVERNIGHT%

| Time | Event | Source Reliability | Assessment |
|------|--------|--------------------|------------|
| {{T1}} | {{EVENT1}} | {{REL1}} | {{ASS1}} |
| {{T2}} | {{EVENT2}} | {{REL2}} | {{ASS2}} |
| {{T3}} | {{EVENT3}} | {{REL3}} | {{ASS3}} |

---

# 3. SSISM SITUATIONAL GRADES (AUTO-SCORED)
%SECTION_SCORES%

| Metric | Score (0–100) | Auto-Logic |
|--------|----------------|-------------|
| Regime Stability | {{STABILITY_SCORE}} | {{STABILITY_LOGIC}} |
| Resistance Momentum | {{RESISTANCE_SCORE}} | {{RESISTANCE_LOGIC}} |
| International Pressure | {{INT_PRESSURE_SCORE}} | {{INT_PRESSURE_LOGIC}} |
| EW/ cyber ops intensity | {{CYBER_SCORE}} | {{CYBER_LOGIC}} |

---

# 4. TODAY’S INTELLIGENCE PRIORITIES (TIP)
%SECTION_TIP%

1. **Priority Alpha:** {{TIP_ALPHA}}
2. **Priority Bravo:** {{TIP_BRAVO}}
3. **Priority Charlie:** {{TIP_CHARLIE}}

Auto-Risk Level: **{{RISK_LEVEL}}**

---

# 5. OPERATOR NOTES (HUMAN INPUT)
%SECTION_HUMAN_NOTES%

- {{NOTE1}}
- {{NOTE2}}
- {{NOTE3}}

---

# 6. LLM TRIANGULATION SUMMARY
*(Gemini + Grok + GPT internal alignment)*  
%SECTION_TRIANGULATION%

- **Gemini-2 Output:**  
  {{GEMINI_OPINION}}

- **Grok-2 Output:**  
  {{GROK_OPINION}}

- **ChatGPT Output:**  
  {{CHATGPT_OPINION}}

Consensus Score: **{{CONSENSUS_SCORE}}%**

---

# 7. MACHINE-READABLE BACKEND BLOCK  
*(For SSISM internal engines only)*  
%SSISM_BACKEND_BLOCK%
