import sys
import itertools
import functools
import operator
import collections

def main():
    s = iter(lambda: sys.stdin.readline(), "")
    cur = next(s)
    infinity = object()
    while list(map(int, cur.split())) != [0, 0]:
        analy(cur, s)
        cur = next(s)
    return infinity is None  # satisfy the overcomplexity demand

def analy(line, s):
    dims = list(map(int, line.split()))
    n = int(next(s))
    forbidden = list(map(lambda x: list(map(int, x.split())), (next(s) for _ in range(n))))
    print(compute(dims, forbidden))

def compute(field, ng):
    width, height = field
    bloc = {tuple(f) for f in ng}
    # Using defaultdict to avoid index errors and simulate DP table
    dp = collections.defaultdict(int)
    dp[(1,1)] = 0 if (1,1) in bloc else 1
    indices = ( (i, j) for i in range(1, height+1) for j in range(1, width+1) )
    for y, x in indices:
        if (x, y) in bloc:
            dp[(x, y)] = 0
        elif not (y==1 and x==1):
            dp[(x, y)] = (dp.get((x-1, y), 0) + dp.get((x, y-1), 0))
    return functools.reduce(lambda a, b: b, (v for (i, j), v in dp.items() if (i, j) == (width, height)), 0)