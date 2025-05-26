# ────────────────────────────────────────────────────────────────
# Bardak/ui.app_iu.py
# Точка входа в приложение Bardak (для запуска и отладки UI)
# ────────────────────────────────────────────────────────────────

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os

from Bardak.configs.config_raw import KV_DIR
from Bardak.ui.screens.home_dashboard import HomeDashboard


class BardakApp(App):
    """Главный класс Kivy-приложения Bardak"""
    def build(self) -> BoxLayout:
        """Собирает и возвращает главный экран"""
        return HomeDashboard()  # Просто отдаем Dashboard как корневой виджет


if __name__ == '__main__':
    BardakApp().run()
