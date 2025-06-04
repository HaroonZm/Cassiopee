import sys
sys.setrecursionlimit(10**7)

W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# 外周の0も含めて探索したいので、1マス外側に拡張
visited = [[False]*(W+2) for _ in range(H+2)]
map_ext = [[0]*(W+2) for _ in range(H+2)]
for y in range(H):
    for x in range(W):
        map_ext[y+1][x+1] = grid[y][x]

# 偶数行奇数行で接続関係が変わるため、(x,y)は1-originで扱う
# y 奇数の時の6方向の相対座標
directions_odd = [(+1,0), (0,+1), (-1,+1), (-1,0), (-1,-1), (0,-1)]
# y 偶数の時の6方向の相対座標
directions_even = [(+1,0), (+1,+1), (0,+1), (-1,0), (0,-1), (+1,-1)]

def inbound(x,y):
    return 0 <= x < W+2 and 0 <= y < H+2

def neighbors(x,y):
    if y % 2 == 1:
        for dx, dy in directions_odd:
            nx, ny = x+dx, y+dy
            if inbound(nx, ny):
                yield nx, ny
    else:
        for dx, dy in directions_even:
            nx, ny = x+dx, y+dy
            if inbound(nx, ny):
                yield nx, ny

# 外から内部の空きスペースに入るため0マスの部分をDFSで訪問する
def dfs(x,y):
    visited[y][x] = True
    for nx, ny in neighbors(x,y):
        if not visited[ny][nx] and map_ext[ny][nx] == 0:
            dfs(nx, ny)

# 外周0マスからDFS開始
for x in range(W+2):
    if not visited[0][x] and map_ext[0][x] == 0:
        dfs(x, 0)
    if not visited[H+1][x] and map_ext[H+1][x] == 0:
        dfs(x, H+1)
for y in range(H+2):
    if not visited[y][0] and map_ext[y][0] == 0:
        dfs(0, y)
    if not visited[y][W+1] and map_ext[y][W+1] == 0:
        dfs(W+1, y)

ans = 0
for y in range(1, H+1):
    for x in range(1, W+1):
        if map_ext[y][x] == 1:
            # 壁があるマス
            # 隣が外(visited==Trueかつ内部0)ならその壁面はイルミネーション対象
            if y % 2 == 1:
                dir_list = directions_odd
            else:
                dir_list = directions_even
            for dx, dy in dir_list:
                nx, ny = x+dx, y+dy
                if inbound(nx, ny):
                    if map_ext[ny][nx] == 0 and visited[ny][nx]:
                        ans += 1

print(ans)