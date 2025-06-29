# ────────────────────────────────────────────────────────────────
# Bardak.models/storage/box.py
# Модель бокса внутри места хранения
# ────────────────────────────────────────────────────────────────

from peewee import CharField, ForeignKeyField, SQL
from Bardak.models.storage.storage_place import StoragePlace
from Bardak.models.models_base import BaseModel

class Box(BaseModel):
    """Модель ящика, принадлежащего месту хранения"""

    name = CharField(max_length=25) # Название бокса, например: "Тумбочка"
    storage_place = ForeignKeyField(StoragePlace, backref='boxes', on_delete='CASCADE')

    class Meta:
        # Уникальность имени бокса в рамках места хранения
        constraints = [SQL('UNIQUE(name, storage_place_id)')]


    def __str__(self):
        return f'{self.name} в {self.storage_place.name}'