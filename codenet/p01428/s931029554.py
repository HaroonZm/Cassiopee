dxy = zip([1,1,0,-1,-1,-1,0,1],[0,1,1,1,0,-1,-1,-1])
A = [list(raw_input()) for i in xrange(8)]
for i in xrange(64):
    hand = ["o","x"][i%2]
    d = [1,-1][i%2]
    mx,nd = 0,[]
    for y in range(8)[::d]:
        for x in range(8)[::d]:
            if A[y][x] == ".":
                tmp,td = 0,[]
                for dx,dy in dxy:
                    nx,ny = x+dx,y+dy
                    while 0 <= min(nx,ny) and max(nx,ny) < 8:
                        if   A[ny][nx] == hand:
                            get = max(abs(nx-x),abs(ny-y))-1
                            if get > 0:
                                tmp += get
                                td.append([dx,dy])
                            break
                        elif A[ny][nx] == ".":
                            break
                        nx += dx; ny += dy
                if tmp > mx:
                    mx,nd = tmp,td
                    px,py = x,y
    if mx == 0: continue
    A[py][px] = hand
    for dx,dy in nd:
        nx,ny = px+dx,py+dy
        while 0 <= min(nx,ny) and max(nx,ny) < 8:
            if A[ny][nx] == hand: break
            A[ny][nx] = hand
            nx += dx; ny += dy
for a in A:
    print "".join(a)