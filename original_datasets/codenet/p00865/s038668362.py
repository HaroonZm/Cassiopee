while 1:
	n,m,k = map(int,raw_input().split(" "))
	if n == m == k == 0: break
	dice = [[0 for _ in range(m * n)] for _ in range(n)]
	for i in range(m):
		dice[0][i] = 1
	for i in range(n-1):
		for j in range(m * n):
			if dice[i][j] == 0: continue
			for l in range(1,m+1):
				dice[i+1][j+l] += dice[i][j]
	print sum([(i+1-k if i+1-k > 1 else 1) * dice[n-1][i] for i in range((1*n-1),m*n)])/(m**n*1.)