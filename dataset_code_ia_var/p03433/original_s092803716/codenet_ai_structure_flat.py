import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal

sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

N = int(input())
A = int(input())

x = N % 500
if x > A:
    print("No")
else:
    print("Yes")