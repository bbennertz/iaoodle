"""Main extraction script. Run: python scripts/extract.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json

from src.client import MoodleClient
from src.extractors.courses import get_all_courses
from src.extractors.users import get_all_users

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def save(name: str, data):
    path = RAW_DIR / f"{name}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"Saved {len(data)} records → {path}")


def main():
    client = MoodleClient()

    print("Extracting courses...")
    courses = get_all_courses(client)
    save("courses", courses)

    print("Extracting users...")
    users = get_all_users(client)
    save("users", users.get("users", users))


if __name__ == "__main__":
    main()
