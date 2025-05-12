N, K = map(int, input().split())
A = N - K + 1
for i in range(1, K+1):
	if i > N - K + 1: print(0)
	else:
		print(A%1000000007)
		A *= (K-i)*(N-K+1-i)
		A //= i*(i+1)