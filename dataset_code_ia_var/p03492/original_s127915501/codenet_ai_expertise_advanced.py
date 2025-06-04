from functools import lru_cache, reduce
from operator import mul
import sys

sys.setrecursionlimit(10**6)

def int1(x): return int(x) - 1

def print2D(x): print(*x, sep="\n")

def input_edges(n):
    return [tuple(map(lambda y: int(y) - 1, input().split())) for _ in range(n - 1)]

def prod(iterable, mod):
    return reduce(lambda x, y: x * y % mod, iterable, 1)

def prepare_factorials(n, mod):
    fac = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % mod
    inv[n] = pow(fac[n], mod - 2, mod)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % mod
    return fac, inv

def main():
    MOD = 10 ** 9 + 7
    n = int(input())
    edges = input_edges(n)

    from collections import defaultdict
    to = defaultdict(list)
    for u, v in edges:
        to[u].append(v)
        to[v].append(u)

    n_nodes = [0] * n

    def centroid(u=0, p=-1):
        u_size = 1
        heavy = False
        centroids = []
        for v in to[u]:
            if v == p: continue
            sub = centroid(v, u)
            centroids += sub
            if n_nodes[v] > n // 2:
                heavy = True
            u_size += n_nodes[v]
        n_nodes[u] = u_size
        if n - u_size > n // 2:
            heavy = True
        if not heavy:
            centroids.append(u)
        return centroids

    # Precompute all subtree sizes
    def dfs_count(u=0, p=-1):
        sz = 1
        for v in to[u]:
            if v != p:
                sz += dfs_count(v, u)
        n_nodes[u] = sz
        return sz
    dfs_count()

    centroids = centroid()
    fac, inv = prepare_factorials(n, MOD)

    @lru_cache(maxsize=None)
    def k_fix_way(com_n, com_r):
        if com_r > com_n or com_r < 0: return 0
        return (fac[com_n] * inv[com_n - com_r] % MOD) * (fac[com_n] * inv[com_r] % MOD) * inv[com_n - com_r] % MOD

    if len(centroids) == 2:
        h = n // 2
        print(pow(fac[h], 2, MOD))
        return

    c = centroids[0]
    subtree_sizes = [n_nodes[v] for v in to[c] if n_nodes[v] <= n // 2]
    if c != 0:
        subtree_sizes.append(n - n_nodes[c])

    dp = [0] * n
    dp[0] = 1
    for node_n in subtree_sizes:
        ndp = dp[:]
        for j in range(n - 1, -1, -1):
            if dp[j]:
                for k in range(1, node_n + 1):
                    if j + k < n:
                        ndp[j + k] = (ndp[j + k] + dp[j] * k_fix_way(node_n, k)) % MOD
        dp = ndp

    ans = 0
    sign = 1
    for j in range(n):
        ans = (ans + sign * dp[j] * fac[n - j]) % MOD
        sign *= -1
    print(ans % MOD)

main()