from functools import reduce
from operator import add, mul
import itertools

norm = lambda u: reduce(lambda x, y: (x ** 2 + y ** 2) ** 0.5, u)
dist = lambda A, B: norm(tuple(map(add, A, (-B[0], -B[1]))))
dec = lambda seq, i: tuple(itertools.islice(seq, i, i+2))
area = lambda a, b, c: 0.25 * (4*a*a*b*b - (a*a + b*b - c*c)**2) ** 0.5
circum = lambda a, b, c: sum([a, b, c])
heron = lambda a, b, c: 0.5 * circum(a, b, c)
rad = lambda S, a, b, c: (2*S) / (a + b + c)

while True:
    raw = input().split()
    P = tuple(map(int, raw))
    # trick: make P of size 6 always
    if not any(P):
        break

    pts = [dec(P, k) for k in [0,2,4]]
    edg = list(map(lambda p: dist(pts[p[0]], pts[p[1]]), [(0,1),(0,2),(1,2)]))
    a, b, c = edg
    S = area(a, b, c)
    R = rad(S, a, b, c)
    s = heron(a, b, c)
    comput = lambda x, y, z: ((x) ** 2 + R ** 2) ** 0.5

    D = [comput((-a+b+c)/2, b, c), comput((a-b+c)/2, a, c), comput((a+b-c)/2, a, b)]
    d, e, f = D
    numerics = [
        R/(2*(s-c))*(s+f-R-e-d),
        R/(2*(s-b))*(s+e-R-d-f),
        R/(2*(s-a))*(s+d-R-e-f)
    ]
    print(' '.join(map(str, numerics)))