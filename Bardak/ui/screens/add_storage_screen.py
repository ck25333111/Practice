# ────────────────────────────────────────────────────────────────
#  Файл: Bardak/ui/screens/add_storage_screen.py
#  Описание: Экран пошагового добавления нового места хранения.
#           Пользователь вводит название места, бокса, секции и сетку.
# ────────────────────────────────────────────────────────────────

from typing import Optional

# ─── Kivy-виджеты ───────────────────────────────────────────────
from kivy.uix.screenmanager import Screen       # Экран приложения (страница внутри ScreenManager)
from kivy.uix.boxlayout import BoxLayout        # Вертикальный или горизонтальный контейнер
from kivy.uix.textinput import TextInput        # Поле ввода текста
from kivy.uix.button import Button              # Кнопка
from kivy.uix.label import Label                # Отображение текста

# ─── Kivy-свойства (реактивные переменные) ──────────────────────
from kivy.properties import StringProperty, ObjectProperty  # Переменные, которые отслеживают изменения

# ─── Кастомные компоненты UI ────────────────────────────────────
from Bardak.ui.widgets.common import HeaderTitle  # Наш кастомный заголовок


class AddStorageScreen(Screen):
    """Экран для пошагового добавления нового места хранения.
    Сейчас реализован первый шаг - ввод названия места хранения."""
    def __init__(self, **kwargs) -> None:
        """Инициализация экрана, создание базового интерфейса с заголовком,
        полем ввода и кнопкой 'Далее'."""
        super().__init__(**kwargs)

        self.name = "add_storage"

        # Основной вертикальный контейнер для виджетов
        self.layout: BoxLayout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.add_widget(self.layout)

        # Заголовок экрана
        self.header: HeaderTitle = HeaderTitle(text='Добавить место хранения')
        self.add_widget(self.header)

        # Инструкция/подсказка
        self.instruction_label: Label = Label(
            text='Введите место хранения: Кухня, Балкон, Зал, Комната',
            size_hint=(1, 0.1))
        self.layout.add_widget(self.instruction_label)

        # Вложенный горизонтальный контейнер для поля и кнопки
        self.input_row: BoxLayout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.1),
            spacing=10  #  отступ между полем и кнопкой
        )

        # Текстовое поле для ввода места хранения
        self.storage_input: TextInput = TextInput(
            multiline=False,     # Однострочное поле
            hint_text="Введите место хранения", # Подсказка-плейсхолдер, пока поле пустое
            size_hint=(1, 0.1),     # Размер поля: по ширине занимает 100% контейнера, по высоте 10%
            write_tab=False         # Отключает ввод табуляции, чтобы не переключаться между виджетами нажатием Tab
        )
        self.input_row.add_widget(self.storage_input)

        # Кнопка "Далее" для перехода к следующему шагу
        self.next_button: Button = Button(
            text="ОК",
            size_hint_x=0.3
        )
        self.next_button.bind(on_release=self.on_next_presset)
        self.input_row.add_widget(self.next_button)

        # добавляется весь input_row в layout
        self.layout.add_widget(self.input_row)


# ─────── Обработчик нажатия кнопки 'Далее'. ─────────────────────
    def on_next_presset(self, instance: Optional[Button]) -> None:
        """Обработчик нажатия кнопки 'Далее'. Сейчас просто печатает ввод.
        В будущем здесь логика перехода к следующему шагу."""
        place_name: str = self.storage_input.text.strip()
        if not place_name:
            # Можно добавить всплывающее окно с ошибкой, но пока просто print
            print("Ошибка: Место хранения не может быть пустым")
            return

        print(f"Введено место хранения: {place_name}")
        # Тут будет логика перехода на следующий экран или обновления UI