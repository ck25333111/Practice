# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_rows_config_screen.py
# Экран конфигурации количества отсеков в каждом ряду (sections)
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty
from Bardak.ui.widgets.common.simple_label_inputs import SimpleLabelInputs
from Bardak.ui.widgets.content_area.screens.storages_screen.storages_cells_config_screen import StoragesCellsConfigScreen
from kivy.app import App


class StoragesRowsConfigScreen(Screen):
    """
    Экран ввода количества ящиков (секций) по каждому ряду.
    Результат сохраняется в wizard_state.sections.
    """
    rows_count: int = NumericProperty(0)  # сколько всего рядов
    row_sections: ListProperty = ListProperty()  # список инпутов по каждому ряду

    def on_pre_enter(self) -> None:
        """
        Перед входом на экран — отрисовывает инпуты под каждый ряд
        """
        container = self.ids.rows_inputs_container
        container.clear_widgets()
        self.row_sections.clear()  # на случай повтора

        for i in range(self.rows_count):
            input_widget = SimpleLabelInputs(
                label_text=f"Ящиков в {i + 1} ряду",
                hint_text="Например: 3"
            )
            container.add_widget(input_widget)
            self.row_sections.append(input_widget)

    def get_sections_structure(self) -> list[dict]:
        """
        Формирует структуру всех ящиков (sections) по рядам
        :return: Список словарей с row, box, label, machine_label
        """
        sections = []

        for row_index, input_widget in enumerate(self.row_sections):
            try:
                sections_count = int(input_widget.ids.input_field.text.strip())
            except ValueError:
                continue  # если не число — нахуй

            for box_index in range(1, sections_count + 1):
                row_num = row_index + 1
                label = f"{row_num} ряд  — ящик №{box_index}"
                machine_label = f"{chr(64 + row_num)}{box_index}"  # A1, B2 и т.д.

                sections.append({
                    "row": row_num,
                    "box": box_index,
                    "label": label,
                    "machine_label": machine_label
                })

        return sections

    def on_continue(self) -> None:
        """
        Обработка нажатия 'Далее':
        - Сохраняет секции в wizard_state
        - Передаёт их на следующий экран
        """
        sections = self.get_sections_structure()

        # Сохраняем в глобальное состояние
        ws = App.get_running_app().wizard_state
        ws.sections = sections

        # Передаём на следующий экран и переключаемся
        next_screen: StoragesCellsConfigScreen = self.manager.get_screen("storages_cells_config_screen")
        next_screen.sections = sections
        self.manager.current = "storages_cells_config_screen"
