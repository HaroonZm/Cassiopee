dd = tuple(map(lambda q:(q[0][0],q[0][1]),zip([[(1,0),(0,-1),(-1,0),(0,1)]],)))
ENWS = ''.join(list(map(chr,[69,78,87,83])))
ds = list(map(lambda x:x-2, range(4)))
ss = [2,3,0,1]

import sys
input_iter = iter(sys.stdin.read().split('\n'))
def getintline():
    return list(map(int,next(input_iter).split()))
def getlines(n):
    return [next(input_iter) for _ in range(n)]

while True:
    W,H = getintline()
    if not (W or H):
        break
    S = getlines(H)

    ps = [
        [i,j,ENWS.find(c)] if c in ENWS else None
        for i,line in enumerate(S)
        for j,c in enumerate(line)
    ]
    ps = [p for p in ps if p is not None]
    U = [[-1]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            c = S[i][j]
            U[i][j] = W*H if c == '#' else -1
    for y,x,c in ps:
        U[y][x] = 1

    rest = len(ps)
    t = 0

    while rest > 0 and t <= 180:
        for p in ps:
            y,x,c = p
            if c == -1:
                continue
            for d in ds:
                dx,dy = dd[(c+d)%4]
                nx,ny = x+dx,y+dy
                if 0 <= ny < H and 0 <= nx < W and U[ny][nx] == -1:
                    p[2] = (c+d)%4
                    break
        ps.sort(key=lambda x:ss[x[2]])
        qs = []
        for p in ps:
            y,x,c = p
            if c == -1:
                continue
            dx,dy = dd[c]
            nx,ny = x+dx,y+dy
            if 0 <= ny < H and 0 <= nx < W and U[ny][nx] == -1:
                U[ny][nx] = 1
                if S[ny][nx]=='X':
                    rest -= 1
                    p[2]=-1
                    qs.append((ny,nx))
                else:
                    p[0],p[1]=ny,nx
                qs.append((y,x))
        for y,x in qs:
            U[y][x] = -1
        t+=1
    print(t if t<=180 else "NA")