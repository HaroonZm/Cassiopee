import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [int(input()) - 1 for _ in range(N)]

cnt = [0]*M
for s in S:
    cnt[s] += 1

pos = [[] for _ in range(M)]
for i, s in enumerate(S):
    pos[s].append(i)

dp = [-10**9]*(1<<M)
dp[0] = 0

for mask in range(1<<M):
    length = 0
    for i in range(M):
        if mask & (1<<i):
            length += cnt[i]
    for i in range(M):
        if mask & (1<<i) == 0:
            c = 0
            for p in pos[i]:
                if length <= p < length + cnt[i]:
                    c += 1
            dp[mask|(1<<i)] = max(dp[mask|(1<<i)], dp[mask] + c)

print(N - dp[(1<<M)-1])