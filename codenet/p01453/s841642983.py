import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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

def bs(f, mi, ma):
    st = time.time()
    mm = -1
    mi = fractions.Fraction(mi, 1)
    ma = fractions.Fraction(ma, 1)
    while ma > mi + eps:
        gt = time.time()
        mm = (ma+mi) / 2
        if gt - st > 35:
            return mm
        if isinstance(mm, float):
            tk = max(1, int(10**15 / mm))
            mm = fractions.Fraction(int(mm*tk), tk)
        if float(mm) == float(ma) or float(mm) == float(mi):
            return mm
        if f(mm):
            mi = mm
        else:
            ma = mm
    if f(mm):
        return mm + eps
    return mm

def main():
    rr = []

    def f(w,h):
        a = [S() for _ in range(h)]
        si = sj = -1
        for i in range(1,h-1):
            for j in range(1,w-1):
                if a[i][j] == 's':
                    si = i
                    sj = j
                    break

        def search(sc):
            d = collections.defaultdict(lambda: inf)
            q = []
            for i in range(1,h-1):
                for j in range(1,w-1):
                    if a[i][j] == sc:
                        d[(i,j)] = 0
                        heapq.heappush(q, (0, (i,j)))

            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for di,dj in dd:
                    ni = u[0] + di
                    nj = u[1] + dj
                    if not a[ni][nj] in '.s':
                        continue
                    uv = (ni,nj)
                    if v[uv]:
                        continue
                    vd = k + 1
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        gd = search('g')
        wd = search('*')

        cgs = []
        cws = []
        for i in range(1,h-1):
            for j in range(1,w-1):
                if not a[i][j] in '.s':
                    continue
                if gd[(i,j)] >= inf:
                    cgs.append((i,j))
                else:
                    cws.append((i,j))
        cc = len(cgs) + len(cws)
        cgc = len(cgs)
        cgw = sum([wd[(i,j)] for i,j in cgs])

        sgw = [(inf,0,0)]
        for i,j in cws:
            gt = gd[(i,j)]
            wt = wd[(i,j)]
            sgw.append((gt-wt, wt, gt))
        sgw.sort()
        # print(sgw[:5], sgw[-5:])
        ls = len(sgw) - 1
        # print('ls', ls, len(cws))

        def ff(t):
            # print('ff', t)
            s = cgw
            si = bisect.bisect_left(sgw,(t,0,0))
            # print('si', si, sgw[si], sgw[si-1])
            tc = cgc
            s2 = cgw
            tc2 = tc + ls - si
            for i in range(si):
                s2 += sgw[i][2]
            for i in range(si,ls):
                s2 += sgw[i][1]

            # for i,j in cws:
            #     gt = gd[(i,j)]
            #     wt = wd[(i,j)]
            #     if t + wt < gt:
            #         s += wt
            #         tc += 1
            #     else:
            #         s += gt

            # print('s,s2,tc,tc2', s,s2,tc,tc2)

            av = (s2 + t*tc2) / cc
            # print('av,t', float(av), float(t))
            return t < av

        k = bs(ff, 0, 10**10)
        gt = gd[(si,sj)]
        wt = wd[(si,sj)]
        r = gt
        if wt + k < gt:
            r = wt + k
        # print('r', r)

        return '{:0.10f}'.format(float(r))

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        break

    return '\n'.join(map(str, rr))

print(main())