def power(A, B):
    if B == 0:
        return 1
    elif B < 0:
        return 1 / power(A, -B)
    elif B % 2 == 0:
        half_power = power(A, B // 2)
        return half_power * half_power
    else:
        return A * power(A, B - 1)


A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)
print(f"{A} в степени {B} равно {result}")
