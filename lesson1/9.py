a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# все три числа различны

if a > b:
    if a < c:
        print(f"Среднее число - {a}")
    elif c > b:
        print(f"Среднее число - {c}")
    elif c < b:
        print(f"Среднее число - {b}")
elif b > a:
    if b < c:
        print(f"Среднее число - {b}")
    elif c > a:
        print(f"Среднее число - {c}")
    elif c < a:
        print(f"Среднее число - {a}")
