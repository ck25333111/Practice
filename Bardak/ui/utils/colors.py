# ────────────────────────────────────────────────────────────────
# Bardak/ui/utils/colors.py
# Утилита для конвертации HEX в RGBA с альфой
# ────────────────────────────────────────────────────────────────
def get_color(color: str | tuple, alpha: float = 1.0) -> tuple:
    """Возвращает RGBA-цвет по названию или HEX-коду с нужной прозрачностью"""
    if isinstance(color, tuple):
        return color[0], color[1], color[2], alpha  # если уже RGBA, просто меняем альфу

    if color in COLOR_PALETTE:
        r, g, b, _ = COLOR_PALETTE[color]
        return r, g, b, alpha                       # берём из палитры и перекидываем альфу

    if isinstance(color, str) and color.startswith("#"):
        return hex_to_rgba(color, alpha)           # если это прям HEX

    raise ValueError(f"Невозможно определить цвет: {color}")

def hex_to_rgba(hex_color: str, alpha: float = 1.0) -> tuple[float, float, float, float]:
    """Преобразует HEX-цвет в формат RGBA с заданной прозрачностью"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return r, g, b, alpha


COLOR_PALETTE: dict[str, tuple[float, float, float, float]] = {
    "YELLOW": hex_to_rgba("#fffb00", 1),
    "WHITE": hex_to_rgba("#ffffff", 1),
    "BLACK_TRANSPARENT": hex_to_rgba("#000000", 0.2),
    "GRAY": hex_to_rgba("#888888", 1),
    "RED": hex_to_rgba("#ff0000", 1),
    "GREEN": hex_to_rgba("#27ff00", 1),

}