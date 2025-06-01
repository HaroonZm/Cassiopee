def translate(x):
    return translate(x // 4) + str(x % 4) if x >= 4 else str(x)

while (n := int(input())) != -1:
    print(translate(n))