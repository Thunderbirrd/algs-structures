number = int(input("Ведите число: "))
even_out = 0
odd_out = 0


def odd_even(x, even, odd):
    if x == 0:
        print(f"Количество чётных - {even}, нечётных - {odd}")
        return
    else:
        last = x % 10
        if last % 2 == 0:
            even += 1
        else:
            odd += 1
        odd_even(x // 10, even, odd)


odd_even(number, even_out, odd_out)
