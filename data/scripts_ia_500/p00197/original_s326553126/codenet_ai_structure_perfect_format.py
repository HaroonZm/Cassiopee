while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        if a >= b:
            x = a
            y = b
        else:
            x = b
            y = a
        s = 0
        while True:
            x = x % y
            x, y = y, x
            s += 1
            if y == 0:
                break
        print(x, s)