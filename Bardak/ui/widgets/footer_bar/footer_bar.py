# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/footer_bar/footer_bar.py
# Нижняя панель с версией приложения и статусом
# ────────────────────────────────────────────────────────────────

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "footer_bar.kv"))

class FooterBar(BoxLayout):
    """Нижняя панель с текстом версии и статусом"""
    version: StringProperty = StringProperty("Версия 0.1.0-dev")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Загружаем kv после объявления класса

