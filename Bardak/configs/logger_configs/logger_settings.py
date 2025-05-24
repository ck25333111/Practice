# ────────────────────────────────────────────────────────────────
# logger_settings
# Конфигурация логгера Loguru: файлы логов, уровни логов, кастомные sink'и
# ────────────────────────────────────────────────────────────────
from loguru import logger
from Bardak.configs import config_raw
from Bardak.configs.logger_configs.write_console import write_log_to_console
from Bardak.configs.logger_configs.write_file import write_log_to_file
import os



# ──────────────────────────────────────────────────────────────────────────────
# НАСТРОЙКА ПАПКИ ДЛЯ ЛОГ-ФАЙЛОВ
# ──────────────────────────────────────────────────────────────────────────────
LOG_DIR = config_raw.LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)
print("LOG_DIR →", LOG_DIR)
# ──────────────────────────────────────────────────────────────────────────────
# КОНФИГУРАЦИЯ ОБРАБОТЧИКОВ LOGURU (sinks)
# ──────────────────────────────────────────────────────────────────────────────
logger.configure(
    handlers=[
        {
            # Запись INFO и выше в файл info.log, error.log
            "sink": write_log_to_file,
            "level": "INFO",
            "enqueue": True,
            "backtrace": True,
            "diagnose": True,
        },
        {
            # Отладочные сообщения в консоль
            "sink": write_log_to_console,
            "level": "DEBUG",
            "colorize": True,
            "backtrace": False,     # стек-трейс для исключений
            "diagnose": False,      # подробности об ошибках
        },
    ]
)
