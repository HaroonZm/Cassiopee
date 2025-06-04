from functools import reduce
from operator import add
from itertools import starmap

N = int(input())
T = list(map(int, input().split()))
M = int(input())
S = reduce(add, T, 0)

for _ in range(M):
    p, x = starmap(lambda y,z:(y,z), [tuple(map(int, input().split()))]).__next__()
    print((lambda s, t, i, v: s - t[i] + v)(S, T, p-1, x))