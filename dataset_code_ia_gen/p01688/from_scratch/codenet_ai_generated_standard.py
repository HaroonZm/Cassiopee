D = int(input())
x = int(input())
single = [input().split() for _ in range(x)]
y = int(input())
double = [input().strip() for _ in range(y)]

# Parse double to (str, int)
double = [(line[:2], int(line[2:].strip())) for line in double]

items = []
for a, p in single:
    d_count = a.count('D')
    items.append((d_count, p))
for s, q in double:
    d_count = s.count('D')
    items.append((d_count, q))

dp = [0]*(D+1)
for cost, val in items:
    for c in range(D, cost-1, -1):
        if dp[c-cost]+val > dp[c]:
            dp[c] = dp[c-cost]+val
print(max(dp))