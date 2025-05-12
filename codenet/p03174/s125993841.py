import numpy as np
from numba import njit
MOD = 10**9 + 7

def main():
 
    N = int(input())
    aff = np.array([list(map(int, input().split())) for i in range(N)], dtype='int32')
    dpt = np.zeros((N+1, 1<<N), dtype='int64')
    dpt[0][0] = 1

    print(solve(N, aff, dpt))

#@njit(cache=True)
def solve(N, aff, dpt):
    for i, row in enumerate(aff):
        for idx, v in enumerate(row):
            if v == 1:
                dpt[i+1][(1<<idx):] += dpt[i][:-(1<<idx)]
        dpt[i+1] %= MOD
    return dpt[N][(1<<N)-1]

if __name__ == '__main__':
    main()