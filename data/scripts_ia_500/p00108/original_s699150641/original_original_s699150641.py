# AOJ 0108 Operation of Frequency of Appearance
# Python3 2018.6.18 bal4u

f = [0]*105
a = [[0 for j in range(15)] for i in range(2)]
while True:
	n = int(input())
	if n == 0: break
	a[0] = list(map(int, input().split()))
	a[1] = [0]*n
	cnt = k1 = 0
	while True:
		for i in range(n): f[a[k1][i]] += 1
		k2 = 1-k1
		for i in range(n): a[k2][i] = f[a[k1][i]]
		for i in range(n): f[a[k1][i]] = 0
		if a[0] == a[1]: break
		k1 = k2
		cnt += 1
	print(cnt)
	print(*a[0])