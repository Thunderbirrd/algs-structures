n = int(input("Введите номер простого числа: "))
i = 0
number = 3
if n == 1:
    print(f"{n} - ое простое число: 2")
elif n == 2:
    print(f"{n} - ое простое число: 3")
else:
    while i < n:
        k = 2
        q = 0
        while k < number / 2:
            if number % k == 0:
                q += 1
                break
            k += 1
        if q == 0:
            i += 1
        number += 1

print(f"{n} - ое простое число: {number - 1}")
