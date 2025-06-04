from sys import stdin
from itertools import product

INF = float('inf')
n, m = map(int, stdin.readline().split())
dp = [[[-INF] * 9 for _ in range(m + 1)] for _ in range(2)]
dp[0][m][0] = 0

for i in range(1, n + 1):
    a, b, c = map(int, stdin.readline().split())
    ndp = [[-INF] * 9 for _ in range(m + 1)]
    for rest, l1, l2 in product(range(m + 1), range(9), range(min(9, rest + 1))):
        val = dp[(i - 1) & 1][rest][l1]
        if val == -INF:
            continue
        if l1 == 0 and l2 == 0:
            add = c
        elif l2 == 0:
            add = max(b, c) if b <= 0 else max(b * l1, c)
        elif l1 == 0:
            add = max(a, c) if a <= 0 else max(a * l2, c)
        else:
            if a <= 0 and b <= 0:
                add = max(a, b, c)
            elif a <= 0:
                add = max(b * l1, c)
            elif b <= 0:
                add = max(a * l2, c)
            elif a <= b:
                add = max(b * l1 + a * min(l2, 8 - l1), c)
            else:
                add = max(a * l2 + b * min(l1, 8 - l2), c)
        nrest = rest - l2
        if nrest >= 0:
            ndp[nrest][l2] = max(ndp[nrest][l2], val + add)
    dp[i & 1] = ndp

print(max(max(row) for row in dp[n & 1]))