# ────────────────────────────────────────────────────────────────
# Bardak.models/storage/section.py
# Модель Section — описывает отсеки (например, "Полка", "Ящик 2")
# Каждый отсек принадлежит конкретному ящику (Box)
# Используется для организации вложенности хранения
# ────────────────────────────────────────────────────────────────

from peewee import CharField, ForeignKeyField
from Bardak.models.storage.box import Box
from Bardak.models.models_base import BaseModel

class Section(BaseModel):
    """Модель отсека внутри ящика (например, 'Полка 1', 'Ящик 2')"""
    name: str = CharField(max_length=100, verbose_name="Название отсека")   # Название отсека
    box: Box = ForeignKeyField(Box, backref='section', on_delete='CASCADE', verbose_name='Ящик, в котором находится отсек') # Связь с ящиком, которому принадлежит отсек

    def __str__(self):
        return f'{self.box.name} -> {self.name}'
