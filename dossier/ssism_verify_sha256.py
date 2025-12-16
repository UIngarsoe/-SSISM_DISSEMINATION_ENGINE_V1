#!/usr/bin/env python3
"""
SSISM SHA-256 Verification Utility
Purpose: Verify integrity of SSISM dossier files
"""

import hashlib
import sys

EXPECTED_SHA256 = "500ea108a68453e96b0bfe8803af07ccfa8d07559fbc292fae4d7ed838fd51e8"

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: python ssism_verify_sha256.py <file.md>")
        sys.exit(1)

    file_path = sys.argv[1]
    calculated = compute_sha256(file_path)

    print("EXPECTED :", EXPECTED_SHA256)
    print("CALCULATED:", calculated)

    if calculated == EXPECTED_SHA256:
        print("✅ INTEGRITY VERIFIED — FILE AUTHENTIC")
    else:
        print("❌ INTEGRITY FAILED — FILE MODIFIED")

if __name__ == "__main__":
    main()
