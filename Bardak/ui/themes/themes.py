# ────────────────────────────────────────────────────────────────
# Bardak/ui/themes/themes.py
# Определение светлой и тёмной тем приложения с цветами рамок
# ────────────────────────────────────────────────────────────────

from typing import Dict


def get_light_theme() -> Dict[str, str]:
    """Возвращает словарь со светлой темой и цветами рамок"""
    return {
        "primary_color": "#FFFFFF",            # основной цвет (фон)
        "text_color": "#000000",               # цвет текста
        "background_color": "#F5F5F5",         # цвет фона интерфейса
        "accent_color": "#2196F3",             # акцентный цвет (например, кнопки)
        "menu_background": "#E0E0E0",          # фон меню
        "button_background": "#00000000",        # фон кнопок
        "button_text": "#FFFFFF",              # цвет текста кнопок
        "border_color_block": "#CCCCCC",       # цвет рамки блоков
        "border_color_button": "#FFFFFF"       # цвет рамки кнопок (ярко-жёлтый)

    }


def get_dark_theme() -> Dict[str, str]:
    """Возвращает словарь с тёмной темой и цветами рамок"""
    return {
        "primary_color": "#121212",            # основной цвет (темный фон)
        "text_color": "#FFFFFF",               # светлый текст
        "background_color": "#1F1F1F",         # темный фон интерфейса
        "accent_color": "#FF4081",             # яркий акцент (розовый)
        "menu_background": "#2C2C2C",          # фон меню в темной теме
        "button_background": "#00000000",        # фон кнопок темной темы
        "button_text": "#FFFFFF",              # светлый текст кнопок
        "border_color_block": "#444444",       # цвет рамки блоков (темно-серый)
        "border_color_button": "#FFFFFF"       # цвет рамки кнопок (жёлтый)
    }
