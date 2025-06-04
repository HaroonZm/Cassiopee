from functools import reduce
from operator import itemgetter, add
import sys
from itertools import product, chain, compress, takewhile, dropwhile

H, W, M = map(int, sys.stdin.readline().split())
bomb = tuple(map(lambda s: tuple(map(lambda x: int(x)-1, s.split())), (sys.stdin.readline() for _ in range(M))))
X = list(map(lambda h: sum(map(itemgetter(0), filter(lambda x: x[0] == h, ((i, 1) for i, _ in bomb)))), range(H)))
Y = list(map(lambda w: sum(map(itemgetter(1), filter(lambda x: x[1] == w, ((1, j) for _, j in bomb)))), range(W)))
maxX = max(X)
maxY = max(Y)
R = list(compress(range(H), map(lambda x: x==maxX, X)))
C = list(compress(range(W), map(lambda y: y==maxY, Y)))
bombset = frozenset(bomb)

def answer():
    candidates = ((r,c) for r,c in product(R,C))
    possible = dropwhile(lambda rc: rc in bombset, candidates)
    rc = next(possible, None)
    print(maxX + maxY if rc is not None else maxX + maxY - 1)

answer()