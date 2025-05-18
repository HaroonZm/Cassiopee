# AOJ 0160 Delivery Fee
# Python3 2018.6.18 bal4u

tbl = [ 600, 800, 1000, 1200, 1400, 1600 ]

while True:
	n = int(input())
	if n == 0: break
	fee = 0
	for i in range(n):
		x, y, h, w = list(map(int, input().split()))
		s = x+y+h
		if s <= 160 and w <= 25:
			k1 = k2 = 0
			if s <= 60: k1 = 0
			else: k1 = (s-61)//20 + 1
			if w <= 2: k2 = 0;
			else: k2 = (w-1)//5 + 1
			if k1 < k2: k1 = k2
			fee += tbl[k1]
	print(fee)