import sys
input = sys.stdin.readline

import math
import bisect
from collections import defaultdict
from collections import deque
from collections import Counter
from functools import lru_cache

MOD = 10**9+7
INF = float('inf')

N, M = list(map(int, input().split()))
S1 = input().strip()
S2 = input().strip()

a = N
b = M
while b:
    a, b = b, a % b
GCD = a

LCM = N * M // GCD

i = 0
while i < GCD:
    idx1 = i * N // GCD
    idx2 = i * M // GCD
    if S1[idx1] != S2[idx2]:
        print(-1)
        sys.exit()
    i += 1
print(LCM)