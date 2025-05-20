"""
🔥 Задача №1: Чётные и нечётные
Условие: Пользователь вводит число n. Напиши программу, которая выводит все чётные числа от 0 до n включительно.
Пример: Введите число: 10  Вывод: 0 2 4 6 8 10
Усложнёнка (по желанию): Сделай, чтобы числа выводились через запятую, но без лишней запятой в конце.
"""
from importlib.resources import read_text


def even_and_odd():
    N = int(input('Введите число: '))

    gen_numb = (i for i in range(N+1) if i % 2 == 0)
    print('Generator')
    print(', '.join(str(num) for num in gen_numb))

    print('\nfunc map filter')
    filter_num = map(str, filter(lambda x: x%2==0, range(N+1)))
    print(' '.join(filter_num))

    # Решение от GPT
    print(', '.join(str(i) for i in range(int(input("Введите число: ")) + 1) if i % 2 == 0))

#******************

"""
🧠 Задача №2: Палиндром
Условие:
Пользователь вводит строку. Нужно определить, является ли она палиндромом — то есть читается одинаково слева направо и справа налево.
Примеры:

Введите строку: казак
Вывод: палиндром

Введите строку: питон
Вывод: не палиндром

Усложнёнка:
Хочешь флексить? Убери пробелы и пунктуацию, чтобы строка "А роза упала на лапу Азора" тоже засчитывалась как палиндром 😏
"""
def palindrome():
    word = input('Введите строку:').lower().replace(' ','')
    print('палиндром' if word == word[::-1] else 'не палиндром')



"""
🧮 Задача №3: Угадай число с минимумом попыток
Условие:
У тебя есть диапазон чисел от 1 до 100. Некий таинственный компьютер задумал одно из них (мы храним его в переменной secret).
Твоя задача — угадать это число за минимальное количество попыток. Но! Вместо угадывания "в лоб", используй алгоритм бинарного поиска.
🎯 Пример вывода:
Попытка 1: пробую 50
Больше!
Попытка 2: пробую 75
Меньше!
...
Угадал! Число: 63. Кол-во попыток: 5

"""
import random
def guess_the_number():
    hidden_number = random.randint(1, 100)
    low = 1
    higt = 100
    count = 0

    while True:
        guess = (higt + low) // 2
        count += 1
        if hidden_number < guess :
            print(f'Ищем в диапазоне от {low} до {higt}')
            print(f'Попытка {count} Пробуем число: {guess }')
            higt = guess -1
        elif hidden_number > guess :
            print(f'Ищем в диапазоне от {low} до {higt}')
            print(f'Попытка {count} Пробуем число: {guess }')
            low = guess +1
        elif hidden_number == guess :
            print('Загаданное число ',hidden_number)
            print('Отгаданое: ', guess )
            break


"""
🧮 Задача №4: Бинарный Поиск по Списку:
📋 Условие:
У тебя есть отсортированный список чисел.
Нужно найти индекс заданного элемента.
Если такого элемента нет — вернуть -1.
Пример:

arr = [3, 8, 15, 23, 42, 55, 78, 90]
target = 42
# Результат: индекс 4

"""
unsorted = [2, 15, 18, 11, 56, 5, 21, 45, 65, 89, 45, 12, 63, 74, 2, 1, 36]
arr = sorted(unsorted)
print(arr)

def binary_search(arr, target):
    low = 0
    hight = len(arr)-1

    while low <= hight:
        mid = (low + hight) // 2
        if arr[mid] > target:
            hight = mid - 1
            print(f"Ищем в диапазоне от {low} до {hight}")
        elif arr[mid] < target:
            low = mid + 1
            print(f"Ищем в диапазоне от {low} до {hight}")
        elif arr[mid] == target:
            return f'Число {target} на индексе {mid}'
    return -1



"""
Бинарный поиск по списку рекурсией
"""
low = 0
hight = len(arr)-1

def binary_search_recurse(arr, target, low, hight):
    if low > hight:
        return -1
    mid = (low + hight) // 2
    if arr[mid] == target:
        return (f'Число {target} на индексе {mid}')
    elif arr[mid] > target:
        hight = (mid - 1)
        print(f"Ищем в диапазоне от {low} до {hight}")
        return binary_search_recurse(arr, target, low, hight)
    else:
        low = (mid + 1)
        print(f"Ищем в диапазоне от {low} до {hight}")
        return binary_search_recurse(arr, target, low, hight)




if __name__ == '__main__':
    # even_and_odd()
    # palindrome()
    # guess_the_number()
    # print(binary_search(arr, 15))
    print(binary_search_recurse(arr, 655, low, hight))
