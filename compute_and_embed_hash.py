#!/usr/bin/env python3
"""
compute_and_embed_hash.py
SSISM SHA-256 Hash Calculator & YAML Front-Matter Embedder
Version: 2025-12-10

Usage:
    python compute_and_embed_hash.py <file.md>
    python compute_and_embed_hash.py <file.md> --inplace

Function:
    - Calculates SHA-256 of a normalized markdown file
      (integrity_sha256 replaced with TO_BE_COMPUTED)
    - Embeds the hash inside YAML front-matter.
    - With --inplace, overwrites original and saves a .bak backup.
"""

import sys
import argparse
import hashlib
import re
import pathlib


def compute_normalized_hash(text: str) -> str:
    """
    Replace integrity_sha256 with TO_BE_COMPUTED before hashing.
    """
    normalized = re.sub(
        r'(integrity_sha256:\s*")[0-9a-fA-F]+(")',
        r'\1TO_BE_COMPUTED\2',
        text
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def embed_hash(text: str, sha: str) -> str:
    """
    Insert or update YAML field integrity_sha256.
    """
    # If the field exists, replace the old hash.
    if re.search(r'integrity_sha256:\s*"[0-9a-fA-F]+"', text):
        return re.sub(
            r'(integrity_sha256:\s*")[0-9a-fA-F]+(")',
            rf'\1{sha}\2',
            text
        )

    # If YAML header exists but no field, insert it after ---
    if text.startswith("---"):
        parts = text.split("\n")
        return f"---\nintegrity_sha256: \"{sha}\"\n" + "\n".join(parts[1:])

    # Otherwise wrap entire file in a new YAML block
    return f"---\nintegrity_sha256: \"{sha}\"\n---\n{text}"


def main():
    parser = argparse.ArgumentParser(description="Embed SHA-256 into YAML front-matter.")
    parser.add_argument("file", help="Path to markdown file")
    parser.add_argument("--inplace", action="store_true", help="Write back to original file (with .bak backup)")
    args = parser.parse_args()

    path = pathlib.Path(args.file)

    if not path.exists():
        print(f"Error: File not found: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")
    sha = compute_normalized_hash(text)
    updated = embed_hash(text, sha)

    if args.inplace:
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(text, encoding="utf-8")
        path.write_text(updated, encoding="utf-8")
        print(f"Updated in place. Backup: {backup}")
        print(f"SHA-256: {sha}")
    else:
        out = path.with_name(path.stem + "_with_hash" + path.suffix)
        out.write_text(updated, encoding="utf-8")
        print(f"Created: {out}")
        print(f"SHA-256: {sha}")


if __name__ == "__main__":
    main()
