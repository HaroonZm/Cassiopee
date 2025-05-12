# AOJ ITP2_8_D: Multi-Map
# Python3 2018.6.24 bal4u

import bisect
from bisect import bisect_left, bisect_right, insort_left
dict = {}
keytbl = []
q = int(input())
for i in range(q):
	a = list(input().split())
	ki = a[1]
	if a[0] == '0':
		if ki not in dict:
			dict[ki] = []
			insort_left(keytbl, ki)
		dict[ki].append(int(a[2]))
	elif a[0] == '1' and ki in dict and dict[ki] != []: print(*dict[ki], sep='\n')
	elif a[0] == '2' and ki in dict: dict[ki] = []
	elif a[0] == '3':
		L = bisect_left (keytbl, a[1])
		R = bisect_right(keytbl, a[2])
		for j in range(L, R):
			for k in dict[keytbl[j]]:
				print(keytbl[j], k)