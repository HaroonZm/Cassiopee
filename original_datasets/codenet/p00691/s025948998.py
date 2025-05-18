# AOJ 1109: Fermat's Last Theorem
# Python3 2018.7.14 bal4u

from bisect import bisect_left

tbl = [i**3 for i in range(1111)]
while True:
	z = int(input())
	if z == 0: break
	ma = 0
	for x in range(z-1, 0, -1):
		y = bisect_left(tbl, tbl[z]-tbl[x])-1
		if tbl[y] > tbl[x]: break
		ma = max(ma, tbl[x]+tbl[y])
	print(tbl[z]-ma)