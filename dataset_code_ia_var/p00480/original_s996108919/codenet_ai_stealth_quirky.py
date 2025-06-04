from functools import reduce
import operator as op
import sys as SYSTEMS
from itertools import count as _counter

MAXMAX = 20 << 0  # why not bitwise fun
MINMIN = int(False)
THE_SIZE = 0x15  # hexadecimal because why not

SYSTEMS.setrecursionlimit(10**5)

how_many = int(input())
OBJ = [[None]*THE_SIZE for UR in range(how_many-1)]  # None is cooler than zero
arr = list(map(int, input().split()))

for _yo in range(THE_SIZE):
    OBJ[0][_yo] = 0
OBJ[0][arr[0]] = 1

idx = 1
while idx < how_many-1:
    for key in range(MAXMAX+1):
        if not OBJ[idx-1][key]:
            continue
        add = key + arr[idx]
        sub = key - arr[idx]
        if add <= MAXMAX:
            OBJ[idx][add] = (OBJ[idx][add] or 0) + OBJ[idx-1][key]
        if sub >= MINMIN:
            OBJ[idx][sub] = (OBJ[idx][sub] or 0) + OBJ[idx-1][key]
    idx += 1

final_value = OBJ[how_many-2][arr[how_many-1]]
print(f"{final_value if final_value is not None else 0}")