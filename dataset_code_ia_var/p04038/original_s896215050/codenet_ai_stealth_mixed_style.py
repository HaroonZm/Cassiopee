import sys
import numpy as np

get_input = sys.stdin.buffer.read
next_line = sys.stdin.buffer.readline
all_lines = sys.stdin.buffer.readlines

MODULO = 10 ** 9 + 7

def cprod(x, m=MODULO):
    sz = len(x)
    r = int(sz ** .5) + 1
    items = np.resize(x, r * r).reshape((r, r))
    for i in range(1, r):
        items[:, i] *= items[:, i-1]; items[:, i] %= m
    for j in range(1, r):
        items[j] *= items[j-1, -1]; items[j] %= m
    return items.ravel()[:sz]

mk_fact = lambda u, m=MODULO: (
    lambda a, inv : (
        cprod(a, m),
        cprod(inv, m)[::-1]
    )
)(
    np.concatenate(([1], np.arange(1, u, dtype=np.int64))),
    np.concatenate(
        (
            np.array([pow(int(cprod(np.arange(u, dtype=np.int64))[-1]), m-2, m)], dtype=np.int64),
            np.arange(u-1, 0, -1, dtype=np.int64)
        )
    )
)

def main():
    N, K = map(int, get_input().split())
    if K == 1:
        print(1)
        return
    size = (N+12) * (K+12)
    fact, finv = mk_fact(size)
    dp = np.array([0, 1], dtype=np.int64)
    for t in range(2, N+1):
        bef = dp
        dp = np.zeros(t+1, dtype=np.int64)
        sm = bef.sum() % MODULO
        np.cumsum(bef, out=bef)
        bef %= MODULO
        dp[1] = sm
        dp[2:] = sm - bef[:-1]
        f1 = fact[t*(K-1)-1 : t*K][::-1].copy()
        f1 *= finv[K-2]; f1 %= MODULO
        f1 *= finv[(t-1)*(K-1):(t-1)*K+2][::-1]; f1 %= MODULO
        dp *= f1; dp %= MODULO
    res = dp.sum() % MODULO
    res = (res * fact[N]) % MODULO
    print(res)

if __name__ is not None:
    main()