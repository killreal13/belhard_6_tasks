"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n: int, current: int = 0, result: int = 1) -> int:
    if result < n:
        fibonacci(n, current=result, result=result + current)
    else:
        print(result)