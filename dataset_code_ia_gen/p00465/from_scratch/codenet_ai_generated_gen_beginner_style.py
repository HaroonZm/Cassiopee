import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def bfs(W, H, X, Y, levels, auth):
    if auth == 0:
        return 0
    visited = [[False]*W for _ in range(H)]
    queue = deque()
    x0, y0 = X-1, Y-1
    if levels[y0][x0] > auth:
        return 0
    visited[y0][x0] = True
    queue.append((x0, y0))
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<W and 0<=ny<H and not visited[ny][nx]:
                if levels[ny][nx] <= auth:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    count += 1
    return count

while True:
    R = int(sys.stdin.readline())
    if R == 0:
        break

    W1,H1,X1,Y1 = map(int, sys.stdin.readline().split())
    levels1 = [list(map(int, sys.stdin.readline().split())) for _ in range(H1)]
    W2,H2,X2,Y2 = map(int, sys.stdin.readline().split())
    levels2 = [list(map(int, sys.stdin.readline().split())) for _ in range(H2)]

    # 認証レベルは0以上最大は部屋の最大の機密レベルの最大値の合計を上限とする
    max_level1 = max(max(row) for row in levels1)
    max_level2 = max(max(row) for row in levels2)
    max_auth_sum = max_level1 + max_level2

    ans = None
    for auth_sum in range(max_auth_sum+1):
        found = False
        # 事務所1の認証レベルは0からauth_sumまで試す
        for auth1 in range(auth_sum+1):
            auth2 = auth_sum - auth1
            c1 = bfs(W1,H1,X1,Y1,levels1,auth1)
            c2 = bfs(W2,H2,X2,Y2,levels2,auth2)
            if c1 + c2 >= R:
                ans = auth_sum
                found = True
                break
        if found:
            print(ans)
            break