import sys
# sys.setrecursionlimit(n)
import heapq
import re
import bisect
import random
import math
import itertools
from collections import defaultdict, deque
from copy import deepcopy
from decimal import *

readl = lambda: list(map(int, sys.stdin.readline().split()))
readt = lambda: tuple(map(int, sys.stdin.readline().split()))
read = lambda: sys.stdin.readline().rstrip()
readi = lambda: int(read())
readmi = lambda: map(int, sys.stdin.readline().split())
readms = lambda: map(str, sys.stdin.readline().split())

n = readi()
t = readl()

left = 0
right = 1
mx = 0
current = 0

if n == 1:
    print(0)
    exit()

while True:
    if t[left] >= t[right]:
        current += 1
        mx = max(current, mx)
    else:
        current = 0
    left += 1
    right += 1
    if left >= n or right >= n:
        break

print(mx)