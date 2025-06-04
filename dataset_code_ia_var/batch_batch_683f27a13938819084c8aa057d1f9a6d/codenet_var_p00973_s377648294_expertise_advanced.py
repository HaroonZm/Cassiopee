from decimal import Decimal, getcontext
from fractions import Fraction
import math
import os
import sys
from functools import lru_cache, reduce
from itertools import islice

getcontext().prec = 60  # Set high precision for Decimal

DEBUG = 'DEBUG' in os.environ

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return list(map(int, inp().split()))

class Vec:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):  return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):  return Vec(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar): return Vec(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar):return Vec(scalar * self.x, scalar * self.y)
    def __truediv__(self, scalar): return Vec(self.x / scalar, self.y / scalar)
    def __neg__(self): return Vec(-self.x, -self.y)
    def __eq__(self, other): return (self.x, self.y) == (other.x, other.y)
    def __hash__(self): return hash(('Vec', self.x, self.y))
    def dot(self, other): return self.x * other.x + self.y * other.y
    def cross(self, other): return self.x * other.y - self.y * other.x
    def abs2(self): return self.x * self.x + self.y * self.y
    def __abs__(self): return float(self.abs2()) ** 0.5
    def __str__(self): return f'({self.x}, {self.y})'
    def __repr__(self): return f'Vec({self.x!r}, {self.y!r})'

def sgn(v):
    return (v > 0) - (v < 0)

EPS = Fraction(1, 10**26)

def solve_poly(poly, minx, maxx):
    poly = poly[:]
    while poly and poly[-1] == 0: poly.pop()
    if len(poly) <= 1: return []
    if len(poly) == 2:
        b, a = poly
        try:
            x = Fraction(-b, a)
            if minx <= x <= maxx:
                return [(x, x)]
        except ZeroDivisionError:
            pass
        return []
    df = [i * poly[i] for i in range(1, len(poly))]
    segs = [(minx, None)] + solve_poly(df, minx, maxx) + [(None, maxx)]
    def f(x):
        return sum(a * (x ** i) for i,a in enumerate(poly))
    sols = []
    for i in range(len(segs)-1):
        lb, ub = segs[i][0], segs[i+1][1]
        if lb is None or ub is None: continue
        lbs, ubs = sgn(f(lb)), sgn(f(ub))
        if (lbs >= 0 and ubs >= 0) or (lbs < 0 and ubs < 0): continue
        orig_lb, orig_ub = lb, ub
        for _ in range(200):
            if ub - lb <= EPS: break
            midf = (lb + ub)/2
            mid = Fraction(Decimal(midf.numerator)/Decimal(midf.denominator))
            if not (lb < mid < ub): mid = midf
            v = f(mid)
            if (v >= 0 and lbs >= 0) or (v < 0 and lbs < 0):
                lb = mid
            else:
                ub = mid
        sols.append((lb, ub))
    return sols

def solve(N, Points):
    dprint('polygon({!r}, fill=False)'.format([(v.x, v.y) for v in Points]))
    total_area_2 = sum(
        (Points[i] - Points[0]).cross(Points[i+1] - Points[i])
        for i in range(1, N-1)
    )
    total_area_4 = 0
    bi, bk, bv = -1, None, None
    for i in range(1, N-1):
        a = Points[i] - Points[0]
        b = Points[i+1] - Points[i]
        area_4 = a.cross(b) * 2
        if total_area_4 + area_4 <= total_area_2:
            total_area_4 += area_4
            continue
        rest = total_area_2 - total_area_4
        k = Fraction(rest, area_4)
        assert 0 <= k < 1
        bi, bk = i, k
        bv = Points[i] + k * (Points[i+1] - Points[i])
        dprint('bi =', bi, 'bk =', bk, 'bv =', bv)
        break
    assert bi != -1
    ai, ak = 0, 0
    maxl = minl = (bv - Points[0]).abs2()
    while bi != 0:
        assert 0 <= ak < 1 and 0 <= bk < 1
        dprint('***\nai =', ai, 'ak =', ak, 'bi =', bi, 'bk =', bk)
        dprint('minl =', minl, 'maxl =', maxl)
        a0, a1 = Points[ai], Points[(ai+1)%N]
        b0, b1 = Points[bi], Points[(bi+1)%N]
        a2 = a0 + ak * (a1 - a0)
        b2 = b0 + bk * (b1 - b0)
        dprint('a0 =', a0, 'a1 =', a1, 'a2 =', a2)
        dprint('b0 =', b0, 'b1 =', b1, 'b2 =', b2)
        al, cross = 1, (b2 - a1).cross(b1 - b0)
        if cross:
            bl = Fraction((b0 - a2).cross(b2 - a1), cross)
        else:
            bl = 2
        assert bk < bl
        if bl > 1:
            al = Fraction((b2 - a0).cross(b1 - a2), (a1 - a0).cross(b1 - a2))
            bl = 1
        assert ak < al <= 1 and bk < bl <=1
        a3 = a0 + al * (a1 - a0)
        b3 = b0 + bl * (b1 - b0)
        dprint('a3 =', a3, 'b3 =', b3)
        b3a3 = b3 - a3
        l = b3a3.abs2()
        dprint('l =', l)
        maxl, minl = max(maxl, l), min(minl, l)
        a3a2 = a3 - a2
        b3b2 = b3 - b2
        b2a2 = b2 - a2
        A0 = a3a2.cross(b2a2)
        B0 = b2a2.cross(b3b2)
        aden = getattr(A0, 'denominator', 1)
        bden = getattr(B0, 'denominator', 1)
        gden = aden * bden // math.gcd(aden, bden)
        A0, B0 = int(A0 * gden), int(B0 * gden)
        g = math.gcd(abs(A0), abs(B0)) if (A0 or B0) else 1
        A0 //= g
        B0 //= g
        dprint('y = ({}) * x / (({}) - ({}) * x)'.format(A0, B0, B0-A0))
        if A0 == B0:
            X2 = (a3a2 - b3b2).abs2()
            X1 = -2 * b2a2.dot(a3a2 - b3b2)
            C = b2a2.abs2()
            dprint('L = ({}) * x^2 + ({}) * x + ({})'.format(X2, X1, C))
            x = Fraction(-X1, 2*X2) if X2 else Fraction(0,1)
            dprint('x =', x)
            if 0 <= x <= 1:
                l = x*(X1 + x*X2) + C
                dprint('l =', l)
                minl = min(minl, l)
        else:
            X2 = a3a2.abs2()
            X1 = 2*(-b2a2.dot(a3a2) + Fraction(A0, B0-A0) * a3a2.dot(b3b2))
            Y2 = b3b2.abs2()
            Y1 = 2*(b2a2.dot(b3b2) - Fraction(B0, B0-A0)*a3a2.dot(b3b2))
            L0 = b2a2.abs2()
            def calc_l(x, y):
                return x*(X1 + x*X2) + y*(Y1 + y*Y2) + L0
            A = Fraction(A0, B0-A0)
            B = Fraction(B0, B0-A0)
            poly = [
                -2*A*A*B*B*Y2,
                -A*B*(2*A*Y2 - Y1),
                0,
                2*B*X2 + X1,
                2*X2
            ]
            dprint('poly =', poly)
            sols = solve_poly(poly, -B, 1-B)
            dprint('sols =', sols)
            for sol_low, sol_high in sols:
                x0, x1 = sol_low+B, sol_high+B
                y0 = Fraction(-A*B, x0-B) - A
                y1 = Fraction(-A*B, x1-B) - A
                l0 = calc_l(x0, y0)
                l1 = calc_l(x1, y1)
                dprint('l0 =', l0, 'l1 =', l1)
                minl = min(minl, l0, l1)
        ak, bk = al, bl
        if ak == 1:
            ai = (ai + 1) % N
            ak = 0
        if bk == 1:
            bi = (bi + 1) % N
            bk = 0
    dprint('minl', minl)
    dprint('maxl', maxl)
    minld = Decimal(minl.numerator) / Decimal(minl.denominator) if isinstance(minl, Fraction) else Decimal(minl)
    maxld = Decimal(maxl.numerator) / Decimal(maxl.denominator) if isinstance(maxl, Fraction) else Decimal(maxl)
    return minld.sqrt(), maxld.sqrt()

def main():
    N = read_int()
    A = [Vec(*read_ints()) for _ in range(N)]
    print(*(solve(N, A)), sep='\n')

if __name__ == '__main__':
    main()