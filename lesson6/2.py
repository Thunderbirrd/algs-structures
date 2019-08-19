# урок 3 задание 2
from memory_profiler import profile
from random import randint

a = []
b = []

n = int(input("Введите длину первого списка: "))
for i in range(n):
    a.append(randint(1, 100))

print(*a)

@profile
def func(a, b, n):
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(i)
    return b


print(*func(a, b, n))

# Программа практически не уеличивает объём используемой памяти, в зависимости от количество элементов в исходном списке
# При колистве элементов от 1 до 700(примерно) memory-usage = 16.7, далее начинает незначительно возрастать.
