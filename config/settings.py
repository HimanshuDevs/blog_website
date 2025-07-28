from pathlib import Path

MEDIA_ROOT = Path("media")
MEDIA_USERS_DIR = MEDIA_ROOT / "users"
MEDIA_USERS_DIR.mkdir(parents=True, exist_ok=True)