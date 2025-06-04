from itertools import product, chain
from operator import eq

d, a = list(map(str, input().split())), list(map(str, input().split()))
p = ((-1,2,4,1,3,-1),(3,-1,0,5,-1,2),(1,5,-1,-1,0,4),(4,0,-1,-1,5,1),(2,-1,5,0,-1,3),(-1,3,1,4,2,-1))

indices = lambda s, v: list(chain.from_iterable([[i]*int(x==v) for i, x in enumerate(s)]))
ts, fs = indices(d, a[0]), indices(d, a[1])

pairs = filter(lambda x: x[0] != x[1] and p[x[0]][x[1]] != -1, product(ts, fs))
cube_faces = lambda T, F: [d[T], d[F], d[p[T][F]], d[5-p[T][F]], d[5-F], d[5-T]]

solve = any(all(map(eq, a, cube_faces(*pair))) for pair in pairs)
print(('No','Yes')[solve])