while True:
    n = int(input())
    if n == 0:
        break
    i = 0
    while i < n:
        vals = input().split()
        x1 = int(vals[0])
        y1 = int(vals[1])
        z1 = int(vals[2])
        w1 = int(vals[3])
        x2 = int(vals[4])
        y2 = int(vals[5])
        z2 = int(vals[6])
        w2 = int(vals[7])
        a = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
        b = x1 * y2 + x2 * y1 + z1 * w2 - z2 * w1
        c = x1 * z2 - y1 * w2 + x2 * z1 + y2 * w1
        d = x1 * w2 + y1 * z2 - y2 * z1 + x2 * w1
        print(a, b, c, d)
        i += 1