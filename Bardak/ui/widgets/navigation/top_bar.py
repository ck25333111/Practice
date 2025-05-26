# ────────────────────────────────────────────────────────────────
# Bardak.ui.widgets.top_bar
# Верхняя панель — логотип, приветствие и кнопка профиля
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from typing import Tuple
import os

from Bardak.configs.config_raw import KV_DIR  # путь до kv-шек

# Грузим kv-шку
Builder.load_file(os.path.join(KV_DIR, "top_bar.kv"))



class TopBar(BoxLayout):
    """Верхняя панель с логотипом, приветствием и кнопкой профиля."""

    def on_profile_pressed(self) -> None:
        """Коллбэк при нажатии на кнопку 'Профиль'."""
        print("👉 Кнопка 'Профиль' нажата")

