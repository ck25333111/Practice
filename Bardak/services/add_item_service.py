# ────────────────────────────────────
# Сервис получения данных для AddItemScreen
# Bardak/services/add_item_service.py
# ────────────────────────────────────

from typing import List, Dict
from Bardak.models.storage.box import Box
from Bardak.models.storage.section import Section
from Bardak.models.storage.cell import Cell
from Bardak.models.storage.storage_place import StoragePlace

class AddItemService:
    """Сервис получения данных для AddItemScreen"""

    @staticmethod
    def get_all_places() -> List[str]:
        print([p.name for p in StoragePlace.select()])
        return [p.name for p in StoragePlace.select()]

    @staticmethod
    def get_boxes_for_place(place_name: str) -> List[str]:
        place = StoragePlace.get_or_none(StoragePlace.name == place_name)
        if not place:
            return []
        return [box.name for box in Box.select().where(Box.storage_place == place)]

    @staticmethod
    def get_sections_for_box(place_name: str, box_name: str) -> List[str]:
        place = StoragePlace.get_or_none(StoragePlace.name == place_name)
        if not place:
            return []
        box = Box.get_or_none(Box.name == box_name, Box.storage_place == place)
        if not box:
            return []
        return [s.name for s in Section.select().where(Section.box == box)]


    @staticmethod
    def get_cells_for_section(section_name: str) -> List[Dict]:
        """
        Получить список ячеек (cell) для конкретной секции по её имени.
        Возвращает список словарей с полями row, column, label и categories.
        """

        section = Section.select().where(Section.name == section_name).first()
        if not section:
            return []

        cells_query = Cell.select(Cell.row, Cell.column, Cell.label).where(Cell.section == section)
        return [{"row": c.row, "column": c.column, "label": c.label} for c in cells_query]


    @staticmethod
    def get_cells_for_box(place_name: str, box_name: str) -> List[Dict]:
        """
        Возвращает ВСЕ ячейки всех секций данного бокса.
        """
        place = StoragePlace.get(StoragePlace.name == place_name)
        box = Box.get(Box.name == box_name, Box.storage_place == place)
        sections = Section.select().where(Section.box == box)

        cells = []
        for section in sections:
            section_cells = Cell.select().where(Cell.section == section)
            for cell in section_cells:
                cells.append({
                    "row": cell.row,
                    "column": cell.column,
                    "label": cell.label,
                    "occupied": bool(cell.categories),  # или другой флаг
                })
        return cells