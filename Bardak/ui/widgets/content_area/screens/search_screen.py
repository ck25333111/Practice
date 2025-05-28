# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/search_screen.py
# Экран для поиска предметов по ключевым словам
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

# Загружаем KV-шку рядом
Builder.load_file(os.path.join(os.path.dirname(__file__), "search_screen.kv"))

class SearchScreen(Screen):
    """Экран поиска предметов по названию, тегам и пр."""
    pass
