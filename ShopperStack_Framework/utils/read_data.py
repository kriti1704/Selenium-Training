import json
from pathlib import Path

# for reading the json file
def read_json(file_path):
    path = Path(file_path)
    if not path.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        path = repo_root / file_path

    with open(path, encoding="utf-8") as f:
        return json.load(f)