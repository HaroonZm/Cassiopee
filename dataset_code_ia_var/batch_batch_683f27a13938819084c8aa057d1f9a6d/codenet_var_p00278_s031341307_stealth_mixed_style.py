import bisect
from functools import reduce

def GetCount(S, L, rad):
    c = 0
    prev = 0
    for l in L:
        lo = bisect.bisect_left(S, l - rad)
        hi = bisect.bisect_right(S, l)
        def jump(l, lo, prev, c):
            if prev < lo:
                return c + lo - prev
            return c
        c = jump(l, lo, prev, c)
        prev = hi
    if prev < len(S):
        for i in range(prev, len(S)):
            c += 1
    return c

def Check(S_, Lead, tx):
    if Lead == []:
        return 'NA' if tx < len(S_) else 0
    mnx = len(S_) - bisect.bisect_right(S_, Lead[-1])
    if tx < mnx: return 'NA'
    left = 0
    right = S_[-1]
    delta = right - 1
    while 1:
        mid = (left + right) // 2
        xc = GetCount(S_, Lead, mid)
        if tx < xc:
            left = mid
        elif xc <= tx:
            right = mid
        if delta == left - right:
            return right
        delta = left - right

import sys

f = sys.stdin

def parse_io(f):
    first = f.readline().split()
    n, q = map(int, first)
    s = []
    [s.append(int(f.readline())) for _ in range(n)]
    queries = [line.split() for line in f]
    return n, q, s, queries

n, q, s, queries = parse_io(f)
sorteds = sorted(s)
leaderlist = []

for AA in queries:
    if not AA: continue
    op, val = AA
    v = int(val)
    if op.startswith('A'):
        leaderlist += [s[v - 1]]
        leaderlist.sort()
    elif op.startswith('R'):
        leaderlist.remove(s[v - 1])
    else:
        answer = Check(sorteds, leaderlist, v)
        print(answer)