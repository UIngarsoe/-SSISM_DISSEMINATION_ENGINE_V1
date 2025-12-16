#!/usr/bin/env python3
# SSISM SHA-256 Integrity Generator
# Purpose: Generate cryptographic hash for dossier verification

import hashlib

FILE_PATH = "SSISM_DOSSIER_Myat_Tun_Oo_Civilian_Facade_Scam_Economy_Election_Transition.md"

def sha256_of_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    print("SHA-256:", sha256_of_file(FILE_PATH))
