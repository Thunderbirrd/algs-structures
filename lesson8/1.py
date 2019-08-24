import hashlib
string = input("Введите строку из строчных латинских букв: ")
hash_set = set()

length = len(string)
for i in range(length):
    if i == 0:
        length -= 1
    else:
        length = len(string)
    for j in range(length, i, -1):
        hash_set.add(hashlib.sha1(string[i:j].encode("utf-8")).hexdigest())

# print(hash_set)
print(f"Количество подстрок в строке '{string}' равняется - {len(hash_set)}")
