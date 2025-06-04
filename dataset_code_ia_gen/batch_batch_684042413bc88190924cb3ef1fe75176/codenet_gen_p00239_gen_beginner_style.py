while True:
    n = int(input())
    if n == 0:
        break
    snacks = []
    for _ in range(n):
        data = input().split()
        s = int(data[0])
        p = int(data[1])
        q = int(data[2])
        r = int(data[3])
        snacks.append((s, p, q, r))
    limits = input().split()
    P = int(limits[0])
    Q = int(limits[1])
    R = int(limits[2])
    C = int(limits[3])

    result = []
    for s, p, q, r in snacks:
        cal = 4 * p + 9 * q + 4 * r
        if p <= P and q <= Q and r <= R and cal <= C:
            result.append(str(s))
    if len(result) == 0:
        print("NA")
    else:
        for s in result:
            print(s)