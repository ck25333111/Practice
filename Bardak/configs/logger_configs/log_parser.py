# ────────────────────────────────────────────────────────────────
# log_parser.py
# ────────────────────────────────────────────────────────────────
# Содержит функции:
# - smart_parse_log: выбирает нужный парсер по типу входа
# - parse_loguru_message: парсит объект Loguru Message - Возвращает: Словарь с полями для модели базы Logs
# - parse_log_file_line: парсит строку из лог-файла
# ────────────────────────────────────────────────────────────────

from typing import Dict, Any, Optional, Union
from datetime import datetime
from loguru._handler import Message
import os

# ────────────────────────────────────────────────────────────────
# Выбирает парсер в зависимости от типа входящего объекта
# ────────────────────────────────────────────────────────────────
def smart_parse_log(source: Union[Message, str]) -> Dict[str, Any]:
    """Выбирает нужный парсер: Message или строка"""
    if isinstance(source, Message):
        return parse_loguru_message(source)
    elif isinstance(source, str):
        return parse_log_file_line(source)
    else:
        raise TypeError(f"Тип {type(source)} не поддерживается для лог-парсинга")

# ────────────────────────────────────────────────────────────────
# Парсит loguru (message: Message) для записи в файл-лог.
# ────────────────────────────────────────────────────────────────
def parse_loguru_message(message: Message) -> Dict[str, Optional[Any]]:
    """
    Sink для Loguru: принимает сообщение лога Message
    Параметры:
        message (Dict[str, Any]): Словарь с информацией о логе от Loguru.
        :return: Словарь с полями для записи в файл-лог.
    """
    record = message.record
    # print('record - ', record)

    # Вытаскиваем базовые поля
    log_time: datetime = record.get('time', datetime.now())
    level = record["level"].name if record.get("level") is not None else "INFO"
    log_message = record["message"] if record.get("message") is not None else "absent"
    file_path = (record["file"].path if record.get("file") is not None and hasattr(record["file"], "path") else "absent")
    line_no = record["line"] if record.get("line") is not None else -1
    func_name = record["function"] if record.get("function") is not None else "absent"
    module_name = os.path.splitext(os.path.basename(file_path))[0] if file_path and file_path != "absent" else "unknown"

    # Exception - если есть, берем стек + сообщение
    stack_trace: Optional[str] = None
    if record.get('exception'):
        stack_trace = str(record['exception'])

    # parsed = {
    #     "time": log_time,
    #     "level": level,
    #     "message": log_message,
    #     "file": file_path,
    #     "line": line_no,
    #     "function": func_name,
    #     "stack_trace": stack_trace,
    #     "module": module_name
    # }
    # print("📦 Парсер вернул лог:", parsed)  # 👈 Выводим в консоль, что именно парсится


    return {
        "time": log_time,
        "level": level,
        "message": log_message,
        "file": file_path,
        "line": line_no,
        "function": func_name,
        "stack_trace": stack_trace,
        "module": module_name,
    }

# ────────────────────────────────────────────────────────────────
# Принимает (line: str) из файла лога Парсит в словарь для записи в БД
# ────────────────────────────────────────────────────────────────
def parse_log_file_line(line: str) -> Dict[str, Any]:
    """
    Ожидает строку формата:
    23-05-2025 14:12:34 | INFO     | my_module:my_func:42 - Сообщение
    :param line: строка из лог-файла
    :return: словарь с полями для записи в БД
    """
    try:
        date_part, rest = line.split(" | ", 1)
        level_part, rest = rest.split(" | ", 1)
        location_part, message_part = rest.split(" - ", 1)

        # Парсим дату
        log_time = datetime.strptime(date_part.strip(), "%d-%m-%Y %H:%M:%S.%f")
        level = level_part.strip()
        module, function, line_no = location_part.strip().split(":")

        return {
            "time": log_time,
            "level": level,
            "message": message_part.strip(),
            "file": "from_log_file",
            "line": int(line_no),
            "function": function,
            "stack_trace": None,
            "module": module,
        }

    except Exception as e:
        raise ValueError(f"Не удалось распарсить строку лога: {line!r} → {e}")