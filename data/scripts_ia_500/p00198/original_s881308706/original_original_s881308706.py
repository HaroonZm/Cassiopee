# AOJ 0198 Trouble in Shinagawa's Artifacts
# Python3 2018.6.20 bal4u

r = [ \
	[0,1,2,3,4,5,6], [0,1,3,5,2,4,6], [0,1,4,2,5,3,6], [0,1,5,4,3,2,6], \
	[0,2,6,3,4,1,5], [0,2,3,1,6,4,5], [0,2,1,4,3,6,5], [0,2,4,6,1,3,5], \
	[0,3,1,2,5,6,4], [0,3,2,6,1,5,4], [0,3,5,1,6,2,4], [0,3,6,5,2,1,4], \
	[0,4,1,5,2,6,3], [0,4,2,1,6,5,3], [0,4,5,6,1,2,3], [0,4,6,2,5,1,3], \
	[0,5,1,3,4,6,2], [0,5,3,6,1,4,2], [0,5,4,1,6,3,2], [0,5,6,4,3,1,2], \
	[0,6,2,4,3,5,1], [0,6,3,2,5,4,1], [0,6,5,3,4,2,1], [0,6,4,5,2,3,1]]

def same(x, y):
	t = ['']*7
	for i in range(24):
		for j in range(1, 7): t[j] = a[y][r[i][j]]
		if a[x] == t: return True
	return False

while True:
	n = int(input())
	if n == 0: break
	f = [0]*n
	a = [['' for j in range(7)] for i in range(n)]
	for i in range(n):
		s = list(input().split())
		for j in range(6): a[i][j+1] = s[j]
	for i in range(n):
		if f[i] == 1: continue
		for j in range(i+1, n):
			if same(i, j): f[j] = 1
	print(sum(f))