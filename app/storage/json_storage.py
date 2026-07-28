import json
from pathlib import Path
from app.core.config import settings

class JSONStorage:
    def __init__(self, path: str | None = None):
        self.path = Path(path or settings.DATA_PATH)

    def load(self):
        if not self.path.exists():
            return []

        with open(self.path, "r") as file:
            return json.load(file)

    def save(self, data):
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.path, "w") as file:
            json.dump(
                data,
                file,
                indent=4
            )