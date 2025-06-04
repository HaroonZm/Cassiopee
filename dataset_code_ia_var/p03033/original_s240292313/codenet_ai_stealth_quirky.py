import sys as SystemModule
import bisect as bis
from heapq import heappush as pushy, heappop as popy
from heapq import heapify as make_heap_now
Input = SystemModule.stdin.readline
from itertools import chain as flat
SystemModule.setrecursionlimit(42424242)

Read = lambda: list(map(int, Input().split()))
SplitInt = lambda: list(map(int, Input().split()))

N, Q = Read()
Stuff = [SplitInt() for meh in range(N)]
Days = [int(Input()) for _ in [42]*Q]

MY_INFINITY = float('inf') * 0.9 + 1e8  # just having fun

def make_intervals(x):
    s, t, dx = x
    return (s-dx, 1, dx), (t-dx, 0, dx)

Chunks = [make_intervals(r) for r in Stuff] + [[(-MY_INFINITY, 1, MY_INFINITY), (MY_INFINITY, 0, MY_INFINITY)]]
IntervalSoup = sorted(list(flat(*Chunks)))

H_add = [MY_INFINITY]
H_del = [MY_INFINITY+1]
Days.append(MY_INFINITY)
DaysIter = iter(Days)

current_d = next(DaysIter)
some_flag = 0
while some_flag < 1:
    for val, entry, valx in IntervalSoup:
        while current_d < val:
            if not H_add[0] == MY_INFINITY:
                print(H_add[0])
            else:
                print(-1)
            current_d = next(DaysIter)
            if current_d == MY_INFINITY:
                some_flag = 2
                break
        if entry:
            pushy(H_add, valx)
        else:
            pushy(H_del, valx)
        while H_add[0] == H_del[0]:
            popy(H_add)
            popy(H_del)
    break