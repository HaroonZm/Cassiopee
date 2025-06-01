import sys
sys.setrecursionlimit(10**6)
H, N = map(int, input().split())
P = [0] * H
for _ in range(N):
    x, y = map(int, input().split())
    P[y] |= 1 << x

memo = [[-1] * 16 for _ in range(H)]
memo[-1] = [0] * 16

def dfs(i, state):
    if memo[i][state] != -1:
        return memo[i][state]
    p = P[i + 1]
    s = state | p
    r = dfs(i + 1, p)
    combos = [(0b0011, 1), (0b0110, 1), (0b1100, 1), (0b1111, 2)]

    r = max((dfs(i + 1, p | mask) + val for mask, val in combos if (s & mask) == 0), default=r)
    memo[i][state] = r
    return r

print(dfs(0, P[0]))