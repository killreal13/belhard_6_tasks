"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""
from typing import Optional


def reverse_dict(dict_1: Optional[dict]) -> dict:
    print(dict_1.fromkeys(dict_1.values(), dict_1.keys()))
    return dict_1.fromkeys(dict_1.values(), dict_1.keys())


reverse_dict({1: "kek", 2: "rofl"})