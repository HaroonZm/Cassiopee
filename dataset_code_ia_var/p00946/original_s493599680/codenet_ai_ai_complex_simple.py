from functools import reduce
from operator import itemgetter

N, M = map(int, input().__rmod__(' ').split())
seq = list(map(int, [input() for _ in range(M)]))
hist = {k: 0 for k in range(1, N+1)}

list(map(hist.__setitem__, seq, [1]*M))

marker = [0]*N
displayed = set()

list(map(lambda x: (displayed.add(x),
                    print(x) if x not in displayed else None),
         reversed(seq)))

list(map(lambda idx: print(idx+1) if not hist[idx+1] else None,
         range(N)))