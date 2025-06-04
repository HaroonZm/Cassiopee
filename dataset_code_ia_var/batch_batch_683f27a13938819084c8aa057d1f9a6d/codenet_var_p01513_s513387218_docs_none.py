while True:
	n = int(input())
	if n == 0:
		break
	m = []
	for i in range(n):
		m.append(set(list(map(int, input().split()))[1:]))
	k = set(list(map(int, input().split()))[1:])
	f = [i+1 for i in range(n) if k <= m[i]]
	if len(f) == 1:
		print(f[0])
	else:
		print(-1)