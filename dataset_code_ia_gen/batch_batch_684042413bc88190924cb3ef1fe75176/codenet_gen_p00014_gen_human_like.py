while True:
    try:
        d = int(input())
        s = 0
        for x in range(d, 600, d):
            s += d * (x ** 2)
        print(s)
    except EOFError:
        break