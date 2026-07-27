import json
from pathlib import Path

from app.core.config import settings


class JSONStorage:

    @staticmethod
    def load():
        path = Path(settings.DATA_PATH)

        if not path.exists():
            return []

        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def save(data):
        path = Path(settings.DATA_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)