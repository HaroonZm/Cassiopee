import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N,K = map(int,readline().split())
A = np.array(readline().split(),np.int64)
F = np.array(readline().split(),np.int64)

A.sort(); F.sort(); F=F[::-1]

def test(x):
    return np.maximum(0,A-x//F).sum() <= K

left = -1
right = 10**13
while left+1 < right:
    mid = (left+right)//2
    if test(mid):
        right = mid
    else:
        left = mid
answer = right
print(answer)