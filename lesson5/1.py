from collections import namedtuple
n = int(input("Введите количество предприятий: "))
a = []
b = []
for i in range(n):
    res = namedtuple(input("Введите название предприятия: "), 'one two three four ')
    a.append(0)
    a[i] = res(
        one=input("Первый квартал: "),
        two=input("Второй квартал: "),
        three=input("Третий квартал: "),
        four=input("Четвёртый квартал: "),
    )
    b.append(int(a[i][0]) + int(a[i][1]) + int(a[i][2]) + int(a[i][3]))
average = sum(b) / n
for i in range(n):
    if b[i] < average:
        print(f"Прибыль предприятия {a[i]} меньше средней")
for i in range(n):
    if b[i] > average:
        print(f"Прибыль предприятия {a[i]} больше средней")
