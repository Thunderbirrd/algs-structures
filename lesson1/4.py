from random import random, choice

b1 = int(input("Минимальная граница: "))
b2 = int(input("Максимальная границп: "))

n = int(random() * (b2 - b1)) + b1
print(n)

b1 = float(input("Минимальная граница: "))
b2 = float(input("Максимальная границп: "))
n = random() * (b2 - b1) + b1
print(round(n, 5))

# возможно, этот способ не очень честный

s = "abcdefjhijklmnopqrstuvwxyz"
b1 = str(input("Минимальная граница: "))
b2 = str(input("Максимальная граница: "))

pos1 = s.index(b1)
pos2 = s.index(b2)

s = s[pos1: pos2 + 1]
n = choice(s)
print(n)
