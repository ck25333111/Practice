# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_screen.py
# Пошаговая форма добавления места хранения с вложенной логикой
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
        # Builder.load_file(os.path.join(os.path.dirname(__file__), "storages_screen.kv"))
        print("[StoragesScreen] Загружен экран")

    # ─────────Рассчитывает имена отсеков────────────────────────────
    def calculate_sections(self) -> list[str]:
        """
        Рассчитывает имена отсеков (ячейки) на основе количества отсеков и размеров сетки.

        section_count: общее количество отсеков (int)
        cells_x_y: размер сетки в формате 'XxY' (str), где
            X — количество ячеек по горизонтали (колонки),
            Y — количество ячеек по вертикали (ряды).

        Возвращает список строк с именами отсеков, например: ['A1', 'A2', 'B1', 'B2']
        """
        print('calculate_sections')
        # Считываем количество отсеков
        try:
            section_count = int(self.ids.section_count.ids.input_field.text)
            print(section_count)
        except ValueError:
            logger.info('Некорректное значение Количества отсеков')
            print('Некорректное значение Количества отсеков')
            return []

        try:
            section_x = int(self.ids.cells_x_y.ids.section_x.text)
            section_y = int(self.ids.cells_x_y.ids.section_y.text)
        except (ValueError, AttributeError) as e:
            logger.info(f"Ошибка чтения размеров ячеек: {e}")
            return []

        # Проверяем совпадение с количеством отсеков
        if section_x * section_y != section_count:
            print(f"❌ Несоответствие: {section_x}x{section_y} = {section_x * section_y}, а ты ввёл {section_count}")
            return []

        # Генерация названий секций A1, A2, ..., B1, B2 и т.д.
        sections = [
            f"{chr(65 + row)}{col}"
            for row in range(section_y)
            for col in range(1, section_x + 1)
        ]

        print(f"✅ Секции сгенерированы: {sections}")
        return sections

