# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_rows_config_screen.py
# Экран конфигурации количества отсеков в каждом ряду
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty
from Bardak.ui.widgets.common.simple_label_inputs import SimpleLabelInputs
from Bardak.ui.widgets.content_area.screens.storages_screen.storages_cells_config_screen import StoragesCellsConfigScreen


class StoragesRowsConfigScreen(Screen):
    rows_count: int = NumericProperty(0)
    row_sections: ListProperty = ListProperty()

    def on_pre_enter(self):
        """При заходе на экран — сгенерировать нужные поля"""
        container = self.ids.rows_inputs_container
        container.clear_widgets()

        for i in range(self.rows_count):
            input_widget = SimpleLabelInputs(
                label_text=f"Ящиков в {i + 1} ряду ",
                hint_text="Например: 3"
            )
            container.add_widget(input_widget)
            self.row_sections.append(input_widget)

    def get_boxes_structure(self) -> list[dict]:
        """Формирует структуру всех ящиков по рядам и количеству в каждом ряду"""
        boxes = []
        for row_index, input_widget in enumerate(self.row_sections):
            try:
                boxes_count = int(input_widget.ids.input_field.text.strip())
                print('boxes_count', boxes_count)
            except ValueError:
                continue  # если не число — нахуй

            for box_index in range(1, boxes_count + 1):
                boxes.append({
                    "row": row_index + 1,
                    "box": box_index
                })
        return boxes

    def on_continue(self) -> None:
        boxes = self.get_boxes_structure()
        print('on_continue -> boxes', boxes)

        next_screen = self.manager.get_screen("storages_cells_config_screen")

        for box in boxes:
            # Придумываем читаемую подпись — это будет использоваться как label в интерфейсе
            box['label'] = f"{box['row']} ряд  — ящик №{box['box']}"  # 🟢 Для отображения
            # Дополнительно добавим machine_label если надо использовать кодовое имя (типа "A1")
            box['machine_label'] = f"{chr(64 + box['row'])}{box['box']}"  # 🟡 Техническая маркировка

        next_screen.boxes = boxes
        self.manager.current = "storages_cells_config_screen"


