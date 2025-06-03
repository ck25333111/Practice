# ────────────────────────────────────────────────────────────────
# Файл: ui/widgets/common/double_input_field.py
# Назначение: Компонент с двумя полями ввода в одной строке
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

# Builder.load_file("ui/widgets/common/double_input_field.kv")


class DoubleInputField(BoxLayout):
    """Компонент, отображающий Label и два поля ввода рядом"""

    label_text: str = StringProperty("")  # Текст слева
    first_hint: str = StringProperty("")  # Подсказка для первого поля
    second_hint: str = StringProperty("")  # Подсказка для второго поля
