# ────────────────────────────────────────────────────────────────
#  Файл: Bardak/ui/widgets/common.py
#  Описание: Общие кастомные виджеты для UI, типа заголовков и т.п.
# ────────────────────────────────────────────────────────────────

from kivy.uix.label import Label
from kivy.properties import StringProperty

class HeaderTitle(Label):
    """Кастомный заголовок для экранов — крупный жирный текст по центру"""
    text = StringProperty()  # Реактивное свойство текста

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_size = '24sp'  # Крупный шрифт
        self.bold = True  # Жирный
        self.halign = 'center'  # Горизонтальное выравнивание
        self.valign = 'middle'  # Вертикальное
        self.size_hint_y = None  # Чтобы высота не зависела от контейнера
        self.height = 50  # Фиксированная высота
        self.padding = (10, 10)  # Отступы от краёв