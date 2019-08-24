n = int(input("Введите число, для которого будем проверять равенство: "))
part2 = n * (n + 1) / 2
part1 = 0
for i in range(n + 1):
    part1 += i

if part2 == part1:
    print(f"{part1} = {part2} при n = {n}")
else:
    print("Вы сломали математику")
