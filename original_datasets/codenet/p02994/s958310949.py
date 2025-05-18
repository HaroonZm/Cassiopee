#import numpy as np
from sys import stdin
from copy import deepcopy
from functools import reduce
from fractions import gcd
import math
import itertools
from collections import Counter
from itertools import chain  ##list(chain.from_iterable(l)) ##flatten
from heapq import heappush, heappop

"""
N = int(input())
A, B = map(int,input().split())
A = list(map(int,input().split())) ## 横一列
A = [int(input()) for _ in range(N)] ## 縦一列
lst = [list(map(int,input().split())) for i in range(M)] ## 二次元
"""

N, L = map(int,input().split())

Sum = N * (N+2*L-1) // 2

if L > 0:
  ans = Sum - L
elif L + N - 1 < 0:
  ans = Sum - (L + N - 1)
else:
  ans = Sum
  
print(ans)