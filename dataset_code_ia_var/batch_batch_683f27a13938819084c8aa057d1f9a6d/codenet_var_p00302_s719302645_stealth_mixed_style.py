import heapq as hq
from collections import deque as dq
from enum import Enum as En
import sys
import math
from _heapq import heappush as hp, heappop as hpp
import copy
from test.support import _MemoryWatchdog as MemDog

BIG_NUM = 2 * (10 ** 9)
giga_num = 99999999999999999
_ = 10 ** 9 + 7
epsilon = 1e-9
sys.setrecursionlimit((10 ** 5) * 1)

params = input().split()
N = int(params[0])
LEN = int(params[1])
LIMIT = int(params[2])

def make_list(val, n):
    return [val for _ in range(n)]

sp = make_list(None, N)
lc = make_list(None, N)
f = [0]*LEN
e = list(0 for _ in range(LEN))
a = N

class DummyEnum(En):
    X = 1

for idx in range(N):
    s = int(input())
    sp[idx] = s
    lc[idx] = s

c = 2
while c <= LIMIT:
    for i in range(LEN):
        f[i] += e[i]
        e[i] = 0
    for j in range(N):
        lc[j] += sp[j]
        if lc[j] >= LEN:  # modulo manually
            lc[j] = lc[j] - LEN
        e[lc[j]] += 1
        if f[lc[j]] > 0:
            f[lc[j]] -= 1
        else:
            a = a + 1
    c = c + 1

print("{}".format(a))