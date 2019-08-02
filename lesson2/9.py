first = int(input("Ведите первое число: "))
second = int(input("Введите второе число: "))


def figures(x):
    if x >= 10:
        return x % 10 + figures(x // 10)
    else:
        return x % 10


sum1 = figures(first)
sum2 = figures(second)

if sum1 > sum2:
    print(f"Наибольшая сумма цифр у числа {first}, равна {sum1}")
elif sum1 < sum2:
    print(f"Наибольшая сумма цифр у числа {second}, равна {sum2}")
else:
    print(f"Сумма цифр у чисел {first} и {second} равны и составляют {sum1}")
