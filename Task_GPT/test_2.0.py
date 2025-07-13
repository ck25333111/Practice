from idlelib.debugger_r import restart_subprocess_debugger
from typing import List, Dict, Optional, Iterator
from functools import wraps
import time
from datetime import datetime

def chunked(data: list[int], size: int) -> Iterator[list[int]]:
    """Генератор, разбивающий список на подсписки указанного размера."""
    for i in range(0, len(data), size):
        yield data[i:i+size]

def repeat(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'Привет {name}')

def logs_time(func_name: str, duration: float) -> None:
    now = datetime.now()
    timestamp = now.strftime('%d.%m.%Y %H:%M:%S')

    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{timestamp} | {func_name} | {duration}\n')

def func_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # старт времени
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f'Функция {func.__name__} работала {duration:.4f} секунды ')
        logs_time(func.__name__, duration)
        return result
    return wrapper

@func_timer
def heavy_function(numb):
    for i in range(1000):
        time.sleep(2.5)
        return numb ** 100

def parser_log() -> List[str]:
    try:
        time_func = []
        with open('log.txt', 'r', encoding='utf-8') as file:
            for line  in file:
                list_string = line.replace(' ','').split('|')
                if float(list_string[2]) > 3:
                    time_func.append(list_string[1])
            return time_func

    except Exception as e:
        print(e)

def bubble_sort(list_sort: List[int]) -> List[int]:
    """Сортировка пузырьками"""

    for i in range(len(list_sort)):
        swapper = False
        for j in range(0, len(list_sort) - i - 1):
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j+1], list_sort[j] = list_sort[j], list_sort[j+1]
                swapper = True
        if not swapper:
            break
    return list_sort

if __name__ == '__main__':
    print(bubble_sort([9, 3, 7, 1, 2]))
    # data = [1, 2, 3, 4, 5, 6, 7]
    # for chunk in chunked(data, 3): #Генератор, разбивающий список на подсписки указанного размера.
    #     print(chunk)
    # greet('Вася')
    # print(heavy_function(99))
    # print(f'Функции работают более 3 секунд:\n{parser_log()}')

