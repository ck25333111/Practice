# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_cells_config_screen.py
# Экран конфигурации ячеек внутри каждого ящика
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import ListProperty
from Bardak.ui.widgets.common.box_label_input import BoxLabelInput

class StoragesCellsConfigScreen(Screen):
    boxes: list = ListProperty()
    print(f"StoragesCellsConfigScreen")

    def on_pre_enter(self):
        print(f"Получили boxes: {self.boxes}")
        """При входе на экран — сгенерировать поля по каждому ящику"""
        container = self.ids.boxes_inputs_container
        container.clear_widgets()

        for index, box in enumerate(self.boxes):
            label = f"Ячейки в ящике {box['label']} (Строки x Столбцы)"
            input_widget = BoxLabelInput(
                label_text=label,
                input_hints=["напр. 4", "напр. 5"],
                divider_text="x"
            )
            container.add_widget(input_widget)

    def on_continue(self):
        """Пока просто заглушка — можно дописать что делать дальше"""
        print("Продолжить нажато — логика ещё не реализована")
