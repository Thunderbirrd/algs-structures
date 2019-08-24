number = int(input("Ведите число: "))
number2 = ""


def reverse(num, num2):
    if num > 0:
        last = num % 10
        num2 += str(last)
        reverse(num // 10, num2)
    else:
        print(f"Перевернутое число - {num2}")


reverse(number, number2)
