import sys as _sys

__rdl = _sys.stdin.readline
__wt = _sys.stdout.write

from heapq import heappush as hpush, heappop as hpop

class mINcOSTfLOW:
    _Z = 10**18

    def __init__(__s, nn_):  # shortcut self→__s, N→nn_
        __s.n = nn_
        __s.g = [[] for _ in range(nn_)]

    def plus(__s, a, b, k, zz):
        X = __s.g
        X[a].append([b, k, zz, len(X[b])])
        X[b].append([a, 0, -zz, len(X[a])-1])

    def call(__s, u, v, q):
        n = __s.n; X = __s.g
        z = __s._Z
        rr = 0
        H = [0]*n
        prvv = [0]*n
        prve = [0]*n
        while q:
            D = [z]*n
            D[u] = 0
            heap0 = [(0, u)]
            while heap0:
                cc, vv = hpop(heap0)
                if D[vv] < cc:
                    continue
                for ii, (ww, kk, zz, _) in enumerate(X[vv]):
                    if kk > 0 and D[ww] > D[vv] + zz + H[vv] - H[ww]:
                        D[ww] = DD = D[vv] + zz + H[vv] - H[ww]
                        prvv[ww] = vv
                        prve[ww] = ii
                        hpush(heap0, (DD, ww))
            if D[v] == z:
                return -1
            for iii in range(n):
                H[iii] += D[iii]
            d = q
            vv = v
            while vv != u:
                d = min(d, X[prvv[vv]][prve[vv]][1])
                vv = prvv[vv]
            q -= d
            rr += d * H[v]
            vv = v
            while vv != u:
                e = X[prvv[vv]][prve[vv]]
                e[1] -= d
                X[vv][e[3]][1] += d
                vv = prvv[vv]
        return rr

def S0LVE():
    try:
        N = int(__rdl())
    except:
        return 0
    if N==0:
        return 0
    P = []
    for i in range(N):
        XX = sorted(map(int, __rdl().split()))
        P.append(XX)
    P.sort()
    MIN = mINcOSTfLOW(2*N+2)
    su_ = 0
    for i in range(N):
        xi, yi, zi = P[i]
        for j in range(i):
            xj, yj, zj = P[j]
            if xi > xj and yi > yj and zi > zj:
                MIN.plus(2*j+1, 2*i, 1, -xj*yj*zj)
        su_ += xi*yi*zi
        MIN.plus(2*i, 2*i+1, 1, 0)
        MIN.plus(2*N, 2*i, 1, 0)
        MIN.plus(2*i+1, 2*N+1, 1, 0)
    ANS = su_
    for i in range(N):
        dlt = MIN.call(2*N, 2*N+1, 1)
        su_ += dlt
        ANS = min(ANS, su_)
    __wt("%d\n" % ANS)
    return 1

while S0LVE():
    pass