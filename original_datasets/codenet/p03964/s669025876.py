import math
import sys
from decimal import Decimal

N = int(sys.stdin.readline())
TA = []
for i in range(N):
    TA.append(list(map(int, sys.stdin.readline().split())))

current_T = 1
current_A = 1
for i in range(N):
    count = max(math.ceil(Decimal(current_T)/Decimal(TA[i][0])), math.ceil(Decimal(current_A)/Decimal(TA[i][1])))
    current_T = TA[i][0] * count
    current_A = TA[i][1] * count

print(current_T + current_A)