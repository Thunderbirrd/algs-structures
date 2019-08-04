from random import randint

number = randint(0, 100)


def guess_number(x, j=0):
    if j == 10:
        print("У вас закончиличь попытки")
        print("Введите 1, если хотите чыграть ещё раз, или любую другую цифру для завершиния")
        if int(input()) == 1:
            guess_number(randint(0, 100), j=0)
        else:
            return
    user_number = int(input("Введите число: "))
    if user_number == x:
        print("Поздравляем! Выугадали число")
        print("Введите 1, если хотите чыграть ещё раз, или любую другую цифру для завершиния")
        if int(input()) == 1:
            guess_number(randint(0, 100), j=0)
        else:
            print("Спасибо за игру")
            return
    elif user_number < x:
        print(f"Ваше число меньше загаданного, у вас осталось {9 - j} попыток")
        guess_number(x, j=j+1)
    else:
        print(f"Ваше число больше загаданного, у вас осталось {9 - j} попыток")
        guess_number(x, j=+1)


guess_number(number)
