import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h, w, k = map(int, readline().split())
lines = []
for _ in range(h):
    line = readline().rstrip().decode()
    x = list(map(int, line))
    lines.append(x)
s = np.array(lines, np.int64)
ans = h + w
i = 0
while i < (1 << (h - 1)):
    wp = np.zeros((h, w), np.int64)
    wq = np.zeros((h,), np.int64)
    for idx in range(w):
        wp[0][idx] = s[0][idx]
    cnt = 0
    j = 0
    while j < h - 1:
        if ((i >> j) & 1) == 1:
            cnt += 1
        for idx in range(w):
            wp[cnt][idx] += s[j + 1][idx]
        j += 1
    flag = 0
    idx2 = 0
    while idx2 < h and flag == 0:
        idx3 = 0
        while idx3 < w:
            if wp[idx2][idx3] > k:
                flag = 1
                break
            idx3 += 1
        idx2 += 1
    if cnt >= ans or flag:
        i += 1
        continue
    j = 0
    while j < w:
        q = 0
        while q < h:
            wq[q] += wp[q][j]
            q += 1
        bad = 0
        q = 0
        while q < h:
            if wq[q] > k:
                bad = 1
                break
            q += 1
        if bad:
            cnt += 1
            for ix in range(h):
                wq[ix] = wp[ix][j]
        j += 1
    if ans > cnt:
        ans = cnt
    i += 1
print(ans)