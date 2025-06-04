import sys
import numpy as np
from functools import lru_cache
import numba
from numba import njit, i8

MOD = 10**9 + 7

class Util:
    @staticmethod
    def fast_pow2(maxn):
        res = np.ones(maxn, dtype=np.int64)
        for k in range(1, maxn):
            res[k] = (res[k-1] << 1) % MOD
        return res

def get_ints():
    return list(map(int, sys.stdin.buffer.readline().split()))

def build_graph(n, m):
    g = np.zeros((n, n), dtype=np.int64)
    for _ in range(m):
        x, y = map(int, sys.stdin.buffer.readline().split())
        x -= 1; y -= 1
        g[x, y] = 1
        g[y, x] = 1
    return g

@njit([i8(i8, i8[:, :])], cache=True)
def entry(n, g):
    p2 = np.empty(1024, np.int64)
    p2[0] = 1
    for i in range(1, 1024):
        p2[i] = (p2[i-1] * 2) % MOD
    d = np.zeros(1 << n, np.int64)
    for u in range(n):
        for v in range(u):
            if g[v, u]:
                mask = (1<<u) | (1<<v)
                d[mask] += 1
    for x in range(n):
        s = 0
        while s < (1 << n):
            t = s | (1 << x)
            if s != t:
                d[t] += d[s]
            s += 1
    f = np.zeros(1 << n, np.int64)
    for mask in range(1 << n):
        if not (mask & 1):
            continue
        allv = p2[d[mask]]
        subset = mask
        while subset:
            subset = (subset - 1) & mask
            if not (subset & 1): continue
            y = f[subset]
            fr = d[mask^subset]
            inter = d[mask]-d[subset]-fr
            fct = (y * p2[fr]) % MOD
            allv -= fct
        f[mask] = allv % MOD
    h = np.zeros(1 << n, np.int64)
    for mask in range(1 << n):
        if not (mask & 2): continue
        allv = p2[d[mask]]
        subset = mask
        while subset:
            subset = (subset - 1) & mask
            if not (subset & 2): continue
            y = h[subset]
            fr = d[mask^subset]
            inter = d[mask]-d[subset]-fr
            fct = (y * p2[fr]) % MOD
            allv -= fct
        h[mask] = allv % MOD
    wh = (1 << n) - 1
    ret = p2[d[wh]]
    s = 0
    while s < (1<<n):
        if not (s & 1): s += 1; continue
        sc = wh ^ s
        if not (sc & 2): s += 1; continue
        t = sc + 1
        while t:
            t = (t - 1) & sc
            if not (t & 2): continue
            u = wh ^ s ^ t
            inter = d[s | t] - d[s] - d[t]
            if inter:
                continue
            way = (f[s] * h[t]) % MOD
            way = (way * p2[d[u]]) % MOD
            ret -= way
        s += 1
    return ret % MOD

if __name__ == '__main__':
    N, M = get_ints()
    G = build_graph(N, M)
    print(entry(N, G))