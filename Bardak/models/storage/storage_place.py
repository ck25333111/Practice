# ────────────────────────────────────────────────────────────────
# Bardak.models/storage/storage_place.py
# Модель места хранения: гараж, балкон, зал, кухня и т.п.
# ────────────────────────────────────────────────────────────────

from peewee import CharField, TextField, DateTimeField
from Bardak.models.models_base import BaseModel
from datetime import datetime

class StoragePlace(BaseModel):
    """Модель места хранения (например, Гараж, Балкон, зал, кухня)"""
    name = CharField(max_length=100, unique=True)  # Название
    description = TextField(null=True)             # Описание
    created_at = DateTimeField(default=datetime.now)  # Когда добавлено
    updated_at = DateTimeField(default=datetime.now)  # Когда обновлено

    def __str__(self) -> str:
        return f'StoragePlice: {self.name}'

