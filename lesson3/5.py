from random import randint

a = []

n = int(input("Введите длину исходного списка: "))
for i in range(n):
    a.append(randint(-100, 100))

print(*a)

number = -101

for i in range(n):
    if a[i] < 0:
        if a[i] > number:
            number = a[i]
            max_index = i

print(f"Максимальный отрицатьный элемент в исходном списке: {number}, его позиция: {max_index}")
