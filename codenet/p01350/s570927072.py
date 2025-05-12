import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    rr = []

    def f():
        n = I()
        r,t = LF()
        a = [LI() for _ in range(n)]
        d = {}
        M = 32
        for i in range(n):
            ax,ay = a[i]
            for j in range(n):
                if i == j:
                    continue
                bx,by = a[j]
                d[i*M+j] = math.atan2(bx-ax,by-ay) / math.pi * 180
        ky = {}
        for i in range(n):
            ax,ay = a[i]
            for j in range(n):
                bx,by = a[j]
                ky[i*M+j] = pow(pow(ax-bx, 2) + pow(ay-by, 2), 0.5)
        e = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ij = i*M+j
                dij = d[ij]
                for k in range(n):
                    if k == j:
                        continue
                    jk = j*M+k
                    djk = d[jk]
                    if abs(dij-djk) <= t or 360 - abs(dij-djk) <= t:
                        e[(i,j)].append(((j,k), ky[jk]))

        def search():
            res = 0
            dp = [[None]*n for _ in range(n)]
            for j in range(1, n):
                k = ky[j]
                if k > r:
                    continue
                s = (j,1)
                res = 1
                dp[0][j] = k
            if res == 0:
                return 0
            while True:
                wf = False
                nd = [[None]*n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        if dp[i][j] is None:
                            continue
                        dij = dp[i][j]
                        for nn,k in e[(i,j)]:
                            nk = dij + k
                            if nk > r or (not nd[j][nn[1]] is None and nd[j][nn[1]] < nk):
                                continue
                            nd[j][nn[1]] = nk
                            wf = True
                if wf:
                    res += 1
                    dp = nd
                else:
                    break
            return res

        return search()

    while True:
        rr.append(f())
        break

    return '\n'.join(map(str,rr))

print(main())