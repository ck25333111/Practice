# ────────────────────────────────────────────────────────────────
# Bardak.ui.screens.home_dashboard
# Экран главной панели — подключает KV-интерфейс и отображает TopBar
# ────────────────────────────────────────────────────────────────

from Bardak.configs.config_raw import KV_DIR  # <- грузим корень kv-шек
from kivy.uix.boxlayout import BoxLayout
from Bardak.ui.widgets.navigation.top_bar import TopBar  #


class HomeDashboard(BoxLayout):
    """Контейнер главного интерфейса с верхней панелью и основным контентом."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.top_bar = TopBar()
        self.add_widget(self.top_bar)
        # Здесь добавим основной контент позже