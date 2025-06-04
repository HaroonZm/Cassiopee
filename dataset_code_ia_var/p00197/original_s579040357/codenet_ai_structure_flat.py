while True:
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    if a == 0 and b == 0:
        break
    if a <= b:
        tmp = a
        a = b
        b = tmp
    d = 1
    while True:
        c = a % b
        if c == 0:
            break
        if c != 0:
            t = a
            a = b
            b = c
            d = d + 1
    print(b, d)