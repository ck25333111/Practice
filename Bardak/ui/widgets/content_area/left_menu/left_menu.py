# ──────────────────────────────────────────────
# Bardak/ui/widgets/content_area/left_menu.py
# Боковое меню с кнопками слева
# ──────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

# Builder.load_file(os.path.join(os.path.dirname(__file__), "left_menu.kv"))

# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/left_menu/left_menu_item.py
# Кастомный элемент меню с коллбеком on_release
# ────────────────────────────────────────────────────────────────

from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem


class LeftMenuItem(OneLineListItem):
    """Элемент левого меню с коллбеком on_release"""
    on_release_callback = ObjectProperty(lambda: None)

    def on_release(self) -> None:
        """Вызывает переданный коллбек при нажатии"""
        self.on_release_callback()

class LeftMenu(BoxLayout):
    """
    Боковое вертикальное меню с кнопками.
    Пока пустое, потом туда кнопки добавим.
    """
    pass
