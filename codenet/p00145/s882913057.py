# AOJ 0145 Cards
# Python3 2018.6.18 bal4u
#　動的計画法　（行列の積に類似）

INF = 0x7fffffff

n = int(input())
c = [[INF for j in range(n)] for i in range(n)]
a = [[0 for j in range(2)] for i in range(n)]

for i in range(n): c[i][i] = 0
for i in range(n): a[i][0], a[i][1] = list(map(int, input().split()))

for l in range(1, n):
	for i in range(n-l):
		j = i + l
		for k in range(i, j):
			c[i][j] = min(c[i][j], c[i][k] +a[i][0]*a[k][1]*a[k+1][0]*a[j][1] +c[k+1][j])

print(c[0][n-1])