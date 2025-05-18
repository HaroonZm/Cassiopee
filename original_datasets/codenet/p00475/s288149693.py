# AOJ 0552: Exposition
# Python3 2018.7.1 bal4u

import sys
from sys import stdin
input = stdin.readline

x, y = [], []
n = int(input())
for i in range(n):
	a, b = map(int, input().split())
	x.append(a+b)
	y.append(a-b)
xmin, xmax = min(x), max(x)
ymin, ymax = min(y), max(y)
ans1 = ans2 = 0
for i in range(n):
	d1 = max(x[i]-xmin, y[i]-ymin)
	d2 = max(xmax-x[i], ymax-y[i])
	ans1 = max(ans1, min(d1, d2))

	d1 = max(x[i]-xmin, ymax-y[i])
	d2 = max(xmax-x[i], y[i]-ymin)
	ans2 = max(ans2, min(d1, d2))
print(min(ans1, ans2))