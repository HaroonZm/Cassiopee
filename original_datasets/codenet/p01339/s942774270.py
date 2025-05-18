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

    def f(n,m):
        a = [LI_() for _ in range(m)]
        p = collections.defaultdict(list)
        c = collections.defaultdict(list)
        for s,d in a:
            p[s].append(d)
            c[d].append(s)

        v = collections.defaultdict(int)
        d = collections.defaultdict(lambda: -1)
        b = collections.defaultdict(set)
        def _f(i):
            # print('_f',i)
            if v[i] == 2:
                return -1
            if v[i] == 1:
                d[i] = i
                b[i].add(i)
                return i
            v[i] = 1
            for j in p[i]:
                r = _f(j)
                if r < 0:
                    continue
                d[i] = r
                b[r].add(i)
            v[i] = 2
            if d[i] == i:
                return -1
            return d[i]

        for i in range(n):
            _f(i)

        def g(i):
            # print('g',i)
            if d[i] >= 0 and d[i] != i:
                return 1
            cs = set(c[i])
            if d[i] == i:
                for j in b[i]:
                    cs |= set(c[j])
            r = 1
            # print('cs',i,cs)
            for j in cs:
                if j in b[i]:
                    continue
                gr = g(j)
                # print('jgr',j,gr)
                r *= gr
                r %= mod
            r += 1
            return r

        r = 1
        for i in range(n):
            if d[i] == i or len(p[i]) == 0:
                gr = g(i)
                # print('igr',i,gr)
                r *= gr
                r %= mod

        return r

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        break

    return '\n'.join(map(str, rr))

print(main())