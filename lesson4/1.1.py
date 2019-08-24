# lesson2 задание 2 рекурсия
from timeit import timeit
number = 1234
even_out = 0
odd_out = 0


def odd_even(x, even, odd):
    if x == 0:
        print(f"Количество чётных - {even}, нечётных - {odd}")
        return
    else:
        last = x % 10
        if last % 2 == 0:
            even += 1
        else:
            odd += 1
        odd_even(x // 10, even, odd)


# odd_even(number, even_out, odd_out)

print(timeit("odd_even(number, even_out, odd_out)", setup="from __main__ import odd_even, number, even_out, odd_out",
             number=1000))

# Результат: время примерно равно: 0.02 сек. сложность алгоритма О(len(n)) т.е чем больше цифр в введённом числе,
# тем больше операций
