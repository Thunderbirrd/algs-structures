n = int(input("Введите длину ряда: "))
summ = 1
first = 1
for _ in range(n - 1):
    first /= -2
    summ += first

print(f"Сумма ряда из {n} чисел = {summ}")
