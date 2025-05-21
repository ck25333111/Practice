# ────────────────────────────────────────────────────────────────
# Общая база для моделей базы данных (например, базовый класс ORM)
# ────────────────────────────────────────────────────────────────

import os
from peewee import Model, CharField, SqliteDatabase
from typing import Optional

# Абсолютный путь к базе — относительно корня проекта
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database'))
os.makedirs(BASE_DIR, exist_ok=True)

# Создаём соединение с SQLite базой
DB_PATH = os.path.join(BASE_DIR, 'storage.db')
db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    """
    Базовый класс модели для работы с базой данных.
    Подключает все модели к одной базе данных.
    """
    class Meta:
        database = db  # Здесь указываем базу для всех моделей, наследующихся от BaseModel


class Furniture(BaseModel):
    """
    Модель мебели.
    Атрибуты:
        name (str): Уникальное имя предмета мебели, например, 'стол' или 'шкаф'.
    """
    name: CharField = CharField(unique=True)