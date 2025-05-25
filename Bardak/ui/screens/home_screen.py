# ────────────────────────────────────────────────────────────────
# 📄 Bardak.ui.screens.home_screen.py — главный экран Bardak UI
# Отображает заглушку или начальную страницу приложения
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen   # Экран для менеджера экранов
from kivy.uix.boxlayout import BoxLayout    # Контейнер для компоновки виджетов
from kivy.uix.label import Label
from kivy.uix.button import Button
from Bardak.ui.widgets.common import HeaderTitle



class HomeScreen(Screen):
    """🏠 Главный экран приложения Bardak UI с кнопкой перехода в хранилище."""
    def __init__(self, **kwargs) -> None:
        """
        Инициализация главного экрана.
        Args:
            **kwargs: Аргументы для базового класса Screen.
        """
        super().__init__(**kwargs)
        self.name = 'home'  # Имя экрана для ScreenManager

        layout = BoxLayout(orientation='vertical')  # Вертикальное расположение виджетов
        self.add_widget(layout)

        header = HeaderTitle(text="Добро пожаловать в Bardak!")
        layout.add_widget(header)

        add_storage_btn: Button = Button(text='➕ Добавить место хранения', size_hint=(1, 0.2))
        add_storage_btn.bind(on_release=self.go_to_add_storage)
        layout.add_widget(add_storage_btn)

        btn = Button(text='Перейти в хранилище', size_hint=(1, 0.1))    # Кнопка перехода на StorageScreen
        btn.bind(on_release=self.go_storage)     # Привязываем обработчик нажатия
        layout.add_widget(btn)


    def go_storage(self, instance):
        """
        Обработчик нажатия кнопки перехода.
        Args:
            instance: Кнопка, вызвавшая событие (не используется).
        """
        self.manager.current = 'storage'    # Меняем текущий экран на 'storage'

    def go_to_add_storage(self, instance):
        """Переключает на экран добавления места хранения"""
        self.manager.current = "add_storage"
