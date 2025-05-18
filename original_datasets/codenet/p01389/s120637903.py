H,W = map(int,raw_input().split())
M = [[500]*(W+1)]+[[500]+map(int,list(raw_input())) for i in range(H)]
M[0][1] = 0
for h in range(1,H+1):
	for w in range(1,W+1):
		M[h][w] += min(M[h-1][w],M[h][w-1])
print M[H][W]