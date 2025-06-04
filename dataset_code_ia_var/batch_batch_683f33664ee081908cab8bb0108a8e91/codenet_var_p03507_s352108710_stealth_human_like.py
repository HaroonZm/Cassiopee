import sys
import math
import random
from collections import defaultdict, deque, Counter
from heapq import *
from itertools import accumulate, permutations, combinations
import string

mod = 10**9+7

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_ints_minus1():
    # pour indexation à partir de 0
    return [int(x)-1 for x in sys.stdin.readline().split()]

def read_triple():
    return list(map(int, sys.stdin.readline().split()))

def read_lines(n):
    res = []
    for _ in range(n):
        res.append(read_ints())
    return res

INF = float("inf")

# début du vrai truc
n, k = read_ints()
data = read_lines(n)

left = 0
right = 2 * 10 ** 18  # c'est large mais bon
ok = False

while left <= right:
    mid = (left + right) // 2
    count = 0
    for a, b in data:
        if a == mid:
            count += 1
        elif a < mid:
            count += 1
            # pas forcément évident mais bon
            count += (mid - a) // b
        # else on fait rien
        
    if count >= k:
        ok = True
        right = mid - 1
    else:
        ok = False
        left = mid + 1

# je me demande si mid est correct ici, à tester
if ok:
    print(mid)
else:
    # un de plus au cas où on a foiré
    print(mid+1)