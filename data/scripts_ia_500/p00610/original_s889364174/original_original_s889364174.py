# AOJ 1024 Cleaning Robot 2.0
# Python3 2018.7.5 bal4u

mv = ((-1,0), (0,1), (1,0), (0,-1))
d2c = {0:'.', 1:'E'}

while True:
	n, k = map(int, input().split())
	if n == 0: break
	k, n1 = k-1, n-1
	if (n & 1) or k >= (1<<(n>>1)):
		print("No\n")
		continue
	arr = [[-1 for c in range(n)] for r in range(n)]
	for c in range(n): arr[0][c] = (k>>((n1-c)>>1)) & 1
	for r in range(n1):
		for c in range(n):
			f, t = 0, arr[r][c]
			for i in range(4):
				nr, nc = r + mv[i][0], c + mv[i][1]
				if nr >= 0 and nr < n and nc >= 0 and nc < n and arr[nr][nc] == t: f += 1
			arr[r+1][c] = 1-t if f==2 else t
	for r in range(n): print(''.join([d2c[arr[r][c]] for c in range(n)]))
	print()