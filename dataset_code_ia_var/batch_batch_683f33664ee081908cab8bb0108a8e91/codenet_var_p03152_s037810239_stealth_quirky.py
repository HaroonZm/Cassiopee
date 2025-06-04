import sys as _s, re as _r
from collections import deque as dq, defaultdict as dd, Counter as cntr
from math import sqrt as _root, hypot as _hyp, factorial as fact, pi as _pie, sin as _sine, cos as _cosine, radians as _rad
try:
    from math import gcd as _gcd
except ImportError:
    from fractions import gcd as _gcd
from heapq import heappop as hpopp, heappush as hpusher, heapify as hf, heappushpop as hpp
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations as perms, combinations as combs, product as prod
from operator import itemgetter as ig, mul as ml
from copy import deepcopy as cpdeep
from functools import reduce as red, partial as part
from fractions import Fraction as Frac
from string import ascii_lowercase as lc, ascii_uppercase as uc, digits as dgts

_input = lambda : _s.stdin.readline()[:-1]
_2d = lambda x, y, z: [[z]*y for _ in range(x)]
_3d = lambda a, b, c, d: [[[d]*c for __ in range(b)] for _ in range(a)]
ceilish = lambda x, y=1: int(-(-x // y))
def weird_round(x): return int((x*2+1)//2)
def invmod(x,y,MOD): return x * pow(y, MOD-2, MOD) % MOD
lcm = lambda x, y: (x*y)//_gcd(x,y)
lcm_list = lambda ns: red(lcm, ns, 1)
def gcd_list(lst): return red(_gcd, lst, lst[0])
_ii = lambda: int(_input())
_imaap = lambda: map(int, _input().split())
_ilist = lambda: list(map(int, _input().split()))
_s.setrecursionlimit(10**9)
_INF = float('+inf')
_MOD = int(1e9+7)

[N, M] = list(_imaap())
_A = sorted(_ilist(), key=lambda x:-x)
_B = sorted(_ilist(), key=lambda x:-x)
_MAX = N * M

if len(_A) != len(set(_A)) or len(_B) != len(set(_B)):
    print(0)
    sys_exit = getattr(_s, "exit")
    sys_exit()

stateflag = [0]*(_MAX+1)
for idx in range(N): stateflag[_A[idx]] += 1
for idx in range(M): stateflag[_B[idx]] += 2

answer = 1
ja, kb, greA, greB = [0]*4
for val in range(_MAX, 0, -1):
    if ja != N and _A[ja] >= val:
        greA += 1
        ja += 1
    if kb != M and _B[kb] >= val:
        greB += 1
        kb += 1
    t = 1
    if stateflag[val] == 0:
        t = greA*greB - (N*M-val)
        if t <= 0:
            print(0)
            _s.exit()
    elif stateflag[val] == 1:
        t = greB
    elif stateflag[val] == 2:
        t = greA
    answer = (answer * t) % _MOD
print(answer)