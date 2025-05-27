# ────────────────────────────────────────────────────────────────
# Bardak/ui.app_iu.py
# Точка входа в приложение Bardak (для запуска и отладки UI)
# ────────────────────────────────────────────────────────────────

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os

from Bardak.ui.main_screen import MainScreen

from Bardak.configs.config_raw import KV_DIR



class BardakApp(App):
    """Главный класс Kivy-приложения Bardak"""

    def build(self) -> MainScreen:
        """Создаем и возвращаем главный экран"""
        return MainScreen()

if __name__ == '__main__':
    BardakApp().run()
