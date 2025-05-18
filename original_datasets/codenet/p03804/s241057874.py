N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

l = 0
while l <= len(A[0]) - len(B[0]):
	for i in range(N - M + 1):
		s = A[i][l:]
		if not B[0] in s:
			continue
		if 0 == s.index(B[0]):
			for m in range(1, M):
				if not B[m] in A[i + m][l:]:
					break
				if 0 != A[i + m][l:].index(B[m]):
					break
			else:
				print("Yes")
				exit()
	l += 1
print("No")