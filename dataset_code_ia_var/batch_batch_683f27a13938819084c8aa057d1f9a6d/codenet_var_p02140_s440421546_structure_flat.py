from collections import deque
R,C,ay,ax,by,bx = map(int,input().split())
MOD = INF = 10**9+7
dists = [[INF]*C for _ in range(R)]
ptns = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        dists[i][j] = INF
        ptns[i][j] = 0
dists[ay][ax] = 0
ptns[ay][ax] = 1
q = deque()
q.append((0,ax,ay))
dxs = [1,0,-1,0]
dys = [0,1,0,-1]
ans_d = None
while q:
    item = q.popleft()
    d = item[0]
    x = item[1]
    y = item[2]
    if ans_d is not None and d > ans_d:
        break
    if x == bx and y == by:
        ans_d = d
    if d > dists[y][x]:
        continue
    dists[y][x] = d
    for i in range(4):
        dx = dxs[i]
        dy = dys[i]
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            continue
        if d+1 > dists[ny][nx]:
            continue
        if dists[ny][nx] == INF:
            q.append((d+1,nx,ny))
            dists[ny][nx] = d+1
        ptns[ny][nx] += ptns[y][x]
        if ptns[ny][nx] >= MOD:
            ptns[ny][nx] %= MOD
    if d+1 <= dists[0][x]:
        if dists[0][x] == INF:
            q.append((d+1,x,0))
            dists[0][x] = d+1
        ptns[0][x] += ptns[y][x]
        if ptns[0][x] >= MOD:
            ptns[0][x] %= MOD
    if d+1 <= dists[R-1][x]:
        if dists[R-1][x] == INF:
            q.append((d+1,x,R-1))
            dists[R-1][x] = d+1
        ptns[R-1][x] += ptns[y][x]
        if ptns[R-1][x] >= MOD:
            ptns[R-1][x] %= MOD
    if d+1 <= dists[y][0]:
        if dists[y][0] == INF:
            q.append((d+1,0,y))
            dists[y][0] = d+1
        ptns[y][0] += ptns[y][x]
        if ptns[y][0] >= MOD:
            ptns[y][0] %= MOD
    if d+1 <= dists[y][C-1]:
        if dists[y][C-1] == INF:
            q.append((d+1,C-1,y))
            dists[y][C-1] = d+1
        ptns[y][C-1] += ptns[y][x]
        if ptns[y][C-1] >= MOD:
            ptns[y][C-1] %= MOD
print(ans_d, ptns[by][bx]%MOD)