while True:
    n = int(input())
    if n == 0:
        break
    c = [1] * (2 * n + 1)
    for i in range(1, n + 1):
        x = int(input())
        c[x] = 0
    m0 = n
    m1 = n
    t = 0
    ba = 0
    while m0 > 0 and m1 > 0:
        f = 1
        for i in range(ba + 1, 2 * n + 1):
            if t == c[i]:
                ba = i
                c[i] = 2
                if t == 0:
                    m0 -= 1
                else:
                    m1 -= 1
                f = 0
                break
            if i == 2 * n:
                ba = 0
        if f == 1:
            ba = 0
        t = 1 - t
    print(m1)
    print(m0)