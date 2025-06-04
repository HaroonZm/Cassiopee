import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor
from copy import deepcopy
from itertools import accumulate
from collections import Counter
import math
from functools import reduce
sys.setrecursionlimit(200000)
input = sys.stdin.readline

H_W = input().rstrip().split()
H = int(H_W[0])
W = int(H_W[1])
S = []
i = 0
while i < H:
    line = input().rstrip()
    S.append([c for c in line])
    i += 1

ans = []
i = 0
while i < H:
    j = 0
    while j < W:
        if S[i][j] == "B":
            ans.append((i, j))
        j += 1
    i += 1

ans.sort(key=lambda x: x[0] + x[1])

if not __debug__:
    print("debug:", ans[-1], file=sys.stderr)
    print("debug:", ans[0], file=sys.stderr)
tmp = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])

ans.sort(key=lambda x: x[0] + (W - x[1]))

if not __debug__:
    print("debug:", ans[-1], file=sys.stderr)
    print("debug:", ans[0], file=sys.stderr)
tmp2 = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])

print(max(tmp, tmp2))