from loguru import logger
from Bardak.models.models_base import Furniture, db


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
        # Создаём таблицы, если ещё не созданы
        db.create_tables([Furniture])

        # Добавляем записи мебели, если они ещё не существуют
        Furniture.get_or_create(name='Стол')
        Furniture.get_or_create(name='Шкаф')

    except Exception as e:
        logger.error(f"Инициализация БД упала с ошибкой: {e}")
    finally:
        # Закрываем соединение
        if not db.is_closed():
            db.close()