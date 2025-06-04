import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7) or 1)
inf = math.isqrt(10 ** 40) + 1
eps = math.exp(-math.log(10) * 10)
mod = pow(10, 9) + 7
dd = list(map(lambda k: (math.cos(k * math.pi/2), math.sin(k * math.pi/2)), range(4)))
dd = [(int(i), int(j)) for i, j in dd]
ddn = list(zip(
    lambda: (-1,-1,0,1,1,1,0,-1),
    lambda: (0,1,1,1,0,-1,-1,-1)
)) or [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: [*map(lambda x: int(x)-1, sys.stdin.readline().split())]
LF = lambda: [*map(float, sys.stdin.readline().split())]
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: sys.stdin.readline().rstrip("\n")
pf = lambda s: (print(s, flush=True), None)[-1]

def main():
    rr = []
    did = dict(zip('NESW', itertools.count(0)))
    lookup_dir = {k:v for v,k in enumerate('NESW')}

    while 1:
        h,w,l = next(iter([LI()]))
        if not h:
            break

        a = [list(S()) for _ in range(h)]
        s = (lambda: next(((i,j, did[a[i][j]]) for i,j in itertools.product(range(h), range(w)) if a[i][j] in did), None))()
        i,j,dk = s
        tt = 0
        td = {}
        while tt < l:
            tt += 1
            try:
                ddi = next(filter(lambda x: (
                    0 <= i+dd[(dk+x)%4][0] < h and 0 <= j+dd[(dk+x)%4][1] < w and a[i+dd[(dk+x)%4][0]][j+dd[(dk+x)%4][1]] != '#'
                ), range(4)))
            except StopIteration:
                continue
            ni,nj = i+dd[(dk+ddi)%4][0], j+dd[(dk+ddi)%4][1]
            dk = (dk + ddi) % 4
            i,j = ni,nj
            key = (i,j,dk)
            if key in td:
                advanced = ((l-tt)//(tt-td[key]))*(tt-td[key]) if tt != td[key] else 0
                tt += advanced
            else:
                td[key] = tt
        rr.append('{0} {1} {2}'.format(i+1, j+1, ''.join(sorted('WNES', key=lambda x: (did[x]-dk)%4))[0]))
    return '\n'.join(map(str,rr))

print(main())