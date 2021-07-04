"""
Написать функцию get_even_number, которая принимает 1 аргумент - номер
четного числа и возвращает само четное число

Например:

- get_even_number(10) -> 20
- get_even_number(3) -> 6
"""
from typing import Optional


def get_even_number(num: Optional[int]) -> int:
    return num * 2


get_even_number_2 = lambda num: num * 2
