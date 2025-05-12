# AOJ 1587: Plants
# Python3 2018.7.13 bal4u

hi = [[0 for j in range(51)] for i in range(51)]
W, H, T = map(int, input().split())
P = int(input())
for i in range(P):
	x, y, t = map(int, input().split())
	hi[x][y] += 1
ans = 0;
for y in range(H):
	v = list(map(int, input().split()))
	for x in range(W):
		if v[x]: ans += hi[x][y]
print(ans)