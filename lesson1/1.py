number = int(input("Введите трёхзначное число: "))
s = 0
composition = 1
s += number % 10
composition *= number % 10
number //= 10
s += number % 10
composition *= number % 10
number //= 10
s += number % 10
composition *= number % 10

print(f"Сумма цифр равна: {s}")
print(f"Протзведение цифр равно {composition}")
