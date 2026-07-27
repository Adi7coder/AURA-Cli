import logging
from pathlib import Path

from app.core.config import settings

Path(settings.LOG_PATH).parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=settings.LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("Aura")