import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
	N, W = MAP()

	n1 = N // 2
	n2 = N - n1

	vw1 = [[0, 0]]
	vw2 = [[0, 0]]

	for _ in range(n1):
		v, w = MAP()
		for i in range(len(vw1)):
			p = vw1[i].copy()
			p[0] += v
			p[1] += w
			vw1.append(p)

	for _ in range(n2):
		v, w = MAP()
		for i in range(len(vw2)):
			p = vw2[i].copy()
			p[0] += v
			p[1] += w
			vw2.append(p)
	vw1.sort(key=lambda x:(x[1], -x[0]))
	vw2.sort(key=lambda x:(x[1], -x[0]))
	tmp_v = 0
	for i in range(1<<n2):  # 要素数を減らさずに無駄な荷物を除く
		v, w = vw2[i]
		if tmp_v < v:
			tmp_v = v
		else:
			vw2[i][0] = tmp_v

	idx1 = 0
	idx2 = 2 ** n2 - 1
	ans = 0
	while idx1 < 2 ** n1 and idx2 >= 0:  # しゃくとり法
		v1, w1 = vw1[idx1]
		v2, w2 = vw2[idx2]
		while idx2 > 0 and w1 + w2 > W:
			idx2 -= 1
			v2, w2 = vw2[idx2]
		if w1 + w2 <= W:
			v_sum = v1 + v2
			ans = ans if ans > v_sum else v_sum
		idx1 += 1

	print(ans)

if __name__ == '__main__':
	main()