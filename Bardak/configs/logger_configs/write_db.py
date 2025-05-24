# ────────────────────────────────────────────────────────────────
#   функция для записи логов в базу данных.
# ────────────────────────────────────────────────────────────────

from Bardak.models.logger_model import Logs
from loguru import logger
from datetime import datetime


def write_log_to_db(log: dict) -> None:
    """
    Функция для записи логов в базу данных.
    :param dict: Словарь с логом от parse_log_file_line().
    """

    """Пишет лог в БД, если time (time) ещё не встречался"""
    if is_duplicate(log, log['time']):
        return
    try:

        Logs.create(
            time=log["time"],
            level=log["level"],
            message=log["message"],
            file_path=log["file"],
            line=log["line"],
            function=log["function"],
            stack_trace=log["stack_trace"],
            module=log['module']
        )
        logger.info('Запись логов в db прошла успешно')

    except Exception as e:
        logger.error(f"Ошибка записи лога в БД: {e}")


def is_duplicate(log: dict, log_time: datetime) -> bool:
    """Проверяет, существует ли такой лог в БД"""
    try:
        if not log_time or not log.get("message"):
            return False

        return Logs.select().where(
            (Logs.time == log_time) &
            (Logs.message == log["message"])
        ).exists()

    except Exception as e:
        print(f"⚠️ Ошибка при проверке на дубликат: {e}")
        return False
