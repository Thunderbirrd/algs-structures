from random import randint


def bubble_sort(a):
    n = 1
    length = len(a)
    while n < length:
        count = 0
        for i in range(length - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
        if count == 0:
            return a
        n += 1
    return a


m = int(input("Введите длину исходного списка: "))
orig_list = []
for j in range(m):
    orig_list.append(randint(-100, 100))

print("Исходный список:",  *orig_list)
print("Отсортированный список: ", *bubble_sort(orig_list))
