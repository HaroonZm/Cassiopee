import sys
from collections import defaultdict

def solve():
    readline, write = sys.stdin.readline, sys.stdout.write
    N = int(readline())
    if N == 0:
        return False

    P = [tuple(map(int, readline().split())) for _ in range(N)]
    L = 2000
    Q = defaultdict(list)
    LS = []
    P_cycle = [P[-1]] + P  # cyclic points for easier indexing

    for i in range(1, N+1):
        x0, y0 = P_cycle[i-1]
        x1, y1 = P_cycle[i]
        if y0 != y1:
            Q[y0].append(i-1)
            Q[y1].append(i-1)
        LS.append(((x0, y0), (x1, y1)) if y0 < y1 else ((x1, y1), (x0, y0)))

    U = bytearray(N)
    active_edges = set()
    ans = 0

    for y in range(-L, L):
        for i in Q.get(y, ()):
            if U[i]:
                active_edges.discard(i)
            else:
                active_edges.add(i)
                U[i] = 1
        js = sorted(active_edges, key=lambda i: (
            (LS[i][0][0] + (LS[i][1][0] - LS[i][0][0]) * (y - LS[i][0][1]) / (LS[i][1][1] - LS[i][0][1]))
            if LS[i][1][0] >= LS[i][0][0]
            else (LS[i][0][0] + (LS[i][1][0] - LS[i][0][0]) * ((y+1) - LS[i][0][1]) / (LS[i][1][1] - LS[i][0][1]))
        ))

        l, r = -5000, -5000
        it = iter(js)
        for k, i in enumerate(it):
            (x0, y0), (x1, y1) = LS[i]
            dx, dy = x1 - x0, y1 - y0
            if k & 1:
                x = (x0 + (dx*((y+1) - y0) + (dy-1 if dx >= 0 else 0)) // dy) if dx >= 0 else (x0 + (dx*(y - y0) + (dy-1 if dx < 0 else 0)) // dy)
                r = x
            else:
                x = (x0 + dx*(y - y0) // dy) if dx >= 0 else (x0 + dx*((y+1) - y0) // dy)
                if r < x:
                    ans += r - l
                    l = x
        ans += r - l

    write(f"{ans}\n")
    return True

while solve():
    pass