import sys
from functools import reduce
from itertools import islice, compress, permutations, groupby, cycle, dropwhile, product

def side(p1, p2, p3):
    a, b, c = (lambda q: (q[1], q[0]))(p1), (lambda q: (q[1], q[0]))(p2), (lambda q: (q[1], q[0]))(p3)
    m = lambda p, q: (q[0] - p[0], q[1] - p[1])
    u, v = m(a, b), m(a, c)
    det = lambda u, v: u[0]*v[1] - u[1]*v[0]
    return det(u, v) > 0

while True:
    try:
        n = int((lambda x: x.strip())(input()))
    except: break
    if not n: break
    D = sorted([[(lambda t: int(t))(x) for x in input().split()] for _ in range(n)], key=lambda z: (z[0], z[1]))
    p1 = D[0]
    D1 = D[:]
    history = []
    while True:
        c = [sum(1 for p3 in D[::-1]
                   if p1 != p3 and p2 != p3 and not side(p1, p2, p3))
             for p2 in D1 if p1 != p2]
        idx = next((i for i, v in enumerate(c) if v == 0), -1)
        if idx == -1: break
        p2 = [p for p in D1 if p != p1][idx]
        p1 = p2
        D1 = list(filter(lambda x: x != p2, D1))
        history.append(id(p2))
        if p2 == D[0]:
            break
    print(len(D1))