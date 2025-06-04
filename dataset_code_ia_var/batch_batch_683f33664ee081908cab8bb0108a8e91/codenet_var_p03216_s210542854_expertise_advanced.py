import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N = int(readline())
S = np.frombuffer(readline().rstrip(), dtype='S1').astype('U1', copy=False)
Q = int(readline())
queries = np.fromstring(readline(), sep=' ', dtype=np.int32)

isD = S == 'D'
isM = S == 'M'
isC = S == 'C'

cumD = np.zeros(N + 1, dtype=np.int64)
cumM = np.zeros(N + 1, dtype=np.int64)
np.cumsum(isD, out=cumD[1:])
np.cumsum(isM, out=cumM[1:])

for K in queries:
    dx = cumD[K:] - cumD[:-K]
    arr = np.zeros(N, dtype=np.int64)
    arr[K:] = dx * isM[K:]
    if K + 1 < N:
        arr[K+1:] -= isD[1:N-K] * (cumM[K+1:] - cumM[1:N-K])
    print(np.sum(np.cumsum(arr) * isC))