# ────────────────────────────────────────────────────────────────
# 📄 app_ui.py — запуск графического интерфейса Bardak на Kivy
# Этот модуль содержит точку входа в Kivy-приложение.
# Инициализирует App-класс, загружает экран(ы) и запускает цикл обработки событий Kivy.
# ⚙️ Используется:
# - Kivy: библиотека для создания кроссплатформенных GUI
# - ScreenManager: переключение между экранами
# - BoxLayout: базовый контейнер для размещения элементов
# ────────────────────────────────────────────────────────────────


from Bardak.configs.logger_configs.logger_settings import logger
import logging
from typing import Optional, Type
from kivy.app import App    # Базовый класс Kivy-приложения
from kivy.uix.screenmanager import ScreenManager, Screen    # Управление экранами
from kivy.uix.label import Label    # Просто для примера — текст в окне
from kivy.uix.boxlayout import BoxLayout    # Контейнер для компоновки элементов

# ────────────────────────────────────────────────────────────────

class InterceptHandler(logging.Handler):
    """Перехватывает логи из стандартного логгера Python и кидает в Loguru"""

    def emit(self, record):
        # Получаем уровень логирования
        level = logger.level(record.levelname).name if record.levelname in logger._core.levels else record.levelno
        # Передаём лог в Loguru
        logger.log(level, record.getMessage())

# Подключаем наш хендлер к корневому логгеру Kivy (и вообще ко всем)
logging.getLogger().handlers = [InterceptHandler()]

# ────────────────────────────────────────────────────────────────


class HomeScreen(Screen):
    """🏠 Главный экран (заглушка пока)"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'  # Важно: имя экрана для ScreenManager
        layout = BoxLayout()
        layout.add_widget(Label(text='Это Bardak UI'))
        self.add_widget(layout)

class BardakApp(App):
    """🚀 Главный класс Kivy-приложения"""

    def build(self) -> ScreenManager:
        """Создаёт и возвращает менеджер экранов (корень интерфейса)"""
        sm = ScreenManager()      # Менеджер для переключения между экранами
        sm.add_widget(HomeScreen())      # Добавляем наш заглушечный экран
        return sm


logger.info("HomeScreen загружен")
# ────────────────────────────────────────────────────────────────
# Позволяет запускать этот файл как скрипт (если нужно)
if __name__ == "__main__":
    BardakApp().run()  # Запуск приложения
# ────────────────────────────────────────────────────────────────