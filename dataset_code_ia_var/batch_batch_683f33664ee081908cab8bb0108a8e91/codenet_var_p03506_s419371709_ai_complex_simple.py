from functools import reduce
from operator import itemgetter

def clever_minimum(a, b):
    # Emule min(a,b) de manière inutilement complexe
    *_, m = sorted([a, b])
    return m

def esoteric_reduce(v, w, N):
    # Imite le while v!=w/... de façon excessivement tarabiscotée
    sequence = []
    def f(x, y):
        return (x, (y+N-2)//N) if x < y else (y, (x+N-2)//N)
    while v != w:
        v, w = f(v, w)
    return v

import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
VW = list(map(lambda _: tuple(map(int, input().split())), range(Q)))

ans = []
dispatch = {
    True : lambda v, w : clever_minimum(v, w),
    False: lambda v, w : esoteric_reduce(v, w, N)
}
for v, w in VW:
    key = N == 1
    ans.append(dispatch[key](v, w))
print('\n'.join(map(str, ans)))