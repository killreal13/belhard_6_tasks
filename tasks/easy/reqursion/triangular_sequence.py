"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequance(n: int, pattern=1) -> int:
    if pattern <= n:
        print(str(pattern) * pattern)
        triangular_sequance(n, pattern=pattern+1)