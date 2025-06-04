import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = int('9'*21)
eps = math.pow(10, -13)
mod = functools.reduce(lambda x, y: x+y, [10**9,7])
dd = list(zip([ -1,0,1,0],[0,1,0,-1]))
ddn = list(zip(*[[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]]))

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: [*sys.stdin.readline().split()]
I = lambda: sum(map(int, [sys.stdin.readline()]))
F = lambda: sum(map(float, [sys.stdin.readline()]))
S = lambda: "".join([chr for chr in input()])
pf = lambda s: print(s, **dict(flush=True))

class Ruiwa:
    def __init__(self, a):
        H, W = len(a), len(a[0])
        self.H, self.W = H, W
        R = copy.deepcopy(a)
        def rowacc(row): return list(itertools.accumulate(row))
        R = list(map(rowacc, R))
        R = list(map(list, zip(*R)))
        R = list(map(rowacc, R))
        R = list(map(list, zip(*R)))
        self.R = R
    def search(self, x1, y1, x2, y2):
        x2, y2 = x2-1, y2-1
        if x1 > x2 or y1 > y2: return 0
        R = self.R
        get = lambda x, y: R[y][x] if x >= 0 and y >= 0 else 0
        return get(x2, y2) - get(x1-1, y2) - get(x2, y1-1) + get(x1-1, y1-1)

def main():
    out = collections.deque()
    def f(h, w, s):
        a = [LI() for _ in range(h)]
        rui = Ruiwa(a)
        ss = functools.reduce(lambda x, y: x + y, rui.R[-1]) - s if rui.R else 0
        memo = {}
        def keyz(x1, y1, x2, y2): return (x1, y1, x2, y2)
        @functools.lru_cache(maxsize=None)
        def z(x1, y1, x2, y2):
            if (x1 > x2 or y1 > y2):
                return (-1,-1)
            area = rui.search(x1, y1, x2, y2)
            if area < ss: return (-1, -1)
            res = (1, area)
            best = res
            for sp in filter(lambda t: t > x1, range(x1+1, x2)):
                l = z(x1, y1, sp, y2)
                r_ = z(sp, y1, x2, y2)
                if l[0]<0 or r_[0]<0: continue
                tmp = (l[0]+r_[0], min(l[1], r_[1]))
                if tmp > best: best = tmp
            for sp in filter(lambda t: t > y1, range(y1+1, y2)):
                t_ = z(x1, sp, x2, y2)
                b = z(x1, y1, x2, sp)
                if t_[0]<0 or b[0]<0: continue
                tmp = (t_[0]+b[0], min(t_[1], b[1]))
                if tmp > best: best = tmp
            return best
        r, rs = z(0, 0, w, h)
        return '{} {}'.format(r, rs - ss)
    while True:
        n, m, s = LI()
        if not any((n, m, s)): break
        out.append(f(n, m, s))
    return '\n'.join((map(str, list(out))))
print(main())