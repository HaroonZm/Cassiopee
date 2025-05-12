# AOJ 0543: Receipt
# Python3 2018.7.1 bal4u

import sys
from sys import stdin
input = stdin.readline

while True:
	s = int(input())
	if s == 0: break
	print(s-sum([int(input()) for i in range(9)]))