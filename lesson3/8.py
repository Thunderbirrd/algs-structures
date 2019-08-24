line = 5
column = 4
a = []
for i in range(column):
    z = []
    el_sum = 0
    for j in range(line):
        if j == 4:
            n = el_sum
        else:
            n = int(input())
            el_sum += n
        z.append(n)
    a.append(z)

for i in range(column):
    for j in range(line):
        print("%4d" % a[i][j], end="")
    print()
print()
