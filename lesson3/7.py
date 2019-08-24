from random import randint

a = []

n = int(input("Введите длину исходного списка: "))
for i in range(n):
    a.append(randint(0, 100))

print(*a)

min1 = 101
min2 = 101

for i in range(n):
    if a[i] < min1:
        min2 = min1
        min1 = a[i]
    elif a[i] < min2:
        min2 = a[i]

print(f"Первый минимум списка: {min1}, второй минимум: {min2}")
