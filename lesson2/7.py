n = int(input("Введите число, для которого будем проверять равенство"))
part2 = n * (n + 1) / 2
part1 = 0
for i in range(n + 1):
    part1 += i

# part2 = part1 при любых n
