while True:
    W,H = map(int,input().split())
    if W == 0:
        break
    tx,ty = map(int,input().split())
    kx,ky = map(int,input().split())
    ma = [[False]*(W+2) for _ in range(H+2)]
    for i in range(1,H+1):
        row = input().split()
        for j in range(1,W+1):
            ma[i][j] = bool(1 - int(row[j-1]))
    from collections import deque
    que = deque()
    que.append([tx,ty,kx,ky,0])
    pas = set()
    ans = "NA"
    while que:
        tx,ty,kx,ky,c = que.popleft()
        if c > 100:
            break
        if tx == kx and ty == ky:
            ans = c
            break
        for dx,dy in [[-1,0],[0,-1],[1,0],[0,1]]:
            tdx,tdy = (dx,dy) if ma[ty+dy][tx+dx] else (0,0)
            kdx,kdy = (-dx,-dy) if ma[ky - dy][kx - dx] else (0,0)
            pos = (tx+tdx, ty+tdy, kx+kdx, ky+kdy)
            if pos in pas:
                continue
            que.append([tx+tdx, ty+tdy, kx+kdx, ky+kdy, c+1])
            pas.add(pos)
    print(ans)