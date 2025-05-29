# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/screens/storages_screen.py
# Экран добавления предмета в базу
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), "storages_screen.kv"))

class StoragesScreen(Screen):
    pass