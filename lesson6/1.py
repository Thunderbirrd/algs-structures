# урок 2 задание 3, рекурсия
from memory_profiler import profile

number = int(input("Ведите число: "))
number2 = ""


@profile
def reverse(num, num2):
    if num > 0:
        last = num % 10
        num2 += str(last)
        reverse(num // 10, num2)
    else:
        print(f"Перевернутое число - {num2}")


reverse(number, number2)

# Результат: memory-usage = 16.3, инкременты отсутвуют, т.к программа не сохраняет какие-либо большие обЬекты
