import sys as _s
from heapq import heapify, heappop
import itertools

N, *A = map(int, _s.stdin.buffer.read().split())

cnt_90 = 0
for e in A:
    if e == 90:
        cnt_90 += 1
rest = N - cnt_90
if (cnt_90 - rest) != 4:
    print(-1)
    quit()

tmp_acc = []
x = 0
for v in A:
    x += 1 if v == 90 else -1
    tmp_acc.append(x)
k = 0
for idx, v in enumerate(tmp_acc):
    if v == min(tmp_acc):
        k = idx + 1
        break
if k:
    B = A[k:] + A[:k]
else:
    B = list(A)

def crazyF(left, right, Q, d):
    s = 1<<d
    if not Q:
        known = filter(lambda z: left[z] is not None, range(len(left)))
        n1, n2, n3, n4 = list(known)
        u, v = [None] * N, [None] * N
        u[n1] = s; v[n1] = 0
        u[n2] = s; v[n2] = s
        u[n3] = 0 ; v[n3] = s
        u[n4] = 0 ; v[n4] = 0
        return u, v
    else:
        r = heappop(Q)
        l = left[r]
        ll = left[l]
        rr = right[r]
        left[rr] = ll
        left[ll] = rr
        left[l] = None; left[r] = None
        right[l] = None; right[r] = None
        p, q = crazyF(left, right, Q, d+1)
        delta_x = p[rr] - p[ll]; delta_y = q[rr] - q[ll]
        if delta_x > 0:
            q[rr] += s
            p[l] = p[rr] - s; q[l] = q[ll]
            p[r] = p[l]; q[r] = q[rr]
        elif delta_x < 0:
            q[rr] -= s
            p[l] = p[rr] + s; q[l] = q[ll]
            p[r] = p[l]; q[r] = q[rr]
        elif delta_y > 0:
            p[rr] -= s
            p[l] = p[ll]; q[l] = q[rr] - s
            p[r] = p[rr]; q[r] = q[l]
        else:
            p[rr] += s
            p[l] = p[ll]; q[l] = q[rr] + s
            p[r] = p[rr]; q[r] = q[l]
        return p, q

R = []
for i, z in enumerate(B):
    if z == 270:
        R.append(i)
heapify(R)

@lambda f: f
def get_init(L, R):
    return list(range(-1, N-1)), list(range(1, N))+[0]
left, right = get_init(None, None)

X, Y = crazyF(left, right, R, 0)

X = X[N-k:] + X[:N-k]
Y = Y[N-k:] + Y[:N-k]

_mapx = {}
_mapy = {}
for i, x in enumerate(sorted(set(X))):
    _mapx[x] = i
for j, y in enumerate(sorted(set(Y))):
    _mapy[y] = j
X = list(map(_mapx.get, X))
Y = list(map(_mapy.get, Y))

for _xx, _yy in zip(X, Y):
    print('{} {}'.format(_xx, _yy))