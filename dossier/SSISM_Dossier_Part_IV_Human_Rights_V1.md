# ------------ PART IV UPLOAD SCRIPT ------------
from github import Github

USERNAME = "your_username"
TOKEN = "your_personal_access_token"
REPO = "-SSISM_DISSEMINATION_ENGINE_V1"

FILE_PATH = "dossier/SSISM_Dossier_Part_IV_Human_Rights_V1.md"
COMMIT_MESSAGE = "Add Part IV — Human Rights & Atrocity Monitoring (SSISM Dossier V1)"

CONTENT = """
# SSISM DOSSIER — PART IV  
## Human Rights & Atrocity Monitoring — December 2025 (HDIW-V1)
System Location: /dossier_system/part_IV/  
Version: 2025-12-12  
Visibility: INTERNAL + VIP  
Signature Mode: 🦚⚡📡 HDIW  

---

## 🧭 1. Forced Displacement Indicators  
- 2.4M internally displaced (UNHCR-compatible estimate)  
- Rakhine spike post-November operations  
- Northern Shan displacements linked to drone strikes  

---

## 🔥 2. Detention Risk Mapping  
High-risk zones:
- Yangon (systematic night raids)  
- Mandalay (mass digital arrest campaigns)  
- Naypyidaw (political detainee processing)  

Patterns:
- Confiscated phones → SIGINT database indexing  
- Coerced confessions → broadcast propaganda  

---

## 📡 3. Media Suppression & Information Blackouts  
- 18+ confirmed tactical internet shutdowns  
- DPI targeting circumvention tools  
- Arrest of journalists and citizen reporters  
- Forced propaganda broadcasts in conflict towns  

---

## 🚨 4. Atrocity Early Warning (AEW) System  
Red Flags:
- Troop buildups in civilian-dense areas  
- Hate-speech spikes on junta channels  
- Forced recruitment  
- Restrictions on humanitarian aid  

---

## 🧾 End of Part IV — Ritual Signatures  
Prepared by: SSISM TIU 2025  
Signature: 🦚⚡📡  
Document Mode: HDIW V1  
"""

g = Github(TOKEN)
repo = g.get_user().get_repo(REPO)

try:
    f = repo.get_contents(FILE_PATH)
    repo.update_file(FILE_PATH, COMMIT_MESSAGE, CONTENT, f.sha)
    print("✔ Updated:", FILE_PATH)
except:
    repo.create_file(FILE_PATH, COMMIT_MESSAGE, CONTENT)
    print("✔ Created:", FILE_PATH)
