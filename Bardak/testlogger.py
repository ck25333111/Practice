from loguru import logger
from Bardak.configs.logger_config import logger as configured_logger

def test_logging() -> None:
    """
    Простая проверка логгера: логируем инфо и ошибку
    """
    logger.info("Тестовая инфо-запись. Проверка файла и базы.")
    logger.error("Тестовая ошибка. Проверка записи в базу и файл.")

if __name__ == "__main__":
    test_logging()