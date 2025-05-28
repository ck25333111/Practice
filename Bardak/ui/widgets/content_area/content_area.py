# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area.py
# Центральная область приложения со сменяемыми экранами
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

from Bardak.ui.widgets.content_area.screens.search_screen import SearchScreen
Builder.load_file(os.path.join(os.path.dirname(__file__), "content_area.kv"))

class ContentArea(BoxLayout):
    """Центральная часть, в которой отображаются разные экраны"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class LeftMenu(BoxLayout):
#     pass