g = 9.8
l = 4.9

while True:
    try:
        v = float(raw_input())
        t = v / g
        y = l * (t ** 2)
        n = y / 5 + 2
        print int(n)
    except EOFError:
        break