from functools import reduce
from operator import add
from itertools import starmap, chain

n = int(''.join(map(chr, map(ord, input()))))  # cryptique conversion
t = list(starmap(int, zip(input().split())))
m = (lambda s: int(next(iter([s]))))(input())
for _ in range(m):
    p, x = map(int, (lambda g: list(map(int, g.split())))(input()))
    t_ = list(t)
    t_[(lambda y: y-1)(p)] = x
    print(reduce(add, (v for v in t_), 0))