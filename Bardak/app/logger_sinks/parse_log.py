# ────────────────────────────────────────────────────────────────
# Парсинг лог-сообщений для записи в БД
# ────────────────────────────────────────────────────────────────

from typing import Dict, Any, Optional
from datetime import datetime
from loguru._handler import Message
import os

def parse_log_message(message: Message) -> Dict[str, Optional[Any]]:
    """
    Sink для Loguru: принимает сообщение лога, сохраняет его в базу.
    Параметры:
        message (Dict[str, Any]): Словарь с информацией о логе от Loguru.
        :return: Словарь с полями для модели базы.
    """
    record = message.record

    # Вытаскиваем базовые поля
    log_time: datetime = record.get('time', datetime.now())
    level = record["level"].name if record.get("level") is not None else "INFO"
    log_message = record["message"] if record.get("message") is not None else "absent"
    file_path = (
        record["file"].path
        if record.get("file") is not None and hasattr(record["file"], "path")
        else "absent"
    )
    line_no = record["line"] if record.get("line") is not None else -1
    func_name = record["function"] if record.get("function") is not None else "absent"
    module_name = os.path.splitext(os.path.basename(file_path))[0] if file_path else None

    # Exception - если есть, берем стек + сообщение
    exception_str: Optional[str] = None
    if record.get('exception'):
        exception_str = str(record['exception'])

    parsed = {
        # "time": log_time,
        # "level": level,
        # "message": log_message,
        # "file": file_path,
        # "line": line_no,
        # "function": func_name,
        "stack_trace": exception_str,
        "module": module_name
    }
    print("📦 Парсер вернул лог:", parsed)  # 👈 Выводим в консоль, что именно парсится


    return {
        "time": log_time,
        "level": level,
        "message": log_message,
        "file": file_path,
        "line": line_no,
        "function": func_name,
        "exception": exception_str,
        "module": module_name,
    }