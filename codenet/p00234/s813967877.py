import queue

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
    w,h = map(int,input().split())
    if w == 0:
        break
    f, m, o = map(int,input().split())
    c = [list(map(int,input().split())) for _ in range(h)]
    d = [[[1e9]*w for x in range(h)] for y in range(m+1)]

    que = queue.PriorityQueue()
    for j in range(w):
        d[o-1][0][j] = -min(0,c[0][j])
        que.put((-min(0,c[0][j]),o-1,0,j))

    while not que.empty():
        p = que.get()
        ox = p[1]
        i = p[2]
        j = p[3]
        if d[ox][i][j] < p[0] or ox <= 1:
            continue
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if ni<0 or ni>=h or nj<0 or nj>=w:
                continue
            if c[ni][nj] < 0:
                if d[ox-1][ni][nj] > d[ox][i][j] - c[ni][nj]:
                    d[ox-1][ni][nj] = d[ox][i][j] - c[ni][nj]
                    que.put((d[ox-1][ni][nj],ox-1,ni,nj))
            else:
                nox = min(ox-1+c[ni][nj],m)
                if d[nox][ni][nj] > d[ox][i][j]:
                    d[nox][ni][nj] = d[ox][i][j]+0
                    que.put((d[nox][ni][nj],nox,ni,nj))
    ans = 1e9
    for j in range(w):
        for ox in range(1,m+1):
            ans = min(ans, d[ox][h-1][j])
    if ans <= f:
        print(ans)
    else:
        print('NA')