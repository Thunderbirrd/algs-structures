l1 = int(input("Введите длину первой стороны: "))
l2 = int(input("Введите длину второй стороны: "))
l3 = int(input("Введите длину третьей стороны: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f"Треугогльник со сторонами: {l1}, {l2}, {l3}, существует")
    if l1 == l2 == l3:
        print("Данный треугольник - равносторонний")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Данный треугольник - равнобедренный")
    else:
        print("Данный треугольник - разносторонний")
else:
    print(f"Треугогльник со сторонами: {l1}, {l2}, {l3}, не существует")
