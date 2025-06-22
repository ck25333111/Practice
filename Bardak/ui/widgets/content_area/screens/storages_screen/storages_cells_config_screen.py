# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_cells_config_screen.py
# Экран конфигурации ячеек внутри каждого ящика
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import ListProperty
from Bardak.ui.widgets.common.box_label_input import BoxLabelInput

class StoragesCellsConfigScreen(Screen):
    """
    Экран, позволяющий указать размеры ячеек для каждого ящика.
    Используется после конфигурации рядов и ящиков.
    """

    boxes: list = ListProperty()

    def on_pre_enter(self):
        """При входе на экран — сгенерировать поля по каждому ящику"""
        self._build_fields_for_each_box()


    def on_continue(self):
        """
        Обработка нажатия кнопки 'Продолжить':
        - Собирает размеры ячеек с экрана
        - Сохраняет в wizard_state
        - Выводит всё содержимое для отладки
        """
        cell_sizes = self._extract_cell_sizes_from_inputs()
        self._save_to_wizard_state(cell_sizes)
        self._log_wizard_state()

    def _build_fields_for_each_box(self) -> None:
        """Очищает контейнер и создаёт по виджету для каждого ящика."""
        container = self.ids.boxes_inputs_container
        container.clear_widgets()

        for box in self.boxes:
            label = f"{box['label']}"
            input_widget = BoxLabelInput(
                label_text=label,
                input_hints=["По оси X", "По оси Y"],
                divider_text="x"
            )
            container.add_widget(input_widget)

    def _extract_cell_sizes_from_inputs(self) -> dict[str, dict[str, int]]:
        """
        Обходит все виджеты BoxLabelInput и достаёт значения X и Y.
        Возвращает словарь вида: { "A1": {"cols": 4, "rows": 5}, ... }
        """
        container = self.ids.boxes_inputs_container
        result = {}

        for idx, widget in enumerate(container.children[::-1]):
            box_data = self.boxes[idx]
            machine_label = box_data['machine_label']
            inputs = self._get_inputs_from_widget(widget)

            if len(inputs) != 2:
                print(f"⚠️ {machine_label}: не найдено два поля ввода")
                continue

            try:
                cols = int(inputs[0].text.strip())
                rows = int(inputs[1].text.strip())
                result[machine_label] = {"cols": cols, "rows": rows}
            except ValueError:
                print(f"⚠️ {machine_label}: некорректные значения — пропущен")
                continue
        return result

    def _get_inputs_from_widget(self, widget) -> list:
        """Возвращает все TextInput из переданного виджета."""
        return [child for child in widget.walk(restrict=True)
                if child.__class__.__name__ == "TextInput"]

    def _save_to_wizard_state(self, cell_sizes: dict) -> None:
        """Сохраняет cell_sizes в wizard_state."""
        ws = App.get_running_app().wizard_state
        ws.cell_sizes = cell_sizes

    def _log_wizard_state(self) -> None:
        """Печатает всё содержимое wizard_state в консоль."""
        ws = App.get_running_app().wizard_state
        print("=== Полный  конечный wizard_state ===")
        for attr in dir(ws):
            if not attr.startswith('_') and not callable(getattr(ws, attr)):
                print(f"{attr}: {getattr(ws, attr)}")
        print("=== Конец конечный wizard_state ===")
