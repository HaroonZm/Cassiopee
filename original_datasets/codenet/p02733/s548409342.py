import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import numpy as np

h, w, k = map(int, readline().split())
s = np.array([list(map(int, readline().rstrip().decode())) for _ in range(h)], np.int64)
ans = h + w
for i in range(2 ** (h - 1)):
    wp = np.zeros((h, w), np.int64)
    wq = np.zeros((h, ), np.int64)
    wp[0] = s[0]
    cnt = 0
    for j in range(h - 1):
        if i >> j & 1:
            cnt += 1
        wp[cnt] += s[j + 1]
    if cnt >= ans or np.count_nonzero(wp > k):
        continue
    for j in range(w):
        wq += wp[:, j]
        if np.count_nonzero(wq > k):
            cnt += 1
            wq = wp[:, j]
    if ans > cnt:
        ans = cnt
print(ans)