# урок 3 задание 7
from memory_profiler import profile
from random import randint

a = []

n = int(input("Введите длину исходного списка: "))
for i in range(n):
    a.append(randint(0, 100))

print(*a)

min1 = 101
min2 = 101


@profile
def func(b, m1, m2, k):
    for j in range(k):
        if b[j] < m1:
            m2 = m1
            m1 = b[j]
        elif b[j] < m2:
            m2 = b[j]
    print(f"Первый минимум списка: {m1}, второй минимум: {m2}")


func(a, min1, min2, n)

# Объем используемой памяти = 16.7, и так же, как в предыдущем примере с увеличением длины исходного списка возрастает
# крайне незначительно
