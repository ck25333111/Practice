from Bardak.loader import bootstrap
from loguru import logger


def test_error() -> None:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        logger.exception("Упс, деление на ноль!")

test_error()

if __name__ == '__main__':
    bootstrap()
    print("Программа готова к работе! 🚀")