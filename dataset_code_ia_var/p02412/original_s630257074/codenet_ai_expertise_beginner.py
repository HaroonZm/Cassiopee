while True:
    k = raw_input().split(" ")
    k0 = int(k[0])
    k1 = int(k[1])
    if k0 == 0 and k1 == 0:
        break
    ct = 0
    max_val = k0
    total = k1
    a = max_val + 1

    while True:
        a = a - 1
        b = a - 1
        c = total - a - b
        if not a > c:
            print ct
            break
        while b > c:
            if c > 0:
                ct = ct + 1
            b = b - 1
            c = c + 1