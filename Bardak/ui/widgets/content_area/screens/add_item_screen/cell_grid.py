# ────────────────────────────────────────────────────────────────
# Bardak/ui/widgets/content_area/screens/add_item_screen/cell_grid.py
# Построение сетки ячеек на основе данных из базы
# ────────────────────────────────────────────────────────────────

from typing import List, Dict, Tuple, Optional
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from Bardak.ui.widgets.content_area.screens.add_item_screen.clickable_cell import ClickableCell


def build_cell_grid(cell_data: List[Dict]) -> GridLayout:
    """
    Строит сетку ClickableCell на основе данных ячеек из базы.

    :param cell_data: Список словарей с ключами 'row', 'column', 'label'.
    :return: GridLayout с ячейками.
    """
    print('cell_data ',cell_data)
    # Получаем размеры сетки
    max_row, max_col = get_grid_dimensions(cell_data)
    print(f'max_row {max_row}\n max_col {max_col}')

    # Создаём пустую матрицу нужного размера
    matrix = create_empty_matrix(max_row, max_col)
    print(f'matrix {matrix}')

    # Заполняем матрицу ячейками
    fill_matrix_with_cells(matrix, cell_data)
    print(f'Заполняем матрицу ячейками')

    # Создаём сам GridLayout и добавляем в него ячейки
    grid = create_grid_layout(matrix, max_row, max_col)
    print(f'Создаём сам GridLayout и добавляем в него ячейки {grid}')

    return grid


def get_grid_dimensions(cell_data: List[Dict]) -> Tuple[int, int]:
    """
    Вычисляет максимальное количество строк и столбцов на основе данных ячеек.

    :param cell_data: Список данных ячеек.
    :return: Кортеж (max_row, max_col).
    """
    max_row = max(cell["row"] for cell in cell_data)
    max_col = max(cell["column"] for cell in cell_data)
    return max_row, max_col


def create_empty_matrix(rows: int, cols: int) -> List[List[Optional[ClickableCell]]]:
    """
    Создаёт двумерную матрицу с заданными размерами.

    :param rows: Кол-во строк.
    :param cols: Кол-во столбцов.
    :return: Матрица из None.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]


def fill_matrix_with_cells(matrix: List[List[Optional[ClickableCell]]], cell_data: List[Dict]) -> None:
    """
    Заполняет матрицу виджетами ClickableCell на основе данных.

    :param matrix: Пустая матрица.
    :param cell_data: Список словарей с данными ячеек.
    """
    for cell in cell_data:
        row_idx = cell["row"] - 1  # 0-индексация
        col_idx = cell["column"] - 1
        label = cell["label"]  # метка ячейки, типа 'A1'
        occupied = cell.get("occupied", False)  # если нет ключа — считаем, что не занята

        # Создаём ячейку с правильным состоянием занятости
        cell_widget = ClickableCell(label=label, occupied=occupied)

        # Кладём в матрицу по координатам
        matrix[row_idx][col_idx] = cell_widget


def create_grid_layout(
    matrix: List[List[Optional[ClickableCell]]],
    rows: int,
    cols: int,
) -> GridLayout:
    """
    Создаёт виджет GridLayout и заполняет его ячейками из матрицы.

    :param matrix: Матрица с виджетами.
    :param rows: Кол-во строк.
    :param cols: Кол-во столбцов.
    :return: GridLayout.
    """
    grid = GridLayout(
        rows=rows,
        cols=cols,
        spacing=dp(4),
        padding=dp(4),
        size_hint=(None, None),
    )

    # Выставляем габариты на основе числа ячеек
    cell_size = dp(50)
    grid.width = cell_size * cols + dp(4) * (cols - 1)
    grid.height = cell_size * rows + dp(4) * (rows - 1)

    # Добавляем виджеты в сетку
    for row in matrix:
        for cell in row:
            if cell:
                grid.add_widget(cell)

    return grid
