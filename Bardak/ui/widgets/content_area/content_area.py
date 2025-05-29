# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area.py
# Центральная область приложения со сменяемыми экранами
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from typing import Optional
import os

from kivy.uix.screenmanager import ScreenManager
from Bardak.ui.widgets.content_area.screens.home_screen import HomeScreen
from Bardak.ui.widgets.content_area.screens.search_screen import SearchScreen
from Bardak.ui.widgets.content_area.screens.add_item_screen import AddItemScreen
from Bardak.ui.widgets.content_area.screens.storages_screen import StoragesScreen
from Bardak.ui.widgets.content_area.screens.settings_screen import SettingsScreen
from Bardak.ui.widgets.content_area.screens.profile_screen import ProfileScreen

Builder.load_file(os.path.join(os.path.dirname(__file__), "content_area.kv"))

# ────────────────────────────────────────────────────────────────
class ContentArea(BoxLayout):
    """Центральная часть, в которой отображаются разные экраны"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def switch_to(self, screen_name: str) -> None:
        """ Переключает экран в ScreenManager на указанный по имени.
        :param screen_name: имя экрана (name), заданное в .kv файле """

        sm: Optional[ScreenManager] = self.ids.get("screen_manager")  # получаем ScreenManager по id
        if sm and screen_name in sm.screen_names:  # проверяем наличие
            sm.current = screen_name  # переключаем экран
        else:
            print(f"[switch_to] Экран '{screen_name}' не найден в ScreenManager!")
