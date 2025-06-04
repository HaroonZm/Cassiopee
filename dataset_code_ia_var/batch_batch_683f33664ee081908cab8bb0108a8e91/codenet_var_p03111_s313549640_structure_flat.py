import sys
input = sys.stdin.readline

import math
import bisect
from collections import defaultdict
from collections import deque
from functools import lru_cache

MOD = 10**9+7
INF = float('inf')

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

MIN = INF
n1 = len(L)
for b1 in range(1, 1 << n1):
    Tdic1 = defaultdict(int)
    for t in L:
        Tdic1[t] += 1
    n = n1
    Ttmp1 = L[:]
    choose1 = 0
    number1 = 0
    for i in range(n1):
        if (b1 >> i) & 1 == 1:
            Tdic1[Ttmp1[i]] -= 1
            choose1 += Ttmp1[i]
            number1 += 1
    MP1 = abs(choose1 - A) + (number1 - 1) * 10
    L1 = []
    for k, v in Tdic1.items():
        L1.extend([k] * v)
    n2 = len(L1)
    for b2 in range(1, 1 << n2):
        Tdic2 = defaultdict(int)
        for t in L1:
            Tdic2[t] += 1
        Ttmp2 = L1[:]
        choose2 = 0
        number2 = 0
        for i in range(n2):
            if (b2 >> i) & 1 == 1:
                Tdic2[Ttmp2[i]] -= 1
                choose2 += Ttmp2[i]
                number2 += 1
        if number2 == 0:
            continue
        MP2 = abs(choose2 - B) + (number2 - 1) * 10
        L2 = []
        for k, v in Tdic2.items():
            L2.extend([k] * v)
        n3 = len(L2)
        for b3 in range(1, 1 << n3):
            Tdic3 = defaultdict(int)
            for t in L2:
                Tdic3[t] += 1
            Ttmp3 = L2[:]
            choose3 = 0
            number3 = 0
            for i in range(n3):
                if (b3 >> i) & 1 == 1:
                    Tdic3[Ttmp3[i]] -= 1
                    choose3 += Ttmp3[i]
                    number3 += 1
            if number3 == 0:
                continue
            MP3 = abs(choose3 - C) + (number3 - 1) * 10
            L3 = []
            for k, v in Tdic3.items():
                L3.extend([k] * v)
            # At this point, all L used up, don't enforce that
            MIN = min(MIN, MP1 + MP2 + MP3)
print(MIN)