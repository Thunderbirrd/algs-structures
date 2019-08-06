a = []
b = []

n = int(input("Введите длину исходного списка: "))
for i in range(n):
    a.append(int(input()))

print(*a)

for i in range(100):
    b.append(0)

for i in range(n):
    for j in range(100):
        if a[i] == j:
            b[j] += 1

k = 0

for i in range(100):
    if b[i] > k:
        k = b[i]
        ind = i

print(f"Чаще всего в исходном списе встречалось число {ind}, а именно: {k} раз")
