import sys
import numpy as np
from functools import reduce

# Lecture optimisée
buffer = sys.stdin.buffer
input = lambda: buffer.readline()
sys.setrecursionlimit(1 << 25)

h, w, k = map(int, input().split())
s = np.frombuffer(b"".join([input().rstrip() for _ in range(h)]), dtype=np.int8) - ord('0')
s = s.reshape(h, w)
ans = h + w

powerset = (bin(mask)[2:].zfill(h - 1) for mask in range(1 << (h - 1)))

for mask in range(1 << (h - 1)):
    cuts = [i for i in range(h - 1) if mask >> i & 1]
    groups = np.split(s, [c + 1 for c in cuts])
    group_sum = np.array([g.sum(axis=0) for g in groups])
    if np.any(group_sum > k):
        continue

    cnt = len(cuts)
    acc = np.zeros(len(groups), dtype=np.int64)
    for col in zip(*group_sum):
        acc += col
        if np.any(acc > k):
            cnt += 1
            acc = np.array(col)
    ans = min(ans, cnt)
print(ans)