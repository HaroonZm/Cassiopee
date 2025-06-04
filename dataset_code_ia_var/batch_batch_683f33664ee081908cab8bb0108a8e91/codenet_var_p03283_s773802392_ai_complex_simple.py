from itertools import accumulate, product
from operator import itemgetter

n, m, q = map(int, input().split())
lr = list(map(lambda x: tuple(map(int, x.split())), [input() for _ in range(m)]))
pq = list(map(lambda x: tuple(map(int, x.split())), [input() for _ in range(q)]))

from collections import defaultdict
inc = defaultdict(int)
list(map(lambda x: inc.update({(x[0]-1, x[1]-1): inc[(x[0]-1, x[1]-1)] + 1}), lr))
sq = [[inc[(i, j)] for j in range(n)] for i in range(n)]

c = [list(accumulate(row)) for row in sq]

for p, qv in pq:
    r = (lambda P, Q: sum((lambda a, b: c[a][b] - (c[a][P-2] if P-1 else 0))(a, Q-1) for a in range(P-1, Q))) 
    print(r(p, qv))