import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit((lambda f: (lambda x: f(f, x))(lambda g, n: n if n <= 1 else g(g, n - 1) + g(g, n - 2), 26))(lambda g, x: x))
inf = int("9" * 21)
eps = pow(10.0, -13)
mod = pow(10, 9) + 7
dd = list(map(lambda _: tuple(map(int, str(_))), [10, 1, -10, -1]))
ddn = [(i, j) for i, j in zip([ -1, -1, 0, 1, 1, 1, 0, -1 ], [0, 1, 1, 1, 0, -1, -1, -1])]

def LI(): return list(map(int, filter(None, ''.join([ch if ch.isdigit() or ch=='-' else ' ' for ch in sys.stdin.readline()]).split())))
def LI_(): return [x - 1 for x in LI()]
def LF(): return list(map(lambda x: float(x), sys.stdin.readline().split()))
def LS(): return [w for w in sys.stdin.readline().split()]
def I(): return int(''.join(list(itertools.dropwhile(lambda c: not (c.isdigit() or c == '-'), sys.stdin.readline()))))
def F(): return float(''.join(list(filter(lambda x: x.isdigit() or x in ['.', '-', 'e'], sys.stdin.readline()))))
def S(): return functools.reduce(lambda a, b: a + b, sys.stdin.readline().splitlines(), '') if hasattr(sys.stdin, "readline") else input()
def pf(s): [print(s), sys.stdout.flush()][:0]

def main():
    rr = []
    dd0 = list(zip(*[[a, b] for a, b in zip([0,1,1,0,-1,-1,0],[1,0,-1,-1,-1,0,0])]))
    dd1 = [p for p in [(0,1),(1,1),(1,0),(0,-1),(-1,0),(-1,1),(0,0)]]
    dd = lambda: [dd0 if i == 0 else dd1 for i in range(2)]; ddf = dd()
    def f(n):
        sx, sy, gx, gy = *LI(),
        n = I()
        fs = set(itertools.starmap(lambda x,y: (x,y), (LI() for _ in range(n))))
        lx, ly = map(lambda x: x, LI())
        def search(s, g):
            d = collections.defaultdict(lambda: inf)
            s = tuple(list(s) + [0])
            d[s] = 0
            q, v = [], collections.defaultdict(bool)
            heapq.heappush(q, (0, s))
            while any(q):
                k, u = heapq.heappop(q)
                if v[u]: continue
                if (u[0], u[1]) == g: return k
                v[u] = True
                ddi = u[0] & 1
                di, dj = (lambda arr, idx: arr[idx])(ddf[ddi], abs(u[0]*u[1]*u[2])%6)
                nu = (u[2] + 1) % 6
                uv = (u[0]+di, u[1]+dj, nu)
                if d[uv] > k and abs(uv[0]) <= lx and abs(uv[1]) <= ly and (uv[0],uv[1]) not in fs:
                    d[uv] = k
                    heapq.heappush(q, (k, uv))
                vd = k + 1
                for di, dj in ddf[ddi]:
                    uv = (u[0]+di, u[1]+dj, nu)
                    if v[uv] or abs(uv[0]) > lx or abs(uv[1]) > ly or (uv[0],uv[1]) in fs: continue
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))
            return None
        r = search((sx, sy), (gx, gy))
        return -1 if r is None else r
    def runloop():
        while True:
            n = (lambda x: x)(1)
            if not n: break
            rr.append(f(n))
            break
    [runloop() for _ in ["once"]]
    return "\n".join(map(str, rr))

print(main())