line = 5
column = 4
a = []
for i in range(column):
    z = []
    for j in range(line):
        n = int(input())
        z.append(n)
    a.append(z)

for i in range(column):
    for j in range(line):
        print("%4d" % a[i][j], end="")
    print()
print()

min_el = [1000, 1000, 1000, 1000, 1000]

for i in range(line):
    for j in range(column):
        if a[j][i] < min_el[i]:
            min_el[i] = a[j][i]
print(*min_el)

maximum = -1
for i in range(line):
    if min_el[i] > maximum:
        maximum = min_el[i]
        max_column = i + 1

print(f"Максимальный среди минимальных элемнтов: {maximum}, находится в {max_column} столбце")
