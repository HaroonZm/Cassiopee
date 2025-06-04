D = int(input())
x = int(input())
one = [tuple(input().split()) for _ in range(x)]
one = [(a, int(p)) for a, p in one]
y = int(input())
two = [input().rstrip() for _ in range(y)]
two = [(s[:2], int(s[2:].lstrip())) for s in two]

# Pour chaque question, compter combien de D sont requis pour être correcte
items = []
for a, p in one:
    d_count = 1 if a == 'D' else 0
    items.append((d_count, p))
for bc, q in two:
    d_count = sum(c == 'D' for c in bc)
    items.append((d_count, q))

# DP knapsack: dp[i]: max score avec i écritures de 'D'
dp = [0] * (D+1)
for d_req, score in items:
    for i in range(D, d_req-1, -1):
        cand = dp[i - d_req] + score
        if cand > dp[i]:
            dp[i] = cand
print(max(dp))