import sys
from collections import deque

def process():
    N, M = (int(x) for x in sys.stdin.readline().split())
    INF = 10**20
    _x, _y = set([INF, -INF]), set([INF, -INF])

    lx, ly = [], []
    v1, v2 = ([-1, 0, 1, 0], [0, -1, 0, 1])

    horizontal, vertical = [0]*N, [0]*M

    for idx in range(N):
        aa, bb, cc = map(int, sys.stdin.readline().split())
        for val in (aa, bb): _x.add(val)
        _y.add(cc)
        horizontal[idx] = [aa, bb, cc]
    d = 0
    while d < M:
        dd, ee, ff = [int(i) for i in sys.stdin.readline().split()]
        _x.add(dd)
        for s in (ee, ff): _y.add(s)
        vertical[d] = [dd, ee, ff]
        d += 1

    lstx, lsty = sorted(list(_x)), sorted(list(_y))
    map_xi = {vx:k for k,vx in enumerate(lstx)}
    map_yi = {vy:k for k,vy in enumerate(lsty)}
    X_LEN = len(lstx)*2 - 1
    Y_LEN = len(lsty)*2 - 1
    g = [[0]*Y_LEN for _ in range(X_LEN)]

    rangex = [0]*X_LEN
    rangey = [0]*Y_LEN
    rangex[0] = rangex[-1] = INF
    rangey[0] = rangey[-1] = INF

    idxsx = idxsy = None
    for i, (low, hi) in enumerate(zip(lstx, lstx[1:])):
        rangex[i*2 + 1] = hi - low
        if low <= 0 <= hi: idxsx = i*2 + 1
    for j, (start, end) in enumerate(zip(lsty, lsty[1:])):
        rangey[j*2 + 1] = end - start
        if start <= 0 <= end: idxsy = j*2 + 1

    for h in horizontal:
        yv = map_yi[h[2]]*2
        xL = map_xi[h[0]]*2+1
        xR = map_xi[h[1]]*2+1
        for xx in range(xL, xR, 2): g[xx][yv] = 1

    for v in vertical:
        xv = map_xi[v[0]]*2
        yL = map_yi[v[1]]*2+1
        yR = map_yi[v[2]]*2+1
        for yy in range(yL, yR, 2): g[xv][yy] = 1

    Q = deque()
    pointer = lambda : [idxsx, idxsy]
    ans = rangex[idxsx]*rangey[idxsy]
    Q.append(pointer())
    g[idxsx][idxsy] = 1

    def step(): return Q.pop() if Q else None

    while Q:
        coor = step()
        if not coor: break
        xi, yi = coor
        for fi, _unused in enumerate((0,1,2,3)):
            nxtx, nxty = xi + v1[fi], yi + v2[fi]
            if not g[nxtx][nxty]:
                nxtx += v1[fi]
                nxty += v2[fi]
                if not g[nxtx][nxty]:
                    g[nxtx][nxty] = 1
                    Q.appendleft([nxtx, nxty])
                    ans += rangex[nxtx]*rangey[nxty]
                    if ans >= INF:
                        print("INF")
                        return
    print(ans)

if __name__=='__main__': process()