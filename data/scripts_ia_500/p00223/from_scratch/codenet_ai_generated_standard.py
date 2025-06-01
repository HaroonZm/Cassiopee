from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def opposite_dir(d):
    # 0:E->W(1),1:W->E(0),2:S->N(3),3:N->S(2)
    return [1,0,3,2][d]

while True:
    W,H = map(int,input().split())
    if W==0 and H==0:
        break
    tx,ty = map(int,input().split())
    kx,ky = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(H)]
    # Positions are 1-based to 0-based
    tx -= 1
    ty -= 1
    kx -= 1
    ky -= 1

    visited = [[[[False]*W for _ in range(H)] for __ in range(W)] for ___ in range(H)]
    queue = deque()
    queue.append((tx,ty,kx,ky,0))
    visited[ty][tx][ky][kx]=True
    ans = "NA"

    while queue:
        t_x,t_y,k_x,k_y,time = queue.popleft()
        if time>=100:
            break
        for d in range(4):
            nt_x = t_x + dx[d]
            nt_y = t_y + dy[d]
            opp = opposite_dir(d)
            nk_x = k_x + dx[opp]
            nk_y = k_y + dy[opp]
            # Check if moves are valid
            t_ok = 0<=nt_x<W and 0<=nt_y<H and grid[nt_y][nt_x]==0
            k_ok = 0<=nk_x<W and 0<=nk_y<H and grid[nk_y][nk_x]==0
            
            # Apply rules if one is invalid, that one stays
            if not t_ok and k_ok:
                nt_x, nt_y = t_x, t_y
            elif t_ok and not k_ok:
                nk_x, nk_y = k_x, k_y
            elif not t_ok and not k_ok:
                nt_x, nt_y = t_x, t_y
                nk_x, nk_y = k_x, k_y

            if nt_x == nk_x and nt_y == nk_y:
                ans = time+1
                queue.clear()
                break

            if not visited[nt_y][nt_x][nk_y][nk_x]:
                visited[nt_y][nt_x][nk_y][nk_x]=True
                queue.append((nt_x,nt_y,nk_x,nk_y,time+1))

    print(ans)