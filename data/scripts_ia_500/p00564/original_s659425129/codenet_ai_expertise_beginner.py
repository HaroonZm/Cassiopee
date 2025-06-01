N, A, B, C, D = input().split()
N = int(N)
A = int(A)
B = int(B)
C = int(C)
D = int(D)

import math

cost1 = math.ceil(N / A) * B
cost2 = math.ceil(N / C) * D

if cost1 > cost2:
    print(cost2)
elif cost2 > cost1:
    print(cost1)
else:
    print(cost1)