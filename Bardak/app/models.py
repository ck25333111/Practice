# Базовая модель
import os
from peewee import *

# Абсолютный путь к базе — относительно корня проекта
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database'))
os.makedirs(BASE_DIR, exist_ok=True)

# Создаём соединение с SQLite базой
DB_PATH = os.path.join(BASE_DIR, 'storage.db')
db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db

# Мебель: например, "стол", "шкаф"
class Furniture(BaseModel):
    name = CharField(unique=True)