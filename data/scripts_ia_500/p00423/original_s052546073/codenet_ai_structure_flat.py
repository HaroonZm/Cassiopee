while True:
    n = int(input())
    if n == 0:
        break
    a = 0
    b = 0
    i = 0
    while i < n:
        c, d = map(int, input().split())
        if c > d:
            a = a + c + d
        elif c < d:
            b = b + c + d
        else:
            a = a + c
            b = b + d
        i = i + 1
    print(a, b)