# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_screen.py
# Пошаговая форма добавления места хранения с вложенной логикой
# Считывание полей с формы "Добавить место хранения" и сбор данных
# Генерация ячеек на экране "Мои Хранилища" по введённым размерам
# ────────────────────────────────────────────────────────────────

from Bardak.configs.logger_configs.logger_settings import logger
from kivy.uix.screenmanager import Screen
from kivy.app import App
from Bardak.ui.style.screen_container import ScreenContainer
from kivy.properties import NumericProperty, ListProperty, StringProperty
from typing import List, Optional

# from datetime import datetime
# from peewee import IntegrityError
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from Bardak.models.storage.storage_place import StoragePlace  # Модель места хранения
# from Bardak.models.storage.box import Box as BoxModel  # Модель бокса
# from Bardak.models.storage.section import Section  # Модель секции
# from Bardak.models.storage.cell import Cell  # Модель ячейки
# from kivy.lang import Builder
# import os
# from Bardak.ui.widgets.content_area.left_menu.left_menu import LeftMenu
# from Bardak.ui.widgets.common.simple_label_inputs import SimpleLabelInputs
# from Bardak.ui.widgets.common.double_input_field import DoubleInputField

class StoragesScreen(Screen):
    """
    Экран для добавления места хранения, бокса, секций и ячеек.
    Вся введённая информация по шагам собирается в глобальный объект
    wizard_state для дальнейшей передачи между экранами.
    """

    def save_form_data_to_wizard_state(self) -> None:
        """
        Считывает текущие значения из всех полей формы на экране
        и сохраняет их в объект wizard_state, который хранится в
        приложении (App.get_running_app()).

        Обработка ошибок при конвертации числовых полей,
        чтобы избежать крашей приложения.
        """
        ws = App.get_running_app().wizard_state

        # Получаем строки из текстовых полей, убираем пробелы, если пусто — None
        ws.storage_place_name = self.ids.storage_place_name.ids.input_field.text.strip() or None
        ws.box_name = self.ids.box_name.ids.input_field.text.strip() or None

        # Пытаемся преобразовать в int, если ошибка — ставим None
        try:
            ws.rows_count = int(self.ids.rows_section_count.ids.input_field.text)
        except (ValueError, AttributeError):
            ws.rows_count = None

        try:
            ws.section_count = int(self.ids.section_count.ids.input_field.text)
        except (ValueError, AttributeError):
            ws.section_count = None

        try:
            ws.x_section = int(self.ids.cells_x_y.ids.section_x.text)
        except (ValueError, AttributeError):
            ws.x_section = None

        try:
            ws.y_section = int(self.ids.cells_x_y.ids.section_y.text)
        except (ValueError, AttributeError):
            ws.y_section = None

        # Логируем текущее состояние wizard_state для отладки
        logger.info(f"wizard_state сохранён: {ws.__dict__}")

    def build_cells_fields(self) -> None:
        """
        Для отладки — выводит в консоль все атрибуты объекта wizard_state,
        чтобы проверить, что данные успешно сохранились и доступны.
        """
        ws = App.get_running_app().wizard_state

        # print("=== Содержимое wizard_state ===")
        # for attr in dir(ws):
        #     # Фильтруем служебные методы и вызываемые объекты
        #     if not attr.startswith('_') and not callable(getattr(ws, attr)):
        #         value = getattr(ws, attr)
        #         print(f"{attr}: {value}")
        # print("=== Конец содержимого wizard_state ===")

        rows_count = int(self.ids.rows_section_count.ids.input_field.text)
        next_screen = self.manager.get_screen("storages_rows_config_screen")
        next_screen.rows_count = rows_count
        self.manager.current = "storages_rows_config_screen"

    def on_next_button_pressed(self) -> None:
        """
        Метод, который должен вызываться при нажатии кнопки 'Далее':
        - Сохраняет текущие данные в wizard_state
        - Показывает их в консоли (для отладки)
        - В дальнейшем сюда добавим переход на следующий экран
        """
        self.save_form_data_to_wizard_state()
        self.build_cells_fields()