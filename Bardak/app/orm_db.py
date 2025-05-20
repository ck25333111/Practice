from Bardak.app.models import Furniture, BaseModel, db
from loguru import logger

# Создаём таблицу
db.connect()
db.create_tables([Furniture])

Furniture.create(name='Стол')
Furniture.create(name='Шкаф')