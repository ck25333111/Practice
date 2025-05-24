# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                               write_console.py                                 ║
# ║        Кастомный sink Loguru без traceback'а, с ручной ANSI-раскраской      ║
# ║                     Используется в консольной отладке                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

from typing import Any  # Для типизации аргумента sink-функции


def write_log_to_console(message: Any) -> None:
    """Выводит лог-сообщение в консоль без traceback, с ANSI-раскраской."""

    record = message.record  # Получаем словарь с данными о лог-сообщении

    # Извлекаем данные из записи
    level = record["level"].name  # Уровень логирования: DEBUG, INFO и т.д.
    time = record["time"].strftime("%d-%m-%Y %H:%M:%S")  # Время логирования
    name = record["name"]  # Имя модуля
    function = record["function"]  # Имя функции
    line = record["line"]  # Номер строки в коде
    log_message = record["message"]  # Само сообщение лога
    exception = record["exception"]  # Объект исключения, если был

    # ANSI-коды цветов для терминала
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Подбор цвета в зависимости от уровня логирования
    level_color = {
        "DEBUG": CYAN,
        "INFO": GREEN,
        "WARNING": YELLOW,
        "ERROR": RED,
        "CRITICAL": RED,
    }.get(level, RESET)

    # Сборка финального текста лога
    output = (
        f"{GREEN}{time}{RESET} | {level_color}{level:<8}{RESET} | "
        f"{CYAN}{name}:{function}:{line}{RESET} - "
    )

    # Добавление текста сообщения или ошибки
    if exception:
        exc_type = exception.type.__name__  # Название типа исключения
        exc_value = exception.value  # Текст ошибки
        output += f"{RED}{exc_type}: {exc_value}{RESET}"  # Покрасим и добавим
    else:
        output += f"{level_color}{log_message}{RESET}"  # Просто сообщение

    print(output)  # Выводим всё это великолепие
