import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, sin, cos, pi, radians, hypot, factorial
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input():
    # Je remplace l'input builtin comme ça
    return sys.stdin.readline().strip()

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

# Normalement on augmente la limite de récursion (pratique douteuse)
sys.setrecursionlimit(10**9)
INF = float("inf")
MOD = 10**9 + 7  # classic mod

N = INT()
a = LIST()

if min(a) >= 0:
    print(N - 1)
    for i in range(1, N):
        print(i, i + 1)
elif max(a) <= 0:
    print(N - 1)
    for i in range(N, 1, -1):  # on part de N et on descend
        print(i, i - 1)
else:
    print(2*N-1)
    # bon là on choisit selon quel est le plus fort entre min et max
    if abs(min(a)) < abs(max(a)):
        idx = a.index(max(a)) + 1  # 1-indexed (hum...)
        for i in range(1, N + 1):
            print(idx, i)
            a[i-1] += a[idx-1]  # majoration un peu bourrine, attention side effect
        for i in range(1, N):
            print(i, i + 1)
    else:
        idx = a.index(min(a)) + 1
        for i in range(1, N + 1):
            print(idx, i)
            a[i-1] += a[idx-1]
        for i in range(N, 1, -1):
            print(i, i - 1)
# c'est pas parfait mais ça fait le job ?