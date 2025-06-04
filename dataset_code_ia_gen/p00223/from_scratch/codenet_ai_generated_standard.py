from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def opposite_dir(d):
    return (d + 2) % 4

while True:
    W,H = map(int,input().split())
    if W == 0 and H == 0:
        break
    tx, ty = map(int,input().split())
    kx, ky = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(H)]

    # Convert to zero-based indices
    tx -= 1
    ty -= 1
    kx -= 1
    ky -= 1

    visited = [[[[False]*W for _ in range(H)] for __ in range(W)] for ___ in range(H)]
    visited[ty][tx][ky][kx] = True
    queue = deque()
    queue.append((tx, ty, kx, ky, 0))
    ans = "NA"

    while queue:
        tx, ty, kx, ky, t = queue.popleft()
        if t >= 100:
            break
        for d in range(4):
            ntx = tx + dx[d]
            nty = ty + dy[d]
            nd = opposite_dir(d)
            nkx = kx + dx[nd]
            nky = ky + dy[nd]

            # Check Takayuki
            if not (0 <= ntx < W and 0 <= nty < H) or grid[nty][ntx] == 1:
                ntx, nty = tx, ty
            # Check Kazuyuki
            if not (0 <= nkx < W and 0 <= nky < H) or grid[nky][nkx] == 1:
                nkx, nky = kx, ky

            # If they meet after move
            if ntx == nkx and nty == nky:
                ans = t+1
                queue.clear()
                break

            if not visited[nty][ntx][nky][nkx]:
                visited[nty][ntx][nky][nkx] = True
                queue.append((ntx, nty, nkx, nky, t+1))
    print(ans)