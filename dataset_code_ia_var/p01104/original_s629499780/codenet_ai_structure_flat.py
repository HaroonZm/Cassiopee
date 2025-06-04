while 1:
    n, m = map(int, input().split())
    if n + m == 0:
        break
    C = {0: 0}
    i = 0
    while i < n:
        b = int(input(), 2)
        tmpC = dict(C)
        for k in tmpC:
            v = tmpC[k]
            x = k ^ b
            if x not in C or C[x] < v + 1:
                C[x] = v + 1
        i += 1
    print(C[0])