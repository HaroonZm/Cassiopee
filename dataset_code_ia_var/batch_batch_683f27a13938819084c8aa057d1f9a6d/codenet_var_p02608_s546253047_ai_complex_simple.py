from functools import reduce
from itertools import product, islice, count, starmap
from operator import add

N = int(input())
size = 10001
X = list(map(int, [0]*size))

def S(i, j, k): 
    return reduce(add, map(lambda t: t[0]*t[1], [(i,i), (j,j), (k,k), (i,j), (j,k), (k,i)]))

triplets = product(*(range(1, 102) for _ in range(3)))

def index_generator():
    for t in triplets:
        s = S(*t)
        if s < size:
            yield s

from collections import Counter
counter = Counter(index_generator())
X = list(map(lambda i: counter.get(i,0), range(size)))

print(*islice(X, 1, N+1), sep='\n')