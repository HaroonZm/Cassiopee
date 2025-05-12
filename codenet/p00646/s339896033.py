while True:
    L = input()
    if L == 0:
        break
    n = 2
    ans = 1
    while n * n <= L:
        if L % n == 0:
            S = 0
            while L % n == 0:
                L /= n
                S += 1
            ans *= S * 2 + 1
        n += 1

    if L != 1:
        ans *= 3

    print ans / 2 + 1