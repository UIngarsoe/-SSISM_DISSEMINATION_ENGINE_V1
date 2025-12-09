import hashlib
import os
import re
from datetime import datetime
import pandas as pd  # For table magic

# Config: Your repo root (adjust if needed)
REPO_ROOT = '.'  # Or '/path/to/-SSISM_DISSEMINATION_ENGINE_V1'
REGISTRY_FILE = 'SSISM_Integrity_Registry_2025.md'

def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def parse_existing_table(registry_content):
    # Extract table rows via regex (robust for Markdown)
    table_pattern = r'\| No \| Date\s+\| Title\s+\| File\s+\| SHA-256\s+\|\s*\n(.*?)\n\|---'
    match = re.search(table_pattern, registry_content, re.DOTALL)
    if match:
        rows = match.group(1).strip().split('\n')
        df = pd.read_csv(pd.StringIO('\n'.join(rows)), sep='|').dropna(how='all')
        df.columns = df.columns.str.strip()
        return df
    return pd.DataFrame()

def add_new_entries(df):
    # Scan for new IR-*.md or .html files
    new_files = [f for f in os.listdir(REPO_ROOT) if re.match(r'IR-\d{4}-\d{2}-\d{2}-.*\.(md|html)', f) and f not in df['File'].values]
    for file in new_files:
        hash_val = compute_sha256(file)
        # Auto-generate row: No (next), Date (from filename or today), Title (from file or prompt), File, SHA
        date = re.search(r'IR-(\d{4}-\d{2}-\d{2})', file).group(1)
        title = input(f"Title for {file}? ") or f"SSISM Report: {file.replace('.md', '').replace('.html', '')}"  # Or parse from content
        new_row = pd.DataFrame({
            'No': [len(df) + 1],
            'Date': [date],
            'Title': [title],
            'File': [f'`{file}`'],
            'SHA-256': [hash_val]
        })
        df = pd.concat([df, new_row], ignore_index=True)
    return df

def update_registry(df, registry_content):
    # Rebuild Markdown table
    table_md = '| No | Date | Title | File | SHA-256 |\n|-----|------|-------|------|---------|\n'
    for _, row in df.iterrows():
        table_md += f"| {row['No']} | {row['Date']} | {row['Title']} | {row['File']} | {row['SHA-256']} |\n"

    # Replace old table in content
    new_content = re.sub(r'\| No \| Date\s+\| Title\s+\| File\s+\| SHA-256\s+\|\s*\n(.*?)\n(?=\|-----)', table_md, registry_content, flags=re.DOTALL)

    # Update progress and date
    new_content = re.sub(r'Articles Completed:\s*\d+ / 100', f"Articles Completed: {len(df)} / 100", new_content)
    new_content = re.sub(r'Last Updated:\s*\*\*(.*?)\*\*', f"Last Updated: **{datetime.now().strftime('%Y-%m-%d') }**", new_content)

    with open(REGISTRY_FILE, 'w') as f:
        f.write(new_content)
    print(f"Registry updated! Now at {len(df)}/100. Commit message suggestion: 'Auto-append {len(new_files)} entries – sealed.'")

# Main run
if __name__ == "__main__":
    with open(REGISTRY_FILE, 'r') as f:
        content = f.read()
    df = parse_existing_table(content)
    df = add_new_entries(df)
    update_registry(df, content)
