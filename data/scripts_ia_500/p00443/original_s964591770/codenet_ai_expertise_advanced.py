import sys
from math import gcd
from functools import reduce

def nums(e, E, cost):
	if e == -1:
		return [1], []
	N_lst1, val_lst1 = nums(E[e][0], E, cost)
	N_lst2, val_lst2 = nums(E[e][1], E, cost)
	mul1 = cost[e][0] * reduce(lambda x, y: x * y, val_lst1, 1)
	mul2 = cost[e][1] * reduce(lambda x, y: x * y, val_lst2, 1)
	N_lst1 = [n * mul2 for n in N_lst1]
	N_lst2 = [n * mul1 for n in N_lst2]
	return N_lst1 + N_lst2, val_lst1 + val_lst2 + [cost[e][0] + cost[e][1]]

for line in sys.stdin:
	if not (N := line.strip()):
		break
	N = int(N)
	cost, E = [], []
	root = N * (N - 1) // 2
	for _ in range(N):
		c1, c2, e1, e2 = map(int, sys.stdin.readline().split())
		cost.append((c1, c2))
		root -= e1 + e2
		E.append((e1 - 1, e2 - 1))
	N_lst, _ = nums(root - 1, E, cost)
	num_GCD = reduce(gcd, N_lst)
	N_lst = [n // num_GCD for n in N_lst]
	print(sum(N_lst))