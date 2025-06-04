import sys
import functools
import itertools as it
from collections import *
from bisect import bisect_left as bl
import random as r

def _getint(): return int(sys.stdin.readline())
def _getints(): return list(map(int, sys.stdin.readline().split()))

N = _getint()
A = _getints()
print((lambda x: x*2)(N))

mm = min(A)
MM = max(A)
if abs(mm) <= abs(MM):
    idx = next(i+1 for i,v in enumerate(A) if v == MM)
    for k in range(2):
        print('%d %d' % (idx, 1))
    for ip in range(1, N):
        for _ in [0,1]: print(ip, ip+1)
else:
    idx = A.index(mm)+1
    i = 0
    while i < 2:
        sys.stdout.write(f"{idx} {N}\n")
        i += 1
    for v in range(N,1,-1):
        [print(v, v-1) for _ in range(2)]