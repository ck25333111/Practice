# ────────────────────────────────────────────────────────────────
# Функция записи логов в файл с разделением по уровням:
# ERROR и выше — в error.log,
# INFO и ниже — в info.log.
# ────────────────────────────────────────────────────────────────

import os
from typing import Optional
from datetime import datetime
from Bardak.configs import config_raw
from Bardak.configs.logger_configs.log_parser import parse_loguru_message

# ────────────────────────────────────────────────────────────────
# Основная функция записи логов в файл
# ────────────────────────────────────────────────────────────────
def write_log_to_file(message) -> None:
    """
    Записывает лог-сообщение в файл error.log или info.log
    в зависимости от уровня логирования.
    Уровень ERROR, CRITICAL, FATAL пишется в error.log,
    остальные (INFO и ниже) — в info.log.
    :return: None
    """
    record = parse_loguru_message(message)      # Парсим входящее сообщение в словарь с нужными полями
    level: str = record.get('level', 'INFO')        # Получаем уровень лога (ERROR, INFO и т.д.)

    if level in ("ERROR", "CRITICAL", "FATAL"): log_filename = "error.log"
    else: log_filename = "info.log"

    log_path = os.path.join(config_raw.LOG_DIR, log_filename)   # Формируем полный путь к файлу лога на основе LOG_DIR из конфига

    # Получаем остальные данные для строки лога с дефолтами
    log_time: datetime = record.get("time", datetime.now())
    module: Optional[str] = record.get("module", "absent")
    function: str = record.get("function", "absent")
    line: int = record.get("line", -1)
    log_message: str = record.get("message", "absent")
    stack_trace: str = record.get('stack_trace')


    log_line = (        # Формируем строку для записи в файл
        f"{log_time.strftime('%d-%m-%Y %H:%M:%S.%f')} | "
        f"{level:<8} | "
        f"{module}:{function}:{line} - "
        f"{log_message}\n"
    )

    os.makedirs(config_raw.LOG_DIR, exist_ok=True)      # Создаём директорию с логами, если она ещё не существует

    with open(log_path, "a", encoding="utf-8") as file:     # Открываем нужный файл в режиме добавления и пишем лог
        file.write(log_line)
