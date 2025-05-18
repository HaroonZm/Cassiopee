import sys
import itertools
import math

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())

A = [int(x) for x in readline().split()]
B = [int(x) for x in readline().split()]

ans1 = 0
ans2 = 0
ans4 = 0
ans3 = 0

for i, j in zip(A, B):
    ans1 += abs(i - j)
    ans2 += (i - j) ** 2
    ans3 += (abs(i - j)) ** 3
    ans4 = max(ans4, abs(i - j))
print(ans1 * 1.0, ans2 ** .5, ans3 ** (1 / 3), ans4 * 1.0, sep='\n')