from typing import Dict, List, Optional, Tuple
import re

def stringt_to_dict(stroka: str) -> Dict[str, int]:
    """Принимает строку и возвращает словарь с частотой каждого символа."""
    to_dict = {}
    for letter in stroka:
        to_dict[letter] = to_dict.get(letter, 0) +1
    return to_dict

def invert_dict(stroka: Dict[str, int]) -> Dict[int, str]:
    str_to_int = {}
    for key, value in stroka.items():
        str_to_int[value] = key
    return str_to_int


def find_key_by_value(d: dict[str, int], value: int) -> str | None:
    for key, val in d.items():
        if value == val:
            return key

def um_even_numbers(numb: List[int]) -> int:
    """принимает список чисел и возвращает сумму всех чётных чисел в этом списке"""
    # total  = 0
    #
    # for i in numb:
    #     if i % 2 == 0:
    #         total += i
    # return total
    return sum(i for i in numb if i%2 == 0)

def find_longest_word(words: List[str]) -> Optional[str]:
    if not words:
        return None

    max_words = words[0]
    for w in words:
        if len(w) > len(max_words):
            max_words = w
    return max_words

def remove_duplicates(list_numb: List[int]) -> List[int]:
    """принимает список целых чисел и возвращает новый список, в котором все элементы уникальны"""
    no_dibl = []
    for n in list_numb:
        if n not in no_dibl:
            no_dibl.append(n)
    return no_dibl

def list_fromkeys_dict(list_nums: List[int]) -> List[int]:
    return list(dict.fromkeys(list_nums))

def merge_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    """Объединяет два списка в один, удаляя дубликаты и сохраняя порядок."""
    return list(dict.fromkeys(list_a + list_b))

def enum_list(words: List[str]) ->  List[str]:
    """Принимает список и нумерует его значения"""
    # enum_ls = []
    # for i, l in enumerate(ls, start=1):
    #     enum_ls.append(f'{i}. {l}')
    # return enum_ls
    return [f'{i}. {word}' for i, word in enumerate(words, start=1)]

def find_long_words_indexes(words: List[str], n: int) -> List[int]:
    """вернёт список индексов тех слов, у которых длина строго больше N"""
    return [i for i, word in enumerate(words) if len(word) > n]

def double_numbers(nums: List[int]) -> List[int]:
    """Удваивает каждый элемент списка с помощью map и lambda."""
    return list(map(lambda n: n*2, nums))

def filter_even(nums: List[int]) -> List[int]:
    """оставляет только чётные числа"""
    return list(filter(lambda n: n % 2 == 0, nums))

def odd_squares(nums: List[int]) -> List[int]:
    """Оставляет только нечётные (n % 2 != 0)
        Возводит каждый в квадрат"""
    return list(map(lambda n: n**2, filter(lambda n: n%2!=0, nums)))

def best_student(names: List[str], scores: List[int]) -> Tuple[int, str, int]:
    """
    Возвращает индекс, имя и балл студента с максимальным баллом.
    """
    # Объединяем имена и оценки с индексами
    best = max(
        enumerate(zip(names, scores)),
        key=lambda x: x[1][1]  # сравниваем по баллам

    )

    print(best)

    index = best[0]      # индекс в списке
    name = best[1][0]    # имя
    score = best[1][1]   # балл

    return index, name, score

def re_gular():
    pattern = r'([А-ЯЁа-яё]+).*?(?:\+7|8|7)[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})'
    with open('phon_i_hueta.txt', 'r', encoding='utf-8') as infile, \
        open('new_phone.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            mathc = re.search(pattern, line)
            if mathc:
                name, code, code_city, num_1, num_2 = mathc.groups()
                normalized = f'{name}: +7({code})-{code_city}-{num_1}-{num_2}\n'
                outfile.writelines(normalized)









if __name__ == '__main__':

    re_gular()

    # print(best_student(['Аня', 'Боря', 'Вика', 'Гриша'], [80, 95, 88, 70]))
    # print(stringt_to_dict('hello'))
    # print(invert_dict(stringt_to_dict('hello')))
    # print(find_key_by_value({'a': 1, 'b': 2, 'c': 3}, 4))
    # print(um_even_numbers([2, 4, 6, 8]))
    # print(find_longest_word(["кусь", "пердолить", "стикер", 'dfdvdsvsdvdsvdsvdsv']))
    # print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    # print(list_fromkeys_dict([1, 2, 2, 3, 1, 4]))
    # print(merge_lists([1, 2, 3, 4], [3, 4, 5, 6]))
    # print(enum_list(['sun', 'moon', 'star']))
    # print(find_long_words_indexes(['cat', 'dinosaur', 'ox', 'hippopotamus', 'dog'], 3))
    # print(double_numbers([1, 2, 3, 4, 5]))
    # print(filter_even([1, 2, 3, 4, 5, 6]))
    # print(odd_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

