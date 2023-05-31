def count_vol(array, x):
    count = 0
    for num in array:
        if num == x:
            count += 1
    return count


n = int(input("Введите количество элементов в массиве: "))
array = []
for _ in range(n):
    num = int(input("Введите число: "))
    array.append(num)
x = int(input("Введите число X: "))

vol = count_vol(array, x)
print("Число", x, "встречается", vol, "раз(а) в массиве.")
