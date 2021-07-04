"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n: int, current: int = 1, result: int = 1):
    if current <= n:
        factorial(n, current + 1, result * current)
    else:
        print(result)
        return result

print(factorial(4))
