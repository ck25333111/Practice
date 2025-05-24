#╔══════════════════════════════════════════════════════════════════╗
#║                            CONFIG.PY                             ║
#║ Конфигурация проекта: загрузка путей из .env, проверка, создание ║
#║ директорий при необходимости, логгирование состояния.            ║
#║ Используется в других частях проекта для настройки логов и БД.   ║
#╚══════════════════════════════════════════════════════════════════╝
from Bardak.configs import config_raw
import os


def check_env_paths() -> None:
    """Проверяет наличие всех критичных переменных в .env и корректность путей."""
    missing = []

    # if not os.getenv("ROOT_DIR"):
    #     missing.append("ROOT_DIR")
    if not os.getenv("DB_PATH"):
        missing.append("DB_PATH")
    if not os.getenv("LOG_DIR"):
        missing.append("LOG_DIR")

    if missing:
        print("\n🔴 Отсутствуют обязательные переменные окружения:")
        for var in missing:
            print(f" - {var}")
        print("💥 Убедись, что файл .env существует и переменные заданы.\n")
        raise EnvironmentError("Остановка из-за отсутствия переменных окружения.")


class Config:
    ROOT_DIR = config_raw.ROOT_DIR
    DB_PATH = config_raw.DB_PATH
    LOG_DIR = config_raw.LOG_DIR
