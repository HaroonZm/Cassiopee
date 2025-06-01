def f(a):
	from itertools import groupby
	return ''.join(f"{sum(1 for _ in g)}{k}" for k, g in groupby(a))

while True:
	n = int(input())
	if n == 0: break
	a = input()
	for _ in range(n):
		a = f(a)
	print(a)