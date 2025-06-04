import sys
from heapq import heapify, heappush, heappop

w = sys.stdout.write
r = sys.stdin.readline

def buildSegmentTree(arr, n, dat, lz, L0, L1, N0):
    # Imperative style
    for idx in range(n):
        dat[N0-1+idx] = arr[idx]
    for idx in range(N0):
        L0[N0-1+idx] = L1[N0-1+idx] = idx
    for idx in range(N0-2, -1, -1):
        dat[idx] = min(dat[2*idx+1], dat[2*idx+2])
        L0[idx] = L0[2*idx+1]
        L1[idx] = L1[2*idx+2]

def gindex(l, r, N0, LV):
    # Generator-based
    L = (l + N0) >> 1
    R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1
        R >>= 1

def doPropagate(*ids, dat, lz):
    # Classic for, procedural
    for i in reversed(ids):
        v = lz[i - 1]
        if v == 0: continue
        lz[2*i-1] += v
        lz[2*i] += v
        dat[2*i-1] += v
        dat[2*i] += v
        lz[i-1] = 0

def setUpdate(l, r, x, N0, dat, lz, LV):
    # More functional-ish & for/while mixed, calls generator
    myids = tuple(gindex(l, r, N0, LV))
    doPropagate(*myids, dat=dat, lz=lz)
    L = N0 + l
    R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lz[R-1] += x; dat[R-1] += x
        if L & 1:
            lz[L-1] += x; dat[L-1] += x
            L += 1
        L >>= 1
        R >>= 1
    for i in myids:
        dat[i-1] = min(dat[2*i-1], dat[2*i])

def segmentQuery(r, N0, dat, lz, L0, L1, LV):
    # Oldschool for/else, object/array access style
    ids = tuple(gindex(0, r, N0, LV))
    doPropagate(*ids, dat=dat, lz=lz)
    R = N0 + r
    while R:
        if R & 1:
            R -= 1
            if dat[R-1] < 2:
                l0 = L0[R-1]
                r0 = L1[R-1]+1
                break
        R >>= 1
    else:
        return 0
    k = R-1
    while k < N0-1:
        v = lz[k]
        if v:
            lz[2*k+1] += v
            lz[2*k+2] += v
            dat[2*k+1] += v
            dat[2*k+2] += v
            lz[k] = 0
        if dat[2*k+2] < 2:
            l0 = (l0 + r0) >> 1
            k = 2*k+2
        else:
            r0 = (l0 + r0) >> 1
            k = 2*k+1
    return r0

def main():
    params = r().split(); N = int(params[0]); Q = int(params[1])
    INF = 2**31-1
    LV = (N-1).bit_length()
    N0 = 1 << LV
    dat = [0] * (2*N0)
    lz = [0] * (2*N0)
    L0 = [0] * (2*N0)
    L1 = [0] * (2*N0)

    s = list(map("()".index, r().strip()))
    a = [0]*N
    C = [0]*N
    que = []
    curr = 0
    idx = 0
    # Some C-style indexing, imperative
    while idx < N:
        if s[idx]:
            que.append(idx)
            C[idx] = 1
            curr -= 1
        else:
            curr += 1
        a[idx] = curr
        idx += 1
    heapify(que)
    buildSegmentTree(a, N, dat, lz, L0, L1, N0)
    # Using classic indexed for, some procedural flavor
    for _ in range(Q):
        q = int(r())
        qv = q-1
        if s[qv] == 0:
            # Remove invalid
            while que and s[que[0]] == 0:
                C[heappop(que)] = 0
            if not que or qv <= que[0]:
                w("%d\n" % q)
            else:
                k = heappop(que)
                C[k] = 0
                s[k] = 0
                s[qv] = 1
                heappush(que, qv)
                w("%d\n" % (k+1))
                setUpdate(k, qv, 2, N0, dat, lz, LV)
        else:
            v = segmentQuery(qv, N0, dat, lz, L0, L1, LV)
            if v == qv:
                w("%d\n" % q)
            else:
                s[v] = 1
                s[qv] = 0
                if C[v] == 0:
                    heappush(que, v)
                    C[v] = 1
                w("%d\n" % (v+1))
                setUpdate(v, qv, -2, N0, dat, lz, LV)
main()