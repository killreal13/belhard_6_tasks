"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
from typing import Optional
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(new_string: Optional[str]) -> dict:
    new_string = new_string.replace(' ', '')
    dict_1 = {key: new_string.count(key) for key in new_string}
    return dict_1


dict_from_str(STR_VAL)

