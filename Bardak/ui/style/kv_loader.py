# ────────────────────────────────────────────────────────────────
# Bardak/ui/style/style_loader.py
# Загружает все необходимые .kv файлы из разных частей ui по проекту
# ────────────────────────────────────────────────────────────────

import os
from kivy.lang import Builder


def load_all_kv() -> None:
    """Загружает все .kv файлы проекта для правильного связывания UI и логики"""
    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))  # ui/ стиль папка, поднимаемся на уровень выше до ui/

    kv_paths = [

        # Виджеты общего назначения
        os.path.join(base_dir, "widgets", "common", "double_input_field.kv"),
        os.path.join(base_dir, "widgets", "common", "simple_label_inputs.kv"),
        os.path.join(base_dir, "widgets", "common", "box_label_input.kv"),

        # Основные виджеты и экраны
        os.path.join(base_dir, "widgets", "content_area", "content_area.kv"),
        os.path.join(base_dir, "widgets", "content_area", "left_menu", "left_menu.kv"),
        os.path.join(base_dir, "widgets", "footer_bar", "footer_bar.kv"),
        os.path.join(base_dir, "widgets", "top_bar", "top_bar.kv"),
        os.path.join(base_dir, "main_screen.kv")
    ]

    # Подгружаем все экраны из content_area/screens/
    screens_dir = os.path.join(base_dir, "widgets", "content_area", "screens")
    # Проходим рекурсивно по всем подпапкам
    for root, dirs, files in os.walk(screens_dir):
        for file in files:
            if file.endswith(".kv"):
                kv_paths.append(os.path.join(root, file))

    # Загружаем каждый файл .kv через Builder.load_file
    for kv_file in kv_paths:
        if os.path.isfile(kv_file):
            Builder.load_file(kv_file)
            print(f"Загружен: {kv_file}")
        else:
            print(f"[style_loader] WARNING: .kv файл не найден: {kv_file}")
