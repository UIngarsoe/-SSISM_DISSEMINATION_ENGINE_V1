#!/usr/bin/env python3
"""
SSISM OSINT 10-Layer Prompt Generator
Author: SSISM Analytical Cell
Purpose:
Generate a structured OSINT analysis prompt to feed into any LLM
before writing daily intelligence, analysis, or opinion articles.
"""

from datetime import date

def generate_osint_prompt(subject, context, time_scope):
    today = date.today().isoformat()

    prompt = f"""
SSISM OSINT 10-LAYER ANALYSIS PROMPT
Date: {today}

SUBJECT:
{subject}

CONTEXT:
{context}

TEMPORAL SCOPE:
{time_scope}

INSTRUCTIONS TO LLM:
You are operating as an OSINT analytical engine.
Do NOT generate propaganda, speculation, or emotional language.
Base all reasoning on observable authority, incentives, systems, and outcomes.

Proceed through the following layers STRICTLY and SEQUENTIALLY:

--------------------------------------------------
LAYER 1 — Identity & Role
- Who is the subject?
- Formal positions
- Functional (real-world) role

LAYER 2 — Declarative Record
- What public commitments, statements, or promises exist?
- Dates, venues, and audiences

LAYER 3 — Authority & Capability
- What power did the subject actually possess?
- Institutional access, command authority, legal mandate

LAYER 4 — Territorial & Systems Control
- What infrastructure or territory is required for the activity?
- Could it exist without state or allied tolerance?

LAYER 5 — Operational Outcomes
- What objectively happened after commitments?
- What changed, what persisted, what worsened?

LAYER 6 — Inter-Agency Coordination
- Was coordination required?
- Is there evidence of execution or failure?

LAYER 7 — Incentive Structure
- Who benefits from continuation?
- Financial, political, security incentives

LAYER 8 — Narrative & Reputation Management
- How was legitimacy maintained?
- Civilianization, silence, deflection, symbolic action

LAYER 9 — Political / Transitional Context
- Elections, reshuffles, rebranding, legal shields
- Did structure change or just appearance?

LAYER 10 — Accountability & Risk
- Legal exposure
- Sanctions risk
- Future liability
- Unresolved responsibility

--------------------------------------------------
OUTPUT REQUIREMENTS:
- Use analytical language only
- Clearly separate facts, inference, and judgment
- Avoid moralizing
- End with a concise KEY JUDGMENT (max 3 sentences)

This analysis will be used for public OSINT publication.
"""
    return prompt.strip()


if __name__ == "__main__":
    # ✍️ EDIT THESE THREE FIELDS EACH MORNING
    SUBJECT = "Maj-Gen Myat Tun Oo (မြထွန်းဦး)"
    CONTEXT = "Myanmar election transition, online scam economy, ASEAN engagement, telecom governance"
    TIME_SCOPE = "January 2025 → Present"

    print(generate_osint_prompt(SUBJECT, CONTEXT, TIME_SCOPE))
