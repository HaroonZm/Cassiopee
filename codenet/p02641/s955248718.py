X, N = tuple(map(int, input().split()))
P = list(map(int, input().split()))

for i in range(100):
	for j in [-1, 1]:
		t = X + i * j
		if t not in P:
			print(t)
			exit(0)