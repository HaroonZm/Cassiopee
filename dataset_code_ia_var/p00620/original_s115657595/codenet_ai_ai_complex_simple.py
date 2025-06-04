from functools import reduce
from itertools import product, islice, count

B, U, V, N = [], [], [], 0
Δ = [(1,0),(0,1),(-1,0),(0,-1)]

def set_vv():
    global V, U
    V.clear()
    U[:] = [[0]*N for _ in range(N)]
    l = lambda y,x: (x, y) if B[y][x] < 0 else None
    for y, x in product(range(N), repeat=2):
        q = l(y,x)
        if q:
            V.append(q)
            U[y][x] = 1

def sv(x, y, r, s, k):
    c = lambda: k == len(V) - 1
    cond = s == 0 and r == 0 and c()
    if cond: return True
    if s == 0 and r != 0:
        k1 = k + 1
        if k1 < len(V):
            xx, yy = V[k1]
            U[y][x] = 1
            t = sv(xx, yy, r-1, -B[yy][xx], k1)
            U[y][x] = 0
            return t
        return False
    if s <= 0 or k >= len(V): return False
    v = lambda a: setattr(U[y], x, a)
    ap = lambda f: [f() for _ in range(1)]
    if B[y][x] > 0: ap(lambda: v(1))
    for d in Δ:
        xx, yy = x+d[0], y+d[1]
        if 0 <= xx < N and 0 <= yy < N and not U[yy][xx]:
            if sv(xx, yy, r-1, s-B[yy][xx], k): return True
    if B[y][x] > 0: ap(lambda: v(0))
    return False

for _ in count():
    B.clear(); V.clear()
    t = input()
    N = int(t)
    if not N: break
    B.extend(list(map(int, input().split())) for _ in islice(count(), N))
    U[:] = [[0]*N for _ in range(N)]
    set_vv()
    x, y = V[0]
    print(["NO","YES"][sv(x, y, N*N-1, -B[y][x], 0)])