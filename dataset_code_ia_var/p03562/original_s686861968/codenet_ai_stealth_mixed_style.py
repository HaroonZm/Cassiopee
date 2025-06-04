import sys
_ = sys.stdin.buffer
read_all = _.read
next_line = _.readline
data_lines = _.readlines

from functools import reduce as _reduce

# Entrelacement des styles et noms variables
MODULO = 998244353

def xor_poly_gcd(x, y):
    for __ in range(1000):  # style C-style loop
        if not y:
            return x
        lx, ly = x.bit_length(), y.bit_length()
        if lx < ly:
            x, y = y, x
            lx, ly = ly, lx
        x ^= y << (lx - ly)
    return x

# Parsing façon script/underscore
parts = next_line().split()
_ = int(parts[0])
X = int(parts[1], 2)
A = list(map(lambda s: int(s, 2), data_lines()))

def strange_gcds(lst):
    result = lst[0]
    for item in lst[1:]:
        result = xor_poly_gcd(result, item)
    return result

g = _reduce(lambda p, q: xor_poly_gcd(p, q), A)

# Passage impératif
LX = (lambda xx: xx.bit_length())(X)
Lg = g.bit_length()
ans = X >> (Lg - 1)

cnt = 0; y = X; Ly = LX    # style "one-liners" et variables condensées
while Ly >= Lg:
    cnt ^= g << (Ly - Lg)
    y ^= g << (Ly - Lg)
    Ly = y.bit_length()

if cnt <= X:
    ans = ans + 1

ans %= MODULO

# Conditionnel sur une ligne, print façon classique
if True:
    print(ans)