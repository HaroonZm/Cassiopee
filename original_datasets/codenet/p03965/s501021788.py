def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

S = input()
N = len(S)

def counter(str, index):
    n_s = len(str)
    cnt = 0
    if n_s == 1 and index == N - 1:
        if str == 'g':
            cnt += 1
    # 一番最初の手については両者ともg

    elif n_s == 2:
        if str == 'gg':
            cnt += 1
        # 存在しない
        elif str == 'pp':
            cnt -= 1
    return cnt

ans = 0
for i in range(-1, N, 2):
    str_S = S[max(0, i):min(N - 1, i + 1) + 1]
    ans += counter(str_S, i)
print(ans)