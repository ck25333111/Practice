# ────────────────────────────────────
# Bardak/services/add_item_service.py
# ────────────────────────────────────

from typing import List
from Bardak.models.storage.box import Box
from Bardak.models.storage.section import Section
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
