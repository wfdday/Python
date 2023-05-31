def find_closest_element(array, x):
    closest_element = array[0]
    closest_difference = (x - closest_element)

    for num in array:
        difference = (x - num)
        if difference < closest_difference:
            closest_element = num
            closest_difference = difference

    return closest_element


n = int(input("Введите количество элементов в массиве: "))
array = []
for _ in range(n):
    num = int(input("Введите число: "))
    array.append(num)
x = int(input("Введите число X: "))

closest = find_closest_element(array, x)
print("Самый близкий элемент к числу", x, "в массиве:", closest)
