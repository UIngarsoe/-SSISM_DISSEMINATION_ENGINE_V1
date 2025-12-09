#!/usr/bin/env python3
import hashlib
import os
from datetime import datetime

ARTICLES_DIR = "articles"
LOG_FILE = "sha256_log.csv"

def sha256_of_file(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def scan_and_log(directory=ARTICLES_DIR, log_file=LOG_FILE):
    if not os.path.exists(directory):
        print(f"[ERROR] Directory '{directory}' does not exist.")
        return

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"=== SSISM SHA-256 Integrity Log ({timestamp}) ===")

    with open(log_file, "a") as log:
        for filename in sorted(os.listdir(directory)):
            full_path = os.path.join(directory, filename)
            if os.path.isfile(full_path):
                hash_value = sha256_of_file(full_path)
                print(f"{filename} --> {hash_value}")
                log.write(f"{timestamp},{filename},{hash_value}\n")

    print(f"\n[OK] Log updated: {log_file}")

def main():
    scan_and_log()

if __name__ == "__main__":
    main()
