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

eps = 1e-4
def bsa(f, mi, ma):
    mm = -1
    while ma > mi + eps:
        mm = (ma+mi) / 2.0
        if f(mm):
            mi = mm + eps
        else:
            ma = mm
    if f(mm):
        return mm + eps
    return mm

def main():
    rr = []

    def f(w,h):
        a = [['.'] * (w+2)] + [['.'] + [c for c in S()] + ['.'] for _ in range(h)] + [['.'] * (w+2)]
        sf = [[None]*(w+2) for _ in range(h+1)] + [[0] * (w+2)]
        bs = []
        bi = 0
        for i in range(1,h+1):
            for j in range(1,w+1):
                if sf[i][j] or a[i][j] == '.':
                    continue
                bi += 1
                c = a[i][j]
                q = []
                q.append((i,j))
                sf[i][j] = bi
                qt = 0
                while len(q) > qt:
                    qi,qj = q[qt]
                    qt += 1
                    for di,dj in dd:
                        ni = qi + di
                        nj = qj + dj
                        if sf[ni][nj] or a[ni][nj] != c:
                            continue
                        sf[ni][nj] = bi
                        q.append((ni,nj))
                bs.append(q)

        # print('\n'.join(' '.join(map(lambda x: '.' if x is None else str(x), _)) for _ in sf))
        def _f(i):
            l = inf
            r = -inf
            bt = set()
            tt = set()
            bi = bs[i-1]
            wd = collections.defaultdict(int)
            for si,sj in bi:
                wd[sj] += 1
                c = sf[si+1][sj]
                if not c is None and c != i:
                    bt.add(c)
                    if l > sj:
                        l = sj
                    if r < sj:
                        r = sj
                c = sf[si-1][sj]
                if not c is None and c != i:
                    tt.add(c)
            if len(bt) != 1:
                return
            for ti in tt:
                td = _f(ti)
                if td is None:
                    return
                for k in td.keys():
                    wd[k] += td[k]
            def __f(j):
                w = 0
                for k in wd.keys():
                    w += (k-j) * wd[k]
                # print('jw',j,w)
                return w > 0

            w = bsa(__f, 0, 11) + 0.5
            # print('lr',l,r)
            # print(i,wd)
            # print(i,w)
            if w < l + eps*10 or w > r + 1 - eps*10:
                return
            return wd

        bti = -1
        for j in range(1,w+1):
            if sf[-2][j]:
                bti = sf[-2][j]
        # print('bti', bti)
        r = _f(bti)
        if r is None:
            return 'UNSTABLE'
        return 'STABLE'

    while 1:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())