# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_screen.py
# Пошаговая форма добавления места хранения с вложенной логикой
# ────────────────────────────────────────────────────────────────

from typing import List, Optional
from datetime import datetime
from peewee import IntegrityError
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from Bardak.models.storage.storage_place import StoragePlace  # Модель места хранения
from Bardak.models.storage.box import Box as BoxModel  # Модель бокса
from Bardak.models.storage.section import Section  # Модель секции
from Bardak.models.storage.cell import Cell  # Модель ячейки


from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "storages_screen.kv"))


class StoragesScreen(Screen):
    """
    Экран "Мои Хранилища" с пошаговой формой для добавления
    места хранения, бокса, секций и ячеек с валидацией.
    """

    step: int = NumericProperty(1)  # Текущий шаг формы
    section_names: List[str] = ListProperty([])  # Названия введенных секций
    sections_to_add: int = 0  # Сколько нужно ввести секций
    box_name: str = StringProperty("")  # Имя бокса для создания
    storage_place: Optional[StoragePlace] = None  # Созданный объект StoragePlace
    box: Optional[BoxModel] = None  # Созданный объект Box
    cells_rows: int = 0  # Кол-во строк ячеек
    cells_columns: int = 0  # Кол-во столбцов ячеек

    def next_step_storage(self, name: str, description: str) -> None:
        """
        Создает StoragePlace в БД. Переходит к следующему шагу.

        :param name: Название места хранения
        :param description: Описание места хранения
        """
        name = name.strip()  # Убираем пробелы
        description = description.strip() if description else None

        if not name:
            print("Ошибка: Название места хранения обязательно")  # Валидация
            return

        try:
            self.storage_place = StoragePlace.create(
                name=name,
                description=description,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            print(f"Место хранения '{name}' успешно создано")
            self.step = 2  # Следующий шаг

        except IntegrityError:
            print(f"Ошибка: Место хранения с именем '{name}' уже существует")

    def next_step_box(self, name: str) -> None:
        """
        Сохраняет имя бокса и переходит к шагу ввода секций.

        :param name: Название бокса
        """
        name = name.strip()
        if not name:
            print("Ошибка: Название бокса обязательно")
            return
        self.box_name = name
        self.step = 3

    def next_step_sections_count(self, count_str: str) -> None:
        """
        Устанавливает количество секций и вызывает отображение полей ввода.

        :param count_str: Кол-во секций в строковом виде
        """
        try:
            count = int(count_str)
            if count <= 0:
                print("Ошибка: Количество секций должно быть больше 0")
                return
            self.sections_to_add = count
            self.section_names = []
            self.step = 4
            self.show_section_inputs()

        except ValueError:
            print("Ошибка: Введите корректное число секций")

    def show_section_inputs(self) -> None:
        """
        Создает динамически поля для ввода названий секций.
        """
        container = self.ids.sections_box  # Контейнер для секций
        container.clear_widgets()  # Чистим перед добавлением новых

        for i in range(self.sections_to_add):
            hlayout = BoxLayout(size_hint_y=None, height='48dp', spacing=10)

            ti = TextInput(hint_text=f"Название секции #{i + 1}", multiline=False)
            btn = Button(text="Далее", size_hint_x=None, width=80)

            def on_next(instance, index=i, textinput=ti):
                val = textinput.text.strip()
                if not val:
                    print(f"Ошибка: Название секции #{index + 1} обязательно")
                    return

                if len(self.section_names) <= index:
                    self.section_names.append(val)
                else:
                    self.section_names[index] = val

                # Если все секции заполнены — идём дальше
                if len(self.section_names) == self.sections_to_add and all(self.section_names):
                    self.step = 5

            btn.bind(on_press=on_next)
            hlayout.add_widget(ti)
            hlayout.add_widget(btn)
            container.add_widget(hlayout)

    def next_step_cells(self, rows_str: str, cols_str: str) -> None:
        """
        Сохраняет размеры сетки ячеек и переходит к финальному шагу.

        :param rows_str: Кол-во строк в виде строки
        :param cols_str: Кол-во столбцов в виде строки
        """
        try:
            rows = int(rows_str)
            cols = int(cols_str)
            if rows <= 0 or cols <= 0:
                print("Ошибка: Кол-во строк и столбцов должно быть больше 0")
                return
            self.cells_rows = rows
            self.cells_columns = cols
            self.step = 6

        except ValueError:
            print("Ошибка: Введите корректные числа для строк и столбцов")

    def submit_all(self) -> None:
        """
        Создаёт в базе место хранения, бокс, секции и ячейки,
        используя данные, введённые пользователем.
        """
        try:
            # Создаем Box, привязываем к месту хранения
            self.box = BoxModel.create(name=self.box_name, storage_place=self.storage_place)
            print(f"Ящик '{self.box_name}' создан")

            # Создаем секции в ящике
            for sec_name in self.section_names:
                Section.create(name=sec_name, box=self.box)
            print(f"Создано секций: {len(self.section_names)}")

            # Создаем ячейки для каждой секции в виде сетки
            section_objs = list(self.box.section)
            for section in section_objs:
                for row in range(self.cells_rows):
                    for col in range(self.cells_columns):
                        Cell.create(
                            section=section,
                            row=row,
                            column=col,
                            label=f"Ячейка {row + 1}x{col + 1}",
                            categories=[],
                            description=None,
                            length=None,
                            width=None,
                            height=None,
                            change_history=None,
                            created_at=datetime.now(),
                            updated_at=datetime.now()
                        )
            print(f"Создана сетка ячеек {self.cells_rows}x{self.cells_columns} для каждой секции")

            self.reset_form()  # Сбрасываем форму

        except IntegrityError as e:
            print(f"Ошибка базы данных: {e}")

    def reset_form(self) -> None:
        """
        Сбрасывает все поля и шаги формы в исходное состояние.
        """
        self.step = 1
        self.section_names = []
        self.sections_to_add = 0
        self.box_name = ""
        self.storage_place = None
        self.box = None
        self.cells_rows = 0
        self.cells_columns = 0

        # Очистка текстовых полей интерфейса
        self.ids.storage_name.text = ""
        self.ids.storage_description.text = ""
        self.ids.box_name.text = ""
        self.ids.sections_count.text = ""
        self.ids.cells_rows.text = ""
        self.ids.cells_columns.text = ""
        self.ids.sections_box.clear_widgets()

