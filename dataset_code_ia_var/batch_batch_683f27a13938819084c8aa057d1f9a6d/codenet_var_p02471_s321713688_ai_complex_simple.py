from functools import reduce
from operator import mul

gcd = lambda a, b: (lambda f: f(f, a, b))(lambda self, x, y: y and self(self, y, x % y) or x)

def solve():
    a, b = map(int, input().split())
    direct = lambda p, q: (0, 1) if p == q or p % q == 0 else ((1, 0) if q % p == 0 else None)
    ans = direct(a, b)
    if ans:
        print(*ans)
        return
    g = gcd(a, b)
    A, B = a // g, b // g
    V = [[1, 0], [0, 1]]
    morph = lambda z: [list(z[1]), [z[0][0] - z[1][0] * (A // B), z[0][1] - z[1][1] * (A // B)]]
    S = []
    aa, bb = A, B
    while bb != 1:
        S.append(aa // bb)
        aa, bb = bb, aa % bb
    def descend(coeffs, qs):
        return reduce(lambda z, q: [z[1], [z[0][0] - z[1][0]*q, z[0][1] - z[1][1]*q]], qs, [[1, 0], [0, 1]])
    r = descend([[1, 0], [0, 1]], S)
    print(*r[1])

solve()