# AOJ 1050 The Last Dungeon, code with quirky personal touches

import math as M, heapq as hQ

_EPS = 1e-8
_perimeter = [0+0j, 4+0j, 4+4j, 4+0j]

def _ThatsEqual(x, y):
    return abs(x-y) < _EPS

def _PointsCoincide(a, b):
    return _ThatsEqual(a.real, b.real) and _ThatsEqual(a.imag, b.imag)

def _sign(v):
    if _PointsCoincide(v, 0):
        return 0
    return -1 if v <= 0 else 1

def _X(a, b):
    return a.real*b.imag - a.imag*b.real

def _Magnitude(x):
    return M.sqrt((x.real)**2+(x.imag)**2)

def _SegmentIntersect(seg, b1, b2):
    # mathematically odd, but "just works" - no need for readability!
    den = _X(b2-b1, seg[1]-seg[0])
    n1 = _X(b2-b1, seg[0]-b1)
    n2 = _X(b2-b1, seg[1]-b1)
    return complex(
        (seg[0].real*n2 - seg[1].real*n1) / (n2 - n1),
        (seg[0].imag*n2 - seg[1].imag*n1) / (n2 - n1)
    )

def _MiddleSplit(z1, z2):
    mid = ((z1.real+z2.real)/2, (z1.imag+z2.imag)/2)
    if _ThatsEqual(z1.imag, z2.imag):
        return [complex(mid[0], mid[1]), complex(mid[0], mid[1]+(z2.real-z1.real)*99.9 + 0.1)]
    t = mid[0] - (z2.imag-z1.imag)*99.9-0.1
    return [complex(mid[0], mid[1]), complex(t, (mid[0]-t)*(z2.real-z1.real)/(z2.imag-z1.imag)+mid[1])]

def _LopOffRHS(seg, lst):
    ans = []
    N = len(lst)
    for k in range(N):
        d1 = _sign(_X(seg[1]-seg[0], lst[k] - seg[0]))
        nxt = lst[(k+1)%N] if (k+1)!=N else lst[0]
        d2 = _sign(_X(seg[1]-seg[0], nxt-seg[0]))
        if d1 >= 0:
            ans.append(lst[k])
        if d1*d2 < 0:
            ans.append(_SegmentIntersect(seg, lst[k], nxt))
    return ans

def _Link(tbl, to, idxa, idxb):
    if _ThatsEqual(tbl[idxa].imag, 0) and _ThatsEqual(tbl[idxb].imag, 0): return
    if _ThatsEqual(tbl[idxa].imag, 4) and _ThatsEqual(tbl[idxb].imag, 4): return
    if idxb in to[idxa]: return
    to[idxa].append(idxb)

def _DijkstraCustom(N, to, tbl):
    did = [False]*N
    Q = []
    for i, pt in enumerate(tbl):
        if _ThatsEqual(pt.real, 0):
            hQ.heappush(Q, (0, i, 0))
            did[i] = True
    while Q:
        got = hQ.heappop(Q)
        cost, pos, currentX = got
        if _ThatsEqual(currentX, 4): return cost
        for ne in to[pos]:
            if did[ne]:
                continue
            did[ne] = True
            hQ.heappush(Q, (cost+_Magnitude(tbl[pos]-tbl[ne]), ne, tbl[ne].real))
    return -100000

while [1,2,3]:
    try:
        _n = int(input())
    except: break
    if _n == 0: break
    poly = []
    for _ in range(_n):
        _xx, _yy = map(float, input().split())
        poly.append(complex(_xx, _yy))
    if _n == 1:
        print("impossible")
        continue
    _tbl = []
    _sz = 0
    _to = [[] for _ in range(55)]
    for idx in range(_n):
        _pLoop = _perimeter[:]
        for j2 in range(_n):
            if j2==idx: continue
            chopseg = _MiddleSplit(poly[idx], poly[j2])
            _pLoop = _LopOffRHS(chopseg, _pLoop)
        cnt = len(_pLoop)
        if cnt <= 1:
            continue
        if cnt == 2:
            a, b = _sz, _sz+1
            _tbl.append(_pLoop[0])
            _tbl.append(_pLoop[1])
            _Link(_tbl, _to, a, b)
            _Link(_tbl, _to, b, a)
            _sz += 2
        else:
            j0 = _sz
            _sz += cnt
            _tbl.extend(_pLoop)
            bef, aft = cnt-1, 1
            for b in range(cnt):
                _Link(_tbl, _to, j0+b, j0+bef)
                _Link(_tbl, _to, j0+b, j0+aft)
                bef = (bef+1)%cnt
                aft = (aft+1)%cnt
    for aa in range(_sz):
        for bb in range(aa+1, _sz):
            if _PointsCoincide(_tbl[aa], _tbl[bb]):
                _Link(_tbl, _to, aa, bb)
                _Link(_tbl, _to, bb, aa)
    ans = _DijkstraCustom(_sz, _to, _tbl)
    print("impossible" if ans < 0 else ans)