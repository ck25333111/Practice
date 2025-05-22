# ────────────────────────────────────────────────────────────────
# Конфигурация логгера Loguru: файлы логов, уровни логов, кастомные sink'и
# ────────────────────────────────────────────────────────────────
from loguru import logger
from Bardak.configs import config_raw
from Bardak.configs.logger_configs.logs_db_sink import logs_db_sink
from Bardak.configs.logger_configs.clean_sink import no_traceback_sink
from Bardak.configs.logger_configs.file_log_sink import write_log_to_file
import os
import sys

# ──────────────────────────────────────────────────────────────────────────────
# НАСТРОЙКА ПАПКИ ДЛЯ ЛОГ-ФАЙЛОВ
# ──────────────────────────────────────────────────────────────────────────────
LOG_DIR = config_raw.LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)


# ──────────────────────────────────────────────────────────────────────────────
# КОНФИГУРАЦИЯ ОБРАБОТЧИКОВ LOGURU (sinks)
# ──────────────────────────────────────────────────────────────────────────────

log_format = (
    '<green>{time:DD-MM-YYYY HH:mm:ss}</green> | ' 
    '<level>{level: <8}</level> | '
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

logger.configure(
    handlers=[
        {
            # Запись INFO и выше в файл info.log, error.log
            "sink": write_log_to_file,
            "level": "INFO",
            "enqueue": True,
            "backtrace": False,
            "diagnose": False,
        },
        {
            # Отладочные сообщения — прямо в консоль
            "sink": no_traceback_sink,
            "level": "DEBUG",
            "colorize": True,
            "backtrace": False,     # стек-трейс для исключений
            "diagnose": False,      # подробности об ошибках
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
