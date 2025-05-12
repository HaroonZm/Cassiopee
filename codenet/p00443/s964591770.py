#!/usr/bin/env python

def GCD(a, b):
	dummy1 = max(a, b)
	dummy2 = min(a, b)
	while True:
		dummy = dummy1 % dummy2
		dummy1 = dummy2
		dummy2 = dummy
		if(dummy == 0):
			break

	return dummy1

while True:
	N = input()
	if not N:
		break
	cost = []
	E = []
	root = N * (N - 1) / 2
	for i in range(N):
		S = raw_input().split()
		c1, c2, e1, e2 = list(map(int,S))
		cost.append((c1, c2))
		root -= e1 + e2
		e1 -= 1
		e2 -= 1
		E.append((e1, e2))
	def nums(e):
		N_lst1 = []
		N_lst2 = []
		val_lst1 = []
		val_lst2 = []
		if E[e][0] != -1:
			N_lst1, val_lst1 = nums(E[e][0])
		else:
			N_lst1 = [1]
			val_lst1 = []
		
		if E[e][1] != -1:
			N_lst2, val_lst2 = nums(E[e][1])
		else:
			N_lst2 = [1]
			val_lst2 = []
		
		mul1 = cost[e][0]
		for num in val_lst1:
			mul1 *= num
		mul2 = cost[e][1]
		for num in val_lst2:
			mul2 *= num
		for i in range(len(N_lst1)):
			N_lst1[i] *= mul2
		for i in range(len(N_lst2)):
			N_lst2[i] *= mul1
		
		return N_lst1 + N_lst2, val_lst1 + val_lst2 + [cost[e][0] + cost[e][1]]
	N_lst, v_lst = nums(root - 1)
	#print N_lst
	num_GCD = N_lst[0]
	for num in N_lst:
		num_GCD = GCD(num, num_GCD)
	
	for i in range(len(N_lst)):
		N_lst[i] //= num_GCD
	#print N_lst
	print sum(N_lst)