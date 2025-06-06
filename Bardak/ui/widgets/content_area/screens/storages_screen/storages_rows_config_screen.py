# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_rows_config_screen.py
# Экран конфигурации количества отсеков в каждом ряду
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty
from Bardak.ui.widgets.common.simple_label_inputs import SimpleLabelInputs

class StoragesRowsConfigScreen(Screen):
    rows_count: int = NumericProperty(0)
    row_sections: ListProperty = ListProperty()

    def on_pre_enter(self):
        """При заходе на экран — сгенерировать нужные поля"""
        container = self.ids.rows_inputs_container
        container.clear_widgets()

        for i in range(self.rows_count):
            input_widget = SimpleLabelInputs(
                label_text=f"Количество отсеков (ящиков) в {i + 1} ряду ",
                hint_text="Например: 3"
            )
            container.add_widget(input_widget)
            self.row_sections.append(input_widget)
