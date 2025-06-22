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

        # Логируем текущее состояние wizard_state для отладки
        logger.info(f"wizard_state сохранён: {ws.__dict__}")

    def build_cells_fields(self) -> None:
        """
        После сохранения формы переходит на экран конфигурации ящиков.
        Все данные берёт из wizard_state.
        """
        ws = App.get_running_app().wizard_state

        # Проверим, что rows_count действительно установлен
        if ws.rows_count is None or ws.rows_count <= 0:
            logger.error(f"Некорректное значение rows_count: {ws.rows_count}")
            return

        # Передаём значение на следующий экран
        next_screen = self.manager.get_screen("storages_rows_config_screen")
        next_screen.rows_count = ws.rows_count

        # Переключаем экран
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