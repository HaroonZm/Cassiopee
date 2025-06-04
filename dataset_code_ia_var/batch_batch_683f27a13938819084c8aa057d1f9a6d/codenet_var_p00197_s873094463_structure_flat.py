while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a < b:
        temp = a
        a = b
        b = temp
    C = 0
    while True:
        a = a % b
        temp = a
        a = b
        b = temp
        C = C + 1
        if b == 0:
            break
    print(a, C)