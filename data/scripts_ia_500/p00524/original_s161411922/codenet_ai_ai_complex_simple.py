from heapq import heappop as _pop, heappush as _push
import sys as _sys
from functools import reduce as _reduce
N, M, X = map(int, iter(lambda:_sys.stdin.readline(), '')().__next__().split())
H = [0]+_reduce(lambda a,b: a+[int(b)], (_sys.stdin.readline() for _ in [0]*N), [])
G = _reduce(lambda acc, x: (
    acc[x[0]].append((x[1], x[2])) or acc[x[1]].append((x[0], x[2])) or acc
), (tuple(map(int, l.split())) for l in _sys.stdin), [[] for _ in range(N+1)])

V = [float('inf')]*(N+1)
Q = [(0, 1, X)]
while Q:
    t,c,h = _pop(Q)
    if c == N:
        print(t+(H[c]-h)); exit(0)
    if t > V[c]:
        continue
    Mx = H[c]
    list(map(lambda p: (
        None if p[1]>h else (
            lambda nt, nh: (
                V.__setitem__(p[0], nt) if V[p[0]]>nt else None,
                _push(Q, (nt, p[0], nh))
            )
        )(*(lambda dt: (
            (t+dt, h-dt) if 0<=h-dt<=H[p[0]] else (
                (t-(h-dt), 0) if h-dt<0 else (t+(h-dt-H[p[0]]), H[p[0]])
            )
        ))(p[1]))
    ), G[c]))
print(-1)