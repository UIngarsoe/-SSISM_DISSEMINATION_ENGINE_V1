# ssism_repo_archiver.py

import subprocess
import os
import sys
from datetime import datetime

# --- Configuration Section ---

# This URL uses the PAT (Personal Access Token) for secure authentication.
# Format: https://<PAT>@github.com/<OWNER>/<REPOSITORY>.git
# IMPORTANT: Replace <PAT>, <YOUR_GITHUB_USERNAME>, and <REPOSITORY_NAME>
# For UIngarsoe/Myanmar-OSINT-Ritual, the owner is 'UIngarsoe'.
GITHUB_REPO_URL = "https://<PAT>@github.com/UIngarsoe/Myanmar-OSINT-Ritual.git"

# Directory where all archived repositories will be stored.
# This should be a secure, non-public directory.
ARCHIVE_ROOT_DIR = os.path.join(os.path.expanduser("~"), "SSISM_GITHUB_ARCHIVE")

# The name of the local directory for this specific archive.
REPO_NAME = "Myanmar-OSINT-Ritual"
ARCHIVE_PATH = os.path.join(ARCHIVE_ROOT_DIR, REPO_NAME + ".git")

# --- SSISM Archival Function ---

def create_mirror_archive(repo_url: str, archive_path: str):
    """
    Performs a git 'mirror' clone of the repository for complete archival.
    A mirror clone includes all branches, tags, and remote tracking information.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SSISM Archiver initiated.")
    print("-" * 50)
    
    # 1. Ensure the root archive directory exists
    os.makedirs(ARCHIVE_ROOT_DIR, exist_ok=True)
    print(f"Archive Root Directory: {ARCHIVE_ROOT_DIR}")

    # 2. Check if the archive already exists
    if os.path.exists(archive_path):
        print(f"Archive already exists at: {archive_path}")
        print("Performing incremental update (git remote update --prune)...")
        
        # Change directory to the existing archive to run the update
        try:
            os.chdir(archive_path)
            # Update the existing mirror clone
            command = ["git", "remote", "update", "--prune"]
        except Exception as e:
            print(f"Error changing directory: {e}")
            return
    else:
        print(f"Creating new mirror archive at: {archive_path}")
        # Clone the repository as a mirror
        command = [
            "git", "clone", "--mirror", repo_url, archive_path
        ]
    
    # 3. Execute the Git command using subprocess
    try:
        # Check shell=True warning, but in this case, command is fixed and safe.
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n" + "*" * 50)
            print(f"ARCHIVE SUCCESS: {REPO_NAME}")
            print(f"Location: {archive_path}")
            print(f"Status: Mirror clone is up to date/created.")
            print("*" * 50 + "\n")
        else:
            # This should be caught by check=True, but included for clarity
            print(f"ARCHIVE FAILURE: Git command failed with code {result.returncode}")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")

    except subprocess.CalledProcessError as e:
        print("\n" + "#" * 50)
        print(f"CRITICAL ARCHIVE ERROR for {REPO_NAME}!")
        print(f"Ensure the PAT in the script is correct and has 'repo' scope.")
        print(f"Git Error Output:\n{e.stderr}")
        print("#" * 50 + "\n")
    except FileNotFoundError:
        print("CRITICAL ERROR: 'git' command not found. Ensure Git is installed.")
        sys.exit(1)


if __name__ == "__main__":
    # You can easily extend this to archive multiple repositories by changing the variables
    # or by wrapping this call in a loop over a list of your repositories.
    
    # For now, we focus on the Myanmar-OSINT-Ritual repository
    create_mirror_archive(GITHUB_REPO_URL, ARCHIVE_PATH)


