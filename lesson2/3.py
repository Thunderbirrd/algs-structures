number = int(input("Ведите число: "))
number2 = ""

while number > 0:
    last = number % 10
    number2 += str(last)
    number //= 10

print(f"Перевернутое число - {number2}")
