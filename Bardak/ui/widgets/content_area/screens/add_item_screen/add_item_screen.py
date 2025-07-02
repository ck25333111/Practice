# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/screens/add_item_screen/add_item_screen.py
# Логика экрана добавления предмета — обработка выбора места хранения
# ────────────────────────────────────────────────────────────────

from typing import List
from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread
from Bardak.services.add_item_service import AddItemService
from Bardak.ui.widgets.content_area.screens.add_item_screen.cell_grid import build_cell_grid


class AddItemScreen(Screen):
    """Экран добавления предмета — управление отображением и обработка событий."""

    def on_pre_enter(self) -> None:
        """Загружается при переходе на экран. Загружает список мест хранения."""

        print("📲 Открыт экран AddItemScreen")
        print("🧪 self.ids:", self.ids.keys())
        self._load_places()

    def _load_places(self) -> None:
        places = AddItemService.get_all_places()
        self._update_place_spinner(places)

    @mainthread
    def _update_place_spinner(self, places: List[str]) -> None:
        spinner = self.ids.place_spinner
        spinner.values = places
        spinner.text = "Место хранения"

        self.ids.box_spinner.disabled = True
        self.ids.section_spinner.disabled = True

    def on_place_selected(self, place_name: str) -> None:
        print(f"📦 Выбрано место хранения: {place_name}")
        if not place_name or place_name == "Место хранения":
            return

        boxes = AddItemService.get_boxes_for_place(place_name)
        self._update_box_spinner(boxes)

    @mainthread
    def _update_box_spinner(self, boxes: List[str]) -> None:
        spinner = self.ids.box_spinner
        spinner.values = boxes
        spinner.text = "Мебель / Бокс"
        spinner.disabled = False

        self.ids.section_spinner.text = "Секция / Ящик"
        self.ids.section_spinner.values = []
        self.ids.section_spinner.disabled = True

    def on_box_selected(self, box_name: str) -> None:
        print(f"📦 Выбран Бокс>: {box_name}")
        place_name = self.ids.place_spinner.text
        if not box_name or box_name == "Мебель / Бокс":
            return

        sections = AddItemService.get_sections_for_box(place_name, box_name)
        self._update_section_spinner(sections)


    def on_section_selected(self, section_name: str) -> None:
        print(f"📊 Выбрана секция / ящик: {section_name}")
        if not section_name or section_name == "Секция / Ящик":
            return
        # Здесь вызываем приватный метод, который отрисует сетку
        self.display_cell_grid_for_section(section_name)


    def display_cell_grid_for_section(self,section_name):
        print(f"Начинаем отрисовку {section_name}")

        # 1. Получаем данные по ячейкам
        cell_data = AddItemService.get_cells_for_section(section_name)

        # Строим сетку
        grid_widget = build_cell_grid(cell_data)

        # Добавляем на экран
        container = self.ids.cell_grid_container  # ← этот id должен быть в .kv-файле!
        container.clear_widgets()  # на всякий случай очищаем
        container.add_widget(grid_widget)


    @mainthread
    def _update_section_spinner(self, sections: List[str]) -> None:
        spinner = self.ids.section_spinner
        spinner.values = sections
        spinner.text = "Секция / Ящик"
        spinner.disabled = False