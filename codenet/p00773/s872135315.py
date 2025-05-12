def tax(p, x):
	return p * (100 + x) // 100

while True:
	x, y, s = map(int, input().split())
	if x == y == s == 0:
		break
	m = 0
	for i in range(1, s):
		for j in range(1, s):
			t = tax(i, x) + tax(j, x)
			if t > s:
				break
			if (t) == s:
				m = max(m, tax(i, y) + tax(j, y))
	print(m)