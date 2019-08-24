from random import randint

number = randint(0, 100)

user_number = int(input("Введите число: "))
for i in range(10):
    if user_number == number:
        print("Поздравляем! Выугадали число")
        quit()
    elif user_number < number:
        print(f"Ваше число меньше загаданного, поробуйте ещё раз, у вас осталось {9 - i} попыток")
        user_number = int(input("Введите новое число: "))
    else:
        print(f"Ваше число больше загаданного, попробуйте ещё раз, у вас осталось {9 - i} попыток")
        user_number = int(input("Введите новое число: "))

print("У вас закончились попытки")
