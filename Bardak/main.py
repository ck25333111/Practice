# ────────────────────────────────────────────────────────────────
#  Bardak.main.py Точка входа приложения, тесты, запуск основных функций
# ────────────────────────────────────────────────────────────────
from Bardak.loader import bootstrap
from Bardak.configs.logger_configs.logger_settings import logger
from Bardak.ui.app_ui import BardakApp


def test_error() -> None:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logger.opt(exception=True).error(f"Ошибка {e}")


if __name__ == '__main__':
    try:
        bootstrap()
        BardakApp().run()
        logger.info("Программа запущена! 🚀")

        # test_error()
    except Exception as e:
        logger.opt(exception=True).error(f"Ошибка {e}")