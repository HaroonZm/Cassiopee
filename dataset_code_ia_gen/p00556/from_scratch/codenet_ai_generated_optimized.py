import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [int(input()) - 1 for _ in range(N)]

total = [0]*M
for x in a:
    total[x] += 1

pos = [[] for _ in range(M)]
for i, x in enumerate(a):
    pos[x].append(i)

dp = [-1]*(1<<M)
dp[0] = 0

for mask in range(1<<M):
    if dp[mask] == -1:
        continue
    l = 0
    for i in range(M):
        if (mask >> i) & 1:
            l += total[i]
    for i in range(M):
        if (mask >> i) & 1 == 0:
            s = dp[mask]
            cnt = 0
            for p in pos[i]:
                if l <= p < l + total[i]:
                    cnt += 1
            nmask = mask | (1 << i)
            val = s + cnt
            if dp[nmask] < val:
                dp[nmask] = val

print(N - dp[(1<<M)-1])