#!/usr/bin/env python3
# SSISM SHA-256 Verifier Utility
# Version: 2025-12-09
# Author: SSISM Threat Intelligence Unit
#
# Description:
#   Lightweight SHA-256 hashing tool for verifying integrity of SSISM reports,
#   field manuals, intelligence briefs, and lecture packs.
#
# Usage:
#   python3 ssism_sha256_verifier.py <path_to_file> [expected_sha256]

import sys
import hashlib
from pathlib import Path

def sha256_of(file_path):
    """Compute SHA-256 hash of a file in a memory-safe streaming mode."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ssism_sha256_verifier.py <file> [expected_sha256]")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found — {file_path}")
        sys.exit(1)

    computed_hash = sha256_of(file_path)
    print(f"\nSHA-256 for '{file_path.name}':")
    print(computed_hash)
    print()

    # Optional integrity check
    if len(sys.argv) == 3:
        expected = sys.argv[2].lower().strip()
        if computed_hash == expected:
            print("✔ Integrity Check: PASS — Hash matches expected value.")
        else:
            print("✘ Integrity Check: FAIL — Hash mismatch.")
            print(f"Expected: {expected}")
            print(f"Got     : {computed_hash}")

if __name__ == "__main__":
    main()
