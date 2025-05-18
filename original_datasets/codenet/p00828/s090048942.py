dx = [1,0,0,1, 1,1, 1,0, 0,1,-1, 1, 1]
dy = [0,1,0,1,-1,0, 0,1, 1,1, 1,-1, 1]
dz = [0,0,1,0, 0,1,-1,1,-1,1, 1, 1,-1]

def judge(B,x,y,z,color):
    for i in range(13):
        seq = B[z][y][x]
        nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
        while 0 <= min(nx,ny,nz) and max(nx,ny,nz) < n:
            seq += B[nz][ny][nx]
            nx += dx[i]; ny += dy[i]; nz += dz[i]
        nx,ny,nz = x-dx[i],y-dy[i],z-dz[i]
        while 0 <= min(nx,ny,nz) and max(nx,ny,nz) < n:
            seq = B[nz][ny][nx] + seq
            nx -= dx[i]; ny -= dy[i]; nz -= dz[i]
        if str(color)*m in seq: return True
    return False
    
while 1:
    n,m,p = map(int,raw_input().split())
    if n == 0: break
    B = [[["-"]*n for i in range(n)] for j in range(n)]
    isWin = False
    for move in xrange(p):
        x,y = map(int,raw_input().split())
        if isWin: continue

        x -= 1; y -= 1
        color = move%2
        for z in range(n):
            if B[z][y][x] == "-":
                B[z][y][x] = str(color)
                isWin = judge(B,x,y,z,color)
                break
        
        if isWin: print ["Black","White"][color],move+1
    if not isWin:
        print "Draw"