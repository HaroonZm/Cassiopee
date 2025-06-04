from bisect import bisect_left

while True:
	n, m, w, h, S = map(int, input().split())
	if n == 0: break
	m, wh2 = m+1, 2*(w*h)
	S = wh2-2*S
	tbl, s = [[0,0,0]], [0]
	for i in range(1, m):
		l, r = map(int, input().split())
		tbl.append([l, r, r-l])
		s.append((l+r)*w)
	p = []
	for i in range(n):
		x, y = map(float, input().split())
		p.append((y, x))
	if S == 0:
		print(n)
		continue
	elif S == wh2:
		print(0)
		continue
	p.sort()
	j, a = 1, [0]*m
	for i in range(n):
		y, x = p[i]
		while True:
			y1 = tbl[j-1][2]*x/w + tbl[j-1][0]
			y2 = tbl[j  ][2]*x/w + tbl[j  ][0]
			if y1 < y:
				if y < y2: break
				j += 1
			else: j -= 1
		a[j] += 1
	for i in range(1, m): a[i] += a[i-1]
	j = bisect_left(s, S, 0, m)
	if s[j] != S: j -= 1
	ans, i = a[j], 1
	while j+1 < m:
		j += 1
		while s[j]-s[i] > S: i += 1
		ans = max(ans, a[j]-a[i])
	print(n - ans)