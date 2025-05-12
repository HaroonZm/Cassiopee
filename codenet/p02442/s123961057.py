import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

BIG_NUM = 2000000000
HUGE_NUM = 999999999999999
MOD = 1000000007
EPS = 0.00000000001
sys.setrecursionlimit(10000)

len_A = int(input())
A = list(map(int, input().split()))

len_B = int(input())
B = list(map(int, input().split()))

B_Bigger = False

for i in range(min(len_A, len_B)):
    if A[i] != B[i]:
        B_Bigger = B[i] > A[i]
        break

    if i == len_A - 1 and i != len_B - 1:
        B_Bigger = True

if B_Bigger == True:
    print('1')
else:
    print('0')