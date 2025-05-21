from loguru import logger
from Bardak.app.logger_sinks.logs_db_sink import logs_db_sink
from typing import Any, Dict
import os
import sys

# ──────────────────────────────────────────────────────────────────────────────
# НАСТРОЙКА ПАПКИ ДЛЯ ЛОГ-ФАЙЛОВ
# ──────────────────────────────────────────────────────────────────────────────

# Абсолютный путь до папки logs/ в корне проекта
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
os.makedirs(LOG_DIR, exist_ok=True)

# ──────────────────────────────────────────────────────────────────────────────
# КОНФИГУРАЦИЯ ОБРАБОТЧИКОВ LOGURU (sinks)
# ──────────────────────────────────────────────────────────────────────────────

logger.configure(
    handlers=[
        {
            # Запись INFO и выше в файл info.log
            "sink": os.path.join(LOG_DIR, "info.log"),
            "level": "INFO",
            "rotation": "10 MB",
            "enqueue": True,
            "backtrace": True,
            "diagnose": True
        },
        {
            # Запись ошибок (ERROR и выше) в файл error.log
            "sink": os.path.join(LOG_DIR, "error.log"),
            "level": "ERROR",
            "rotation": "10 MB",    # новый файл после 10 МБ
            "enqueue": True,        # очередь для многопоточности
            "backtrace": True,      # стек-трейс для исключений
            "diagnose": True        # подробности об ошибках
        },
        {
            # Отладочные сообщения — прямо в консоль
            "sink": sys.stderr,
            "level": "DEBUG",
            "colorize": True
        },
        {
            # Запись логов в базу данных через кастомную sink-функцию
            'sink': logs_db_sink,
            'level': 'INFO',
            'enqueue': True,    # важна, если логи будут сыпаться параллельно
            'catch': True
        }
    ]
)
