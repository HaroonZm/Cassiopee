N = int(input())
A = list(map(int, input().split()))

for n in range(N, 0, -1):
	tmp = len([i for i in A if i>=n])
	if n<=tmp:
		print(n)
		break