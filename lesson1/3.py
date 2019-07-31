x1, y1 = input().split()
x2, y2 = input().split()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

k = (y1 - y2) / (x1 - x2)
b = y1 - x1 * k
if k != 0 and k != 1 and b != 0:
    print(f"Прямая имеет вид: y = {k}x + {b}")
elif b == 0:
    if k == 0:
        print(f"Прямая имеет вид: y = 0")
    elif k == 1:
        print(f"Прямая имеет вид: y = x")
    else:
        print(f"Прямая имеет вид: y = {k}x")
elif k == 0:
    print(f"Прямая имеет вид: y = {b}")
elif k == 1:
    print(f"Прямая имеет вид: y = x + {b}")
