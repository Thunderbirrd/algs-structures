first = int(input("Введите первое число: "))
operation = str(input("Введите операцию: "))
second = int(input("Введите второе число: "))
while operation != "0":
    if operation == "+":
        print(f"Сумма введенных чисел = {first + second}")
    elif operation == "-":
        print(f"Разность введенных чисел ={first - second}")
    elif operation == "*":
        print(f"Произведение введенных чисел = {first * second}")
    elif operation == "/":
        print(f"астное введенных числе = {first / second}")
    else:
        print("Вы ввели недопустимый символ")
    first = int(input("Введите первое число: "))
    operation = str(input("Введите операцию: "))
    second = int(input("Введите второе число: "))

print("Работа завершена")
