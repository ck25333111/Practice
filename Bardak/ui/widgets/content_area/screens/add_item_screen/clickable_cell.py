# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/screens/add_item_screen/clickable_cell.py
# Виджет ClickableCell — кликабельная ячейка в сетке ячеек
# ────────────────────────────────────────────────────────────────

from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

class ClickableCell(Button):
    """
    Кастомный виджет ячейки в сетке — позволяет отображать название,
    а также меняет визуальный стиль по состоянию (занята/свободна).
    """

    label: str = StringProperty("")             # Название ячейки (например A1, B2)
    occupied: bool = BooleanProperty(False)     # Признак занятости ячейки

    def on_press(self) -> None:
        """Метод вызывается при клике на ячейку. Можно расширить под открытие модалки и прочее."""

        print(f"🟡 Нажата ячейка: {self.label} (Занята: {self.occupied})")