# AOJ 1020: Cleaning Robot
# Python3 2018.7.5 bal4u

mv = ((-1,0),(0,1),(1,0),(0,-1))
while True:
	n = int(input())
	if n == 0: break
	t1, t2, t3 = input().split()
	s, t, b = ord(t1)-ord('A'), ord(t2)-ord('A'), ord(t3)-ord('A')
	f = [[[0.0 for a in range(3)] for c in range(3)] for r in range(17)]
	f[0][s//3][s%3] = 1
	for j in range(1, n+1):
		for r in range(3):
			for c in range(3):
				for i in range(4):
					r2, c2 = r + mv[i][0], c + mv[i][1]
					if r2 < 0 or r2 >= 3 or c2 < 0 or c2 >= 3 or 3*r2+c2 == b:
						r2, c2 = r, c
					f[j][r2][c2] += f[j-1][r][c]/4
	print(f[n][t//3][t%3])