import math

while True:
    try:
        a = input()
        a = float(a)
        t = a / 9.8
        y = 4.9 * (t ** 2)
        n = math.ceil((y + 5) / 5)
        print(n)
    except EOFError:
        break