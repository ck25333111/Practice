# ────────────────────────────────────────────────────────────────
# ui/style/style_loader.py — Централизованная загрузка всех kv-стилей
# ────────────────────────────────────────────────────────────────

from kivy.lang import Builder

# Список всех kv-файлов со стилями
STYLE_FILES = [
    "ui/style/screen_container.kv",
    # "ui/style/rounded_border.kv",
    # "ui/style/buttons.kv",
    # "ui/style/forms.kv",
    # "ui/style/containers.kv",
    # "ui/style/labels.kv",
    # добавляй по ходу пьесы
]

def load_all_styles() -> None:
    """Загружает все kv-файлы со стилями"""
    for path in STYLE_FILES:
        Builder.load_file(path)
