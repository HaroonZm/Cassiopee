def translate(x):
    if int(x/4):
        return translate(int(x/4)) + str(x % 4)
    return str(x % 4)

while 1:
    n = int(input())
    if n == -1:
        break

    n4 = translate(n)
    print(n4)