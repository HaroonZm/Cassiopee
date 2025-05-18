#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N = int(readline())

m = map(int, read().split())
A, B = zip(*zip(m, m))
A = np.array(A[::-1])
B = np.array(B[::-1])

cnt = 0
for i in range(N):
    acc = B[i] - A[i] % B[i] if A[i] % B[i] != 0 else 0
    A[i:] += acc
    cnt += acc

print(cnt)