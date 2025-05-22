# ────────────────────────────────────────────────────────────────
# config_raw
# ────────────────────────────────────────────────────────────────

from dotenv import load_dotenv
import os

load_dotenv()


ROOT_DIR = os.path.abspath(os.getenv("ROOT_DIR", "."))
DB_PATH = os.path.abspath(os.getenv("DB_PATH", "database/storage.db"))
LOG_DIR = os.path.abspath(os.getenv("LOG_DIR", "logs"))
