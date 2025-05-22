# ────────────────────────────────────────────────────────────────
# Функция записи логов в файл с разделением по уровням:
# ERROR и выше — в error.log,
# INFO и ниже — в info.log.
# ────────────────────────────────────────────────────────────────

import os
from typing import Optional
from datetime import datetime
from Bardak.configs import config_raw
from Bardak.configs.logger_configs.log_parser import parse_log_message


def write_log_to_file(message) -> None:
    """
    Записывает лог-сообщение в файл error.log или info.log
    в зависимости от уровня логирования.

    Уровень ERROR, CRITICAL, FATAL пишется в error.log,
    остальные (INFO и ниже) — в info.log.

    :return: None
    """

    # Парсим входящее сообщение в словарь с нужными полями
    record = parse_log_message(message)

    # Получаем уровень лога (ERROR, INFO и т.д.)
    level: str = record.get('level', 'INFO')

    # Выбираем файл для записи в зависимости от уровня лога
    if level in ("ERROR", "CRITICAL", "FATAL"):
        log_filename = "error.log"
    else:
        log_filename = "info.log"

    # Формируем полный путь к файлу лога на основе LOG_DIR из конфига
    log_path = os.path.join(config_raw.LOG_DIR, log_filename)

    # Получаем остальные данные для строки лога с дефолтами
    log_time: datetime = record.get("time", datetime.now())
    module: Optional[str] = record.get("module", "absent")
    function: str = record.get("function", "absent")
    line: int = record.get("line", -1)
    log_message: str = record.get("message", "absent")

    # Формируем строку для записи в файл с красивым форматированием
    log_line = (
        f"{log_time.strftime('%d-%m-%Y %H:%M:%S')} | "
        f"{level:<8} | "
        f"{module}:{function}:{line} - "
        f"{log_message}\n"
    )

    # Создаём директорию с логами, если она ещё не существует
    os.makedirs(config_raw.LOG_DIR, exist_ok=True)

    # Открываем нужный файл в режиме добавления и пишем лог
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(log_line)
