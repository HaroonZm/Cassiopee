while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a <= b:
        a, b = b, a
    d = 1
    while True:
        c = a % b
        if c == 0:
            break
        a, b = b, c
        d += 1
    print(b, d)