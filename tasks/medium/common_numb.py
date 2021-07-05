"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""
from typing import Optional


def common_numbers(list_1: Optional[list], list_2: Optional[list], common_list: list = []) -> list:
    for i in range(len(list_1)):
        if list_1[i] in list_2:
            common_list.append(list_1[i])
    else:
        return sorted(common_list, reverse=True)
