while 1:
    n, m, h, k = [int(x) for x in input().split()]
    if n == 0:
        break
    A = []
    B = [[] for _ in range(h)]
    C = list(range(n))
    S = [0 for _ in range(n)]
    X = []
    for _ in range(n):
        A.append(int(input()))
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        B[b].append(a)
    for y in range(h):
        for a in B[y]:
            C[a-1:a+1] = [C[a], C[a-1]]
            X.append(sorted(C[a-1:a+1]))
    for i in range(n):
        S[C[i]] = A[i]
    ans = sum(S[:k])
    tmpdif = 0
    for xx in X:
        if xx[0] < k and xx[1] >= k:
            tmpdif = min(tmpdif, S[xx[1]] - S[xx[0]])
    print(ans + tmpdif)