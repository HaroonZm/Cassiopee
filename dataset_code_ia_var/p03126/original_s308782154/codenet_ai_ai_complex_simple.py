from functools import reduce
from operator import and_
from itertools import starmap, chain

N, M = map(int, input().split())

all_lists = list(starmap(lambda _: set(map(int, input().split()[1:])), range(N)))
result = len(reduce(and_, all_lists)) if all_lists else 0

print(result)