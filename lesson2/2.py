number = int(input("Ведите число: "))
even = 0
odd = 0
while number > 0:
    last = number % 10
    if last % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10

print(f"Количество чётных - {even}, нечётных - {odd}")
