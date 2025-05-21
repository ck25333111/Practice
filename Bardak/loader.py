from Bardak.configs.logger_config import logger
from Bardak.app.init_db import initialize

def bootstrap() -> None:
    """
    Запускает все необходимые процессы инициализации перед стартом приложения:
    - Настройка логирования.
    - Подключение и настройка базы данных.
    - И другие будущие штуки.
    """
    try:
        logger.info("Старт инициализации приложения...")
        initialize()
        logger.info("Инициализация завершена успешно.")
    except Exception as e:
        logger.exception(f"Ошибка во время инициализации: {e}")
        raise