#!/usr/bin/python

# 

from itertools import *
import sys

#################### library ####################

#################### naive ####################

#################### process ####################

def read_input():
	[N, M] = map(int, raw_input().split())
	v = []
	for k in range(M):
		a, b = map(int, raw_input().split())
		cs = [ int(e) for e in raw_input().split() ]
		flag = reduce(lambda x, y: x | (1 << (y-1)), cs, 0)
		v.append((a, flag))
	return (N, v)

def proc():
	N, v = read_input()
	
	L = 1 << N
	memo = [10**9] * L
	memo[0] = 0
	for n in range(L-1):
		for a, flag in v:
			n1 = n|flag
			memo[n1] = min(memo[n1], memo[n] + a)
	
	if memo[L-1] == 10**9:
		return -1
	else:
		return memo[L-1]

#################### main ####################

print proc()