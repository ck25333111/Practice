from typing import Optional, List, Dict


class WizardState:
    """
    Хранит состояние мастера добавления хранилища.
    Все поля объявлены с аннотациями и базовыми значениями.
    """

    def __init__(self) -> None:
        # Название общего места хранения (например: "Балкон", "Гараж")
        self.storage_place_name: Optional[str] = None

        # Название самого контейнера (шкаф, стеллаж, ящик и т.п.)
        self.box_name: Optional[str] = None

        # Количество горизонтальных рядов (по вертикали)
        self.rows_count: Optional[int] = None

        # Количество секций (отсеков) в каждом ряду (если нужно)
        self.section_count: Optional[int] = None

        # Список всех ящиков по рядам и индексам:
        # Пример:
        # [{"row": 1, "box": 1, "label": "1 ряд — ящик №1", "machine_label": "A1"}, ...]
        self.boxes: List[Dict] = []

        # Размеры ячеек в каждом ящике по machine_label:
        # Пример: {"A1": {"rows": 4, "cols": 5}}
        self.cell_sizes: Dict[str, Dict[str, int]] = {}

    def validate(self) -> None:
        """
        Простейшая валидация полей. Бросает исключение если что не так.
        Вызывай перед использованием.
        """
        if not self.storage_place_name:
            raise ValueError("storage_place_name не может быть пустым")

        if not self.box_name:
            raise ValueError("box_name не может быть пустым")

        if self.rows_count is None or self.rows_count <= 0:
            raise ValueError("rows_count должен быть положительным числом")

        # section_count может быть None или >=0 (если надо, добавь проверку)

    def clear(self) -> None:
        """Сброс всех данных в изначальное состояние"""
        self.storage_place_name = None
        self.box_name = None
        self.rows_count = None
        self.section_count = None
        self.boxes.clear()
        self.cell_sizes.clear()
