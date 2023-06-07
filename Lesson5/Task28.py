def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a - 1, b + 1)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum(a, b)
print(f"Сумма чисел {a} и {b} равна {result}")
