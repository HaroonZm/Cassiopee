H,W = map(int,raw_input().split())
M = [map(int,list(raw_input())) for i in range(H)]
M.insert(0,[0]+[500]*(W-1))
for h in range(1,H+1):
	M[h][0] += M[h-1][0]
	for w in range(1,W):
		M[h][w] += min(M[h-1][w],M[h][w-1])
print M[H][W-1]