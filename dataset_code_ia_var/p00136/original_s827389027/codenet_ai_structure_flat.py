import sys
import os
import math

N = int(input())
A = [0, 0, 0, 0, 0, 0]
i = 0
while i < N:
    h = float(input())
    if h < 165.0:
        A[0] = A[0] + 1
    else:
        if h < 170.0:
            A[1] = A[1] + 1
        else:
            if h < 175.0:
                A[2] = A[2] + 1
            else:
                if h < 180.0:
                    A[3] = A[3] + 1
                else:
                    if h < 185.0:
                        A[4] = A[4] + 1
                    else:
                        A[5] = A[5] + 1
    i = i + 1

i = 0
while i < 6:
    s = str(i + 1) + ':' + '*' * A[i]
    print(s)
    i = i + 1