from random import random


def merger_sort(a):
    length = len(a)
    if length > 1:
        center = length // 2
        left = a[:center]
        right = a[center:]

        merger_sort(left)
        merger_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        return a


n = int(input("Введите длину исходного списка: "))
orig_list = []
for _ in range(n):
    orig_list.append(random() * 50)
print("Исходный список:",  *orig_list)
print("Отсортированный список: ", *merger_sort(orig_list))
