n = int(input("Введите количество монет: "))
sides = input("Введите стороны монет (равные количеству указанных монет) подряд, где 1 - решка и 0 - орел (например: 101101): ")

top = sides.count('1')
bottom = sides.count('0')

flips = min(top, bottom)
print("Минимальное количество монет, которые нужно перевернуть:", flips)
