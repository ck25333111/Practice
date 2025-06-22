from typing import Optional, List, Dict


class WizardState:
    """
    Хранит состояние мастера добавления хранилища.
    Все поля объявлены с аннотациями и базовыми значениями.
    """

    def __init__(self) -> None:
        """
        Хранилище состояния мастера добавления хранилища (wizard_state).
        Служит для накопления всех данных между шагами.
        """

        # Название общего места хранения (например: "Балкон", "Гараж")
        self.storage_place_name: Optional[str] = None

        # Название самого контейнера (шкаф, стеллаж, ящик и т.п.)
        self.box_name: Optional[str] = None

        # Количество горизонтальных рядов (по вертикали)
        self.rows_count: Optional[int] = None

        # Список всех ящиков по рядам и индексам:
        # Пример: [{"row": 1, "box": 1, "label": "...", "machine_label": "A1"}, ...]
        self.boxes: List[Dict] = []

        # Размеры ячеек в каждом ящике по machine_label:
        # Пример: {"A1": {"rows": 4, "cols": 5}}
        self.cell_sizes: Dict[str, Dict[str, int]] = {}

    def validate(self) -> None:
        """
        Простейшая валидация полей.
        Бросает исключение, если какие-то ключевые поля не заполнены.
        Вызывай перед сохранением в БД.
        """
        if not self.storage_place_name:
            raise ValueError("Поле 'storage_place_name' не может быть пустым")

        if not self.box_name:
            raise ValueError("Поле 'box_name' не может быть пустым")

        if self.rows_count is None or self.rows_count <= 0:
            raise ValueError("Поле 'rows_count' должно быть положительным числом")

        if not self.boxes:
            raise ValueError("Список 'boxes' пуст. Нужно добавить хотя бы один ящик.")

        if not self.cell_sizes:
            raise ValueError("Словарь 'cell_sizes' пуст. Нужно указать размеры ячеек.")

        # Дополнительно — проверим, что размеры есть для всех ящиков
        for box in self.boxes:
            label = box.get("machine_label")
            if label not in self.cell_sizes:
                raise ValueError(f"Нет размеров ячеек для ящика '{label}'")

    def clear(self) -> None:
        """
        Сбрасывает все данные мастера в изначальное состояние.
        Использовать после успешного сохранения или при сбросе формы.
        """
        self.storage_place_name = None
        self.box_name = None
        self.rows_count = None
        self.boxes.clear()
        self.cell_sizes.clear()

