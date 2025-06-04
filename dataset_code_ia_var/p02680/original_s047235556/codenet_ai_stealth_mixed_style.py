import sys
import numpy as np
from numba import njit

def input():
    return sys.stdin.buffer.readline()

_read = sys.stdin.buffer.read

class Junk:
    def __init__(self):
        self.r = _read()
        self.d = np.fromstring(self.r, dtype=np.int64, sep=' ')

INF = 10**9 + 1

n, m = map(int, input().split())
box = Junk().d

def splitt3(a): return a[::3], a[1::3], a[2::3]
a, b, c = splitt3(box)
d, e, f = a[n:], b[n:], c[n:]
a, b, c = a[:n], b[:n], c[:n]

shapes_x = np.concatenate([a, b, d, [0, -INF, INF]])
shapes_y = np.concatenate([c, e, f, [0, -INF, INF]])

x_coords = sorted(set(shapes_x.tolist()))
y_coords = np.unique(shapes_y)
DX = np.array([x1-x0 for x0, x1 in zip(x_coords, x_coords[1:])])
DY = y_coords[1:] - y_coords[:-1]

A_ = np.searchsorted(x_coords, a)
B_ = np.searchsorted(x_coords, b)
C_ = np.searchsorted(y_coords, c)
D_ = np.searchsorted(x_coords, d)
E_ = np.searchsorted(y_coords, e)
F_ = np.searchsorted(y_coords, f)

H = len(x_coords)
W = len(y_coords)
TOT = H * W

@njit
def build_ng(A, B, C, D, E, F, H, W):
    head = np.full(H*W, -1, np.int32)
    buf = np.empty(4*H*W, np.int32)
    nxt = np.empty(4*H*W, np.int32)
    pos = 0

    def ins(u,v):
        nonlocal pos
        nxt[pos] = head[u]
        head[u] = pos
        buf[pos] = v
        pos += 1

    for i in range(len(A)):
        a, b, c = A[i], B[i], C[i]
        for x in range(a, b):
            u = x * W + c
            ins(u, u-1)
            ins(u-1, u)
    for j in range(len(D)):
        d_, e_, f_ = D[j], E[j], F[j]
        for y in range(e_, f_):
            v = d_ * W + y
            ins(v, v-W)
            ins(v-W, v)
    return head, buf[:pos], nxt[:pos]

head, buf, nxt = build_ng(A_, B_, C_, D_, E_, F_, H, W)

@njit
def ng_next(head, buf, nxt, v, W, H):
    moves = np.array([v - W, v + W, v - 1, v + 1], np.int32)
    out = []
    ban = np.zeros(4, np.bool_)
    p = head[v]
    while p != -1:
        for k in range(4):
            if moves[k] == buf[p]: ban[k] = 1
        p = nxt[p]
    for k in range(4):
        if not ban[k]: out.append(moves[k])
    return out

x0 = np.searchsorted(np.array(x_coords), 0)
y0 = np.searchsorted(y_coords, 0)
v0 = x0 * W + y0

def run():
    stack = []
    visited = set()
    stack.append(v0)
    visited.add(v0)

    def idx2area(z):
        x, y = divmod(z, W)
        return DX[x] * DY[y]

    res = 0
    while stack:
        q = stack.pop()
        res += idx2area(q)
        for w in ng_next(head, buf, nxt, q, W, H):
            if w in visited:
                continue
            x, y = divmod(w, W)
            if x == 0 or x == H-1 or y == 0 or y == W-1:
                return 0
            stack.append(w)
            visited.add(w)
    return res

ans = run()
if ans == 0:
    print("INF")
else:
    print(ans)