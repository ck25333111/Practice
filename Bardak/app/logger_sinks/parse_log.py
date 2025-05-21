# ────────────────────────────────────────────────────────────────
# Парсинг лог-сообщений для записи в БД
# ────────────────────────────────────────────────────────────────

from typing import Dict, Any, Optional
from datetime import datetime
from loguru._handler import Message

def parse_log_message(message: Message) -> Dict[str, Optional[Any]]:
    """
    Sink для Loguru: принимает сообщение лога, сохраняет его в базу.
    Параметры:
        message (Dict[str, Any]): Словарь с информацией о логе от Loguru.
        :return: Словарь с полями для модели базы.
    """
    record = message.record


    # Вытаскиваем базовые поля
    log_time: datetime = record.get('time')
    level: str = record.get('level').name if record.get('level') else 'INFO'
    log_message: str = record.get('message', '')
    file_path: str = record.get('file').path if record.get('file') else ''
    line_no: int = record.get('line', 0)
    func_name: Optional[str] = record.get('function', '')

    # Exception - если есть, берем стек + сообщение
    exception_str: Optional[str] = None
    if record.get('exception'):
        exception_str = str(record['exception'])

    return {
        "time": log_time,
        "level": level,
        "message": log_message,
        "file": file_path,
        "line": line_no,
        "function": func_name,
        "exception": exception_str,
    }