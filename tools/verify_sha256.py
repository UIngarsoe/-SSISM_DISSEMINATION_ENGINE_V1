#!/usr/bin/env python3
# SSISM SHA-256 Integrity Verifier
# Version: 2025-12-11
# Author: SSISM Strategic Analysis Division

import hashlib
import sys

EXPECTED_HASH = "b4f2cc0f0cdb1e4c1cbb7bd8251d9f63d082be54bd217e2691d9c5cd88f1ca72"

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            h.update(block)
    return h.hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 verify_sha256.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    computed = sha256sum(filename)

    print(f"Computed SHA-256:   {computed}")
    print(f"Expected SHA-256:   {EXPECTED_HASH}")

    if computed.lower() == EXPECTED_HASH.lower():
        print("\n✔️  Integrity Verified — File matches official SSISM release.")
    else:
        print("\n❌  Integrity Check Failed — File does NOT match official release.")

if __name__ == "__main__":
    main()
