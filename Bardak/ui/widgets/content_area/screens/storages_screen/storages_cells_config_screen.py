# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/content_area/screens/storages_cells_config_screen.py
# Экран конфигурации ячеек внутри каждого ящика
# ────────────────────────────────────────────────────────────────

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import ListProperty
from Bardak.ui.widgets.common.box_label_input import BoxLabelInput
from Bardak.services.storage_wizard_db_save import StorageWizardSaver

class StoragesCellsConfigScreen(Screen):
    """
    Экран, позволяющий указать размеры ячеек для каждой секции.
    Используется после ввода количества ящиков по рядам.
    """

    sections: list = ListProperty()

    def on_pre_enter(self):
        """При входе на экран — построить поля ввода для каждой секции"""
        self._build_fields_for_each_section()

    def _build_fields_for_each_section(self) -> None:
        """Создаёт поля ввода X/Y для каждой секции (ящика в ряду)"""
        container = self.ids.sections_inputs_container  # ⚠️ Переименуй в .kv файле тоже
        container.clear_widgets()

        for section in self.sections:
            label = f"{section['label']}"  # Например: "2 ряд — ящик №3"
            input_widget = BoxLabelInput(
                label_text=label,
                input_hints=["По оси X", "По оси Y"],
                divider_text="x"
            )
            container.add_widget(input_widget)

    def _extract_cell_sizes_from_inputs(self) -> dict[str, dict[str, int]]:
        """
        Собирает размеры ячеек из виджетов.
        Возвращает: {'A1': {'cols': 4, 'rows': 3}, ...}
        """
        container = self.ids.sections_inputs_container
        result = {}

        for idx, widget in enumerate(container.children[::-1]):
            section_data = self.sections[idx]
            machine_label = section_data['machine_label']
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
        """Находит все TextInput в переданном виджете."""
        return [child for child in widget.walk(restrict=True)
                if child.__class__.__name__ == "TextInput"]

    def _save_to_wizard_state(self, cell_sizes: dict) -> None:
        """Сохраняет данные в wizard_state приложения."""
        ws = App.get_running_app().wizard_state
        ws.cell_sizes = cell_sizes
        ws.log()

    def on_continue(self) -> None:
        """Запуск сохранения всех данных в БД"""
        cell_sizes = self._extract_cell_sizes_from_inputs()
        self._save_to_wizard_state(cell_sizes)

        ws = App.get_running_app().wizard_state
        try:
            saver = StorageWizardSaver(ws)
            saver.save()
        except Exception as e:
            print(f"❌ Ошибка при сохранении в базу: {e}")
        else:
            print("✅ Успешно сохранено в базу")
