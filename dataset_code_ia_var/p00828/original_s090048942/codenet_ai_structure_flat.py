dx = [1,0,0,1,1,1,1,0,0,1,-1,1,1]
dy = [0,1,0,1,-1,0,0,1,1,1,1,-1,1]
dz = [0,0,1,0,0,1,-1,1,-1,1,1,1,-1]

while 1:
    nmp = raw_input().split()
    n = int(nmp[0])
    m = int(nmp[1])
    p = int(nmp[2])
    if n == 0: break
    B = []
    for j in range(n):
        B.append([])
        for i in range(n):
            B[j].append(["-"]*n)
    isWin = False
    move = 0
    while move < p:
        xy = raw_input().split()
        x = int(xy[0]) - 1
        y = int(xy[1]) - 1
        if isWin:
            move += 1
            continue
        color = move % 2
        placed = False
        for z in range(n):
            if B[z][y][x] == "-":
                B[z][y][x] = str(color)
                for i in range(13):
                    seq = B[z][y][x]
                    nx = x + dx[i]
                    ny = y + dy[i]
                    nz = z + dz[i]
                    while 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
                        seq += B[nz][ny][nx]
                        nx += dx[i]
                        ny += dy[i]
                        nz += dz[i]
                    nx = x - dx[i]
                    ny = y - dy[i]
                    nz = z - dz[i]
                    while 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
                        seq = B[nz][ny][nx] + seq
                        nx -= dx[i]
                        ny -= dy[i]
                        nz -= dz[i]
                    if str(color) * m in seq:
                        isWin = True
                        break
                placed = True
                break
        if isWin:
            print ["Black", "White"][color], move + 1
        move += 1
    if not isWin:
        print "Draw"