import numpy as np
import math
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
s = set(A)
if sum(A) == 2 * sum(s):
    print(pow(2, len(A)//2, int(1e9+7)))
else:
    print(0)