from random import randint

a = []
b = []

n = int(input("Введите длину первого списка: "))
for i in range(n):
    a.append(randint(1, 100))

print(*a)

for i in range(n):
    if a[i] % 2 == 0:
        b.append(i)

print(*b)
