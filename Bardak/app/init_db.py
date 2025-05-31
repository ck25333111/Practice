# ────────────────────────────────────────────────────────────────
# ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ
# ────────────────────────────────────────────────────────────────
from Bardak.models.models_base import Furniture, db
from Bardak.models.logger_model import Logs

from Bardak.models.storage.storage_place import StoragePlace
from Bardak.models.storage.box import Box
from Bardak.models.storage.section import Section
from Bardak.models.storage.cell import Cell

from loguru import logger

def initialize() -> None:
    """
    Инициализирует базу данных:
    - Устанавливает соединение с БД.
    - Создаёт таблицы, если они ещё не существуют.
    - Добавляет базовые записи мебели, если их нет.
    - Закрывает соединение с БД.
    Returns:
        None
    """
    # Проверяем, если база ещё не подключена — подключаемся
    if db.is_closed():
        db.connect()
    try:
        # Создаём таблицы всех нужных моделей
        db.create_tables([
            StoragePlace,
            Box,
            Section,
            Cell,
            Logs,
        ], safe=True)

    except Exception as e:
        logger.error(f"Инициализация БД упала с ошибкой: {e}")
    finally:
        # Закрываем соединение
        if not db.is_closed():
            db.close()