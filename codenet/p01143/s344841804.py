while True:
	n, m, p = map(int, input().split())
	if (n, m, p) == (0, 0, 0):
		break
	x = [int(input()) for i in range(n)]
	if x[m-1] == 0:
		print(0)
	else:
		print(int(sum(x) * (100-p) / x[m-1]))