while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a < b:
        a, b = b, a
    C = 0
    while True:
        a = a % b
        a, b = b, a
        C = C + 1
        if b == 0:
            break
    print(a, C)