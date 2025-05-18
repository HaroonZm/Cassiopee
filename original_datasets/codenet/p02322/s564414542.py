#!python3

iim = lambda: map(int, input().rstrip().split())
from heapq import heappush, heappop

def resolve():
    N, W = iim()
    S = [list(iim()) for i in range(N)]

    def f1(v, w, m):
        mm = []
        i = 1
        while i <= m:
            yield i
            m -= i
            i <<= 1

        if m:
            yield m
    SS = list(sorted(((v*i, w*i) for v, w, m in S for i in f1(v, w, m)), key=lambda x: (x[0]/x[1], x[1]), reverse=True))
    NN = len(SS)

    def ubound(v, w, i):
        for j in range(i, NN):
            vj, wj = SS[j]

            if w + wj > W:
                return (-v, -v - (W - w) * vj / wj)

            w += wj
            v += vj

        return (-v, -v)

    u0, u1 =  ubound(0, 0, 0)
    um = u0
    ans = 0

    q = []
    heappush(q, (u1, u0, 0, 0, 0))

    #print(S, NN)
    #print(W, SS)
    while q:
        #print(q)
        uq0, uq1, vq, wq, i = heappop(q)

        if uq0 > um:
            break

        if i >= NN: continue

        vi, wi = SS[i]
        if wq + wi < W:
            heappush(q, (uq0, uq1, vq+vi, wq+wi, i + 1))

        u0, u1 = ubound(vq, wq, i + 1)
        if u1 <= um:
            if u0 < um:
                um = u0
            heappush(q, (u1, u0, vq, wq, i + 1))

    print(-um)

if __name__ == "__main__":
    resolve()