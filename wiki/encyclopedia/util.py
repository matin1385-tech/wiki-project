import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRIES_DIR = os.path.join(BASE_DIR, "entries")

def list_entries():
    return sorted([
        filename.replace(".md", "")
        for filename in os.listdir(ENTRIES_DIR)
        if filename.endswith(".md")
    ])

def save_entry(title, content):
    with open(os.path.join(ENTRIES_DIR, f"{title}.md"), "w", encoding="utf-8") as f:
        f.write(content)

def get_entry(title):
    try:
        with open(os.path.join(ENTRIES_DIR, f"{title}.md"), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

def entry_exists(title):
    return os.path.isfile(os.path.join(ENTRIES_DIR, f"{title}.md"))