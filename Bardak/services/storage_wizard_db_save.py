# ────────────────────────────────────────────────────────────────
# Bardak/services/storage_wizard_db_save.py
# Сервис сохранения данных из wizard_state в базу данных (Peewee)
# Класс StorageWizardSaver — архитектурная основа сохранения
# ────────────────────────────────────────────────────────────────

from typing import List, Optional
from Bardak.models.storage.box import Box
from Bardak.models.storage.cell import Cell
from Bardak.models.storage.section import Section
from Bardak.models.storage.storage_place import StoragePlace
from Bardak.services.wizard_state import WizardState

class StorageWizardSaver:
    """
    Класс-сервис для пошагового сохранения всех данных из wizard_state в БД.
    Предназначен для использования на последнем шаге мастера.
    """

    def __init__(self, wizard_state: WizardState) -> None:
        """
        Инициализирует сервис сохранения, принимает на вход wizard_state.

        :param wizard_state: Состояние мастера добавления хранилища.
        """

        self.ws: WizardState = wizard_state
        self.storage_place: Optional[StoragePlace] = None


    def _save_storage_place(self) -> StoragePlace:
        """
        Сохраняет (или получает) место хранения на основе данных из wizard_state.
        :return: Экземпляр модели StoragePlace (существующий или созданный).
        """
        # Достаём название места хранения из wizard_state
        name = self.ws.storage_place_name

        # Если оно пустое
        if not name:
            raise ValueError("Поле 'storage_place_name' обязательно для сохранения.")

        # Пытаемся найти существующую запись по имени
        existing = StoragePlace.get_or_none(StoragePlace.name == name)

        if existing:
            # Если место уже есть — логируем и возвращаем
            self.storage_place = existing
            return existing

        # Если не нашли — создаём новое место хранения
        place = StoragePlace.create(name=name)

        # Сохраняем его в атрибут, чтобы дальше использовать при связях
        self.storage_place = place

        # Возвращаем сохранённый экземпляр
        return place

    def _save_boxes(self) -> List[Box]:
        if not self.storage_place:
            raise ValueError("Невозможно сохранить боксы без StoragePlace.")

        saved_boxes: List[Box] = []

        # self.ws.box_name — вот тут лежит название мебели, типа "Стол"
        box_name = self.ws.box_name or "Без имени"

        # В wizard_state.boxes у тебя список с инфой по рядам и ящикам — их нужно использовать для _save_sections, а не для названий боксов!

        # Создаём один бокс с именем мебели — в твоём примере "Стол"
        box = Box.create(
            name=box_name,
            storage_place=self.storage_place
        )

        saved_boxes.append(box)

        return saved_boxes


    def _save_sections(self, box: Box) -> List[Section]:
        """
        Сохраняет все секции (отсеки) внутри одного Box (мебели),
        используя данные из wizard_state.sections

        :param box: Экземпляр Box (мебели), к которому будут привязаны секции.
        :return: Список созданных Section-ов.
        """
        saved_sections: List[Section] = []

        # Проходим по всем секциям из состояния визарда
        for section_data in self.ws.sections:
            label = section_data.get("label")  # например: "1 ряд — ящик №1"

            if not label:
                continue  # пропускаем, если нет названия секции

            section = Section.create(
                name=label,  # читаемое название секции
                box=box  # связываем с конкретной мебелью (Box)
            )

            saved_sections.append(section)

        return saved_sections

    def _save_cells(self, sections: List[Section]) -> List[Cell]:
        """
        Создаёт ячейки (Cell) внутри каждой секции (Section) по конфигурации
        размеров из wizard_state.cell_sizes, используя machine_label.

        :param sections: Список созданных секций
        :return: Список всех созданных ячеек
        """
        ws = self.ws
        created_cells: List[Cell] = []

        # Создаём карту: machine_label -> размеры
        cell_sizes = ws.cell_sizes  # {'A1': {'cols': 5, 'rows': 4}, ...}

        # Создаём карту: section.name -> machine_label
        label_to_machine_label = {
            s['label']: s['machine_label']
            for s in ws.sections
            if 'label' in s and 'machine_label' in s
        }

        for section in sections:
            machine_label = label_to_machine_label.get(section.name)

            if not machine_label:
                continue  # если не нашли соответствие — пропускаем

            size = cell_sizes.get(machine_label)
            if not size:
                continue  # нет размеров — тоже пропускаем

            rows = size.get("rows", 0)
            cols = size.get("cols", 0)

            for row in range(1, rows + 1):
                for col in range(1, cols + 1):
                    label = f"{chr(64 + row)}{col}"  # генерим названия A1, B2 и т.п.

                    cell = Cell.create(
                        section=section,
                        row=row,
                        column=col,
                        label=label,
                        categories=[],
                        description=None,
                        length=None,
                        width=None,
                        height=None,
                        change_history=None
                    )

                    created_cells.append(cell)

        return created_cells

    def save(self) -> None:
        """
        Точка входа — запускает последовательное сохранение всех сущностей:
        - Места хранения
        - Мебели (Box)
        - Секций (ящиков)
        - Ячеек внутри каждой секции
        """
        # 1. Сохраняем место хранения (например: "Кухня")
        self._save_storage_place()

        # 2. Сохраняем саму мебель (например: "Шкаф") — вернётся 1 элемент
        boxes = self._save_boxes()
        box = boxes[0]  # Мы точно знаем, что он один

        # 3. Сохраняем секции (например: "2 ряд — ящик №3"), привязанные к box
        sections = self._save_sections(box)

        # 4. Сохраняем ячейки (например: A1, B2...) внутри каждой секции
        self._save_cells(sections)

