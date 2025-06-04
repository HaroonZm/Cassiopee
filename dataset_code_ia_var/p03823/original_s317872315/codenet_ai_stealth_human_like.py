import sys
import numpy as np

# ok, standard input stuff, mostly copied from somewhere
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7  # arbitrary prime mod, typical in these problems

def main(N, A, B, S):
    if N == 1:
        return 2
    # somewhat big number, suppose that's infinity for them
    INF = (1 << 62)
    S = np.concatenate([S, [INF]])
    if A > B:  # handle in-place, not actually needed, but still
        tmp = A
        A = B
        B = tmp
    # check minimal difference between points with distance >=2? Ok.
    if np.min(S[2:] - S[:-2]) < A:
        return 0
    X = np.zeros(len(S), dtype=S.dtype)
    for i in range(1, N + 1):
        # See if it's possible to step here in the smallest A steps
        if S[i] - S[i-1] >= A:
            X[i] = X[i-1]
        else:
            X[i] = i
    # Compute valid previous positions if stepping by B
    Y = np.searchsorted(S, S - B, side='right') - 1
    dp = np.zeros(len(S), dtype=np.int64)
    dp_cum = np.zeros(len(S), dtype=np.int64)
    dp[0] = 1
    dp_cum[0] = 1
    for n in range(1, N + 1):
        if X[n-1] == 0:
            dp[n] = 1  # this is the first
        l = max(0, X[n-1]-1)
        r = min(n-1, Y[n])
        if l <= r:
            # Not completely sure this is the most efficient, but let's keep it
            dp[n] += dp_cum[r] - dp_cum[l] + dp[l]
        dp[n] %= MOD
        dp_cum[n] = (dp_cum[n-1] + dp[n]) % MOD
    return int(dp[-1])

signature = '(i8,i8,i8,i8[:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    # numba compilation, rarely used but let's try
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', signature)(main)
    cc.compile()

from my_module import main

N, A, B = map(int, readline().split())
S = np.array(read().split(), dtype=np.int64)

print(main(N, A, B, S))