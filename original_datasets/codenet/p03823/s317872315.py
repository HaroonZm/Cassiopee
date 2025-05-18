import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7

def main(N, A, B, S):
    if N == 1:
        return 2
    INF = 1 << 62
    S = np.append(S, INF)
    if A > B:
        A, B = B, A
    if np.min(S[2:] - S[:-2]) < A:
        return 0
    # A 未満でたどって、Xがどこまで置けるか
    X = np.zeros_like(S)
    for i in range(1, N + 1):
        if S[i] - S[i - 1] >= A:
            X[i] = X[i - 1]
        else:
            X[i] = i
    # 直前の Y としてありうる最も右
    Y = np.searchsorted(S, S - B, side='right') - 1
    dp = np.zeros_like(S)
    dp_cum = np.zeros_like(S)

    dp[0] = 1
    dp_cum[0] = 1
    for n in range(1, N + 1):
        if X[n - 1] == 0:
            # 初出の Y
            dp[n] = 1
        # 直前の Y の範囲
        l, r = max(0, X[n - 1] - 1), min(n - 1, Y[n])
        if l <= r:
            dp[n] += dp_cum[r] - dp_cum[l] + dp[l]
        dp[n] %= MOD
        dp_cum[n] = (dp_cum[n - 1] + dp[n]) % MOD
    return dp[-1]

signature = '(i8,i8,i8,i8[:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', signature)(main)
    cc.compile()

from my_module import main

N, A, B = map(int, readline().split())
S = np.array(read().split(), np.int64)

print(main(N, A, B, S))