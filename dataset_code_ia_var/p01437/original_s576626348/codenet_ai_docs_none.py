dxy = zip([1,0,-1,0],[0,1,0,-1])
while 1:
    H,W,L = map(int,raw_input().split())
    if H == 0: break
    c = [raw_input() for i in xrange(H)]
    for h in xrange(H):
        for w in xrange(W):
            if c[h][w] in "ESWN":
                x,y = w,h
                d = "ESWN".index(c[h][w])
    visited = [[[-1]*4 for i in xrange(W)] for j in xrange(H)]
    visited[y][x][d] = 0
    step = 0
    inloop = False
    while L:
        dx,dy = dxy[d]
        nx,ny = x+dx,y+dy
        if not (0 <= nx < W and 0 <= ny < H and c[ny][nx] != "#"):
            d = (d+1)%4
        else:
            x,y = nx,ny
            step += 1
            L -= 1
        if visited[y][x][d] > -1 and not inloop:
            L %= step-visited[y][x][d]
            L += step-visited[y][x][d]
            inloop = True
        visited[y][x][d] = step
    print y+1,x+1,"ESWN"[d]