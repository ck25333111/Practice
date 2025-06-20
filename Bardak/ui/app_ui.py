# ────────────────────────────────────────────────────────────────
# Bardak/ui.app_iu.py
# Точка входа в приложение Bardak (для запуска и отладки UI)
# ────────────────────────────────────────────────────────────────

from kivy.app import App
import os

from Bardak.ui.main_screen import MainScreen
from Bardak.ui.utils.colors import get_color
from Bardak.ui.style.style_loader import load_all_styles
from Bardak.ui.style.kv_loader import load_all_kv
from Bardak.configs.config_raw import KV_DIR
from Bardak.services.wizard_state import WizardState



class BardakApp(App):
    """Главный класс Kivy-приложения Bardak"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        load_all_styles()
        load_all_kv()
        self.wizard_state: WizardState = WizardState()

    def build(self) -> MainScreen:
        self.colors = get_color
        return MainScreen()



if __name__ == '__main__':
    BardakApp().run()
