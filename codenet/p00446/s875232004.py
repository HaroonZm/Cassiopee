# AOJ 0523: Card GameI
# Python3 2018.6.30 bal4u

while True:
	n = int(input())
	if n == 0: break
	c = [1] * (2*n+1)
	for i in range(1, n+1): c[int(input())] = 0
	m = [n]*2
	t, ba = 0, 0
	while m[0] > 0 and m[1] > 0:
		f = 1
		for i in range(ba+1, 2*n+1):
			if t == c[i]:
				ba = i
				c[i] = 2
				m[t] -= 1
				f = 0
				break
			if i == 2*n: ba = 0
		if f: ba = 0
		t = 1-t
	print(m[1], m[0], sep='\n')