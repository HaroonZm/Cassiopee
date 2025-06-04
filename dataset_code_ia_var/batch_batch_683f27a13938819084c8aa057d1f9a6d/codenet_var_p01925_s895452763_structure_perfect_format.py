import sys

def solve(n, m, s, k, c):
    maxvs = [0] * (n + 1)
    minvs = [0] * (n + 1)
    for idx, members in enumerate(c):
        for j in members:
            maxvs[j] += s[idx]
            if k[idx] == 1:
                minvs[j] += s[idx]
    ans = -1
    for i in range(1, n + 1):
        minval = min(minvs[1:i] + minvs[i + 1:])
        diff = maxvs[i] - minval
        ans = max(ans, diff)
    print(ans + 1)

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S = []
    K = []
    C = []
    for _ in range(M):
        Skc = list(map(int, input().split()))
        S.append(Skc[0])
        K.append(Skc[1])
        C.append(Skc[2:])
    solve(N, M, S, K, C)