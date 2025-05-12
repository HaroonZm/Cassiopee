import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
P = np.array(read().split(),np.int64)

P.sort()

P *= np.arange(N+N)
answer = P.sum() / (N+N-1)
print(answer)