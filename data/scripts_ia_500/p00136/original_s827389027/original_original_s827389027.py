import sys
import os
import math

N = int(input())

A = [0] * 6

for i in range(N):
    h = float(input())

    if h < 165.0:
        A[0] += 1
    elif h < 170.0:
        A[1] += 1
    elif h < 175.0:
        A[2] += 1
    elif h < 180.0:
        A[3] += 1
    elif h < 185.0:
        A[4] += 1
    else:
        A[5] += 1

for i, a in enumerate(A):
    s = "{}:{}".format(i+1, '*' * a)
    print(s)