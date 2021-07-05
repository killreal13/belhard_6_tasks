"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
from typing import Optional


def yes_or_no(list_1: Optional[list]) -> str:
    if len(list_1) > len(set(list_1)):
        print('Yes')
    else:
        print('No')
