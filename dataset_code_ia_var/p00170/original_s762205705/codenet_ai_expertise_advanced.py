from sys import stdin
from functools import lru_cache

def read_int():
    while True:
        n = stdin.readline()
        if not n:
            return 0
        try:
            return int(n.strip())
        except ValueError:
            continue

while True:
    n = read_int()
    if n == 0:
        break

    F, W, S = [], [], []
    for _ in range(n):
        name, w, s = stdin.readline().split()
        F.append(name)
        W.append(int(w))
        S.append(int(s))

    indices = list(range(n))

    @lru_cache(maxsize=None)
    def dfs(used_mask, su, last):
        if used_mask == (1 << n) - 1:
            return 0, []
        best = float('inf'), []
        for i in indices:
            if not (used_mask >> i & 1) and S[i] >= su:
                cost, order = dfs(used_mask | (1 << i), su + W[i], i)
                my_cost = (n - bin(used_mask).count('1')) * W[i]
                total_cost = cost + my_cost
                candidate = (total_cost, order + [i])
                if candidate < best:
                    best = candidate
        return best

    total_cost, order = dfs(0, 0, -1)
    for idx in reversed(order):
        print(F[idx])