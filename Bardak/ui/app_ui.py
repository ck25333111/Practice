# ────────────────────────────────────────────────────────────────
# 📄 Bardak.ui.app_ui.py — запуск графического интерфейса Bardak на Kivy
# ────────────────────────────────────────────────────────────────

import os
from loguru import logger
from Bardak.ui.setup_ui_logger import setup_ui_logger
from Bardak.configs import config_raw

from kivy.app import App    # Базовый класс Kivy-приложения
from kivy.uix.screenmanager import ScreenManager, Screen    # Управление экранами
from Bardak.ui.screens.home_screen import HomeScreen        # главный экран Bardak UI
from Bardak.ui.screens.storage_screen import StorageScreen  # экран хранилища Bardak UI
from Bardak.ui.screens.add_storage_screen import AddStorageScreen  # Экран пошагового добавления нового места хранения.
from Bardak.ui.widgets.common import HeaderTitle        #Общие кастомные виджеты для UI, типа заголовков и т.п.

os.chdir(config_raw.ROOT_DIR)
setup_ui_logger()

# ────────────────────────────────────────────────────────────────


class BardakApp(App):
    """Менеджер экранов Bardak UI — управляет переключением между экранами"""
    def build(self) -> ScreenManager:
        """
        Создаёт и возвращает ScreenManager с зарегистрированными экранами.
        Returns:
            ScreenManager: Менеджер экранов с добавленными HomeScreen и StorageScreen.
        """
        sm = ScreenManager()             # Менеджер экранов#
        sm.add_widget(HomeScreen())      # Главный экран
        sm.add_widget(StorageScreen())   # Экран хранилища
        sm.add_widget(AddStorageScreen())  # Экран пошагового добавления нового места хранения
        sm.current = 'home'              # Стартовый экран

        return sm

logger.info("HomeScreen загружен")

# ────────────────────────────────────────────────────────────────
# Позволяет запускать этот файл как скрипт (если нужно)
if __name__ == "__main__":
    BardakApp().run()  # Запуск приложения
# ────────────────────────────────────────────────────────────────