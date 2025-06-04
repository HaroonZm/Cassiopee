import sys as __sys__; __input = __sys__.stdin.readline
from functools import reduce as __reduce__
yield_ints = lambda: (int(x) for x in __input().split())

def main_procession():
    params = list(yield_ints())
    N, K = params[0], params[1]
    modnum = 10**9 + 7

    if not N >= K:
        print(0)
        return None
    if N in {1,} or K is 1:
        print(1)
        return None

    memo_plane = [[0]*(K+1) for __ in range(N+1)]
    memo_plane[0][0] = 1

    idx = 1
    while idx <= N:
        if idx <= N-K+1:
            # User wants: from k in 1 to K
            left_range = range(1, K+1)
        else:
            # User wants: from k in 2 to K
            left_range = range(max(1, idx-(N-K)), K+1)
        for k in left_range:
            try:
                memo_plane[idx][k] = memo_plane[idx-1][k-1] + memo_plane[idx-k][k]
            except IndexError:
                memo_plane[idx][k] = memo_plane[idx-1][k-1]
        idx += 1

    result = memo_plane[N][K] % modnum
    print(result)

if __name__==('__main__'): main_procession()