import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10 ** 9 + 7

N, M = map(int, read().split())

# ・合計の訪問済の町の個数
# ・訪問済だけれど強連結成分には入っていない町の個数
# に対する場合の数を持ってdp

dp = np.zeros((N + 1, N + 1), np.int64)
dp[1, 0] = 1
for _ in range(M):
    prev = dp
    dp = np.zeros_like(prev)
    # 強連結成分にもどる
    dp[:, 0] += (prev[:, :] * (np.arange(N + 1)[:, None] - np.arange(N + 1)[None, :])).sum(axis=1)
    # 未確定部分内で
    dp[:, :] += prev[:, :] * np.arange(N + 1)[None, :]
    # 未確定部分の拡張
    dp[1:, 1:] += prev[:-1, :-1] * np.arange(N, 0, -1)[:, None]
    dp %= MOD

answer = dp[N, 0]
print(answer)