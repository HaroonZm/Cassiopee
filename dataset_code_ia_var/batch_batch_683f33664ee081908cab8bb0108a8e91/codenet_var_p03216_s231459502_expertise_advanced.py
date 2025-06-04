import sys
import numpy as np
from functools import partial

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N = int(readline())
S = np.frombuffer(readline().rstrip(), dtype='S1')
Q = int(readline())
queries = np.frombuffer(read(), dtype=np.int64, count=Q, sep=b' ')

isD = (S == b'D')
isM = (S == b'M')
isC = (S == b'C')

cumD = np.concatenate(([0], np.cumsum(isD, dtype=np.int64)))
cumM = np.concatenate(([0], np.cumsum(isM, dtype=np.int64)))

@np.vectorize
def solve_one(K):
    # Sliding window of width K counting D and M before each position
    D = cumD[K:] - cumD[:-K]
    M = cumM[K:] - cumM[:-K]
    # DM-pair tracking
    DM = np.zeros_like(S, dtype=np.int64)
    mask = isM
    DM[K:] = D * mask[K:]
    DM[K:] -= isD[:-K] * M
    np.cumsum(DM, out=DM)
    return DM[isC].sum()

results = solve_one(queries)
print('\n'.join(map(str, results)))