n = int(input("Введите число n: "))

x = 0
result = 1
output = ""

while result <= n:
    output += str(result) + " "
    x += 1
    result = 2 ** x

print(n, "->", output.strip())
