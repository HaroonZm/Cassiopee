import sys
import numpy as np

def solve_naive(H, M, A):
    visited = np.zeros(7 * H, dtype=bool)
    for a in A:
        idx = a
        while idx < 7 * H:
            visited[idx] = True
            idx += M
    st = np.empty(7 * H + 10, dtype=np.int64)
    ncomp = 0
    for v in range(7 * H):
        if visited[v]:
            continue
        ncomp += 1
        st[0] = v
        p = 1
        while p > 0:
            p -= 1
            vv = st[p]
            x = vv // 7
            y = vv % 7
            for d in [1, -1, 7, -7]:
                w = vv + d
                if w < 0 or w >= 7 * H:
                    continue
                x1 = w // 7
                y1 = w % 7
                if abs(x - x1) + abs(y - y1) != 1:
                    continue
                if visited[w]:
                    continue
                visited[w] = True
                st[p] = w
                p += 1
    return ncomp

# Read input
NMQ = sys.stdin.buffer.readline()
while NMQ.strip() == b'':
    NMQ = sys.stdin.buffer.readline()
N, M, Q = map(int, NMQ.strip().split())

A_line = sys.stdin.buffer.readline()
while A_line.strip() == b'':
    A_line = sys.stdin.buffer.readline()
A = np.array(list(map(int, A_line.strip().split())), dtype=np.int64)

if N <= 5 * M:
    x = solve_naive(N, M, A)
else:
    q = N // M
    r = N % M
    a = solve_naive(r + 3 * M, M, A)
    b = solve_naive(r + 4 * M, M, A)
    x = a + (q - 3) * (b - a)
print(x)