import sys
import numpy as np
from numba import njit, i8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

@njit(fastmath=True, cache=True)
def solve_optimized(H: int, M: int, A: np.ndarray) -> int:
    lim = 7 * H
    visited = np.zeros(lim, dtype=np.bool_)
    for a in A:
        visited[a : lim : M] = True

    ncomp = 0
    stack = np.empty(lim + 10, dtype=np.int64)
    offsets = np.array([1, -1, 7, -7], dtype=np.int64)

    for v in range(lim):
        if visited[v]: continue
        ncomp += 1
        ptr = 1
        stack[0] = v
        visited[v] = True
        while ptr:
            ptr -= 1
            idx = stack[ptr]
            x, y = divmod(idx, 7)
            for d in offsets:
                w = idx + d
                if not (0 <= w < lim):
                    continue
                x1, y1 = divmod(w, 7)
                if abs(x - x1) + abs(y - y1) != 1:
                    continue
                if visited[w]: continue
                visited[w] = True
                stack[ptr] = w
                ptr += 1
    return ncomp

N, M, Q = map(int, readline().split())
A = np.frombuffer(readline(), dtype=np.int64, sep=b' ')

if N <= 5 * M:
    x = solve_optimized(N, M, A)
else:
    q, r = divmod(N, M)
    a = solve_optimized(r + 3 * M, M, A)
    b = solve_optimized(r + 4 * M, M, A)
    x = a + (q - 3) * (b - a)
print(x)