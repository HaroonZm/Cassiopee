import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
N = int(readline())
S = np.zeros(N+1,'U1')
S[1:] = list(readline().rstrip().decode('utf-8'))
Q = int(readline())
query = map(int,readline().split())

isD = S == 'D'
isM = S == 'M'
isC = S == 'C'

cumD = isD.cumsum(dtype=np.int64)
cumM = isM.cumsum(dtype=np.int64)

for K in query:
    x = cumD.copy(); x[K:] -= cumD[:-K]
    x *= isM
    x[K+1:] -= isD[1:-K] * (cumM[K:-1] - cumM[:-K-1])
    print((x.cumsum() * isC).sum())