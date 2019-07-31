s = "abcdefjhijklmnopqrstuvwxyz"

l1 = input("Введите первую букву: ")
l2 = input("Введите вторую букву: ")
pos1 = s.index(l1) + 1
pos2 = s.index(l2) + 1

print(f"{l1} является {pos1} буквой алфавита")
print(f"{l2} является {pos2} буквой алфавита")
dist = abs(pos1 - pos2) - 1
print(f"Букв между ними: {dist}")
