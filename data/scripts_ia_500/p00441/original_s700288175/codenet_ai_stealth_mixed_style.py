while True:
    n = int(input())
    if n == 0:
        break
    P = []
    for _ in range(n):
        parts = input().split()
        x = int(parts[0])
        y = int(parts[1])
        P.append((x, y))
    S = set(P)
    ans = 0
    for i in range(len(P) - 1):
        xi, yi = P[i]
        j = i + 1
        while j < len(P):
            xj, yj = P[j]
            q = (xj - yj + yi, yj + xj - xi)
            r = tuple(map(lambda a, b, c: a - b + c, (xi, yi), (yj, yj), (yi, xi)))
            if q in S and r in S:
                dist_sq = (xi - xj) ** 2 + (yi - yj) ** 2
                ans = ans if ans > dist_sq else dist_sq
            j += 1
    print(ans)