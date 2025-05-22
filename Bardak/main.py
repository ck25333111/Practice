# ────────────────────────────────────────────────────────────────
# Точка входа приложения, тесты, запуск основных функций
# ────────────────────────────────────────────────────────────────
from Bardak.loader import bootstrap
from Bardak.configs.logger_configs.logger_settings import logger


def test_error() -> None:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logger.opt(exception=True).error(f"Ошибка {e}")



if __name__ == '__main__':
    try:
        bootstrap()
        logger.info("Программа готова к работе! 🚀")
        test_error()
    except Exception as e:
        logger.opt(exception=True).error(f"Ошибка {e}")