# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_cells_config_screen.py
# Экран конфигурации ячеек внутри каждого ящика (визуально по секциям)
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import ListProperty
from Bardak.ui.widgets.common.section_visual import SectionVisual
from Bardak.services.storage_wizard_db_save import StorageWizardSaver


class StoragesCellsConfigScreen(Screen):
    """
    Экран, отображающий все секции (ящики в рядах), позволяя разбивать их на ячейки.
    Используется после указания количества ящиков по рядам.
    """

    sections: list = ListProperty()

    def on_pre_enter(self):
        """При входе на экран — визуально отрисовать секции по рядам"""
        self._build_visual_sections_grid()

    def _build_visual_sections_grid(self) -> None:
        """Строит визуальные компоненты SectionVisual для каждой секции"""
        container = self.ids.sections_inputs_container
        container.clear_widgets()

        # Группируем секции по рядам
        rows: dict[int, list] = {}
        for section in self.sections:
            row = section.get("row", 1)
            rows.setdefault(row, []).append(section)

        # Для каждого ряда создаём горизонтальную строку с секциями
        for row_index in sorted(rows.keys()):
            row_box = self._create_row_box()

            for section in rows[row_index]:
                label = section["label"]
                machine_label = section["machine_label"]
                cell_sizes = App.get_running_app().wizard_state.cell_sizes
                cell_data = self._generate_fake_cell_data_if_exists(cell_sizes.get(machine_label), machine_label)

                section_widget = SectionVisual(
                    label=label,
                    machine_label=machine_label,
                    row=str(row_index),
                    cell_data=cell_data,
                    on_updated=self._build_visual_sections_grid
                )
                row_box.add_widget(section_widget)

            container.add_widget(row_box)

    def _generate_fake_cell_data_if_exists(self, size: dict | None, machine_label: str) -> list:
        """Если для секции уже заданы размеры — генерируем структуру ячеек"""
        if not size:
            return []

        rows = size.get("rows", 1)
        cols = size.get("cols", 1)
        data = []

        for y in range(1, rows + 1):
            for x in range(1, cols + 1):
                label = f"{chr(64 + y)}{x}"  # A1, B2 и т.д.
                data.append({"row": y, "column": x, "label": label, "occupied": False})
        return data

    def _create_row_box(self):
        """Создаёт один горизонтальный ряд для секций"""
        from kivy.uix.boxlayout import BoxLayout

        row_box = BoxLayout(
            orientation="horizontal",
            spacing=20,
            size_hint_y=None
        )
        row_box.bind(minimum_width=row_box.setter("width"))  # если вдруг по ширине
        row_box.bind(minimum_height=row_box.setter("height"))  # это основное

        return row_box

    def on_continue(self) -> None:
        """Запускает финальное сохранение в БД"""
        try:
            ws = App.get_running_app().wizard_state
            saver = StorageWizardSaver(ws)
            saver.save()
        except Exception as e:
            print(f"❌ Ошибка при сохранении: {e}")
        else:
            print("✅ Успешно сохранено")
