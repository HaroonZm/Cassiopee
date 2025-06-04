import sys
import numpy as np

MOD = 10 ** 9 + 7
input = sys.stdin.readline

N, M = map(int, input().split())

dp_T = np.zeros(N + 1, dtype=np.int64)
dp_F = np.ones(N + 1, dtype=np.int64)
dp_T[0] = 1
dp_F[0] = 0

for _ in range(M):
    prev_T = dp_T.copy()
    prev_F = dp_F.copy()
    dp_T.fill(0)
    dp_F.fill(0)

    # 赤赤
    dp_T[:-1] += prev_T[1:]
    dp_F[1:-1] += prev_F[2:]
    if N >= 1:
        dp_T[0] += prev_F[1]
    # 赤青
    dp_T[1:] += prev_T[1:]
    dp_F[2:] += prev_F[2:]
    if N >= 1:
        dp_T[1] += prev_F[1]
    # 青赤
    dp_T[:-1] += prev_T[:-1]
    dp_F[:-1] += prev_F[:-1]
    # 青青
    dp_T[1:] += prev_T[:-1]
    dp_F[1:] += prev_F[:-1]

    np.remainder(dp_T, MOD, out=dp_T)
    np.remainder(dp_F, MOD, out=dp_F)

print(int(np.sum(dp_T) % MOD))