from random import randint

a = []
maximum = -1
minimum = 101

n = int(input("Введи длину списка: "))
for i in range(n):
    a.append(randint(0, 100))

print("Исходный список: ", *a)

for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        max_index = i
    elif a[i] < minimum:
        minimum = a[i]
        min_index = i

k = a[max_index]
a[max_index] = a[min_index]
a[min_index] = k

print("Изменённый списко: ", *a)

