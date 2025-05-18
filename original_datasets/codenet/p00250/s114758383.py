# AOJ 0254: Scone
# Python3 2018.6.25 bal4u

s = [0 for i in range(30001)]
while True:
	n, m = map(int, input().split())
	if n == 0: break
	f = [-1 for i in range(m)]
	sum, nmax, ans = 0, 0, 0
	a = list(map(int, input().split()))
	for i in range(n):
		sum += a[i]
		a[i] %= m
		if a[i] > nmax: nmax = a[i]
		if a[i] == m-1: ans = a[i]
		s[i+1] = s[i] + a[i]
		if s[i+1] >= m: s[i+1] -= m
		f[s[i+1]] = i+1
	if ans == 0:
		if nmax == 0: ans = 0
		elif sum < m: ans = sum
		else:
			done = False
			for ans in range(m-1, nmax-1, -1):
				for i in range(n+1):
					x = s[i]+ans
					if x >= m: x -= m
					if f[x] >= i:
						done = True
						break
				if done: break
	print(ans)