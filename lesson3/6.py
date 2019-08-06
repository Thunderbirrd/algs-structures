from random import randint

a = []

n = int(input("Введите длину исходного списка: "))
for i in range(n):
    a.append(randint(0, 100))

print(*a)

maximum = -1
minimum = 101

for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        max_index = i
    if a[i] < minimum:
        minimum = a[i]
        min_index = i

el_sum = 0
if max_index > min_index:
    for i in range(min_index + 1, max_index):
        el_sum += a[i]
elif min_index > max_index:
    for i in range(max_index + 1, min_index):
        el_sum += a[i]
else:
    print("Все элементы массива одинаковы")
    quit()

print(f"Сумма элементов между максимальным и минимальным элементами списка равна: {el_sum}")
