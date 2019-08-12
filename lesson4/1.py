# lesson2 задание 2 цикл
from timeit import timeit

number = 1234
even = 0
odd = 0


def f(n, e, o):
    while n > 0:
        last = n % 10
        if last % 2 == 0:
            e += 1
        else:
            o += 1
        n //= 10

# print(f"Количество чётных - {even}, нечётных - {odd}")


print(timeit("f(number, even, odd)", setup="from __main__ import f, number, even, odd", number=1000))

# Результат: время прирно равно: 0.0011 секунд => алгоритм с циклом работает быстрее, чем рекурсивный, однако сложность
# алгоритма не меняется: она всё так же зависит от количества разрядов в исходном числе
