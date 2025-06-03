# ────────────────────────────────────────────────────────────────
# Bardak/ui/main_screen.py
# Основной экран приложения с базовой структурой
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
import os

from Bardak.ui.widgets.top_bar.top_bar import TopBar
from Bardak.ui.widgets.content_area.content_area import ContentArea
from Bardak.ui.widgets.content_area.left_menu.left_menu import LeftMenu
from Bardak.ui.widgets.footer_bar.footer_bar import FooterBar


class MainScreen(BoxLayout):
    """Главный экран приложения."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

