import sys
from functools import reduce
from operator import itemgetter
from itertools import repeat, cycle
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, Q = map(int, input().split())
H = defaultdict(list)

for _ in range(Q):
    *args, = map(int, input().split())
    action, idx, *vals = args + [None] * (3 - len(args))
    ops = {
        0: lambda: heapq.heappush(H[idx], -vals[0]),
        1: lambda: print(-next(iter(H[idx]), float('nan'))) if H[idx] else None,
        2: lambda: heapq.heappop(H[idx]) if H[idx] else None
    }
    ops.get(action, lambda: None)()