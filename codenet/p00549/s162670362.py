# AOJ 0626 Collecting Stamps 2
# Python3 2018.7.2 bal4u

import sys
from sys import stdin
input = stdin.readline

n = int(input())
si, sj = [0]*(n+1), [0]*(n+1)
s = input().strip()
for i in range(n):
	sj[i+1] = sj[i] + (s[i] == 'J')
	si[i+1] = si[i] + (s[i] == 'I')

ans = a = b = c = 0
for i in range(1, n): a = max(a, sj[i] * (si[n]-si[i]))
for i in range(n):
	if s[i] == 'O':
		b += si[n]-si[i+1]
		c += sj[i]
		ans += (si[n]-si[i+1]) * sj[i]
print(ans + max(a, b, c))