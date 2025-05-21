# ────────────────────────────────────────────────────────────────
#   функция для записи логов в базу данных.
# ────────────────────────────────────────────────────────────────
from Bardak.models.logger_model import Logs
from Bardak.app.logger_sinks.parse_log import parse_log_message
from loguru import logger
from typing import TYPE_CHECKING, Any
""""""
if TYPE_CHECKING:
    from loguru._handler import Message
else:
    Message = Any  # Тип не влияет на выполнение

def logs_db_sink(message: Message) -> None:
    record = message.record
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


