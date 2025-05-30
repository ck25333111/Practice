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
from Bardak.ui.style.box_label_input import BoxLabelInput
from Bardak.ui.style.screen_container import ScreenContainer

Builder.load_file(os.path.join(os.path.dirname(__file__), "storages_screen.kv"))


class StoragesScreen(Screen):
    """
    Экран "Мои Хранилища" с пошаговой формой для добавления
    места хранения, бокса, секций и ячеек с валидацией.
    """
    pass