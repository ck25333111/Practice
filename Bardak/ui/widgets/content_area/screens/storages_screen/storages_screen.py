# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_screen.py
# Пошаговая форма добавления места хранения с вложенной логикой
# Считывание полей с формы "Добавить место хранения" и сбор данных
# Генерация ячеек на экране "Мои Хранилища" по введённым размерам
# ────────────────────────────────────────────────────────────────
from Bardak.configs.logger_configs.logger_settings import logger

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
from Bardak.ui.style.screen_container import ScreenContainer
from Bardak.ui.widgets.content_area.left_menu.left_menu import LeftMenu

from Bardak.ui.widgets.common.simple_label_inputs import SimpleLabelInputs
from Bardak.ui.widgets.common.double_input_field import DoubleInputField


class StoragesScreen(Screen):
    """
    Экран "Мои Хранилища" с пошаговой формой для добавления
    места хранения, бокса, секций и ячеек с валидацией.
    """


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("[StoragesScreen] Загружен экран")

    # ─────────Считывает все поля из формы ────────────────────────────
    def read_storage_form_data(self) -> dict:
        """Считывает все поля из формы добавления хранилища и возвращает словарь данных """

        try:
            storage_place_name = self.ids.storage_place_name.ids.input_field.text
            box_name = self.ids.box_name.ids.input_field.text
            section_count = int(self.ids.section_count.ids.input_field.text)
            x_section = int(self.ids.cells_x_y.ids.section_x.text)
            y_section = int(self.ids.cells_x_y.ids.section_y.text)

            data_textinputs: dict[str, str | int] = {
                'storage_place_name' : storage_place_name,
                'box_name' : box_name,
                'section_count' : section_count,
                'x_section' : x_section,
                'y_section' : y_section
            }
            print(data_textinputs)

        except ValueError as e:
            # Логируем и возвращаем пустой словарь при ошибке преобразования
            logger.info(f"Ошибка при считывании формы: {e}")
            print(f"Ошибка при считывании формы: {e}")
            return {}

        return data_textinputs

    # ─────────Рассчитывает имена отсеков────────────────────────────
    def build_cells_fields(self) -> None:
        """
        Строит поля для ячеек на основе введённых данных
        """
        data = self.read_storage_form_data()
        if not data:
            return  # Данные кривые — не продолжаем

        section_count: int = data["section_count"]
        x_section: int = data["x_section"]
        y_section: int = data["y_section"]

        # 👇 А дальше твоя логика построения UI, которая использует эти значения
        print(f"Создаём {section_count} отсеков с {x_section}x{y_section} ячеек")

