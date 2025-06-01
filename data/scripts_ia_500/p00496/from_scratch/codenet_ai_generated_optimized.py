import sys
input = sys.stdin.readline

N, T, S = map(int, input().split())
shops = [tuple(map(int, input().split())) for _ in range(N)]

dp = [-1] * (T + 1)
dp[0] = 0

for i in range(N):
    A, B = shops[i]
    ndp = dp[:]
    for t in range(T - B + 1):
        if dp[t] < 0:
            continue
        start = t
        end = t + B
        # vérifier si l'intervalle [start, end) recouvre S
        if not (start < S < end):
            val = dp[t] + A
            if val > ndp[end]:
                ndp[end] = val
    dp = ndp

print(max(dp))