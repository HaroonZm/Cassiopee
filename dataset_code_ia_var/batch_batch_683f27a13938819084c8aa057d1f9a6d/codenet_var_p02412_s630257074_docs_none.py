while True:
    k = list(map(int, input().split()))
    if k[0] == k[1] == 0:
        break
    ct = 0
    max_val = k[0]
    total = k[1]
    a = max_val + 1
    while True:
        a -= 1
        b = a - 1
        c = total - a - b
        if not a > c:
            print(ct)
            break
        while b > c:
            if c > 0:
                ct += 1
            b -= 1
            c += 1