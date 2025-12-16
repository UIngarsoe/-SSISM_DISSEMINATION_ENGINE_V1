#!/usr/bin/env python3
# SSISM SHA-256 Verification Script
# No bash required. Just run with any Python environment.

import hashlib
import sys

FILE_PATH = "SSISM_DOSSIER_Myat_Tun_Oo_Civilian_Facade_Scam_Economy_Election_Transition.md"

# 🔐 PASTE THE OFFICIAL SHA-256 HERE (once generated)
EXPECTED_SHA256 = "PASTE_SHA256_HASH_HERE"

def calculate_sha256(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    try:
        calculated = calculate_sha256(FILE_PATH)
        print("Calculated SHA-256:", calculated)
        print("Expected   SHA-256:", EXPECTED_SHA256)

        if calculated.lower() == EXPECTED_SHA256.lower():
            print("\n✅ VERIFICATION PASSED: File integrity confirmed.")
        else:
            print("\n❌ VERIFICATION FAILED: File has been altered.")

    except FileNotFoundError:
        print("❌ ERROR: Dossier file not found.")
        sys.exit(1)
