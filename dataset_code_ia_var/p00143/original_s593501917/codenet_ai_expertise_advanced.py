from operator import itemgetter

def side(a, b, c):
    (ax, ay), (bx, by), (cx, cy) = a, b, c
    return (cy - ay) * (bx - ax) - (by - ay) * (cx - ax) > 0

def is_inner(x, p):
    return all(side(*triple) == side(*next_triple)
               for triple, next_triple in zip(
                   [(p[0], p[1], x), (p[1], p[2], x), (p[2], p[0], x)],
                   [(p[1], p[2], x), (p[2], p[0], x), (p[0], p[1], x)]
               ))

for _ in range(int(input())):
    *P, = map(int, input().split())
    pts = [tuple(P[i:i+2]) for i in range(0, 6, 2)]
    x1, x2 = tuple(P[6:8]), tuple(P[8:10])
    result = is_inner(x1, pts) != is_inner(x2, pts)
    print('OK' if result else 'NG')