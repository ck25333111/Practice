# ────────────────────────────────────────────────────────────────
# Файл: ui/style/box_label_input.py
# Назначение: Стиль и визуальное оформление форм ввода
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "box_label_input.kv"))

class BoxLabelInput(BoxLayout):
    """
    Горизонтальный блок: Label + TextInput.
    Используется в формах для ввода с подписями.
    """
    label_text: str = StringProperty("")  # Подпись слева
    hint_text: str = StringProperty("")   # Подсказка в поле ввода
    input_width: float = NumericProperty(0.6)  # Ширина поля TextInput (по умолчанию 0.6)