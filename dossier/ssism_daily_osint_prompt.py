#!/usr/bin/env python3
"""
SSISM Daily OSINT Prompt Generator
Designed for morning use before writing analysis or articles.
"""

from datetime import date

def generate_prompt(subject, context, time_scope):
    today = date.today().isoformat()

    return f"""
SSISM DAILY OSINT 10-LAYER PROMPT
Date: {today}

SUBJECT:
{subject}

CONTEXT:
{context}

TIME SCOPE:
{time_scope}

INSTRUCTIONS:
Analyze using the SSISM OSINT 10-Layer Matrix.
No propaganda. No speculation. No emotional language.
Base analysis on authority, systems, incentives, and outcomes.

End with a KEY JUDGMENT (max 3 sentences).
"""

if __name__ == "__main__":
    SUBJECT = "EDIT SUBJECT"
    CONTEXT = "EDIT CONTEXT"
    TIME_SCOPE = "EDIT TIME RANGE"

    print(generate_prompt(SUBJECT, CONTEXT, TIME_SCOPE))
