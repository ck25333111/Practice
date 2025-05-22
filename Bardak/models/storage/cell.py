# ────────────────────────────────────────────────────────────────
# Bardak.models/storage/cell.py
# Модель: Ячейка (Cell)
# Назначение: Представляет отдельную ячейку внутри отсека Section,
# содержит информацию о содержимом и метаданных для поиска.
# ────────────────────────────────────────────────────────────────


from Bardak.models.storage.section import Section
from Bardak.models.models_base import BaseModel
from peewee import CharField, ForeignKeyField, IntegerField, TextField, DateTimeField
from datetime import datetime
import playhouse.sqlite_ext as ext


class Cell(BaseModel):
    """Модель ячейки хранения внутри отсека (Section)"""
    section = ForeignKeyField(Section, backref='cells', on_delete='CASCADE')  # Ссылка на родительский отсек
    row: int = IntegerField()   # Номер строки (позиция ячейки внутри сетки)
    column: int = IntegerField()    # Номер столбца (позиция ячейки внутри сетки)
    label: str = CharField(max_length=100, null=True)    # Назначение/подпись
    categories = ext.JSONField(default=list)(default=list)    # Категории (может быть несколько)
    description = TextField(null=True)      # Описание содержимого

    # Размеры ячейки (мм или см — определим потом)
    length = IntegerField(null=True)
    width = IntegerField(null=True)
    height = IntegerField(null=True)

    # Таймстемпы
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    # История перемещений/изменений (пока просто текстом)
    change_history = TextField(null=True)

    def __str__(self) -> str:
        """Текстовое представление ячейки"""
        return f"Cell ({self.row}, {self.column}) in Section {self.section.id}"
