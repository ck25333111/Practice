def hex_to_rgba_string(hex_color: str, alpha: float = 1.0) -> str:
    """
    Конвертирует HEX в строку 'rgba: R, G, B, A' для kv.

    :param hex_color: Цвет в формате '#RRGGBB' или 'RRGGBB'
    :param alpha: Прозрачность от 0 до 1
    :return: Строка вида 'rgba: 171, 255, 177, 0.2'
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba: {r / 255:.1f}, {g / 255:.1f}, {b / 255:.1f}, {alpha:.1f}"


print(hex_to_rgba_string("#bfff90", 1))
