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
    oks = collections.defaultdict(set)

    def a2k(a, n):
        r = 0
        for i in range(n):
            for j in range(n):
                r *= 3
                r += a[i][j]
        return r

    def k2a(k, n):
        a = []
        for i in range(n):
            t = []
            for j in range(n):
                t.append(k%3)
                k //= 3
            a.append(t[::-1])
        return a

    def moves(a,n):
        si = sj = -1
        for i in range(n):
            for j in range(n):
                if a[i][j] == 2:
                    si = i
                    sj = j
                    break
            if si >= 0:
                break

        r = set()
        a[si][sj] = 0
        for i in range(max(0,si-1), min(n,si+2)):
            for j in range(max(0,sj-1), min(n,sj+2)):
                if a[i][j] != 0 or (si == i and sj == j):
                    continue
                a[i][j] = 2
                na = [[0]*n for _ in range(n)]
                zf = 1
                for k in range(n):
                    for l in range(n):
                        if a[k][l] == 2:
                            continue
                        c = 0
                        for m in range(max(0, k-1), min(n, k+2)):
                            for o in range(max(0, l-1), min(n, l+2)):
                                if m == k and o == l:
                                    continue
                                if a[m][o] > 0:
                                    c += 1
                        if (a[k][l] == 0 and c == 3) or (a[k][l] == 1 and 2 <= c <= 3):
                            na[k][l] = 1
                            zf = 0
                na[i][j] = 2
                if zf == 1:
                    return 'ok'
                r.add(a2k(na, n))
                a[i][j] = 0
        return r

    def f(n):
        sd = {}
        sd['.'] = 0
        sd['#'] = 1
        sd['@'] = 2
        a = [[sd[c] for c in S()] for _ in range(n)]
        zf = 1
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    zf = 0
                    break
        if zf == 1:
            return 0
        r = inf
        d = collections.defaultdict(lambda: inf)
        k = a2k(a,n)
        q = set([k])
        d[k] = 0
        t = 0
        while q:
            t += 1
            nq = set()
            if q & oks[n]:
                return t
            for k in q:
                a = k2a(k,n)
                r = moves(a,n)
                if r == 'ok':
                    oks[n].add(k)
                    return t
                for nk in r:
                    if d[nk] > t:
                        d[nk] = t
                        nq.add(nk)
            q = nq
        return -1

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))

print(main())