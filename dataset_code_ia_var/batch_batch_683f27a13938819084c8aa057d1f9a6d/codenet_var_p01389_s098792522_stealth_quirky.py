H,W=[int(x)for x in raw_input().split()]
world=[map(int,list(raw_input()))for _ in[0]*H]
world = [[None]+[5e2]*(W-1)]+world
for r in xrange(1,1+H):
	world[r][0]+=world[r-1][0] or 0
	for c in xrange(1,W):
		world[r][c]+=(world[r][c-1],world[r-1][c])[world[r][c-1]>world[r-1][c]]
print world[H][W-1]