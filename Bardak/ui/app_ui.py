# ────────────────────────────────────────────────────────────────
# Bardak/ui.app_iu.py
# Точка входа в приложение Bardak (для запуска и отладки UI)
# ────────────────────────────────────────────────────────────────

from kivy.app import App
import os


from Bardak.ui.main_screen import MainScreen
from Bardak.ui.utils.colors import get_color
from Bardak.ui.style.style_loader import load_all_styles
from Bardak.configs.config_raw import KV_DIR



class BardakApp(App):
    """Главный класс Kivy-приложения Bardak"""

    def build(self) -> MainScreen:
        self.colors = get_color
        load_all_styles()

        """Создаем и возвращаем главный экран"""
        return MainScreen()


if __name__ == '__main__':
    BardakApp().run()
