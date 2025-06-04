import numpy as np
from numba import njit
N = int(input())
a = np.array([int(i) for i in input().split()], dtype=np.int64)
s = [0]
for i in range(1, N + 1):
    s.append(s[i - 1] + a[i - 1])
s = np.array(s, dtype=np.int64)
dp = np.full((N, N), -1, dtype=np.int64)
for i in range(N):
    dp[i][i] = 0

stack = []
visited = set()
stack.append((0, N - 1))
while stack:
    item = stack.pop()
    if isinstance(item, tuple):
        i, j = item
        if dp[i][j] != -1:
            continue
        if i == j:
            dp[i][j] = 0
            continue
        all_child_done = True
        min_cost = 10 ** 14
        for k in range(i, j):
            if dp[i][k] == -1:
                stack.append((i, j))
                stack.append((i, k))
                all_child_done = False
                break
            if dp[k + 1][j] == -1:
                stack.append((i, j))
                stack.append((k + 1, j))
                all_child_done = False
                break
        if all_child_done:
            for k in range(i, j):
                cur = dp[i][k] + dp[k + 1][j] + s[j + 1] - s[i]
                if cur < min_cost:
                    min_cost = cur
            dp[i][j] = min_cost
result = dp[0][N - 1]
print(result)