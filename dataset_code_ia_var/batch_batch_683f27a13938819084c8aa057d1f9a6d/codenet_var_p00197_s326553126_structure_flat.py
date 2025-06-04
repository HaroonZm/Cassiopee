while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a >= b:
        x = a
        y = b
    else:
        x = b
        y = a
    s = 0
    while True:
        t = x % y
        x = y
        y = t
        s = s + 1
        if y == 0:
            break
    print(x, s)