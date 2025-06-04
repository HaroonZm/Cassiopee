from functools import reduce
from itertools import starmap, repeat, chain
from operator import contains

_ = input()
S = frozenset(map(int, input().split()))
_ = input()
T = map(int, input().split())
print(sum(starmap(contains, zip(repeat(S), T))))