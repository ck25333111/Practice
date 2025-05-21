# ────────────────────────────────────────────────────────────────
#   функция для записи логов в базу данных.
# ────────────────────────────────────────────────────────────────
from Bardak.models.logger_model import Logs
from Bardak.app.logger_sinks.parse_log import parse_log_message
from loguru._handler import Message
from loguru import logger


def logs_db_sink(message: Message) -> None:
    print(">>> message:", message)
    """
    Loguru sink-функция для записи логов в базу данных.
    :param message: Словарь с логом от Loguru.
    """
    log_data = parse_log_message(message)

    try:
        Logs.create(
            time=log_data["time"],
            level=log_data["level"],
            message=log_data["message"],
            file=log_data["file"],
            line=log_data["line"],
            function=log_data["function"],
            exception=log_data["exception"],
        )
        logger.info('Запись логов в db прошла успешно')

    except Exception as e:
        logger.error(f"Ошибка записи лога в БД: {e}")


