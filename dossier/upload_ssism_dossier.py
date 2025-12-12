import base64
import requests
import json

# -----------------------------
# USER CONFIGURATION
# -----------------------------

GITHUB_TOKEN = "YOUR_GITHUB_PAT_HERE"     # ← put your GitHub personal access token
REPO_OWNER = "UIngarsoe"                  # ← your GitHub username
REPO_NAME = "SSISM_DISSEMINATION_ENGINE_V1"   # ← repo name
FILE_PATH = "dossier/SSISM_Strategy_Draft_Maung_Chan_Thar_100YP_20251212.md"
LOCAL_FILE = "SSISM_Strategy_Draft_Maung_Chan_Thar_100YP.md"

COMMIT_MESSAGE = "Add SSISM Strategy Dossier (Auto-Upload) — MCTM-100YP-V1"

# -----------------------------
# CORE UPLOAD LOGIC
# -----------------------------

def upload_file():
    with open(LOCAL_FILE, "rb") as f:
        content = f.read()

    encoded = base64.b64encode(content).decode("utf-8")

    # Check if the file already exists on GitHub
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # File exists → update
        sha = response.json()["sha"]
        print(f"Updating existing file: {FILE_PATH}")
        data = {
            "message": COMMIT_MESSAGE,
            "content": encoded,
            "sha": sha
        }
    else:
        # File does not exist → create
        print(f"Creating new file: {FILE_PATH}")
        data = {
            "message": COMMIT_MESSAGE,
            "content": encoded
        }

    result = requests.put(url, headers=headers, data=json.dumps(data))

    if result.status_code in [200, 201]:
        print("✅ Upload successful!")
        print("🔗 File URL:", result.json()["content"]["html_url"])
    else:
        print("❌ Error:", result.status_code, result.text)


if __name__ == "__main__":
    upload_file()
