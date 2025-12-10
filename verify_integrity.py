#!/usr/bin/env python3
"""
verify_integrity.py
SSISM SHA-256 Integrity Verifier for Markdown Files with YAML Front-Matter
Version: 2025-12-10

Usage:
    python verify_integrity.py <file.md>

Behaviour:
    - Extracts the integrity_sha256 field from the YAML header.
    - Replaces its value with the literal string TO_BE_COMPUTED.
    - Computes SHA-256 over the normalized content.
    - Compares stored hash vs computed hash.
    - Returns exit code 0 on match, 1 on mismatch, 2 on errors.
"""

import sys
import hashlib
import re
import pathlib


def compute_normalized_hash(text: str) -> str:
    """
    Replace the integrity_sha256 value with TO_BE_COMPUTED and compute hash.
    """
    normalized = re.sub(
        r'(integrity_sha256:\s*")[0-9a-fA-F]+(")',
        r'\1TO_BE_COMPUTED\2',
        text
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def extract_stored_hash(text: str) -> str:
    """
    Pull the stored SHA-256 hash from the YAML header.
    """
    match = re.search(r'integrity_sha256:\s*"([0-9a-fA-F]+)"', text)
    return match.group(1) if match else None


def main():
    if len(sys.argv) != 2:
        print("Usage: python verify_integrity.py <file.md>")
        sys.exit(2)

    path = pathlib.Path(sys.argv[1])

    if not path.exists():
        print(f"Error: File not found: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")

    stored = extract_stored_hash(text)
    if not stored:
        print("Error: YAML field integrity_sha256 not found.")
        sys.exit(2)

    computed = compute_normalized_hash(text)

    print(f"Stored:   {stored}")
    print(f"Computed: {computed}")

    if stored.lower() == computed.lower():
        print("OK: Integrity verified.")
        sys.exit(0)
    else:
        print("FAIL: Integrity mismatch.")
        sys.exit(1)


if __name__ == "__main__":
    main()
