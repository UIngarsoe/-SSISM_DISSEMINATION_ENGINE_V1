import hashlib
import os

def sha256_of_file(filepath):
    """Return SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def scan_articles(directory="articles"):
    """Scan all files inside /articles and print their SHA-256 hashes."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return

    print("=== SSISM SHA-256 Hash Report ===")
    for filename in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            hash_value = sha256_of_file(full_path)
            print(f"{filename}  -->  {hash_value}")

def main():
    scan_articles()

if __name__ == "__main__":
    main()
