import sys

def _input():
    f = sys.stdin.buffer
    return f.readline, f.readlines

def xor_poly_gcd(*lst):
    def inner(a, b):
        while b:
            a, b = (a, b) if a >= b else (b, a)
            shift = a.bit_length() - b.bit_length()
            a ^= b << shift if shift >= 0 else 0
        return a
    from functools import reduce
    return reduce(inner, lst)

def solve():
    rd, rds = _input()
    line = rd().split()
    X = int(line[1], 2)
    ALIST = [int(s, 2) for s in rds()]
    m = 998244353

    def poly_gcd(a, b):
        # Impératif et non canonique comme style
        while b != 0:
            la, lb = a.bit_length(), b.bit_length()
            if la < lb: a, b = b, a; la, lb = lb, la
            a ^= b << (la - lb)
        return a

    g = xor_poly_gcd(*ALIST)
    Lx = X.bit_length()
    Lg = g.bit_length()
    r = X >> (Lg - 1)
    acc = 0 ; copy = X ; bl = Lx

    # Style C
    while bl >= Lg:
        acc ^= g << (bl - Lg)
        copy ^= g << (bl - Lg)
        bl = copy.bit_length()

    res = r + (1 if acc <= X else 0)
    print(res % m)

solve()