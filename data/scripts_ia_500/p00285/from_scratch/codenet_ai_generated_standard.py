import sys
sys.setrecursionlimit(10**7)

def energy(bm, bw):
    d = abs(bm - bw)
    return d * (d - 30) if d > 30 else 0

def dfs(i, W, M, bw, memo, bm):
    if i == M:
        return 0
    if i in memo:
        return memo[i]
    res = dfs(i + 1, W, M, bw, memo, bm)  # skip pairing
    for j in range(W):
        if not used[j]:
            used[j] = True
            val = energy(bm[i], bw[j]) + dfs(i + 1, W, M, bw, memo, bm)
            used[j] = False
            if val > res:
                res = val
    memo[i] = res
    return res

for line in sys.stdin:
    if line.strip() == '':
        continue
    M, W = map(int, line.split())
    if M == 0 and W == 0:
        break
    bm = list(map(int, sys.stdin.readline().split()))
    bw = list(map(int, sys.stdin.readline().split()))
    used = [False]*W
    memo = {}
    print(dfs(0, W, M, bw, memo, bm))