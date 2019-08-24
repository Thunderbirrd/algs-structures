# урок 2 задание 3, цикл
from memory_profiler import profile


number = int(input("Ведите число: "))
number2 = ""


@profile
def func(num, num2):
    while num > 0:
        last = num % 10
        num2 += str(last)
        num //= 10
    return num2


print(f"Перевернутое число - {func(number, number2)}")

# Результат такой же, как у рекрсии, т.к все переменные в двух вариантах программы - идентичны
# Python 3.6, windows 64-bit
