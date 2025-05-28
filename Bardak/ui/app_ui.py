# ────────────────────────────────────────────────────────────────
# Bardak/ui.app_iu.py
# Точка входа в приложение Bardak (для запуска и отладки UI)
# ────────────────────────────────────────────────────────────────

from kivy.app import App
import os

from Bardak.ui.utils.color import hex_to_rgba
from Bardak.ui.main_screen import MainScreen


from Bardak.configs.config_raw import KV_DIR



class BardakApp(App):
    """Главный класс Kivy-приложения Bardak"""

    def hex(self, hex_color: str, alpha: float = 1.0) -> tuple:
        """Обертка - конвертер HEX-RGBA, чтобы вызвать из kv"""
        return hex_to_rgba(hex_color, alpha)


    def build(self) -> MainScreen:
        """Создаем и возвращаем главный экран"""
        return MainScreen()

if __name__ == '__main__':
    BardakApp().run()
