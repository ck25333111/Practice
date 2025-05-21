"""Модель логов для записи лог-сообщений в базу данных."""

from peewee import *
from Bardak.models.models_base import BaseModel
from datetime import datetime

class Logs(BaseModel):
    """
    Модель для хранения логов в базе данных.

    Атрибуты:
        level (str): Уровень логирования (INFO, ERROR и т.п.)
        message (str): Текст лог-сообщения
        created_at (datetime): Дата и время создания записи
    """
    level: str = CharField()    # Уровень логирования
    message: str = TextField()   # Основной текст лог-сообщения
    stack_trace: str | None = TextField(null=True)  # Полный traceback (если сообщение об ошибке). Может быть пустым (null=True)
    create_ad: datetime = DateTimeField(default=datetime.now)   # Дата и время, когда лог был записан
    module:str = CharField(null=True)   # Имя модуля
    function: str = CharField(null=True)    # Имя функции
    line: int = IntegerField(null=True)     # Номер строки
    file_path: str = CharField(null=True)   # Путь до файла
