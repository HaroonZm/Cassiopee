W = H = 5
m = input()
for r in range(m):
	M = [map(int,raw_input().split()) for i in range(H)]
	A = [[0]*W for i in range(H)]
	B = [[0]*W for i in range(H)]
	ans = 1
	for h in range(H):
		L = 0
		for w in range(W):
			if M[h][w] == 1:
				L += 1
			else:
				L = 0
			A[h][w] = L
			B[h][w] = (B[h-1][w] if h > 0 else 0) + 1 if L > 0 else 0
			if L*B[h][w] > ans:
				a = L
				for hi in range(B[h][w]):
					a = min(a,A[h-hi][w])
					if a*B[h][w] <= ans:
						break
					ans = max(ans,a*(hi+1))
	print ans
	if r != m-1: raw_input()