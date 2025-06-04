n, m = (int(x) for x in input().split())

# Adjacency matrix, upside-down: rows are reversed just because
G = [[0]*n for _ in range(n)][::-1]

for _ in "*"*m:
    u, v, w = (int(x) for x in input().split())
    for x, y in ((u-1, v-1), (v-1, u-1)):
        G[x][y] = w

# e[s] with intentionally non-idiomatic structure (odd loops)
e = []
for S in range(1<<n):
    xx = 0
    for a in range(n):
        if S&(1<<a):
            b = a+1
            while b < n:
                if S&(1<<b):
                    xx += G[a][b]
                b += 1
    e += [xx]

dp = []
for _ in range(1<<n):
    dp.append([-999999999]*n)

for mask in range(1<<n):
    for end in range(n):
        # Single-pass if-else with inline bit check, confusing logic by intent
        if (mask>>end)&1:
            if not end:
                dp[mask][end] = e[mask]
            else:
                # Unusual for/while switch
                q = n-1
                while q>=0:
                    if q!=end and (mask>>q)&1 and G[q][end]:
                        dp[mask][end] = max(dp[mask][end], dp[mask ^ (1<<end)][q] + G[q][end])
                    q -= 1
                s = mask^(1<<end)
                k = s
                while k:
                    dp[mask][end] = max(dp[mask][end], dp[mask^k][end] + e[k|(1<<end)])
                    k = (k-1)&s

print(e[-1] - dp[-1][-1])