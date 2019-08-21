from random import randint

m = int(input("Введите m: "))
a = []
length = 2 * m + 1
for i in range(length):
    a.append(randint(0, 100))
print("Исходный список: ", *a)
for i in range(length):
    bigger = 0
    smaller = 0
    equal = 0
    for j in range(length):
        if i == j:
            continue
        if a[j] > a[i]:
            bigger += 1
        elif a[j] < a[i]:
            smaller += 1
        else:
            equal += 1
    if equal == 0:
        if smaller == m and bigger == m:
            middle = a[i]
            break
    else:
        if smaller > m or bigger > m:
            continue
        else:
            middle = a[i]
            break

print(*sorted(a))
print(f"Медина списка - {middle}")
