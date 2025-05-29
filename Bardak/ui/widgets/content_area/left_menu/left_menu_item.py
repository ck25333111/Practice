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
