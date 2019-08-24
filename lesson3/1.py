a = []
for i in range(2, 10):
    a.append(0)  # a[0] - кратные 2(кол-во), a[1] - кратные 3 итд
b = []
for i in range(2, 100):
    b.append(i)
for i in range(2, 100):
    for j in range(2, 10):
        if b[i - 2] % j == 0:
            a[j - 2] += 1

for i in range(len(a)):
    print(f"{a[i]} чисел кратны {i + 2}")
