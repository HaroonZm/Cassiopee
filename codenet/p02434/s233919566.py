# AOJ ITP2_1_D: Vector II
# Python3 2018.6.24 bal4u

from collections import deque
n, q = map(int, input().split())
Q = []
for i in range(n): Q.append(deque())
for i in range(q):
	a = input().split()
	t = int(a[1])
	if   a[0] == '0': Q[t].append(a[2])   # pushBack
	elif a[0] == '1': print(*Q[t])        # dump
	else: Q[t].clear()                    # clear