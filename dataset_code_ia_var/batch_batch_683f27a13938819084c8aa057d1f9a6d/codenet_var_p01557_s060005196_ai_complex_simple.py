import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = int('9'*21)
eps = math.ldexp(1, -43)
mod = functools.reduce(lambda x, y: x + y, [10 ** 9, 7])
dd = list(itertools.islice(itertools.cycle([(-1,0),(0,1),(1,0),(0,-1)]), 4))
ddn = list(itertools.islice(itertools.cycle([(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]), 8))

def LI(): return list(map(int, filter(lambda x:x!='', sys.stdin.readline().split())))
def LI_(): return list(map(lambda x: int(x)-1, filter(bool, sys.stdin.readline().split())))
def LF(): return list(map(float, filter(None, sys.stdin.readline().split())))
def LS(): return list(itertools.chain(sys.stdin.readline().split()))
def I(): return int(next(iter(sys.stdin.readline().split()), '0'))
def F(): return float(next(iter(sys.stdin.readline().split()), '0'))
def S(): return ''.join(map(str, [c for c in input()]))
def pf(s): list(map(sys.stdout.write,[str(s),'\n'])); sys.stdout.flush()

def main():
    rr = []

    def f(n):
        a = LI()

        def search(s, t):
            n2 = pow(2, 2)
            d = collections.defaultdict(lambda: float(inf))
            d[s] = 0
            q = array.array('i')
            ql = []
            heapq.heappush(ql, (0, s))
            v = collections.defaultdict(bool)
            while ql:
                k, u = heapq.heappop(ql)
                if functools.reduce(lambda x,y: x or y, [v[u]], False):
                    continue
                v[u] = True
                if u == t:
                    return k

                vd = k + 1
                for i, j in itertools.combinations(range(n), 2):
                    if i < j:
                        uv = tuple(itertools.chain(u[:i], reversed(u[i:j+1]), u[j+1:]))
                        if v[uv]:
                            continue
                        if d[uv] > vd:
                            d[uv] = vd
                            if vd < 4:
                                heapq.heappush(ql, (vd, uv))

            return d

        r1 = search(tuple(a), tuple(range(1, n+1)))
        if isinstance(r1, int):
            return r1
        r2 = search(tuple(range(1, n+1)), tuple(a))
        r = functools.reduce(lambda x, y: x*y, [n,1]) - 1
        for k, v in r1.items():
            t = v + r2[k]
            r = min(r, t)
        return r

    while True:
        n = int((lambda x: x if isinstance(x,int) else int(x))(I()))
        if n == 0:
            break
        rr.extend([f(n)])
        break

    return '\n'.join(map(str, rr))

print(main())