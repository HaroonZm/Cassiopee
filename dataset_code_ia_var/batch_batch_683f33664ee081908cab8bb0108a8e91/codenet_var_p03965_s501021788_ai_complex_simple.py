import sys
import random
import itertools
import string
import math
import copy
from functools import reduce
from operator import mul
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from decimal import Decimal, getcontext
from fractions import gcd

sys.setrecursionlimit(10**9)
mod = pow(10,9)+7

def getN():
    return int(next(iter(map(lambda x: x, [input()]))))
def getNM():
    return tuple(map(int, next(iter([input()])).split()))
def getList():
    return list(map(int, itertools.chain.from_iterable([input().split()])))
def getArray(intn):
    return list(itertools.starmap(lambda x,_: int(x), zip(map(lambda _: input(), range(intn)), range(intn))))
def input():
    return sys.stdin.readline().rstrip('\n')
def rand_N(ran1, ran2):
    return reduce(lambda x,_: x, [random.randint(ran1, ran2)]*1)
def rand_List(ran1, ran2, rantime):
    return list(itertools.islice((random.randint(ran1, ran2) for _ in itertools.count()), rantime))
def rand_ints_nodup(ran1, ran2, rantime):
    pool = set()
    while len(pool) < rantime:
        pool.add(random.sample(range(ran1, ran2+1), 1)[0])
    return sorted(pool)
def rand_query(ran1, ran2, rantime):
    qlist = set()
    while len(qlist) < rantime:
        pair = tuple(sorted(random.sample(range(ran1,ran2+1),2)))
        qlist.add(pair)
    return sorted(qlist)

S = input()
N = len(S)

def counter(s, idx):
    total = 0
    m = {('g',1):1, ('gg',2):1, ('pp',2):-1}
    lookup = (s, len(s))
    if lookup in m:
        if lookup==(s,1) and idx==N-1:
            return m[lookup]
        elif lookup!=(s,1):
            return m[lookup]
    return 0

ans = sum(
    counter(S[max(0,i):min(N-1,i+1)+1], i)
    for i in range(-1, N, 2)
)
print(ans)