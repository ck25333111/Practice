# ────────────────────────────────────────────────────────────────
# Файл: ui/style/screen_container.py
# Назначение: Стиль и визуальное оформление контейнера экранов
# ────────────────────────────────────────────────────────────────

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "screen_container.kv"))

class ScreenContainer(BoxLayout):
    """
    Контейнер с отступами, фоном и скругленной рамкой для экранов.
    Цвет фона задается через функцию app.hex из главного приложения.
    """
    pass