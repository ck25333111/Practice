# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/common/section_visual.py
# Компонент визуализации секции (ящика) с возможностью разбивки на ячейки
# ────────────────────────────────────────────────────────────────

from typing import Callable, List, Dict
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty

class SectionVisual(BoxLayout):
    """
    Виджет для отображения одной секции внутри бокса.
    Может показывать:
    - кнопку "Разбить на ячейки", если cell_data пусто
    - или визуальную сетку ячеек (CellGrid), если данные есть

    Также поддерживает ввод размеров ячеек по клику.
    """
    print('SectionVisual')

    label: str = StringProperty()
    machine_label: str = StringProperty()
    row: int = StringProperty()
    cell_data: List[Dict] = ListProperty([])
    on_updated: Callable = ObjectProperty(None)