first = int(input("Введите первое число: "))
operation = str(input("Введите операцию: "))
second = int(input("Введите второе число: "))


def calculator(x, o, y):
    if o == "0":
        return
    elif o == "+":
        print(f"Сумма введенных чисел = {x + y}")
    elif o == "-":
        print(f"Разность введенных чисел ={x - y}")
    elif o == "*":
        print(f"Произведение введенных чисел = {x * y}")
    elif o == "/":
        print(f"астное введенных числе = {x / y}")
    else:
        print("Вы ввели недопустимый символ")
    x = int(input("Введите первое число: "))
    o = str(input("Введите операцию: "))
    y = int(input("Введите второе число: "))
    calculator(x, o, y)


calculator(first, operation, second)
print("Работа завершена")
