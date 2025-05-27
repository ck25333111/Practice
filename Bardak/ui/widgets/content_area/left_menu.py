# ──────────────────────────────────────────────
# Bardak/ui/widgets/content_area/left_menu.py
# Боковое меню с кнопками слева
# ──────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "left_menu.kv"))

class LeftMenu(BoxLayout):
    """
    Боковое вертикальное меню с кнопками.
    Пока пустое, потом туда кнопки добавим.
    """
    pass
