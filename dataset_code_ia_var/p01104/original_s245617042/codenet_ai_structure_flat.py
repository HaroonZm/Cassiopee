while 1:
    n, m = map(int, input().split())
    if n+m == 0:
        break
    B = []
    for i in range(n):
        B.append(int(input(), 2))
    C = {0: 0}
    i = 0
    while i < len(B):
        b = B[i]
        D = []
        for k in C:
            D.append((k, C[k]))
        j = 0
        while j < len(D):
            k, v = D[j]
            if (k^b) in C:
                if C[k^b] < v+1:
                    C[k^b] = v+1
            else:
                C[k^b] = v+1
            j += 1
        i += 1
    print(C[0])