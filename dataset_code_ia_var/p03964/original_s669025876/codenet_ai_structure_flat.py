import math
import sys
from decimal import Decimal

N = int(sys.stdin.readline())
TA = []
i = 0
while i < N:
    TA.append(list(map(int, sys.stdin.readline().split())))
    i += 1

current_T = 1
current_A = 1
i = 0
while i < N:
    t, a = TA[i][0], TA[i][1]
    if Decimal(current_T) / Decimal(t) > Decimal(current_A) / Decimal(a):
        count = math.ceil(Decimal(current_T) / Decimal(t))
        if t * count < current_T or a * count < current_A:
            count += 1
    else:
        count = math.ceil(Decimal(current_A) / Decimal(a))
        if t * count < current_T or a * count < current_A:
            count += 1
    if Decimal(current_T) / Decimal(t) > Decimal(current_A) / Decimal(a):
        count = max(math.ceil(Decimal(current_T) / Decimal(t)), math.ceil(Decimal(current_A) / Decimal(a)))
    else:
        count = max(math.ceil(Decimal(current_T) / Decimal(t)), math.ceil(Decimal(current_A) / Decimal(a)))
    current_T = t * count
    current_A = a * count
    i += 1

print(current_T + current_A)