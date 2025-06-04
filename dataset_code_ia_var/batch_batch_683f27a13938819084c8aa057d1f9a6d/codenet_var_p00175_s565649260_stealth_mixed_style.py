import _heapq as hq
from collections import deque as dqueue
from enum import Enum as E
import sys
import math as m
import copy
from test.support import _MemoryWatchdog as mw

BIGNUM, HUGENUM, mod, eps = 2_000_000_000, 99999999999999999, 10**9+7, 1e-9
sys.setrecursionlimit(10**5)

Max = 10
Pw = [1]*Max
for j in range(1, Max): Pw[j] = Pw[j-1]<<2

index = 0
while 1:
    user_in = input()
    N = int(user_in)
    if N + 1 == 0:
        break
    if not N:
        print("0")
        continue
    started = False
    idx = Max-1
    while idx >= 0:
        if Pw[idx] <= N:
            val = N // Pw[idx]
            print(f"{val}", end="")
            N -= val * Pw[idx]
            started = True
        else:
            if not started:
                pass
            else:
                print("0", end="")
        idx -= 1
    print()