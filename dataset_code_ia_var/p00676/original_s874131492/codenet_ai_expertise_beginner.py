import math

while True:
    try:
        parts = input().split()
        a = int(parts[0])
        l = int(parts[1])
        x = int(parts[2])
        first = l * math.sqrt(x * (2 * l + x)) / 2
        second = a * math.sqrt(4 * l * l - a * a) / 4
        result = first + second
        print("%.10f" % result)
    except EOFError:
        break