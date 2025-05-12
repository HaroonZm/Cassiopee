import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
a = LIST()

if min(a) >= 0:
	print(N-1)
	for i in range(1, N):
		print(i, i+1)
elif max(a) <= 0:
	print(N-1)
	for i in range(N, 1, -1):
		print(i, i-1)
else:
	print(2*N-1)
	if abs(min(a)) < abs(max(a)):  # max(a)を加える
		idx = a.index(max(a))+1
		for i in range(1, N+1):
			print(idx, i)
			a[i-1] += a[idx-1]
		for i in range(1, N):
			print(i, i+1)
	else:
		idx = a.index(min(a))+1
		for i in range(1, N+1):
			print(idx, i)
			a[i-1] += a[idx-1]
		for i in range(N, 1, -1):
			print(i, i-1)