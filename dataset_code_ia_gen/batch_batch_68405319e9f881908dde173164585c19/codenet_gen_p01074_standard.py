N, M, L = map(int, input().split())
classes = []
for _ in range(M):
    d, a, k, t = map(int, input().split())
    mask = 0
    for i in range(k):
        mask |= 1 << (d * N + (a - 1 + i))
    classes.append((mask, t))

from collections import defaultdict

dp = defaultdict(int)
dp[0] = 0
for mask, t in classes:
    for used, val in list(dp.items()):
        if (used & mask) == 0:
            dp[used | mask] = max(dp.get(used | mask, 0), val + t)

results = [0]*(L+1)
for used, val in dp.items():
    cnt = bin(used).count('1')
    # Number of classes selected = number of distinct intervals = count of (used bits)/class bits not directly countable here
    # Instead, we track selecting classes cumulatively by the dp process but we don't know count by bits
    # Alternative : store dp with count keys
    pass

# To handle limit L on number of classes, redo dp with class count dimension

dp = [defaultdict(int) for _ in range(L+1)]
dp[0][0] = 0
for mask, t in classes:
    for l in range(L-1, -1, -1):
        for used, val in list(dp[l].items()):
            if (used & mask) == 0:
                dp[l+1][used | mask] = max(dp[l+1].get(used | mask, 0), val + t)

print(max([max(d.values()) if d else 0 for d in dp]))