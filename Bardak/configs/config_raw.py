# ────────────────────────────────────────────────────────────────
# config_raw
# ────────────────────────────────────────────────────────────────

from dotenv import load_dotenv
import os

load_dotenv()

import os
from dotenv import load_dotenv

# Загружаем .env из корня проекта, если нужно
# Предполагаем, что .env лежит в Bardak/ рядом с этим файлом или выше
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Bardak/configs
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))  # Bardak


# Загружаем .env из PROJECT_ROOT, если он есть
dotenv_path = os.path.join(PROJECT_ROOT, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

def make_abs_path(env_var: str, default_relative_path: str) -> str:
    """
    Превращает значение из env в абсолютный путь относительно PROJECT_ROOT.
    Если env переменная не задана, берёт default_relative_path от PROJECT_ROOT.
    """
    path = os.getenv(env_var)
    if not path:
        path = default_relative_path
    # Если путь абсолютный — просто возвращаем
    if os.path.isabs(path):
        return os.path.abspath(path)
    # Иначе считаем относительно PROJECT_ROOT
    return os.path.abspath(os.path.join(PROJECT_ROOT, path))

ROOT_DIR = PROJECT_ROOT
DB_PATH = make_abs_path("DB_PATH", "database/storage.db")
LOG_DIR = make_abs_path("LOG_DIR", "logs")
ASSETS_DIR = make_abs_path("ASSETS_DIR", "assets")
KV_DIR = make_abs_path("KV_DIR", "ui/kv")

# --- Дополнительно можно сделать проверку на существование папок и базы

if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

db_dir = os.path.dirname(DB_PATH)
if not os.path.isdir(db_dir):
    os.makedirs(db_dir, exist_ok=True)

# Просто для контроля — выведем пути, чтобы не гадать
# print(f"config_raw.py: ROOT_DIR = {ROOT_DIR}")
# print(f"config_raw.py: DB_PATH = {DB_PATH}")
# print(f"config_raw.py: LOG_DIR = {LOG_DIR}")









# # Абсолютный путь до корня проекта (где лежит .env и pyproject.toml)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # → Bardak/configs/
# BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # → Bardak/
#
# # Теперь всё строим от BASE_DIR, даже если .env содержит относительные пути
# ROOT_DIR = os.path.abspath(os.getenv("ROOT_DIR", BASE_DIR))
# DB_PATH = os.path.join(ROOT_DIR, os.getenv("DB_PATH", "database/storage.db"))
# LOG_DIR = os.path.join(ROOT_DIR, os.getenv("LOG_DIR", "logs"))

# ROOT_DIR = os.path.abspath(os.getenv("ROOT_DIR", "."))
# DB_PATH = os.path.abspath(os.getenv("DB_PATH", "database/storage.db"))
# LOG_DIR = os.path.abspath(os.getenv("LOG_DIR", "logs"))
# print('ROOT_DIR',ROOT_DIR)
# print('ROOT_DIR',DB_PATH)
# print('ROOT_DIR',LOG_DIR)
