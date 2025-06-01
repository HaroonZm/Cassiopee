while True:
    L = int(input())
    if not L > 0:
        break
    a = 0
    t = 0
    i = 0
    while i < 12:
        k = list(map(int, input().split()))
        t += k[0] - k[1]
        if L <= t:
            a += 1
        i += 1
    print((12 - a + 1) if a else "NA")