# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/top_bar/top_bar.py
# Верхняя панель приложения с названием и кнопкой профиля
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "top_bar.kv"))


class TopBar(BoxLayout):
    """Верхняя панель с заголовком и кнопкой"""
    # title: StringProperty = StringProperty("держи Bardak под контролем")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


