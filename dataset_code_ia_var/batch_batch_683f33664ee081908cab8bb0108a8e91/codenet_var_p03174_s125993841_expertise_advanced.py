import sys
import numpy as np
from functools import lru_cache

MOD = 10 ** 9 + 7

def readint():
    return int(sys.stdin.readline())

def readints():
    return map(int, sys.stdin.readline().split())

def main():
    N = readint()
    aff = np.fromiter((int(x) for _ in range(N) for x in sys.stdin.readline().split()), dtype=np.int8, count=N*N).reshape(N, N)
    print(solve(N, aff))

def solve(N, aff):
    # Use a flat array to reduce memory usage and improve cache locality
    dpt = np.zeros((N + 1, 1 << N), dtype=np.int64)
    dpt[0, 0] = 1

    # Precompute the indices for bitmask updates in order to vectorize inner loop
    for i, row in enumerate(aff):
        mask_indices = [idx for idx, v in enumerate(row) if v]
        if not mask_indices:
            continue
        for m in range(1 << N):
            if dpt[i, m]:
                for idx in mask_indices:
                    if not (m & (1 << idx)):
                        dpt[i + 1, m | (1 << idx)] = (dpt[i + 1, m | (1 << idx)] + dpt[i, m]) % MOD
    return int(dpt[N, (1 << N) - 1])

if __name__ == '__main__':
    main()