# ────────────────────────────────────────────────────────────────
# Загрузка и запуск приложения, вызов bootstrap, инициализация
# ────────────────────────────────────────────────────────────────
from Bardak.configs.config import check_env_paths
from Bardak.configs.logger_configs.logger_settings import logger
from Bardak.app.init_db import initialize


def bootstrap() -> None:
    """
    Запускает все необходимые процессы инициализации перед стартом приложения:
    - Настройка логирования.
    - Подключение и настройка базы данных.
    - И другие будущие штуки.
    """
    try:
        check_env_paths()

        initialize()
        logger.info("Инициализация завершена успешно.")
    except Exception as e:
        logger.error(f"Ошибка во время инициализации: {e}")
        raise
