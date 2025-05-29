# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/screens/add_item_screen.py
# Экран добавления предмета в базу
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import os

from Bardak.ui.widgets.content_area.screens.search_screen import SearchScreen
Builder.load_file(os.path.join(os.path.dirname(__file__), "add_item_screen.kv"))

class AddItemScreen(Screen):
    pass