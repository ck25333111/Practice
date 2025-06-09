# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/common/box_label_input.py
# Виджет: подпись + два поля ввода с символом между (например: "4 x 5")
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty


class BoxLabelInput(BoxLayout):
    """Виджет с подписью и двумя полями ввода, разделёнными символом (например: 'x')"""
    label_text: str = StringProperty("")  # Основная надпись над полями
    input_hints: list[str] = ListProperty(["", ""])  # Подсказки в полях
    divider_text: str = StringProperty("x")  # Текст между полями (по умолчанию "x")

    def get_values(self) -> tuple[int, int]:
        """
        Возвращает значения из двух полей в виде кортежа (int, int)
        Если не число — возвращает 0
        """
        try:
            first = int(self.ids.input_1.text.strip())
        except ValueError:
            first = 0
        try:
            second = int(self.ids.input_2.text.strip())
        except ValueError:
            second = 0
        return first, second
