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

    def f(n):
        a = [LS() for _ in range(n)]
        sn = {}
        for i in range(n):
            sn[a[i][0]] = i
        b = []
        bs = {}
        bb = {}
        kr = int(a[0][1])
        for i in range(1, n):
            ai = a[i]
            if a[0][0] in ai[3:]:
                continue
            if ai[2] == '0':
                kr += int(ai[1])
                continue
            b.append([2**sn[ai[0]],int(ai[1]), sum(map(lambda x: 2**sn[x],ai[3:]))])
            bs[b[-1][0]] = b[-1][-1]
            bb[b[-1][0]] = b[-1][1]

        fm = {}
        def _f(i):
            if i == 0:
                return 0
            if i in fm:
                return fm[i]
            r = 0
            si = 0
            kr = 0
            nsi = 0
            while i > si:
                ti = i - si
                ni = ti - (ti & (ti-1))
                si += ni
                if (bs[ni] & i) == 0:
                    nsi += ni
                    kr += bb[ni]

            si = nsi
            while i > si:
                ti = i - si
                ni = ti - (ti & (ti-1))
                nr = bb[ni]
                si += ni
                nr += _f(i - nsi - ni - (i & bs[ni]))
                if r < nr:
                    r = nr

            fm[i] = r + kr
            return r + kr

        r = 0
        l = len(b)
        l2 = l//2
        ii = [b[i][0] for i in range(l2)]
        ab = sum(map(lambda x: x[0], b))
        anb = sum(map(lambda x: x[0], b[l2:]))
        # print('ii',ii)
        # print('b',b)
        # print('bb',bb)
        # print('bs',bs)
        # return _f(anb)
        for i in range(l2+1):
            for ia in itertools.combinations(ii, i):
                ti = sum(ia)
                tf = False
                tr = 0
                ts = 0
                for j in ia:
                    if bs[j] & ti:
                        tf = True
                        break
                    tr += bb[j]
                    ts |= bs[j]
                if tf:
                    continue
                # print('tr',tr)
                tr += _f(anb - (anb & ts))
                # print('i',i,ti,tr,ts)
                if r < tr:
                    r = tr

        return r + kr

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print(n, rr[-1])

    return '\n'.join(map(str, rr))

print(main())