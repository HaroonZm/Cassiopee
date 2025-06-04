def solve():
    import sys
    import itertools
    import functools
    from operator import mul
    z = lambda x, y: complex(x, y)
    def h(*p): return abs(p[0] - p[1])
    def Δ(a, b, c): return (a + b + c) / 2
    def s_area(a, b, c): 
        s = Δ(a, b, c)
        return (reduce(mul, (s, s - a, s - b, s - c)) if all(x > 0 for x in (a, b, c)) else 0) ** 0.5
    reduce = functools.reduce
    for line in iter(sys.stdin.readline, ''):
        vals = tuple(map(int, line.split()))
        if len(vals) < 6: continue
        if vals[0:4] == (0, 0, 0, 0): break
        pts = [z(*vals[i:i+2]) for i in (0, 2, 4)]
        a, b, c = (h(pts[i], pts[(i+1)%3]) for i in range(3))
        s = Δ(a, b, c)
        r = (s * (s - a) * (s - b) * (s - c))**0.5 / s if s else 0
        D = functools.reduce(lambda u, v: u+v,
            map(lambda i: [b, c][i] * pts[1+i], range(2))) / (b+c)
        BD = abs(D - pts[1])
        I = (BD * pts[0] + c * D) / (c + BD)
        sides = tuple(abs(pt - I) for pt in pts)
        def R(rx, s_, r_, sides_, skip):
            S = s_ + sides_[rx] - r_ - sum(sides_[(rx+j)%3] for j in [1,2])
            return r_ / 2 / (s_ - [a,b,c][rx]) * S if s_ - [a,b,c][rx] else 0
        print(*(R(i, s, r, sides, [a, b, c]) for i in range(3)))
solve()