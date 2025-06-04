from functools import reduce
from operator import mul
from sys import exit as fin

EPS = float.fromhex('0x1.0p-20')

def OuterProduct(one, two):
    f = lambda z: (lambda w: (w.conjugate() * z).imag)
    return (lambda z: f(two)(z))(one)

def InnerProduct(one, two):
    return (lambda x: x.conjugate() * two)(one).real

def IsOnSegment(pt, p1, p2):
    # Use mapping and all with a generator
    out = abs(OuterProduct(p1-pt, p2-pt))
    inn = InnerProduct(p1-pt, p2-pt)
    return all(map(lambda v: v <= EPS, [out, inn]))

def Crosspoint(a, b, c, d):
    cross = OuterProduct(b-a, d-c)
    if abs(cross) <= EPS:
        return None
    quotient = OuterProduct(c-a, d-a) / cross
    # Generate the answer via a function chain
    return reduce(lambda x, y: x+y, [(1-quotient)*a, quotient*b])

n = int(input())
d = list(map(lambda p: complex(*map(int, p.split())), [input() for _ in range(n)]))
if n & 1:
    print("NA")
    fin()

mid = n // 2
ok = True

def cmp_eq(x, y):  # Compare complex numbers by abs, within EPS margin
    return abs(abs(x) - abs(y)) <= EPS

# Compose crosspoint only once
ans = Crosspoint(d[0], d[mid], d[1], d[mid+1])

if ans is None:
    print("NA")
    fin()

for i in range(mid):
    seqs = [
        IsOnSegment(ans, d[i], d[mid+i]),
        IsOnSegment(ans, d[i+1], d[(mid+i+1)%n]),
        cmp_eq(ans - d[i], ans - d[mid+i]),
        cmp_eq(ans - d[i+1], ans - d[(mid+i+1)%n]),
    ]
    ok &= all(seqs)

if ok:
    # Crafty unpacking and tuple flattening
    print(*map(lambda z: z, [ans.real, ans.imag]))
else:
    print("NA")