while True:
    n = input()
    if n == 0: break
    P = [(map(int, raw_input().split())) for i in range(n)]
    S = set(map(tuple, P))
    ans = 0
    for i in range(n - 1):
        xi, yi = P[i]
        for j in range(i + 1, n):
            xj, yj = P[j]
            q = (xj - yj + yi, yj + xj - xi)
            r = (xi - yj + yi, yi + xj - xi)
            if q in S and r in S:
                ans = max(ans, (xi - xj) ** 2 + (yi - yj) ** 2)
    print ans