# ────────────────────────────────────────────────────────────────
# ui/ui_logger_configs.py
# ────────────────────────────────────────────────────────────────
from Bardak.configs.logger_configs.logger_settings import logger
import logging

class InterceptHandler(logging.Handler):
    """Перехватывает логи из стандартного логгера Python и кидает в Loguru"""
    def emit(self, record):
        # Пример фильтрации (можно кастомизировать)
        if record.levelno < logging.INFO:
            return

        level = logger.level(record.levelname).name if record.levelname in logger._core.levels else record.levelno
        logger.log(level, record.getMessage())

def setup_ui_logger():
    # Подключаем перехватчик к корневому логгеру
    logging.getLogger().handlers = [InterceptHandler()]
    logging.getLogger().setLevel(logging.DEBUG)  # Можно повысить до WARNING, если будет мусор