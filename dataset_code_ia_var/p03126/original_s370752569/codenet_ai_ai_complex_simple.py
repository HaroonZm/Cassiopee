from functools import reduce
from operator import and_
from itertools import starmap

N, M = starmap(int, (input().split(),))
universe = set(range(1, M + 1))
shared = [set(map(int, input().split()[1:])) for _ in range(N)]
print(len(reduce(and_, shared, universe)))