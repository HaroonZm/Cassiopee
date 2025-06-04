import sys
import os
import math

def freq_op(A):
    B = []
    for a in A:
        B.append(A.count(a))
    return B

for s in sys.stdin:
    n = int(s)
    if n == 0:
        break

    A = list(map(int, input().split()))

    cnt = 0
    while True:
        B = freq_op(A)
        cnt += 1
        if B == A:
            break
        else:
            A = B

    print(cnt - 1)
    print(*A)