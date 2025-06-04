def calc(x1, y1, x2, y2):
    return S[y2-1][x2-1] - S[y1-1][x2-1] - S[y2-1][x1-1] + S[y1-1][x1-1]

INF = 10**18
def dfs(x1, y1, x2, y2):
    key = (x1, y1, x2, y2)
    if key in memo:
        return memo[key]
    val = calc(x1, y1, x2, y2)
    if val < rest:
        memo[key] = (0, -1)
        return (0, -1)
    res = (1, val)
    for i in range(x1+1, x2):
        k1, r1 = dfs(x1, y1, i, y2)
        k2, r2 = dfs(i, y1, x2, y2)
        if r1 >= 0 and r2 >= 0:
            res = max(res, (k1+k2, min(r1, r2)))
    for i in range(y1+1, y2):
        k1, r1 = dfs(x1, y1, x2, i)
        k2, r2 = dfs(x1, i, x2, y2)
        if r1 >= 0 and r2 >= 0:
            res = max(res, (k1+k2, min(r1, r2)))
    memo[key] = res
    return res

while True:
    h, w, s = map(int, input().split())
    if h == 0:
        break
    U = [list(map(int, input().split())) for _ in range(h)]
    S = [[0]*(w+1) for _ in range(h+1)]
    su = sum(sum(e) for e in U)
    rest = su-s
    memo = {}
    for i in range(h):
        tmp = 0
        for j in range(w):
            tmp += U[i][j]
            S[i][j] = S[i-1][j] + tmp
    k, r = dfs(0, 0, w, h)
    print(k, r - rest)