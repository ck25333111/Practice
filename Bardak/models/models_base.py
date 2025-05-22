# ────────────────────────────────────────────────────────────────
# Общая база для моделей базы данных (например, базовый класс ORM)
# ────────────────────────────────────────────────────────────────

from Bardak.configs.config import Config
import os
from peewee import Model, CharField, SqliteDatabase
from typing import Optional

os.makedirs(Config.ROOT_DIR, exist_ok=True)

# Создаём соединение с SQLite базой
db = SqliteDatabase(Config.DB_PATH)


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