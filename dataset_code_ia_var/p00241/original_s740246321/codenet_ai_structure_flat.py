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
        x3 = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
        y3 = x1 * y2 + y1 * x2 + z1 * w2 - w1 * z2
        z3 = x1 * z2 - y1 * w2 + z1 * x2 + w1 * y2
        w3 = x1 * w2 + y1 * z2 - z1 * y2 + w1 * x2
        print(x3, y3, z3, w3)
        i += 1