import sys
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return list(map(int, input().split()))
def MAP(): return map(int, input().split())

ans = []
while 1:
	n = INT()
	if n == 0:
		break
	a = LIST()
	a.sort()
	min_ = 100000000
	for i in range(n-1):
		min_ = min(min_, abs(a[i] - a[i+1]))
	ans.append(min_)
for x in ans:
	print(x)