# ────────────────────────────────────────────────────────────────
# 📄 Bardak.ui.screens.storage_screen.py — экран хранилища Bardak UI
# Отображает интерфейс управления местами хранения
# ────────────────────────────────────────────────────────────────
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen     # Экран для менеджера экранов
from kivy.uix.boxlayout import BoxLayout      # Контейнер для компоновки виджетов
from kivy.uix.button import Button            # Кнопка для возврата на главный экран

class StorageScreen(Screen):
    """📦 Экран управления местами хранения с кнопкой возврата"""
    def __init__(self, **kwargs) -> None:
        """
        Инициализация экрана хранилища.
        Args:
            **kwargs: Аргументы для базового класса Screen.
        """
        super().__init__(**kwargs)              # Инициализируем базовый класс Screen
        self.name = 'storage'                   # Имя экрана для ScreenManager

        layout = BoxLayout(orientation ='vertical')  # Вертикальная компоновка
        # Создаем кнопку "Назад", чтобы возвращаться на HomeScreen
        layout.add_widget(Label(text='экран хранилища Bardak UI'))
        back_button = Button(text='Назад', size_hint=(1, 0.1))
        back_button.bind(on_release=self.go_back)   # При нажатии вызывается метод go_back
        layout.add_widget(back_button)              # Добавляем кнопку в наш layout
        self.add_widget(layout)                     # Добавляем весь layout на экран

    def go_back(self, instance) -> None:
        """Обработчик кнопки 'Назад', переключает экран на 'home'"""
        self.manager.current = 'home'       # self.manager — это ScreenManager, переключаем на 'home'