while True:
    a = 0
    b = 0
    n = int(input())
    if n == 0:
        break
    i = 0
    while i < n:
        values = input().split()
        c = int(values[0])
        d = int(values[1])
        if c > d:
            a = a + c + d
        elif c < d:
            b = b + c + d
        else:
            a = a + c
            b = b + d
        i = i + 1
    print(a, b)